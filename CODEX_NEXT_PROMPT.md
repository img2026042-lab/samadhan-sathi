# Codex task: turn Samadhan Sathi into a full-stack app

Use the current prototype as the UI/product reference. First restore the original HTML with `python tools/build.py --output dist/index.html`; preserve the Samadhan Sathi brand, layout, and working interaction patterns. Do not replace it with a generic landing page.

Build a responsive civic grievance platform for Gwalior, Madhya Pradesh. Inspect the workspace and choose a compatible stack; prefer React + TypeScript + Vite, Express, PostgreSQL + Drizzle, Zod, secure session authentication, and Leaflet if practical. Implement the application directly.

Prioritize:
1. Persistent complaint submission, unique IDs, validation, complaint search/tracking, status timeline, citizen feedback, and reopening requests.
2. Real authentication, backend-enforced citizen/admin permissions, complaint review, assignments, status updates, and append-only audit history.
3. Dashboard metrics, filters, duplicate suggestions with human review, in-app notifications, and CSV exports.
4. Hindi/English UI, AI wording/category/summary suggestions through a server-only API key, and a clearly labelled rule-based fallback if no key is configured.
5. Civic analytics and a map. Label demo data; never imply simulated records are real or that the system integrates with government.

Reuse compatible dependencies; add migrations and seed scripts; validate on the client and server; keep secrets in environment variables; securely validate uploads; protect private details and addresses. AI must not reject, deprioritize, or resolve complaints. Never invent official wards, departments, deadlines, or government integrations.

Run available tests, type checks, and production build; fix errors introduced. Finish with setup instructions, required environment variables, secure first-admin bootstrap steps, test results, and clear live-versus-simulated limitations. If full scope cannot be completed in one pass, finish and test the core workflow before expanding.

