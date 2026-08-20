---
name: pptx-cli
description: Build and edit PowerPoint decks through the officecli document DOM — precise shape-level control, layout inspection, and PNG rendering to verify the result. Use for brand-compliant decks, for editing or auditing an existing .pptx (extracting content, fixing layout, restyling, checking overflow), for merging or splitting decks, and whenever slide geometry must land exactly. Distinct from the python-based pptx skill — prefer this one for editing existing files and for anything on house style.
---
> Routed here by `corp-deliverable`. If you arrived directly and the task might involve a **new deck**, check `corp-deliverable` first — new decks go through `deck-design` → `deck-build`, not through this skill.


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
3. **Inspect before editing.** Never edit an existing deck blind:
   ```bash
   officecli view deck.pptx outline               # slide-by-slide structure
   officecli get  deck.pptx '/slide[3]' --json    # exact geometry & formatting
   officecli view deck.pptx screenshot --grid --out contact.png   # then read the PNG
   ```
4. **Edit** with `add` / `set` / `remove` / `move`, or a `batch` array for anything multi-step.
5. **Verify.** `view issues`, then re-render and read the PNG.
6. **Flush.** `officecli close deck.pptx` before `SendUserFile` or `device_commit_files`.

## Reference files

Load on demand — do not read all of them:

| File | When |
|---|---|
| `references/officecli-core.md` | Command surface, layer model (L1 read → L2 DOM → L3 raw XML), batch semantics |
| `references/officecli-pptx.md` | Full pptx element schema — shapes, charts, tables, animations, connectors, notes |
| `references/officecli-pitch-deck.md` | Narrative structure for fundraising / investor decks |
| `references/officecli-morph-ppt.md` | Morph transitions and animated sequences |

These are an upstream snapshot and **drift from the installed binary**. When a property name or enum is uncertain, `officecli help pptx <element>` is authoritative.

## Traps that cost the most time

- **Quote every path.** `"/slide[1]/shape[@id=100000]"` — unquoted `[1]` gets globbed by zsh.
- **Single-quote currency.** `--prop text='$15M'`; inside an unquoted batch heredoc escape as `\$`. Then `view text` and confirm the `$` survived — this fails silently.
- **`\n` in `text=` starts a new paragraph; `\v` is a line break within one.**
- **Set sizes explicitly on every text shape.** Theme defaults drift between masters. The house decks carry an Office theme with Calibri as its default — anything not explicitly set to Arial comes out wrong.
- **Check after structural ops.** After adding a slide, chart, or table, `get` it before stacking more on top.
- **Clean-slate replay:** `close` → `rm` → `create` → `batch` → `close`. `create` refuses to overwrite, and ignoring its exit code silently replays onto the previous run's file.

## Starting from the corporate deck

The most reliable way to get an on-brand deck is to inherit the master, theme, and wordmark rather than rebuilding them:

```bash
cp corporate_master_deck.pptx new_deck.pptx
officecli view new_deck.pptx outline          # pick a slide whose layout matches the need
officecli remove new_deck.pptx '/slide[8]'    # trim down
```

Then rebuild content shapes on the retained slides using the geometry in `house-style/references/slide-grid.md`.

## Delivering

Render a contact sheet and read it before every handoff. Grid drift, overflowing text boxes, and collided shapes are invisible in the DOM and immediately obvious in the render.

```bash
officecli view deck.pptx issues
officecli view deck.pptx screenshot --grid --out contact.png
officecli close deck.pptx
```
