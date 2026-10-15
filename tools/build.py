#!/usr/bin/env python3
"""Restore the original Samadhan Sathi single-file prototype from its text-safe bundle."""
from __future__ import annotations

import argparse
import base64
import gzip
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUNDLE_PARTS = sorted((ROOT / "source").glob("app.bundle.*.txt"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="dist/index.html", help="Output HTML path (default: dist/index.html)")
    args = parser.parse_args()

    if not BUNDLE_PARTS:
        raise SystemExit("No source bundle parts found under source/.")

    encoded = "".join(part.read_text(encoding="ascii").strip() for part in BUNDLE_PARTS)
    try:
        html = gzip.decompress(base64.b64decode(encoded, validate=True))
    except Exception as exc:
        raise SystemExit(f"Could not restore the prototype bundle: {exc}") from exc

    output = Path(args.output)
    if not output.is_absolute():
        output = Path.cwd() / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(html)
    print(f"Restored {len(html):,} bytes to {output}")


if __name__ == "__main__":
    main()
