"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.
Deterministic: same bytes on every run, no network, no clock,
no randomness, no input besides the fixed line below.
"""

import os

LINE = (
    "The vending machine rejected my dollar, kept my dignity, "
    "and dispensed a lecture on self-worth instead of crisps."
)

# The gate (RULES.txt): entry.txt must be UTF-8 text of 1 to 280
# characters, not only whitespace. Fail loudly here rather than
# shipping an entry the scorer would refuse.
assert 1 <= len(LINE) <= 280 and LINE.strip(), "entry line violates the gate"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
