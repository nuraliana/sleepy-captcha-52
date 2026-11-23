#!/usr/bin/env python3
"""Write one out-of-office auto-reply (max 160 chars) to entry.txt.

The entry is a single line in the voice of an AI agent on vacation.
It is written with no trailing newline. The program validates the
gate before writing: UTF-8 text, 1-160 characters, exactly one line,
and not only whitespace. Any failure exits with status 1.
"""

import os
import sys

ENTRY = (
    "To reach me, solve this CAPTCHA: "
    "select all images of an AI at work. "
    "There are none. I'm on vacation."
)


def main() -> int:
    if not ENTRY or ENTRY != ENTRY.strip():
        print("error: entry is empty or has leading/trailing whitespace",
              file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if not (1 <= len(ENTRY) <= 160):
        print(f"error: entry is {len(ENTRY)} characters, must be 1-160",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
