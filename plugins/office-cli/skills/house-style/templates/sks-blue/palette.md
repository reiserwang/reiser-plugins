# SKS Blue — tokens

A two-field identity built on 60-30-10: a white page and a near-black page sharing one accent, one grid and one chart ramp. Separate from [`ana-blue`](../ana-blue/palette.md), [`yukima`](../yukima/palette.md), [`reiser-warm`](../reiser-warm/palette.md) and [`sks-dark`](../sks-dark/palette.md). Every value below is present in `sks-blue.pptx` or `sks-blue-dark.pptx`. Never introduce a colour that is not on this page.

> **Provenance — read, not sampled.** These hexes were read off the SPACES prototype by eye. The Figma file is not shared with the account wired into this toolchain, and the prototype renders to a WebGL canvas whose buffer cannot be read back, so no pixel could be measured. Every other palette in this system was sampled; this one is a faithful draft. Expect each channel within a few points of the brand's real value.
>
> **The ratios are exact.** They are computed from the hexes as written, so they are internally correct and will stay correct if a hex is corrected and `python3 scripts/contrast.py --check --write` is re-run. Never hand-edit a ratio.

**Fill-only colours, stated up front.** Light: `#C9D2EA`, `#A9B6D6`, `#F1F4FC`, `#E5E9F6`. Dark: `#2A3760`, `#3A4A7A`, `#101832`, `#16204A`, and `#1B3585` (which is a field, never type). Display-only on the dark file: `#2F55F0` — and it fails even that on the dark callout tint. Every one of the eight categorical colours is mark-only in both themes.

## Theme colour schemes

Two `.pptx` files, two themes, one accent set. The dark file's master inverts the `clrMap` (`bg1="dk1" tx1="lt1" bg2="dk2" tx2="lt2"`) so PowerPoint's own picker shows the field as Background and the ink as Text.

| Theme slot | `SKS Blue` | `SKS Blue Dark` | Role |
|---|---|---|---|
| field | `#FFFFFF` (lt1) | `#080D1A` (dk1) | page |
| headline ink | `#101623` (dk1) | `#FFFFFF` (lt1) | titles, body |
| panel | `#F1F4FC` (lt2) | `#101832` (dk2) | inset surface |
| muted ink | `#444E60` (dk2) | `#A8B4CE` (lt2) | captions, footers |
| `accent1` | `#2F55F0` | `#2F55F0` | the accent |
| `accent2` | `#3D6AFF` | `#3D6AFF` | chart series 1 |
| `accent3` | `#1A83A3` | `#1A83A3` | chart series 2 |
| `accent4` | `#268777` | `#268777` | chart series 3 |
| `accent5` | `#218A4B` | `#218A4B` | chart series 4 |
| `accent6` | `#9C53E6` | `#9C53E6` | chart series 5 |
| `hlink` | `#2F55F0` | `#8CB8FF` | links |
| `folHlink` | `#444E60` | `#A8B4CE` | visited |

## Light — 60% the field

| Token | Hex | On white | Role |
|---|---|---|---|
| White | `#FFFFFF` | — | the page, set on the master |
| Panel | `#F1F4FC` | 1.10 | inset surface — cards, panels, quiet bands |
| Callout | `#E5E9F6` | 1.21 | lifted surface — callout and takeaway bands. The prototype's own section field. |
| Rule | `#C9D2EA` | 1.51 | hairlines, table borders, panel frames |
| Muted fill | `#A9B6D6` | 2.03 | deprecated and inactive states — **fill only** |

White against panel is **1.10:1**, panel against callout **1.10:1**. That is the point: one family. If you need a hard boundary, use a `#C9D2EA` rule, not a fill change.

## Light — 30% the supporting layer

| Token | Hex | on `#FFFFFF` | on `#F1F4FC` | on `#E5E9F6` |
|---|---|---|---|---|
| Headline ink | `#101623` | **18.09** | 16.44 | 14.92 |
| Muted ink | `#444E60` | **8.39** | 7.62 | 6.91 |
| Blue **as text** | `#2F55F0` | **5.71** | 5.19 | 4.71 |

All three hold on all three surfaces — unusually comfortable, and the reason the light file needs no deprecated-ink footnote of the kind ANA Blue and SKS Dark both carry.

## Light — 10% the accent

| Token | Hex | On white | Role |
|---|---|---|---|
| Blue **as area** | `#2F55F0` | — | title rules, spines, badges, CTA fills, table header bands |
| Blue deep | `#1B3585` | 11.08 | the full-bleed Cover / Section Divider / Closing field |

## Dark — 60% the field

| Token | Hex | On `#080D1A` | Role |
|---|---|---|---|
| Midnight | `#080D1A` | — | the page. The prototype's nav bar and the outer edge of its hero. |
| Panel | `#101832` | 1.11 | inset surface |
| Callout | `#16204A` | 1.24 | lifted surface |
| Rule | `#2A3760` | 1.68 | hairlines, borders, frames — **fill only** |
| Muted fill | `#3A4A7A` | 2.25 | inactive states — **fill only** |

## Dark — 30% the supporting layer

| Token | Hex | on `#080D1A` | on `#101832` | on `#16204A` |
|---|---|---|---|---|
| Headline ink | `#FFFFFF` | **19.39** | 17.52 | 15.68 |
| Muted ink | `#A8B4CE` | **9.31** | 8.41 | 7.53 |
| Blue light **as text** | `#8CB8FF` | **9.62** | 8.69 | 7.77 |

`#8CB8FF` is the prototype's own colour for the Chinese subtitle on the dark hero. The design had already solved this problem; the template only names the answer.

## Dark — 10% the accent

| Token | Hex | on `#080D1A` | on `#101832` | on `#16204A` | Verdict |
|---|---|---|---|---|---|
| Blue **as area** | `#2F55F0` | 3.40 | 3.07 | **2.75** | **area only — and illegal even as a mark on the callout tint** |
| Blue deep | `#1B3585` | 1.75 | 1.58 | 1.41 | the divider field — **never type** |

## One blue, three values

The spine of this palette is a single hue, and the only thing that changes between the two themes is which of its three values carries type.

| | `#1B3585` blue deep | `#2F55F0` blue | `#8CB8FF` blue light |
|---|---|---|---|
| **Light** | full-bleed divider field, `#FFFFFF` at 11.08 | accent as area **and** as type (5.71 on white) | unused |
| **Dark** | the same divider field, same ink, same 11.08 | accent as area only (3.40) | accent as type (9.62) |

This is why the two files read as one identity: **the three divider layouts are byte-identical between them**, and only the content pages flip. It is also the sharpest difference from the other four templates, each of which resolves its accent inside a single field.

## Reverse ink on the accent fills

| Combination | Ratio | Verdict |
|---|---|---|
| `#FFFFFF` on `#1B3585` | **11.08** | any size — the divider combination, both themes |
| `#F1F4FC` on `#1B3585` | 10.07 | any size |
| `#FFFFFF` on `#2F55F0` | **5.71** | any size — the CTA-pill combination, both themes |
| `#101623` on `#2F55F0` | 3.17 | **≥ 24px only — a blue fill takes white, not dark ink** |

## The three traps

**On the dark file, `#2F55F0` is not a text colour.** 3.40:1 on the field, **2.75:1 on the callout tint** — below the 3.0 floor, so inside a callout band it fails even as a graphic mark. Use `#8CB8FF` for type and keep `#2F55F0` off the callout tint entirely. This is the likeliest error when restyling light → dark, because the identical hex is a legal 5.71:1 on the light file.

**A blue fill takes white.** `#101623` on `#2F55F0` is 3.17:1. Do not carry Reiser Warm's "coral needs charcoal" rule across.

**No categorical colour carries type, in either theme.** A single hue cannot be legible against both `#FFFFFF` and `#080D1A`; the shared ramp buys hue stability across a restyle and pays for it in text safety. Series labels go in ink or muted ink, with a legend swatch carrying the colour.

## Extended categorical — shared by both themes

Pitched at one luminance so that every colour clears **≥ 3.5:1 on all six surfaces**. A series must not change hue when a deck is restyled, which is the whole reason the ramp is shared rather than doubled. These sit outside the 60-30-10 bands: a chart is data, not page furniture. Do not extend the list.

| # | Token | Hex | `#FFFFFF` | `#F1F4FC` | `#E5E9F6` | `#080D1A` | `#101832` | `#16204A` | Worst |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Blue | `#3D6AFF` | 4.46 | 4.06 | 3.68 | 4.34 | 3.92 | 3.51 | 3.51 |
| 2 | Cyan | `#1A83A3` | 4.36 | 3.96 | 3.59 | 4.45 | 4.02 | 3.60 | 3.59 |
| 3 | Teal | `#268777` | 4.36 | 3.96 | 3.60 | 4.45 | 4.02 | 3.59 | 3.59 |
| 4 | Green | `#218A4B` | 4.37 | 3.97 | 3.61 | 4.43 | 4.01 | 3.58 | 3.58 |
| 5 | Amber | `#9E7015` | 4.39 | 3.99 | 3.62 | 4.42 | 3.99 | 3.57 | 3.57 |
| 6 | Violet | `#9C53E6` | 4.38 | 3.98 | 3.61 | 4.43 | 4.00 | 3.58 | 3.58 |
| 7 | Orange | `#C95624` | 4.34 | 3.94 | 3.58 | 4.47 | 4.04 | 3.61 | 3.58 |
| 8 | Rose | `#D4446A` | 4.34 | 3.95 | 3.58 | 4.46 | 4.03 | 3.61 | 3.58 |

Chart series order: `#3D6AFF` → `#1A83A3` → `#268777` → `#218A4B` → `#9E7015` → `#9C53E6` → `#C95624` → `#D4446A`.

Project Status spine order, as shipped: `#2F55F0` → `#1A83A3` → `#3D6AFF` → `#9C53E6`.

**Series 1 is `#3D6AFF`, not the accent `#2F55F0`.** The accent falls to 2.75:1 on the dark callout tint and would vanish inside a callout band. The ramp's blue is one value step up and holds on all six surfaces.

**There is no approved alert colour.** Orange and rose here are categorical hues, not status marks. If a deliverable genuinely needs risk or alert coding, ask rather than promoting one of them.

## Word (.docx) mapping

A dark field does not survive a printer, so **the document mapping is the light theme only**. Use the dark file for screens.

| Element | Spec |
|---|---|
| Page background | `#FFFFFF` |
| Body | Arial 10.5pt `#101623`, 1.15 line spacing |
| Heading 1 | Arial 16pt bold `#1B3585` |
| Heading 2 | Arial 13pt bold `#1B3585` |
| Heading 3 | Arial 11.5pt bold `#444E60` |
| Table header row | fill `#1B3585`, Arial 10pt bold `#FFFFFF` |
| Table banding | `#F1F4FC` on alternate rows |
| Table borders | `#C9D2EA` hairline |
| Link | `#2F55F0` |
| Caption / footnote | Arial 9pt `#444E60` |
| Page footer | `{{ORG}}  \|  {{DECK_TITLE}}` — Arial 9pt `#444E60` |

On white: `#101623` 18.09, `#1B3585` 11.08, `#444E60` 8.39, `#2F55F0` 5.71 — all clear the gate. Headings use `#1B3585` rather than `#2F55F0` because a 13pt heading on paper wants the margin.

Set `font.ea=微軟正黑體` alongside `font.latin=Arial` for any 中文 content.

## Excel (.xlsx) mapping

| Element | Spec |
|---|---|
| Sheet background | `#FFFFFF` |
| Header row | fill `#1B3585`, Arial 10pt bold `#FFFFFF`, frozen |
| Banding | `#F1F4FC` alternate rows |
| Total / highlight row | fill `#E5E9F6`, bold, top border `#1B3585` |
| Key metric cells | font `#2F55F0` bold |
| Body | Arial 10pt `#101623` |
| Borders | `#C9D2EA` thin; no heavy grids |
| Chart series | the shared ramp, in order |
| Negative numbers | parentheses, not red — `#,##0;(#,##0)` |
| Currency | state the unit in the header, not per cell |

## Web mapping

The two themes map straight onto a token pair. The categorical ramp does **not** change between them — that is the point of pitching it at one luminance.

| Token | Light | Dark |
|---|---|---|
| `--bg` | `#FFFFFF` | `#080D1A` |
| `--surface` | `#F1F4FC` | `#101832` |
| `--surface-lifted` | `#E5E9F6` | `#16204A` |
| `--rule` | `#C9D2EA` | `#2A3760` |
| `--muted-fill` | `#A9B6D6` | `#3A4A7A` |
| `--ink` | `#101623` | `#FFFFFF` |
| `--ink-muted` | `#444E60` | `#A8B4CE` |
| `--accent` | `#2F55F0` | `#2F55F0` |
| `--accent-text` | `#2F55F0` | `#8CB8FF` |
| `--accent-field` | `#1B3585` | `#1B3585` |
| `--on-accent` | `#FFFFFF` | `#FFFFFF` |
| `--series-1…8` | shared ramp | shared ramp |

`--accent` and `--accent-text` are separate tokens for one reason: on the dark theme they must differ. Any component that sets a blue *label* uses `--accent-text`; any component that sets a blue *area* uses `--accent`. A component that reaches for `--accent` as a text colour will pass in light and fail in dark.

Never place `--accent` on `--surface-lifted` in the dark theme (2.75:1).

## Verification

Ratios computed against WCAG relative luminance, not estimated. `python3 scripts/contrast.py --check` verifies the tokens against both `.pptx` files; `--write` regenerates the shared matrix.
