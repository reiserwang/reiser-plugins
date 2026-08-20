# Palette & type tokens

Extracted from `corporate_master_deck.pptx` (20 slides) and `reference_architecture.pptx` by frequency analysis of every shape fill and run color. Frequencies shown are the observed counts — they indicate which tokens are load-bearing.

## Brand core

| Token | Hex | Observed | Use |
|---|---|---|---|
| ANA Blue / deep | `#0B318F` | 25 fills, 99 runs | Primary. Icon badges, card titles, table headers, section titles, chart series 1, callout lead-ins. |
| ANA Blue dark variant | `#0A308E`, `#12327E` | 6 | Gradient partners and hover/darker band only. Do not use as a second primary. |
| Sky | `#00A3E6` | 5 fills, 34 runs | Eyebrows, links, accent rules, "future / vision" framing, chart series 2. |

## Tints (backgrounds & panels)

| Token | Hex | Use |
|---|---|---|
| Panel | `#F0F6FC` | Card and panel fills. The default surface for grouped content. |
| Callout | `#E6F2FC` | Full-width callout bands, emphasis strips, card borders. |
| Rule / divider | `#C3D6EE` | Hairlines, table borders, dividers. |
| Muted fill | `#AEC6E8`, `#AFC0D6` | Deprecated / secondary states, inactive roadmap phases. |
| Background | `#FFFFFF` | Slide and page background. Always. Never a colored master. |

## Ink

| Token | Hex | Use |
|---|---|---|
| Headline | `#1A2230` | Titles, taglines, callout body. |
| Body | `#5A6676` | All body copy, footers, captions. The most-used text color in the deck (163 runs). |
| Body alt | `#647084` | Interchangeable with body; prefer `#5A6676` for new work. |
| Reverse | `#FFFFFF` | Text on `#0B318F` fills. |

## Categorical / semantic accents

Use in this order for chart series 3+, architecture-layer coding, and status marks. Do not extend the list.

| Hex | Convention |
|---|---|
| `#2E5BF0` | Blue — compute / cloud layer, neutral series |
| `#2FA84F` | Green — healthy, operational, "yes" |
| `#7C4DB8` | Purple — AI / analytics layer |

Chart series order: `#0B318F` → `#00A3E6` → `#2E5BF0` → `#7C4DB8` → `#2FA84F` → `#AFC0D6`.

There is no approved red or amber. If a deck genuinely needs a risk/alert color, ask the user rather than inventing one.

## Typography

Arial only. Observed size distribution across the corporate decks:

| Size | Observed | Role |
|---|---|---|
| 24pt | hero | Page tagline |
| 19–22pt | 16+2 | Section / slide title |
| 16–16.5pt | 72 | Card title, block heading |
| 14–14.5pt | 19 | Eyebrow (bold, sky), callout band |
| 12–12.5pt | 113 | Body — the workhorse size |
| 11–11.5pt | 43 | Dense body, table cells |
| 9–10.5pt | 91 | Captions, footers, axis labels, legal |

Bold is the only weight variation. No italics, no letter-spacing tricks, no all-caps runs longer than three words.

## Spacing grid

Base unit **10.8pt** (0.15in). Every offset in the corporate decks is a multiple.

| Multiple | pt | Use |
|---|---|---|
| 1× | 10.8 | Inner card padding (left/right of title) |
| 2× | 21.6 | Card top padding, footer band height |
| 4× | 43.2 | Left page margin (text), title block height |
| Content band | `x = 37.4 → 918` (width 880.6) | All full-width elements |
| Card gutter | 13.7 | Between cards in a row |

## Word (.docx) mapping

| Element | Spec |
|---|---|
| Body | Arial 10.5pt, `#1A2230`, 1.15 line spacing |
| Heading 1 | Arial 16pt bold `#0B318F` |
| Heading 2 | Arial 13pt bold `#0B318F` |
| Heading 3 | Arial 11.5pt bold `#5A6676` |
| Table header row | fill `#0B318F`, Arial 10pt bold `#FFFFFF` |
| Table banding | `#F0F6FC` on alternate rows |
| Table borders | `#C3D6EE` hairline |
| Caption / footnote | Arial 9pt `#5A6676` |
| Page footer | `<Company>  |  <document title>` — Arial 9pt `#5A6676` |

## Excel (.xlsx) mapping

| Element | Spec |
|---|---|
| Header row | fill `#0B318F`, Arial 10pt bold white, frozen |
| Banding | `#F0F6FC` alternate rows |
| Total / highlight row | fill `#E6F2FC`, bold, top border `#0B318F` |
| Key metric cells | font `#00A3E6` bold |
| Body | Arial 10pt `#1A2230` |
| Borders | `#C3D6EE` thin; no heavy grids |
| Negative numbers | parentheses, not red — e.g. `#,##0;(#,##0)` |
| Currency | `NT$#,##0` for TWD, `$#,##0` for USD; state the unit in the header, not per cell |
