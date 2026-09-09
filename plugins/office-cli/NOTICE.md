# Third-party notices

## consulting-pptx-skill

`skills/house-style/references/slide-craft.md` and the checkers under
`skills/house-style/scripts/` (`check_deck.py`, `check_doc.py`, `check_book.py`,
`house_prose.py`) are adapted from **consulting-pptx-skill** — https://github.com/gozen3ji/consulting-pptx-skill

The craft rules and the idea of a machine-checkable content gate come from that project's
`references/slide-rules.md`, a canon accumulated one line at a time from real review feedback,
and from its `scripts/check_deck.py`. Both files here are re-implemented for this system's
canvas, standing furniture, palettes and bilingual EN·中文 convention rather than copied; the
rules specific to the original's Japanese-consulting context are not carried across.

```
MIT License

Copyright (c) 2026 Carnot AI Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## diagram-design

`skills/diagram-design/references/` and `skills/diagram-design/scripts/self_check.py`,
`drawio_extract.py`, `mermaid_extract.py` are vendored verbatim from **diagram-design** v2.6 —
https://github.com/cathrynlavery/diagram-design

`skills/diagram-design/scripts/make_profile.py` is new work for this system: it derives a
diagram-design style guide from a `house-style` template's `theme.json` so the palettes cannot
drift apart. Upstream's `assets/` (158 example HTML files) is not bundled — upstream's own style
guide notes they were built under an earlier skin.

```
MIT License

Copyright (c) 2025 Cathryn Lavery
```
