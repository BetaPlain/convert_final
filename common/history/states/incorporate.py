#!/usr/bin/env python3

STATE_FILE = "./99_converter_states.txt"

import pathlib
import re
import sys

PATTERN = re.compile(r'(\bstate_type\s*=\s*)unincorporated\b', flags=re.IGNORECASE)

def convert(text: str) -> str:
    """Replace every unincorporated state_type with incorporated."""
    return PATTERN.sub(r'\1incorporated', text)

def main() -> None:
    path = pathlib.Path(STATE_FILE)
    if not path.is_file():
        sys.exit(f"File not found: {path}")

    original = path.read_text(encoding="utf-8")
    updated = convert(original)
    path.write_text(updated, encoding="utf-8")
    print(f"Converted all unincorporated state_type entries in {path}")

if __name__ == "__main__":
    main()
