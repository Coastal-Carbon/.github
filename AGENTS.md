# Agent instructions

This repo holds hum.ai's organization-wide GitHub defaults. Keep it small; every repo in the org
depends on `main` here.

## Pull request descriptions

A PR body has a human-written summary above the separator line

🙂 ↑ ────────────────────────── ↓ 🤖

and an agent-written section below it. Put everything you write, including
your summary of the change, below the line. Never edit text above it. If you
open the PR, leave the human part empty; do not draft it.

## Working here

- Run the tests with `python -m pytest -q` (stdlib only, pytest is the one dependency).
- The separator line and the stanza above are the contract. Changing either
  changes every repo's check, so do not.
