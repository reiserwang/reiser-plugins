---
name: house-style
description: Universal entry point for any styled deliverable — decks, reports, memos, board papers, workbooks. Picks a style template (ANA Blue or Reiser Warm), routes the request to the right tool (deck-design/deck-build for new decks, the officecli skills for editing existing files) and applies the template's palette, type scale and slide grid. Use whenever the user asks for a presentation, deck, report, document, workbook or meeting record, or says "on-brand", "in our style", "for the board" or "for the investor briefing".
---

# house style — entry point

One skill, two jobs: **pick the template**, then **pick the pipeline**. Do neither by feel — a deck built with the wrong tool has to be rebuilt, not patched, and a deliverable in the wrong palette is off-brand, not a stylistic variation.

Read this file, then read exactly one `templates/<name>/TEMPLATE.md`. Everything else is loaded on demand.

## 1. Pick the template

| Template | Field | Accent | Use for |
|---|---|---|---|
| **ANA Blue** — [`templates/ana-blue/`](templates/ana-blue/TEMPLATE.md) | white `#FFFFFF` | deep blue `#0B318F` | Anything going out under the organisation's mark: board, regulator, investor briefing, customer, partner, ESG |
| **Reiser Warm** — [`templates/reiser-warm/`](templates/reiser-warm/TEMPLATE.md) | warm cream `#F5F1ED` | coral `#CC785C` | Personal work, drafts, internal thinking documents, anything that is not brand-facing |

**Never mix them in one file.** Different fields (pure white vs. warm cream) and different accents; the mixture reads as a mistake, not a blend. When the route is genuinely unclear, ask.

Each template folder holds the same four things, so the two are interchangeable at the folder level:

```
templates/<name>/
├── TEMPLATE.md      the layout inventory, standing furniture, and what this template is for
├── palette.md       every token, with verified WCAG ratios
├── theme.json       drop-in theme_overrides for deck-build
└── <name>.pptx      one master, 19 layouts, one blank starter slide — copy this as a starting file
```

Adding a third template means adding a folder with those four files and one row to the table above. See [`templates/README.md`](templates/README.md).

## 2. Pick the pipeline

| What the user wants | Route |
|---|---|
| A **new deck** where the template's layouts fit | `cp templates/<name>/<name>.pptx deck.pptx`, then `pptx-cli`. Fastest path, and the only one that inherits the master and theme. |
| A **new deck** from a brief or source docs, with a bespoke narrative | `deck-design` → `deck-build` with `theme.json` → officecli finish pass ([`references/pipelines.md`](references/pipelines.md) § A) |
| **Edit / restyle / audit an existing** `.pptx` | `pptx-cli` directly. Never rebuild a deck that already exists. |
| A **report, memo, board paper, meeting record** | `docx-cli` ([`references/pipelines.md`](references/pipelines.md) § B) |
| A **financial model, KPI workbook, budget** | `xlsx-cli` |
| "Which layout should this be?" | [`references/layouts.md`](references/layouts.md) — 19 named layouts with exact geometry |

Two routing mistakes account for most wasted work:

- **Rebuilding instead of editing.** If a `.pptx` exists and the ask is "fix / update / restyle", it is `pptx-cli`. `deck-build` writes new files; it does not ingest templates or existing decks.
- **Building before designing.** `deck-build` without a spec produces a card grid with a title on top. Its own documentation says so. Run `deck-design` first — unless you are starting from the template `.pptx`, in which case the layouts *are* the spec.

## 3. Non-negotiables, both templates

**Typeface: Arial** for Latin, **微軟正黑體** for 中文, everywhere, all weights. Never Calibri, never a theme default. Arial carries no CJK glyphs — set both faces or Windows falls back to a serif (新細明體) and the file looks wrong to every reviewer on a PC while looking fine on the Mac it was authored on.

**Canvas: 1440 × 810 pt** (16:9). Margin 56pt, content band `x = 56 → 1384` (width 1328), gutter 16.2pt. Full geometry in [`references/grid.md`](references/grid.md).

**Read, not projected.** The upstream OfficeCLI pptx skill mandates ≥36pt titles — **that rule does not apply here and must be overridden.** These are dense, analyst-style documents reviewed on a laptop or printed. Titles are 30pt on a 1440pt canvas, which is 20pt on a conventional 960pt canvas. The measured scale is in each template's `palette.md`.

**Standing furniture.** Every content slide carries an eyebrow, a title, the rule under it, a footer and a page number. Omitting them is an incomplete deliverable, not a minimal one. Three layouts are deliberate exceptions: **Quote** and **Blank** ship without the eyebrow / title / rule trio, and **Cover** / **Section Divider** / **Closing** carry their own furniture instead.

**Bilingual convention.** Traditional characters (zh-Hant) only, and the two are separated by ` · ` (space-middot-space) or set on a second line. Keep the pairing at eyebrow and section-title level; body copy is single-language, matched to the audience. Board, regulator and investor material is bilingual throughout; internal working documents may be English-only.

Which language leads depends on the slot, and the shipped layouts are the reference:

- **Eyebrows lead with 中文** — `風險 · RISK`, `數據 · DATA`, `專案進度 · PROJECTS`. `AGENDA · 議程` is the one shipped exception, because the English word is the label.
- **Panel headings pair 中文 then English** across an ideographic space — `事件概要　Summary`, `現況　Before`.
- **Cover** sets `{{DECK_TITLE}}　|　{{DECK_TITLE_EN}}` — 中文, ideographic space, pipe, English.
- **Titles and body** are single-language.

Match the slot rather than applying one rule everywhere.

**Contrast is a gate, not a preference.** Each palette has at least one colour that fails as text and is fill-only. Read the template's `palette.md` before setting any coloured text, and [`references/contrast.md`](references/contrast.md) before overriding a checker.

## 4. No content is encoded here

**This skill carries no product, positioning or organisational language, by design.** Product names, service descriptions, SKUs, partner platforms, roadmap claims, taglines, org names and unit names all live in the approved source the organisation maintains — read them from there for every deliverable, and never infer or invent them.

The template `.pptx` files ship with placeholders for exactly this reason:

| Placeholder | Fill with |
|---|---|
| `{{ORG}}` | the organisation name as it appears in the footer |
| `{{UNIT}}` | the issuing department or unit |
| `{{DECK_TITLE}}` / `{{DECK_TITLE_EN}}` | the deliverable's title, 中文 and English |
| `{{CLASSIFICATION}}` | the handling marking, if the deliverable carries one |

Replace every one before delivery. A shipped file containing `{{` is a defect.

Two content failure modes to watch for regardless of the source:

- **Shipping product vs. vision.** Do not describe what the organisation sells today in the language of the roadmap. Forward-looking pillars belong on slides labelled as such.
- **Pillar-specific taglines.** A line written for one pillar does not transfer to a current-product slide.

## 5. Before delivering anything

1. Run the format skill's own verification — `officecli view <file> issues`, `check_deck.py`, `officecli validate`.
2. **Render it and look at it.** `officecli view <file> screenshot --grid --out contact.png`, then read the PNG. Grid drift and text overflow are invisible in the DOM and obvious in an image.
3. Confirm eyebrow, title rule, footer and page number are on every content slide.
4. Confirm no Calibri survived, no off-palette colour crept in, and 中文 has a real CJK face set.
5. `grep` the file for `{{` — no placeholder may ship.
6. Check every product, roadmap and market claim against the approved source. This skill does not carry one.
7. `officecli close <file>` before `SendUserFile` or `device_commit_files` — otherwise you deliver the pre-edit version.
8. Flag anything you could not verify rather than presenting it as done.

## References

- [`references/grid.md`](references/grid.md) — canvas, margins, the column arithmetic, vertical rhythm, unit conversions to `deck-build`
- [`references/layouts.md`](references/layouts.md) — all 19 layouts, every shape, exact coordinates
- [`references/pipelines.md`](references/pipelines.md) — the `deck-design` → `deck-build` pipeline, and the Word / Excel path
- [`references/contrast.md`](references/contrast.md) — the contrast gate, verified ratios, the recompute snippet
- Sibling skills: `pptx-cli`, `docx-cli`, `xlsx-cli`, `officecli-setup`
