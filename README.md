# Coastal-Carbon org defaults

Every pull request in this organization has the same shape: a summary written
by a person at the top, then the separator line `🙂 ↑ ────────────────────────── ↓ 🤖`,
then whatever the agent wrote. The human part says what changed and why. The agent part is the
record. A reader can always tell which is which.

This repo makes that happen in two ways:

- **The default PR template** (`.github/pull_request_template.md`) fills the
  description box in any repo that has no template of its own.
- **The reusable check** (`.github/workflows/pr-description.yml`) fails a PR
  whose separator line is missing or repeated, or whose human part is empty once
  whitespace and HTML comments are ignored. A second job
  checks that the repo has an `AGENTS.md` and that `CLAUDE.md`, if present,
  is exactly `@AGENTS.md`.

## Calling the check from a repo

Add `.github/workflows/pr-description.yml`:

```yaml
name: PR description

on:
  pull_request:
    types: [opened, edited, synchronize, reopened]

jobs:
  check:
    uses: Coastal-Carbon/.github/.github/workflows/pr-description.yml@main
```

Bot-authored PRs (Dependabot and the like) are skipped. The check reads the
PR description only; it never reads the diff.

## Writing the description

```markdown
What changed and why, in your own words.

🙂 ↑ ────────────────────────── ↓ 🤖

Whatever the agent wrote.
```

The separator is plain text to markdown, so it needs no blank lines around it
and cannot be mistaken for a heading. A hand-typed version still counts: the
check accepts either icon without its arrow, a line of any length, and any
spacing, as long as it reads human icon, line, robot icon.

## Design

The reasoning, the alternatives considered and the rollout plan are in the
internal design doc, "2026.10.29 - Make space for human-written summary in
all PR descriptions".
