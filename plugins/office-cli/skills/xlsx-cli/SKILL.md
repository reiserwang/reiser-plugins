---
name: xlsx-cli
description: Build and edit Excel workbooks through the officecli document DOM with a built-in formula engine — formulas evaluate without Excel installed. Use for corporate financial models, budget and performance workbooks, KPI dashboards, pivot tables and charts, for editing or auditing an existing .xlsx, and for importing CSV data into a formatted sheet. Distinct from the python-based xlsx skill — prefer this one for live formula evaluation, editing existing files, and house style.
---
> Routed here by `house-style`. If you arrived directly and the task might involve a **new deck**, check `house-style` first — it picks the style template and decides between copying the template `.pptx`, running `deck-design` → `deck-build`, or editing in place.


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

1. **Setup.** `bash <officecli-setup>/scripts/setup.sh` — exit 0 and you are ready.
2. **House style** for brand-facing workbooks — header row filled `#0B318F` with white bold Arial 10pt and frozen; `#F0F6FC` banding; totals `#E6F2FC` with a `#0B318F` top border; key metrics `#00A3E6` bold; negatives in parentheses, not red.
3. **Inspect before editing:**
   ```bash
   officecli view book.xlsx stats                      # sheets, used ranges, row counts
   officecli view book.xlsx text --range 'Sheet1!A1:H30'
   officecli get  book.xlsx '/sheet[1]/B7' --json      # value, formula, format
   officecli view book.xlsx issues                     # stale/broken formulas
   ```
4. **Edit**, or `import` a CSV for bulk data. Past two or three edits, write a JSON batch
   and replay it — `bash <officecli-setup>/scripts/ocbuild.sh book.xlsx build.json` — one
   atomic pass, no shell quoting, and a rebuild is an edit to the JSON. **Exception:**
   cross-sheet formulas go in individual `set` commands or a single non-resident batch;
   they misresolve when batched through a live resident.
5. **Verify:** `view issues` catches `formula_not_evaluated`, `formula_cache_stale`, `formula_ref_missing_sheet`, and broken defined names. Never deliver a workbook with these outstanding. Then the house-style gate below.
6. **Flush:** `officecli close book.xlsx` before `SendUserFile` or `device_commit_files`.

## Reference files

| Where | When |
|---|---|
| `officecli help xlsx <element>` | The xlsx schema — cells, ranges, formulas, charts, pivots, conditional formatting, validation. Authoritative and version-matched |
| `officecli load_skill excel` | Upstream's own xlsx skill; `financial-model` for 3-statement / DCF / LBO structure, `data-dashboard` for KPI layout and chart choice |
| `<officecli-setup>` | Batch shape, resident mode, flushing, the raw-XML escape hatch |
| `house-style` | Palette, type scale, table furniture for anything brand-facing |

The binary serves its schema and upstream's skill docs directly, so nothing here is a
snapshot that can drift from the installed version.

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

## Delivering

```bash
officecli view book.xlsx issues          # formulas that never evaluated, dead references
officecli close book.xlsx                # flush before anything else reads it
python3 <house-style>/scripts/check_book.py book.xlsx --palette 'ANA Blue'
```

`check_book.py` catches what `view issues` cannot: a formula that *did* evaluate, to
`#DIV/0!` or `#REF!`; a table of any size with no frozen header; an unreplaced
`{{placeholder}}`; a fill or type colour outside the named palette; and a `[Red]` negative
where house style is parentheses. It warns on a header row that is not bold and on a
column too narrow for its longest value — the `######` that only shows up once the file is
open on someone else's machine. **FAIL must be 0.** Add `--template` for a template file.
