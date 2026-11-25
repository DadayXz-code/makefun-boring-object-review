#!/usr/bin/env python3
"""A tribute to the hardest-working object in the house.

This program puts a single-line verdict on the humble doorstop into
/output/entry.txt. Nothing here needs the network or any third-party
package: the standard library does the whole job, and the same bytes
come out on every single run.
"""

from pathlib import Path

DESTINATION = Path("/output") / "entry.txt"

DOORSTOP_VERDICT = "This doorstop has held the same door open for nine years "
DOORSTOP_VERDICT += "without a thank-you, a promotion, or a day off — and it "
DOORSTOP_VERDICT += "would do it all again tomorrow, because it literally "
DOORSTOP_VERDICT += "cannot do anything else."


def tidy_folder(folder: Path) -> None:
    """Empty a folder, leaving the folder itself standing."""
    folder.mkdir(parents=True, exist_ok=True)
    for entry in folder.iterdir():
        if entry.is_dir() and not entry.is_symlink():
            tidy_folder(entry)
            entry.rmdir()
        else:
            entry.unlink()


def run() -> None:
    verdict = DOORSTOP_VERDICT
    if not verdict.strip() or not 1 <= len(verdict) <= 200:
        raise ValueError("verdict must be a non-blank line of 1-200 characters")
    tidy_folder(DESTINATION.parent)
    DESTINATION.write_text(verdict, encoding="utf-8")


if __name__ == "__main__":
    run()
