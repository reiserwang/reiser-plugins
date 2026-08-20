# office-cli

Office document creation and editing through the [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) document DOM, with Corporate house style applied by default.

## Why this exists

OfficeCLI addresses `.pptx` / `.docx` / `.xlsx` as a path-addressable DOM (`/slide[1]/shape[@id=100000]`) and can render any document to PNG. That makes two things possible that the python-based Office skills do not do well: **editing an existing file in place**, and **seeing whether the result actually looks right** before delivering it.

This plugin wraps that capability and adds the house-style layer — the Corporate Blue palette, the Arial type scale and the exact slide grid, all measured from the live corporate decks rather than invented.

## Skills

| Skill | Purpose |
|---|---|
| `corp-deliverable` | **Start here.** Universal router for any corporate deliverable — sends new decks to `deck-design` → `deck-build`, existing files to the officecli skills, and applies house style to all of them. Carries the corporate `theme_overrides` block for deck-build. |
| `officecli-setup` | Install and verify the binary. Handles the two environment-specific traps below. Run first in any fresh session. |
| `house-style` | Palette, typography, layout grid, bilingual conventions. Loaded by the three format skills; also stands alone for non-officecli work. |
| `pptx-cli` | Decks — build, edit, audit, render. |
| `docx-cli` | Reports, memos, board papers, 簽呈, template merges, tracked changes. |
| `xlsx-cli` | Financial models, KPI workbooks, pivots, charts, with live formula evaluation. |

Each format skill carries the relevant upstream OfficeCLI skills under `references/` for the full element schema, loaded on demand.

## Two install traps this plugin exists to prevent

1. **The documented installer is blocked in the Cowork cloud sandbox.** `curl -fsSL https://d.officecli.ai/install.sh | bash` returns 403; so do GitHub Releases and `api.github.com`. The npm registry works.
2. **`npm install -g officecli` installs the wrong product.** The unscoped `officecli` name on npm belongs to an unrelated hosted-credit AI generation TUI with none of the DOM commands. The correct package is **`@officecli/officecli`**.

On the user's Mac, `device_bash` has no network access and cannot install anything — either install locally by hand, or stage files into the cloud sandbox and commit the results back.

## Coexistence with the built-in Office skills

Named distinctly so both sets stay enabled and neither hijacks the other. Rough division:

- **Editing an existing file, tracked changes, live formulas, exact geometry, anything on corporate brand** → these skills.
- **Generating from scratch with no brand constraint, heavy programmatic generation from a dataset** → the built-in `pptx` / `docx` / `xlsx` skills.

Do not run both against the same file in one pass; `officecli close` before handing off.

## House style at a glance

Deep blue `#0B318F` · sky `#00A3E6` · panel `#F0F6FC` · callout `#E6F2FC` · headline ink `#1A2230` · body ink `#5A6676`. Arial throughout, 960×540pt canvas, 10.8pt base grid.

Note that house decks are **read, not projected** — the type scale runs 12.5pt body / 16.5pt card titles / 24pt taglines. This deliberately overrides the upstream OfficeCLI pptx skill's "titles ≥ 36pt" rule.

## Attribution

Bundled reference files under `skills/*/references/officecli-*.md` are from [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI), Apache-2.0. See `LICENSE-officecli.txt` and `NOTICE-officecli.txt`. They are a snapshot and drift from whatever binary is installed — `officecli help <format> <element>` is always authoritative.

Verified against officecli **1.0.144**.
