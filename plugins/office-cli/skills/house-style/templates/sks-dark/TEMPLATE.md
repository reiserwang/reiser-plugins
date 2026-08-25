# SKS Dark

The dark-field template. Midnight navy field, amber accent, the same dense analyst-style pages as [`ana-blue`](../ana-blue/TEMPLATE.md), built on 60-30-10.

**Use for** screen-first material where a dark field is the point: on-stage and on-screen decks, product and platform walkthroughs, launch and demo sets, operations and monitoring views, and anything shown next to dark UI or video.
**Do not use for** printed or PDF-distributed board, regulator and investor material — a dark field costs ink and washes out on office printers. That is [`ana-blue`](../ana-blue/TEMPLATE.md). Never mix the two in one file.

| | |
|---|---|
| File | [`sks-dark.pptx`](sks-dark.pptx) — 1 master, 19 layouts, 1 blank starter slide |
| Theme name | `SKS Dark` |
| Canvas | 1440 × 810 pt |
| Field | `#1A293A` on the master. Four layouts override it: Cover / Section Divider / Closing on `#8A5613`, Quote on `#213040`. |
| Accent | `#B57319` amber, with `#CCA348` gold as type and `#8A5613` as field |
| deck-build override | [`theme.json`](theme.json) |
| Tokens and ratios | [`palette.md`](palette.md) |

## Start here

```bash
cp sks-dark.pptx deck.pptx
officecli open deck.pptx
officecli add deck.pptx slide --layout 'Cover'
```

Layout names, placeholder indices and geometry are identical to the other three templates — [`../../references/layouts.md`](../../references/layouts.md) and [`../../references/grid.md`](../../references/grid.md) apply unchanged. This template differs **only in colour**, which is what makes restyling a deck into or out of it a master swap rather than a rebuild.

## Where the colours come from

Every token except three was sampled from the two reference comps, not invented: the cover comp supplied the field, the ink and the amber; the agenda comp supplied the row hairline, the four category-spine colours and the inactive grey. The three exceptions are marked *(derived)* below and in [`palette.md`](palette.md), each one a value-shift of a sampled colour that failed the contrast gate in the role it was being asked to play.

## The 60-30-10 split

The rule is about *area*, not importance. Sixty percent is the surface you barely notice; ten percent is the thing you notice first. On a dark field the arithmetic is unchanged but the direction inverts: the field is the darkest thing on the page and every tint steps *up* from it.

- **60% field** — `#1A293A` midnight, `#213040` panel, `#273546` callout, `#3E4C5A` rules, plus `#546D85` and `#5D6874` as muted fills for inactive states. Their separation is deliberately low: midnight against panel is 1.10:1, panel against callout 1.08:1. The tints are one family, and the eye should not be asked to parse them as distinct zones. If you need a hard boundary, use a `#3E4C5A` rule, not a fill change.
- **30% supporting** — `#F4F1EF` headline ink (13.13:1 on the field), `#A9B2BB` muted ink (6.87:1), and gold `#CCA348` *as text* (6.26:1).
- **10% accent** — amber `#B57319` *as area* — title rules, category spines, badges — plus amber deep `#8A5613` for bands and fields that carry light ink. One accent per page. Ten percent is a ceiling, not a target: a page with no amber fill at all is fine; a page with four amber blocks has no accent, only decoration.

**The accent sits in three steps, and this is where SKS Dark diverges from every light template.** On a dark field a single mid-chroma warm cannot do all three jobs at once, so the hue is held and the value moved:

| Step | Hex | Job | Why this step and not another |
|---|---|---|---|
| Amber | `#B57319` | Title rules, category spines, badges, chart series 1 — **area that carries no type** | 3.82:1 on the field. Legal as a graphic element, illegal as small text. |
| Gold | `#CCA348` | Eyebrows, section titles, panel headings, big numbers, links — **the accent as type** | 6.26:1 on the field and 5.29:1 on the callout tint, so it holds on all three surfaces. Also takes `#1A293A` ink at 6.26:1 when used as a filled block. |
| Amber deep *(derived)* | `#8A5613` | Cover / Section Divider / Closing fields, table header bands — **accent area carrying light text** | 5.46:1 under `#F4F1EF`. `#B57319` would be 3.44:1 there and fail. |

Both `#B57319` and `#CCA348` are sampled values — the reference agenda comp uses them as adjacent spine colours, which is the same relationship at a smaller scale.

**Cover, Section Divider and Closing are the deliberate exception** — full-bleed `#8A5613`, 100% accent area. The ceiling is a per-content-page rule; those three layouts exist to spend the accent all at once.

## Category spines and chart series

The reference agenda comp establishes the ramp: a rotating set of low-chroma spines against the navy, warm and cool alternating so adjacent rows separate without any of them shouting. Nine steps, in this order:

| # | Token | Hex | On field | Use |
|---|---|---|---|---|
| 1 | amber | `#B57319` | 3.82 | series 1, primary spine — **area only** |
| 2 | gold | `#CCA348` | 6.26 | series 2, and the accent as type |
| 3 | steel | `#698EB1` | 4.29 | series 3 — area and display type only |
| 4 | deep steel | `#546D85` | 2.74 | series 4 — **area only** |
| 5 | grey | `#5D6874` | 2.60 | inactive / unshipped states — **area only** |
| 6 | steel light *(derived)* | `#8FA9C4` | 6.08 | the text-safe steel, for labels in the steel hue |
| 7 | teal | `#5FB3AA` | 5.99 | series 5 |
| 8 | violet | `#A79EDA` | 6.01 | series 6 |
| 9 | sage | `#8FB07E` | 6.10 | series 7 |

Steps 1–5 are sampled from the comps; 6–9 extend the ramp for charts that need more than five series, pitched at the same value so no series jumps forward. Do not extend the list further, and do not use a categorical colour as page furniture — a chart is data, not furniture.

**There is still no approved alert colour.** Amber is the accent here, so it cannot double as a caution mark the way it might in a light template, and none of the cool steps read as danger. If a deliverable genuinely needs risk or alert coding, ask rather than inventing one.

## Type scale

Arial for Latin, 微軟正黑體 for 中文. Bold is the only weight variation — no italics, no letter-spacing tricks, no all-caps runs longer than three words. Sizes are unchanged from `ana-blue`; only the colours move.

| Element | Size | Weight | Colour |
|---|---|---|---|
| Cover title | 40pt | bold | `#F4F1EF` |
| Section / Closing title | 34pt | bold | `#F4F1EF` |
| Slide title | 30pt | bold | `#F4F1EF` |
| Quote opening glyph | 130pt | bold | `#CCA348` |
| Quote body | 28pt | regular | `#F4F1EF` |
| Big Number | 96pt | bold | `#CCA348` |
| KPI value | 54pt | bold | `#CCA348` |
| Eyebrow | 20pt | bold | `#CCA348` |
| Cover subtitle · takeaway · rationale | 21pt | regular | `#F4F1EF` |
| Panel heading, table header | 18pt | bold | `#CCA348`, or `#F4F1EF` on an `#8A5613` band |
| Body — the workhorse | 18pt | regular | `#F4F1EF` body, `#A9B2BB` supporting |
| Footer, page number, source line | 13pt | regular | `#A9B2BB` |

These are sizes on a **1440pt** canvas. On a conventional 960pt canvas they are 2/3 of these numbers — a 30pt title here is a 20pt title there. The upstream OfficeCLI pptx skill's ≥36pt title rule assumes a projected 960pt deck and **does not apply**: override it.

**One dark-field typographic rule the light templates do not need.** Light type on a dark ground blooms — strokes read heavier than they measure. Do not add bold to body copy to compensate; if a line is not reading, it is a colour problem (`#A9B2BB` where `#F4F1EF` belongs, or `#727C86` where `#A9B2BB` belongs), not a weight problem.

## Standing furniture

Fourteen of the nineteen layouts carry all five. Omitting any of them on those layouts is an incomplete deliverable; the five exceptions are listed below.

| Element | Position | Spec |
|---|---|---|
| Eyebrow | `56, 48` | 20pt bold `#CCA348`, bilingual, ` · `-separated. The shipped eyebrows lead with 中文 — `風險 · RISK`, `數據 · DATA` — except `AGENDA · 議程`. |
| Title | `56, 76` | 30pt bold `#F4F1EF` |
| Title rule | `56, 142`, `1328 × 1.5` | filled rectangle, `#B57319` |
| Footer | `56, 772` | 13pt `#A9B2BB` — `{{ORG}}  \|  {{DECK_TITLE}}` |
| Page number | `1324, 772` | 13pt `#A9B2BB`, right-aligned |

Three layouts substitute their own furniture: **Cover**, **Section Divider** and **Closing** are full-bleed `#8A5613` with `#F4F1EF` reverse-ink text; Cover and Section Divider carry a short `#F4F1EF` underline rule (`120 × 3` and `100 × 3`), Closing carries none, and the classification marking appears on Cover only. Two more ship deliberately bare: **Quote** (panel-tint `#213040` field, footer and page number only) and **Blank** (title rule, footer and page number only).

## The two traps

**Amber `#B57319` is a fill colour, not a text colour.** 3.82:1 on the field — legal as a rule, a spine or a chart bar, illegal as an eyebrow, a label or any type below 24px. Substitute `#CCA348`, which is the same warm two steps up at 6.26:1. The template's own eyebrows are `#CCA348` for exactly this reason; a comp that sets amber eyebrows in `#B57319` would be flagged, so do not carry that pattern forward.

**`#727C86` is the reference's secondary grey and it fails as body text.** 3.48:1 on the field, 2.81:1 on the callout tint. It is the dark-field twin of ANA Blue's `#647084`. Use it for hairlines and inactive marks only; the muted ink is `#A9B2BB`, which holds 5.80 even on the callout tint.

Full ratio table: [`palette.md`](palette.md) and [`../../references/contrast.md`](../../references/contrast.md).

## Placeholders to replace

`{{ORG}}` · `{{UNIT}}` · `{{DECK_TITLE}}` · `{{DECK_TITLE_EN}}` · `{{CLASSIFICATION}}`

Take the values from the approved source the organisation maintains. This template encodes no organisational, product or positioning language by design. A delivered file containing `{{` is a defect.

## Before delivering

1. `officecli view deck.pptx issues`
2. `officecli view deck.pptx screenshot --grid --out contact.png`, then read the PNG — a dark field hides overflow and mis-set ink far better than a white one does
3. Eyebrow, title rule, footer, page number on every content slide
4. No Calibri, no off-palette colour, `font.ea` set for any 中文
5. No `#B57319` and no `#727C86` on a text run
6. `grep -c '{{' ` → 0
7. `officecli close deck.pptx` before delivery
