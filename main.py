#!/usr/bin/env python3
"""Pigeon Pitch, One Line.

Writes one elevator pitch -- a city pigeon pitching its startup to
investors -- to /output/entry.txt. Standard library only.
"""

import os

PITCH = (
    "I'm raising a seed round \u2014 literally, seeds \u2014 for Statuebnb: "
    "premium perches above every monument, and our guests never check "
    "out, they just poop and leave."
)


def write_entry(path: str, text: str) -> None:
    """Write the pitch to *path*, creating the output directory first."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


def main() -> None:
    output_dir = "/output"
    path = os.path.join(output_dir, "entry.txt")
    write_entry(path, PITCH)


if __name__ == "__main__":
    main()
