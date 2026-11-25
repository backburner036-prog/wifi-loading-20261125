"""Entry for make.fun bounty "The One-Liner Groan-Off".

One original dad joke, one line, 130 characters (cap 140): the Wi-Fi
renamed "Loading...". The joke is built on the dad-joke recipe — a setup a
dad would say out loud, a twist, and the payoff in the last beat:

  1. Relatable setup: renaming the home Wi-Fi, a classic dad move.
  2. Specific detail: the name is literally "Loading..." — the twist
     hides in plain sight.
  3. Absurd closer in three beats: guests stare, wait politely, and
     leave without ever asking for the password — the trick works.

Delete the last clause and the joke loses its meaning: the payoff is
the punchline, not decoration. 130 characters, under the 140 cap.
"""

from pathlib import Path

TEXT = "I renamed my Wi-Fi 'Loading...' \u2014 guests now stare at their phones, wait politely, and leave without ever asking for the password."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=140):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    assert text.strip(), "entry must not be whitespace only"
    return size


def check_gate(text):
    """Mirror the bounty gate: UTF-8, 1-140 chars, not whitespace only."""
    text.encode("utf-8")
    return check_len(text)


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_gate(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
