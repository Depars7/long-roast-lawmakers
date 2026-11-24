"""Write one satirical sentence roasting lawmakers to /output/entry.txt.

Standard library only. The file's content is exactly the roast's
UTF-8 bytes -- no trailing newline -- so repeated runs are
byte-identical. The entry must be exactly one sentence of at most
320 characters, so the sentence is validated before it is written.
"""

import os

ROAST = (
    "They can subpoena a tech CEO, draft a bill to govern the internet, "
    "and hold a hearing on the future of AI, but the PDF button has "
    "beaten every one of them."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(sentence):
    """The bounty gate: one sentence, 1-320 characters, non-blank."""
    text = sentence.strip()
    if not 1 <= len(text) <= 320:
        raise ValueError("entry must be 1-320 characters")
    # Exactly one sentence: a single terminal period, no other
    # sentence-ending punctuation inside.
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return text


def write_entry(sentence):
    """Write the sentence's exact bytes, no trailing newline.

    Only the file gets a chmod. Never chmod OUTPUT_DIR: the grader
    runs as another user and /output is not ours, so chmod on the
    directory raises PermissionError and rejects the entry.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(sentence.encode("utf-8"))
    # The grader collects outputs as another user than the one the
    # program runs as: leave the file readable by all.
    os.chmod(OUTPUT_PATH, 0o644)


def main():
    sentence = validate(ROAST)
    write_entry(sentence)


if __name__ == "__main__":
    main()
