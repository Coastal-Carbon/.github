"""Check that a PR body has a human-written summary above the marker line.

Reads the body from the PR_BODY environment variable. Exit 1 with one reason
per line when the body does not follow the convention. Bot-authored PRs are
skipped because no human author exists to write the summary.
"""

from __future__ import annotations

import argparse
import os
import re
import sys

MARKER = "AI Generated Below"
_HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
_RULE_LINE = re.compile(r"^\s*-{3,}\s*$", re.M)  # the horizontal rule above the marker


def check(body: str | None, author_type: str) -> tuple[bool, list[str]]:
    if author_type == "Bot":
        return True, ["skipped: bot author"]
    lines = (body or "").splitlines()
    marker_lines = [i for i, line in enumerate(lines) if line.strip() == MARKER]
    if len(marker_lines) != 1:
        return False, [
            f"expected the marker line '{MARKER}' exactly once, found {len(marker_lines)}"
        ]
    above = "\n".join(lines[: marker_lines[0]])
    text = _RULE_LINE.sub("", _HTML_COMMENT.sub("", above))
    if not text.strip():
        return False, ["the human-written summary above the marker is empty"]
    return True, []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--author-type", default="User", help="GitHub user type of the PR author")
    args = parser.parse_args()
    ok, reasons = check(os.environ.get("PR_BODY"), args.author_type)
    for reason in reasons:
        print(reason)
    if ok:
        print("ok: human summary present above the marker" if not reasons else "ok")
        return 0
    print()
    print("A PR description is a human-written summary, a blank line, then:")
    print()
    print("---")
    print(MARKER)
    print()
    print("followed by anything the agent wrote. Edit the description and the check re-runs.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
