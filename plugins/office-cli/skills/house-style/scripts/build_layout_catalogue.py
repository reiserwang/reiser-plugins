# -*- coding: utf-8 -*-
"""Build a layout-catalogue .pptx per house-style template.

    python3 scripts/build_layout_catalogue.py

One slide per named layout, built on that layout so it inherits the real master,
theme and standing furniture. Every placeholder is labelled with its index, name
and geometry; nothing is filled with sample copy, so the file answers "what does
this layout give me and where" without pretending to be a deck.

Reads  templates/<folder>/<file>.pptx
Writes references/layout-catalogue/<file>-layouts.pptx

Re-run after any change to a template's layouts, or the catalogue goes stale.
"""
import os, sys
from pptx import Presentation
from pptx.util import Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

MUTED = {
    "ana-blue":      "5A6676",
    "yukima":        "3B576A",
    "reiser-warm":   "5C5650",
    "sks-dark":      "A9B2BB",
    "sks-blue":      "444E60",
    "sks-blue-dark": "A8B4CE",
}
REVERSE = "FFFFFF"                       # ink on the accent-field layouts
ACCENT_FIELD_LAYOUTS = {"cover", "section divider", "closing"}
EMU_PT = 12700.0

def pt_(v): return round((v or 0) / EMU_PT)

def set_label(ph, text, hexcol, size=11):
    tf = ph.text_frame
    tf.clear()
    para = tf.paragraphs[0]
    para.text = ""
    run = para.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = False
    run.font.name = "Arial"
    run.font.color.rgb = RGBColor.from_string(hexcol)
    # 中文 face, so a label containing 中文 never falls back to a serif on Windows
    rPr = run._r.get_or_add_rPr()
    ns = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    ea = rPr.makeelement(ns + "ea", {"typeface": "微軟正黑體"})
    rPr.append(ea)

def set_title(ph, text):
    tf = ph.text_frame
    tf.clear()
    para = tf.paragraphs[0]
    run = para.add_run()
    run.text = text
    # deliberately no font.name: the layout already sets Arial + 微軟正黑體, and
    # setting the latin face alone strips the ea face from a title carrying 中文


# ── the palette slide ────────────────────────────────────────────────────────
PALETTE_NAME = {
    "ana-blue": "ANA Blue", "yukima": "Yukima", "reiser-warm": "Reiser Warm",
    "sks-dark": "SKS Dark", "sks-blue": "SKS Blue", "sks-blue-dark": "SKS Blue Dark",
}
BAND_TITLE = {"field": "60%  ·  THE FIELD",
              "supporting": "30%  ·  THE SUPPORTING LAYER",
              "accent": "10%  ·  THE ACCENT"}


def _lum(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def _rgb(h):
    h = h.lstrip("#")
    return "RGB  " + "  ".join(str(int(h[i:i + 2], 16)) for i in (0, 2, 4))


def _cr(a, b):
    l1, l2 = sorted([_lum(a), _lum(b)], reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def _box(slide, x, y, w, h, fill=None, line=None):
    from pptx.enum.shapes import MSO_SHAPE
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Emu(int(x * EMU_PT)), Emu(int(y * EMU_PT)),
                                Emu(int(w * EMU_PT)), Emu(int(h * EMU_PT)))
    sh.shadow.inherit = False
    if fill:
        sh.fill.solid(); sh.fill.fore_color.rgb = RGBColor.from_string(fill.lstrip("#"))
    else:
        sh.fill.background()
    if line:
        sh.line.color.rgb = RGBColor.from_string(line.lstrip("#")); sh.line.width = Pt(0.75)
    else:
        sh.line.fill.background()
    sh.text_frame.word_wrap = True
    return sh


def _text(slide, x, y, w, h, text, size, colour, bold=False, space=0):
    box = slide.shapes.add_textbox(Emu(int(x * EMU_PT)), Emu(int(y * EMU_PT)),
                                   Emu(int(w * EMU_PT)), Emu(int(h * EMU_PT)))
    tf = box.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    para = tf.paragraphs[0]; para.alignment = PP_ALIGN.LEFT
    run = para.add_run(); run.text = text
    run.font.size = Pt(size); run.font.bold = bold; run.font.name = "Arial"
    run.font.color.rgb = RGBColor.from_string(colour.lstrip("#"))
    rPr = run._r.get_or_add_rPr()
    ns = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    rPr.append(rPr.makeelement(ns + "ea", {"typeface": "微軟正黑體"}))
    if space:
        rPr.set("spc", str(int(space * 100)))
    return box


def add_palette_slides(prs, stem):
    """Two reference pages, drawn from contrast.py so they can never drift:
    the 60-30-10 bands with HEX + RGB, then the chart ramp and the type stack."""
    import contrast
    p = contrast.PALETTES[PALETTE_NAME[stem]]
    field = p["surfaces"][0]
    toks = p["tokens"]
    supporting = [t for t in toks if t[2] == "supporting"]
    ink = supporting[0][1] if supporting else "#000000"
    muted = supporting[1][1] if len(supporting) > 1 else ink
    accent_t = [t for t in toks if t[2] == "accent"]
    acc_text = accent_t[0][1] if accent_t else ink
    if _lum(field) < 0.2 and len(accent_t) > 1:      # dark field: the accent as type is the light step
        acc_text = max(accent_t, key=lambda t: _lum(t[1]))[1]
    rule = next((t[1] for t in toks if "rule" in t[0].lower()), muted)
    blank = {l.name: l for l in prs.slide_masters[0].slide_layouts}["Blank"]

    # ── page 1: the bands ────────────────────────────────────────────────────
    s1 = prs.slides.add_slide(blank)
    _text(s1, 56, 48, 1328, 26, "色彩 · PALETTE", 20, acc_text, bold=True, space=0.6)
    _text(s1, 56, 76, 1328, 44, "Palette — 60 / 30 / 10 by area", 30, ink, bold=True)

    y = 178
    for band in ("field", "supporting", "accent"):
        row = [t for t in toks if t[2] == band]
        if not row:
            continue
        _text(s1, 56, y, 700, 18, BAND_TITLE[band], 12, muted, bold=True, space=1.0)
        n, gap = len(row), 14
        w = (1328 - gap * (n - 1)) / n
        for i, (name, hexv, _b, _role) in enumerate(row):
            x = 56 + i * (w + gap)
            same = hexv.upper() == field.upper()
            # outline every field swatch: several sit within 1.1:1 of the page and
            # would otherwise have no edge at all
            edge = rule if band == "field" else None
            _box(s1, x, y + 26, w, 60, fill=hexv, line=edge)
            _text(s1, x, y + 92, w, 16, name, 12, ink, bold=True)
            _text(s1, x, y + 110, w, 14, hexv.upper(), 10.5, muted)
            _text(s1, x, y + 126, w, 14, _rgb(hexv), 10.5, muted)
            _text(s1, x, y + 142, w, 14, "—" if same else f"{_cr(hexv, field):.2f} : 1", 10.5, muted)
        y += 176

    # ── page 2: the ramp and the type stack ──────────────────────────────────
    s2 = prs.slides.add_slide(blank)
    _text(s2, 56, 48, 1328, 26, "字體 · TYPE", 20, acc_text, bold=True, space=0.6)
    _text(s2, 56, 76, 1328, 44, "Chart series, and type that survives the platform", 30, ink, bold=True)

    series = [t for t in toks if t[2] == "categorical"] or accent_t
    y = 178
    _text(s2, 56, y, 700, 18, "CHART SERIES, IN ORDER", 12, muted, bold=True, space=1.0)
    n, gap = len(series), 12
    w = (1328 - gap * (n - 1)) / n
    for i, (name, hexv, _b, _role) in enumerate(series):
        x = 56 + i * (w + gap)
        _box(s2, x, y + 26, w, 44, fill=hexv)
        _text(s2, x, y + 76, w, 14, name, 11, ink, bold=True)
        _text(s2, x, y + 92, w, 14, hexv.upper(), 10, muted)
        _text(s2, x, y + 108, w, 14, _rgb(hexv), 10, muted)

    y = 350
    _text(s2, 56, y, 700, 18, "TYPE — WINDOWS · MACOS · WEB", 12, muted, bold=True, space=1.0)
    rows = [
        ("Latin", "Arial", "Arial", "Arial",
         'Arial, Helvetica, "Liberation Sans", sans-serif'),
        ("中文", "微軟正黑體", "PingFang TC *", "—",
         '"PingFang TC", "Microsoft JhengHei", "Noto Sans TC", sans-serif'),
        ("Mono", "Consolas", "Menlo", "—",
         'Consolas, Menlo, "SF Mono", ui-monospace, monospace'),
    ]
    hdr = ["", "Windows", "macOS", "Web font file", "CSS stack"]
    cols = [56, 176, 316, 456, 616]
    widths = [110, 130, 130, 150, 768]
    _box(s2, 56, y + 26, 1328, 1.5, fill=acc_text)
    for c, h in zip(cols, hdr):
        _text(s2, c, y + 34, 200, 16, h, 11.5, acc_text, bold=True)
    yy = y + 58
    for label, win, mac, webf, css in rows:
        _box(s2, 56, yy - 6, 1328, 0.75, fill=rule)
        for c, wdt, txt, bold in zip(cols, widths, [label, win, mac, webf, css],
                                     [True, False, False, False, False]):
            _text(s2, c, yy, wdt, 18, txt, 12, ink if bold else muted, bold=bold)
        yy += 34

    _text(s2, 56, yy + 14, 1328, 60,
          "*  微軟正黑體 ships with Windows only. macOS substitutes — PingFang TC is the close "
          "equivalent, Heiti TC on older systems — and no browser has it, so the web stack leads with "
          "PingFang TC and falls back to Noto Sans TC. A .pptx run carries exactly one latin face and "
          "one east-asian face, with no fallback list: this deck sets latin=Arial, ea=微軟正黑體, and "
          "PowerPoint on macOS does the substitution itself.", 11.5, muted)
    return s1, s2



def build(stem):
    prs = Presentation(os.path.join(TEMPLATES, FOLDER[stem], stem + ".pptx"))
    master = prs.slide_masters[0]
    muted = MUTED[stem]

    # drop the blank starter slide — the catalogue replaces it
    xml_slides = prs.slides._sldIdLst
    for sld in list(xml_slides):
        prs.part.drop_rel(sld.rId)      # drop the part too, not just the id
        xml_slides.remove(sld)

    for n, lay in enumerate(master.slide_layouts, 1):
        slide = prs.slides.add_slide(lay)
        name = (lay.name or "").strip()
        low = name.lower()
        ink = REVERSE if low in ACCENT_FIELD_LAYOUTS else muted

        saw_title = False
        for ph in list(slide.placeholders):
            pf = ph.placeholder_format
            if pf.type is not None and "SLIDE_NUMBER" in str(pf.type):
                continue
            if not ph.has_text_frame:
                continue
            x, y = pt_(ph.left), pt_(ph.top)
            w, h = pt_(ph.width), pt_(ph.height)
            # SUBTITLE also stringifies with "TITLE" in it — match the name exactly
            tname = str(pf.type).split(" ")[0]
            is_title = tname in ("TITLE", "CENTER_TITLE")
            if is_title:
                saw_title = True
                if n == 1:
                    set_title(ph, TITLE_TEXT[stem])
                else:
                    set_title(ph, name)
            else:
                if n == 1:
                    set_label(ph, SUB_TEXT[stem], ink, 14)
                else:
                    set_label(ph, f"[{pf.idx}] {ph.name} · {x},{y} · {w}×{h}pt", ink, 11)

        # Quote and Blank carry no title placeholder — name them anyway, or the
        # catalogue ends up with an anonymous page in it
        if not saw_title:
            box = slide.shapes.add_textbox(Emu(int(56 * EMU_PT)), Emu(int(76 * EMU_PT)),
                                           Emu(int(1328 * EMU_PT)), Emu(int(44 * EMU_PT)))
            para0 = box.text_frame.paragraphs[0]
            para0.alignment = PP_ALIGN.LEFT
            r = para0.add_run()
            r.text = f"{name}  — no title placeholder; free canvas"
            r.font.size = Pt(30); r.font.bold = True; r.font.name = "Arial"
            r.font.color.rgb = RGBColor.from_string(muted)

    add_palette_slides(prs, stem)         # 60-30-10 bands, then the ramp and the type stack

    out = os.path.join(OUT, stem + "-layouts.pptx")
    prs.save(out)
    print(f"{os.path.basename(out)}: {len(prs.slides._sldIdLst)} slides")

TITLE_TEXT = {
    "ana-blue":      "ANA Blue",
    "yukima":        "Yukima 雪間",
    "reiser-warm":   "Reiser Warm",
    "sks-dark":      "SKS Dark",
    "sks-blue":      "SKS Blue",
    "sks-blue-dark": "SKS Blue Dark",
}
SUB_TEXT = {k: "Layout catalogue · 19 named layouts · 1440 × 810 pt"
            for k in TITLE_TEXT}

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
sys.path.insert(0, HERE)   # contrast.py lives beside this script
TEMPLATES = os.path.join(SKILL, "templates")
OUT = os.path.join(SKILL, "references", "layout-catalogue")

# stem -> template folder (sks-blue ships two files from one folder)
FOLDER = {
    "ana-blue": "ana-blue", "yukima": "yukima", "reiser-warm": "reiser-warm",
    "sks-dark": "sks-dark", "sks-blue": "sks-blue", "sks-blue-dark": "sks-blue",
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for stem in MUTED:
        build(stem)
