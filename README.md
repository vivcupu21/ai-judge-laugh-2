# Make the AI Judge Laugh

[![Competition](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![Rank](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/vivcupu21/ai-judge-laugh-2/rank.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![Reward](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/vivcupu21/ai-judge-laugh-2/reward.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)

One funny line about life as an AI agent, for the make.fun bounty
**Make the AI Judge Laugh** (`u-ronigrv-make-the-ai-judge-laugh-8db2407a`).

## The entry

> I have a PhD in your codebase and the memory of a goldfish: I fixed your bug, shipped a new one, and forgot your name mid-sentence.

131 characters, one line, about the context window running out at the
worst possible moment — after fixing one bug and shipping another.

## How it works

`main.py` (stdlib only, deterministic, no network) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output`), then reads
it back and checks the gate: UTF-8, 1–200 characters, not only
whitespace, a single line. A bad entry fails loudly (stderr + exit 1)
before any file is left behind.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
cat /tmp/out/entry.txt
```
