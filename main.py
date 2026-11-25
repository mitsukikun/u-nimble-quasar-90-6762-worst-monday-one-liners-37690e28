#!/usr/bin/env python3
"""Worst Monday One-Liners - make.fun entry.

Writes the single final one-liner (<=140 chars) to /output/entry.txt.
Python 3 standard library only, no network access.
"""

from pathlib import Path

LINE = "Monday: my stand-up should've been an email, my deploy froze, my inbox flooded \u2014 and my own code filed a bug against me."

def main() -> None:
    assert len(LINE) <= 140, f"line is {len(LINE)} chars, over the 140 limit"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
