# Kandor Implementation Plan

## Prioritized findings

1. Backend provider credentials were read from environment but K2/Gemini calls lacked configurable endpoints, timeouts, and validation.
2. Gemini failures could raise or return unstructured results; fallback was not consistently labeled.
3. Extension permissions were overly broad (`<all_urls>`).
4. Stored results included extracted raw messages.
5. Demo mode existed as backend HTML but lacked a clear fallback/demo indicator.
6. Missing automated tests and deployment artifacts.

## Implemented changes

- Configurable provider architecture via `KANDOR_PROVIDER`.
- Environment-based K2/Gemini endpoints, models, and timeouts.
- Schema validation and safe fallback handling.
- Restricted extension origins and content script matches.
- Minimized stored conversation data.
- Demo/fallback indicators in banner and popup.
- Automated backend tests and Playwright extension E2E test.
- Deployment artifacts: `.env.example`, Dockerfile, GitHub Actions, DEPLOYMENT.md.