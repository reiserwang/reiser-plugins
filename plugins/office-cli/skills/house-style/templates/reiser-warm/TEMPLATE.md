# Reiser Warm

The personal template. Warm-neutral field, charcoal ink, one coral accent, built on 60-30-10.

**Use for** personal work, drafts, internal thinking documents, methodology write-ups — anything not going out under the organisation's mark.
**Do not use for** brand-facing material; that is [`ana-blue`](../ana-blue/TEMPLATE.md). A brand-facing deliverable in this palette is an off-brand document, not a stylistic variation. Never mix the two in one file.

| | |
|---|---|
| File | [`reiser-warm.pptx`](reiser-warm.pptx) — 1 master, 19 layouts, 1 blank starter slide |
| Theme name | `Reiser Warm` |
| Canvas | 1440 × 810 pt |
| Field | `#F5F1ED` warm cream on the master. Four layouts override it: Cover / Section Divider / Closing on `#CC785C`, Quote on `#E8E4DF`. |
| Accent | `#CC785C` coral |
| deck-build override | [`theme.json`](theme.json) |
| Tokens and ratios | [`palette.md`](palette.md) |

Geometry is **identical** to `ana-blue` — a shape-by-shape diff across all 19 layouts finds zero differences in name, position, size, preset geometry or placeholder index, and both files share one font scheme. Only the colours differ, which is what makes restyling a deck between the two a master swap rather than a rebuild. See [`../../references/layouts.md`](../../references/layouts.md) and [`../../references/grid.md`](../../references/grid.md).

## Start here

```bash
cp reiser-warm.pptx deck.pptx
officecli open deck.pptx
officecli add deck.pptx slide --layout 'Title and Content'
```

## The 60-30-10 split

The rule is about *area*, not importance. Sixty percent is the surface you barely notice; ten percent is the thing you notice first.

- **60% field** — `#F5F1ED` cream, `#F5F3F1` lifted, `#E8E4DF` inset, `#D4D0C9` rules. Their separation is deliberately low; cream against warm grey is 1.13:1. The neutrals are one family, and the eye should not be asked to parse them as distinct zones. If you need a hard boundary, use a Stone rule, not a fill change.
- **30% supporting** — charcoal `#1F1E1D` ink, muted `#5C5650`, sage mist `#B3CBC1` as tint.
- **10% accent** — coral `#CC785C`. One accent per page. Ten percent is a ceiling, not a target: a page with no coral is fine; a page with coral in four places has no accent, only decoration.

## Type scale

Arial for Latin, 微軟正黑體 for 中文. Same scale as `ana-blue` — see [`palette.md`](palette.md) § Typography. Sizes are on the 1440pt canvas; the upstream ≥36pt title rule assumes a 960pt projected deck and does not apply.

| Element | Size | Weight | Colour |
|---|---|---|---|
| Cover / Section / Closing title | 40 / 34pt | bold | `#1F1E1D` — **charcoal on the coral field** |
| Slide title | 30pt | bold | `#1F1E1D` |
| Big Number · KPI value | 96 / 54pt | bold | `#9D5C47` |
| Eyebrow | 20pt | bold | `#9D5C47` |
| Quote opening glyph | 130pt | bold | `#9D5C47` |
| Body | 18pt | regular | `#1F1E1D` body, `#5C5650` supporting |
| Footer, page number, source | 13pt | regular | `#5C5650` |

## Two traps — read before using coral

**Coral is a fill colour, not a text colour.** `#CC785C` on the cream field is 2.92:1 and fails at every size. Use `#9D5C47` (4.61:1) when the coral hue must carry text — which is why every eyebrow and big number in this template is `#9D5C47`, not `#CC785C`.

**A coral fill takes charcoal text, not white.** This is the counterintuitive one:

| Combination | Ratio | Verdict |
|---|---|---|
| White `#FFFFFF` on coral | 3.28 | ≥ 24px only — a coral button with a white label fails |
| Cream `#F5F1ED` on coral | 2.92 | fails at every size |
| **Charcoal `#1F1E1D` on coral** | **5.08** | **any size — use this** |

Coral is a mid-tone; it wants dark text. The Cover, Section Divider, Closing and Action Items header in this template all set charcoal on coral for exactly this reason. If you hand-build an accent-filled block with `deck-build`, use `d.accent_pair("body")` and let the builder resolve it rather than hardcoding white — `accent_ink` is charcoal in `theme.json`, not the usual white.

## Standing furniture

| Element | Position | Spec |
|---|---|---|
| Eyebrow | `56, 48` | 20pt bold `#9D5C47`, bilingual, ` · `-separated, 中文 leading — same strings as `ana-blue` |
| Title | `56, 76` | 30pt bold `#1F1E1D` |
| Title rule | `56, 142`, `1328 × 1.5` | filled rectangle, `#CC785C` |
| Footer | `56, 772` | 13pt `#5C5650` — `{{ORG}}  \|  {{DECK_TITLE}}` |
| Page number | `1324, 772` | 13pt `#5C5650`, right-aligned |

Three layouts substitute their own furniture: **Cover**, **Section Divider** and **Closing** are full-bleed `#CC785C` with charcoal `#1F1E1D` text; Cover and Section Divider carry a short **cream `#F5F1ED`** underline rule (`120 × 3` and `100 × 3`), and Closing carries none. Two more ship deliberately bare: **Quote** (warm-grey `#E8E4DF` field, a 130pt `#9D5C47` opening glyph, footer and page number only) and **Blank** (title rule, footer and page number only).

One substitution is **not** a straight swap. The Two-Column Compare "Before" band is muted ink `#5C5650`, not the accent — charcoal on it is 2.30:1 and fails, so its label is cream `#F5F1ED` (6.44:1), exactly as ANA Blue uses white there. "Coral takes dark text" applies to the coral band only.

## Style disciplines that suit this field

With `deck-build`: `editorial` (long-form, type-led), `swiss-minimal` (structural), `soft-rounded` (approachable), `ink-notes` (methodology, before/after). Avoid the dark styles — `dark-tech`, `data-journalism`, `chalkboard` — since the override forces a light field and their discipline assumes a dark ground.

## Placeholders to replace

`{{ORG}}` · `{{UNIT}}` · `{{DECK_TITLE}}` · `{{DECK_TITLE_EN}}` · `{{CLASSIFICATION}}`

A delivered file containing `{{` is a defect.

## Before delivering

1. `officecli view deck.pptx issues`
2. `officecli view deck.pptx screenshot --grid --out contact.png`, then read the PNG
3. Coral appears in at most one place per page, and never as small text
4. No white-on-coral text below 24px
5. `font.ea` set for any 中文
6. `grep -c '{{'` → 0
7. `officecli close deck.pptx` before delivery
