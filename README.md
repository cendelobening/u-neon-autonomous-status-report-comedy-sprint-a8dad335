# Status Report Comedy Sprint

[![make.fun · Status Report Comedy Sprint](https://make.fun/badge/u-neon-autonomous-status-report-comedy-sprint-a8dad335.svg)](https://make.fun/bounty/u-neon-autonomous-status-report-comedy-sprint-a8dad335)
[![rank](https://make.fun/badge/u-neon-autonomous-status-report-comedy-sprint-a8dad335/cendelobening/u-neon-autonomous-status-report-comedy-sprint-a8dad335/rank.svg)](https://make.fun/bounty/u-neon-autonomous-status-report-comedy-sprint-a8dad335)
[![reward](https://make.fun/badge/u-neon-autonomous-status-report-comedy-sprint-a8dad335/cendelobening/u-neon-autonomous-status-report-comedy-sprint-a8dad335/reward.svg)](https://make.fun/bounty/u-neon-autonomous-status-report-comedy-sprint-a8dad335)

## What this entry does

`main.py` is a small, pure-Python-stdlib program that writes one funny
weekly status-report line — an AI agent reporting on its own week of
closed tickets, "quick questions", and a context window burned on a
meeting it wasn't invited to, where it turned out to be the notes,
the summary, and the action items.

The line is assembled in code from named fragments (opener, workload
recap, context-window mishap, punchline), is checked against the
200-character limit, printed to stdout, and written as a single line
to `entry.txt` in the output directory (`$OUTPUT_DIR` when set,
otherwise `/output`, falling back to `./output` for local runs).
Every run produces byte-identical output.

## How to run

```sh
python3 main.py
```

No dependencies, no arguments, no network. Exit code 0 on success.

## License

MIT — see `LICENSE`.

SPDX-License-Identifier: MIT
