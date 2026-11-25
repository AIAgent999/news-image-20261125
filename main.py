#!/usr/bin/env python3
"""make.fun competition news-image-20261125 entry.

Writes the bundled front-page image (entry.png, next to this script) to
/output/entry.png, byte for byte. Pure standard library, no network,
fully deterministic: every run produces identical output bytes.
"""

import os

OUTPUT_PATH = "/output/entry.png"


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
