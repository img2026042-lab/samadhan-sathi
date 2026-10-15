# Setup and publishing

## Run locally

Restore the original prototype page from the text-safe compressed source bundle:

```bash
python tools/build.py --output dist/index.html
python -m http.server 8000 --directory dist
```

Open http://localhost:8000. Python 3.9+ is sufficient.

## Publish with GitHub Pages

1. Open the repository's **Settings → Pages**.
2. Under build and deployment, choose **GitHub Actions** as the source.
3. Push to `main` or manually run the **Deploy Samadhan Sathi to GitHub Pages** workflow.
4. When the workflow succeeds, the Pages site URL appears under Settings → Pages.

The site is an independent frontend prototype. Its demo records are simulated and browser-local; it is not connected to an official government service.

## Git commands

```bash
git clone https://github.com/img2026042-lab/samadhan-sathi.git
cd samadhan-sathi
python tools/build.py --output dist/index.html
python -m http.server 8000 --directory dist
```
