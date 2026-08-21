# Canvas, grid and vertical rhythm

Shared by every template in `templates/`. The two templates are **geometrically identical** — a shape-by-shape diff across all 19 layouts finds zero differences in name, position, size, preset geometry or placeholder index. They also share one font scheme. Only colour differs, which is why a deck can be restyled from one to the other by swapping the master.

All values in **points**, measured from the shipping template files, not chosen.

## Canvas

| | |
|---|---|
| Size | **1440 × 810 pt** (16:9) — `cx=18288000 cy=10287000` EMU |
| Margin | **56** left and right |
| Content band | `x = 56 → 1384`, width **1328** |
| Gutter | **16.2** between columns |
| Background | template field colour, set on the master — never a picture, never a gradient. Four layouts override it: Cover, Section Divider and Closing sit on the accent field, Quote on the panel tint. |

`1440 × 810 pt` is 1.5× the conventional `960 × 540 pt` deck. If you are reading a size from a 960pt-canvas source, multiply by 1.5 before using it here.

## Column arithmetic

Every multi-column layout in the template derives from `band = 1328`, `gutter = 16.2`:

| Columns | Width | Pitch | x positions |
|---|---|---|---|
| 2 | 655.9 | 672.1 | 56, 728.1 |
| 3 | 431.9 | 448.1 | 56, 504.1, 952.1 |
| 4 | 319.9 | 336.1 | 56, 392.1, 728.1, 1064.2 |

`width(n) = (1328 − (n−1) × 16.2) / n`. Inner padding inside a panel is **16.2** on every side, so a panel's text box is `x + 16.2`, `w − 32.4`.

Asymmetric splits used by the template:

| Layout | Left | Right |
|---|---|---|
| Picture with Caption | picture `56, w 770.2` | caption `858.6, w 525.4` |
| Chart + Commentary | chart `56, w 823.4` | reading panel `895.6, w 488.4` |
| Big Number | number `56, w 610.9` | rationale `773.1, w 610.9`, divider rule at `x 720` |
| Project Status | label `72.2, w 398.4` | detail `507.5, w 823.4` |

## Vertical rhythm

```
0                                                                    1440
│                                                                      │
│  eyebrow          56,48   w 1328  h 24    20pt bold, accent          │  y 48
│  title            56,76   w 1328  h 56    30pt bold, ink             │  y 76
│  ─────────────── rule  56,142  w 1328  h 1.5  accent fill ───────────│  y 142
│                                                                      │
│  ┌ content band  y 172 → 692  (h 520) ────────────────────────────┐  │  y 172
│  │                                                                │  │
│  └────────────────────────────────────────────────────────────────┘  │
│  [below-content band: 606 / 646 / 706 depending on layout]           │
│  footer  56,772  w 929.6  h 22   13pt muted    page # 1324,772 w 60  │  y 772
└──────────────────────────────────────────────────────────────────────┘ 810
```

| Element | x | y | w | h |
|---|---|---|---|---|
| Eyebrow | 56 | 48 | 1328 | 24 |
| Title | 56 | 76 | 1328 | 56 |
| Title rule | 56 | 142 | 1328 | 1.5 |
| Content band | 56 | 172 | 1328 | 520 |
| Footer | 56 | 772 | 929.6 | 22 |
| Page number | 1324 | 772 | 60 | 22 |

Below-content bands, by layout:

| Purpose | y | h | Fill |
|---|---|---|---|
| Chart takeaway strip | 606 | 48 | callout tint |
| Chart source line | 668 | 22 | none |
| Diagram source / note | 646 | 34 | none |
| KPI takeaway band | 706 | 56 | callout tint |
| Table source line | 662 | 22 | none |

## Recurring shape vocabulary

| Element | Spec |
|---|---|
| Panel | `roundRect`, fill = panel tint; line = rule colour hairline only when the panel must read as a frame. **Corner radius is not uniform** — the shipped values run from 2.0 (header bands) through 4.5–4.7 (KPI takeaway, Project Status rows), 10.4–12.6 (Agenda, KPI cards, Incident panels), 18.4 (Diagram Frame) to 24.4–26.0 (Chart + Commentary, Two-Column panels). Read the radius off the layout you are matching rather than assuming one value. |
| Title rule | plain rectangle `h 1.5`, accent fill — a filled shape, not a line, so it renders identically everywhere |
| Accent spine | `4 × panel-height` rectangle on the panel's left edge, accent fill — used by Incident Detail and Project Status to code category |
| Divider rule | `1.5 × 260` vertical rectangle, rule colour — Big Number only |
| Cover / Section underline | `120 × 3` (Cover) or `100 × 3` (Section Divider), filled with the **field** colour — `#FFFFFF` in ANA Blue, `#F5F1ED` in Reiser Warm, not the ink colour. Closing has no underline. |
| Table header band | `h 38–40`, accent fill, reverse or charcoal text per the template's contrast table |
| Table row band | `h 44`, panel tint, with `h 0.75` rule-colour separators |

## Overflow — the one thing to check every time

Boxes in the template are sized for the copy they shipped with. A string that wraps overflows silently in the DOM.

Rule of thumb: a text box needs `lines × size × 1.45` points of height. `officecli view <file> issues` reports the exact shortfall and a `suggest.height` — take it rather than guessing.

The boxes most likely to need growing:

| Element | Shipped h | Trigger |
|---|---|---|
| Title (`56,76`) | 56 | any title wrapping to 2 lines at 30pt — grow to 84 and keep `y` |
| Agenda item | 54 | more than ~8 words at 18pt |
| Panel body | varies | more than ~20 words at 18pt |
| Cover title | 130 | more than 2 lines at 40pt |

Do not shrink type to make copy fit. Cut the copy, or move to a layout with more room.

## Converting to deck-build

`deck-build` works in design pixels on a **1280 × 720** grid where `1px = 9,525 EMU`. That grid is `960 × 540 pt`, so it is the same 16:9 shape as this canvas at 2/3 scale.

**px = pt × 8/9.**

| Template value (pt) | deck-build (px) | Meaning |
|---|---|---|
| 1440 × 810 | 1280 × 720 | canvas |
| 56 | 49.8 → **50** | margin → `geometry.margin: 50` |
| 16.2 | 14.4 → **14** | gutter → `geometry.gutter: 14` |
| 1328 | 1180.4 | content band width |
| 319.9 | 284.4 | four-column width |
| 30 (title) | 26.7 | title size |
| 18 (body) | 16 | body size |

Because the margins agree after conversion, a `deck-build` page and a hand-built officecli page sit on the same grid — you can mix them in one file without visible drift, provided you scale the deck-build output back up by 1.5 when the target canvas is 1440pt.

`deck-build` takes **roles**, never raw sizes: `hero` `cover` `section` `quote` `title` `subtitle` `lead` `body` `annotation` `footnote`. Density drives the ramp. `density="text"` gives an 18px body ≈ 13.5pt on a 960pt canvas ≈ 20pt here — the closest setting to the measured scale. That is the mechanical reason `text` is the default here. `balanced` (22px) is the right call for internal review decks and for `swiss-minimal`, whose whitespace discipline `text` density fights. `presentation` (28px) is for an actual stage — it does not merely enlarge type, it reduces what each page can hold, which is wrong for a deck meant to be read.
