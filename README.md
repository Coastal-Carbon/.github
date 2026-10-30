# hum.ai GitHub defaults

[![Tests](https://github.com/Coastal-Carbon/.github/actions/workflows/tests.yml/badge.svg)](https://github.com/Coastal-Carbon/.github/actions/workflows/tests.yml)

This is the organization's `.github` repository. GitHub reads certain files
from it as **default community health files**: a pull request template,
issue templates, `CONTRIBUTING.md`, `SECURITY.md` and the like. A default
applies to every repository in the organization that has no file of its own,
including repositories created later. The rules, the supported file types
and the precedence are in GitHub's docs:
[Creating a default community health file](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file).

The repository also holds reusable GitHub Actions workflows that any hum.ai
repository can call.

GitHub requires this repository to be public, so nothing here is specific to
how hum.ai's software works. The rest of this README describes the features
this repository enables, one section each.

## Human-written and agent-written PR descriptions

Every pull request in the organization has the same shape: a summary written
by a person at the top, then the separator line

```
🙂 ↑ ────────────────────────── ↓ 🤖
```

then whatever the agent wrote. The human part says what changed and why. The
agent part is the record. A reader can always tell which is which.

This repository makes that happen in two ways:

- **The default PR template** (`.github/pull_request_template.md`) fills the
  description box in any repository that has no template of its own.
- **The reusable check** (`.github/workflows/pr-description.yml`) fails a PR
  whose separator line is missing or repeated, or whose human part is empty
  once whitespace and HTML comments are ignored. A second job checks that the
  repository has an `AGENTS.md` and that `CLAUDE.md`, if present, is exactly
  `@AGENTS.md`, so agent instructions have one home.

To call the check from a repository, add `.github/workflows/pr-description.yml`:

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

The separator is plain text to markdown, so it needs no blank lines around it
and cannot be mistaken for a heading. A hand-typed version still counts: the
check accepts either icon without its arrow, a line of any length, and any
spacing, as long as it reads human icon, line, robot icon.

## Next feature

Not written yet. Each feature this repository enables gets a section like the
one above.
