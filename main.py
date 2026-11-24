#!/usr/bin/env python3
"""Write one one-line cat joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

The joke: a cat walks across the keyboard during a work call and ends up
promoted before its owner. Setup, turn, done — under 200 characters.
Standard library only, no network, no input files.
"""

import os
import sys

JOKE = (
    "My cat walked across my keyboard during a work call "
    "and somehow got promoted before I did."
)


def validate(text: str) -> str:
    """Return the joke cleaned up, or fail loudly if it breaks the gate.

    The gate wants UTF-8 text of 1 to 200 characters, not only whitespace,
    as a single line. Checking here keeps a bad joke from ever being
    submitted instead of failing silently in the grader.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("joke must not be empty")
    if len(cleaned) > 200:
        raise ValueError("joke must be under 200 characters")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("joke must be a single line")
    return cleaned


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(validate(JOKE) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
