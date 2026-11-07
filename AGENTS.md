# AGENTS.md — Books

> Role: **Books** · Member of Enterprise Agentic Platform

## CR-CONTEXT-SQUEEZE-001: Compress Context with SuperSqueeze (CRITICAL — Org-Wide · CANONICAL)

1. **Squeeze before you load**: Bulky context (whole files, logs, CI/tool output, KB/RAG hits, transcripts, anything over ~2,000 tokens) MUST go through SuperSqueeze before it enters an agent's context or a prompt: `hath0r squeeze -q "<active query>" -f <file>` (or `-c "<text>"`), or `SuperSqueezeBot` in code. No hand-rolled truncation.
2. **Anchor on the active query** and re-squeeze when the query changes.
3. **Quality floor**: if `verifier.quality_score` < 0.90, lower `--threshold` or switch to targeted reads (line ranges, `grep`, `hath0r code`); never dump the whole source.
4. **Local-first**: use `--local` for sensitive content; never squeeze secrets.
5. **Exact-text exceptions**: code being edited, diffs under review, quoted legal text and fixtures are read verbatim with targeted reads.
6. **Pipelines route through SuperSqueeze** (`CAGEngine.pack_context()`, `HybridCAGRAGRouter`, HAHP envelopes, MCP responses); audited by `SubstrateUtilizationBot` and the Tier 2 eval.

Canonical: [HATH0R-CLI `docs/governance/rules/cr-context-squeeze-001.md`](https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/rules/cr-context-squeeze-001.md).

## CR-CLI-ENTRY-001: Start with the CLI (CRITICAL — Org-Wide)

1. **Start with the CLI (CRITICAL ENTRY GATE)**: When receiving ANY request or starting any task, agents **MUST ALWAYS START WITH THE OPERATOR CLI (`hath0r`)** rather than inventing ad-hoc scripts.
2. **Missing Capability Offer**: If the required connection, MCP, workflow, bot, or factory does not exist in `hath0r`, offer to register the missing capability.
3. **Docs before code**: Require procedure/playbook/runbook before scaffolding implementation.

---

## Author MCP Knowledge Protocol (cr-author-mcp-001)

1. **Always Check Hath0r CLI First**: All agent reasoning and document exploration MUST query through `hath0r` CLI first:
   - Check connection health: `hath0r mcp check`
   - List configured MCP servers: `hath0r mcp list`
   - Verify server status: `hath0r atc status`
2. **Leverage Author MCP for Knowledge Retrieval**: All knowledge, character, lore, outline, and chapter lookups MUST query through the Author MCP via Hath0r CLI:
   - Search knowledge: `hath0r mcp call author-mcp search_author_knowledge --args '{"query": "<query>", "limit": 5}'`
   - Fetch document content: `hath0r mcp call author-mcp get_author_document --args '{"doc_id": "<path-or-id>"}'`
   - Search canonical FTS5 index: `hath0r kb search -q "<term>" --fts-only`
3. **MCP Connection Access**: The Hath0r framework maintains direct active connection to `author-mcp` (Priority 1 Root MCP) on port `18083` via `.hath0r/mcp.json`.
4. **Preserve Original Manuscripts**: Original manuscript drafts in `manuscripts/` and idea notes in `ideas/` are strictly immutable source artifacts. NEVER modify or delete source `.docx` or original manuscript files.
5. **Site-Free Policy**: Books is strictly text documents, codices, and manuscripts. NO web application or static site may be generated in this repository.

---

## Promotion Path (CR-BAI-001)

```text
local → development → testing → staging → master (Production)
```

## Branch Governance (cr-branch-gov-001)

- Issue first: create an issue before cutting a branch.
- Naming: `feature|bugfix|enhancement|chore/<issue-number>-slug`
- Base PR target: `development`

## AgentGraph Substrate

This repository is governed by the Hath0r AgentGraph substrate. Dynamic rule retrieval, role RBAC, and policy graphs are stored under `.hath0r/agentgraph/`.
- Query status: `hath0r agentgraph status`
- Query rules: `hath0r agentgraph query "<topic>"`
- Route role: `hath0r agentgraph route --role <role>`
- Validate rules: `hath0r agentgraph validate`

## Hyper Context Pointers
- **Contracts Subsystem**: `/Users/raybayly/Development/Projects/Author/Books/contracts/AGENTS.md`
- **Docs Subsystem**: `/Users/raybayly/Development/Projects/Author/Books/docs/AGENTS.md`
- **Tests Subsystem**: `/Users/raybayly/Development/Projects/Author/Books/tests/AGENTS.md`
- **Cfg Subsystem**: `/Users/raybayly/Development/Projects/Author/Books/cfg/AGENTS.md`

---

## CR-SONAR-PREANNOUNCE-001 (SonarCloud Thresholds Before Announcing Complete — CANONICAL)
- **Pre-Announcement SonarCloud Gate**: Before announcing any work as Complete, the agent MUST analyze the code and confirm it meets this repository's SonarCloud Quality Gate thresholds (coverage on new code, duplication, reliability, security, maintainability, and security hotspots reviewed).
- **How to Verify**: Use `hath0r quality sonar` (project key from `sonar-project.properties`) together with local test and coverage runs. If the gate cannot be checked, state that plainly instead of announcing Complete.
- **Not Complete Until Green**: A failing or unverified Quality Gate means the work is not Complete.

---

## CR-SEMVER-BUMP-001 (Semantic Version Bump on Every PR — CANONICAL)
- Every pull request that is created and merged must create or bump this product's Semantic Version (`MAJOR.MINOR.PATCH`, https://semver.org). The root `VERSION` file is the source of truth; keep `VERSION` and `CHANGELOG.md` in step with it.
- Pick the bump by impact: MAJOR for breaking changes, MINOR for backward-compatible features, PATCH for fixes, docs, chores and everything else. `Version Impact: none` is not allowed.
- New products start at `0.1.0`.
- Declare the bump in the PR body as `Version Impact: patch|minor|major` and add a matching `CHANGELOG.md` entry. Verify with `hath0r release validate` before announcing complete.
- A PR merged without a version bump is not Complete.

---

## CR-TASK-EVAL-001 (Automatic Task Evaluation Before Announcing Complete — CRITICAL · CANONICAL)
- **Mandatory Pre-Announcement Task Evaluation Gate**: Every task MUST be evaluated across the 4-tier hybrid evaluation pipeline (Tier 1 Deterministic Rubrics, Tier 2 Trajectory & FinOps Efficiency, Tier 3 Adversarial & Diff Critics, Tier 4 Goal Alignment & Consensus) prior to announcing work as Complete.
- **Composite Reward Threshold**: Task completion requires `passed_gate: true` and composite reward score `R_task >= 0.80` persisted in `.hath0r/evals/latest.json` and compounded as an `eval:<task_id>` node in `.hath0r/memory/graph.json`.
- **How to Verify**: Run `hath0r evals run` and `hath0r evals verify` before announcing Complete (`EndOfTaskBot`, `TaskAnnouncerBot.announce_complete`, and `CleanReposWorkflowBot` enforce this gate automatically).
- **Mandatory Eval Scorecard Summary After Every Task (CRITICAL · CANONICAL)**: Immediately after running task evaluations (`hath0r evals run`), the agent MUST always return a structured summary of the **Eval Scorecard** (`eval_id`, `task_id`, `passed_gate`, composite `R_task`, Tier 1–4 scores, and `.hath0r/evals/latest.json` path) in its completion response to the user.
- **Not Complete Until Evaluated & Scorecard Returned**: A missing, failing, unverified, or unreported task evaluation scorecard means the work is not Complete.
