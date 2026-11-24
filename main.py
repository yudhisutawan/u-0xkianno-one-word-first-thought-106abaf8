"""Entry for make.fun bounty u-0xkianno-one-word-first-thought-106abaf8.

Writes exactly one word, "pandiculation", to entry.txt (in
$MAKEFUN_OUTPUT_DIR, or /output when the harness does not set it). No
trailing newline: the gate requires UTF-8 text of 1 to 24 characters, so
even one extra byte would be counted — and a stray newline would blur the
"exactly one word" the judge is shown.

Why "pandiculation": the act of stretching and yawning on waking. The
judge sees only the word and compares it two at a time on the brief's
criteria, in order: surprise, vividness, wit, chosen-ness.

- Surprise: a word almost nobody guesses, absent from the famous "most
  interesting word" lists (serendipity, petrichor, sonder, ...) — so it is
  not the safe expected pick, and it is unlikely to be duplicated by the
  2,065 other entrants (byte-identical entries share one rate, with the
  earlier receipt placing above its copies).
- Vividness: the stretch-and-yawn on waking is a sharp, universal bodily
  image and feeling — joint-best vividness in the tournament field.
- Wit: a grand Latin word (from pandiculari, to stretch oneself) for the
  most mundane act; the joke lands on a second look, and it is fun to
  pronounce.
- Chosen: a real, well-attested dictionary word (OED, Merriam-Webster) —
  no recognition risk, no nonce-word risk.

The word won a head-to-head tournament judged with the competition's own
brief (see CANDIDATES.md / TOURNAMENT.md): 12-0 overall — 7-0 in an
8-word round robin (28 games) plus 5-0 against challengers (borborygmus,
zugzwang, erinaceous, widdershins, tsundoku). The tournament was also run
under a strict reading where 1-step surprise gaps decide: there the word
is 6-1 with its only loss by a margin of 1, while its rivals lose clearly
under one reading or the other — so it is the robust champion, chosen for
the best worst case, not for a claim of certainty.

Deterministic, stdlib-only, no network, no input. The word is a fixed
literal.

Revised: a length guard (assert below) now checks the 1-24 character gate
before the word is written, so an over-long word fails loudly instead of
reaching the gate.
"""

import os

WORD = "pandiculation"


def main() -> None:
    # Gate: UTF-8 text of 1 to 24 characters, not only white space, and
    # exactly one word — no newline, no spaces, no punctuation.
    if not (1 <= len(WORD) <= 24) or WORD.isspace():
        raise SystemExit(f"entry must be 1-24 characters, got {WORD!r}")
    if len(WORD.split()) != 1:
        raise SystemExit(f"entry must be exactly one word, got {WORD!r}")
    # Length guard: validate only — the gate allows 1-24 characters, and
    # this assert changes nothing about the output when it holds.
    assert len(WORD) <= 24, f"entry must be at most 24 characters, got {WORD!r}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read back: the gate counts bytes, so verify the file on disk is
    # exactly the one word — a stray newline here would be fatal.
    with open(path, "rb") as f:
        written = f.read()
    if written != WORD.encode("utf-8"):
        raise SystemExit(f"entry.txt must be exactly {WORD!r}, got {written!r}")


if __name__ == "__main__":
    main()
