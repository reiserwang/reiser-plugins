---
name: officecli-setup
description: Install, verify, and troubleshoot the officecli binary before any OfficeCLI-based Office document work. Use when officecli is missing or errors with "command not found", when a session starts fresh in the Cowork cloud sandbox, when officecli commands fail with unexpected syntax, or when the user asks to set up / install / update officecli.
---

# officecli setup

Run this before the first officecli command of a session. It is idempotent and takes seconds when already installed.

## Step 1 — check

```bash
officecli --version
```

Expect a bare semver like `1.0.144`. Proceed straight to the format skill if it prints one.

**If it prints a banner about "AI document generation", "hosted credits", "100 free credits", or a `new` / `login` / `whoami` command list — the WRONG package is installed.** See Wrong Package below.

## Step 2 — install by environment

Determine which environment the command will run in, then use the matching path. The two are not interchangeable.

### Cowork cloud sandbox (the `Bash` tool)

```bash
npm install -g @officecli/officecli
```

The **scoped** name is mandatory. Two things break here otherwise:

| Trap | What happens |
|---|---|
| `curl -fsSL https://d.officecli.ai/install.sh \| bash` | **403.** The upstream docs' primary install path is not on the sandbox network allowlist. GitHub Releases and `api.github.com` are also 403. |
| `npm install -g officecli` (unscoped) | **Installs an unrelated package.** `officecli` on npm is a different product (officecli.io, UNLICENSED, hosted-credit AI generation TUI). It has no `create`/`add`/`set`/`get`/`view` DOM commands and will silently derail the whole task. |

npm registry access works, so the scoped package is the only reliable route. Install once per session — the cloud container is ephemeral, so a fresh session needs it again.

### The user's Mac (`device_bash`, or their local Claude Code)

`device_bash` has **no network access** — it cannot install anything. Check whether it is already present:

```bash
officecli --version || echo "NOT INSTALLED"
```

If not installed, do not try to install it from `device_bash`. Tell the user to run **one** of these in their own terminal, then continue:

```bash
curl -fsSL https://d.officecli.ai/install.sh | bash    # upstream installer
npm install -g @officecli/officecli                    # or via npm
```

Meanwhile, the fallback that always works: stage the file into the cloud sandbox with `device_stage_files`, do the officecli work there against a copy, and write the result back with `device_commit_files`. Prefer this over blocking on a local install.

## Step 3 — verify the DOM API, not just the version

A version string alone does not prove the right binary. Confirm with a real round-trip:

```bash
cd /tmp && officecli create _probe.pptx \
  && officecli add _probe.pptx / --type slide --prop title="probe" \
  && officecli view _probe.pptx text \
  && officecli close _probe.pptx && rm -f _probe.pptx
```

`create` → `add` → `view text` returning `probe` means the document-DOM binary is live.

## Wrong package installed

```bash
npm uninstall -g officecli
npm install -g @officecli/officecli
hash -r
officecli --version
```

## Help is authoritative

The bundled reference files in this plugin were captured from an upstream snapshot and **drift from the installed binary**. When a property name, enum value, verb, or alias is uncertain, query the binary instead of guessing:

```bash
officecli help                        # all commands
officecli help pptx                   # elements for a format
officecli help pptx shape             # full schema for one element
officecli help pptx add shape         # verb-scoped props
officecli help pptx shape --json      # machine-readable
```

Format aliases: `word`→`docx`, `excel`→`xlsx`, `ppt`/`powerpoint`→`pptx`.

Where help and a reference file disagree, **help wins**. One help query beats a guess-fail-retry loop.

## Operating notes that prevent most failures

- **Quote every path.** `"/slide[1]/shape[@id=100000]"` — zsh globs an unquoted `[1]` to `no matches found`.
- **Single-quote currency.** `--prop text='$15M'`. Double quotes let the shell eat `$1`. Inside an unquoted `batch` heredoc, escape as `\$`. Verify with `view text` afterwards.
- **Flush before anyone else reads.** officecli keeps documents resident in memory. Run `officecli save <file>` (keeps it warm) or `officecli close <file>` (flush + release) before python-docx/openpyxl, a renderer, `SendUserFile`, or `device_commit_files` touches the file. officecli's own reads always see uncommitted edits — the failure mode is delivering a stale file.
- **Sheet-scope xlsx selectors.** `officecli set book.xlsx A1` is rejected as a bare selector; use `"/sheet[1]/A1"`.
- **Clean-slate replay.** `create` refuses to overwrite. Idiom: `close` → `rm` → `create` → `batch` → `close`.
- **One command, check exit code, continue.** After any structural op (new slide, chart, table), run `get` before stacking more onto it.

## Rendering to check the work

```bash
officecli view deck.pptx screenshot --page 3 --out s3.png     # one slide
officecli view deck.pptx screenshot --grid --out contact.png  # contact sheet
officecli view deck.pptx issues                               # overflow, low contrast, stale fields
```

Read the PNG back. Layout defects — overflowing text boxes, collided shapes, unreadable contrast — are invisible in the DOM and obvious in the render. Do this before delivering any deck.
