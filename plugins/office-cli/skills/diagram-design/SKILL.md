---
name: diagram-design
description: Draw editorial diagrams as self-contained HTML/SVG in any house template's palette — architecture, flowchart, sequence, state machine, ER, timeline, swimlane, quadrant, layer stack, tree, Venn, funnel, Sankey, fishbone, Wardley, Gantt, user journey, dependency graph and 20 more. Use when a reader would learn more from a picture than from prose or a table, when a deck or report needs an architecture, process, risk or data-flow visual, or when redrawing a draw.io or Mermaid source. Not for charts inside a deck — those are native chart parts.
---

# diagram design

Thirty-nine diagram types as self-contained HTML with inline SVG. No JavaScript, no build step, no external images.

Vendored from [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) v2.6 (MIT). **The upstream instructions are [`references/upstream-SKILL.md`](references/upstream-SKILL.md) — read that for type selection and layout grammar.** This file covers only what differs here.

## 1. Generate the profile, don't hand-write it

The five templates in [`house-style`](../house-style/SKILL.md) are the single source of truth for every palette in this system. A diagram profile is *derived* from the template, never transcribed:

```bash
python3 scripts/make_profile.py ana-blue -o references/style-guide.md
```

`--all -o <dir>` writes every template at once. Slugs: `ana-blue`, `yukima`, `reiser-warm`, `sks-dark`, `sks-blue`.

This replaces upstream's first-run onboarding gate (§0 of `upstream-SKILL.md`) — **skip that gate, and never run brand extraction from a website.** It also replaces the `~/.diagram-design/profiles/` library described in [`references/profiles.md`](references/profiles.md); that mechanism still works, but a profile generated here cannot drift from the template it came from, and a hand-saved one can.

Match the profile to the deliverable the diagram lands in. A Reiser Warm diagram dropped into an ANA Blue deck is an off-brand asset, not a variation.

## 2. What the generator derives, and why

Two roles have no equivalent in `theme.json` and are computed:

**`accent` must survive as text.** diagram-design paints node labels with `accent`, not just strokes. Where a template's accent cannot carry type, the generator preserves the hue and moves the value until it clears 4.5:1 — darker on a light field, lighter on a dark one. Reiser Warm's coral `#CC785C` (2.92:1) becomes `#9E5D47`; SKS Dark's amber `#B57319` (3.82:1) becomes `#C67E1B`. The template's original value stays as `accent-tint`, which is the fill role it was always safe in.

**`soft` carries 9px sublabels**, so it is derived to clear 4.5:1 on the **panel tint** rather than the field — a sublabel inside a panel is the case that fails first, and checking it against the field alone hides the failure.

Every ratio in a generated profile was computed at generation time. Regenerate after any template change rather than patching the output.

## 3. Geometry diverges from the deck, on purpose

Containers square, nodes and chips at most 4px, 1px hairlines, no shadows — against templates whose panels run to 18–26pt radius.

A deck panel is brand surface; a diagram node is structure. Near-square keeps nodes reading as schematic rather than as UI cards. **Do not reconcile the two in either direction.**

## 4. The two rules that carry the most weight

**The highest-quality move is usually deletion.** Target density 4/10. Two nodes that always travel together are one node. Above nine nodes it is probably two diagrams.

**One accent, one or two focal elements.** On five nodes it is not an accent, it is decoration — the same 60-30-10 ceiling `house-style` applies to decks.

## 5. Where the output goes

| Destination | How |
|---|---|
| Into a deck | Render to PNG and place it, or rebuild the geometry natively with `pptx-cli` when it must stay editable in PowerPoint |
| Into a document | Render to PNG and place with `docx-cli` |
| On its own | Deliver the HTML |

A pasted PNG is not editable and does not reflow. Say so rather than presenting it as native.

## 6. Choosing this over the alternatives

| Need | Use |
|---|---|
| Structure, relationships, flow, hierarchy, boundaries | **this skill** |
| Quantitative values inside a `.pptx` | `deck-build` native chart parts — a real chart the recipient can click and edit |
| A chart in an HTML artifact or a Python figure | `dataviz` |
| Whether the slide should exist at all | [`house-style/references/slide-craft.md`](../house-style/references/slide-craft.md) |

Upstream ships bar, line, scatter, treemap and Sankey types. Prefer them for a standalone editorial figure; prefer a native chart inside a `.pptx`, because a PNG of a chart loses the data behind it.

## 7. Before delivering

```bash
python3 scripts/self_check.py <file>.html
```

Then look at it. The checker catches geometry and label overlap; it cannot tell you whether the diagram was worth drawing. Ask that question before you start — if a well-written paragraph would teach the reader more, write the paragraph.

## Vendoring notes

`assets/` is not bundled: 158 example HTML files, 2.4MB, which upstream's own style guide notes were built under an older skin. Fetch them from the repo to browse examples. The 54 references, the 39 type specs, `scripts/self_check.py` and the draw.io / Mermaid importers are upstream verbatim; `scripts/make_profile.py` is new work for this system. Attribution in [`../../NOTICE.md`](../../NOTICE.md).
