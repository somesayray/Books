# Books

**Author Text Documents & Manuscript Library**

> Technical Reference: See [TECH_README.md](TECH_README.md) for repository architecture and Hath0r alignment.

---

## Overview

The `Books` repository contains text manuscripts, chapter drafts, outlines, lore bibles, and character dossiers for Ray Bayly's literary works.

> **CRITICAL RULE**: There is NO site or web application for Books. This repository contains only text documents.

- 📖 **Text Documents Only**: Pure markdown, text drafts, and lore documentation.
- 🗼 **Orchestrated by ATC**: Managed and observed by the Author Air Traffic Control (`mcp`).
- 🧠 **Root MCP Integration**: Indexed and served via `Author-MCP` (`http://127.0.0.1:18083`) for agent knowledge sharing and retrieval.

---

## Directory Structure

```text
Books/
├── manuscripts/       # Story drafts, chapters, and complete manuscripts
├── characters/        # Character dossiers, relationships, and voice profiles
├── worldbuilding/     # Lore bibles, faction codices, and setting rules
├── outlines/          # Chapter synopses, story arcs, and series structures
├── notes/             # Ideation memos, research notes, and editorial feedback
├── docs/              # Governance and operational documents
└── tests/             # Integrity and compliance tests
```

---

## Quick Start with Hath0r

```sh
# Verify repository health with Hath0r CLI
hath0r doctor

# Verify compliance tests
pytest tests/
```

---

## License

Apache License 2.0
