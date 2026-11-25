#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes one dry, petty, specific note from a smart fridge to its owner
to /output/entry.txt (no trailing newline). Deterministic: the same
bytes on every run.
"""

import os

ENTRY = "You opened me 14 times today and took nothing. I am not a window. Pick something or close me."

# The gate allows 1..200 characters, a single line, no trailing newline.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
assert "\n" not in ENTRY, "entry must be a single line"


def write_entry(path: str = "/output/entry.txt") -> str:
    """Write the note deterministically and return the bytes written."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Round-trip check: what landed on disk must be exactly the note.
    with open(path, "rb") as f:
        on_disk = f.read().decode("utf-8")
    assert on_disk == ENTRY, "written bytes differ from ENTRY"
    assert not on_disk.endswith("\n"), "no trailing newline allowed"
    return ENTRY


def main() -> None:
    text = write_entry()
    print(f"chars: {len(text)}")


if __name__ == "__main__":
    main()
