"""Check a repo's agent-instruction files.

AGENTS.md must exist at the repo root. CLAUDE.md, if present, must be exactly
the line `@AGENTS.md` so that AGENTS.md stays the single source of agent
instructions. Exit 1 with one reason per line otherwise.
"""

from __future__ import annotations

import sys
from pathlib import Path

STANZA = """## Pull request descriptions

A PR body has a human-written summary above the line `AI Generated Below`
and an agent-written section below it. Put everything you write, including
your summary of the change, below the line. Never edit text above it. If you
open the PR, leave the human part empty; do not draft it. Leave a blank line
before the `---` that precedes the marker.
"""

CLAUDE_MD = "@AGENTS.md"


def check(root: Path) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    agents = root / "AGENTS.md"
    if not agents.is_file():
        reasons.append(
            "AGENTS.md is missing. Create it at the repo root with at least this section:\n\n"
            + STANZA
        )
    claude = root / "CLAUDE.md"
    if claude.is_file() and claude.read_text().strip() != CLAUDE_MD:
        reasons.append(
            f"CLAUDE.md must contain only the line `{CLAUDE_MD}`; "
            "move its other content into AGENTS.md"
        )
    return not reasons, reasons


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    ok, reasons = check(root)
    for reason in reasons:
        print(reason)
        print()
    if ok:
        print("ok: AGENTS.md present" + (", CLAUDE.md imports it" if (root / "CLAUDE.md").is_file() else ""))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
