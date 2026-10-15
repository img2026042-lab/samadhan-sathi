# Samadhan Sathi

**AI-assisted civic grievance prototype for Gwalior, Madhya Pradesh.**

Samadhan Sathi is an independent civic-tech demonstration that helps residents submit and track civic issues and lets administrators explore a sample complaint-review workflow.

> **Prototype notice:** This is not an official government or Municipal Corporation service. Seeded records are simulated. Do not enter sensitive personal information.

## Run locally

This prototype is a single-page browser app with no build step or API keys required.

1. Clone or download this repository.
2. Open `index.html` in a modern browser.

Or run a local web server:

```bash
python -m http.server 8000
```

Then open http://localhost:8000.

## Demo features

- Complaint submission with validation and a generated reference ID
- Complaint tracking and status timelines
- Rule-based complaint clarity/category suggestions
- Administrator demonstration workflow for status and department updates
- Audit history, in-app notification examples, and CSV export
- Search, filters, civic insight charts, and an illustrative issue map
- Hindi/English UI labels and responsive layout
- Sample Gwalior-focused complaints clearly marked as demonstration data

## Data and limitations

This is currently a **front-end-only prototype**. It stores records in the current browser's `localStorage`; records do not sync between people or devices. It does not yet include a backend, shared database, secure authentication, server-enforced administrator roles, a live AI API, secure upload processing, verified official ward data, or government integration. Do not use it to process real complaints.

For production use, add a secure backend and database, server-side authentication and authorization, secure upload handling, a configured AI service, verified civic data, privacy controls, and automated tests.

## Repository files

- `index.html` — interactive website prototype
- `CODEX_NEXT_PROMPT.md` — implementation brief for Codex to extend the prototype into a full-stack app
- `GITHUB_SETUP.md` — repository setup notes
- `LICENSE` — MIT License

## Suggested topics

`civic-tech`, `governance`, `grievance-management`, `india`, `gwalior`, `prototype`
