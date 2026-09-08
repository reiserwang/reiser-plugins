---
name: officecli-setup
description: Verify the officecli binary and drive the mechanics every OfficeCLI skill shares — schema lookup, JSON batch builds, resident mode, flushing. Use before the first officecli command of a session, when officecli is missing or errors with "command not found", when a session starts fresh in the Cowork cloud sandbox, when a command fails with unexpected syntax, or when building a document from more than a couple of edits.
---

# officecli — setup and shared mechanics

## 1. Verify

```bash
bash <officecli-setup>/scripts/setup.sh
```

Idempotent, a second or two when already installed. It checks the version, catches
the wrong same-named npm package, and proves the document DOM round-trips with a
real `create` → `add` → `view text`.

| Exit | Meaning |
|---|---|
| 0 | ready |
| 1 | not installed — the script prints the install lines for this environment |
| 2 | wrong package: unscoped `officecli` on npm is a hosted-credit AI TUI, not this tool |
| 3 | installed but the native binary never downloaded (proxy, air-gap, `--ignore-scripts`) |

Two environment facts the script cannot fix for you:

- **Cowork cloud sandbox** — `npm install -g @officecli/officecli` is the only route.
  The upstream `curl … install.sh` path, GitHub Releases and `api.github.com` are all
  403 here. The container is ephemeral, so a fresh session installs again.
- **`device_bash` (the user's Mac)** — no network at all, so nothing installs from there.
  Either the user runs `officecli install` in their own terminal, or you stage the file
  into the sandbox with `device_stage_files`, work there, and `device_commit_files` back.
  Prefer staging over blocking on a local install.

## 2. Ask the binary, never a snapshot

The binary serves its own schema and its own skill documentation, always matching the
installed version. This plugin deliberately vendors neither.

```bash
officecli help pptx                   # elements for a format
officecli help pptx shape             # full schema for one element
officecli help pptx add shape         # verb-scoped props
officecli help pptx shape --json      # machine-readable

officecli load_skill                  # upstream's skills and when each applies
officecli load_skill word             # its SKILL.md + a manifest of reference files
officecli load_skill excel --path reference/decision-rules.md
```

Upstream skills available: `pptx`, `word`, `excel`, `word-form`, `morph-ppt`,
`morph-ppt-3d`, `pitch-deck`, `academic-paper`, `data-dashboard`, `financial-model`.
Format aliases: `word`→`docx`, `excel`→`xlsx`, `ppt`/`powerpoint`→`pptx`.

One help query beats a guess-fail-retry loop.

## 3. Build with a JSON batch, not a command per edit

Anything past two or three edits is a batch. Each item is an object whose `command`
is the bare verb, with the verb's arguments as sibling fields:

```json
[
  {"command":"add","parent":"/","type":"slide","props":{"layout":"Title and Content"}},
  {"command":"add","parent":"/slide[1]","type":"placeholder",
   "props":{"phType":"title","text":"Q3 review"}},
  {"command":"set","path":"/slide[1]/shape[@phType=title]","props":{"bold":"true"}}
]
```

Note what the second item is **not**: a `shape` with hand-written coordinates. A slide
added with `layout` has zero shapes — the layout's slots are metadata until a placeholder
materialises them — so `set '/slide[1]/shape[1]'` here would fail with "Shape 1 not found
(total: 0)" and, a batch being atomic, take the whole build down with it. A placeholder
arrives carrying its layout slot's geometry, which is how a deck stays on the grid without
a single coordinate in the JSON.

Write that to a file, then:

```bash
bash <officecli-setup>/scripts/ocbuild.sh deck.pptx build.json
bash <officecli-setup>/scripts/ocbuild.sh --from <house-style>/templates/yukima/yukima.pptx \
     deck.pptx build.json          # inherit a template's master, theme and 19 layouts
```

`ocbuild.sh` runs `close` → `rm` → `create` (or copy the template) → `batch` → `close`
and checks every exit code. The order is not cosmetic: `create` refuses to overwrite, so
a rerun that ignores its exit code replays onto the *previous* run's document and every
`add style` fails with "already exists". The template file is copied, never opened for
writing. A batch is atomic by default — one bad item rolls the whole thing back, so a
failed run leaves nothing half-built. Rebuilding is then just editing the JSON and
running it again, which is also what makes a build reviewable.

To apply a batch to a document you are keeping, that is plain `officecli batch file
--input patch.json` followed by `officecli save` or `close`.

**Resident mode.** `officecli open <file>` holds the document in memory; subsequent
commands and batches apply there and the disk write is deferred (adaptive 2–10s idle
autosave, or `OFFICECLI_RESIDENT_FLUSH=each|auto|<seconds>|off`). For a long build that
is one process instead of a hundred. officecli's own reads always see uncommitted edits
— the failure mode is a *different* program reading a stale file, so `save` (flush, keep
warm) or `close` (flush, release) before python-docx/openpyxl, a renderer, `SendUserFile`
or `device_commit_files` touches it. **The `check_*.py` gates are such a program.** Run
`save` before them or they grade the last flushed version and pass a deck you have since
changed.

## 4. Notes that prevent most failures

- **Quote every path.** `"/slide[1]/shape[@id=100000]"` — zsh globs an unquoted `[1]` to
  `no matches found`. A JSON batch sidesteps the shell entirely, which is half of why it
  is the better default.
- **Single-quote currency.** `--prop text='$15M'` — double quotes let the shell eat `$1`.
  Then `view text` and confirm the `$` survived; it fails silently.
- **`\n` starts a new paragraph, `\v` is a line break within one.** In a JSON batch write
  the line break as `\u000b` — JSON has no `\v` escape and the file will not parse.
  `ocbuild.sh` says so by name when it rejects one.
- **A style must exist before it is used.** `"props":{"style":"Heading1"}` against a
  document that never defined `Heading1` writes the reference and renders as body text.
  Nothing errors. `check_doc.py` fails the document on it.
- **Sheet-scope xlsx selectors.** `officecli set book.xlsx A1` is rejected; use
  `"/sheet[1]/A1"` or `"/Sheet1/A1"`.
- **Check after structural ops.** After a new slide, chart or table, `get` it before
  stacking more onto it.
- **`raw` / `raw-set` / `add-part`** are the documented escape hatch when the DOM has no
  property for what you need — raw OpenXML, same file, no rebuild.

## 5. Verify what you built

```bash
officecli view deck.pptx issues                               # overflow, low contrast, stale fields
officecli validate report.docx                                # OpenXML schema
officecli view deck.pptx screenshot --page 3 --out s3.png     # one slide
officecli view deck.pptx screenshot --grid --out contact.png  # contact sheet
```

Read the PNG back. Overflowing text boxes, collided shapes and unreadable contrast are
invisible in the DOM and obvious in the render. Do this before delivering anything.
House-style deliverables have a further gate — `check_deck.py`, `check_doc.py`,
`check_book.py` in `house-style/scripts/`; see that skill.

## MCP, if you would rather have tools than a shell

The binary registers itself as an MCP server in Claude Code:

```bash
officecli mcp claude      # register    (targets: claude, cursor, vscode, lms)
officecli mcp list        # registration status
```

That trades shell quoting for structured tool calls, at the cost of the tool definitions
sitting in context for the whole session. This plugin does not register it for you —
the skills above are written for the CLI, and both surfaces drive the same DOM.
