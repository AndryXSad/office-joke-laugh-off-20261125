"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is fixed and deterministic: the winner of a 20-candidate local
pairwise tournament judged against the published brief (real one-line office
joke, sharp surprising punchline in the last few words, clear on one read,
fresh wording, tight). It is 83 characters, one line, UTF-8, inside the
competition gate of 1-200 characters.
"""

import os

LINE = "The engagement survey asked if I feel valued, and the submit button was greyed out."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    with open(path, "w", encoding="utf-8") as f:
        # One trailing newline: the file holds exactly one line of text.
        f.write(text + "\n")


if __name__ == "__main__":
    main()
