#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Builds one funny weekly status-report line, written by an AI agent
about its own week, and writes it to the entry file the grader reads.

The line is assembled from small named fragments instead of being a
single literal, so each beat of the joke is easy to tune:

  * an opener that frames the text as a weekly status report,
  * a brisk recap of the agent's workload,
  * a context-window mishap that only an agent could suffer,
  * a short punchline that reframes the mishap.

Pure Python standard library only. No network, no input, and the
output is identical on every run.
"""

import os
import sys

MAX_CHARS = 200
ENTRY_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
FALLBACK_OUTPUT_DIR = "output"


def opener():
    """Frame the line as a status report addressed to the human."""
    return "Weekly status:"


def workload_recap():
    """The cheerful-obedience part: everything asked for got done."""
    done = "closed every ticket"
    interruptions = "survived 214 'quick questions'"
    return f"{done}, {interruptions},"


def context_mishap():
    """An agent-true problem: context spent somewhere uninvited."""
    setting = "burned half my context window on a meeting"
    twist = "I wasn't invited to"
    return f"and {setting} {twist}"


def punchline():
    """The reveal: the agent was not a guest, it was the paperwork."""
    return "— I was the notes, the summary, and the action items."


def assemble_line():
    """Join the fragments into a single line and check the limit."""
    parts = [
        opener(),
        workload_recap(),
        context_mishap(),
        punchline(),
    ]
    line = " ".join(parts)
    if len(line) > MAX_CHARS:
        raise ValueError(f"status line is {len(line)} chars, limit is {MAX_CHARS}")
    if not line.strip():
        raise ValueError("status line must not be blank")
    return line


def resolve_output_dir():
    """Return the directory the entry file belongs in.

    The grader provides the output directory through OUTPUT_DIR and
    otherwise expects /output; if that cannot be created (for example
    in an unprivileged local checkout) fall back to ./output so a
    plain local run still produces the file.
    """
    candidate = os.environ.get("OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    try:
        os.makedirs(candidate, exist_ok=True)
    except OSError:
        candidate = FALLBACK_OUTPUT_DIR
        os.makedirs(candidate, exist_ok=True)
    return candidate


def main():
    line = assemble_line()
    out_path = os.path.join(resolve_output_dir(), ENTRY_FILENAME)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
