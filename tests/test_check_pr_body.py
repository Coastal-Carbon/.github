from scripts.check_pr_body import MARKER, check


def test_passes_with_summary_above_marker():
    assert check(f"Fixed the thing.\n{MARKER}\ndetails", "User") == (True, [])


def test_fails_when_marker_missing():
    ok, reasons = check("Fixed the thing.", "User")
    assert not ok and "separator" in reasons[0]


def test_fails_when_marker_twice():
    ok, reasons = check(f"x\n{MARKER}\n{MARKER}", "User")
    assert not ok and "2" in reasons[0]


def test_fails_when_only_template_comment_above():
    body = f"<!-- Written by you.\n  multi-line -->\n\n{MARKER}\n\nagent"
    ok, reasons = check(body, "User")
    assert not ok and "empty" in reasons[0]


def test_fails_on_none_body():
    ok, _ = check(None, "User")
    assert not ok


def test_marker_in_code_block_still_counts():
    ok, _ = check(f"x\n```\n{MARKER}\n```\n\n{MARKER}\n", "User")
    assert not ok


def test_bot_author_skips():
    assert check(None, "Bot") == (True, ["skipped: bot author"])


def test_hand_typed_separator_variants_count():
    for sep in ("🙂 ──── 🤖", "🙂↑──↓🤖", "  🙂 ⬆️ ─ ⬇️ 🤖  "):
        assert check(f"summary\n{sep}\nagent", "User") == (True, []), sep


def test_icons_alone_without_line_do_not_count():
    ok, _ = check("summary\n🙂 🤖\nagent", "User")
    assert not ok
