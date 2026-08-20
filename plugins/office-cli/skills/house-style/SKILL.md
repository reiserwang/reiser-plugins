---
name: house-style
description: Corporate house style — Corporate Blue palette, Arial typography scale, bilingual EN·中文 conventions and layout grid. Load before producing any brand-compliant deck, report, memo, or workbook, and whenever the user asks for something "on-brand", "in our style" or "for the board".
---
> Routed here by `corp-deliverable`. If you arrived directly and the task might involve a **new deck**, check `corp-deliverable` first — new decks go through `deck-design` → `deck-build`, not through this skill.


# house style

Apply to every brand-facing deliverable. Values below were extracted from the live corporate decks (`corporate_master_deck.pptx`, `reference_architecture.pptx`), not invented — treat them as the source of truth.

Load `references/palette.md` for the full token table and `references/slide-grid.md` for exact geometry and copy-paste officecli recipes.

## Non-negotiables

**Typeface: Arial.** Latin and 中文, everywhere, all weights. Futura Medium appears only inside the locked corporate wordmark artwork — never set live text in it. Never Calibri, never a theme default.

**Canvas: 960 × 540 pt** (16:9). Content band `x = 37.4 → 918`. Base spacing unit **10.8pt**; all offsets are multiples of it.

**Core palette:**

| Role | Hex |
|---|---|
| Deep blue (primary) | `#0B318F` |
| Sky (accent, eyebrows, links) | `#00A3E6` |
| Panel tint | `#F0F6FC` |
| Callout tint | `#E6F2FC` |
| Headline ink | `#1A2230` |
| Body / muted ink | `#5A6676` |
| Background | `#FFFFFF` |

Never introduce a color outside `references/palette.md`. Charts draw from the categorical ramp there, in order.

**These decks are read, not projected.** The upstream OfficeCLI pptx skill mandates ≥36pt titles — **that rule does not apply here and must be overridden.** house decks are dense, analyst-style documents reviewed on a laptop or printed. The real scale:

| Element | Size | Weight | Color |
|---|---|---|---|
| Page tagline / hero | 24pt | regular | `#1A2230` |
| Section title | 19–22pt | bold | `#0B318F` or `#1A2230` |
| Eyebrow (above content) | 14pt | bold | `#00A3E6` |
| Card / block title | 16–16.5pt | bold | `#0B318F` |
| Body | 11.5–12.5pt | regular | `#5A6676` |
| Callout band | 14.5pt | lead-in bold | `#0B318F` + `#1A2230` |
| Caption / footer | 9–10.5pt | regular | `#5A6676` |

## Standing slide furniture

Every content slide carries these. Omitting them is an incomplete deliverable.

- **Wordmark** top-left at `x=20.3, y=26.4, w=432.6, h=59.7` (reuse the picture from an existing deck; do not redraw it).
- **Tagline** top-right at `x=467.3, y=26.4`, 24pt — one lowercase line, e.g. `next-generation resilient security, on a smart cloud`.
- **Eyebrow** at `x=42.5, y=123.0`, 14pt bold `#00A3E6` — bilingual, ` · `-separated: `<English tagline>  ·  <中文標語>`.
- **Footer** at `x=43.2, y=509.8`, 9pt `#5A6676`: `<Company>   |   <deck title>`.
- **Page number** at `x=874.8, y=509.8`, 9pt `#5A6676`, right-aligned.

## Bilingual convention

English leads, 中文 follows, separated by ` · ` (space-middot-space) or on a second line. Traditional characters only — this is a Taiwan-market company. Keep the pairing at eyebrow and section-title level; body copy is single-language, matched to the audience. Board, regulator, and investor-relations material is bilingual throughout; internal working documents may be English-only.

## Positioning discipline

Getting this wrong is worse than getting the colors wrong.

**This plugin encodes no product or positioning language, by design.** Product names, service descriptions, SKUs, partner platforms, roadmap claims and taglines all live in the approved source your organisation maintains — read them from there for every deliverable, and never infer or invent them.

Two failure modes to watch for regardless of the source:

- **Shipping product vs. vision.** Do not describe what the company sells today in the language of the roadmap. Forward-looking pillars belong on slides labelled as such.
- **Pillar-specific taglines.** A line written for one pillar does not transfer to a current-product slide.

## Before delivering

1. `officecli view <file> issues` — catches overflow, low contrast, stale fields.
2. `officecli view <file> screenshot --grid --out contact.png`, then read the PNG. Grid drift and text overflow are invisible in the DOM.
3. Confirm wordmark, eyebrow, footer, and page number are on every content slide.
4. Confirm no Calibri survived and no off-palette color crept in.
5. `officecli close <file>` before `SendUserFile` or `device_commit_files` — otherwise the delivered file is the pre-edit version.

## Word and Excel

The palette, typeface, and positioning rules carry over unchanged. Documents: Arial 10.5pt body, headings in `#0B318F`, table header rows filled `#0B318F` with white text, banding in `#F0F6FC`. Workbooks: header row `#0B318F` on white bold, `#F0F6FC` banding, `#00A3E6` for highlighted totals, freeze the header, no gridline-colored borders. Details in `references/palette.md`.
