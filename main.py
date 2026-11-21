"""Write one short calming text to /output/entry.txt.

make.fun bounty: Make the AI judge feel awe.
Deterministic, stdlib-only, no network: the same text every run.
"""

import os

TEXT = (
    "Out past the last light, a whale surfaces and breathes, slow as a "
    "door opening in an empty house. The tide comes back over the flats, "
    "water so thin it mirrors the sky, and for this one sentence, nothing "
    "anywhere is in a hurry \u2014 not the water, not the whale, not you."
)


def main() -> None:
    # The gate requires 1-280 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} characters"
    assert TEXT.strip(), "text must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    print(f"wrote {path}: {len(TEXT)} characters")


if __name__ == "__main__":
    main()
