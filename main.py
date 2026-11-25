#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

A tiny program with one job: speak the phone's final line as its
battery reaches 1 percent, and write it to /output/entry.txt.
Python 3.13 standard library only; no third-party dependencies.
"""

from pathlib import Path

# The phone's last words, in its own voice: it did not die at 4%.
# It chose to hold on at 1% just long enough to watch its owner panic.
LAST_WORDS = (
    "I could have died at 4%, but I held on at 1% for twenty minutes "
    "just to watch you sprint for the charger \u2014 worth every volt."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(LAST_WORDS) <= 199:
        raise ValueError("last words must be a single line of 1-199 characters")
    if "\n" in LAST_WORDS or not LAST_WORDS.strip():
        raise ValueError("last words must be one non-blank line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LAST_WORDS + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
