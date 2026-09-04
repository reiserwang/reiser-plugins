# SKS Blue

The product-facing template, and the only one in this system that ships **two fields**. A white page and a near-black page, one accent, one grid, one type scale. Read from the SPACES prototype, which does exactly this: a dark hero, then light sections, with the same blue running through both.

**Use for** product and platform material — SPACES and its siblings, launch and demo sets, digital-product decks, anything that has to sit next to the live site without looking like a different company.
**Do not use for** board, regulator and investor material under the corporate mark — that is [`ana-blue`](../ana-blue/TEMPLATE.md), whose deep navy is the corporate register. Never mix the two in one file.

| | |
|---|---|
| Files | [`sks-blue.pptx`](sks-blue.pptx) and [`sks-blue-dark.pptx`](sks-blue-dark.pptx) — each 1 master, 19 layouts, 1 blank starter slide |
| Theme names | `SKS Blue` · `SKS Blue Dark` |
| Canvas | 1440 × 810 pt |
| Light field | `#FFFFFF`, with `#F1F4FC` panel and `#E5E9F6` callout. Three layouts override it: Cover / Section Divider / Closing on `#1B3585`; Quote on `#F1F4FC`. |
| Dark field | `#080D1A`, with `#101832` panel and `#16204A` callout. Same three overrides on `#1B3585`; Quote on `#101832`. |
| Accent | `#2F55F0` in both themes |
| deck-build overrides | [`theme.json`](theme.json) · [`theme.dark.json`](theme.dark.json) |
| Tokens and ratios | [`palette.md`](palette.md) |

## ⚠ The hex values are read, not sampled

Every other template in this system was measured — pixels sampled out of a source deck or a comp. **These were read off the SPACES prototype by eye**, because the Figma file is not shared with the account wired into this toolchain and the prototype renders to a WebGL canvas whose buffer cannot be read back. Expect each channel to be within a few points of the real brand value, not exact.

The **ratios below are exact** — they are computed from the hexes as written. If a hex moves, the ratio moves with it, so re-run `python3 scripts/contrast.py --check --write` after any correction rather than editing a number by hand.

To replace the estimates with the real thing: share the Figma file with the connected account as an editor, read its design variables, and reconcile. Until then, treat this palette as a faithful draft with verified internal arithmetic, not as the brand's authoritative source.

## Start here

```bash
cp sks-blue.pptx deck.pptx          # light
cp sks-blue-dark.pptx deck.pptx     # dark
officecli open deck.pptx
officecli add deck.pptx slide --layout 'Cover'
```

Layout names, placeholder indices and geometry are identical across all five templates and both themes — [`../../references/layouts.md`](../../references/layouts.md) and [`../../references/grid.md`](../../references/grid.md) apply unchanged. Restyling a deck between the light and dark file is a master swap, not a rebuild.

## The 60-30-10 split

The rule is about *area*, not importance. Sixty percent is the surface you barely notice; ten percent is the thing you notice first. The split is the same in both themes; only the values move, and on the dark field the tints step *up* from the ground rather than down.

**Light — field `#FFFFFF`**

- **60% field** — `#FFFFFF` page, `#F1F4FC` panel, `#E5E9F6` callout, `#C9D2EA` rules, plus `#A9B6D6` as the muted fill for inactive states. White against panel is 1.10:1 and panel against callout 1.10:1: one family, not distinct zones. For a hard boundary use a `#C9D2EA` rule, not a fill change.
- **30% supporting** — `#101623` headline ink (18.09:1), `#444E60` muted ink (8.39:1), and `#2F55F0` blue *as text* (5.71:1).
- **10% accent** — `#2F55F0` blue *as area*: title rules, spines, badges, the CTA fill.

**Dark — field `#080D1A`**

- **60% field** — `#080D1A` page, `#101832` panel, `#16204A` callout, `#2A3760` rules, `#3A4A7A` muted fill. Same 1.1-ish separations, same reasoning.
- **30% supporting** — `#FFFFFF` headline ink (19.39:1), `#A8B4CE` muted ink (9.31:1), and `#8CB8FF` blue *as text* (9.62:1).
- **10% accent** — `#2F55F0` blue *as area*, unchanged from the light theme.

One accent per page in both. Ten percent is a ceiling, not a target: a page with no blue fill at all is fine; a page with four is decoration.

## One blue, three jobs

The palette's spine is a single hue at three values, and which of the three is *type* is the only thing that changes between the themes:

| Token | Hex | Light | Dark |
|---|---|---|---|
| Blue deep | `#1B3585` | Cover / Section Divider / Closing field, taking `#FFFFFF` at **11.08:1** | the same three fields, same ink, same ratio |
| Blue | `#2F55F0` | accent as **area** *and* as **type** (5.71:1 on white) | accent as **area only** — 3.40:1 on the field, and **2.75:1 on the callout tint**, so it fails there even as a graphic element |
| Blue light | `#8CB8FF` | not used | the accent as **type**: eyebrows, section titles, panel headings, big numbers, links (9.62:1) |

`#8CB8FF` is the prototype's own colour for the Chinese subtitle on the dark hero — the design had already solved this, and the template just names it.

**The Cover, Section Divider and Closing layouts are the deliberate exception** to the 10% ceiling: full-bleed `#1B3585`, 100% accent area, in *both* themes. That is what makes the two files read as one identity rather than two — the divider pages are literally identical, and only the content pages flip.

## The chart ramp is shared, and that costs something

Both themes use the **same** eight categorical colours. A series must not change hue when a deck is restyled, so the ramp is pitched at a single luminance that clears **≥ 3.5:1 on all six surfaces** — the three light tints and the three dark ones.

| # | Token | Hex | Worst of the six |
|---|---|---|---|
| 1 | Blue | `#3D6AFF` | 3.51 |
| 2 | Cyan | `#1A83A3` | 3.59 |
| 3 | Teal | `#268777` | 3.59 |
| 4 | Green | `#218A4B` | 3.58 |
| 5 | Amber | `#9E7015` | 3.57 |
| 6 | Violet | `#9C53E6` | 3.58 |
| 7 | Orange | `#C95624` | 3.58 |
| 8 | Rose | `#D4446A` | 3.58 |

The cost is that **no categorical colour is text-safe in either theme**. A colour cannot be simultaneously legible against white and against near-black; that is arithmetic, not taste. So series labels are set in the theme's own ink or muted ink, never in the series hue, and a legend swatch does the colour-carrying instead.

**Series 1 is `#3D6AFF`, not the accent.** `#2F55F0` falls to 2.75:1 on the dark callout tint and would disappear inside a callout band. The ramp's blue is one step up and holds everywhere.

**There is no approved alert colour.** Orange and rose are categorical hues, not status marks. If a deliverable genuinely needs risk coding, ask rather than promoting one of them.

## Type scale

Arial for Latin, 微軟正黑體 for 中文. Bold is the only weight variation. Sizes are identical to the rest of the system; only the colours move.

| Element | Size | Weight | Light | Dark |
|---|---|---|---|---|
| Cover title | 40pt | bold | `#FFFFFF` | `#FFFFFF` |
| Section / Closing title | 34pt | bold | `#FFFFFF` | `#FFFFFF` |
| Slide title | 30pt | bold | `#101623` | `#FFFFFF` |
| Quote opening glyph | 130pt | bold | `#2F55F0` | `#8CB8FF` |
| Quote body | 28pt | regular | `#101623` | `#FFFFFF` |
| Big Number | 96pt | bold | `#2F55F0` | `#8CB8FF` |
| KPI value | 54pt | bold | `#2F55F0` | `#8CB8FF` |
| Eyebrow | 20pt | bold | `#2F55F0` | `#8CB8FF` |
| Cover subtitle · takeaway · rationale | 21pt | regular | `#101623` / `#FFFFFF` | `#FFFFFF` |
| Panel heading, table header | 18pt | bold | `#2F55F0`, or `#FFFFFF` on a blue band | `#8CB8FF`, or `#FFFFFF` on a blue band |
| Body — the workhorse | 18pt | regular | `#101623` body, `#444E60` supporting | `#FFFFFF` body, `#A8B4CE` supporting |
| Footer, page number, source line | 13pt | regular | `#444E60` | `#A8B4CE` |

These are sizes on a **1440pt** canvas — two-thirds of these numbers on a conventional 960pt canvas. The upstream OfficeCLI pptx skill's ≥36pt title rule assumes a projected 960pt deck and **does not apply**: override it.

On the dark file, do not add bold to body copy to compensate for the ground. Light type on dark blooms; if a line is not reading it is a colour problem, not a weight problem.

## Standing furniture

Fourteen of the nineteen layouts carry all five, in both themes.

| Element | Position | Light | Dark |
|---|---|---|---|
| Eyebrow | `56, 48` | 20pt bold `#2F55F0` | 20pt bold `#8CB8FF` |
| Title | `56, 76` | 30pt bold `#101623` | 30pt bold `#FFFFFF` |
| Title rule | `56, 142`, `1328 × 1.5` | `#2F55F0` | `#2F55F0` |
| Footer | `56, 772` | 13pt `#444E60` | 13pt `#A8B4CE` |
| Page number | `1324, 772` | 13pt `#444E60`, right-aligned | 13pt `#A8B4CE`, right-aligned |

Eyebrows are bilingual, ` · `-separated, leading with 中文 — `風險 · RISK`, `數據 · DATA` — except `AGENDA · 議程`.

Three layouts substitute their own furniture: **Cover**, **Section Divider** and **Closing** are full-bleed `#1B3585` with `#FFFFFF` text in both themes; Cover and Section Divider carry a short white underline rule (`120 × 3` and `100 × 3`), Closing carries none, and the classification marking appears on Cover only. Two more ship bare: **Quote** (panel-tint field, footer and page number only) and **Blank** (title rule, footer and page number only).

## The traps

**On the dark file, `#2F55F0` is not a text colour.** 3.40:1 on the field and 2.75:1 on the callout tint. Use `#8CB8FF`. This is the single most likely mistake when moving a deck from the light file to the dark one, because on the light file the same hex is a perfectly legal 5.71:1.

**A `#2F55F0` fill takes white, not dark ink.** White on it is 5.71:1; `#101623` on it is 3.17:1 and fails below 24px. The CTA pill in the prototype is white-on-blue for exactly this reason.

**No categorical colour carries type, in either theme.** See the ramp section above. Set labels in ink or muted ink.

Full ratio tables: [`palette.md`](palette.md) and [`../../references/contrast.md`](../../references/contrast.md).

## Placeholders to replace

`{{ORG}}` · `{{UNIT}}` · `{{DECK_TITLE}}` · `{{DECK_TITLE_EN}}` · `{{CLASSIFICATION}}`

Take the values from the approved source the organisation maintains. This template encodes no organisational, product or positioning language by design. A delivered file containing `{{` is a defect.

## Before delivering

1. `officecli view deck.pptx issues`
2. `officecli view deck.pptx screenshot --grid --out contact.png`, then read the PNG
3. Eyebrow, title rule, footer, page number on every content slide
4. No Calibri, no off-palette colour, `font.ea` set for any 中文
5. On the dark file: no `#2F55F0` on a text run
6. In either file: no categorical colour on a text run
7. `grep -c '{{' ` → 0
8. `officecli close deck.pptx` before delivery
