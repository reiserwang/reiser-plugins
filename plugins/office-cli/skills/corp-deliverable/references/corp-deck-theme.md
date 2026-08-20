# corporate theme for deck-build

The machine-readable copy is `corp_theme.json` in this folder — load it rather than retyping. Every value is measured from `corporate_master_deck.pptx` and `reference_architecture.pptx` by frequency analysis of shape fills and text runs.

## Use it

```python
import sys, json
sys.path.insert(0, "<deck-build-skill>/scripts")
from deckbuild import Deck

THEME = json.load(open("<this-skill>/references/corp_theme.json"))

d = Deck(
    style="soft-rounded",          # the discipline; corporate overrides the identity
    density="text",                # board / investor. "balanced" for internal review
    canvas="16:9",
    footer="<Company>  ·  <deck title>",
    page_numbers=True,
    theme_overrides=THEME,
)
```

`deck-build` merges the override over the chosen style, so the style still supplies its geometry discipline where the override is silent. The override deliberately sets `geometry` too, because the house margin and gutter are measured values, not the style's defaults.

## Colour map

| deck-build key | house value | Where it came from |
|---|---|---|
| `accent` | `#0B318F` | ANA Blue — 25 shape fills, 99 text runs |
| `series[1]` | `#00A3E6` | Sky — eyebrows, accents, "future" framing |
| `bg` | `#FFFFFF` | Always. There is no coloured corporate master |
| `bg_alt` / `surface` | `#F0F6FC` | Panel tint — 37 fills, the default grouped-content surface |
| `rule_soft` | `#E6F2FC` | Callout band tint — 32 fills |
| `rule` | `#C3D6EE` | Hairlines, table borders |
| `ink` | `#1A2230` | Headline ink — 107 runs |
| `ink_soft` | `#5A6676` | Body ink — 163 runs, the most-used text colour in the deck |

Series order is the house categorical ramp: deep blue → sky → blue → purple → green → muted. There is no approved red or amber; if a deck genuinely needs a risk colour, ask rather than inventing one.

## Geometry — the pt ↔ px conversion

deck-build works in design pixels on a 1280×720 grid where `1px = 9,525 EMU`. `house-style` works in points on 960×540. **They are the same canvas.** Convert with **px = pt × 4/3**.

| House-style value (pt) | deck-build (px) | Meaning |
|---|---|---|
| 960 × 540 | 1280 × 720 | canvas |
| 37.4 | ~50 | left/right margin → `geometry.margin: 50` |
| 10.8 | 14.4 | base spacing unit |
| 13.7 | ~18 | card gutter → `geometry.gutter: 18` |
| 208.8 | 278.4 | four-card column width |
| 222.5 | ~297 | four-card column pitch |
| 241.2 | 321.6 | card height |
| 880.6 | ~1174 | content band width |

Because the margins agree, a deck-build page and a hand-built officecli page sit on the same grid — you can mix them in one file without visible drift.

## Type

deck-build takes **roles**, never raw sizes: `hero` `cover` `section` `quote` `title` `subtitle` `lead` `body` `annotation` `footnote`. The density setting drives the ramp. `density="text"` gives an 18px body — which is 13.5pt, close to the house style's 11.5–12.5pt body and much closer than `balanced` (22px ≈ 16.5pt) or `presentation` (28px ≈ 21pt).

That is the mechanical reason house decks use `text` density: it is the only setting whose ramp lands near the measured house scale. Choosing `presentation` does not just enlarge type — it reduces what each page can hold, which is wrong for a deck meant to be read.

## Fonts and CJK

```json
"heading": "Arial", "heading_alt": "微軟正黑體",
"body":    "Arial", "body_alt":    "微軟正黑體"
```

There is no font embedding in `.pptx` — only fonts installed on the recipient's machine render. Arial covers Latin everywhere; Arial has **no CJK glyphs**, so 中文 falls through to the alternate. Without a real CJK alternate set, Windows substitutes a serif (新細明體) and the deck looks wrong to every reviewer on a PC while looking fine on the Mac it was authored on.

微軟正黑體 (Microsoft JhengHei) ships with Windows and is the closest sans-serif match to the Mac-rendered look of the live decks. This is a documented deviation from `house-style`, which says Arial for both — that rule was derived from Mac-authored decks and does not survive contact with Word/PowerPoint on Windows.

## Contrast — verified ratios

deck-build's `check_deck.py` H4 rule: **≥4.5:1 below 24px, ≥3.0:1 at or above**.

| Foreground | On `#FFFFFF` | On `#F0F6FC` | Verdict |
|---|---|---|---|
| `#1A2230` ink | 15.96 | 14.67 | any size |
| `#0B318F` accent | 11.35 | 10.43 | any size |
| `#7C4DB8` purple | 5.82 | — | any size |
| `#5A6676` body ink | 5.84 | 5.36 | any size |
| `#2E5BF0` blue | 5.43 | — | any size |
| `#2FA84F` green | 3.07 | — | **≥24px only** |
| `#00A3E6` sky | **2.84** | — | **fails at every size** |
| `#FFFFFF` on `#0B318F` | 11.35 | — | any size |
| `#00A3E6` on `#0B318F` | 3.99 | — | ≥24px only |

**Sky is a fill colour, not a text colour.** It is correct for chart series, rules, icon badges and panel accents — the gate only measures text. When the sky hue is genuinely wanted for small text, `#00719E` preserves the hue at 5.45:1 on white and 5.00:1 on the panel tint.

The live corporate decks set 14pt sky eyebrows on white. Those would be flagged. Set new eyebrows in `#0B318F`, or in `#00719E` if the distinction from headings matters.

## Per-style notes

| Style | Use for | What the corporate override changes |
|---|---|---|
| `soft-rounded` | Default corporate, product, partner | Closest native match — rounded tinted cards are already the house pattern. Radius 18 matches the measured card corner. |
| `data-journalism` | investor briefing, financial results, market review | Ships `dark: true` on a `#0D1117` field. The override forces white; check the built deck, since this style's discipline assumes a dark ground. |
| `blueprint` | Reference architecture, systems | Keep its rule weights; the layer-band pattern in `house-style/references/slide-grid.md` maps onto it directly. |
| `swiss-minimal` | Vision, keynote, anniversary | Most type-led. Pair with `density="balanced"` — `text` density fights its whitespace. |

Avoid `memphis`, `pixel-art`, `zine`, `vintage-poster`, `chalkboard` and `paper-cut` for anything brand-facing. Their decoration density contradicts the house discipline, and the override cannot fix that — it only swaps identity, not geometry.
