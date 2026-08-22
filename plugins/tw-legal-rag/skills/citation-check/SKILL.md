---
name: citation-check
description: Package Taiwan judgments into a portable bundle for another AI, and audit an AI-generated legal answer's citations against that bundle. Use when the user wants to hand judgment research to ChatGPT/Gemini/another model, asks to verify or 查核 the citations in a legal answer, suspects a case number was fabricated (幻覺/捏造), or asks whether an answer's quotes actually come from the cited judgments.
---

# Bundle and citation check

Two jobs: build a portable evidence bundle from TLR retrieval, and audit an answer's
citations against that bundle. Both run through the `twlegalrag` CLI — deterministic
string analysis, no LLM, no database access.

## Setup

```bash
pip install twlegalrag          # add --break-system-packages in a sandbox
twlegalrag health               # confirm the endpoint responds
```

## Build a bundle

```bash
twlegalrag pack "車禍對方全責,我可以求償什麼?" -o bundle.json
```

Query must be Traditional Chinese. The bundle carries `query`, and per judgment
`citation_id` (J1, J2, …), `citation_text`, `citation_url`, `doc_id`, the Layer-1
listing, `fulltext_excerpt`, plus `allowed_citations` and `verification_instructions`
that tell the downstream model to cite only what is inside the bundle and to flag
unsupported propositions as unverified.

Hand the user `bundle.json` with one instruction to pass along: cite only bundle
judgments, mark anything else unverified.

## Audit an answer

```bash
twlegalrag check bundle.json answer.txt
```

Verdicts are `pass` / `needs_review` / `fail`, deliberately conservative — ambiguity
returns `needs_review` rather than `fail` to hold false positives down.

## Report the verdict honestly

This is the part that matters. State plainly what the check covers.

**It verifies:**

- every case number cited in the answer belongs to the bundle — catching citations to
  judgments outside it, or to judgments that do not exist;
- that a verbatim quote appears **somewhere** in the bundle text.

**It cannot verify:**

- that a quote came from *the specific judgment the answer attributes it to* — existence
  is checked bundle-wide, not per document;
- that the court's holding was read correctly;
- that a party's argument (原告/被告/上訴人主張) was not mistaken for the court's view;
- that dicta were not presented as controlling authority;
- paraphrase-level distortion of a holding.

A `pass` therefore means **"the cited case numbers match bundle identities"** — not that
the legal reasoning is sound, and not that each quote came from the judgment named.
Never report `pass` as "the answer is verified" or "citations are correct". Say what was
actually checked, then point the user at the judgment texts.

Scope is also limited to the bundle as packed. If the user later opened a full judgment
and rewrote the answer from it, `check` still only sees the original excerpts.

## Caveat on the vendored code

`twlegalrag/faithful/` is a snapshot of internal code and contains functions the CLI
never calls (e.g. `check_party_as_court`, `run_all_checks`). Their presence does **not**
mean semantic or holding-level verification is available — the CLI uses two
bundle-level checks only. Do not read the file listing as a feature list, and do not
promise the user checks the CLI does not perform.

## Retrieval

To gather the judgments in the first place, or to work interactively rather than via
bundles, use the `judgment-research` skill in this plugin.
