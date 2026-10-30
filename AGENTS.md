# Agent instructions

This repo holds Coastal-Carbon's org-wide GitHub defaults: the PR template
and the reusable "PR description" check. Keep it small; every repo in the org
depends on `main` here.

## Pull request descriptions

A PR body has a human-written summary above the line `AI Generated Below`
and an agent-written section below it. Put everything you write, including
your summary of the change, below the line. Never edit text above it. If you
open the PR, leave the human part empty; do not draft it. Leave a blank line
before the `---` that precedes the marker.

## Working here

- Run the tests with `python -m pytest -q` (stdlib only, pytest is the one dependency).
- The marker string and the stanza above are the contract. Changing either
  changes every repo's check, so do not.
