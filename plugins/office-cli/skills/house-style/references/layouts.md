# Layout inventory

Nineteen layouts, on **one master per template**, in this order in both templates. Coordinates are in points on the 1440 × 810 pt canvas and are **measured from the shipping template file** — reported to 2 decimal places, which is the file's own precision.

Colours below are the **ANA Blue** values. The Reiser Warm master carries the same geometry with these substitutions:

| Role | ANA Blue | Reiser Warm |
|---|---|---|
| Field | `#FFFFFF` | `#F5F1ED` |
| Panel tint | `#F0F6FC` | `#E8E4DF` |
| Callout / lifted tint | `#E6F2FC` | `#F5F3F1` |
| Rule | `#C3D6EE` | `#D4D0C9` |
| Accent (fills, rules, bands) | `#0B318F` | `#CC785C` |
| Accent as text (eyebrow, big number, Quote glyph) | `#0B318F` | `#9D5C47` |
| Ink | `#1A2230` | `#1F1E1D` |
| Muted ink | `#5A6676` | `#5C5650` |
| Text on the **accent** field or fill | `#FFFFFF` | `#1F1E1D` — coral takes **dark** text |
| Text on the **muted-ink** band (Two-Column "Before") | `#FFFFFF` | `#F5F1ED` — charcoal on `#5C5650` is only 2.30:1 |
| Category spines | `#0B318F` `#00A3E6` `#2E5BF0` `#7C4DB8` | `#CC785C` `#5C7B9C` `#6B8E5C` `#C28E3D` |

Those last two rows are the substitutions that are **not** a straight swap. Getting them wrong produces the only contrast failures either template can generate.

`kind` is the PowerPoint placeholder type; `idx` is the index you address it by; `—` means the shape is static furniture drawn on the layout, inherited rather than editable per slide, so do not try to retitle it. `sldNum` owns `idx=12` by convention throughout, and no other placeholder collides with it.

Four layouts override the slide background — Cover, Section Divider and Closing sit on the accent field, and Quote sits on the panel tint. Each is flagged in place below.

## Layouts without standing furniture

Two layouts deliberately ship without the eyebrow / title / title-rule trio:

- **Quote** — panel-tint field, a 130pt opening glyph, the quotation and its attribution. Footer and page number only.
- **Blank** — title rule, footer and page number only; nothing else.

Cover, Section Divider and Closing carry their own furniture instead of the standard set. Every other layout carries all five standing elements.

## Choosing a layout

| The page argues… | Layout |
|---|---|
| the title of the deliverable | Cover |
| what we will cover | Agenda |
| a new act begins | Section Divider |
| a single prose or bullet argument | Title and Content |
| this state versus that state | Two-Column Compare |
| one number is the whole point | Big Number |
| four numbers frame the period | KPI Dashboard |
| the chart, plus the one sentence it proves | Chart with Takeaway |
| the chart, plus a column of reading | Chart + Commentary |
| the rows matter individually | Data Table |
| how the parts connect | Diagram Frame |
| look at this artefact | Picture with Caption |
| where the exposure sits | Risk Matrix |
| what happened and what we did | Incident Detail |
| where each workstream stands | Project Status |
| who owes what by when | Action Items |
| someone else said it better | Quote |
| none of the above | Blank |
| here is the decision I need | Closing |


### 1. Cover

Background override: **`#0B318F`** (warm: `#CC785C`) — this layout is not on the default field.

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `tx101` | — |  | 56 | 300 | 1328 | 30 | “{{DECK_TITLE}}　\|　{{DECK_TITLE_EN}}” 20pt bold `#FFFFFF` |
| `ctrTitle102` | center_title | 0 | 56 | 340 | 1328 | 130 | 40pt bold `#FFFFFF` l |
| `subTitle103` | subtitle | 1 | 56 | 486 | 823.36 | 60 | 21pt `#FFFFFF` l |
| `sh104` | — |  | 56 | 580 | 120 | 3 | fill `#FFFFFF` |
| `tx105` | — |  | 56 | 610 | 1328 | 26 | “{{ORG}} · {{UNIT}}” 18pt `#FFFFFF` |
| `tx106` | — |  | 56 | 772 | 1328 | 22 | “{{CLASSIFICATION}}” 13pt bold `#FFFFFF` |

### 2. Agenda

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `tx101` | — |  | 56 | 48 | 1328 | 24 | “AGENDA · 議程” 20pt bold `#0B318F` |
| `title102` | title | 0 | 56 | 76 | 1328 | 56 | 30pt bold `#1A2230` l |
| `sh103` | — |  | 56 | 142 | 1328 | 1.5 | fill `#0B318F` |
| `tx104` | — |  | 56 | 772 | 929.6 | 22 | “{{ORG}}  \|  {{DECK_TITLE}}” 13pt `#5A6676` |
| `sldNum105` | slide_number | 12 | 1324 | 772 | 60 | 22 | 13pt `#5A6676` r |
| `sh106` | — |  | 56 | 172 | 431.87 | 130 | fill `#F0F6FC` |
| `tx107` | — |  | 72.2 | 188.2 | 40 | 34 | “01” 24pt bold `#0B318F` |
| `body108` | body | 10 | 72.2 | 230 | 399.47 | 54 | 18pt `#5A6676` l |
| `sh109` | — |  | 504.07 | 172 | 431.87 | 130 | fill `#F0F6FC` |
| `tx110` | — |  | 520.27 | 188.2 | 40 | 34 | “02” 24pt bold `#0B318F` |
| `body111` | body | 11 | 520.27 | 230 | 399.47 | 54 | 18pt `#5A6676` l |
| `sh112` | — |  | 952.13 | 172 | 431.87 | 130 | fill `#F0F6FC` |
| `tx113` | — |  | 968.33 | 188.2 | 40 | 34 | “03” 24pt bold `#0B318F` |
| `body114` | body | 41 | 968.33 | 230 | 399.47 | 54 | 18pt `#5A6676` l |

### 3. Section Divider

Background override: **`#0B318F`** (warm: `#CC785C`) — this layout is not on the default field.

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `body101` | body | 2 | 56 | 300 | 120 | 60 | 34pt bold `#FFFFFF` l |
| `title102` | title | 0 | 56 | 370 | 1062.4 | 80 | 34pt bold `#FFFFFF` l |
| `body103` | body | 1 | 56 | 470 | 796.8 | 50 | 18pt `#FFFFFF` l |
| `sh104` | — |  | 56 | 452 | 100 | 3 | fill `#FFFFFF` |

### 4. Title and Content

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `tx101` | — |  | 56 | 48 | 1328 | 24 | “EYEBROW · 分類” 20pt bold `#0B318F` |
| `title102` | title | 0 | 56 | 76 | 1328 | 56 | 30pt bold `#1A2230` l |
| `sh103` | — |  | 56 | 142 | 1328 | 1.5 | fill `#0B318F` |
| `tx104` | — |  | 56 | 772 | 929.6 | 22 | “{{ORG}}  \|  {{DECK_TITLE}}” 13pt `#5A6676` |
| `sldNum105` | slide_number | 12 | 1324 | 772 | 60 | 22 | 13pt `#5A6676` r |
| `body106` | body | 1 | 56 | 172 | 1328 | 520 | 18pt `#1A2230` l |

### 5. Two-Column Compare

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `tx101` | — |  | 56 | 48 | 1328 | 24 | “比較 · COMPARE” 20pt bold `#0B318F` |
| `title102` | title | 0 | 56 | 76 | 1328 | 56 | 30pt bold `#1A2230` l |
| `sh103` | — |  | 56 | 142 | 1328 | 1.5 | fill `#0B318F` |
| `tx104` | — |  | 56 | 772 | 929.6 | 22 | “{{ORG}}  \|  {{DECK_TITLE}}” 13pt `#5A6676` |
| `sldNum105` | slide_number | 12 | 1324 | 772 | 60 | 22 | 13pt `#5A6676` r |
| `sh106` | — |  | 56 | 172 | 655.9 | 520 | fill `#F0F6FC` |
| `sh107` | — |  | 56 | 172 | 655.9 | 40 | fill `#5A6676` |
| `tx108` | — |  | 72.2 | 181 | 623.5 | 26 | “現況　Before” 18pt bold `#FFFFFF` |
| `body109` | body | 10 | 72.2 | 230 | 623.5 | 448 | 18pt `#5A6676` l |
| `sh110` | — |  | 728.1 | 172 | 655.9 | 520 | fill `#E6F2FC` |
| `sh111` | — |  | 728.1 | 172 | 655.9 | 40 | fill `#0B318F` |
| `tx112` | — |  | 744.3 | 181 | 623.5 | 26 | “目標　After” 18pt bold `#FFFFFF` |
| `body113` | body | 11 | 744.3 | 230 | 623.5 | 448 | 18pt `#5A6676` l |

### 6. Big Number

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `tx101` | — |  | 56 | 48 | 1328 | 24 | “重點 · HEADLINE” 20pt bold `#0B318F` |
| `title102` | title | 0 | 56 | 76 | 1328 | 56 | 30pt bold `#1A2230` l |
| `sh103` | — |  | 56 | 142 | 1328 | 1.5 | fill `#0B318F` |
| `tx104` | — |  | 56 | 772 | 929.6 | 22 | “{{ORG}}  \|  {{DECK_TITLE}}” 13pt `#5A6676` |
| `sldNum105` | slide_number | 12 | 1324 | 772 | 60 | 22 | 13pt `#5A6676` r |
| `body106` | body | 10 | 56 | 212 | 610.88 | 200 | 96pt bold `#0B318F` ctr |
| `body107` | body | 41 | 56 | 422 | 610.88 | 30 | 18pt `#5A6676` ctr |
| `sh108` | — |  | 720 | 212 | 1.5 | 260 | fill `#C3D6EE` |
| `body109` | body | 11 | 773.12 | 212 | 610.88 | 280 | 21pt `#1A2230` l |

### 7. KPI Dashboard

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `tx101` | — |  | 56 | 48 | 1328 | 24 | “指標 · KPI” 20pt bold `#0B318F` |
| `title102` | title | 0 | 56 | 76 | 1328 | 56 | 30pt bold `#1A2230` l |
| `sh103` | — |  | 56 | 142 | 1328 | 1.5 | fill `#0B318F` |
| `tx104` | — |  | 56 | 772 | 929.6 | 22 | “{{ORG}}  \|  {{DECK_TITLE}}” 13pt `#5A6676` |
| `sldNum105` | slide_number | 12 | 1324 | 772 | 60 | 22 | 13pt `#5A6676` r |
| `sh106` | — |  | 56 | 172 | 319.85 | 200 | fill `#F0F6FC` |
| `body107` | body | 10 | 72.2 | 194 | 287.45 | 74 | 54pt bold `#0B318F` ctr |
| `body108` | body | 14 | 72.2 | 280 | 287.45 | 26 | 18pt bold `#1A2230` ctr |
| `body109` | body | 18 | 72.2 | 312 | 287.45 | 44 | 13pt `#5A6676` ctr |
| `sh110` | — |  | 392.05 | 172 | 319.85 | 200 | fill `#F0F6FC` |
| `body111` | body | 11 | 408.25 | 194 | 287.45 | 74 | 54pt bold `#0B318F` ctr |
| `body112` | body | 15 | 408.25 | 280 | 287.45 | 26 | 18pt bold `#1A2230` ctr |
| `body113` | body | 19 | 408.25 | 312 | 287.45 | 44 | 13pt `#5A6676` ctr |
| `sh114` | — |  | 728.1 | 172 | 319.85 | 200 | fill `#F0F6FC` |
| `body115` | body | 41 | 744.3 | 194 | 287.45 | 74 | 54pt bold `#0B318F` ctr |
| `body116` | body | 16 | 744.3 | 280 | 287.45 | 26 | 18pt bold `#1A2230` ctr |
| `body117` | body | 20 | 744.3 | 312 | 287.45 | 44 | 13pt `#5A6676` ctr |
| `sh118` | — |  | 1064.15 | 172 | 319.85 | 200 | fill `#F0F6FC` |
| `body119` | body | 13 | 1080.35 | 194 | 287.45 | 74 | 54pt bold `#0B318F` ctr |
| `body120` | body | 17 | 1080.35 | 280 | 287.45 | 26 | 18pt bold `#1A2230` ctr |
| `body121` | body | 21 | 1080.35 | 312 | 287.45 | 44 | 13pt `#5A6676` ctr |
| `sh122` | — |  | 56 | 706 | 1328 | 56 | fill `#E6F2FC` |
| `body123` | body | 30 | 72.2 | 720 | 1295.6 | 30 | 21pt `#1A2230` l |

### 8. Chart with Takeaway

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `tx101` | — |  | 56 | 48 | 1328 | 24 | “數據 · DATA” 20pt bold `#0B318F` |
| `title102` | title | 0 | 56 | 76 | 1328 | 56 | 30pt bold `#1A2230` l |
| `sh103` | — |  | 56 | 142 | 1328 | 1.5 | fill `#0B318F` |
| `tx104` | — |  | 56 | 772 | 929.6 | 22 | “{{ORG}}  \|  {{DECK_TITLE}}” 13pt `#5A6676` |
| `sldNum105` | slide_number | 12 | 1324 | 772 | 60 | 22 | 13pt `#5A6676` r |
| `chart106` | chart | 10 | 56 | 172 | 1328 | 424 | 18pt `#5A6676` ctr |
| `sh107` | — |  | 56 | 606 | 1328 | 48 | fill `#E6F2FC` |
| `body108` | body | 11 | 72.2 | 618 | 1295.6 | 30 | 21pt `#1A2230` l |
| `tx109` | — |  | 56 | 668 | 1328 | 22 | “Source:” 13pt `#5A6676` |

### 9. Chart + Commentary

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `tx101` | — |  | 56 | 48 | 1328 | 24 | “數據 · DATA” 20pt bold `#0B318F` |
| `title102` | title | 0 | 56 | 76 | 1328 | 56 | 30pt bold `#1A2230` l |
| `sh103` | — |  | 56 | 142 | 1328 | 1.5 | fill `#0B318F` |
| `tx104` | — |  | 56 | 772 | 929.6 | 22 | “{{ORG}}  \|  {{DECK_TITLE}}” 13pt `#5A6676` |
| `sldNum105` | slide_number | 12 | 1324 | 772 | 60 | 22 | 13pt `#5A6676` r |
| `chart106` | chart | 10 | 56 | 172 | 823.36 | 490 | 18pt `#5A6676` ctr |
| `sh107` | — |  | 895.56 | 172 | 488.44 | 490 | fill `#F0F6FC` |
| `tx108` | — |  | 911.76 | 188 | 456.04 | 26 | “解讀　Reading” 18pt bold `#0B318F` |
| `body109` | body | 11 | 911.76 | 224 | 456.04 | 420 | 18pt `#5A6676` l |

### 10. Data Table

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `tx101` | — |  | 56 | 48 | 1328 | 24 | “表格 · TABLE” 20pt bold `#0B318F` |
| `title102` | title | 0 | 56 | 76 | 1328 | 56 | 30pt bold `#1A2230` l |
| `sh103` | — |  | 56 | 142 | 1328 | 1.5 | fill `#0B318F` |
| `tx104` | — |  | 56 | 772 | 929.6 | 22 | “{{ORG}}  \|  {{DECK_TITLE}}” 13pt `#5A6676` |
| `sldNum105` | slide_number | 12 | 1324 | 772 | 60 | 22 | 13pt `#5A6676` r |
| `tbl106` | table | 10 | 56 | 172 | 1328 | 480 | 18pt `#1A2230` l |
| `tx107` | — |  | 56 | 662 | 1328 | 22 | “Source:” 13pt `#5A6676` |

### 11. Diagram Frame

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `tx101` | — |  | 56 | 48 | 1328 | 24 | “架構 · ARCHITECTURE” 20pt bold `#0B318F` |
| `title102` | title | 0 | 56 | 76 | 1328 | 56 | 30pt bold `#1A2230` l |
| `sh103` | — |  | 56 | 142 | 1328 | 1.5 | fill `#0B318F` |
| `tx104` | — |  | 56 | 772 | 929.6 | 22 | “{{ORG}}  \|  {{DECK_TITLE}}” 13pt `#5A6676` |
| `sldNum105` | slide_number | 12 | 1324 | 772 | 60 | 22 | 13pt `#5A6676` r |
| `sh106` | — |  | 56 | 172 | 1328 | 460 | fill `#F0F6FC` line `#C3D6EE` |
| `dgm107` | org_chart | 10 | 72.2 | 188.2 | 1295.6 | 427.6 | 18pt `#5A6676` ctr |
| `body108` | body | 11 | 56 | 646 | 1328 | 34 | 13pt `#5A6676` l |

### 12. Picture with Caption

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `tx101` | — |  | 56 | 48 | 1328 | 24 | “圖說 · EXHIBIT” 20pt bold `#0B318F` |
| `title102` | title | 0 | 56 | 76 | 1328 | 56 | 30pt bold `#1A2230` l |
| `sh103` | — |  | 56 | 142 | 1328 | 1.5 | fill `#0B318F` |
| `tx104` | — |  | 56 | 772 | 929.6 | 22 | “{{ORG}}  \|  {{DECK_TITLE}}” 13pt `#5A6676` |
| `sldNum105` | slide_number | 12 | 1324 | 772 | 60 | 22 | 13pt `#5A6676` r |
| `pic106` | picture | 10 | 56 | 172 | 770.24 | 520 | 18pt `#5A6676` ctr |
| `body107` | body | 11 | 858.64 | 172 | 525.36 | 480 | 18pt `#5A6676` l |
| `tx108` | — |  | 858.64 | 658 | 525.36 | 24 | “Source:” 13pt `#5A6676` |

### 13. Risk Matrix

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `tx101` | — |  | 56 | 48 | 1328 | 24 | “風險 · RISK” 20pt bold `#0B318F` |
| `title102` | title | 0 | 56 | 76 | 1328 | 56 | 30pt bold `#1A2230` l |
| `sh103` | — |  | 56 | 142 | 1328 | 1.5 | fill `#0B318F` |
| `tx104` | — |  | 56 | 772 | 929.6 | 22 | “{{ORG}}  \|  {{DECK_TITLE}}” 13pt `#5A6676` |
| `sldNum105` | slide_number | 12 | 1324 | 772 | 60 | 22 | 13pt `#5A6676` r |
| `tx106` | — |  | 56 | 412 | 80 | 30 | “衝擊\nImpact” 13pt bold `#5A6676` |
| `tx107` | — |  | 146 | 660 | 480 | 24 | “可能性　Likelihood” 13pt bold `#5A6676` |
| `sh108` | — |  | 146 | 172 | 240 | 240 | fill `#E6F2FC` line `#C3D6EE` |
| `body109` | body | 10 | 162.2 | 188.2 | 207.6 | 207.6 | 18pt `#5A6676` l |
| `sh110` | — |  | 386 | 172 | 240 | 240 | fill `#F0F6FC` line `#C3D6EE` |
| `body111` | body | 11 | 402.2 | 188.2 | 207.6 | 207.6 | 18pt `#5A6676` l |
| `sh112` | — |  | 146 | 412 | 240 | 240 | fill `#F0F6FC` line `#C3D6EE` |
| `body113` | body | 41 | 162.2 | 428.2 | 207.6 | 207.6 | 18pt `#5A6676` l |
| `sh114` | — |  | 386 | 412 | 240 | 240 | fill `#0B318F` line `#C3D6EE` |
| `body115` | body | 13 | 402.2 | 428.2 | 207.6 | 207.6 | 18pt `#FFFFFF` l |

### 14. Incident Detail

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `tx101` | — |  | 56 | 48 | 1328 | 24 | “關注事件 · INCIDENT” 20pt bold `#0B318F` |
| `title102` | title | 0 | 56 | 76 | 1328 | 56 | 30pt bold `#1A2230` l |
| `sh103` | — |  | 56 | 142 | 1328 | 1.5 | fill `#0B318F` |
| `tx104` | — |  | 56 | 772 | 929.6 | 22 | “{{ORG}}  \|  {{DECK_TITLE}}” 13pt `#5A6676` |
| `sldNum105` | slide_number | 12 | 1324 | 772 | 60 | 22 | 13pt `#5A6676` r |
| `sh106` | — |  | 56 | 172 | 655.9 | 251.9 | fill `#F0F6FC` |
| `sh107` | — |  | 56 | 172 | 4 | 251.9 | fill `#0B318F` |
| `tx108` | — |  | 72.2 | 186 | 623.5 | 26 | “事件概要　Summary” 18pt bold `#0B318F` |
| `body109` | body | 10 | 72.2 | 220 | 623.5 | 189.9 | 18pt `#5A6676` l |
| `sh110` | — |  | 728.1 | 172 | 655.9 | 251.9 | fill `#F0F6FC` |
| `sh111` | — |  | 728.1 | 172 | 4 | 251.9 | fill `#0B318F` |
| `tx112` | — |  | 744.3 | 186 | 623.5 | 26 | “處置作為　Response” 18pt bold `#0B318F` |
| `body113` | body | 11 | 744.3 | 220 | 623.5 | 189.9 | 18pt `#5A6676` l |
| `sh114` | — |  | 56 | 440.1 | 655.9 | 251.9 | fill `#F0F6FC` |
| `sh115` | — |  | 56 | 440.1 | 4 | 251.9 | fill `#0B318F` |
| `tx116` | — |  | 72.2 | 454.1 | 623.5 | 26 | “影響評估　Impact” 18pt bold `#0B318F` |
| `body117` | body | 41 | 72.2 | 488.1 | 623.5 | 189.9 | 18pt `#5A6676` l |
| `sh118` | — |  | 728.1 | 440.1 | 655.9 | 251.9 | fill `#F0F6FC` |
| `sh119` | — |  | 728.1 | 440.1 | 4 | 251.9 | fill `#0B318F` |
| `tx120` | — |  | 744.3 | 454.1 | 623.5 | 26 | “後續追蹤　Follow-up” 18pt bold `#0B318F` |
| `body121` | body | 13 | 744.3 | 488.1 | 623.5 | 189.9 | 18pt `#5A6676` l |

### 15. Project Status

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `tx101` | — |  | 56 | 48 | 1328 | 24 | “專案進度 · PROJECTS” 20pt bold `#0B318F` |
| `title102` | title | 0 | 56 | 76 | 1328 | 56 | 30pt bold `#1A2230` l |
| `sh103` | — |  | 56 | 142 | 1328 | 1.5 | fill `#0B318F` |
| `tx104` | — |  | 56 | 772 | 929.6 | 22 | “{{ORG}}  \|  {{DECK_TITLE}}” 13pt `#5A6676` |
| `sldNum105` | slide_number | 12 | 1324 | 772 | 60 | 22 | 13pt `#5A6676` r |
| `sh106` | — |  | 56 | 172 | 1328 | 117 | fill `#F0F6FC` |
| `sh107` | — |  | 56 | 172 | 4 | 117 | fill `#0B318F` |
| `body108` | body | 10 | 72.2 | 184 | 398.4 | 30 | 18pt bold `#1A2230` l |
| `body109` | body | 11 | 507.52 | 184 | 823.36 | 95 | 18pt `#5A6676` l |
| `sh110` | — |  | 56 | 297 | 1328 | 117 | fill `#F0F6FC` |
| `sh111` | — |  | 56 | 297 | 4 | 117 | fill `#00A3E6` |
| `body112` | body | 41 | 72.2 | 309 | 398.4 | 30 | 18pt bold `#1A2230` l |
| `body113` | body | 13 | 507.52 | 309 | 823.36 | 95 | 18pt `#5A6676` l |
| `sh114` | — |  | 56 | 422 | 1328 | 117 | fill `#F0F6FC` |
| `sh115` | — |  | 56 | 422 | 4 | 117 | fill `#2E5BF0` |
| `body116` | body | 14 | 72.2 | 434 | 398.4 | 30 | 18pt bold `#1A2230` l |
| `body117` | body | 15 | 507.52 | 434 | 823.36 | 95 | 18pt `#5A6676` l |
| `sh118` | — |  | 56 | 547 | 1328 | 117 | fill `#F0F6FC` |
| `sh119` | — |  | 56 | 547 | 4 | 117 | fill `#7C4DB8` |
| `body120` | body | 16 | 72.2 | 559 | 398.4 | 30 | 18pt bold `#1A2230` l |
| `body121` | body | 17 | 507.52 | 559 | 823.36 | 95 | 18pt `#5A6676` l |

### 16. Action Items

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `tx101` | — |  | 56 | 48 | 1328 | 24 | “追蹤事項 · ACTIONS” 20pt bold `#0B318F` |
| `title102` | title | 0 | 56 | 76 | 1328 | 56 | 30pt bold `#1A2230` l |
| `sh103` | — |  | 56 | 142 | 1328 | 1.5 | fill `#0B318F` |
| `tx104` | — |  | 56 | 772 | 929.6 | 22 | “{{ORG}}  \|  {{DECK_TITLE}}” 13pt `#5A6676` |
| `sldNum105` | slide_number | 12 | 1324 | 772 | 60 | 22 | 13pt `#5A6676` r |
| `sh106` | — |  | 56 | 172 | 1328 | 38 | fill `#0B318F` |
| `tx107` | — |  | 66 | 180 | 72.96 | 24 | “項次” 18pt bold `#FFFFFF` |
| `tx108` | — |  | 158.96 | 180 | 564.32 | 24 | “事項” 18pt bold `#FFFFFF` |
| `tx109` | — |  | 743.28 | 180 | 179.2 | 24 | “負責人” 18pt bold `#FFFFFF` |
| `tx110` | — |  | 942.48 | 180 | 205.76 | 24 | “完成期限” 18pt bold `#FFFFFF` |
| `tx111` | — |  | 1168.24 | 180 | 205.76 | 24 | “狀態” 18pt bold `#FFFFFF` |
| `sh112` | — |  | 56 | 210 | 1328 | 44 | fill `#F0F6FC` |
| `sh113` | — |  | 56 | 254 | 1328 | 0.75 | fill `#C3D6EE` |
| `sh114` | — |  | 56 | 298 | 1328 | 0.75 | fill `#C3D6EE` |
| `sh115` | — |  | 56 | 298 | 1328 | 44 | fill `#F0F6FC` |
| `sh116` | — |  | 56 | 342 | 1328 | 0.75 | fill `#C3D6EE` |
| `sh117` | — |  | 56 | 386 | 1328 | 0.75 | fill `#C3D6EE` |
| `sh118` | — |  | 56 | 386 | 1328 | 44 | fill `#F0F6FC` |
| `sh119` | — |  | 56 | 430 | 1328 | 0.75 | fill `#C3D6EE` |
| `sh120` | — |  | 56 | 474 | 1328 | 0.75 | fill `#C3D6EE` |
| `tbl121` | table | 10 | 56 | 210 | 1328 | 264 | 18pt `#1A2230` l |

### 17. Quote

Background override: **`#F0F6FC`** (warm: `#E8E4DF`) — this layout is not on the default field.

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `tx101` | — |  | 56 | 250 | 90 | 110 | ““” 130pt bold `#0B318F` |
| `body102` | body | 10 | 126 | 290 | 1188 | 200 | 28pt `#1A2230` l |
| `sh103` | — |  | 126 | 520 | 90 | 3 | fill `#0B318F` |
| `body104` | body | 11 | 126 | 545 | 1188 | 40 | 18pt `#5A6676` l |
| `tx105` | — |  | 56 | 772 | 929.6 | 22 | “{{ORG}}  \|  {{DECK_TITLE}}” 13pt `#5A6676` |
| `sldNum106` | slide_number | 12 | 1324 | 772 | 60 | 22 | 13pt `#5A6676` r |

### 18. Blank

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `sh101` | — |  | 56 | 142 | 1328 | 1.5 | fill `#0B318F` |
| `tx102` | — |  | 56 | 772 | 929.6 | 22 | “{{ORG}}  \|  {{DECK_TITLE}}” 13pt `#5A6676` |
| `sldNum103` | slide_number | 12 | 1324 | 772 | 60 | 22 | 13pt `#5A6676` r |

### 19. Closing

Background override: **`#0B318F`** (warm: `#CC785C`) — this layout is not on the default field.

| shape | kind | idx | x | y | w | h | size / colour |
|---|---|---|---|---|---|---|---|
| `title101` | title | 0 | 56 | 300 | 1062.4 | 80 | 34pt bold `#FFFFFF` l |
| `body102` | body | 1 | 56 | 400 | 929.6 | 200 | 21pt `#FFFFFF` l |
| `tx103` | — |  | 56 | 772 | 1328 | 22 | “{{ORG}} · {{UNIT}}” 13pt `#FFFFFF` |
