from scripts.check_pr_body import check


def test_passes_with_summary_above_marker():
    assert check("Fixed the thing.\n\n---\nAI Generated Below\n\ndetails", "User") == (True, [])


def test_fails_when_marker_missing():
    ok, reasons = check("Fixed the thing.", "User")
    assert not ok and "marker" in reasons[0]


def test_fails_when_marker_twice():
    ok, reasons = check("x\n\nAI Generated Below\nAI Generated Below", "User")
    assert not ok and "2" in reasons[0]


def test_fails_when_only_template_comment_above():
    body = "<!-- Written by you.\n  multi-line -->\n\n---\nAI Generated Below\n\nagent"
    ok, reasons = check(body, "User")
    assert not ok and "empty" in reasons[0]


def test_fails_on_none_body():
    ok, _ = check(None, "User")
    assert not ok


def test_marker_in_code_block_still_counts():
    ok, _ = check("x\n```\nAI Generated Below\n```\n\n---\nAI Generated Below\n", "User")
    assert not ok


def test_bot_author_skips():
    assert check(None, "Bot") == (True, ["skipped: bot author"])


def test_rule_line_alone_is_not_a_summary():
    ok, reasons = check("\n---\nAI Generated Below\n\nagent", "User")
    assert not ok and "empty" in reasons[0]
