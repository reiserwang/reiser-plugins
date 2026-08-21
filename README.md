# reiser-plugins

Claude plugin marketplace — Office document tooling and house style.

> **Private repository.** These plugins encode house design style. Before any change to visibility, re-read every skill **and unzip every bundled `.pptx`** looking for organisation names, product names, roadmap language, partner names, device SKUs, classification markings, internal file paths and personal identifiers — none belong in a public repo. `docProps/core.xml` inside a `.pptx` records the last editor's name; check it.
>
> ```bash
> # leak check across markdown and every bundled template
> grep -rniE '<your org and product names>' --include='*.md' --include='*.json' .
> for f in $(find . -name '*.pptx'); do
>   d=$(mktemp -d); unzip -qo "$f" -d "$d"
>   grep -rl --include='*.xml' -iE '<your org and product names>' "$d" && echo "LEAK in $f"
> done
> ```

## Install

```
/plugin marketplace add reiserwang/reiser-plugins
/plugin install office-cli@reiser-plugins
```

If the install summary says `Run /reload-plugins to activate.`, run that.

Because this repo is private, git must be able to authenticate on its own before the marketplace can be added:

```bash
gh auth setup-git          # GitHub over HTTPS
git ls-remote https://github.com/reiserwang/reiser-plugins   # should not prompt
```

GitHub `owner/repo` shorthand clones over SSH by default. If you'd rather use HTTPS, set `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1`.

For private marketplaces, background auto-updates run `git pull` with credential helpers disabled and can fail intermittently. Two settings make this predictable:

```bash
export CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE=1   # keep the clone instead of re-cloning
```

...and update manually when you want the latest:

```
/plugin marketplace update reiser-plugins
```

An SSH remote with a key in `ssh-agent` avoids the problem entirely — background pulls authenticate the same way your own commands do.

## Plugins

| Plugin | What it does |
|---|---|
| [`office-cli`](plugins/office-cli) | Office document creation and editing through the [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) document DOM, with interchangeable house-style templates applied by default. Five skills; `house-style` is both the router over `deck-design` / `deck-build` and the host for the template folders. |

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
└── README.md
```

Style templates live one-per-folder under `plugins/office-cli/skills/house-style/templates/`, each shipping `TEMPLATE.md`, `palette.md`, `theme.json` and a `.pptx`. Adding a template touches only its own folder plus two index tables — see `templates/README.md`.

`metadata.pluginRoot` is set to `./plugins`, so plugin `source` values are bare directory names (`"source": "office-cli"`) rather than full relative paths.

## Releasing a change

Users only receive an update when the **version field changes** — pushing edited files alone will not reach anyone.

1. Edit files under `plugins/<name>/`.
2. Bump `version` in **both** `plugins/<name>/.claude-plugin/plugin.json` and the matching entry in `.claude-plugin/marketplace.json`. Keep them equal; a mismatch is the most common cause of "my change didn't ship".
3. Validate: `claude plugin validate .` from the repo root. If a template `.pptx` changed, also open it and confirm the layout count, layout names and theme name before committing.
4. Commit and push.
5. Users run `/plugin marketplace update reiser-plugins`.

## Adding another plugin

```bash
mkdir -p plugins/new-plugin/.claude-plugin
# write plugins/new-plugin/.claude-plugin/plugin.json
```

Then add an entry to the `plugins` array in `.claude-plugin/marketplace.json` — a plugin directory that isn't listed there is invisible to the marketplace.

## Maintenance note

`office-cli` bundles a snapshot of the upstream OfficeCLI skill files as reference material. They drift from whatever `officecli` binary is installed, and the skills say so — `officecli help <format> <element>` is authoritative at runtime. When bumping the plugin version, that's the moment to re-pull the upstream skills and check whether the schema has moved.

Verified against officecli **1.0.144**.
