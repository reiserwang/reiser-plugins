# ANA Blue

The brand-facing template. White field, deep blue accent, dense analyst-style pages.

**Use for** anything going out under the organisation's mark: board papers, regulator submissions, investor briefings, customer and partner decks, ESG material.
**Do not use for** personal drafts or internal thinking documents — that is [`reiser-warm`](../reiser-warm/TEMPLATE.md). Never mix the two in one file.

| | |
|---|---|
| File | [`ana-blue.pptx`](ana-blue.pptx) — 1 master, 19 layouts, 1 blank starter slide |
| Theme name | `ANA Blue` |
| Canvas | 1440 × 810 pt |
| Field | `#FFFFFF` on the master. Four layouts override it: Cover / Section Divider / Closing on `#0B318F`, Quote on `#F0F6FC`. |
| Accent | `#0B318F` |
| deck-build override | [`theme.json`](theme.json) |
| Tokens and ratios | [`palette.md`](palette.md) |

## Start here

```bash
cp ana-blue.pptx deck.pptx
officecli open deck.pptx
officecli add deck.pptx slide --layout 'Cover'
```

The 19 layouts, their placeholder indices and exact geometry are in [`../../references/layouts.md`](../../references/layouts.md). The grid is in [`../../references/grid.md`](../../references/grid.md).

## Type scale

Arial for Latin, 微軟正黑體 for 中文. Bold is the only weight variation — no italics, no letter-spacing tricks, no all-caps runs longer than three words.

| Element | Size | Weight | Colour |
|---|---|---|---|
| Cover title | 40pt | bold | `#FFFFFF` |
| Section / Closing title | 34pt | bold | `#FFFFFF` |
| Slide title | 30pt | bold | `#1A2230` |
| Quote opening glyph | 130pt | bold | `#0B318F` |
| Quote body | 28pt | regular | `#1A2230` |
| Big Number | 96pt | bold | `#0B318F` |
| KPI value | 54pt | bold | `#0B318F` |
| Eyebrow | 20pt | bold | `#0B318F` |
| Cover subtitle · takeaway · rationale | 21pt | regular | `#1A2230` / `#FFFFFF` |
| Panel heading, table header | 18pt | bold | `#0B318F`, or `#FFFFFF` on an accent band |
| Body — the workhorse | 18pt | regular | `#1A2230` body, `#5A6676` supporting |
| Footer, page number, source line | 13pt | regular | `#5A6676` |

These are sizes on a **1440pt** canvas. On a conventional 960pt canvas they are 2/3 of these numbers — a 30pt title here is a 20pt title there. The upstream OfficeCLI pptx skill's ≥36pt title rule assumes a projected 960pt deck and **does not apply**: override it.

## Standing furniture

Fourteen of the nineteen layouts carry all five. Omitting any of them on those layouts is an incomplete deliverable; the five exceptions are listed below.

| Element | Position | Spec |
|---|---|---|
| Eyebrow | `56, 48` | 20pt bold `#0B318F`, bilingual, ` · `-separated. The shipped eyebrows lead with 中文 — `風險 · RISK`, `數據 · DATA` — except `AGENDA · 議程`. |
| Title | `56, 76` | 30pt bold `#1A2230` |
| Title rule | `56, 142`, `1328 × 1.5` | filled rectangle, `#0B318F` |
| Footer | `56, 772` | 13pt `#5A6676` — `{{ORG}}  \|  {{DECK_TITLE}}` |
| Page number | `1324, 772` | 13pt `#5A6676`, right-aligned |

Three layouts substitute their own furniture: **Cover**, **Section Divider** and **Closing** are full-bleed `#0B318F` with reverse-ink text; Cover and Section Divider carry a short `#FFFFFF` underline rule (`120 × 3` and `100 × 3`), Closing carries none, and the classification marking appears on Cover only. Two more ship deliberately bare: **Quote** (panel-tint `#F0F6FC` field, footer and page number only) and **Blank** (title rule, footer and page number only).

## The fill-only colour

**Sky `#00A3E6` is a fill colour, not a text colour.** 2.84:1 on white — it fails the gate at every size. Correct for chart series, rules, icon badges, category spines and panel accents; wrong for eyebrows, labels and any small text. Substitute `#0B318F` (11.35:1), or `#00719E` (5.45:1) when the sky hue itself is the point.

The template's own eyebrows are `#0B318F` for exactly this reason. Source decks that set 14pt sky eyebrows on white would be flagged — do not copy that pattern forward.

Full ratio table: [`palette.md`](palette.md) and [`../../references/contrast.md`](../../references/contrast.md).

## Placeholders to replace

`{{ORG}}` · `{{UNIT}}` · `{{DECK_TITLE}}` · `{{DECK_TITLE_EN}}` · `{{CLASSIFICATION}}`

Take the values from the approved source the organisation maintains. This template encodes no organisational, product or positioning language by design. A delivered file containing `{{` is a defect.

## Before delivering

1. `officecli view deck.pptx issues`
2. `officecli view deck.pptx screenshot --grid --out contact.png`, then read the PNG
3. Eyebrow, title rule, footer, page number on every content slide
4. No Calibri, no off-palette colour, `font.ea` set for any 中文
5. `grep -c '{{' ` → 0
6. `officecli close deck.pptx` before delivery
