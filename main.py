#!/usr/bin/env python3
"""Write the 3AM commit message entry to /output/entry.txt."""

import os

ENTRY = "fix: deleted the feature to fix the bug. the feature was the bug all along. merging before i change my mind"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
