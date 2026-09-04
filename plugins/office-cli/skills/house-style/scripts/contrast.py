#!/usr/bin/env python3
"""Compute every contrast ratio in every house-style palette.

Run from anywhere:

    python3 scripts/contrast.py               # print the matrix
    python3 scripts/contrast.py --write       # regenerate references/contrast-matrix.md
    python3 scripts/contrast.py --check       # verify tokens against the .pptx files, exit 1 on drift

The token tables below are the authoritative list. `--check` confirms that every
token in the field, supporting and accent bands actually appears inside its
template's .pptx, so the docs cannot claim page furniture the file does not
contain. Categorical tokens and tokens marked `optional` are palette entries
available for charts and coding; the 19 layouts do not have to use them, so
their absence is reported as a note rather than a failure.

WCAG gate: >= 4.5:1 below 24px, >= 3.0:1 at or above.
"""
import argparse
import json
import os
import re
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
TEMPLATES = os.path.join(SKILL, "templates")

# name, hex, band, role.  band: field | supporting | accent | categorical | derived-ink
PALETTES = {
    "ANA Blue": {
        "folder": "ana-blue",
        "surfaces": ["#FFFFFF", "#F0F6FC", "#E6F2FC"],
        "accent_field": "#0B318F",
        "tokens": [
            ("white",            "#FFFFFF", "field",       "page"),
            ("panel",            "#F0F6FC", "field",       "inset surface"),
            ("callout",          "#E6F2FC", "field",       "lifted surface"),
            ("rule",             "#C3D6EE", "field",       "rules and borders"),
            ("muted fill",       "#AFC0D6", "field",       "inactive states"),
            ("muted fill alt",   "#AEC6E8", "field",       "inactive states"),
            ("headline ink",     "#1A2230", "supporting",  "titles, body"),
            ("muted ink",        "#5A6676", "supporting",  "captions, footers"),
            ("muted ink alt",    "#647084", "supporting",  "deprecated - fails on callout"),
            ("deep blue",        "#0B318F", "accent",      "accent as area; supporting as type"),
            ("sky",              "#00A3E6", "accent",      "fill only"),
            ("text-safe sky",    "#00719E", "accent",      "derived text-safe sky"),
            ("cat blue",         "#2E5BF0", "categorical", "compute / cloud"),
            ("cat purple",       "#7C4DB8", "categorical", "AI / analytics"),
            ("cat green",        "#2FA84F", "categorical", "healthy / operational"),
        ],
        "derived": ["#00719E"],
        "optional": ["#AEC6E8", "#647084"],
    },
    "Reiser Warm": {
        "folder": "reiser-warm",
        "surfaces": ["#F5F1ED", "#E8E4DF", "#F5F3F1"],
        "accent_field": "#CC785C",
        "tokens": [
            ("warm cream",       "#F5F1ED", "field",       "page"),
            ("cool white",       "#F5F3F1", "field",       "lifted surface"),
            ("warm grey",        "#E8E4DF", "field",       "inset surface"),
            ("stone",            "#D4D0C9", "field",       "rules and borders"),
            ("charcoal",         "#1F1E1D", "supporting",  "titles, body"),
            ("muted ink",        "#5C5650", "supporting",  "captions, footers"),
            ("sage mist",        "#B3CBC1", "supporting",  "tint, fill only"),
            ("coral",            "#CC785C", "accent",      "fill only"),
            ("coral deep",       "#9D5C47", "accent",      "derived text-safe coral"),
            ("cat blue",         "#5C7B9C", "categorical", "series 2"),
            ("cat sage",         "#6B8E5C", "categorical", "series 3"),
            ("cat gold",         "#C28E3D", "categorical", "series 4"),
            ("cat violet",       "#8B7BAB", "categorical", "series 5"),
            ("cat teal",         "#5C9C8E", "categorical", "series 6"),
        ],
        "derived": ["#9D5C47", "#5C5650"],
        "optional": ["#B3CBC1"],
    },
    "SKS Blue": {
        "folder": "sks-blue",
        "surfaces": ["#FFFFFF", "#F1F4FC", "#E5E9F6"],
        "accent_field": "#1B3585",
        "tokens": [
            ("white",            "#FFFFFF", "field",       "page"),
            ("panel",            "#F1F4FC", "field",       "inset surface"),
            ("callout",          "#E5E9F6", "field",       "lifted surface"),
            ("rule",             "#C9D2EA", "field",       "rules and borders"),
            ("muted fill",       "#A9B6D6", "field",       "inactive states"),
            ("headline ink",     "#101623", "supporting",  "titles, body"),
            ("muted ink",        "#444E60", "supporting",  "captions, footers"),
            ("blue",             "#2F55F0", "accent",      "accent as area; supporting as type"),
            ("blue deep",        "#1B3585", "accent",      "the full-bleed divider field"),
            ("cat blue",         "#3D6AFF", "categorical", "series 1 - shared ramp, mark only"),
            ("cat cyan",         "#1A83A3", "categorical", "series 2 - shared ramp, mark only"),
            ("cat teal",         "#268777", "categorical", "series 3 - shared ramp, mark only"),
            ("cat green",        "#218A4B", "categorical", "series 4 - shared ramp, mark only"),
            ("cat amber",        "#9E7015", "categorical", "series 5 - shared ramp, mark only"),
            ("cat violet",       "#9C53E6", "categorical", "series 6 - shared ramp, mark only"),
            ("cat orange",       "#C95624", "categorical", "series 7 - shared ramp, mark only"),
            ("cat rose",         "#D4446A", "categorical", "series 8 - shared ramp, mark only"),
        ],
        "derived": [],
        "optional": [],
    },
    "SKS Blue Dark": {
        "folder": "sks-blue",
        "pptx_file": "sks-blue-dark.pptx",
        "theme_file": "theme.dark.json",
        "surfaces": ["#080D1A", "#101832", "#16204A"],
        "accent_field": "#1B3585",
        "tokens": [
            ("midnight",         "#080D1A", "field",       "page"),
            ("panel",            "#101832", "field",       "inset surface"),
            ("callout",          "#16204A", "field",       "lifted surface"),
            ("rule",             "#2A3760", "field",       "rules and borders"),
            ("muted fill",       "#3A4A7A", "field",       "inactive states"),
            ("headline ink",     "#FFFFFF", "supporting",  "titles, body, reverse ink"),
            ("muted ink",        "#A8B4CE", "supporting",  "captions, footers"),
            ("blue light",       "#8CB8FF", "supporting",  "the accent as type on this field"),
            ("blue",             "#2F55F0", "accent",      "accent as area only - 3.40 on the field"),
            ("blue deep",        "#1B3585", "accent",      "the full-bleed divider field"),
            ("cat blue",         "#3D6AFF", "categorical", "series 1 - shared ramp, mark only"),
            ("cat cyan",         "#1A83A3", "categorical", "series 2 - shared ramp, mark only"),
            ("cat teal",         "#268777", "categorical", "series 3 - shared ramp, mark only"),
            ("cat green",        "#218A4B", "categorical", "series 4 - shared ramp, mark only"),
            ("cat amber",        "#9E7015", "categorical", "series 5 - shared ramp, mark only"),
            ("cat violet",       "#9C53E6", "categorical", "series 6 - shared ramp, mark only"),
            ("cat orange",       "#C95624", "categorical", "series 7 - shared ramp, mark only"),
            ("cat rose",         "#D4446A", "categorical", "series 8 - shared ramp, mark only"),
        ],
        "derived": [],
        "optional": [],
    },
    "SKS Dark": {
        "folder": "sks-dark",
        "surfaces": ["#1A293A", "#213040", "#273546"],
        "accent_field": "#8A5613",
        "tokens": [
            ("midnight",         "#1A293A", "field",       "page"),
            ("panel",            "#213040", "field",       "inset surface"),
            ("callout",          "#273546", "field",       "lifted surface"),
            ("rule",             "#3E4C5A", "field",       "rules and borders"),
            ("deep steel",       "#546D85", "field",       "inactive states"),
            ("grey",             "#5D6874", "field",       "inactive numerals and spines"),
            ("headline ink",     "#F4F1EF", "supporting",  "titles, body, reverse ink"),
            ("muted ink",        "#A9B2BB", "supporting",  "derived - captions, footers"),
            ("muted ink alt",    "#727C86", "supporting",  "deprecated - fails as supporting copy"),
            ("amber",            "#B57319", "accent",      "accent as area - never type below 24px"),
            ("gold",             "#CCA348", "accent",      "accent as type; area with dark ink"),
            ("amber deep",       "#8A5613", "accent",      "derived - accent field and bands"),
            ("cat steel",        "#698EB1", "categorical", "series 3 - compute / cloud"),
            ("cat steel light",  "#8FA9C4", "categorical", "derived text-safe steel"),
            ("cat teal",         "#5FB3AA", "categorical", "series 5"),
            ("cat violet",       "#A79EDA", "categorical", "series 6 - AI / analytics"),
            ("cat sage",         "#8FB07E", "categorical", "series 7 - healthy / operational"),
        ],
        "derived": ["#A9B2BB", "#8A5613", "#8FA9C4"],
        "optional": ["#727C86", "#5D6874"],
    },
    "Yukima": {
        "folder": "yukima",
        "surfaces": ["#F1F6FA", "#C8DAE8", "#F5F3F1"],
        "accent_field": "#4B6F87",
        "tokens": [
            ("kan-no-modori 寒の戻り", "#F1F6FA", "field",       "page"),
            ("off-white",             "#F5F3F1", "field",       "lifted surface"),
            ("yukidoke 雪解け",        "#C8DAE8", "field",       "inset surface"),
            ("light blue",            "#AACEE7", "field",       "rules and borders"),
            ("sage",                  "#CAD2C4", "field",       "inactive states"),
            ("sankan-shion 三寒四温",  "#E1EDD5", "field",       "pale category tint"),
            ("headline ink",          "#22333D", "supporting",  "derived - titles, body"),
            ("muted ink",             "#3B576A", "supporting",  "derived - captions, footers"),
            ("dark blue",             "#4B6F87", "accent",      "accent as area; supporting as type"),
            ("mid blue",              "#7499BA", "accent",      "fill only"),
            ("tokiwagi 常磐木",        "#558860", "accent",      "second accent fill"),
            ("text-safe tokiwagi",    "#4D7B57", "accent",      "derived text-safe green"),
            ("moegi 萌黄",             "#86B655", "categorical", "series 2 - fill only"),
            ("olive",                 "#9A9641", "categorical", "series 3 - fill only"),
            ("ikoi 憩い",              "#7C754F", "categorical", "series 4"),
            ("ochre",                 "#BD7E1A", "categorical", "series 5"),
            ("gold",                  "#D2AD52", "categorical", "series 6 - fill only"),
            ("slate",                 "#5F7890", "categorical", "series 7"),
        ],
        "derived": ["#22333D", "#3B576A", "#4D7B57"],
        "optional": ["#E1EDD5", "#7499BA"],
    },
}


def lum(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def cr(a, b):
    l1, l2 = sorted([lum(a), lum(b)], reverse=True)
    return round((l1 + 0.05) / (l2 + 0.05), 2)


def verdict(r):
    if r >= 4.5:
        return "any size"
    if r >= 3.0:
        return "large only"
    return "**fill only**"


def matrix():
    out = ["# Contrast matrix", "",
           "Generated by [`../scripts/contrast.py`](../scripts/contrast.py) — do not hand-edit. "
           "Re-run `python3 scripts/contrast.py --write` after any token change.", "",
           "Gate: **≥ 4.5:1** below 24px, **≥ 3.0:1** at or above. "
           "`large only` means the colour is legal at display sizes and illegal as body text. "
           "`fill only` means it never carries type at any size.", ""]
    for name, p in PALETTES.items():
        out += [f"## {name}", "",
                f"Surfaces: {' · '.join('`%s`' % s for s in p['surfaces'])} · accent field `{p['accent_field']}`", ""]
        head = "| Token | Hex | Band | " + " | ".join("on `%s`" % s for s in p["surfaces"])
        head += f" | on `{p['accent_field']}` | Verdict on page |"
        out.append(head)
        out.append("|---|---|---|" + "---|" * (len(p["surfaces"]) + 2))
        for tname, hexv, band, role in p["tokens"]:
            cells = []
            for s in p["surfaces"]:
                cells.append("—" if s.upper() == hexv.upper() else f"{cr(hexv, s):.2f}")
            acc = "—" if p["accent_field"].upper() == hexv.upper() else f"{cr(hexv, p['accent_field']):.2f}"
            v = "—" if p["surfaces"][0].upper() == hexv.upper() else verdict(cr(hexv, p["surfaces"][0]))
            mark = " *(derived)*" if hexv in p["derived"] else ""
            out.append(f"| {tname}{mark} | `{hexv}` | {band} | " + " | ".join(cells) + f" | {acc} | {v} |")
        out += ["", "**Reverse text on the accent field.**", "",
                "| Foreground | on `%s` | Verdict |" % p["accent_field"], "|---|---|---|"]
        for fg in ["#FFFFFF", p["surfaces"][0], p["tokens"][6][1] if len(p["tokens"]) > 6 else "#000000"]:
            out.append(f"| `{fg}` | {cr(fg, p['accent_field']):.2f} | {verdict(cr(fg, p['accent_field']))} |")
        out.append("")
    return "\n".join(out) + "\n"


def check():
    bad = 0
    notes = []
    for name, p in PALETTES.items():
        pptx = os.path.join(TEMPLATES, p["folder"], p.get("pptx_file", p["folder"] + ".pptx"))
        if not os.path.exists(pptx):
            print(f"  MISSING {pptx}")
            bad += 1
            continue
        z = zipfile.ZipFile(pptx)
        xml = "".join(z.read(n).decode("utf-8", "ignore") for n in z.namelist()
                      if n.endswith(".xml") and ("slideLayout" in n or "slideMaster" in n or "theme1" in n))
        present = set(m.upper() for m in re.findall(r'val="([0-9A-Fa-f]{6})"', xml))
        optional = set(p.get("optional", []))
        for tname, hexv, band, role in p["tokens"]:
            h = hexv.lstrip("#").upper()
            if hexv in p["derived"]:
                continue
            if h in present:
                continue
            if band == "categorical" or hexv in optional:
                notes.append(f"  note: {name} {tname} {hexv} is a palette entry the 19 layouts do not use")
                continue
            print(f"  {name}: {band} token {tname} {hexv} is not in {p['folder']}.pptx")
            bad += 1
        theme = os.path.join(TEMPLATES, p["folder"], p.get("theme_file", "theme.json"))
        if os.path.exists(theme):
            j = json.load(open(theme))
            if j.get("name") != name:
                print(f"  {name}: theme.json name is {j.get('name')!r}")
                bad += 1
    for n in notes:
        print(n)
    print("  all required tokens present in every template" if not bad else f"  {bad} problem(s)")
    return bad


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.check:
        sys.exit(1 if check() else 0)
    m = matrix()
    if a.write:
        dst = os.path.join(SKILL, "references", "contrast-matrix.md")
        open(dst, "w").write(m)
        print("wrote", dst)
    else:
        print(m)
