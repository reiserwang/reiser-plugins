# Slide grid & officecli recipes

All geometry in points on a **960 × 540pt** canvas. Coordinates are measured from the shipping corporate deck — use them verbatim rather than eyeballing new positions.

## Canvas map

```
0                                                                     960
├─ 20.3 ─────────────────────────────────────────────────────────────┤
│  [wordmark 432.6×59.7 @ 20.3,26.4]      [tagline 24pt @ 467.3,26.4] │  y 26.4–86.1
│                                                                      │
│  eyebrow 14pt bold #00A3E6 @ 42.5,123.0  w=871.2                     │  y 123.0
│                                                                      │
│  ┌ content band: x 37.4 → 918 (w 880.6), y 156.8 → 400 ┐             │
│  │                                                      │            │
│  └──────────────────────────────────────────────────────┘            │
│  [callout band 880.6×51.8 @ 37.4,421.0 fill #E6F2FC]                 │  y 421.0
│  footer 9pt @ 43.2,509.8            page # 9pt @ 874.8,509.8         │  y 509.8
└──────────────────────────────────────────────────────────────────────┘
```

## Four-card row (the signature house layout)

Card `n` (0-indexed), width 208.8, gutter 13.7:

`card_x(n) = 37.4 + n × 222.5` → **37.4, 259.9, 482.4, 704.9**

Within each card (`cx` = card x, `cy` = 156.8):

| Part | x | y | w | h | Spec |
|---|---|---|---|---|---|
| Card panel | `cx` | 156.8 | 208.8 | 241.2 | `roundRect`, fill `#F0F6FC`, line `#E6F2FC` |
| Icon badge | `cx + 64.8` | 178.4 | 79.2 | 79.2 | `ellipse`, fill `#0B318F` |
| Icon glyph | `cx + 83.8` | 197.4 | 41.2 | 41.2 | white picture, centered in badge |
| Title | `cx + 10.8` | 268.4 | 187.2 | 43.2 | 16.5pt bold `#0B318F`, centered |
| Body | `cx + 18.0` | 315.2 | 172.8 | 72.0 | 12.5pt `#5A6676`, centered |

### Known overflow points — fix these, don't inherit them

The shipping deck's boxes are sized for single-line copy. `view issues` flags them the moment a string wraps. Apply these corrections in new work:

| Element | Shipping height | Use instead | Trigger |
|---|---|---|---|
| Card title | 43.2 | **54.0**, y stays 268.4 | any title wrapping to 2 lines (e.g. "Disaster Early Warning") |
| Tagline | 59.7 | **72.0** | tagline wrapping to 2 lines at 24pt |
| Card body | 72.0 | **86.4** | body over ~14 words at 12.5pt |

Rule of thumb: a text box needs `lines × size × 1.45` points of height. `view issues` reports the exact shortfall and a `suggest.height` — take it.

**Three-card variant:** width 284.3, gutter 13.7 → `card_x(n) = 37.4 + n × 298.0`.
**Two-card variant:** width 433.5, gutter 13.6 → `card_x(n) = 37.4 + n × 447.1`.
Keep the same internal y-offsets; recenter the badge and text horizontally.

## Batch recipe — full content slide

Run `officecli create deck.pptx` first, or `add` a slide to an existing file. Note the heredoc is unquoted so `$SLIDE` expands; escape literal `$` in copy as `\$`.

```bash
SLIDE='/slide[1]'
cat <<EOF | officecli batch deck.pptx
[
 {"command":"set","path":"$SLIDE","props":{"background":"FFFFFF"}},

 {"command":"add","parent":"$SLIDE","type":"shape","props":{
   "text":"next-generation resilient security, on a smart cloud",
   "x":"467.3pt","y":"26.4pt","width":"472.4pt","height":"59.7pt",
   "font":"Arial","size":"24","color":"1A2230","fill":"none","valign":"middle"}},

 {"command":"add","parent":"$SLIDE","type":"shape","props":{
   "text":"<English tagline>  ·  <中文標語>",
   "x":"42.5pt","y":"123.0pt","width":"871.2pt","height":"25.2pt",
   "font":"Arial","size":"14","bold":"true","color":"00A3E6","fill":"none","align":"left"}},

 {"command":"add","parent":"$SLIDE","type":"shape","props":{
   "x":"37.4pt","y":"156.8pt","width":"208.8pt","height":"241.2pt",
   "geometry":"roundRect","fill":"F0F6FC","line.color":"E6F2FC"}},
 {"command":"add","parent":"$SLIDE","type":"shape","props":{
   "x":"102.2pt","y":"178.4pt","width":"79.2pt","height":"79.2pt",
   "geometry":"ellipse","fill":"0B318F","line":"none"}},
 {"command":"add","parent":"$SLIDE","type":"shape","props":{
   "text":"Remote Monitoring",
   "x":"48.2pt","y":"268.4pt","width":"187.2pt","height":"43.2pt",
   "font":"Arial","size":"16.5","bold":"true","color":"0B318F","fill":"none","align":"center","valign":"middle"}},
 {"command":"add","parent":"$SLIDE","type":"shape","props":{
   "text":"24/7 cloud-connected live view; video-verified before dispatch.",
   "x":"55.4pt","y":"315.2pt","width":"172.8pt","height":"72.0pt",
   "font":"Arial","size":"12.5","color":"5A6676","fill":"none","align":"center","wrap":"true"}},

 {"command":"add","parent":"$SLIDE","type":"shape","props":{
   "x":"37.4pt","y":"421.0pt","width":"880.6pt","height":"51.8pt",
   "geometry":"roundRect","fill":"E6F2FC","line":"none"}},
 {"command":"add","parent":"$SLIDE","type":"shape","props":{
   "text":"<one-line proof point  ·  separated by middots>",
   "x":"37.4pt","y":"421.0pt","width":"880.6pt","height":"51.8pt",
   "font":"Arial","size":"14.5","color":"1A2230","fill":"none","align":"center","valign":"middle"}},

 {"command":"add","parent":"$SLIDE","type":"shape","props":{
   "text":"<Company>   |   <deck title>",
   "x":"43.2pt","y":"509.8pt","width":"720.0pt","height":"21.6pt",
   "font":"Arial","size":"9","color":"5A6676","fill":"none","align":"left","valign":"middle"}},
 {"command":"add","parent":"$SLIDE","type":"shape","props":{
   "text":"3",
   "x":"874.8pt","y":"509.8pt","width":"43.2pt","height":"21.6pt",
   "font":"Arial","size":"9","color":"5A6676","fill":"none","align":"right","valign":"middle"}}
]
EOF
```

Repeat the three card shapes for cards 2–4 at `cx = 259.9, 482.4, 704.9`, adding the same offsets.

This recipe is verified end-to-end against officecli 1.0.144 — 23/23 batch items succeed and the render matches the shipping deck. What it does **not** produce is the wordmark picture and the white icon glyphs inside the badges; those are images, covered under *Reusing the wordmark* below.

Confirm property names against `officecli help pptx shape` before trusting `line.color`, `valign`, or `align` — these are the aliases most likely to have drifted.

## Reusing the wordmark

Do not redraw the corporate wordmark. Extract it from an existing deck and re-insert:

```bash
officecli query corporate_master_deck.pptx 'picture' --json    # find the wordmark's path
officecli get  corporate_master_deck.pptx '/slide[3]/picture[@id=28]' --json
```

Simplest reliable route for a new deck: copy an existing deck as the starting file, `remove` the body shapes from a slide, and rebuild the content — the wordmark, master, and theme come along intact.

```bash
cp corporate_master_deck.pptx new_deck.pptx
officecli remove new_deck.pptx '/slide[4]'   # trim to the slides you want as a base
```

## Other recurring layouts

**Section divider** — full-bleed `#0B318F` rectangle `0,0,960,540`; section number 60pt `#00A3E6` at `x=43.2,y=200`; title 32pt bold white at `x=43.2,y=270`; no footer.

**Two-column text + visual** — text column `x=37.4,w=420`, visual `x=482.4,w=435.6`, both `y=156.8,h=241.2`. Column body 12.5pt `#5A6676`.

**Layer stack (reference-architecture style)** — full-width bands at `x=37.4,w=880.6`, height 54, stacked from `y=140` with 10.8 gaps; band fill alternates `#F0F6FC` / `#E6F2FC`; band label 11.5pt bold `#0B318F` at left; layer chips inside at 9.5pt. Layer accent colors from the categorical ramp: cloud `#2E5BF0`, AI `#7C4DB8`, operational `#2FA84F`.

**Roadmap / timeline** — horizontal rule `#C3D6EE` at `y=300`, phase markers as 21.6pt `ellipse` on the rule; shipped phases `#0B318F`, future phases outline-only with `#AEC6E8`; labels 11.5pt above, dates 9pt `#5A6676` below.
