# Reiser Warm — tokens

A warm-neutral identity built on 60-30-10, separate from [`ana-blue`](../ana-blue/palette.md). Every value below is present in `reiser-warm.pptx`. Never introduce a colour that is not on this page.

## Theme colour scheme

The `.pptx` theme is named `Reiser Warm`:

| Theme slot | Hex | Role |
|---|---|---|
| `dk1` / tx1 | `#1F1E1D` | charcoal ink |
| `lt1` / bg1 | `#F5F1ED` | warm cream field |
| `dk2` / tx2 | `#5C5650` | muted ink |
| `lt2` / bg2 | `#E8E4DF` | warm grey inset |
| `accent1` | `#CC785C` | coral — **fill only** |
| `accent2` | `#5C7B9C` | blue |
| `accent3` | `#6B8E5C` | sage |
| `accent4` | `#C28E3D` | gold |
| `accent5` | `#8B7BAB` | violet |
| `accent6` | `#5C9C8E` | teal |
| `hlink` | `#9D5C47` | links — the text-safe coral |
| `folHlink` | `#5C5650` | visited |

## 60% — the field

Four neutrals carry the surface and almost never carry text.

| Token | Hex | Role | ANA Blue equivalent |
|---|---|---|---|
| Warm cream | `#F5F1ED` | The default page, set on the master. Everything else sits on this. | `#FFFFFF` |
| Cool white | `#F5F3F1` | Lifted surface — a card that reads as *above* the page; callout and takeaway bands. | `#E6F2FC` |
| Warm grey | `#E8E4DF` | Inset surface — panels, sidebars, code blocks, quiet bands. | `#F0F6FC` |
| Stone | `#D4D0C9` | Rules, borders, table gridlines, dividers. | `#C3D6EE` |

Cream against warm grey is 1.13:1. That is deliberate — the neutrals are one family. For a hard boundary use a Stone rule, not a fill change.

## 30% — the supporting layer

| Token | Hex | On cream | Role |
|---|---|---|---|
| Charcoal | `#1F1E1D` | **14.81** | Primary ink. Headings and body. The workhorse. |
| Muted ink | `#5C5650` | **6.44** | Captions, labels, sources, footers, page numbers. |
| Sage mist | `#B3CBC1` | 1.53 | Supporting tint. **Fill only, never text.** |

`#5C5650` is a derived value, not an original swatch colour. The source swatch had no readable secondary text colour — everything in it either sat at 14.81:1 or failed as small text, and a palette needs a muted ink between those or every caption either shouts or is illegible. This one clears 4.5:1 on all three neutral surfaces including Stone (4.71:1).

## 10% — the accent

| Token | Hex | On cream | Role |
|---|---|---|---|
| Coral | `#CC785C` | 2.92 | The one accent. Fills, badges, title rules, the emphasised row, the single highlighted number, chart series 1. **Fill only.** |
| Coral deep | `#9D5C47` | **4.61** | Derived text-safe variant. Eyebrows, big numbers, KPI values, links — anywhere the coral hue must be text. |

One accent per page.

## Two traps

**Coral is a fill colour, not a text colour.** 2.92:1 on the cream field, fails at every size. Use `#9D5C47`.

**A coral fill takes charcoal text, not white.**

| Combination | Ratio | Verdict |
|---|---|---|
| `#FFFFFF` on `#CC785C` | 3.28 | ≥ 24px only |
| `#F5F1ED` on `#CC785C` | 2.92 | fails at every size |
| **`#1F1E1D` on `#CC785C`** | **5.08** | **any size — use this** |

## Extended categorical

For charts and multi-category coding. As *fills* they are all fine — the gate only measures text. As text on cream none clear 4.5:1, so each has a derived text-safe variant.

| Name | Fill | On cream | Text-safe | Variant ratio |
|---|---|---|---|---|
| Coral | `#CC785C` | 2.92 | `#9D5C47` | 4.61 |
| Blue | `#5C7B9C` | 3.92 | `#557190` | 4.50 |
| Sage | `#6B8E5C` | 3.31 | `#59764C` | 4.54 |
| Gold | `#C28E3D` | 2.58 | `#8C662C` | 4.61 |
| Violet | `#8B7BAB` | 3.39 | `#756790` | 4.56 |
| Teal | `#5C9C8E` | 2.83 | `#46776C` | 4.54 |
| Mauve | `#B07A9C` | 3.06 | `#8B607B` | 4.61 |
| Tan | `#8C7355` | 3.98 | `#816A4E` | 4.55 |

Chart series order: Coral → Blue → Sage → Gold → Violet → Teal. It alternates warm and cool so adjacent series separate. Mauve and Tan are held back for a seventh and eighth category; needing them usually means the chart should be split.

Project Status spine order: `#CC785C` → `#5C7B9C` → `#6B8E5C` → `#C28E3D`.

## Typography

Arial (Latin) + 微軟正黑體 (中文). Sizes on the 1440 × 810 pt canvas:

| Size | Role | Colour |
|---|---|---|
| 130pt | Quote opening glyph | `#9D5C47` |
| 96pt | Big Number | `#9D5C47` |
| 54pt | KPI value | `#9D5C47` |
| 40pt | Cover title | `#1F1E1D` on coral |
| 34pt | Section / Closing title | `#1F1E1D` on coral |
| 30pt | Slide title | `#1F1E1D` |
| 28pt | Quote body | `#1F1E1D` |
| 24pt | Agenda numeral | `#9D5C47` |
| 21pt | Cover subtitle, takeaway, rationale | `#1F1E1D` |
| 20pt | Eyebrow (bold) | `#9D5C47` |
| 18pt | Body, panel heading, table header | `#1F1E1D` / `#5C5650` |
| 13pt | Footer, page number, source, caption | `#5C5650` |

Bullet ramp on the master: 18 → 16 → 15 → 14 → 13pt, `#1F1E1D` at level 1 and `#5C5650` below. Bold is the only weight variation.

## Word (.docx) mapping

| Element | Spec |
|---|---|
| Page background | `#F5F1ED` warm cream |
| Body | Arial 10.5pt `#1F1E1D`, 1.15 line spacing |
| Heading 1 / 2 | `#1F1E1D` — weight carries the hierarchy, not colour |
| Caption, footnote, source | Arial 9pt `#5C5650` |
| Table header row | fill `#E8E4DF`, charcoal bold text — *not* a coral fill |
| Table banding | `#F5F3F1` |
| Table borders | `#D4D0C9` hairline |
| Emphasised row / total | fill `#CC785C` with **charcoal** text, or a `#CC785C` top border only |
| Hyperlink | `#557190` |

Set `font.ea=微軟正黑體` alongside `font.latin=Arial` for any 中文 content.

## Excel (.xlsx) mapping

| Element | Spec |
|---|---|
| Sheet background | `#F5F1ED` |
| Header row | fill `#E8E4DF`, Arial 10pt bold `#1F1E1D`, frozen |
| Banding | `#F5F3F1` alternate rows |
| Total / highlight row | fill `#CC785C` with charcoal text, or top border `#CC785C` only |
| Key metric cells | font `#9D5C47` bold |
| Body | Arial 10pt `#1F1E1D` |
| Borders | `#D4D0C9` thin; no heavy grids |
| Negative numbers | parentheses, not red — `#,##0;(#,##0)` |

## Verification

Every ratio here was computed against WCAG relative luminance, not estimated. Re-run after any change — snippet in [`../../references/contrast.md`](../../references/contrast.md).
