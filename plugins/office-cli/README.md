# office-cli

Office document creation and editing through the [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) document DOM, with a house-style layer of interchangeable design templates.

## Why this exists

OfficeCLI addresses `.pptx` / `.docx` / `.xlsx` as a path-addressable DOM (`/slide[1]/shape[@id=100000]`) and can render any document to PNG. That makes two things possible that the python-based Office skills do not do well: **editing an existing file in place**, and **seeing whether the result actually looks right** before delivering it.

This plugin wraps that capability and adds the style layer — palette, type scale, slide grid and 19 named layouts, all measured from real template files rather than invented.

## Skills

| Skill | Purpose |
|---|---|
| `house-style` | **Start here.** Picks the style template, then routes the request: copy the template `.pptx`, run `deck-design` → `deck-build`, or edit in place. Hosts one folder per template under `skills/house-style/templates/`. |
| `officecli-setup` | Install and verify the binary. Handles the two environment-specific traps below. Run first in any fresh session. |
| `pptx-cli` | Decks — build, edit, audit, render. |
| `docx-cli` | Reports, memos, board papers, approval routing forms, template merges, tracked changes. |
| `xlsx-cli` | Financial models, KPI workbooks, pivots, charts, with live formula evaluation. |

Each format skill carries the relevant upstream OfficeCLI skills under `references/` for the full element schema, loaded on demand.

## Style templates

Two ship today. Each is a folder with the same four files, so adding a third changes nothing outside its own directory.

| Template | Field | Accent | Use for |
|---|---|---|---|
| `ana-blue` | white `#FFFFFF` | deep blue `#0B318F` | brand-facing: board, regulator, investor, customer, partner, ESG |
| `reiser-warm` | warm cream `#F5F1ED` | coral `#CC785C` | personal work, drafts, internal thinking documents |

```
skills/house-style/
├── SKILL.md
├── references/          grid.md · layouts.md · pipelines.md · contrast.md   (shared)
└── templates/
    ├── ana-blue/        TEMPLATE.md · palette.md · theme.json · ana-blue.pptx
    └── reiser-warm/     TEMPLATE.md · palette.md · theme.json · reiser-warm.pptx
```

Geometry is shared and identical across templates: **1440 × 810 pt** canvas, 56pt margins, 1328pt content band, 16.2pt gutter, 19 layouts with the same names and order in both. Restyling a deck from one template to the other is a master swap, not a rebuild.

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

Bundled reference files under `skills/*/references/officecli-*.md` are from [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI), Apache-2.0. See `LICENSE-officecli.txt` and `NOTICE-officecli.txt`. They are a snapshot and drift from whatever binary is installed — `officecli help <format> <element>` is always authoritative.

Verified against officecli **1.0.144**.
