---
name: corp-deliverable
description: Universal entry point for any corporate deliverable — decks, reports, memos, board papers, 簽呈, workbooks. Routes the request to the right tool (deck-design/deck-build for new decks, the officecli skills for editing existing files, slideland for visual vocabulary) and applies house style across all of them. Use whenever the user asks for a presentation, deck, report, document, workbook or meeting record, or says "on-brand", "in our style", "for the board" or "for the investor briefing".
---

# corporate deliverable — router

One entry point. Read the request, pick the pipeline, apply the house style. Do not start producing before the route is settled — a deck built with the wrong tool has to be rebuilt, not patched.

## Route first

| What the user wants | Route |
|---|---|
| A **new deck** from a brief, source docs or data | `deck-design` → `deck-build` → officecli finish pass (§ Pipeline A) |
| **Edit / restyle / audit an existing** `.pptx` | `pptx-cli` directly. Never rebuild a deck that already exists. |
| A **report, memo, board paper, 簽呈, meeting record** | `docx-cli` (§ Pipeline B) |
| A **financial model, KPI workbook, budget** | `xlsx-cli` |
| "Which layout / template / colour family should this be?" | `slideland-powerpoint-design` for vocabulary, then come back here |
| Anything at all that is brand-facing | load `house-style` regardless of route |

Two routing mistakes account for most wasted work:

- **Rebuilding instead of editing.** If a `.pptx` exists and the ask is "fix / update / restyle", it is `pptx-cli`. `deck-build` writes new files; it does not ingest templates or existing decks.
- **Building before designing.** `deck-build` without a spec produces a card grid with a title on top. Its own documentation says so. Run `deck-design` first.

---

## Pick the identity first

Two palettes live in this skill. They are not interchangeable and must never appear in the same file.

| Identity | Field | Accent | Use for |
|---|---|---|---|
| **Corporate Blue** — `references/corp_theme.json` | white `#FFFFFF` | deep blue `#0B318F` | Anything going out under the <Company> mark: board, investor briefing, investor, customer, partner, ESG |
| **Warm Neutral** — `references/warm_theme.json` | warm cream `#F5F1ED` | coral `#CC785C` | Personal work, drafts, internal thinking documents, anything not brand-compliant |

Both are drop-in `theme_overrides` blocks for `deck-build`, and both carry a verified contrast table. When the route is unclear, ask — an corporate deliverable in the warm palette is an off-brand document, not a stylistic variation.

Each palette has one colour that fails as text and must be used as fill only: sky `#00A3E6` for Corporate Blue, coral `#CC785C` for Warm. Both reference files say so at the top; read the one you are using before setting any coloured text.

---

## Pipeline A — new deck

### A1. Design

Run `deck-design`. It fixes the communication contract, picks a narrative mode, density and visual style, then writes `deck_spec.md`.

Two of its choices are pre-decided for corporate work — override its defaults:

**Density.** house decks are read on a laptop or printed, not projected. Use `text` for board, regulator, investor and analyst material; `balanced` for internal review. Reserve `presentation` for an actual stage. This is the same fact `house-style` encodes as its 12.5pt body / 16.5pt card titles.

**Visual style.** Pick the *discipline*, then swap in the corporate identity (§ A2):

| Occasion | Style discipline |
|---|---|
| Standard corporate, product, partner-facing | `soft-rounded` — matches the rounded panels and tinted cards the real decks use |
| Financial results, investor briefing, market or performance review | `data-journalism`, but with `dark: false` via the override — house decks are on white |
| Architecture, reference architecture, systems walkthrough | `blueprint` |
| Vision, keynote, launch moment | `swiss-minimal` |

**Positioning language is out of scope for this plugin.** Product, roadmap and market claims are not encoded here — take them from the approved source your organisation maintains, and never invent them. Getting this wrong in the spec propagates into every slide.

### A2. Build with the corporate theme

Run `deck-build` with the brand override in `references/corp-deck-theme.md`. Copy it verbatim — the values are measured from the live corporate decks, not chosen.

```python
import sys, json
sys.path.insert(0, "<deck-build-skill>/scripts")
from deckbuild import Deck

THEME = json.load(open("<this-skill>/references/corp_theme.json"))
d = Deck(style="soft-rounded", density="text",
         footer="<Company>  ·  <deck title>",
         theme_overrides=THEME)
```

**The canvases already agree.** deck-build's 1280×720 design-pixel grid is exactly 960×540pt — the same canvas `house-style` measures. Convert by **×4/3**: the 37.4pt left margin is 50px, the 10.8pt base unit is 14.4px, the 13.7pt card gutter is 18px. Those numbers are already in the theme's `geometry` block, so the built deck lands on the house grid without hand-nudging.

### A3. Finish pass with officecli

`deck-build` cannot insert the corporate wordmark — it has no image ingestion for brand marks and no template ingestion. Do this after `save()`:

```bash
officecli view deck.pptx issues
officecli view deck.pptx screenshot --grid --out contact.png   # then read the PNG
```

Add the wordmark by copying it from an existing deck (`pptx-cli` § Starting from the corporate deck), or accept a text-set masthead if speed matters more.

### A4. Gate

Both checkers must pass, and they check different things:

```bash
python3 <deck-build-skill>/scripts/check_deck.py deck.pptx    # overflow, collision, contrast
officecli view deck.pptx issues                                # low contrast, stale fields, broken refs
officecli close deck.pptx                                      # flush before delivery
```

---

## Pipeline B — documents and workbooks

`docx-cli` / `xlsx-cli`, with `house-style` loaded. The one thing that catches people out:

**Word on Windows needs a real CJK face.** The house style says Arial for Latin and 中文, which is what the Mac-authored decks do — but Arial carries no CJK glyphs, so Word on Windows falls back to a serif (新細明體) and the document looks wrong to every reviewer on a PC. Set both:

```
--prop font.latin=Arial --prop font.ea=微軟正黑體
```

Same split in a `deck-build` theme: `"heading": "Arial", "heading_alt": "微軟正黑體"`.

---

## The contrast trap — read before using sky

`#00A3E6` is **2.84:1 on white**. It fails deck-build's H4 gate at every size (that gate needs ≥4.5:1 below 24px and ≥3.0:1 at or above). The eyebrows in the live corporate decks would be flagged.

| Use of sky | Verdict |
|---|---|
| Chart series, rules, fills, icon badges | Fine — the gate only measures text |
| Text on deep blue `#0B318F` | 3.99:1 — only at ≥24px |
| Small text on white (eyebrows, labels) | **Fails.** Use `#0B318F` (11.35:1), or `#00719E` (5.45:1) when the sky hue is the point |

`#2FA84F` green is 3.07:1 on white — display sizes only, never body text. `#0B318F`, `#1A2230`, `#5A6676`, `#2E5BF0` and `#7C4DB8` all clear 4.5:1 on both white and the `#F0F6FC` panel tint.

Do not silence a checker finding by editing the spec until the problem disappears. Fix the colour or the geometry, and say so if a page can only pass by changing what it argues.

---

## Before delivering anything

1. Run the format skill's own verification (`view issues`, `check_deck.py`, `validate`).
2. **Render it and look at it.** Layout defects are invisible in the DOM and obvious in a PNG.
3. Confirm no Calibri survived, no off-palette colour crept in, and 中文 has a real CJK font set.
4. Check every product, roadmap and market claim against the approved source — this plugin does not carry one.
5. `officecli close <file>` before `SendUserFile` or `device_commit_files` — otherwise you deliver the pre-edit version.
6. Flag anything you could not verify rather than presenting it as done.

## References

- [`references/warm-palette.md`](references/warm-palette.md) — the Warm Neutral 60-30-10 palette, contrast audit and text-safe variants
- `references/warm_theme.json` — the Warm override, loadable directly
- [`references/corp-deck-theme.md`](references/corp-deck-theme.md) — the corporate `theme_overrides` block, the pt↔px conversion table, and per-style notes
- `references/corp_theme.json` — the same override, loadable directly
- Sibling skills: `house-style`, `pptx-cli`, `docx-cli`, `xlsx-cli`, `officecli-setup`
