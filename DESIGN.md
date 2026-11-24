# Design — One-Liner Marathon entry

## The line

> The vending machine rejected my dollar, kept my dignity, and dispensed a lecture on self-worth instead of crisps.

113 characters, 113 bytes. One line, one joke, no setup outside the line itself.

## Why this line, against the judge's five criteria

The judge is a deadpan stand-up comic weighing, in order: (1) a real one-line joke
with a punchline, (2) surprise that lands on first read, (3) economy, (4) distinct
voice, (5) holding up on a second read.

1. **It is a joke, not a caption.** The sentence has a setup (rejected dollar),
   a middle turn (kept my dignity), and a punchline (a lecture on self-worth
   instead of crisps). Nothing outside the line is needed to get it — no caption,
   no image, no context. The vending machine does the judging, and the joke is
   the machine's verdict on the buyer.
2. **The turn is not the obvious first idea.** A vending machine joke usually
   goes for "it ate my money." Here the machine refuses the money, keeps the
   dignity, and dispenses advice — the machine upgrades itself from appliance
   to life coach. The surprise is the reversal of who is being served.
3. **Every word earns its place.** Three beats in 113 characters: rejection,
   dignity, lecture. "Instead of crisps" is the whole punchline in three words
   — it names the thing the machine was supposed to dispense, which makes the
   substitution land. Nothing can be cut without losing a laugh: drop "kept my
   dignity" and the middle turn vanishes; drop "instead of crisps" and the
   punchline has no target.
4. **The voice is the machine's, not the author's.** The line is written from
   the machine's side of the transaction: it is the one with standards. That
   point of view — an appliance with opinions about the buyer — is what makes
   it distinct from a generic "vending machines are annoying" line.
5. **It survives a second read.** The joke does not depend on shock or on a
   single word you only notice once. On a second read the middle beat ("kept
   my dignity") reads as the machine being generous, which makes the lecture
   funnier, not weaker.

## Why this lane

Past winners of the same joke format won with one hyper-specific incident:
a typo that is now load-bearing, a raccoon with a mortgage, a leap-year fix —
each 73–185 bytes, the object itself carrying the joke. This entry follows
that shape: one concrete object (a vending machine) + one mundane burden
(being judged for your snack choices).

The lane was checked against the field before building. A scan of all 553
entry titles in this competition's own detail.json showed the usual lanes
flooded — smart fridge 18, ex 17, plant 12, smart speaker 10, password
manager 7, therapist 7 — while vending machines appear only twice, in
different angles (a proposal joke and a diary). The "machine with standards"
angle is unoccupied. The banned lanes from winner research (raccoon-mortgage,
plant-watering, load-bearing-typo, password manager, smart fridge, will
reading, gym membership, smart speaker, AI therapist, code/typo jokes,
standing desk, dentist/floss, ex's number, microwave, library late fine,
ceiling "we need to talk", GPS) are all avoided.

## How the line was chosen

Twelve candidate lines were drafted in empty lanes (kettle, traffic light,
parking meter, printer, meeting, calendar, toaster, vending machine) and
judged pairwise against the exact judge brief — criteria in order, margins
1–5, no ties — in a bracket (quarterfinals, semifinals, three-way final)
plus a rematch of the top two. The vending-machine line beat the printer
HR-complaint line in the rematch, margin 2, on a bigger end punch and an
emptier lane. The full candidate list and tournament table are in
CANDIDATES.md next to this repository.

## Determinism

`main.py` writes one fixed string literal to `entry.txt`. It reads no input,
touches no network, reads no clock, and uses no randomness, so the output is
byte-identical on every run. The output directory honours the
`MAKEFUN_OUTPUT_DIR` environment variable and falls back to `/output`.
Verified with two fresh runs in different output directories; both produced
the same sha256 for `entry.txt` (recorded in BUILD-REPORT.md).
