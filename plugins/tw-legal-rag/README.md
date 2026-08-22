# tw-legal-rag

Taiwan legal research for Claude: semantic retrieval over ~22M Taiwan court judgments
plus administrative interpretations (函釋), with strict citation discipline and a
bundle-level citation check.

Retrieval only. Nothing here generates legal advice or endorses a model's output — the
answer comes from Claude reading the retrieved judgments, and the user reads them too.

Wraps the open-source [tw-legal-rag](https://github.com/aa0101181514/tw-legal-rag) CLI
and the TLR endpoint behind it (`https://tlr.dr-lawbot.com`).

## What you get

| Skill | Use for |
|---|---|
| `judgment-research` | "What have Taiwanese courts held on…", a case number lookup, a 函釋 serial, or checking whether an interpretation is still in force. |
| `citation-check` | Packaging judgments for another AI, or auditing an answer's citations for fabricated case numbers. |

Both are pulled in automatically when a request matches; no slash command needed.

## Setup

**MCP server (default path).** The plugin registers `tlr` →
`https://tlr.dr-lawbot.com/mcp`. It requires a one-time OAuth authorization
(scope `judgments:read`) — approve it via `/mcp` in an interactive session. Until then
the endpoint answers `401`.

**CLI (optional, for bundles and citation checks).**

```bash
pip install twlegalrag
twlegalrag health
```

`httpx` / `typer` / `rich` only. No LLM libraries, no API key.

**Key-free REST fallback.** `POST https://tlr.dr-lawbot.com/v1/search` and friends need
no auth at all — used automatically when the MCP server is not yet authorized.

## How the workflow is constrained

Search returns structured listings — court, case number, outcome, cited articles — and
**no judicial reasoning**. So the skills require reading full text via
`getJudgmentFulltext` before any holding is described, and require citations to be
emitted as the server's own `citation_markdown` string rather than a hand-written case
number. Empty results are reported as empty, never filled in.

Administrative interpretations get a second gate: `searchLegalReferences` returns
similarity candidates, so anything cited must first be verified with `getLegalReference`
for existence and effect status (`repealed` / `ceased` / `unknown`).

## What the citation check proves

`twlegalrag check` confirms that cited case numbers belong to the bundle and that a
quoted string exists somewhere in the bundle text. It does **not** confirm the quote came
from the judgment it is attributed to, that the holding was read correctly, that a
party's argument was not mistaken for the court's view, or that dicta were not passed off
as authority. `pass` means "citation identities line up" — nothing more. The
`citation-check` skill is written to report it that way.

## Privacy

Query text reaches `tlr.dr-lawbot.com`, which may log the query string, timestamp,
IP-derived metadata and result counts for retrieval-quality analysis. Queries are not
used to train generative models. Do not submit client secrets or confidential case
facts — abstract the question to its legal issue first.

Optional API key, if the operator issues one:

```bash
export TWLEGALRAG_TLR_BASE_URL=https://tlr.dr-lawbot.com
export TWLEGALRAG_TLR_API_KEY=...
```

Or `~/.twlegalrag/config.toml`. Never commit it.

## Disclaimer

An analysis aid, not legal advice and not a lawyer. Read the cited judgments in full.
Judgments retrieved are Taiwan public court records; you are responsible for your use of
them.

Upstream CLI: MIT.
