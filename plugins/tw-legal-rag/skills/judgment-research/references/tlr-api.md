# TLR endpoint reference

Base URL: `https://tlr.dr-lawbot.com` (public, no API key). Optional key via
`TWLEGALRAG_TLR_API_KEY` / `~/.twlegalrag/config.toml` if the operator issues one.

Two access paths to the same backend:

| Path | Auth | Use when |
|---|---|---|
| MCP `https://tlr.dr-lawbot.com/mcp` | OAuth (scope `judgments:read`), one-time | Default. Tools appear natively. |
| REST `POST /v1/...` | none | MCP unauthorized/unavailable, or scripting. |
| CLI `twlegalrag` (`pip install twlegalrag`) | none | Bundling for another AI, citation check. |

The MCP endpoint returns `401 unauthorized` with a `WWW-Authenticate: Bearer` challenge
until authorized. Authorization is interactive — it cannot be completed in a
non-interactive session. Do not ask the user for tokens or callback URLs; tell them to
authorize the `tlr` server via `/mcp` in an interactive session, and use REST meanwhile.

## Tools / endpoints

### searchJudgments — `POST /v1/search`

```json
{"query": "保全業 僱用人 侵權責任", "max_results": 5}
```

`query` 繁中, ≤500 chars. `max_results` 1–10, default 5.

Returns `results[]`: `rank`, `doc_id`, `citation_text`, `court_name`, `jdate`,
`case_category`, `snippet`, `citation_url`, `citation_markdown`, `result_token`.

`snippet` is a **structured summary** — outcome, cited articles, case type. Not reasoning.
`result_token` is required for the fulltext call; carry it forward.

### getJudgmentFulltext — `POST /v1/fulltext`

```json
{"doc_id": "CYDV,103,重訴,10,20140618,1", "result_token": "<from search>"}
```

Returns `citation_text`, `court_name`, `jdate`, `text_excerpt` (reasoning, length-capped),
`cited_articles[]`, `citation_url`, `citation_markdown`.

Required before quoting or paraphrasing any judicial view. Quoted wording must match
`citation_text` for the case identity.

### searchLegalReferences — `POST /v1/legal_references/search`

```json
{"query": "扣繳義務人未依限申報扣繳憑單之處罰", "authority": "財政部",
 "source_kind": "tax_interpretation", "max_results": 5}
```

`query` ≤300 chars. `authority` is an exact filter. `source_kind` ∈
`administrative_interpretation` | `administrative_order` | `tax_interpretation` |
`constitutional_interpretation` | `constitutional_judgment`.

Returns `results[]`: `citation`, `serial_no`, `authority`, `title`, `issue_date`,
`source_kind`, `status`, `score`, `excerpt`; plus `notes[]`.

Candidates only. `score` measures similarity, not relevance or validity.

### getLegalReference — `POST /v1/legal_reference`

```json
{"serial": "台財稅第881945861號", "authority": "財政部"}
```

Serial formatting differences (全/半形, 臺/台, 字第) are normalised server-side.
`authority` only affects ranking.

Returns `found`, `matches[]` (`authority`, `serial_no`, `title`, `issue_date`, `status`,
`superseded_by`, `source_url`, `fulltext`), `notes[]`.

`status`: `repealed` / `ceased` → not current law. `unknown` → unverified, not invalid.

## REST fallback pattern

```bash
curl -sS -X POST https://tlr.dr-lawbot.com/v1/search \
  -H 'Content-Type: application/json' \
  --data-binary '{"query":"勞資 加班費 舉證責任","max_results":5}'
```

For Chinese payloads inside restrictive shells, write the JSON to a file and use
`--data-binary @file.json` rather than inlining it — quoting mangles the characters.

## CLI

```bash
pip install twlegalrag
twlegalrag search "勞資 加班費" -n 5 --read      # listing
twlegalrag pack "車禍對方全責,我可以求償什麼?" -o bundle.json
twlegalrag check bundle.json answer.txt          # bundle-level citation check
twlegalrag health
```

Deps are `httpx` / `typer` / `rich` only — no LLM libraries, no keys. In a sandbox use
`pip install twlegalrag --break-system-packages`.

Source: https://github.com/aa0101181514/tw-legal-rag (MIT). The judgment corpus,
embeddings and retrieval logic are server-side, not in the repo.
