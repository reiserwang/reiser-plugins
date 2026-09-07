#!/usr/bin/env bash
# Verify officecli is installed, is the right package, and actually serves the
# document DOM. Idempotent; a second or two when it is already good.
#
#   bash <officecli-setup>/scripts/setup.sh
#
# exit 0 ready | 1 not installed | 2 wrong package | 3 present but DOM API broken
set -uo pipefail

ver=$(officecli --version 2>/dev/null | head -1)

if [ -z "$ver" ]; then
  cat <<'EOF'
NOT INSTALLED

  npm install -g @officecli/officecli     # the scoped name is mandatory
  officecli install                       # or: binary + skills + MCP in one step

The unscoped `officecli` on npm is a different product and will derail the task.
In the Cowork sandbox the upstream curl installer is blocked (403) — npm works.
device_bash has no network at all: either the user installs it in their own
terminal, or stage the file into the sandbox and do the work there.
EOF
  exit 1
fi

if ! printf '%s' "$ver" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+'; then
  cat <<EOF
WRONG PACKAGE — --version printed a banner, not a bare semver:

  $ver

That is officecli.io's hosted-credit AI generation TUI, not the document DOM.

  npm uninstall -g officecli && npm install -g @officecli/officecli && hash -r
EOF
  exit 2
fi

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
(
  cd "$tmp" || exit 3
  officecli create _probe.pptx >/dev/null 2>&1 &&
  officecli add _probe.pptx / --type slide --prop title=probe >/dev/null 2>&1 &&
  officecli view _probe.pptx text 2>/dev/null | grep -q probe
) || {
  echo "officecli $ver is installed but create → add → view did not round-trip."
  echo "The npm shim downloads a native binary on postinstall; a proxy, an"
  echo "air-gapped machine or --ignore-scripts leaves the shim without it."
  officecli close "$tmp/_probe.pptx" >/dev/null 2>&1
  exit 3
}
officecli close "$tmp/_probe.pptx" >/dev/null 2>&1

echo "officecli $ver — document DOM verified (create → add → view text)."
echo "Schema is served by the binary itself, always version-matched:"
echo "  officecli help pptx shape        # or docx / xlsx, any element"
echo "  officecli load_skill             # upstream's own skill docs, on demand"
