# Samadhan Sathi

**AI-assisted civic grievance prototype for Gwalior, Madhya Pradesh.**

Samadhan Sathi is an independent civic-tech demo for submitting and tracking civic issues and reviewing simulated complaint workflows.

> **Prototype notice:** This is not an official government or Municipal Corporation service. Seeded records are simulated. Do not enter sensitive or real personal information.

## Quick start

The original self-contained browser app is stored as a compact gzip/Base64 bundle in `source/` so it can be published reliably through GitHub's text-file API. Restore the normal, editable HTML before local development:

```bash
python tools/build.py --output dist/index.html
python -m http.server 8000 --directory dist
```

Open http://localhost:8000. Python 3.9+ is sufficient; there are no package installs or API keys needed for this demo.

The root `index.html` is a lightweight browser loader that also works when served from GitHub Pages or another static host.

## Demo features

- Complaint submission with validation and locally generated reference IDs
- Complaint tracking and status timelines
- Rule-based complaint-clarity/category suggestions
- Demonstration admin workflow for status and department updates
- Audit history, notifications, CSV export, search, and filters
- Civic insight charts and an illustrative issue map
- Hindi/English interface labels and responsive layout
- Simulated Gwalior-focused sample reports

## Data and limitations

This version is **front-end only** and stores records in the current browser's `localStorage`; it does not sync between users or devices. It has no backend, shared database, secure authentication, server-enforced administrator roles, live AI API, secure upload pipeline, verified official ward data, or government integration. Do not use it to process real complaints.

For production use, add a secure backend and database, server-side authentication and authorization, safe uploads, a configured AI service, verified civic data, privacy controls, and automated tests.

## Repository contents

- `index.html` — lightweight loader for the demo
- `source/` — compressed original prototype payload, in text-safe parts
- `tools/build.py` — reconstructs the normal HTML source from the payload
- `CODEX_NEXT_PROMPT.md` — brief for Codex to extend this prototype into a full-stack app
- `GITHUB_SETUP.md` — publishing and Pages notes
- `LICENSE` — MIT License

## GitHub Pages

A deployment workflow is included at `.github/workflows/pages.yml`. In the repository, open **Settings → Pages** and select **GitHub Actions** as the build and deployment source. A push to `main` will then publish the site.

Suggested topics: `civic-tech`, `governance`, `grievance-management`, `india`, `gwalior`, `prototype`.
