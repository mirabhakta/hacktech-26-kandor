# Kandor Deployment Guide

## Local demonstration

1. Create a virtual environment and install backend dependencies:

```powershell
cd Backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

2. Start the backend:

```powershell
python main.py
```

Health check: `http://127.0.0.1:8000/health`

3. Load the unpacked extension:

- Open `chrome://extensions`
- Enable Developer mode
- Click "Load unpacked"
- Select the `Frontend` directory

4. Open the demo:

- Visit `http://127.0.0.1:8000/demo`
- Kandor scans the synthetic conversation and shows an alert.
- Open the extension popup to see the current analysis status.

## Hosted demonstration

- Use the provided `Backend/Dockerfile`.
- Set environment variables from `Backend/.env.example`.
- Put the backend behind HTTPS (for example Render, Fly.io, Railway, or a VPS with Caddy).
- Update the extension's Backend base URL in the popup settings to the HTTPS endpoint.
- Restrict `KANDOR_ALLOWED_ORIGINS` to the hosted frontend origin and extension origins as appropriate.

## Environment variables

See `Backend/.env.example`.

## Recommended hosted deployment (Render free tier)

1. Push the repository to GitHub (with approval).
2. In Render, create a new Web Service from the repository.
3. Render will use `render.yaml`: root directory `Backend`, build `pip install -r requirements.txt`, start `python main.py`.
4. Set `KANDOR_ALLOWED_ORIGINS` to the public HTTPS URL and any local origins you need.
5. Keep provider keys unset for the deterministic demo, or add them only in Render's secret environment variables.
6. Verify `https://<service>.onrender.com/health`, `/demo`, and `/demo/console`.

Expected cost: Render free web service tier may sleep after inactivity; paid tier is optional.

## Known limitations:

- The default provider is `rules`, so AI providers are not required for demos.
- Browser/extension end-to-end testing was verified with Chromium and Playwright in this environment.
- Production use requires additional security, privacy, and detection-quality validation.