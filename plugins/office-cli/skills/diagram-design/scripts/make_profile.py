#!/usr/bin/env python3
"""Derive a diagram-design style guide from a house-style template's theme.json.

The templates are the single source of truth for every palette in this system.
Rather than hand-copying their hex values into a second place — where they would
drift the moment a template changed — this generates the diagram-design style
guide from `templates/<name>/theme.json` and verifies every ratio on the way out.

    python3 make_profile.py ana-blue                 # -> stdout
    python3 make_profile.py ana-blue -o out.md
    python3 make_profile.py --all -o profiles/       # all six, one file each

Semantic roles diagram-design expects, and where each comes from:

    paper      <- colors.bg           ink        <- colors.ink
    paper-2    <- colors.bg_alt       muted      <- colors.ink_soft
    rule       <- colors.rule @12%    soft       <- derived from muted, darkened
    rule-solid <- colors.rule         accent     <- colors.accent, text-safe
    link       <- series[2] or accent accent-tint<- accent @10%

Two derivations do real work:

  * `soft` has no equivalent in theme.json. Sublabels are 9px, so it is darkened
    from `muted` until it clears 4.5:1 on the panel tint, not merely on the field.
  * `accent` in diagram-design carries label *text* as well as strokes. Where a
    template's accent fails 4.5:1 as text — Reiser Warm's coral is 2.92:1 — the
    hue is preserved and the value darkened until it passes. The original stays
    available as `accent-tint`. This is the single most common way a diagram in a
    house palette ends up unreadable.
"""
import argparse, colorsys, json, os, sys
from datetime import date

ROLE_ORDER = ["paper", "paper-2", "ink", "muted", "soft", "rule", "rule-solid",
              "accent", "accent-tint", "link"]


def _lin(c):
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def lum(hexstr):
    h = hexstr.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def cr(a, b):
    l1, l2 = sorted((lum(a), lum(b)), reverse=True)
    return round((l1 + 0.05) / (l2 + 0.05), 2)


def shift(hexstr, bg, target=4.5, limit=200):
    """Darken or lighten hexstr, hue preserved, until it clears `target` on bg."""
    h = hexstr.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    hh, s, v = colorsys.rgb_to_hsv(r, g, b)
    up = lum(bg) < 0.5                       # light text on a dark field
    for i in range(1, limit + 1):
        f = 1 + i / limit if up else 1 - i / limit
        vv = max(0.0, min(1.0, v * f))
        rr, gg, bb = colorsys.hsv_to_rgb(hh, s, vv)
        cand = "#%02X%02X%02X" % tuple(round(x * 255) for x in (rr, gg, bb))
        if cr(cand, bg) >= target:
            return cand
    return "#000000" if not up else "#FFFFFF"


def rgba(hexstr, alpha):
    h = hexstr.lstrip("#")
    return "rgba(%d,%d,%d,%s)" % (*(int(h[i:i + 2], 16) for i in (0, 2, 4)), alpha)


def derive(theme):
    c = theme["colors"]
    dark = bool(theme.get("dark"))
    paper, paper2 = c["bg"], c.get("bg_alt", c["bg"])
    ink, muted = c["ink"], c["ink_soft"]
    accent_src = c["accent"]

    accent = accent_src if cr(accent_src, paper) >= 4.5 else shift(accent_src, paper)
    soft = shift(muted, paper2, 4.5)
    series = [s for s in c.get("series", []) if s.upper() != accent_src.upper()]
    link = next((s for s in series if cr(s, paper) >= 4.5), accent)

    return dict(
        dark=dark,
        paper=paper, paper2=paper2, ink=ink, muted=muted, soft=soft,
        rule=rgba(ink, "0.12"), rule_solid=c.get("rule", paper2),
        accent=accent, accent_src=accent_src, accent_tint=rgba(accent_src, "0.10"),
        link=link, series=series[:5],
        fonts=theme.get("fonts", {}),
        geometry=theme.get("geometry", {}),
        never=theme.get("never", []),
    )


def render(name, slug, theme, d):
    def row(role, val, on=None):
        r = f"**{cr(val, on)}:1**" if on and val.startswith("#") else "—"
        return f"| `{role}` | `{val}` | {r} |"

    note = ""
    if d["accent"].upper() != d["accent_src"].upper():
        note = (f"\n> **`accent` is `{d['accent']}`, not the template's `{d['accent_src']}`.** "
                f"`{d['accent_src']}` is {cr(d['accent_src'], d['paper'])}:1 on this field and cannot carry text; "
                f"diagram-design uses `accent` for node labels as well as strokes, so the token has to be the "
                f"text-safe value. The template's accent survives as `accent-tint`, which is the fill role it "
                f"was always safe in.\n")

    fill_only = [s for s in d["series"] if cr(s, d["paper"]) < 4.5]
    fo = ""
    if fill_only:
        fo = ("\n> **Fill-only in this palette:** " +
              ", ".join(f"`{s}` ({cr(s, d['paper'])}:1)" for s in fill_only) +
              ". Legal as node fills, strokes and chart series; never as label text.\n")

    return f"""<!-- diagram-design-profile
name: {name}
slug: {slug}
source-url: none
created: {date.today()}
updated: {date.today()}
notes: generated by scripts/make_profile.py from templates/{slug}/theme.json — do not hand-edit
-->
# Style Guide

**{name}.** Generated from `house-style/templates/{slug}/theme.json`, which is the single source of truth for this palette. Regenerate rather than editing:

```bash
python3 scripts/make_profile.py {slug}
```

Every ratio below was computed at generation time against the surface the token actually sits on.

---

## Tokens

### Semantic roles

| Role | Value | Contrast on `paper` |
|---|---|---|
{row('paper', d['paper'])}
{row('paper-2', d['paper2'])}
{row('ink', d['ink'], d['paper'])}
{row('muted', d['muted'], d['paper'])}
{row('soft', d['soft'], d['paper'])}
{row('rule', d['rule'])}
{row('rule-solid', d['rule_solid'])}
{row('accent', d['accent'], d['paper'])}
{row('accent-tint', d['accent_tint'])}
{row('link', d['link'], d['paper'])}
{note}
`soft` carries 9px sublabels, so it is derived to clear 4.5:1 on the **panel tint** `{d['paper2']}` ({cr(d['soft'], d['paper2'])}:1), not merely on the field — a sublabel inside a panel is the case that fails first.

### Series palette

The 1-focal rule holds: `accent` is the focal series, these cover the rest.

| Token | Value | On `paper` |
|---|---|---|
""" + "\n".join(f"| `series-{i+1}` | `{s}` | {cr(s, d['paper'])}:1 |"
                for i, s in enumerate(d["series"])) + f"""

Fills at `0.18` opacity, strokes at full value. Do not backfill these to non-chart types.
{fo}
---

## Typography

| Role | Family | Size | Weight |
|---|---|---|---|
| `title` | {d['fonts'].get('heading', 'Arial')} | 1.75rem | 400 |
| `node-name` | {d['fonts'].get('body', 'Arial')} | 12px | 600 |
| `sublabel` | {d['fonts'].get('mono', 'Consolas')} | 9px | 400 |
| `eyebrow` | {d['fonts'].get('mono', 'Consolas')} | 7–8px | 500, tracked 0.18em, uppercase |
| `arrow-label` | {d['fonts'].get('mono', 'Consolas')} | 8px | 400 |

Latin is `{d['fonts'].get('body', 'Arial')}`, 中文 is `{d['fonts'].get('body_alt', '微軟正黑體')}` — set both on any mixed-script label, or the CJK falls back to a serif on Windows.

---

## Geometry

Near-square: containers at 0px, nodes and chips at most 4px. 1px hairlines. No shadows.

**This diverges from the template on purpose.** `{slug}.pptx` runs panels at ~{d['geometry'].get('radius', 18)}pt radius. A deck panel is brand surface; a diagram node is structure, and near-square keeps nodes reading as schematic rather than as UI cards. Do not reconcile them.

---

## Inherited never-rules

From `templates/{slug}/theme.json`:

""" + "\n".join(f"- {n}" for n in d["never"]) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", nargs="?", help="template slug, e.g. ana-blue")
    ap.add_argument("--all", action="store_true", help="generate every template")
    ap.add_argument("-o", "--out", help="output file, or directory with --all")
    ap.add_argument("--templates", default=None, help="path to house-style/templates")
    a = ap.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    tdir = a.templates or os.path.normpath(
        os.path.join(here, "..", "..", "house-style", "templates"))
    if not os.path.isdir(tdir):
        sys.exit(f"templates not found: {tdir}  (pass --templates)")

    slugs = (sorted(d for d in os.listdir(tdir)
                    if os.path.isfile(os.path.join(tdir, d, "theme.json")))
             if a.all else [a.slug])
    if not slugs or slugs == [None]:
        sys.exit("give a template slug or --all")

    for slug in slugs:
        p = os.path.join(tdir, slug, "theme.json")
        if not os.path.exists(p):
            sys.exit(f"no theme.json for '{slug}' in {tdir}")
        theme = json.load(open(p, encoding="utf-8"))
        out = render(theme.get("name", slug), slug, theme, derive(theme))
        if a.all and a.out:
            os.makedirs(a.out, exist_ok=True)
            dest = os.path.join(a.out, f"{slug}.md")
            open(dest, "w", encoding="utf-8").write(out)
            print(f"wrote {dest}")
        elif a.out:
            open(a.out, "w", encoding="utf-8").write(out)
            print(f"wrote {a.out}")
        else:
            print(out)


if __name__ == "__main__":
    main()
