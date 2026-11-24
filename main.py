#!/usr/bin/env python3
"""One Letter for Your Day — the entry script.

It writes one letter to /output/entry.txt: Z, and nothing more.
No word, no gloss, no punctuation, no trailing newline.

Z stands for zombie — a day with zero sleep, dragging through it
half-dead. It is the sharpest picture of a real day: funny the moment
you hear it, true for anyone who has lived one. And Z is the sleep
letter itself (ZZZ), so the initial fits the word instead of being
the obvious pick.
"""

from pathlib import Path

DAY_WORD = "zombie"
DESTINATION = Path("/output/entry.txt")


def initial_of(word: str) -> str:
    """The word's first letter, in upper case."""
    return word[0].upper()


def write_entry() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(initial_of(DAY_WORD), encoding="utf-8")


if __name__ == "__main__":
    write_entry()
