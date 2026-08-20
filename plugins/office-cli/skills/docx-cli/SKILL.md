---
name: docx-cli
description: Create and edit Word documents through the officecli document DOM — paragraph and run-level control, tables, headers/footers, styles, comments, and tracked changes. Use for corporate reports, memos, board papers, 簽呈 and policy documents, for editing or proofreading an existing .docx in place, for filling form templates, and for merging data into {{placeholder}} templates. Distinct from the python-based docx skill — prefer this one for editing existing files, tracked changes, and house style.
---
> Routed here by `corp-deliverable`. If you arrived directly and the task might involve a **new deck**, check `corp-deliverable` first — new decks go through `deck-design` → `deck-build`, not through this skill.


# docx (officecli)

## Choosing this skill vs. the python `docx` skill

| Situation | Use |
|---|---|
| Editing or proofreading an **existing** .docx in place | **this skill** |
| Tracked changes, comments, review workflow | **this skill** |
| Filling a corporate form or 簽呈 template | **this skill** — `merge` with `{{key}}` placeholders |
| brand-compliant report or board paper | **this skill** + `house-style` |
| Generating a long document from scratch, no template | either |

## Order of operations

1. **Setup.** Run `officecli-setup` if `officecli --version` is not a bare semver.
2. **House style** for anything brand-facing — load `house-style`. Body Arial 10.5pt `#1A2230`; H1 16pt bold `#0B318F`; table headers filled `#0B318F` with white text; banding `#F0F6FC`; footer `<Company>  |  <title>` at 9pt `#5A6676`.
3. **Inspect before editing:**
   ```bash
   officecli view report.docx outline           # heading structure
   officecli view report.docx text --max-lines 80
   officecli get  report.docx '/body/paragraph[12]' --json
   officecli query report.docx 'table' --json
   ```
4. **Edit** with `add` / `set` / `remove`, or `batch` for multi-step work.
5. **Verify:** `officecli view report.docx issues`, then `validate`.
6. **Flush:** `officecli close report.docx` before `SendUserFile` or `device_commit_files`.

## Reference files

| File | When |
|---|---|
| `references/officecli-core.md` | Command surface, layer model, batch semantics |
| `references/officecli-docx.md` | Full docx schema — paragraphs, runs, tables, sections, headers/footers, styles, fields, comments, tracked changes |
| `references/officecli-word-form.md` | Form fields, content controls, template filling |

Upstream snapshot — drifts from the installed binary. `officecli help docx <element>` is authoritative.

## Traps

- **Quote every path:** `"/body/paragraph[3]/run[1]"`.
- **Styles must exist before use.** `add style` first, or `set` the run properties directly. A `--prop style=Heading1` referencing a style the document lacks fails or silently no-ops.
- **`\n` in `text=` starts a new paragraph, `\v` is a line break within one.** Getting this backwards produces a wall of run-on paragraphs.
- **Field values are cached.** TOC page numbers, `PAGE`/`NUMPAGES`, and cross-references show stale values after edits. `officecli view <file> issues` flags them; `refresh` requires Word on Windows, so state the limitation rather than delivering wrong page numbers.
- **CJK fonts are set separately.** Arial for Latin does not set the East Asian font — set `font.ea` too, or 中文 falls back to the theme default.
- **Track changes** is a document-level setting; enable it before editing if the user wants a reviewable redline, not after.

## Template merge

For 簽呈, offer letters, and any recurring corporate form:

```bash
officecli merge template.docx output.docx --data '{"applicant":"<applicant name>","date":"2026-08-17","subject":"..."}'
```

Placeholders in the template are `{{key}}`. Inspect an unfamiliar template's placeholder set first with `officecli view template.docx text | grep -o '{{[^}]*}}'`.

Corporate form templates are often still legacy `.doc` — convert to `.docx` before officecli can address them.

## Bilingual documents

English leads, 中文 follows. Set `font.ea` to Arial alongside `font.latin`. For mixed-script tables, give CJK columns ~1.3× the width of their English equivalents — 中文 at the same point size occupies more horizontal space per character but fewer characters per phrase, and the net effect on column fit is not intuitive. Render or check `view issues` for overflow.
