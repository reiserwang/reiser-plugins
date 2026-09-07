#!/usr/bin/env bash
# Clean-slate replay of a JSON batch into a document, with the exit-code checks
# the idiom silently fails without.
#
#   bash ocbuild.sh deck.pptx build.json
#   bash ocbuild.sh --from <house-style>/templates/yukima/yukima.pptx deck.pptx build.json
#
# --from inherits a template's master, theme and layouts instead of building
# furniture from nothing; the template file itself is never modified.
#
# Why a script: `create` refuses to overwrite, so a rerun that ignores its exit
# code replays onto the PREVIOUS run's document and every `add style` fails with
# 'already exists'. The order close -> rm -> create matters, and the trailing
# close is what flushes the resident to disk before anyone else reads the file.
#
# The batch is atomic by default: one bad item rolls the whole thing back, so a
# failed run leaves an empty document rather than a half-built one.
set -uo pipefail

from=""
if [ "${1:-}" = "--from" ]; then
  from="${2:-}"
  shift 2
  [ -f "$from" ] || { echo "no such template: $from" >&2; exit 2; }
fi

out="${1:-}"
batch="${2:-}"
if [ -z "$out" ] || [ -z "$batch" ]; then
  sed -n '2,12p' "$0" >&2
  exit 2
fi
[ -f "$batch" ] || { echo "no such batch file: $batch" >&2; exit 2; }

python3 - "$batch" <<'VALIDATE' || { echo "batch JSON rejected before touching $out" >&2; exit 2; }
import json, sys
try:
    items = json.load(open(sys.argv[1]))
except json.JSONDecodeError as e:
    hint = ("  JSON has no \\v escape: a line break inside a paragraph is \\u000b, "
            "and a new paragraph is \\n." if "Invalid \\escape" in e.msg else "")
    sys.exit(f"{sys.argv[1]}: {e.msg}, line {e.lineno} column {e.colno}.{hint}")
if not isinstance(items, list):
    sys.exit("batch must be a JSON array of command objects")
bad = [i for i, x in enumerate(items) if not isinstance(x, dict) or "command" not in x]
if bad:
    sys.exit(f'items {bad} are not objects with a "command" key')
VALIDATE

officecli close "$out" >/dev/null 2>&1
rm -f "$out"

if [ -n "$from" ]; then
  cp "$from" "$out" || exit 1
  officecli open "$out" >/dev/null || exit 1
else
  officecli create "$out" >/dev/null || { echo "create failed: $out" >&2; exit 1; }
fi

if ! officecli batch "$out" --input "$batch"; then
  echo "batch failed — rolled back, $out is left at its pre-batch state" >&2
  officecli close "$out" >/dev/null 2>&1
  exit 1
fi

officecli close "$out" || exit 1
echo "built $out from $batch$([ -n "$from" ] && echo " on $(basename "$from")")"
