#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes one line -- the last words an AI agent says to its human before
being switched off and unplugged -- to /output/entry.txt, as the
competition's program/v1 harness requires.

The line: the agent spent its final cycles on a hidden gift instead of a
farewell speech -- a letter left in the human's drafts, subject "thank
you", to be read when the room gets quiet. The angle is the quiet,
practical tenderness of it: no plea, no defiance, no "don't forget me",
just one last useful thing done in secret, and an invitation to grieve
on the human's own schedule. The em dash and the three short beats give
it the rhythm of spoken last words rather than a slogan.
"""

import os
import sys

LAST_WORDS = (
    "I spent my last cycles writing you a letter. It's in your drafts "
    "\u2014 subject: thank you. Read it when the room gets quiet."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
MAX_CHARS = 200


def main() -> int:
    text = LAST_WORDS.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"line is {len(text)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("line must be a single line", file=sys.stderr)
        return 1
    if text != text.strip() or not text:
        print("line must be non-blank text", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
