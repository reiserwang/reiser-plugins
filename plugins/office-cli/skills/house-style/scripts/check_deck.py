#!/usr/bin/env python3
"""Content and craft checks for a house-style .pptx.

    python3 <house-style>/scripts/check_deck.py deck.pptx
    python3 scripts/check_deck.py deck.pptx --palette 'SKS Blue'
    python3 scripts/check_deck.py deck.pptx --template     # a template file, not a deliverable

`officecli view issues` catches overflow and stale fields. `contrast.py` catches
colour that fails the gate. Neither reads what the slide says. This does: the
title column, the agreement between a number in a title and the body under it,
the tells of a deck assembled from a template rather than written.

Exit code 1 if any FAIL. WARN never fails the run — read it and decide.

Craft rules adapted from consulting-pptx-skill (Carnot AI Inc., MIT):
https://github.com/gozen3ji/consulting-pptx-skill — a canon accumulated one line
at a time from real review feedback. The checks below are re-implemented for this
system's canvas, furniture, palettes and bilingual EN·中文 convention.
"""
import argparse
import os
import re
import sys
import unicodedata

try:
    from pptx import Presentation
    from pptx.util import Emu
except ImportError:
    sys.exit("needs python-pptx:  pip3 install python-pptx --break-system-packages")

EMU_PT = 12700.0

# ── house-style furniture, in pt on the 1440 x 810 canvas ────────────────────
TITLE_Y, TITLE_BAND = 76, 60          # title sits at y=76
RULE_Y = 142                           # title rule
FOOTER_Y = 772                         # footer / page number
CONTENT_BAND = (172.0, 760.0)          # body lives between these
TITLE_W, TITLE_PT = 1328.0, 30.0       # title box width, size
# these five carry their own furniture; the standing-furniture and fill checks skip them
EXEMPT_LAYOUTS = {"cover", "section divider", "closing", "quote", "blank"}

# ── terminology drift: both spellings in one deck is a WARN (§ one term per deck)
TERM_PAIRS = [
    ("使用者", "用戶"), ("網路", "網絡"), ("資訊安全", "資安"),
    ("軟體", "軟件"), ("硬體", "硬件"), ("影像", "視訊"),
    ("供應商", "廠商"), ("雲端", "雲"), ("風險評估", "風險盤點"),
    ("e-mail", "email"), ("web site", "website"), ("data set", "dataset"),
    ("real time", "real-time"), ("roadmap", "road map"),
]

# ── AI-smell: high-confidence only. A hit is a prompt to reread, not a verdict.
AI_SMELL_EN = [
    "leverage", "utilize", "seamless", "synergy", "robust solution",
    "cutting-edge", "state-of-the-art", "game-chang", "revolutionary",
    "in today's fast-paced", "it is worth noting", "delve into",
    "unlock the power", "at the end of the day", "holistic approach",
    "best-in-class", "moving forward, we will",
]
AI_SMELL_ZH = [
    "賦能", "抓手", "打造全方位", "全面提升", "深度融合", "生態圈",
    "數位轉型之旅", "不僅如此", "值得一提的是", "綜上所述",
    "極大地", "有效地提升", "進一步強化", "持續精進",
]

# counters that make a number in a title a promise about the body
COUNTERS = ["段階", "階段", "步驟", "面向", "支柱", "大", "項", "個", "類", "層",
            "steps", "step", "phases", "phase", "pillars", "pillar",
            "stages", "stage", "themes", "theme", "priorities", "areas", "lines"]
NUM_WORD = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
            "seven": 7, "eight": 8, "nine": 9, "ten": 10,
            "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6,
            "七": 7, "八": 8, "九": 9, "十": 10}

fails, warns = [], []
def FAIL(m): fails.append(m)
def WARN(m): warns.append(m)


def hw(text):
    """Half-width length: a CJK/fullwidth glyph counts 2, everything else 1."""
    n = 0
    for ch in text:
        n += 2 if unicodedata.east_asian_width(ch) in ("W", "F", "A") else 1
    return n


def pt(v):
    return (v or 0) / EMU_PT


def shape_text(sh):
    if not sh.has_text_frame:
        return ""
    return "\n".join(p.text for p in sh.text_frame.paragraphs).strip()


def classify(slide, sw, sh_h):
    """Return (title_shape, eyebrow_shape, footer_shapes, body_shapes)."""
    title = eyebrow = None
    footers, body = [], []
    for shp in slide.shapes:
        y, h = pt(shp.top), pt(shp.height)
        txt = shape_text(shp)
        if y >= FOOTER_Y - 12:
            footers.append(shp)
        elif abs(y - 48) < 14 and txt:
            eyebrow = shp
        elif abs(y - TITLE_Y) < 20 and txt:
            if title is None or pt(shp.width) > pt(title.width):
                title = shp
        elif y >= CONTENT_BAND[0] - 20:
            body.append(shp)
    return title, eyebrow, footers, body


def title_lines(text):
    """Lines the title will take in a 1328pt box at 30pt bold Arial."""
    per_line = TITLE_W / (TITLE_PT * 0.52)     # ~0.52em average advance, bold
    lines, cur = 1, 0
    for seg in text.split("\n"):
        cur = 0
        for ch in seg:
            w = 2 if unicodedata.east_asian_width(ch) in ("W", "F", "A") else 1
            if cur + w > per_line:
                lines += 1
                cur = 0
            cur += w
        lines += 0
    return lines, cur, per_line


def check_title(idx, text):
    if not text:
        return
    lines, last, per = title_lines(text)
    if lines > 2:
        FAIL(f"p{idx}: title needs {lines} lines in the 1328pt box — cut it, do not shrink the type")
    if lines == 2 and 0 < last <= 3:
        WARN(f"p{idx}: title's second line is {last} half-widths — an orphan; break at the sense join")
    if re.match(r"^\s*[^:：\n]{1,14}[:：]\s*\S", text):
        head = re.split(r"[:：]", text, 1)[0].strip()
        WARN(f"p{idx}: title reads as a label — '{head}: …'. Write the conclusion, not the section name")
    if re.search(r"[。.]\s*$", text):
        WARN(f"p{idx}: title ends in a full stop — titles are message lines, not sentences to close")


def title_number(text):
    m = re.search(r"(\d+|[一二三四五六七八九十]|one|two|three|four|five|six|seven|eight|nine|ten)\s*"
                  r"(" + "|".join(map(re.escape, COUNTERS)) + r")", text, re.I)
    if not m:
        return None
    tok = m.group(1)
    return int(tok) if tok.isdigit() else NUM_WORD.get(tok.lower())


def body_item_count(body_shapes):
    """Count leading enumerators across body text — 01 / 1. / ① / Step 2."""
    seen = set()
    for shp in body_shapes:
        for line in shape_text(shp).split("\n"):
            line = line.strip()
            m = (re.match(r"^(\d{1,2})[.)、．]", line)
            or re.match(r"^0(\d)\b", line)
            or re.match(r"^[Ss]tep\s*(\d)", line)
            or re.match(r"^第\s*([一二三四五六七八九十\d])\s*[階步項]", line))
            if m:
                tok = m.group(1)
                seen.add(int(tok) if tok.isdigit() else NUM_WORD.get(tok, 0))
            elif line[:1] in "①②③④⑤⑥⑦⑧⑨⑩":
                seen.add("①②③④⑤⑥⑦⑧⑨⑩".index(line[0]) + 1)
    seen.discard(0)
    return len(seen)


def signature(text):
    """Crude sentence-shape signature, for spotting a deck written from one mould."""
    t = re.sub(r"[A-Za-z0-9]+", "W", text)
    t = re.sub(r"[一-鿿]+", "C", t)
    return re.sub(r"\s+", "", t)[:24]


def check_fonts(idx, shapes):
    for shp in shapes:
        if not shp.has_text_frame:
            continue
        for para in shp.text_frame.paragraphs:
            for run in para.runs:
                if not run.text.strip():
                    continue
                latin = run.font.name
                if latin and latin != "Arial":
                    FAIL(f"p{idx}: run set in {latin!r} — this system is Arial only")
                # a run with no rPr inherits the master, which is correct. Only a run
                # that sets a latin face and omits the ea face is a real defect: 中文
                # then falls through to whatever the reader's Windows picks.
                if latin and re.search(r"[一-鿿]", run.text):
                    A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
                    rpr = run._r.find(A + "rPr")
                    ea = rpr.find(A + "ea") if rpr is not None else None
                    if ea is None or not ea.get("typeface"):
                        FAIL(f"p{idx}: 中文 run sets latin={latin!r} but no font.ea — "
                             f"Windows falls back to a serif")


def check_fill_ratio(idx, body):
    if not body:
        return
    top, bot = CONTENT_BAND
    spans = []
    for shp in body:
        y0, y1 = pt(shp.top), pt(shp.top) + pt(shp.height)
        y0, y1 = max(y0, top), min(y1, bot)
        if y1 > y0:
            spans.append((y0, y1))
    if not spans:
        return
    spans.sort()
    used, cur_s, cur_e = 0.0, *spans[0]
    for s, e in spans[1:]:
        if s > cur_e:
            used += cur_e - cur_s
            cur_s, cur_e = s, e
        else:
            cur_e = max(cur_e, e)
    used += cur_e - cur_s
    ratio = used / (bot - top)
    if ratio < 0.55:
        WARN(f"p{idx}: body fills {ratio:.0%} of the content band — under 55%, the page reads half-empty")


def check_palette(prs, path, palette_name):
    """Every srgbClr on a slide must be in the named palette. Needs contrast.py."""
    here = os.path.dirname(os.path.abspath(__file__))
    for cand in (here,                                              # installed beside contrast.py
                 os.path.join(here, "..", "..", "house-style", "scripts")):
        if os.path.exists(os.path.join(cand, "contrast.py")):
            sys.path.insert(0, os.path.abspath(cand))
            break
    try:
        import contrast
    except Exception as exc:
        WARN(f"palette check skipped — contrast.py not importable ({exc})")
        return
    p = contrast.PALETTES.get(palette_name)
    if not p:
        FAIL(f"unknown palette {palette_name!r} — known: {', '.join(contrast.PALETTES)}")
        return
    allowed = {h.lstrip('#').upper() for _, h, _, _ in p["tokens"]}
    allowed.add(p["accent_field"].lstrip('#').upper())
    allowed |= {"FFFFFF", "000000"}
    import zipfile
    z = zipfile.ZipFile(path)
    stray = {}
    for name in z.namelist():
        if not re.match(r"ppt/slides/slide\d+\.xml$", name):
            continue
        idx = int(re.search(r"slide(\d+)", name).group(1))
        for col in set(re.findall(r'srgbClr val="([0-9A-Fa-f]{6})"',
                                  z.read(name).decode("utf-8", "ignore"))):
            if col.upper() not in allowed:
                stray.setdefault(col.upper(), []).append(idx)
    for col, pages in sorted(stray.items()):
        FAIL(f"#{col} is not in {palette_name} — on slide(s) {', '.join(map(str, sorted(pages)))}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("--palette", help="check every slide colour against this contrast.py palette")
    ap.add_argument("--template", action="store_true",
                    help="a template file: {{placeholders}} are expected, not a defect")
    a = ap.parse_args()

    prs = Presentation(a.deck)
    sw, sh_h = pt(prs.slide_width), pt(prs.slide_height)
    if abs(sw - 1440) > 1 or abs(sh_h - 810) > 1:
        FAIL(f"canvas is {sw:.0f} x {sh_h:.0f}pt — this system is 1440 x 810")

    titles, all_text = [], []
    for i, slide in enumerate(prs.slides, 1):
        title_shp, eyebrow, footers, body = classify(slide, sw, sh_h)
        ttl = shape_text(title_shp) if title_shp is not None else ""
        titles.append((i, ttl))
        # (Cover / Divider / Closing titles sit elsewhere on the canvas by design)
        page_text = "\n".join(shape_text(s) for s in slide.shapes)
        all_text.append((i, page_text))

        if not a.template and "{{" in page_text:
            left = sorted(set(re.findall(r"\{\{[^}]*\}\}", page_text)))
            FAIL(f"p{i}: unreplaced placeholder(s) {' '.join(left)}")

        check_title(i, ttl)
        n = title_number(ttl)
        if n is not None:
            got = body_item_count(body)
            if got and got != n:
                FAIL(f"p{i}: title promises {n} but the body has {got} — "
                     f"the reader sees this first. Fix the number or the body")
        check_fonts(i, slide.shapes)

        layout = (slide.slide_layout.name or "").strip().lower()
        if layout not in EXEMPT_LAYOUTS:
            check_fill_ratio(i, body)
            # the eyebrow, footer and page number live on the layout in this system,
            # so a slide inherits them. Only flag when neither the slide nor its
            # layout carries them — i.e. someone built on Blank or stripped them.
            l_title, l_eyebrow, l_footers, _ = classify(slide.slide_layout, sw, sh_h)
            if body and eyebrow is None and l_eyebrow is None:
                WARN(f"p{i}: no eyebrow at y=48 on the slide or its layout "
                     f"({slide.slide_layout.name}) — standing furniture is incomplete")
            if body and not footers and not l_footers:
                WARN(f"p{i}: no footer / page number at y=772 on the slide or its layout")

    real = [t for _, t in titles if t]
    if len(real) >= 5:
        sigs = {}
        for t in real:
            sigs.setdefault(signature(t), 0)
            sigs[signature(t)] += 1
        top = max(sigs.values())
        if top / len(real) >= 0.6:
            WARN(f"{top} of {len(real)} titles share one sentence shape — "
                 f"that is a template being filled in, not a deck being written")

    joined = "\n".join(t for _, t in all_text).lower()
    for a_, b_ in TERM_PAIRS:
        if a_.lower() in joined and b_.lower() in joined:
            WARN(f"both '{a_}' and '{b_}' appear — one term per deck")
    for w in AI_SMELL_EN + AI_SMELL_ZH:
        if w.lower() in joined:
            WARN(f"'{w}' — reads as generated; say the plain thing")

    if a.palette:
        check_palette(prs, a.deck, a.palette)

    print("Title column — read it top to bottom; it should be one argument:\n")
    for i, t in titles:
        print(f"  {i:>3}  {t or '—'}")
    print()
    for w in warns:
        print("WARN ", w)
    for f in fails:
        print("FAIL ", f)
    print(f"\n{len(fails)} FAIL / {len(warns)} WARN")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
