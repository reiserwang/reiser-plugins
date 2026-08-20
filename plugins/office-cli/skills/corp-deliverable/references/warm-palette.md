# Warm Neutral — house palette (60-30-10)

A personal warm-neutral identity, separate from the Corporate Blue corporate palette. Use it for personal work, drafts, internal thinking documents, and anything not going out under the <Company> mark. **Never mix the two in one deliverable** — they have different fields (warm cream vs pure white) and the mixture reads as a mistake, not a blend.

Machine-readable: `warm_theme.json` in this folder, a drop-in `theme_overrides` for `deck-build`.

## The 60-30-10 split

The rule is about *area*, not importance. Sixty percent is the surface you barely notice; ten percent is the thing you notice first.

### 60% — the field

The page is warm-neutral. These four carry the surface and almost never carry text.

| Token | Hex | Role |
|---|---|---|
| Warm cream | `#F5F1ED` | The default page. Everything else sits on this. |
| Cool white | `#F5F3F1` | Lifted surface — a card that should read as *above* the page. |
| Warm grey | `#E8E4DF` | Inset surface — a sidebar, a code block, a quiet band. |
| Stone | `#D4D0C9` | Rules, borders, table gridlines, dividers. |

Their separation is deliberately low — cream against warm grey is 1.13:1. That is the point: the neutrals are a single family, and the eye should not be asked to parse them as distinct zones. If you need a hard boundary, use a Stone rule, not a fill change.

### 30% — the supporting layer

| Token | Hex | On cream | Role |
|---|---|---|---|
| Charcoal | `#1F1E1D` | **14.81:1** | Primary ink. Headings and body. The workhorse. |
| Warm grey ink | `#5C5650` | **6.44:1** | Secondary ink — captions, labels, sources, footers. |
| Sage mist | `#B3CBC1` | 1.53:1 | Supporting tint. Fill only, never text. |

`#5C5650` is a derived value, not from the original swatch. The swatch had no readable secondary text colour — every colour in it either sits at 14.81:1 (charcoal) or fails as small text. A palette needs a muted ink between those, or every caption ends up either shouting or illegible. This one clears 4.5:1 on all three neutral surfaces including Stone (4.71:1).

### 10% — the accent

| Token | Hex | Role |
|---|---|---|
| Coral | `#CC785C` | The one accent. Fills, badges, the emphasised row, the single highlighted number, chart series 1. |
| Coral deep | `#9D5C47` | Derived text-safe variant — 4.61:1 on cream. Use when coral must be *text*. |

One accent per page. The ten percent is a ceiling, not a target — a page with no coral at all is fine; a page with coral in four places has no accent, only decoration.

## Two traps — read before using coral

**Coral is a fill colour, not a text colour.** `#CC785C` on the cream field is **2.92:1** and fails at every size. Use `#9D5C47` when the coral hue must carry text.

**A coral fill takes charcoal text, not white.** This is the counterintuitive one:

| Combination | Ratio | Verdict |
|---|---|---|
| White `#FFFFFF` on coral | **3.28** | ≥24px only — a coral button with a white label fails |
| Cream `#F5F1ED` on coral | 2.92 | Fails at every size |
| **Charcoal `#1F1E1D` on coral** | **5.08** | **Any size — use this** |

The instinct to put white on a saturated fill is wrong here. Coral is a mid-tone; it wants dark text.

## Extended categorical

For charts and multi-category coding. As *fills* they are all fine — the contrast gate only measures text. As text on cream, none of them clear 4.5:1, so each has a derived text-safe variant.

| Name | Fill | On cream | Text-safe variant | Variant ratio |
|---|---|---|---|---|
| Coral | `#CC785C` | 2.92 | `#9D5C47` | 4.61 |
| Blue | `#5C7B9C` | 3.92 | `#557190` | 4.50 |
| Sage | `#6B8E5C` | 3.31 | `#59764C` | 4.54 |
| Gold | `#C28E3D` | 2.58 | `#8C662C` | 4.61 |
| Violet | `#8B7BAB` | 3.39 | `#756790` | 4.56 |
| Teal | `#5C9C8E` | 2.83 | `#46776C` | 4.54 |
| Mauve | `#B07A9C` | 3.06 | `#8B607B` | 4.61 |
| Tan | `#8C7355` | 3.98 | `#816A4E` | 4.55 |

Chart series order in the theme is Coral → Blue → Sage → Gold → Violet → Teal, which alternates warm and cool so adjacent series separate. Mauve and Tan are held back for a seventh and eighth category; needing them usually means the chart should be split.

## Use with deck-build

```python
import sys, json
sys.path.insert(0, "<deck-build-skill>/scripts")
from deckbuild import Deck

WARM = json.load(open("<this-skill>/references/warm_theme.json"))

d = Deck(style="editorial", density="balanced",
         footer="the maintainer  ·  <title>",
         theme_overrides=WARM)
```

Style disciplines that suit a warm neutral field: `editorial` (long-form, type-led), `swiss-minimal` (structural), `soft-rounded` (approachable), `ink-notes` (methodology, before/after). Avoid the dark styles — `dark-tech`, `data-journalism`, `chalkboard` — since the override forces a light field and their discipline assumes a dark ground.

`accent_ink` is set to charcoal in the JSON rather than the usual white, for the reason above. If you hand-build an accent-filled block, use `d.accent_pair("body")` and let the builder resolve it rather than hardcoding white.

## Use in Word and Excel

| Element | Spec |
|---|---|
| Page / sheet background | `#F5F1ED` warm cream |
| Body text | Arial 10.5pt `#1F1E1D` |
| Caption, footnote, source | Arial 9pt `#5C5650` |
| Heading 1 / 2 | `#1F1E1D`, weight carries the hierarchy, not colour |
| Table header row | fill `#E8E4DF`, charcoal bold text — *not* a coral fill |
| Table banding | `#F5F3F1` |
| Borders | `#D4D0C9` hairline |
| Emphasised row / total | fill `#CC785C` with **charcoal** text, or a `#CC785C` top border only |
| Hyperlink | `#557190` (text-safe blue) |

Set `font.ea` to 微軟正黑體 alongside Arial for any 中文 content — Arial has no CJK glyphs and Windows falls back to a serif otherwise.

## Verification

Every ratio on this page was computed against WCAG relative luminance, not estimated. Re-run after any change:

```python
def lum(h):
    h=h.lstrip('#'); c=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    c=[x/12.92 if x<=0.03928 else ((x+0.055)/1.055)**2.4 for x in c]
    return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]
def cr(a,b):
    l1,l2=sorted([lum(a),lum(b)],reverse=True); return (l1+0.05)/(l2+0.05)
```

`deck-build`'s gate is ≥4.5:1 below 24px and ≥3.0:1 at or above. `check_deck.py` enforces it; `officecli view <file> issues` flags low contrast in built files.
