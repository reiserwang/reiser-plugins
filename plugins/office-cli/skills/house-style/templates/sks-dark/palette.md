# SKS Dark — tokens

A dark-field identity built on 60-30-10, separate from [`ana-blue`](../ana-blue/palette.md), [`yukima`](../yukima/palette.md) and [`reiser-warm`](../reiser-warm/palette.md). Every value below is present in `sks-dark.pptx`. Never introduce a colour that is not on this page.

**Provenance.** All but three tokens were sampled from the two reference comps rather than invented — the cover comp gave the field, the ink and the amber; the agenda comp gave the row hairline, the four category-spine colours and the inactive grey. The three exceptions are marked *(derived)*: each is a value-shift of a sampled colour, same hue, moved only far enough to clear the contrast gate in the role it was failing.

**Fill-only colours, stated up front** — these never carry type at any size: `#8A5613`, `#546D85`, `#5D6874`, `#3E4C5A`, `#273546`, `#213040`. Two more are display-only, legal at ≥ 24px and illegal below it: `#B57319` and `#698EB1`. And one is a documented trap: `#727C86`.

## Theme colour scheme

The `.pptx` theme is named `SKS Dark`. Because the field is dark, the master's `clrMap` is inverted (`bg1="dk1" tx1="lt1" bg2="dk2" tx2="lt2"`) so PowerPoint's own picker shows the field as Background and the ink as Text:

| Theme slot | Hex | Role |
|---|---|---|
| `dk1` → bg1 | `#1A293A` | field |
| `lt1` → tx1 | `#F4F1EF` | headline ink |
| `dk2` → bg2 | `#213040` | panel tint |
| `lt2` → tx2 | `#A9B2BB` | muted ink |
| `accent1` | `#B57319` | amber — **fill only** |
| `accent2` | `#CCA348` | gold — the accent as type |
| `accent3` | `#698EB1` | steel |
| `accent4` | `#546D85` | deep steel — **fill only** |
| `accent5` | `#5FB3AA` | teal |
| `accent6` | `#8FA9C4` | steel light |
| `hlink` | `#CCA348` | links |
| `folHlink` | `#A9B2BB` | visited |

## 60% — the field

Six surfaces carry the page and almost never carry text.

| Token | Hex | Role | ANA Blue equivalent |
|---|---|---|---|
| Midnight | `#1A293A` | The default page, set on the master. Everything else sits on this. *(sampled)* | `#FFFFFF` |
| Panel | `#213040` | Inset surface — cards, panels, quiet bands. The default surface for grouped content. *(interpolated step)* | `#F0F6FC` |
| Callout | `#273546` | Lifted surface — full-width callout and takeaway bands, emphasis strips, Risk Matrix low cells. Sampled from the agenda comp's row hairline. | `#E6F2FC` |
| Rule | `#3E4C5A` | Hairlines, table borders, dividers, panel frames, the inactive spine. *(sampled)* | `#C3D6EE` |

Their separation is deliberately low — midnight against panel is **1.10:1**, panel against callout **1.08:1**. That is the point: the tints are a single family, and the eye should not be asked to parse them as distinct zones. If you need a hard boundary, use a `#3E4C5A` rule, not a fill change. On a dark field this restraint matters more than on a light one, because raising a tint too far reads as a lit panel rather than a grouping.

Two further fills belong to this band rather than to the accent, because they are area and never text:

| Token | Hex | Role |
|---|---|---|
| Deep steel | `#546D85` | Deprecated or inactive states, quiet spines, unshipped roadmap phases. 2.74:1 — **fill only**. |
| Grey | `#5D6874` | The inactive numeral and spine in the agenda comp. 2.60:1 — **fill only**. |

## 30% — the supporting layer

| Token | Hex | On midnight | Role |
|---|---|---|---|
| Headline ink | `#F4F1EF` | **13.13** | Titles, body, callout body, panel body, reverse ink on the accent field. *(sampled)* |
| Muted ink *(derived)* | `#A9B2BB` | **6.87** | Supporting body, footers, captions, axis labels, source lines. Lightened from the comp's `#727C86`. |
| Gold **as text** | `#CCA348` | **6.26** | Eyebrows, section titles, panel headings, table header text, big numbers, links. See the dual-role note below. *(sampled)* |

**`#727C86` is the reference's own secondary grey and it does not survive the gate.** It sets the English subtitles in the agenda comp at 3.48:1 on the field and 2.94:1 on the callout tint — legal at display sizes, illegal as the 13–18pt supporting copy it was doing there. It is the dark-field twin of ANA Blue's `#647084`. Keep it for hairlines and inactive marks; use `#A9B2BB`, which holds **5.80** even on the callout tint.

## 10% — the accent

| Token | Hex | On midnight | Role |
|---|---|---|---|
| Amber **as area** | `#B57319` | 3.82 | Title rules, category spines, icon badges, chart series 1. **Never type below 24px.** *(sampled)* |
| Gold **as area** | `#CCA348` | — | Filled blocks that carry `#1A293A` ink at 6.26:1 — KPI chips, emphasis marks. *(sampled)* |
| Amber deep *(derived)* | `#8A5613` | 2.41 | The full-bleed Cover / Section Divider / Closing field, and any accent band carrying `#F4F1EF` at 5.46:1. |

One accent per page.

## The three-step accent — how this differs from the light templates

Reiser Warm's coral **cannot** be text (2.92:1 on cream), so its 10% band is unambiguous. ANA Blue's deep blue **is** text-safe at 11.35:1, so it occupies the 30% as type and the 10% as area. SKS Dark needs a third arrangement, because on a dark field one warm cannot both sit quietly as a rule and carry small type:

- **`#B57319` amber** is the accent as area. 3.82:1 — a legal graphic element, an illegal label.
- **`#CCA348` gold** is the accent as type, and it is part of the 30% when it is set as words. It also takes dark ink as a fill.
- **`#8A5613` amber deep** exists only because `#F4F1EF` on `#B57319` is 3.44:1 and fails. It is the accent as *field*.

**The 10% ceiling governs amber as area, not gold as type.** A page can carry gold headings throughout and stay on-discipline; a page with four amber-filled blocks does not.

**Divider pages are a deliberate exception.** Cover, Section Divider and Closing are full-bleed `#8A5613` — 100% accent area. The 10% ceiling is a per-content-page rule; the three divider layouts exist precisely to spend the accent all at once, exactly as ANA Blue does with deep blue and Reiser Warm with coral.

## Two traps

**Amber is a fill colour, not a text colour.** 3.82:1 on the field — it fails below 24px. Use `#CCA348` (6.26), which is the same warm two steps up. The reference cover comp sets its eyebrow in `#B57319`; that would be flagged, and the shipping template uses `#CCA348` instead.

**An amber fill does not take light text; a deep-amber fill does.** `#F4F1EF` on `#B57319` is 3.44:1. Either drop the fill to `#8A5613` (5.46) or raise it to `#CCA348` and set the ink dark (6.26). Do not carry ANA Blue's "a deep-blue fill takes white text" rule across unchanged.

| Combination | Ratio | Verdict |
|---|---|---|
| `#F4F1EF` on `#8A5613` | **5.46** | any size — the divider and band combination |
| `#FFFFFF` on `#8A5613` | 6.14 | any size — but the template's reverse ink is `#F4F1EF` |
| `#1A293A` on `#CCA348` | **6.26** | any size — the gold-chip combination |
| `#F4F1EF` on `#B57319` | 3.44 | **≥ 24px only — do not use for labels** |
| `#F4F1EF` on `#CCA348` | 2.10 | **fill only** |

## Extended categorical

The agenda comp establishes the ramp — warm and cool alternating so adjacent rows separate without any of them shouting. Steps 1–5 are sampled; 6–9 extend it for charts needing more than five series, pitched at the same value so no series jumps forward. These sit outside the 60-30-10 bands: a chart is data, not page furniture. Do not extend the list.

| # | Hex | Convention | On midnight |
|---|---|---|---|
| 1 | `#B57319` | Amber — series 1, primary spine | 3.82 — **≥ 24px only** |
| 2 | `#CCA348` | Gold — series 2 | 6.26 |
| 3 | `#698EB1` | Steel — series 3, compute / cloud layer | 4.29 — **≥ 24px only** |
| 4 | `#546D85` | Deep steel — series 4 | 2.74 — **fill only** |
| 5 | `#5D6874` | Grey — inactive / unshipped | 2.60 — **fill only** |
| 6 | `#8FA9C4` *(derived)* | Steel light — the text-safe steel, for labels in that hue | 6.08 |
| 7 | `#5FB3AA` | Teal — series 5 | 5.99 |
| 8 | `#A79EDA` | Violet — series 6, AI / analytics layer | 6.01 |
| 9 | `#8FB07E` | Sage — series 7, healthy / operational | 6.10 |

Chart series order: `#B57319` → `#CCA348` → `#698EB1` → `#546D85` → `#5FB3AA` → `#A79EDA` → `#8FB07E` → `#5D6874`.

Project Status spine order, as shipped in the layout: `#B57319` → `#698EB1` → `#CCA348` → `#546D85`.

**There is still no approved red or amber alert colour.** Amber is the accent here, so it cannot double as a caution mark, and no cool step reads as danger. If a deliverable genuinely needs risk or alert coding, ask rather than inventing one.

## Contrast — verified, not estimated

| Foreground | on `#1A293A` | on `#213040` | on `#273546` | Verdict |
|---|---|---|---|---|
| `#F4F1EF` | 13.13 | 11.96 | 11.09 | any size |
| `#A9B2BB` | 6.87 | 6.26 | 5.80 | any size |
| `#CCA348` | 6.26 | 5.70 | 5.29 | any size |
| `#8FB07E` | 6.10 | 5.56 | 5.15 | any size |
| `#8FA9C4` | 6.08 | 5.53 | 5.13 | any size |
| `#A79EDA` | 6.01 | 5.47 | 5.08 | any size |
| `#5FB3AA` | 5.99 | 5.45 | 5.06 | any size |
| `#698EB1` | 4.29 | 3.91 | 3.63 | **≥ 24px only** |
| `#B57319` | 3.82 | 3.48 | 3.23 | **≥ 24px only** |
| `#727C86` | 3.48 | 3.17 | **2.94** | **≥ 24px only — and fails as area type on the callout tint** |
| `#546D85` | 2.74 | 2.50 | 2.32 | **fill only** |
| `#5D6874` | 2.60 | 2.37 | 2.20 | **fill only** |
| `#8A5613` | 2.41 | 2.19 | 2.03 | **fill only** |
| `#3E4C5A` | 1.68 | 1.53 | 1.42 | **rules only** |

Gate: ≥ 4.5:1 below 24px, ≥ 3.0:1 at or above. Recompute snippet in [`../../references/contrast.md`](../../references/contrast.md); the full generated matrix is [`../../references/contrast-matrix.md`](../../references/contrast-matrix.md).

## Typography

Arial (Latin) + 微軟正黑體 (中文). Sizes on the 1440 × 810 pt canvas — identical to `ana-blue`; only the colours move.

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

Bullet ramp on the master: 18 → 16 → 15 → 14 → 13pt, ink `#F4F1EF` at level 1 and `#A9B2BB` below. Bold is the only weight variation.

**Light type on a dark ground blooms.** Do not add bold to body copy to compensate — if a line is not reading, it is a colour problem, not a weight problem.

## Word (.docx) mapping

A dark field does not survive printing, so **the document mapping keeps a white page** and borrows only the accent. Use `ana-blue` outright if the document is going to a printer under the organisation's mark; this mapping is for screen-read PDFs that must sit alongside an SKS Dark deck.

| Element | Spec |
|---|---|
| Page background | `#FFFFFF` |
| Body | Arial 10.5pt `#1A293A`, 1.15 line spacing |
| Heading 1 | Arial 16pt bold `#8A5613` |
| Heading 2 | Arial 13pt bold `#8A5613` |
| Heading 3 | Arial 11.5pt bold `#546D85` |
| Table header row | fill `#1A293A`, Arial 10pt bold `#F4F1EF` |
| Table banding | `#F1EDE6` on alternate rows |
| Table borders | `#D8D2C8` hairline |
| Caption / footnote | Arial 9pt `#546D85` |
| Page footer | `{{ORG}}  \|  {{DECK_TITLE}}` — Arial 9pt `#546D85` |

On white: `#1A293A` 14.77, `#8A5613` 6.14, `#546D85` 5.38 — all clear the gate. `#CCA348` is **2.36 on white** and `#B57319` is 3.87; neither may carry document text.

Set `font.ea=微軟正黑體` alongside `font.latin=Arial` for any 中文 content.

## Excel (.xlsx) mapping

Same reasoning — the grid stays white; the accent and the dark ink come across.

| Element | Spec |
|---|---|
| Sheet background | `#FFFFFF` |
| Header row | fill `#1A293A`, Arial 10pt bold `#F4F1EF`, frozen |
| Banding | `#F1EDE6` alternate rows |
| Total / highlight row | fill `#FAF3E4`, bold, top border `#8A5613` |
| Key metric cells | font `#8A5613` bold — not `#CCA348`, which fails on white |
| Body | Arial 10pt `#1A293A` |
| Borders | `#D8D2C8` thin; no heavy grids |
| Negative numbers | parentheses, not red — `#,##0;(#,##0)` |
| Currency | state the unit in the header, not per cell |

## Verification

Every ratio here was computed against WCAG relative luminance, not estimated. Re-run after any change: `python3 scripts/contrast.py --check` verifies the tokens against `sks-dark.pptx`, `--write` regenerates the shared matrix.
