# ANA Blue — tokens

Every value below is present in `ana-blue.pptx`. Never introduce a colour that is not on this page.

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

## Brand core

| Token | Hex | Use |
|---|---|---|
| Deep blue (primary) | `#0B318F` | Icon badges, panel headings, table headers, section titles, title rules, category spines, chart series 1, big numbers |
| Sky | `#00A3E6` | Accent rules, chart series 2, category spines, "future / vision" framing. **Fill only** — see below. |
| Deep blue dark variants | `#0A308E`, `#12327E` | Gradient partners and darker bands only. Not a second primary. |

## Tints and surfaces

| Token | Hex | Use |
|---|---|---|
| Field | `#FFFFFF` | Slide and page background. Set on the master; overridden only by Cover / Section Divider / Closing (`#0B318F`) and Quote (`#F0F6FC`). |
| Panel | `#F0F6FC` | Card and panel fills — the default surface for grouped content |
| Callout | `#E6F2FC` | Full-width callout and takeaway bands, emphasis strips, Risk Matrix low cells |
| Rule / divider | `#C3D6EE` | Hairlines, table borders, dividers, panel frames |
| Muted fill | `#AEC6E8`, `#AFC0D6` | Deprecated or inactive states, unshipped roadmap phases |

## Ink

| Token | Hex | Use |
|---|---|---|
| Headline | `#1A2230` | Titles, taglines, callout body, panel body |
| Muted | `#5A6676` | Supporting body, footers, captions, axis labels, source lines |
| Muted alt | `#647084` | Interchangeable with muted; prefer `#5A6676` for new work |
| Reverse | `#FFFFFF` | Text on `#0B318F` fills and on the Cover / Section / Closing field |

## Categorical and semantic accents

Use in this order for chart series 3+, architecture-layer coding, and category spines. Do not extend the list.

| Hex | Convention |
|---|---|
| `#2E5BF0` | Blue — compute / cloud layer, neutral series |
| `#7C4DB8` | Purple — AI / analytics layer |
| `#2FA84F` | Green — healthy, operational, "yes". **≥ 24px only** (3.07:1) |

Chart series order: `#0B318F` → `#00A3E6` → `#2E5BF0` → `#7C4DB8` → `#2FA84F` → `#AFC0D6`.

Project Status spine order: `#0B318F` → `#00A3E6` → `#2E5BF0` → `#7C4DB8`.

**There is no approved red or amber.** If a deliverable genuinely needs a risk or alert colour, ask rather than inventing one.

## Contrast — verified, not estimated

| Foreground | on `#FFFFFF` | on `#F0F6FC` | Verdict |
|---|---|---|---|
| `#1A2230` | 15.96 | 14.67 | any size |
| `#0B318F` | 11.35 | 10.43 | any size |
| `#5A6676` | 5.84 | 5.36 | any size |
| `#7C4DB8` | 5.82 | — | any size |
| `#00719E` | 5.45 | 5.00 | any size — the text-safe sky |
| `#2E5BF0` | 5.43 | — | any size |
| `#2FA84F` | 3.07 | — | **≥ 24px only** |
| `#00A3E6` | **2.84** | — | **fails at every size — fill only** |
| `#FFFFFF` on `#0B318F` | 11.35 | — | any size |
| `#00A3E6` on `#0B318F` | 3.99 | — | ≥ 24px only |

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

Bullet ramp on the master: 18 → 16 → 15 → 14 → 13pt, ink `#1A2230` at level 1 and `#5A6676` below.

## Word (.docx) mapping

| Element | Spec |
|---|---|
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
| Header row | fill `#0B318F`, Arial 10pt bold white, frozen |
| Banding | `#F0F6FC` alternate rows |
| Total / highlight row | fill `#E6F2FC`, bold, top border `#0B318F` |
| Key metric cells | font `#0B318F` bold — not `#00A3E6`, which fails as text |
| Body | Arial 10pt `#1A2230` |
| Borders | `#C3D6EE` thin; no heavy grids |
| Negative numbers | parentheses, not red — `#,##0;(#,##0)` |
| Currency | state the unit in the header, not per cell |
