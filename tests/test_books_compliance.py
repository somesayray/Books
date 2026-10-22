"""Compliance and integrity tests for Books repository."""

import json
from pathlib import Path


def test_no_site_directory_exists():
    """Verify strictly: There is no site for Books, only text documents."""
    repo_root = Path(__file__).resolve().parent.parent
    site_dir = repo_root / "site"
    assert not site_dir.exists(), "Books repository MUST NOT contain a 'site' directory. Text documents only."


def test_root_mcp_is_author_mcp():
    """Verify that author-mcp is the root/Priority 1 MCP server."""
    repo_root = Path(__file__).resolve().parent.parent
    mcp_json = repo_root / ".hath0r" / "mcp.json"
    assert mcp_json.exists(), ".hath0r/mcp.json must exist"
    data = json.loads(mcp_json.read_text(encoding="utf-8"))
    assert data.get("default_server") == "author-mcp"
    servers = data.get("servers", [])
    prio_1 = next((s for s in servers if s.get("priority") == 1), None)
    assert prio_1 is not None
    assert prio_1.get("id") == "author-mcp"


def test_manuscripts_are_valid_text():
    """Verify manuscripts and text document directories contain valid UTF-8 text."""
    repo_root = Path(__file__).resolve().parent.parent
    for folder in ["manuscripts", "characters", "worldbuilding", "outlines"]:
        target_dir = repo_root / folder
        if target_dir.exists():
            for f in target_dir.glob("*.md"):
                content = f.read_text(encoding="utf-8")
                assert len(content.strip()) > 0
