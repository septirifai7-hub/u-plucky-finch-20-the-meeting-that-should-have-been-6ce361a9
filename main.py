"""The Meeting That Should Have Been an Email.

The joke needs no setup because everyone has lived it: a meeting that
could have been one email, stretched out while one colleague eats lunch
in front of twelve silent people. Dave is every office's Dave.

Running this file writes the line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``), with no trailing newline.
"""

import os

ENTRY = (
    "This meeting could have been an email, but then twelve people would "
    "never have learned what Dave eats for lunch."
)


def get_entry() -> str:
    """Return the meeting joke."""
    return ENTRY


def write_entry(output_dir: str | None = None) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    directory = output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry and print where it went."""
    print(write_entry())


if __name__ == "__main__":
    main()
