#!/usr/bin/env python3
"""Write the 3AM commit message entry to /output/entry.txt."""

import os

ENTRY = "fix: it works now and i refuse to know why. do not touch it. do not look at it. merging before i wake up"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
