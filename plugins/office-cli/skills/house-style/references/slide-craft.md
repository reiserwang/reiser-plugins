# Slide craft

The rest of this skill governs how a deck **looks** — palette, grid, geometry, contrast. This file governs whether it **says anything**. A deck can pass `officecli view issues`, `contrast.py --check` and `check_deck.py`'s colour gate and still be worthless, because none of those read the argument.

Read this before writing the first slide, not after.

> **Provenance.** The craft rules below are adapted from [`consulting-pptx-skill`](https://github.com/gozen3ji/consulting-pptx-skill) (Carnot AI Inc., MIT) — a canon accumulated one line at a time from real review feedback on real decks. They are re-expressed here for this system's canvas, standing furniture and bilingual EN·中文 convention, and trimmed to what survives the move out of its original Japanese-consulting context. Rules specific to that context (their A4 exception, their 36-type catalogue, their HTML pipeline) are deliberately not carried across.

---

## 0. Before you build

**Define before you produce.** Three to five lines, agreed before any file is created: who the deck is for, what decision it is meant to support, and what is in and out of scope. A thin argument in a beautiful template is the worst possible outcome — it costs a reviewer's time to discover the thinness.

**Write the storyline first — as a list of titles.** One line per slide, in order, before choosing a single layout. Beside each line, note how it will be shown: figure, table, two-column, chevrons, big number. Slide count and layout come *after* this list, never before.

**If you cannot name the meeting and the decision, do not build a deck.** Put the argument on one page, or in prose. Every additional slide multiplies both the surface for error and the chance the whole thing reads as generated. One accurate page beats twelve assembled ones.

**Read the source material first.** Never infer a figure, a date, or a proper noun. Check each against a primary source; for a negative claim, open the document rather than trusting a summary.

---

## 1. Titles

The title carries the message. Everything else on the slide is evidence for it.

1. **State the conclusion in the title.** Not the topic — the finding. "Coverage reached all 12 subsidiaries in Q3" not "Coverage status".
2. **No label prefixes.** `現況與挑戰：…`, `Roadmap: …`, `Overview — …`. A label tells the reader which bucket the slide is in; it does not tell them what to conclude. `check_deck.py` flags these.
3. **One line, two if the message needs it.** Never shrink the type to force one line. On a two-line title, break at the sense join — a second line of one or two words is an orphan and reads as a mistake.
4. **A plain sentence, not a slogan.** Keep the subject and the object. No compression into noun stacks (`稽核強化`, `Process Optimization`) — say who does what.
5. **Self-contained.** No "this", "the above", "as discussed" pointing at another slide.
6. **Do not put the page's own item count in the title.** "Four initiatives to…" tells the reader nothing they cannot see. If a number *is* the message ("three stages, not five"), keep it — and then rule 7 applies.
7. **A number in the title must match the body.** Title says three phases, body shows four chevrons: that contradiction is the first thing a reader notices and the fastest way to lose them. `check_deck.py` fails the deck on it.
8. **No colour inside a title.** Titles are ink — `#101623` on a light field, `#FFFFFF` on a dark one. Accent runs inside a title read as decoration.
9. **The title column must read as one argument.** Extract every title, read them top to bottom, and check they form a single line of reasoning. `check_deck.py` prints the column for exactly this.
10. **Do not write titles from the template's sample titles.** They show the *grain* of claim a layout carries, not a mould to fill. If most of your titles share one sentence shape, you are transcribing a template rather than writing a deck — `check_deck.py` warns at 60%.
11. **A chart slide always carries a so-what.** The figure states the fact; the title or the right column states what follows from it. A chart with no consequence is decoration.
12. **Never claim more than the evidence.** Especially about a client or a partner. Conservative and checkable beats strong and challengeable.

## 2. No subtitles

No explanatory line under the title. No caption above a figure or table, and none below an image. What a table shows is the slide's title, or the panel heading inside the card.

**The one exception is an axis title** — a single line naming the data and its unit and period, immediately above the figure: `Recorded incidents, count, FY2024–FY2026`. That is data labelling, not a subtitle.

## 3. Layout

1. **One slide, one message.** If two things must be said, that is two slides.
2. **Split left–right, not top–bottom.** Left carries the fact or the figure; right carries what it means. A reader scans a wide 16:9 page horizontally; stacking forces a vertical read the format fights.
3. **No "POINT" band across the bottom.** The point belongs in the title.
4. **No floating elements.** Every label, chip and box belongs to a structure — a table cell, a column, a chart axis. A box that appears with no axis to hang from is the single clearest tell of a generated slide.
5. **The body fills at least 55% of the content band** (`y = 172 → 760`). A page whose lower half is empty was under-thought, not minimal. `check_deck.py` warns below that.
6. **Bottom-align the columns.** In a two-column layout, the left and right blocks end level.

## 4. Boxes, colour, legends

1. **Square corners.** No `roundRect` anywhere. The only exception is a status pill under about 20pt tall.
2. **A filled box takes no border.** The fill already marks the region; a stroke on top of it is noise. Borders belong to unfilled elements only.
3. **Rules only where something is being separated.** No rule under a table's last row, none across the bottom of a slide (the footer rule excepted).
4. **Colour-coding requires a legend on the same slide** — swatch plus meaning. A dark card used only for emphasis, with no encoded meaning, is decoration.
5. **Include a neutral in any categorical set.** Every one of this system's ramps already carries a grey or a slate for exactly this — the baseline, the third party, the non-highlighted case. Colouring every category is how a chart stops meaning anything.
6. **Highlight the side that wins.** In a comparison table, the highlight follows the better answer, not always your own column — and a fair comparison includes at least one axis where the other side wins.
7. **A bounded metric is drawn on its full scale.** Percentages, rates, correlation coefficients: axis runs 0 to the theoretical maximum. Truncating the axis to make a difference look bigger is the oldest chart lie there is.
8. **Measured figures carry their conditions** — what was measured, how many, by whom.

## 5. Tables

A table in this system has an **axis**: rows are the things, columns are the viewpoints. A grid of cards with a heading each is not a table; it is a list wearing a table's clothes.

| Element | Rule |
|---|---|
| Header row | Bold, 2pt larger than the body, in the accent-as-type colour. **No fill** — the axis is marked by a heavy rule under the header, not by a coloured band. |
| Row-axis column | The leftmost column is the axis: 4pt larger than the body, so it reads as the thing the row *is*. |
| Rules | Heavy under the header, hairline between rows, **nothing under the last row**. |
| Banding | Not in this system for slides. The `.docx` and `.xlsx` mappings use it; a slide table does not. |
| Column names | Concrete nouns naming what the cell holds. Never `Facts`, `Items`, `Details` — those are placeholders that survived. |
| Rows | Only members of the set the axis names. A row that is not one of those things is the most common table defect there is. |
| Columns | Only those the argument needs. An `Achievements` column in a role-assignment table makes the reader compare achievements instead of reading the assignment. |
| Granularity | Every cell in a column answers the same question at the same grain. |
| N/A cells | `—`, filled with the muted fill, so the eye skips them. Never blank. |
| Dense cells | A cell holding two or more items becomes two or three bullets, not one run-on sentence. |
| Emphasis | Bold the cells that drive the decision. A table where every cell has the same weight has no argument. |
| Source | Bottom-left of the slide, never inside the table or its title. |

## 6. Charts

1. **A trend, a composition, a distribution or a correlation is a chart.** Not a column of numbers, not a table. This is the rule most often broken when a template offers a convenient table component — the page ends up tidy and the point invisible.
2. **Pick a standard form.** Trend over time → line or column. Composition → stacked bar or, for one moment, a pie. Contribution to a change → waterfall. Two-axis positioning → scatter or a 2×2. Do not invent a shape.
3. **The chart carries its axes.** Both named, with units. A figure with no axis is the floating-box problem in graphical form.
4. **Series follow the template's chart order.** Each palette declares one; the order is part of the identity.
5. **Series labels are never in the series colour.** In SKS Blue this is a hard constraint — the shared ramp is mark-only in both themes. Elsewhere it is a good habit: label in ink, let the legend swatch carry the colour.

## 7. Prose

1. **One term per deck.** Pick `使用者` or `用戶`, `供應商` or `廠商`, `roadmap` or `road map` — and never both. `check_deck.py` warns on the common pairs.
2. **Expand an abbreviation on first use**, then use it consistently.
3. **Bullets: one claim per line.** A paragraph poured into a text box, unbroken, is the second-clearest tell of a generated slide.
4. **Bullet endings agree within a level.** All noun phrases, or all verb phrases — not a mix.
5. **No over-compression.** `手動建立`, `精度提升`, `Process Enhancement` — restore the subject and the verb.
6. **Cut the AI register.** `leverage`, `utilize`, `seamless`, `holistic`, `best-in-class`, `賦能`, `全面提升`, `深度融合`, `綜上所述`. `check_deck.py` warns on a high-confidence list; the list is a prompt to reread, not a verdict.
7. **No emoji, no traffic-light tables, no bold scattered for texture.**

## 8. The two review gates

Neither replaces the other, and neither is optional on a deliverable.

**Machine check.**

```bash
python3 <house-style>/scripts/check_deck.py deck.pptx --palette 'ANA Blue'
```

FAIL count must be 0. Read every WARN and decide — a WARN is a question, not a defect. Then read the printed title column top to bottom and confirm it is one argument.

**Fresh-eye review.** Hand the finished file to an agent that has not seen this conversation — the `Agent` tool, or a new session — with no explanation of how it was built, and ask it to read the deck and report: awkward phrasing, jumps in the logic, a number in a title that disagrees with its page, a title that disagrees with its own figure, an unsupported evaluative word, a page that restates an earlier one.

Then write the findings into an accept / reject table with a reason for each, fix only the accepted ones, and re-run the machine check.

Machine checks cannot see a broken argument, and the person who wrote the deck cannot see it either. That is what this gate is for.

**Then look at it.** `officecli view deck.pptx screenshot --grid --out contact.png`, and read the PNG — every page. Not just the text: the margins, the balance of the page, orphaned line breaks, overflow, whether the two columns end level.

## 9. When a rule here fights a rule elsewhere

The order of precedence in this skill is: the user's explicit instruction, then the template's `palette.md`, then `references/grid.md` and `references/layouts.md` for geometry, then this file. Where this file and the upstream OfficeCLI pptx reference disagree — the ≥36pt title rule is the standing example — this system wins, and the reason is in `SKILL.md` § 3.

A rule that turns out to be wrong for this organisation should be edited here, with the reason, rather than quietly ignored.
