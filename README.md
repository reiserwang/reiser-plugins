# reiser-plugins

**English** · [繁體中文](README.zh-TW.md)

Claude plugin marketplace — Office document tooling and house-style templates.

> **Private repository.** These plugins encode house design style. Before any change to visibility, re-read every skill **and unzip every bundled `.pptx`** looking for organisation names, product names, roadmap language, partner names, device SKUs, classification markings, internal file paths and personal identifiers — none belong in a public repo. `docProps/core.xml` inside a `.pptx` records the last editor's name; check it. See [Leak check](#leak-check).

---

## What you get

One plugin, `office-cli`, with five skills and two interchangeable design templates.

| Skill | What it does |
|---|---|
| `house-style` | **The entry point.** Picks the design template, then picks the tool — copy a template, generate a new deck, or edit an existing file. |
| `officecli-setup` | Installs and verifies the `officecli` binary. Run first in a fresh session. |
| `pptx-cli` | Slide decks — build, edit, audit, render to PNG. |
| `docx-cli` | Reports, memos, board papers, approval routing forms, tracked changes. |
| `xlsx-cli` | Financial models, KPI workbooks, pivots, charts, with live formulas. |

| Template | Field | Accent | Use it for |
|---|---|---|---|
| **ANA Blue** | white | deep blue `#0B318F` | anything brand-facing — board, regulator, investor, customer, partner |
| **Reiser Warm** | warm cream | coral `#CC785C` | personal work, drafts, internal thinking documents |

Both carry the same 19 named layouts on the same 1440 × 810 pt grid, so switching between them is a restyle, not a rebuild.

---

## Install

```
/plugin marketplace add reiserwang/reiser-plugins
/plugin install office-cli@reiser-plugins
```

If the install summary says `Run /reload-plugins to activate.`, run that.

Alternatively, if someone hands you an `office-cli.plugin` file, open it — the desktop app shows the contents and an install button, no repo access needed.

### Private-repo authentication

Because this repo is private, git must be able to authenticate on its own before the marketplace can be added:

```bash
gh auth setup-git                                            # GitHub over HTTPS
git ls-remote https://github.com/reiserwang/reiser-plugins   # should not prompt
```

GitHub `owner/repo` shorthand clones over SSH by default. To prefer HTTPS, set `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1`.

Background auto-updates for private marketplaces run `git pull` with credential helpers disabled and can fail intermittently. This makes it predictable:

```bash
export CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE=1   # keep the clone instead of re-cloning
```

…then update manually when you want the latest:

```
/plugin marketplace update reiser-plugins
```

An SSH remote with a key in `ssh-agent` avoids the problem entirely — background pulls then authenticate the same way your own commands do.

---

## Using it

You don't call the skills directly. Describe the deliverable and `house-style` routes it. Some things that work:

```
Build me a board deck on Q3 security posture, ANA Blue, from these notes.
Restyle this deck into Reiser Warm.
Fix the overflowing titles in slides 4-9 of deck.pptx.
Turn this spreadsheet into a KPI workbook on brand.
Draft the quarterly report as a Word document.
```

### First run in a fresh session

The `officecli` binary is not preinstalled. Say **"set up officecli"** — or just start a task and the skill will handle it. Two traps it exists to avoid:

- The documented curl installer (`d.officecli.ai/install.sh`) returns **403** in the cloud sandbox, as do GitHub Releases. The npm registry works.
- `npm install -g officecli` installs the **wrong product** — an unrelated AI TUI. The correct package is `@officecli/officecli`.

### Starting a deck from a template

The fastest and most faithful route, because it inherits the master, theme and all 19 layouts:

```bash
cp plugins/office-cli/skills/house-style/templates/ana-blue/ana-blue.pptx deck.pptx
officecli open deck.pptx
officecli add  deck.pptx slide --layout 'Cover'
```

Layout names, placeholder indices and exact coordinates are in `skills/house-style/references/layouts.md`.

### Filling in the placeholders

The templates carry **no** organisation or product language by design. Footers and covers ship placeholders you must replace:

| Placeholder | Fill with |
|---|---|
| `{{ORG}}` | the organisation name as it appears in the footer |
| `{{UNIT}}` | the issuing department or unit |
| `{{DECK_TITLE}}` / `{{DECK_TITLE_EN}}` | the title, 中文 and English |
| `{{CLASSIFICATION}}` | the handling marking, if the deliverable carries one |

A delivered file still containing `{{` is a defect. Check before you send:

```bash
officecli view deck.pptx text | grep '{{' && echo "PLACEHOLDERS LEFT"
```

### Before you send anything

```bash
officecli view  deck.pptx issues                              # overflow, low contrast, stale fields
officecli view  deck.pptx screenshot --grid --out contact.png # then actually look at it
officecli close deck.pptx                                     # flush, or you deliver the pre-edit file
```

That middle step matters more than it sounds: grid drift and overflowing text boxes are invisible in the document model and obvious in an image.

### One rule about the template files

**Never open a shipped template in PowerPoint.** A re-save re-injects revision-tracking parts and stamps the editor's name into `docProps/core.xml`. Copy the file first, then edit the copy.

---

## Where the documentation lives

```
plugins/office-cli/skills/house-style/
├── SKILL.md                 pick a template, pick a pipeline, the non-negotiables
├── references/
│   ├── grid.md              canvas, margins, column arithmetic, vertical rhythm
│   ├── layouts.md           all 19 layouts, every shape, exact coordinates
│   ├── pipelines.md         template copy · deck-design/deck-build · Word & Excel
│   └── contrast.md          the contrast gate and every verified ratio
└── templates/
    ├── README.md            how to add a third template
    ├── ana-blue/            TEMPLATE.md · palette.md · theme.json · ana-blue.pptx
    └── reiser-warm/         TEMPLATE.md · palette.md · theme.json · reiser-warm.pptx
```

Read `SKILL.md`, then exactly one `TEMPLATE.md`. Everything else loads on demand.

---

## Repo layout

```
reiser-plugins/
├── .claude-plugin/
│   └── marketplace.json        # the catalog — every plugin must be listed here
├── plugins/
│   └── office-cli/
│       ├── .claude-plugin/plugin.json
│       └── skills/
│           ├── house-style/    # router + shared references + templates/<name>/
│           ├── officecli-setup/
│           ├── pptx-cli/
│           ├── docx-cli/
│           └── xlsx-cli/
├── README.md
└── README.zh-TW.md
```

`metadata.pluginRoot` is set to `./plugins`, so plugin `source` values are bare directory names rather than full relative paths.

---

## Releasing a change

Users only receive an update when the **version field changes** — pushing edited files alone will not reach anyone.

1. Edit files under `plugins/<name>/`.
2. Bump `version` in **both** `plugins/<name>/.claude-plugin/plugin.json` and the matching entry in `.claude-plugin/marketplace.json`. Keep them equal; a mismatch is the most common cause of "my change didn't ship".
3. Validate: `claude plugin validate .` from the repo root.
4. If a template `.pptx` changed, open it and confirm the layout count, layout names and theme name — and run the leak check below.
5. Commit and push.
6. Users run `/plugin marketplace update reiser-plugins`.

### Packaging a standalone `.plugin`

To hand the plugin to someone without repo access:

```bash
cd plugins/office-cli
zip -rq /tmp/office-cli.plugin . -x "*.DS_Store"
```

The archive root must contain `.claude-plugin/plugin.json` — no wrapper folder.

### Leak check

Run this before any release, and always before changing repository visibility. Replace the pattern with your own organisation, unit and product names.

```bash
PAT='your-org|your-unit|your-product'

grep -rniE "$PAT" --include='*.md' --include='*.json' .

for f in $(find . -name '*.pptx'); do
  d=$(mktemp -d); unzip -qo "$f" -d "$d"
  grep -rl --include='*.xml' --include='*.rels' -iE "$PAT" "$d" && echo "LEAK in $f"
  grep -o '<cp:lastModifiedBy>[^<]*' "$d/docProps/core.xml"
  rm -rf "$d"
done
```

The `lastModifiedBy` line is the one people forget. It is how a personal name gets into a "de-identified" template.

---

## Adding another plugin

```bash
mkdir -p plugins/new-plugin/.claude-plugin
# write plugins/new-plugin/.claude-plugin/plugin.json
```

Then add an entry to the `plugins` array in `.claude-plugin/marketplace.json` — a plugin directory that isn't listed there is invisible to the marketplace.

---

## Maintenance note

`office-cli` bundles a snapshot of the upstream OfficeCLI skill files as reference material. They drift from whatever `officecli` binary is installed, and the skills say so — `officecli help <format> <element>` is authoritative at runtime. When bumping the plugin version, that's the moment to re-pull the upstream skills and check whether the schema has moved.

Bundled reference files under `skills/*/references/officecli-*.md` are from [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI), Apache-2.0. See `LICENSE-officecli.txt` and `NOTICE-officecli.txt`.

Verified against officecli **1.0.144**.
