# ANA Blue — tokens

A white-field identity built on 60-30-10, separate from [`reiser-warm`](../reiser-warm/palette.md). Every value below is present in `ana-blue.pptx`. Never introduce a colour that is not on this page.

## Theme colour scheme

The `.pptx` theme is named `ANA Blue` and maps as follows, so `schemeClr` references resolve correctly in PowerPoint's own colour picker:

| Theme slot | Hex | Role |
|---|---|---|
| `dk1` / tx1 | `#1A2230` | headline ink |
| `lt1` / bg1 | `#FFFFFF` | field |
| `dk2` / tx2 | `#5A6676` | muted ink |
| `lt2` / bg2 | `#F0F6FC` | panel tint |
| `accent1` | `#0B318F` | primary |
| `accent2` | `#00A3E6` | sky — **fill only** |
| `accent3` | `#2E5BF0` | blue |
| `accent4` | `#7C4DB8` | purple |
| `accent5` | `#2FA84F` | green |
| `accent6` | `#AFC0D6` | muted |
| `hlink` | `#0B318F` | links |
| `folHlink` | `#5A6676` | visited |

## 60% — the field

Four surfaces carry the page and almost never carry text.

| Token | Hex | Role | Reiser Warm equivalent |
|---|---|---|---|
| White | `#FFFFFF` | The default page, set on the master. Everything else sits on this. | `#F5F1ED` |
| Panel | `#F0F6FC` | Inset surface — cards, panels, quiet bands. The default surface for grouped content. | `#E8E4DF` |
| Callout | `#E6F2FC` | Lifted surface — full-width callout and takeaway bands, emphasis strips, Risk Matrix low cells. | `#F5F3F1` |
| Rule | `#C3D6EE` | Hairlines, table borders, dividers, panel frames. | `#D4D0C9` |

Their separation is deliberately low — white against panel is **1.09:1**, panel against callout **1.04:1**. That is the point: the tints are a single family, and the eye should not be asked to parse them as distinct zones. If you need a hard boundary, use a `#C3D6EE` rule, not a fill change.

Two further fills belong to this band rather than to the accent, because they are area and never text:

| Token | Hex | Role |
|---|---|---|
| Muted fill | `#AFC0D6`, `#AEC6E8` | Deprecated or inactive states, unshipped roadmap phases. 1.85:1 and 1.74:1 on white — **fill only**. |

## 30% — the supporting layer

| Token | Hex | On white | Role |
|---|---|---|---|
| Headline ink | `#1A2230` | **15.96** | Titles, taglines, callout body, panel body. |
| Muted ink | `#5A6676` | **5.84** | Supporting body, footers, captions, axis labels, source lines. |
| Deep blue **as text** | `#0B318F` | **11.35** | Section titles, panel headings, table header text, big numbers, links. See the dual-role note below. |
| Reverse | `#FFFFFF` | 11.35 on `#0B318F` | Text on a deep-blue fill and on the Cover / Section / Closing field. |

`#647084` also appears in the source decks as a second muted ink. **It is not interchangeable with `#5A6676`** — it clears 4.5:1 on white (5.01) and on the panel tint (4.60) but falls to **4.41 on the callout tint**, which fails. Prefer `#5A6676`, which holds 5.14 even there.

## 10% — the accent

| Token | Hex | On white | Role |
|---|---|---|---|
| Deep blue **as area** | `#0B318F` | — | Title rules, category spines, icon badges, table header fills, chart series 1, the full-bleed divider field. |
| Sky | `#00A3E6` | 2.84 | Accent rules, chart series 2, category spines, "future / vision" framing. **Fill only.** |
| Text-safe sky | `#00719E` | **5.45** | Derived variant. Use when the sky hue must carry text — 5.00 on the panel tint. |

One accent per page.

## The dual role of deep blue — how this differs from Reiser Warm

This is the one place the two templates are not structurally parallel, and it matters.

Reiser Warm's accent **cannot** be text: coral is 2.92:1 on cream, so it is confined to fills, and the 10% band is unambiguous. ANA Blue's accent **is** text-safe at 11.35:1, so `#0B318F` legitimately appears in two bands at once:

- as **ink** — section titles, panel headings, table header text — it is part of the 30%;
- as **area** — rules, spines, badges, fills, chart series — it is part of the 10%.

**The 10% ceiling governs blue as area, not blue as type.** A page can carry blue headings throughout and still be on-discipline; a page with four blue-filled blocks is not. In practice this is why an ANA Blue deck reads bluer than a Reiser Warm deck reads coral, without either breaking its rule.

**Divider pages are a deliberate exception.** Cover, Section Divider and Closing are full-bleed `#0B318F` — 100% accent area. The 10% ceiling is a per-content-page rule; the three divider layouts exist precisely to spend the accent all at once. Reiser Warm does the same with coral.

## Two traps

**Sky is a fill colour, not a text colour.** 2.84:1 on white, fails at every size. Use `#0B318F` (11.35), or `#00719E` (5.45) when the sky hue itself is the point. The source decks set 14pt sky eyebrows on white; those would be flagged, and the shipping template uses `#0B318F` instead.

**A deep-blue fill takes white text.** 11.35:1 — unlike coral, which needs charcoal. Do not carry the Reiser Warm rule across.

| Combination | Ratio | Verdict |
|---|---|---|
| `#FFFFFF` on `#0B318F` | **11.35** | any size — use this |
| `#E6F2FC` on `#0B318F` | 9.98 | any size |
| `#C3D6EE` on `#0B318F` | 7.66 | any size |
| `#00A3E6` on `#0B318F` | 3.99 | ≥ 24px only |

## Extended categorical

For chart series 3+, architecture-layer coding, and category spines. These sit outside the 60-30-10 bands — a chart is data, not page furniture. Do not extend the list.

| Hex | Convention | On white |
|---|---|---|
| `#2E5BF0` | Blue — compute / cloud layer, neutral series | 5.43 |
| `#7C4DB8` | Purple — AI / analytics layer | 5.82 |
| `#2FA84F` | Green — healthy, operational, "yes" | 3.07 — **≥ 24px only** |

Chart series order: `#0B318F` → `#00A3E6` → `#2E5BF0` → `#7C4DB8` → `#2FA84F` → `#AFC0D6`.

Project Status spine order: `#0B318F` → `#00A3E6` → `#2E5BF0` → `#7C4DB8`.

**There is no approved red or amber.** If a deliverable genuinely needs a risk or alert colour, ask rather than inventing one.

Deep blue dark variants `#0A308E` and `#12327E` appear in the source decks as gradient partners and darker bands only. Not a second primary.

## Contrast — verified, not estimated

| Foreground | on `#FFFFFF` | on `#F0F6FC` | on `#E6F2FC` | Verdict |
|---|---|---|---|---|
| `#1A2230` | 15.96 | 14.67 | 14.04 | any size |
| `#0B318F` | 11.35 | 10.43 | 9.98 | any size |
| `#5A6676` | 5.84 | 5.36 | 5.14 | any size |
| `#7C4DB8` | 5.82 | — | — | any size |
| `#00719E` | 5.45 | 5.00 | — | any size — the text-safe sky |
| `#2E5BF0` | 5.43 | — | — | any size |
| `#647084` | 5.01 | 4.60 | **4.41** | **fails on the callout tint** |
| `#2FA84F` | 3.07 | — | — | **≥ 24px only** |
| `#00A3E6` | **2.84** | — | — | **fails at every size — fill only** |
| `#AFC0D6` | 1.85 | — | — | **fill only** |
| `#C3D6EE` | 1.48 | — | — | **rules only** |

Gate: ≥ 4.5:1 below 24px, ≥ 3.0:1 at or above. Recompute snippet in [`../../references/contrast.md`](../../references/contrast.md).

## Typography

Arial (Latin) + 微軟正黑體 (中文). Sizes on the 1440 × 810 pt canvas:

| Size | Role |
|---|---|
| 130pt | Quote opening glyph |
| 96pt | Big Number |
| 54pt | KPI value |
| 40pt | Cover title |
| 34pt | Section / Closing title |
| 30pt | Slide title |
| 28pt | Quote body |
| 24pt | Agenda numeral |
| 21pt | Cover subtitle, takeaway, rationale |
| 20pt | Eyebrow (bold) |
| 18pt | Body, panel heading, table header — the workhorse |
| 13pt | Footer, page number, source line, caption |

Bullet ramp on the master: 18 → 16 → 15 → 14 → 13pt, ink `#1A2230` at level 1 and `#5A6676` below. Bold is the only weight variation.

## Word (.docx) mapping

The same 60-30-10 split: the page and its banding are the 60%, ink is the 30%, and blue fills are the 10%.

| Element | Spec |
|---|---|
| Page background | `#FFFFFF` |
| Body | Arial 10.5pt `#1A2230`, 1.15 line spacing |
| Heading 1 | Arial 16pt bold `#0B318F` |
| Heading 2 | Arial 13pt bold `#0B318F` |
| Heading 3 | Arial 11.5pt bold `#5A6676` |
| Table header row | fill `#0B318F`, Arial 10pt bold `#FFFFFF` |
| Table banding | `#F0F6FC` on alternate rows |
| Table borders | `#C3D6EE` hairline |
| Caption / footnote | Arial 9pt `#5A6676` |
| Page footer | `{{ORG}}  \|  {{DECK_TITLE}}` — Arial 9pt `#5A6676` |

Set `font.ea=微軟正黑體` alongside `font.latin=Arial` for any 中文 content.

## Excel (.xlsx) mapping

| Element | Spec |
|---|---|
| Sheet background | `#FFFFFF` |
| Header row | fill `#0B318F`, Arial 10pt bold white, frozen |
| Banding | `#F0F6FC` alternate rows |
| Total / highlight row | fill `#E6F2FC`, bold, top border `#0B318F` |
| Key metric cells | font `#0B318F` bold — not `#00A3E6`, which fails as text |
| Body | Arial 10pt `#1A2230` |
| Borders | `#C3D6EE` thin; no heavy grids |
| Negative numbers | parentheses, not red — `#,##0;(#,##0)` |
| Currency | state the unit in the header, not per cell |

## Verification

Every ratio here was computed against WCAG relative luminance, not estimated. Re-run after any change — snippet in [`../../references/contrast.md`](../../references/contrast.md).
