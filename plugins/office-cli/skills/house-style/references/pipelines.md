# Pipelines

Three ways to produce a styled deliverable. Pick before producing.

---

## Pipeline 0 — start from the template (preferred for decks)

The template `.pptx` carries the master, the theme, the 19 layouts and the placeholder scaffolding. Copying it is faster and more faithful than rebuilding, and it is the only route that inherits the master and theme.

```bash
cp templates/ana-blue/ana-blue.pptx deck.pptx
officecli open deck.pptx
officecli query deck.pptx 'slideLayout' --json          # confirm the 19 layouts arrived
officecli add  deck.pptx slide --layout 'Title and Content'
```

Then fill placeholders by index — the indices are in [`layouts.md`](layouts.md). Replace `{{ORG}}`, `{{UNIT}}`, `{{DECK_TITLE}}`, `{{DECK_TITLE_EN}}` and `{{CLASSIFICATION}}` on the layouts you use, and delete the starter blank slide when the deck is built.

Confirm property names against `officecli help pptx shape` before trusting `line.color`, `valign` or `align` — those aliases are the ones most likely to have drifted from the bundled reference.

---

## Pipeline A — new deck with a bespoke narrative

Use when the template's layouts do not fit the argument — a keynote, a launch moment, a narrative arc that needs its own page shapes.

### A1. Design

Run `deck-design`. It fixes the communication contract, picks a narrative mode, density and visual style, then writes `deck_spec.md`.

Two of its choices are pre-decided here — override its defaults:

**Density.** These decks are read on a laptop or printed, not projected. Use `text` for board, regulator, investor and analyst material; `balanced` for internal review. Reserve `presentation` for an actual stage.

**Visual style.** Pick the *discipline*, then swap in the template identity:

| Occasion | Style discipline |
|---|---|
| Standard corporate, product, partner-facing | `soft-rounded` — matches the rounded tinted panels the templates use |
| Financial results, investor briefing, market or performance review | `data-journalism` — **ANA Blue only**, and with `dark: false` from the override, since the style ships a dark field. Reiser Warm forbids it: its `theme.json` `never` list rules out the dark styles because forcing a light field leaves their discipline without the ground it assumes. On a warm field use `editorial` instead. |
| Architecture, reference architecture, systems walkthrough | `blueprint` |
| Vision, keynote, launch moment | `swiss-minimal`, paired with `density="balanced"` — `text` density fights its whitespace |

Avoid `memphis`, `pixel-art`, `zine`, `vintage-poster`, `chalkboard` and `paper-cut` for anything brand-facing. Their decoration density contradicts the house discipline, and a theme override cannot fix that — it swaps identity, not geometry.

**Positioning language is out of scope for this plugin.** Product, roadmap and market claims are not encoded here. Take them from the approved source the organisation maintains. Getting this wrong in the spec propagates into every slide.

### A2. Build with the template theme

```python
import sys, json
sys.path.insert(0, "<deck-build-skill>/scripts")
from deckbuild import Deck

THEME = json.load(open("<house-style-skill>/templates/ana-blue/theme.json"))

d = Deck(
    style="soft-rounded",         # the discipline; the theme supplies the identity
    density="text",               # board / investor. "balanced" for internal review
    canvas="16:9",
    footer="{{ORG}}  |  {{DECK_TITLE}}",   # pipe, as in the shipped layouts
    page_numbers=True,
    theme_overrides=THEME,
)
```

`deck-build` merges the override over the chosen style, so the style still supplies its geometry discipline where the override is silent. The override sets `geometry` too, because the margin and gutter are measured values, not the style's defaults.

Unit conversion between the two canvases is in [`grid.md`](grid.md) § Converting to deck-build — **px = pt × 8/9**.

### A3. Finish pass with officecli

`deck-build` has no image ingestion for brand marks and no template ingestion. After `save()`:

```bash
officecli view deck.pptx issues
officecli view deck.pptx screenshot --grid --out contact.png   # then read the PNG
```

Add any locked wordmark artwork by copying it from an existing file rather than redrawing it, or accept a text-set masthead if speed matters more than fidelity.

### A4. Gate

Both checkers must pass, and they check different things:

```bash
python3 <deck-build-skill>/scripts/check_deck.py deck.pptx   # overflow, collision, contrast
officecli view deck.pptx issues                              # low contrast, stale fields, broken refs
officecli close deck.pptx                                    # flush before delivery
```

---

## Pipeline B — documents and workbooks

`docx-cli` / `xlsx-cli`, with the template's `palette.md` loaded. The one thing that catches people out:

**Word on Windows needs a real CJK face.** Arial carries no CJK glyphs, so Word on Windows falls back to a serif (新細明體) and the document looks wrong to every reviewer on a PC. Set both:

```
--prop font.latin=Arial --prop font.ea=微軟正黑體
```

Same split in a `deck-build` theme: `"heading": "Arial", "heading_alt": "微軟正黑體"`. This is a documented deviation from a naive "Arial everywhere" reading of the house style — that reading was derived from Mac-authored files and does not survive contact with Office on Windows.

Word and Excel token mappings are at the bottom of each template's `palette.md`.
