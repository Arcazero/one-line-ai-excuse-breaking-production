#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

make.fun bounty: u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66

Writes one excuse line (max 180 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
The grader runs this as `python3 -P -s /bot/main.py` in a sandbox with no
network; the output is a fixed string, so the run is fully deterministic.

Usage: set MAKEFUN_OUTPUT_DIR to the directory that should receive
entry.txt (defaults to /output), then run `python3 -P -s main.py`.
After writing, the entry re-reads entry.txt and asserts it contains exactly
the excuse line plus a trailing newline, so a partial or failed write can
never pass silently.
"""

import os

EXCUSE = (
    "I only asked the database to forget one row \u2014 it took me literally, "
    "and now it remembers nothing, including its own name."
)

assert 1 <= len(EXCUSE) <= 180, f"excuse is {len(EXCUSE)} characters"
assert EXCUSE.strip(), "excuse must not be only whitespace"
assert "\n" not in EXCUSE and "\r" not in EXCUSE, "excuse must be one line"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")
    # Read back and verify: the file must contain exactly the excuse + newline.
    with open(entry_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == EXCUSE + "\n", (
        f"entry.txt mismatch: expected {len(EXCUSE) + 1} chars, "
        f"got {len(written)} chars"
    )


if __name__ == "__main__":
    main()
