#!/usr/bin/env python3

STATE_FILE = "./12_indonesia.txt"

import pathlib
import re
import sys

ARABLE_RE = re.compile(r'(\barable_land\s*=\s*)(\d+)(\b)')

def double_values(text: str) -> str:
    """Return text with all arable_land numbers doubled."""
    def repl(m):
        return f"{m.group(1)}{int(m.group(2)) * 2}{m.group(3)}"
    return ARABLE_RE.sub(repl, text)

def main() -> None:
    path = pathlib.Path(STATE_FILE)
    if not path.is_file():
        sys.exit(f"File not found: {path}")

    path.write_text(double_values(path.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"Doubled arable_land values in {path}")

if __name__ == "__main__":
    main()
