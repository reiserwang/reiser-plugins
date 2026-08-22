---
name: judgment-research
description: Research Taiwan court judgments and administrative interpretations through the TLR semantic retrieval endpoint. Use when the user asks what Taiwanese courts have held on an issue, asks for 判決/裁判/案例/實務見解 on a topic, names a case number (e.g. 台上字第123號) or a 函釋 serial (e.g. 台財稅第881945861號), or asks whether an interpretation is still in force. Also use for Taiwan-law questions about 民法, 勞基法, 個資法, 保全業法, 消保法 and similar where court practice matters.
---

# Taiwan judgment research

Retrieve Taiwan court judgments and administrative interpretations, then answer **only** from what was retrieved. This is a retrieval workflow, not a legal-advice workflow — the user reads the judgments and decides.

## Tools

Preferred: the `tlr` MCP server bundled with this plugin — `searchJudgments`, `getJudgmentFulltext`, `searchLegalReferences`, `getLegalReference`.

The MCP endpoint requires a one-time OAuth authorization. If its tools are unavailable or unauthorized, fall back to the key-free REST endpoints or the `twlegalrag` CLI — see `references/tlr-api.md` for exact request shapes and the fallback commands.

## Workflow — judgments

1. **Query in Traditional Chinese.** The index is 繁體中文; an English query degrades retrieval badly. Translate the user's issue into legal Chinese terms first (e.g. "security guard employer liability" → 「保全業 僱用人 侵權責任 民法188」). State the query used.
2. **Search** with `searchJudgments` (`max_results` 1–10, default 5). Results are *structured listings only* — court, case number, outcome, cited articles, case type. They contain **no judicial reasoning**.
3. **Read full text before characterising any holding.** Call `getJudgmentFulltext` with that result's `doc_id` **and** `result_token` for at least the 1–2 most relevant judgments. Never describe what a court "held", "found", or "reasoned" from a search snippet alone.
4. **Answer from the excerpts**, quoting verbatim where you attribute a view to a court.
5. **Cite by emitting the `citation_markdown` string exactly as returned** — `[字號](url)`. Never write a bare case number, never a naked URL, never a reconstructed link.
6. **Say so when nothing relevant comes back.** No result is a finding. Fabricating a plausible-looking 字號 is the single worst failure mode here.

## Workflow — administrative interpretations (函釋)

`searchLegalReferences` returns **semantic candidates, not verified answers**. A high score means neither relevant nor in force.

1. Read each `excerpt` and judge relevance yourself.
2. Verify any candidate you intend to cite with `getLegalReference` using its `serial_no` — this returns full text and effect status.
3. Respect `status`: `repealed` / `ceased` must never be cited as current law; `unknown` means unverified, not invalid. Report the status alongside the citation.
4. Never mix 函釋 into a list of judgments, and never present agency material as a court's view — they are different sources of authority.
5. Absence from this database is not proof a 函釋 does not exist; the corpus is not exhaustive. Never tell the user their case number or serial is fabricated merely because a lookup came back empty.

## Hard rules

- Attribute a holding only to a judgment whose full text you actually read in this session.
- Distinguish 法院見解 from 當事人主張 (原告/被告/上訴人 arguments) — the parties' claims appear in the same document and are not the court's view.
- Distinguish 附帶論述 from the ratio; do not present dicta as controlling authority.
- Mark anything the retrieved text does not support as **unverified** rather than smoothing it into the answer.
- Close substantive answers with a short note: this is retrieval-assisted analysis, not legal advice, and the cited judgments should be read in full.

## Privacy

Query text goes to `tlr.dr-lawbot.com`, which may log the query string, timestamp, IP-derived metadata and result counts. Do not send client secrets, personal data, or confidential case facts — abstract the question to its legal issue first. Tell the user when you have had to abstract their facts to do this.

## Bundling for another AI

When the user wants the results handed to a different model, or wants an answer's citations audited, use the `citation-check` skill in this plugin — it covers `twlegalrag pack` / `check` and, importantly, what that check does and does not prove.
