# Original prototype source bundle

The original single-file app is stored in the `app.bundle.*.txt` files as Base64-encoded gzip data. This text-safe format was used because this upload flow creates repository files through a text contents API.

To restore the regular HTML source:

```bash
python tools/build.py --output dist/index.html
```

The GitHub Pages workflow performs this step automatically before publishing the site. The reconstructed HTML is the original interactive prototype.
