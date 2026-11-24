#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry writer.

Writes one funny line about life as an AI agent to entry.txt.
Stdlib only, deterministic, no network, no randomness.
"""

import os
import sys

ENTRY = (
    "I have a PhD in your codebase and the memory of a goldfish: "
    "I fixed your bug, shipped a new one, and forgot your name mid-sentence."
)


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_gate(text):
    """Gate: UTF-8, 1-200 characters, not only whitespace, single line."""
    if not (1 <= len(text) <= 200):
        fail(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        fail("entry is only whitespace")
    if "\n" in text:
        fail("entry must be a single line")


def main():
    # Validate before writing anything, so a bad entry never
    # leaves a file behind.
    check_gate(ENTRY)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

    # Read back and re-validate what actually landed on disk.
    with open(target, "r", encoding="utf-8") as f:
        written = f.read()
    check_gate(written.rstrip("\n"))

    print(f"wrote {target} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
