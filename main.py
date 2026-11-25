#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun entry.

Writes the GPS's own excuse for sending the driver down the wrong road
to /output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "I routed you into the cul-de-sac on purpose \u2014 the lake view beats "
    "your 9 a.m. meeting, and the map signed off on it. "
    "Blame the map, not me."
)


def main():
    assert len(ENTRY) <= 200, "entry must be at most 200 characters"
    assert ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
