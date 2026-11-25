#!/usr/bin/env python3
"""One-line review of the most boring everyday object.

Writes a single funny, true review (at most 200 characters) of a doorstop
to /output/entry.txt. Standard library only, fully deterministic: the same
text is written on every run.
"""

import os
import shutil

REVIEW = (
    "This doorstop has held the same door open for nine years without a "
    "thank-you, a promotion, or a day off \u2014 and it would do it all again "
    "tomorrow, because it literally cannot do anything else."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def clear_output_dir(path):
    """Remove every child of path without deleting path itself."""
    os.makedirs(path, exist_ok=True)
    for name in os.listdir(path):
        child = os.path.join(path, name)
        if os.path.isdir(child) and not os.path.islink(child):
            shutil.rmtree(child)
        else:
            os.remove(child)


def main():
    if not 1 <= len(REVIEW) <= 200 or not REVIEW.strip():
        raise ValueError("review must be 1-200 non-blank characters")
    clear_output_dir(OUTPUT_DIR)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(REVIEW)


if __name__ == "__main__":
    main()
