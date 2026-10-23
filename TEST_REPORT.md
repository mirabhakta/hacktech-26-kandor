# Kandor Test Report

## Commands executed

```powershell
.venv\Scripts\python.exe -m pytest tests/test_backend.py -q
node --check Frontend/background.js
node --check Frontend/content.js
node --check Frontend/popup.js
node tests/e2e_extension.mjs
```

## Results

- Backend tests: 12 passed.
- Frontend JavaScript syntax: passed.
- Playwright/Chromium extension E2E: passed (banner present, risk 100, fallback indicator shown).
- Instagram synthetic extraction fixture: passed (3 messages, sidebar excluded).
- Backend health check and demo routes: passed.
- Docker build: not verified (Docker daemon unavailable).

## Unverified

- Hosted HTTPS deployment was not performed (no deployment account/credentials).
- Real Instagram DOM extraction was not exercised against live Instagram in this environment.