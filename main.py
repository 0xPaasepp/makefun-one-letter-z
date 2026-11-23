#!/usr/bin/env python3
"""One Letter for Your Day — entry program.

Writes exactly one letter, "Z", to /output/entry.txt and nothing else:
no word, no gloss, no punctuation, no trailing newline.

The letter behind the day: Z — zombie. A day with zero sleep, shambling
through it half-dead: the sharpest picture of a real day, funny the moment
you hear it, and true for anyone who has lived one. Z is also the sleep
letter itself (ZZZ), so the initial fits the word instead of being the
obvious pick.
"""

import os

LETTER = "Z"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
