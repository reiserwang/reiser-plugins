# office-cli

Office document creation and editing through the [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) document DOM, with a house-style layer of interchangeable design templates.

## Why this exists

The binary is one npm line away and ships nothing this plugin needs to carry — no vendored executable, no SDK dependency. What OfficeCLI gives you is a path-addressable DOM over `.pptx` / `.docx` / `.xlsx` (`/slide[1]/shape[@id=100000]`) and a PNG renderer: **edit an existing file in place**, and **look at the result** before delivering it. It has no opinion about what a deck should look like.

That opinion is the plugin. Three things, in order of what they're worth:

1. **Five design templates.** Six `.pptx` masters — SKS Blue ships a light and a dark field on one accent — 19 named layouts each on one shared 1440 × 810 pt grid, a `theme.json` per template for `deck-build`, and palettes whose every contrast ratio is *generated* by `scripts/contrast.py` rather than typed. Interchangeable at the folder level, so ANA Blue → SKS Dark is a master swap, not a rebuild. None of this exists upstream.
2. **Routing.** `house-style` picks the template, then the pipeline. It exists to prevent the two mistakes that cost the most: rebuilding a deck that should have been edited, and running `deck-build` with no spec — which produces a card grid with a title on top, as its own documentation admits.
3. **Failure modes someone already paid for.** The wrong npm package, the 403 installer, zsh globbing an unquoted `[1]`, the shell eating `$15M`, and officecli's resident documents handing a stale file to whatever reads next. Each is a burned turn or a silently wrong deliverable for a session that hasn't met them before.

What this plugin deliberately does **not** carry is documentation of the binary. `officecli help <format> <element>` and `officecli load_skill <name>` serve the schema and upstream's own skill docs from the installed binary, always version-matched; a vendored snapshot of them could only drift. Strip the templates, the routing and the gates and what remains is a thin wrapper around that help output, not worth installing.

## Skills

| Skill | Purpose |
|---|---|
| `house-style` | **Start here.** Picks the style template, then routes the request: copy the template `.pptx`, run `deck-design` → `deck-build`, or edit in place. Hosts one folder per template under `skills/house-style/templates/`. |
| `officecli-setup` | Verify the binary and drive the mechanics the other skills share — schema lookup, JSON batch builds, resident mode, flushing. Handles the two environment-specific traps below. Run first in any fresh session. |
| `pptx-cli` | Decks — build, edit, audit, render. |
| `docx-cli` | Reports, memos, board papers, approval routing forms, template merges, tracked changes. |
| `xlsx-cli` | Financial models, KPI workbooks, pivots, charts, with live formula evaluation. |

The format skills carry no vendored schema. They point at `officecli help <format> <element>` for the element schema and `officecli load_skill <name>` for upstream's own skills (`pptx`, `word`, `excel`, `word-form`, `morph-ppt`, `pitch-deck`, `academic-paper`, `data-dashboard`, `financial-model`), both served by the installed binary.

## Scripts, not just prose

Everything a session would otherwise retype as shell is a script:

| Script | Does |
|---|---|
| `skills/officecli-setup/scripts/setup.sh` | Version check, wrong-package detection, and a real `create` → `add` → `view` round-trip. Distinct exit codes for missing / wrong package / broken binary |
| `skills/officecli-setup/scripts/ocbuild.sh` | Clean-slate JSON batch replay — `close` → `rm` → `create` → `batch` → `close`, every exit code checked. `--from <template>` inherits a template's master, theme and layouts without opening the template for writing |
| `skills/house-style/scripts/check_deck.py` | The deck gate — title column, palette, typeface, assembly tells, and the three defects a template-built deck inherits rather than contains: `{{placeholders}}` living on the layout, a title box off the house grid, the starter blank slide left in |
| `skills/house-style/scripts/check_doc.py` | The Word gate — heading outline, placeholders, palette, non-house faces, 中文 with no East Asian font set |
| `skills/house-style/scripts/check_book.py` | The Excel gate — placeholders, evaluated formula errors, unfrozen headers, palette, red negatives, columns that will render `######` |
| `skills/house-style/scripts/contrast.py` | Regenerates the contrast matrix; `--check` verifies tokens against the `.pptx` files |
| `skills/house-style/scripts/build_layout_catalogue.py` | Rebuilds every layout catalogue from the templates |
| `skills/house-style/scripts/test_checks.py` | Self-check: builds a broken `.docx`, `.xlsx` and `.pptx` and asserts each gate still catches its own fixture |

A batch is atomic by default, so a build is one reviewable JSON file that either applies or does not — and a rebuild is an edit to that file rather than a hundred re-typed commands.

## Style templates

Five ship today. Each is a folder with the same four files, so adding a sixth changes nothing outside its own directory.

| Template | Field | Accent | Use for |
|---|---|---|---|
| `ana-blue` | white `#FFFFFF` | deep blue `#0B318F` | brand-facing: board, regulator, investor, customer, partner |
| `yukima` 雪間 | cool blue-grey `#F1F6FA` | slate `#4B6F87` | research, ESG and sustainability, long-form analysis |
| `reiser-warm` | warm cream `#F5F1ED` | coral `#CC785C` | personal work, drafts, internal thinking documents |
| `sks-dark` | midnight `#1A293A` | amber `#B57319` | screen-first: on-stage and on-screen decks, product walkthroughs, launch sets, operations views |
| `sks-blue` | white `#FFFFFF` **and** near-black `#080D1A` | blue `#2F55F0` | product and platform material that has to sit next to the live site — two fields, one accent, one grid |

```
skills/house-style/
├── SKILL.md
├── references/          grid.md · layouts.md · pipelines.md · contrast.md
│                        contrast-matrix.md   (generated — every ratio, all palettes)
├── scripts/             contrast.py · build_layout_catalogue.py · house_prose.py
│                        check_deck.py · check_doc.py · check_book.py · test_checks.py
└── templates/
    ├── ana-blue/        TEMPLATE.md · palette.md · theme.json · ana-blue.pptx
    ├── yukima/          TEMPLATE.md · palette.md · theme.json · yukima.pptx
    ├── reiser-warm/     TEMPLATE.md · palette.md · theme.json · reiser-warm.pptx
    ├── sks-dark/        TEMPLATE.md · palette.md · theme.json · sks-dark.pptx
    └── sks-blue/        TEMPLATE.md · palette.md · theme.json · theme.dark.json
                         sks-blue.pptx · sks-blue-dark.pptx
```

Geometry is shared and identical across templates: **1440 × 810 pt** canvas, 56pt margins, 1328pt content band, 16.2pt gutter, 19 layouts with the same names and order in every one. Restyling a deck from one template to another is a master swap, not a rebuild.

All five palettes are built on **60-30-10 by area** — 60% field and tints, 30% ink, 10% accent — declared in each `palette.md` and machine-readable in each `theme.json`. Where they differ: coral cannot be text, so Reiser Warm's accent band is fills only; ANA Blue's deep blue and Yukima's slate are both text-safe, so each counts as supporting when it is type and accent when it is area. Yukima's source palette had no ink at all, so both of its inks are derived from the accent hue and marked as such. SKS Dark inverts the whole arrangement onto a dark field and needs three value steps of one warm — amber for area, gold for type, deep amber for the full-bleed dividers — because on a dark ground no single warm carries all three jobs and stays legible. SKS Blue runs one accent across both a white and a near-black field, so its dark master inverts the `clrMap` rather than redefining the palette.

Every ratio for every palette lives in `references/contrast-matrix.md`, generated by `scripts/contrast.py`. `--check` verifies that no palette document claims a colour its `.pptx` does not contain.

Note that these decks are **read, not projected** — 30pt titles and 18pt body on a 1440pt canvas, equivalent to 20pt / 12pt on a conventional 960pt deck. This deliberately overrides the upstream OfficeCLI pptx skill's "titles ≥ 36pt" rule.

## Two install traps this plugin exists to prevent

1. **The documented installer is blocked in the Cowork cloud sandbox.** `curl -fsSL https://d.officecli.ai/install.sh | bash` returns 403; so do GitHub Releases and `api.github.com`. The npm registry works.
2. **`npm install -g officecli` installs the wrong product.** The unscoped `officecli` name on npm belongs to an unrelated hosted-credit AI generation TUI with none of the DOM commands. The correct package is **`@officecli/officecli`**.

On a local Mac, `device_bash` has no network access and cannot install anything — either install by hand, or stage files into the cloud sandbox and commit the results back.

## Coexistence with the built-in Office skills

Named distinctly so both sets stay enabled and neither hijacks the other. Rough division:

- **Editing an existing file, tracked changes, live formulas, exact geometry, anything on a style template** → these skills.
- **Generating from scratch with no style constraint, heavy programmatic generation from a dataset** → the built-in `pptx` / `docx` / `xlsx` skills.

Do not run both against the same file in one pass; `officecli close` before handing off.

## No content is encoded here

The templates carry geometry and colour only. Organisation names, unit names, product names, taglines, roadmap claims and classification markings are **not** in this plugin by design — the template files ship `{{ORG}}`, `{{UNIT}}`, `{{DECK_TITLE}}`, `{{DECK_TITLE_EN}}` and `{{CLASSIFICATION}}` placeholders, filled from whatever approved source the user maintains. A delivered file containing `{{` is a defect.

## Attribution

This plugin wraps [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI), Apache-2.0 — see `LICENSE-officecli.txt` and `NOTICE-officecli.txt`. Earlier versions vendored a snapshot of its reference docs; they were removed in 0.12.0 in favour of `officecli help` and `officecli load_skill`, which the installed binary serves version-matched.

Verified against officecli **1.0.147**.
