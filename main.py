#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

The phone's final line as its battery hits 1 percent: it did not die at
4% — it held on at 1% for twenty minutes on purpose, just to watch its
owner sprint for the charger. Written in Python 3.13 standard library
only; the output is a single line, at most 199 characters, UTF-8.
"""

from pathlib import Path

ENTRY = (
    "I didn't die at 4%. I hovered at 1% for twenty minutes just to watch "
    "you sprint across the room for the charger — worth every volt."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 199


def main() -> int:
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, f"entry length {len(line)} out of range"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
