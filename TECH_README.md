# Books — Technical Specification & Governance

## 1. Architectural Intent
`Books` is a purely document-oriented repository within the `Author` suite. It strictly excludes website frontends, static site generators, and web runtimes.

- **Frontend/Site**: None (`site_enabled: false`).
- **Primary Data Type**: UTF-8 Markdown and Plain Text.
- **Root MCP Server**: `author-mcp` (Priority 1).
- **Control Plane**: Air Traffic Control (ATC) in `../mcp`.

## 2. Hath0r Integration
- **Framework**: HATHOR Agentic Architecture v1.0.
- **Cognitive Substrate**: KnowledgeGraph, ContextGraph, MemoryGraph under `.hath0r/`.
- **MCP Provider**: Local `author-mcp` on `http://127.0.0.1:18083/mcp`.

## 3. Verification & Testing
```sh
pytest tests/
hath0r preflight
```
