---
name: docx-cli
description: Create and edit Word documents through the officecli document DOM — paragraph and run-level control, tables, headers/footers, styles, comments, and tracked changes. Use for reports, memos, board papers, approval routing forms and policy documents, for editing or proofreading an existing .docx in place, for filling form templates, and for merging data into {{placeholder}} templates. Distinct from the python-based docx skill — prefer this one for editing existing files, tracked changes, and house style.
---
> Routed here by `house-style`. If you arrived directly and the task might involve a **new deck**, check `house-style` first — it picks the style template and decides between copying the template `.pptx`, running `deck-design` → `deck-build`, or editing in place.


# docx (officecli)

## Choosing this skill vs. the python `docx` skill

| Situation | Use |
|---|---|
| Editing or proofreading an **existing** .docx in place | **this skill** |
| Tracked changes, comments, review workflow | **this skill** |
| Filling a recurring form template | **this skill** — `merge` with `{{key}}` placeholders |
| brand-compliant report or board paper | **this skill** + `house-style` |
| Generating a long document from scratch, no template | either |

## Order of operations

1. **Setup.** `bash <officecli-setup>/scripts/setup.sh` — exit 0 and you are ready.
2. **House style** for anything brand-facing — load `house-style`. Body Arial 10.5pt `#1A2230`; H1 16pt bold `#0B318F`; table headers filled `#0B318F` with white text; banding `#F0F6FC`; footer `{{ORG}}  |  {{DECK_TITLE}}` at 9pt `#5A6676`.
3. **Inspect before editing:**
   ```bash
   officecli view report.docx outline           # heading structure
   officecli view report.docx text --max-lines 80
   officecli get  report.docx '/body/paragraph[12]' --json
   officecli query report.docx 'table' --json
   ```
4. **Edit.** Past two or three edits, write a JSON batch and replay it:
   ```bash
   bash <officecli-setup>/scripts/ocbuild.sh report.docx build.json
   ```
   One atomic pass, no shell quoting, and a rebuild is an edit to the JSON. Single
   `add` / `set` / `remove` commands are for probing and one-off fixes.
5. **Verify:** `officecli view report.docx issues`, then `validate`, then the house-style
   gate below.
6. **Flush:** `officecli close report.docx` before `SendUserFile` or `device_commit_files`.

## Reference files

| Where | When |
|---|---|
| `officecli help docx <element>` | The docx schema — paragraphs, runs, tables, sections, headers/footers, styles, fields, comments, tracked changes. Authoritative and version-matched |
| `officecli load_skill word` | Upstream's own docx skill; `word-form` for fillable forms and content controls, `academic-paper` for citations and cross-references |
| `<officecli-setup>` | Batch shape, resident mode, flushing, the raw-XML escape hatch |
| `house-style` | Palette, type scale, furniture for anything brand-facing |

The binary serves its schema and upstream's skill docs directly, so nothing here is a
snapshot that can drift from the installed version.

## Traps

- **Quote every path:** `"/body/paragraph[3]/run[1]"`.
- **Styles must exist before use.** `add style` first, or `set` the run properties directly. A `--prop style=Heading1` referencing a style the document lacks fails or silently no-ops.
- **`\n` in `text=` starts a new paragraph, `\v` is a line break within one.** Getting this backwards produces a wall of run-on paragraphs.
- **Field values are cached.** TOC page numbers, `PAGE`/`NUMPAGES`, and cross-references show stale values after edits. `officecli view <file> issues` flags them; `refresh` requires Word on Windows, so state the limitation rather than delivering wrong page numbers.
- **CJK fonts are set separately.** Arial for Latin does not set the East Asian font — set `font.ea` too, or 中文 falls back to the theme default.
- **Track changes** is a document-level setting; enable it before editing if the user wants a reviewable redline, not after.

## Template merge

For offer letters, approval routing forms, and any recurring form:

```bash
officecli merge template.docx output.docx --data '{"applicant":"<applicant name>","date":"2026-08-17","subject":"..."}'
```

Placeholders in the template are `{{key}}`. Inspect an unfamiliar template's placeholder set first with `officecli view template.docx text | grep -o '{{[^}]*}}'`.

Corporate form templates are often still legacy `.doc` — convert to `.docx` before officecli can address them.

## Bilingual documents

English leads, 中文 follows. Set `font.ea` to Arial alongside `font.latin`. For mixed-script tables, give CJK columns ~1.3× the width of their English equivalents — 中文 at the same point size occupies more horizontal space per character but fewer characters per phrase, and the net effect on column fit is not intuitive. Render or check `view issues` for overflow.

## Delivering

```bash
officecli view report.docx issues        # overflow, stale TOC and page fields
officecli validate report.docx           # OpenXML schema
officecli close report.docx              # flush before anything else reads it
python3 <house-style>/scripts/check_doc.py report.docx --palette 'ANA Blue'
```

`check_doc.py` is the gate the other two cannot cover. It prints the heading outline for
a read-through, and fails the document on an unreplaced `{{placeholder}}`, on a run set
in a face that is not house, on any colour outside the named palette, and on 中文 in a
document where no East Asian font was ever set — the trap above, invisible until it
renders on a machine without the fallback. It warns on a missing footer, a heading level
that jumps, an unfilled table header, two spellings of one term, and AI register.
**FAIL must be 0.** Add `--template` when checking a template, where `{{placeholders}}`
are the point, and `--font 'Noto Sans TC'` to admit a second house face.
