#!/usr/bin/env python3
"""Prose tells shared by the house-style checkers — terminology drift and AI register.

One term per document, and the words that read as generated rather than written.
Used by check_deck.py (slides) and check_doc.py (Word). Workbooks skip it: a
spreadsheet has no prose to speak of.
"""

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


def scan(texts, unit="deck"):
    """Yield a warning string for each terminology clash and AI-register hit."""
    joined = "\n".join(t for t in texts if t).lower()
    for a, b in TERM_PAIRS:
        if a.lower() in joined and b.lower() in joined:
            yield f"both '{a}' and '{b}' appear — one term per {unit}"
    for w in AI_SMELL_EN + AI_SMELL_ZH:
        if w.lower() in joined:
            yield f"'{w}' — reads as generated; say the plain thing"
