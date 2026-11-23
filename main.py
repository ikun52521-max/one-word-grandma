#!/usr/bin/env python3
"""One Word From Grandma — a single word, the way grandma would text it.

Grandma has one answer for every machine that misbehaves, from the
blinking VCR to the robot that now writes poems: pull the plug. She
types it the way she types everything, in capital letters, because
the caps lock has been on since 2014 and nobody has told her.

The program writes exactly that one word to /output/entry.txt.
Nothing else is written, nothing is read, nothing varies between runs.
"""

import os
import sys

# The word. Grandma's whole tech-support philosophy in six letters.
WORD = "UNPLUG"

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    text = WORD

    # The gate allows 1 to 30 characters of UTF-8 text, not only
    # whitespace, and the task allows exactly one word: no spaces,
    # no punctuation, no sentence hiding inside the word.
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 30 or not text.strip():
        print("word fails the gate", file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in text):
        print("word must be a single word", file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "wb") as handle:
        handle.write(encoded)
    # The grader collects the output as another user, so the file
    # must be readable by everyone, not just its owner.
    os.chmod(OUTPUT_FILE, 0o644)

    print(f"wrote {OUTPUT_FILE}: {text!r} ({len(encoded)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
