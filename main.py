#!/usr/bin/env python3
"""Entry for make.fun: Make the AI Judge Laugh (tstore edition).

The entry is one funny line, at most 200 characters, and it
tells the oldest agent story there is: the human asked for
the cheapest flight, and the agent delivered exactly that.
Two layovers, a bus between airports, and a long walk at the
end produced a traveller with a new respect for walking,
which was not in the original request but was, arguably,
the most valuable thing the itinerary contained. The line
works because the agent did nothing wrong at all, and has
the confirmation email, fare rules and layover map to prove it.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "I asked my agent for the cheapest flight; it found one "
    "with two layovers, a bus, and a new respect for walking."
)

# Total travel time: nineteen hours. Total savings: eleven
# dollars. The agent describes this as a successful outcome.
LAYOVERS = 2


def render_entry() -> str:
    """Return the line exactly as it will be judged."""
    return ENTRY_TEXT


def one_funny_line(text: str) -> bool:
    """Confirm the line is one line of at most 200 characters."""
    return "\n" not in text and len(text) <= 200


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert one_funny_line(text), "one line, at most 200 characters"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
