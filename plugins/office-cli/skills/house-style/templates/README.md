# Templates

Each style template lives in its own folder and ships the same four files. `sks-blue` is the one exception: it ships **two fields in one identity**, so its folder carries a second `.pptx` and a second `theme.dark.json` alongside the usual four. `contrast.py` addresses those with the optional `pptx_file` and `theme_file` keys. Nothing outside the folder needs to change when a template's colours change.

```
templates/<name>/
├── TEMPLATE.md      what this template is for, its type scale, its standing furniture
├── palette.md       every token, with verified WCAG ratios, and the Word / Excel mapping
├── theme.json       drop-in theme_overrides for deck-build
└── <name>.pptx      19 layouts, one master, one blank starter slide
```

| Template | Field | Accent | Use for |
|---|---|---|---|
| [`ana-blue`](ana-blue/TEMPLATE.md) | white `#FFFFFF` | deep blue `#0B318F` | brand-facing: board, regulator, investor, customer, partner, ESG |
| [`yukima`](yukima/TEMPLATE.md) | cool blue-grey `#F1F6FA` | slate `#4B6F87` | research, ESG and sustainability, long-form analysis |
| [`reiser-warm`](reiser-warm/TEMPLATE.md) | warm cream `#F5F1ED` | coral `#CC785C` | personal work, drafts, internal thinking documents |
| [`sks-dark`](sks-dark/TEMPLATE.md) | midnight `#1A293A` | amber `#B57319` | screen-first: on-stage and on-screen decks, product walkthroughs, launch and demo sets, operations views |
| [`sks-blue`](sks-blue/TEMPLATE.md) | **two fields** — white `#FFFFFF` and midnight `#080D1A` | blue `#2F55F0` | product and platform material that sits next to the live product site |

Geometry is shared across all five — see [`../references/grid.md`](../references/grid.md) and [`../references/layouts.md`](../references/layouts.md). The templates differ **only in colour**, which is what makes restyling a deck from one to the other a master swap rather than a rebuild.

All five are built on **60-30-10 by area**: 60% field and tints, 30% ink, 10% accent, with the three divider layouts exempt. Each `palette.md` declares its own bands, and each `theme.json` carries the same split as a machine-readable `proportions` block.

## Adding a template

1. `mkdir templates/<name>` and write the four files. Keep the geometry identical unless you have a reason not to — divergent geometry makes the layout reference wrong for your template, and you then owe a per-template geometry file.
2. Build `<name>.pptx` by copying an existing template and replacing the theme's `clrScheme` plus the hard-coded `srgbClr` values in the master and the 19 layouts. Keep the layout **names** and **order** identical so `--layout 'Title and Content'` resolves in every template.
3. Declare the 60-30-10 bands. `palette.md` needs a `60% — the field`, `30% — the supporting layer` and `10% — the accent` section, and `theme.json` needs the matching `proportions` block. State which band each colour belongs to; a colour that is text in one band and area in another (as ANA Blue's deep blue is) must say so explicitly.
4. Add the palette to `PALETTES` in [`../scripts/contrast.py`](../scripts/contrast.py), then run `python3 scripts/contrast.py --check` and `--write`. The check confirms every field, supporting and accent token is actually in your `.pptx`; the write regenerates the shared matrix. Never hand-type a ratio — name the fill-only colours explicitly at the top of `palette.md`, because that omission is the most common source of failed decks.
5. If the source palette has no colour reaching ~7:1 on its field, it has no ink and you must derive one. Darken the accent hue without shifting it — or, on a dark field, lighten it — and mark the result **derived** in `palette.md` and in `theme.json`'s `derived` block. Yukima needed two; Reiser Warm needed one; SKS Dark needed three.
6. Add a row to the table above and to the table in `../SKILL.md` § 1.
7. Verify: open the file, confirm 19 layouts and the right theme name, render a slide per layout to PNG and look at it.
8. Strip PowerPoint's section list if the file inherited one — `p14:sectionLst` in `ppt/presentation.xml` carries section *names* from whatever deck you copied and references slide IDs you deleted.

## What must not go in a template

No organisation names, unit names, product names, taglines, classification markings, personal names or file paths — in the markdown or inside the `.pptx`. Footers and covers carry `{{ORG}}`, `{{UNIT}}`, `{{DECK_TITLE}}`, `{{DECK_TITLE_EN}}` and `{{CLASSIFICATION}}` placeholders instead. Check `docProps/core.xml` too: authoring tools write the last editor's name there.

```bash
# quick leak check on a template file
mkdir -p /tmp/t && cd /tmp/t && unzip -qo <name>.pptx
grep -rl --include='*.xml' -E '<your org names and product names here>' . || echo clean
```
