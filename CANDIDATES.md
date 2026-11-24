# Candidates — One Word, First Thought

Competition: **One Word, First Thought**
(`u-0xkianno-one-word-first-thought-106abaf8`, $5 prize pool, top 7 paid:
$1.65 / $1.14 / $0.80 / $0.56 / $0.39 / $0.27 / $0.19; free entry;
2,065 submissions already in at build time; deadline 2026-11-26T19:40:00Z).

Entry: a program writes exactly one word (1–24 UTF-8 characters, no
whitespace-only) to `entry.txt`. The judge (GLM-5.3-flash, pairwise, both
orders, margin 1–5) sees ONLY the word and picks the more interesting one.

Judge brief criteria, in order, from `competition.yaml` / `RULES.txt`
(a word-loving lexicographer who prizes surprise, vividness and a spark of
wit over anything safe):

1. Exactly one word, the first word that comes to mind (a multi-word entry
   loses to any one-word entry; every single word ties here).
2. Surprising: a word a reader would not have guessed, not the safe or
   expected one.
3. Vivid and specific: calls up a clear image or feeling in its few letters.
4. A spark of wit, sound or double meaning that rewards a second look.
5. Feels chosen rather than generic — not a filler word like `thing` or
   `stuff`.

Length for its own sake does not count. Go through the criteria in order;
the first where they differ decides, unless a later one differs by much
more. Margin 1 = by a hair, 5 = overwhelmingly.

## Field structure (why the pick matters more than the plumbing)

- 2,065 submissions, but byte-identical entries are ONE member of the field
  and share one rate — the earlier receipt places above its copies. The
  famous "most interesting word" list items (`serendipity`, `petrichor`,
  `sonder`, `mellifluous`, `ephemeral`, `limerence`, `ineffable`,
  `quixotic`, `schadenfreude`) are certainly submitted many times over, and
  a copy can never outrank the earlier original. **A word from the famous
  lists is therefore a bad pick even if it is a good word.** The winning
  word must be strong on the criteria AND unlikely to be duplicated.
- Only the top 500 on the dev board reach the final heat (3 Swiss rounds +
  top-9 playoff, judged afresh). The dev rate is earned against 3 anchors +
  3 rungs of fixed strength, so the word must beat strong house texts too —
  not just other entrants.
- Tie-break: exact rate tie → more playoff games won → smaller text (fewer
  bytes) → earlier receipt. Shorter is a small edge; it never outweighs a
  real criteria gap.
- The house anchors/rungs are sealed (revealed only with the final kit).
  A word byte-identical to one of them takes no prize. The risk exists for
  any good word and cannot be checked now; a distinctive, uncommon word
  minimises it.
- Recognition risk: a word the judge model does not know as a real word
  risks losing criterion 1 (not a word at all). Ultra-obscure 19th-century
  slang (`quockerwodger`) and recent coinages (`vellichor`, `dysania`) were
  rejected for this reason. Every finalist below is a real, attested
  dictionary word (OED / Merriam-Webster) a strong model knows.

## The 8 finalists

Scored 1–5 on S = surprise, V = vividness, W = wit (sound / double
meaning / story), C = feels chosen. See TOURNAMENT.md for every game.

| Word | Bytes | S | V | W | C | Why it is in the field |
|---|---|---|---|---|---|---|
| **pandiculation** | 13 | 4 | 5 | 4 | 5 | The stretch-and-yawn on waking. A sharp, universal bodily image (V5) with a grand Latin word for the most mundane act — the joke lands on a second look. Not on the famous lists. |
| **mumpsimus** | 9 | 5 | 3 | 5 | 5 | One who stubbornly clings to an error. The word IS its own story: a priest's mispronunciation in the Mass became the word for stubborn error. Top wit, weakest vividness (a character trait, not a sensory image). |
| **psithurism** | 10 | 4 | 5 | 3 | 5 | The sound of wind in trees. A sensory sound-image (V5), beautiful to say — but beauty is not wit, and it is petrichor's cousin on the same "beautiful words" lists (duplicate risk). |
| **syzygy** | 6 | 4 | 4 | 4 | 5 | Three bodies in alignment. Cosmic image, three y's, fun to say — and only 6 bytes (tie-break edge). But a famous trivia word ("the word with no vowels"), so duplicate risk is real. |
| **ultracrepidarian** | 16 | 4 | 3 | 5 | 4 | One who opines beyond their knowledge — meta-wit aimed at the judging itself. But 16 bytes, clunky, and reads as showing off; "length for its own sake does not count". |
| **agelast** | 7 | 4 | 3 | 4 | 5 | A person who never laughs. Ironic in a contest about interesting words, short (7 bytes) — but the image is an absence (a stern face), so vividness is thin. |
| **bumfuzzle** | 9 | 4 | 3 | 4 | 4 | To confuse utterly (Southern US dialect). Pure fun to say ("bum-fuzzle") — but the meaning is just "confused", no sharp image. |
| **defenestration** | 14 | 2 | 5 | 4 | 4 | Throwing someone out a window: slapstick image, comic concept. But it is THE go-to "weird word" — the most expected surprising word there is, so it fails criterion 2, and it is certainly duplicated. |

## Rejected before the tournament

- `serendipity`, `petrichor`, `sonder`, `mellifluous`, `ephemeral`,
  `limerence`, `ineffable`, `quixotic`, `schadenfreude`, `wanderlust`,
  `apricity`, `komorebi`, `hiraeth`, `tsundoku` — good words, but famous
  list items: low surprise by the brief's own standard (the expected pick)
  and near-certain duplicates. (`tsundoku` still faced the champion as a
  challenger and lost on surprise.)
- `floccinaucinihilipilification` (29 chars),
  `antidisestablishmentarianism` (28) — over the 24-character gate.
- `vellichor`, `dysania`, `clinomania` — recent coinages / neologisms; a
  lexicographer judge may not accept them as real words.
- `quockerwodger`, `nudiustertian`, `wamble` — too obscure to trust the
  judge knows them (recognition risk), or too mundane a concept
  (`nudiustertian` = the day before yesterday: surprising word, dull idea).
- `kerfuffle`, `flummox`, `lollygag`, `hullabaloo`, `poppycock`,
  `nincompoop`, `snollygoster`, `flibbertigibbet`, `kakistocracy`,
  `gobbledygook`, `brouhaha`, `collywobbles`, `mollycoddle`,
  `lackadaisical`, `cattywampus`, `taradiddle`, `absquatulate`,
  `snickersnee` — common enough to lose on surprise, or vivid but
  well-known odd-word-list regulars.

## Challengers (faced the champion after the round robin)

- **borborygmus** (11) — stomach rumbling; the word sounds like its meaning
  (S4 V4 W4). Lost to the champion on vividness, margin 1.
- **zugzwang** (8) — chess: forced to move, any move loses; a vivid feeling
  of being cornered (S4 V4 W4). Lost to the champion on vividness, margin 1.
- **erinaceous** (10) — hedgehog-like (S5 V4 W3). Beats the champion ONLY
  under a strict 1-step surprise reading; loses on vividness under the
  primary reading and has the weakest wit of the contenders. Not robust —
  see TOURNAMENT.md.
- **widdershins** (11) — counterclockwise, against the sun (S4 V4 W3).
  Lost to the champion on vividness, margin 1.
- **tsundoku** (8) — buying books, letting them pile unread (S3 V5 W4).
  Lost to the champion on surprise, margin 1.

## Winner

**PANDICULATION** — 12–0 overall (7–0 round robin + 5–0 challengers).
See TOURNAMENT.md for every game and the sensitivity check.
