from scripts.check_agent_files import STANZA, check


def test_missing_agents_md_fails_and_prints_stanza(tmp_path):
    ok, reasons = check(tmp_path)
    assert not ok
    assert "## Pull request descriptions" in "\n".join(reasons)
    assert STANZA in "\n".join(reasons)


def test_claude_md_import_only_passes(tmp_path):
    (tmp_path / "AGENTS.md").write_text("# x\n")
    (tmp_path / "CLAUDE.md").write_text("@AGENTS.md\n")
    assert check(tmp_path) == (True, [])


def test_claude_md_crlf_passes(tmp_path):
    (tmp_path / "AGENTS.md").write_text("# x\n")
    (tmp_path / "CLAUDE.md").write_bytes(b"@AGENTS.md\r\n")
    assert check(tmp_path) == (True, [])


def test_claude_md_with_extra_content_fails(tmp_path):
    (tmp_path / "AGENTS.md").write_text("# x\n")
    (tmp_path / "CLAUDE.md").write_text("@AGENTS.md\n# more\n")
    ok, reasons = check(tmp_path)
    assert not ok and "CLAUDE.md" in reasons[0]


def test_no_claude_md_passes(tmp_path):
    (tmp_path / "AGENTS.md").write_text("# x\n")
    assert check(tmp_path) == (True, [])
