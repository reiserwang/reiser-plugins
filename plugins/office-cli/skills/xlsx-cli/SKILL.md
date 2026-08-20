---
name: xlsx-cli
description: Build and edit Excel workbooks through the officecli document DOM with a built-in formula engine — formulas evaluate without Excel installed. Use for corporate financial models, budget and performance workbooks, KPI dashboards, pivot tables and charts, for editing or auditing an existing .xlsx, and for importing CSV data into a formatted sheet. Distinct from the python-based xlsx skill — prefer this one for live formula evaluation, editing existing files, and house style.
---
> Routed here by `corp-deliverable`. If you arrived directly and the task might involve a **new deck**, check `corp-deliverable` first — new decks go through `deck-design` → `deck-build`, not through this skill.


# xlsx (officecli)

## Choosing this skill vs. the python `xlsx` skill

| Situation | Use |
|---|---|
| Workbook whose **formulas must evaluate** without Excel | **this skill** — 350+ functions, auto-evaluated |
| Editing or auditing an **existing** .xlsx | **this skill** |
| Pivot tables, conditional formatting, sparklines, data validation | **this skill** |
| brand-compliant financial or KPI workbook | **this skill** + `house-style` |
| Pure data transformation, no formatting | pandas + python `xlsx` is often simpler |

## Order of operations

1. **Setup.** Run `officecli-setup` if `officecli --version` is not a bare semver.
2. **House style** for brand-facing workbooks — header row filled `#0B318F` with white bold Arial 10pt and frozen; `#F0F6FC` banding; totals `#E6F2FC` with a `#0B318F` top border; key metrics `#00A3E6` bold; negatives in parentheses, not red.
3. **Inspect before editing:**
   ```bash
   officecli view book.xlsx stats                      # sheets, used ranges, row counts
   officecli view book.xlsx text --range 'Sheet1!A1:H30'
   officecli get  book.xlsx '/sheet[1]/B7' --json      # value, formula, format
   officecli view book.xlsx issues                     # stale/broken formulas
   ```
4. **Edit**, or `import` a CSV for bulk data.
5. **Verify:** `view issues` catches `formula_not_evaluated`, `formula_cache_stale`, `formula_ref_missing_sheet`, and broken defined names. Never deliver a workbook with these outstanding.
6. **Flush:** `officecli close book.xlsx` before `SendUserFile` or `device_commit_files`.

## Reference files

| File | When |
|---|---|
| `references/officecli-core.md` | Command surface, layer model, batch semantics |
| `references/officecli-xlsx.md` | Full xlsx schema — cells, ranges, formulas, charts, pivots, conditional formatting, validation |
| `references/officecli-financial-model.md` | Financial model structure, driver sheets, scenario toggles |
| `references/officecli-data-dashboard.md` | KPI dashboard layout and chart selection |

Upstream snapshot — drifts from the installed binary. `officecli help xlsx <element>` is authoritative.

## Traps

- **Sheet-scope every selector.** `officecli set book.xlsx A1` is **rejected** — a bare selector would match across the whole workbook. Use `"/sheet[1]/A1"` or `"/Sheet1/A1"`.
- **Quote ranges and paths** — `"/sheet[1]/A1:D20"`.
- **`formula=` vs `value=`.** `--prop formula="=SUM(A1:A2)"` writes and evaluates a formula; `--prop value=42` writes a literal. Setting `value` on a formula cell destroys the formula.
- **Import before format.** `officecli import book.xlsx '/sheet[1]/A1' data.csv`, then apply styling — formatting first gets overwritten by the import.
- **Number formats are strings:** `#,##0`, `NT$#,##0`, `0.0%`, `#,##0;(#,##0)` for parenthesised negatives.
- **Charts reference ranges, not values.** Moving or inserting rows after building a chart silently breaks its series — `view issues` reports `chart_series_ref_missing_sheet`. Build charts last.

## Financial and performance work

When a corporate reference workbook already exists for the same subject, read its structure before designing a new one so column conventions and account naming match what the finance team already uses.

State units in the header (`NT\$ thousands`), never per cell. For year references, the corporate files use ROC calendar years (民國, e.g. 112年 = 2023) — carry that convention forward rather than silently converting to Gregorian, and label which one is in use.
