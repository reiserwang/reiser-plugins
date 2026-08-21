# Yukima 雪間

The seasonal template. Cool blue-grey field, slate accent, an earth-and-growth categorical ramp, built on 60-30-10.

**雪間** (*yukima*) is the early-spring word for the patches of bare ground that appear as snow melts — a kigo, a seasonal word. It is what this palette does: snow-blues giving way to emerging greens and warm earth. The source swatches carry their own seasonal names, and they are kept: 雪解け snowmelt, 寒の戻り the cold's return, 常磐木 evergreen, 萌黄 fresh bud, 三寒四温 three cold days and four warm, 憩い repose.

**Use for** material that wants a quieter, more natural register than [`ana-blue`](../ana-blue/TEMPLATE.md) without dropping to a personal one — research write-ups, ESG and sustainability reporting, long-form analysis, anything where the subject is the natural world or the audience is not a boardroom.
**Do not use for** anything that must carry the organisation's primary mark; that is `ana-blue`. Never mix templates in one file.

| | |
|---|---|
| File | [`yukima.pptx`](yukima.pptx) — 1 master, 19 layouts, 1 blank starter slide |
| Theme name | `Yukima` |
| Canvas | 1440 × 810 pt |
| Field | `#F1F6FA` 寒の戻り on the master. Four layouts override it: Cover / Section Divider / Closing on `#4B6F87`, Quote on `#C8DAE8` 雪解け. |
| Accent | `#4B6F87` dark blue, with `#558860` 常磐木 as a second fill |
| deck-build override | [`theme.json`](theme.json) |
| Tokens and ratios | [`palette.md`](palette.md) · [`../../references/contrast-matrix.md`](../../references/contrast-matrix.md) |

Geometry is **identical** to `ana-blue` and `reiser-warm` — same 19 layouts, same names, same order, same coordinates, same font scheme. Only the colours differ.

## Start here

```bash
cp yukima.pptx deck.pptx
officecli open deck.pptx
officecli add deck.pptx slide --layout 'Title and Content'
```

## The 60-30-10 split

- **60% field** — `#F1F6FA` page (寒の戻り), `#F5F3F1` lifted, `#C8DAE8` inset (雪解け), `#AACEE7` rules, plus `#CAD2C4` sage for inactive states. Their separation is 1.02–1.52:1, so the tints read as one family, the same discipline the other two templates hold. For a hard boundary use an `#AACEE7` rule, not a fill change.
- **30% supporting** — `#22333D` headline ink and `#3B576A` muted ink, both **derived** (see below), plus `#4B6F87` where the blue is type at 4.92:1.
- **10% accent** — `#4B6F87` as area, with `#558860` 常磐木 as a second fill. One accent per page; ten percent is a ceiling, not a target.

As in `ana-blue`, the accent is text-safe, so `#4B6F87` sits in two bands: supporting when it is type, accent when it is area. The ceiling governs area.

**Cover, Section Divider and Closing** are full-bleed `#4B6F87` — the deliberate exception, as in both other templates.

## Two derived inks — the source palette has none

This is the one substantive way Yukima differs from the other two templates, and it is worth understanding before you extend the palette.

**The fifteen source colours contain no ink.** The darkest is `#4B6F87` at 4.92:1 on the field — enough for body text, nowhere near the ≥7:1 a heading wants or the ≥12:1 the other two templates give their headlines. Nine of the fifteen are fill-only. So two inks are derived by darkening the `#4B6F87` hue (H 197.8°, S 0.317) without shifting it:

| Token | Hex | On field | Role |
|---|---|---|---|
| Headline ink | `#22333D` | **12.00** | Titles, body, panel body. Matches `#1A2230`'s 15.96 and `#1F1E1D`'s 14.81 in spirit if not in number. |
| Muted ink | `#3B576A` | **7.00** | Captions, footers, source lines, the Two-Column "Before" band. |

Both are same-hue derivations, so the page still reads as one blue family. This mirrors what `reiser-warm` had to do for `#5C5650`: a palette assembled as a swatch board usually has no readable secondary ink, and one has to be built.

## Three traps

**Nothing in the source palette carries white text comfortably.** The best is the accent itself, `#4B6F87` at 5.35:1. 常磐木 `#558860` is 4.14 (display sizes only), ochre `#BD7E1A` is 3.41, 萌黄 `#86B655` is 2.38. Table header bands therefore use the accent or the muted ink `#3B576A` (white on it is 7.62:1), never a green or gold fill.

**萌黄 and gold take dark text, not white** — the coral trap again, for the same reason: both are mid-tones.

| Fill | White on it | Ink `#22333D` on it | Use |
|---|---|---|---|
| `#4B6F87` accent | **5.35** | 2.44 | white |
| `#3B576A` muted ink | **7.62** | 1.42 | white |
| `#558860` 常磐木 | 4.14 | 3.16 | white, ≥ 24px only |
| `#BD7E1A` ochre | 3.41 | 3.83 | either, ≥ 24px only |
| `#86B655` 萌黄 | 2.38 | **5.49** | **ink** |
| `#D2AD52` gold | 2.13 | **6.12** | **ink** |

**常磐木 is not text at body size.** 3.80:1 on the field. Use the derived `#4D7B57` (4.50) when the green must be type.

## Type scale

Same scale as the other templates — see [`palette.md`](palette.md) § Typography.

| Element | Size | Weight | Colour |
|---|---|---|---|
| Cover / Section / Closing title | 40 / 34pt | bold | `#FFFFFF` on the accent field |
| Slide title | 30pt | bold | `#22333D` |
| Big Number · KPI value | 96 / 54pt | bold | `#4B6F87` |
| Eyebrow | 20pt | bold | `#4B6F87` |
| Quote opening glyph | 130pt | bold | `#4B6F87` |
| Body | 18pt | regular | `#22333D` body, `#3B576A` supporting |
| Footer, page number, source | 13pt | regular | `#3B576A` |

## Standing furniture

| Element | Position | Spec |
|---|---|---|
| Eyebrow | `56, 48` | 20pt bold `#4B6F87`, bilingual, ` · `-separated, 中文 leading |
| Title | `56, 76` | 30pt bold `#22333D` |
| Title rule | `56, 142`, `1328 × 1.5` | filled rectangle, `#4B6F87` |
| Footer | `56, 772` | 13pt `#3B576A` — `{{ORG}}  \|  {{DECK_TITLE}}` |
| Page number | `1324, 772` | 13pt `#3B576A`, right-aligned |

Quote sits on `#C8DAE8` 雪解け with a 130pt `#4B6F87` opening glyph, footer and page number only. Blank carries the title rule, footer and page number only.

## Provenance

The fifteen source colours came from a Japanese-authored swatch board, supplied as a screenshot. Sampling that screenshot gave values ~2–3% off the printed labels, so **the labels are the tokens** and the sampled pixels were discarded. Two labels were initially illegible and were reconstructed by fitting the screenshot's colour shift across the thirteen readable cells; both were subsequently confirmed against a clearer capture — `#4B6F87` (reconstruction was within 6/255) and `#7C754F` (within 6/255). No token in this template is an estimate.

## Placeholders to replace

`{{ORG}}` · `{{UNIT}}` · `{{DECK_TITLE}}` · `{{DECK_TITLE_EN}}` · `{{CLASSIFICATION}}`

A delivered file containing `{{` is a defect.

## Before delivering

1. `officecli view deck.pptx issues`
2. `officecli view deck.pptx screenshot --grid --out contact.png`, then read the PNG
3. No white text on a 萌黄 or gold fill, and no 常磐木 text below 24px
4. The accent appears as area in at most one place per page
5. `font.ea` set for any 中文
6. `grep -c '{{'` → 0
7. `officecli close deck.pptx` before delivery
