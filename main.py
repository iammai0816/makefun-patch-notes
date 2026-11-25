#!/usr/bin/env python3
"""Write one original real-life patch note to /output/entry.txt.

The program is deterministic: it always emits the same single patch note,
the entry itself, into entry.txt under MAKEFUN_OUTPUT_DIR.
"""

import os

ENTRY = (
    "v2.9.4: fixed a bug where the eyes watered at onions "
    "but stayed dry through every sad movie."
)


def main() -> None:
    # Guard: the entry must be a single line under 160 chars before writing.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= 160, f"entry too long: {len(ENTRY)} chars"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
