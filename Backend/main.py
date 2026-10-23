import os
import time
from collections import defaultdict, deque

import fastapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn
from v1 import router as v1_router

app = fastapi.FastAPI(title="Kandor Backend", version="0.2.0")

ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "KANDOR_ALLOWED_ORIGINS",
        "http://localhost:8000,http://127.0.0.1:8000,http://localhost:5173,http://127.0.0.1:5173",
    ).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_origin_regex=os.getenv("KANDOR_ALLOWED_ORIGIN_REGEX", r"chrome-extension://.*"),
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

# Simple in-memory per-IP rate limiting (best-effort; use a real limiter for production).
RATE_LIMIT_PER_MINUTE = int(os.getenv("KANDOR_RATE_LIMIT_PER_MINUTE", "120"))
_rate_buckets: dict[str, deque] = defaultdict(deque)


@app.middleware("http")
async def rate_limit_and_size(request: fastapi.Request, call_next):
    client_host = request.client.host if request.client else "unknown"
    now = time.time()
    bucket = _rate_buckets[client_host]
    while bucket and now - bucket[0] > 60:
        bucket.popleft()
    if len(bucket) >= RATE_LIMIT_PER_MINUTE:
        return fastapi.responses.JSONResponse(
            status_code=429, content={"detail": "Rate limit exceeded"}
        )
    bucket.append(now)

    content_length = request.headers.get("content-length")
    max_bytes = int(os.getenv("KANDOR_MAX_REQUEST_BYTES", "2097152"))
    if content_length and content_length.isdigit() and int(content_length) > max_bytes:
        return fastapi.responses.JSONResponse(
            status_code=413, content={"detail": "Request body too large"}
        )
    return await call_next(request)


app.include_router(v1_router, prefix="/v1")


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "kandor-backend",
        "provider": os.getenv("KANDOR_PROVIDER", "auto"),
    }


@app.get("/demo", response_class=HTMLResponse)
async def demo():
    from demo_html import DEMO_HTML

    return DEMO_HTML


@app.get("/demo/console")
async def demo_console_redirect():
    from fastapi.responses import RedirectResponse

    return RedirectResponse(url="/demo", status_code=307)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("KANDOR_HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", os.getenv("KANDOR_PORT", "8000"))),
        reload=os.getenv("KANDOR_RELOAD", "false").lower() == "true",
    )