---
name: pptx-cli
description: Build and edit PowerPoint decks through the officecli document DOM — precise shape-level control, layout inspection, and PNG rendering to verify the result. Use for brand-compliant decks, for editing or auditing an existing .pptx (extracting content, fixing layout, restyling, checking overflow), for merging or splitting decks, and whenever slide geometry must land exactly. Distinct from the python-based pptx skill — prefer this one for editing existing files and for anything on house style.
---
> Routed here by `house-style`. If you arrived directly and the task might involve a **new deck**, check `house-style` first — it picks the style template and decides between copying the template `.pptx`, running `deck-design` → `deck-build`, or editing in place.


# pptx (officecli)

## Choosing this skill vs. the python `pptx` skill

| Situation | Use |
|---|---|
| Editing, restyling, or auditing an **existing** .pptx | **this skill** — path-addressable DOM, no rebuild |
| brand-compliant deck, exact grid geometry required | **this skill** |
| Need to see what a slide actually looks like | **this skill** — `view screenshot` |
| Generating a deck from scratch with no brand constraints | either; python `pptx` is fine |
| Heavy programmatic generation from a dataset | python `pptx` |

Do not mix the two on one file in one pass. If both are needed, `officecli close` before handing off.

## Order of operations

1. **Setup.** Run the `officecli-setup` skill if `officecli --version` is not a bare semver. Non-negotiable in a fresh Cowork session — the binary is not preinstalled and the documented curl installer is blocked here.
2. **House style.** For any brand-facing deck, load `house-style` and follow it. Its typography scale **overrides** the ≥36pt title rule in the upstream reference — house decks are dense read-not-projected documents.
3. **Slide craft.** Before writing the first slide, read `house-style/references/slide-craft.md` and write the storyline — one title per slide, in order, with how each will be shown. Everything in this file governs how a deck looks; that one governs whether it says anything. A deck built layout-first reads as a template that was filled in, and no amount of geometry fixes it afterwards.
4. **Inspect before editing.** Never edit an existing deck blind:
   ```bash
   officecli view deck.pptx outline               # slide-by-slide structure
   officecli get  deck.pptx '/slide[3]' --json    # exact geometry & formatting
   officecli view deck.pptx screenshot --grid --out contact.png   # then read the PNG
   ```
5. **Edit** with `add` / `set` / `remove` / `move`, or a `batch` array for anything multi-step.
6. **Verify.** `view issues`, then re-render and read the PNG.
7. **Flush.** `officecli close deck.pptx` before `SendUserFile` or `device_commit_files`.

## Reference files

Load on demand — do not read all of them:

| File | When |
|---|---|
| `house-style/references/layout-catalogue/<name>-layouts.pptx` | Picking a layout. 19 slides, one per named layout, each placeholder labelled with its index and geometry; plus the palette and type reference pages |
| `house-style/references/slide-craft.md` | **Read before writing slides.** Titles, layout, tables, charts, prose — what makes a slide worth showing |
| `references/officecli-core.md` | Command surface, layer model (L1 read → L2 DOM → L3 raw XML), batch semantics |
| `references/officecli-pptx.md` | Full pptx element schema — shapes, charts, tables, animations, connectors, notes |
| `references/officecli-pitch-deck.md` | Narrative structure for fundraising / investor decks |
| `references/officecli-morph-ppt.md` | Morph transitions and animated sequences |

These are an upstream snapshot and **drift from the installed binary**. When a property name or enum is uncertain, `officecli help pptx <element>` is authoritative.

## Traps that cost the most time

- **Quote every path.** `"/slide[1]/shape[@id=100000]"` — unquoted `[1]` gets globbed by zsh.
- **Single-quote currency.** `--prop text='$15M'`; inside an unquoted batch heredoc escape as `\$`. Then `view text` and confirm the `$` survived — this fails silently.
- **`\n` in `text=` starts a new paragraph; `\v` is a line break within one.**
- **Set sizes explicitly on every text shape.** Theme defaults drift between masters. Decks that started life in another tool often carry an Office theme with Calibri as its default — anything not explicitly set to Arial comes out wrong.
- **Check after structural ops.** After adding a slide, chart, or table, `get` it before stacking more on top.
- **Clean-slate replay:** `close` → `rm` → `create` → `batch` → `close`. `create` refuses to overwrite, and ignoring its exit code silently replays onto the previous run's file.

## Starting from a style template

The most reliable way to get an on-style deck is to inherit the master, theme and layouts rather than rebuilding them. `house-style` ships one template file per style, each with 19 named layouts:

```bash
cp <house-style-skill>/templates/ana-blue/ana-blue.pptx deck.pptx
officecli open  deck.pptx
officecli query deck.pptx 'slideLayout' --json          # confirm the 19 layouts arrived
officecli add   deck.pptx slide --layout 'Title and Content'
```

Fill placeholders by index — the indices and exact geometry are in `house-style/references/layouts.md`, the grid in `house-style/references/grid.md`. Replace `{{ORG}}`, `{{UNIT}}`, `{{DECK_TITLE}}`, `{{DECK_TITLE_EN}}` and `{{CLASSIFICATION}}` before delivery; a file containing `{{` is a defect.

When starting from an **existing** deck instead, trim rather than rebuild:

```bash
cp existing_deck.pptx new_deck.pptx
officecli view   new_deck.pptx outline        # pick a slide whose layout matches the need
officecli remove new_deck.pptx '/slide[8]'    # trim down
```

## Delivering

Render a contact sheet and read it before every handoff. Grid drift, overflowing text boxes, and collided shapes are invisible in the DOM and immediately obvious in the render.

```bash
officecli view deck.pptx issues                                   # overflow, stale fields
python3 <house-style>/scripts/check_deck.py deck.pptx \
        --palette 'ANA Blue'                                      # content, craft, palette
officecli view deck.pptx screenshot --grid --out contact.png      # then read the PNG
officecli close deck.pptx
```

`check_deck.py` is the gate the other two cannot cover. It prints the title column for a
read-through, and fails the deck on an unreplaced `{{placeholder}}`, on a title that promises
a number its body contradicts, on a title too long for two lines, on a run set in the wrong
face, and on any colour outside the named palette. It warns on the tells of a deck assembled
rather than written: label-style titles, one sentence shape repeated across the deck, a body
filling under 55% of the content band, two spellings of one term, AI register. **FAIL must be 0.**
Add `--template` when checking a template file, where `{{placeholders}}` are the point.

Then the gate no machine can run: hand the file to an agent that has not seen the conversation
— the `Agent` tool, or a new session — and ask it to read the deck cold and report awkward
phrasing, jumps in the logic, a title that disagrees with its own figure, unsupported evaluative
words, a page that restates an earlier one. Sort the findings into accept / reject with a reason,
fix the accepted ones, re-run the machine check. `slide-craft.md` § 8 has the full procedure.
