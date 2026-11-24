# Design system on a 1920×1080 stage

The tokens, typefaces and colour roles come from `hs-vilab-frontend-design` (copied into
`assets/tokens.css`, `fonts.css`, `base.css`). That skill is written for interfaces; this file
says how its rules translate to a projected slide. The engine (`assets/engine/deck.css`) already
implements all of it — this is what to keep in mind when choosing blocks and writing copy, and what
not to work around.

## Stage and type

- One logical stage, 1920×1080, scaled to the window with letterboxing. A 1024×768 projector sees
  the same layout at 53% — **judge legibility there** (`qa_render.py --viewport 1024x768`).
- Type ladder: 80 / 56 / 48 / 40 / 36 / 32 / 28 / 24 px. Floor 24px, measured on every text node,
  SVG text included. Body weight 500 (Geomini 500 + Gmarket Sans Medium), headings 700. Light
  weights disappear on a projector.
- Latin in Geomini, Hangul in Gmarket Sans; QA checks the face Chromium actually drew for every
  glyph. Math is TeX (Arev Sans) rendered to SVG at build time.

## Colour and surfaces

- White ground, HSU Dark Blue headings, one accent (sky blue) for the current item, the focus bar,
  the selected toggle, the chart highlight. The warm accent marks pairs (delta ↔ rows) and is never
  text.
- `wash` (grey ground) for slides whose evidence is a chart or table drawn by the build.
- Dark statement slides (`#12263D`) for TL;DR and discussion only: no panels there, dividers instead.
- One surface: `panel` (radius 6, 1px border, no shadow, never nested, ≤ 2 per slide, ≥ 40% of
  slides without one). Cards are ruled columns. No gradients, no shadows, no left colour stripes.

## What is banned and why it matters here

- **Eyebrows**, uppercase tracked labels, `A · B · C` meta lines: the footer progress bar carries the
  section, with real information (where the talk is, how long each part is).
- Titles that deliver the verdict (the speaker's punchline on the slide) — `narrative-rules.md`.
- Shrinking type to make content fit. Cut, split, or change the block.
- Decorative motion. One automatic motion per slide, all of it finishing on the next key press.

## Figures

- Paper figures: crop the region at 400 dpi (`extract_figures.py crop --dpi 400`), keep axes,
  ticks and legend, leave the paper's caption out — the slide writes its own `**Fig. n**` caption
  with the conditions (dataset, model size, steps, CFG).
- A figure with small text (legends of eight curves, rollout strips) is shown alone and large —
  a toggle tab or a full-width slide — or cut with a reason in the ledger. Never three strips side
  by side.
- Our own diagrams are SVG in token colours with `role="img"` and a `<title>`; illustrations that
  re-draw a paper figure (e.g. noise on a token grid) say so in the caption.

## Cover and footer

- Cover: title, subtitle, a thin rule with a short accent, the teaser figure, and on the right the
  presenter block (name 40px, affiliation 28px, event/date) above the HSU signature (48px tall).
  The reviewed paper's authors sit small under the subtitle.
- Footer on every other slide: section progress (segment length ∝ slide count), folio, signature
  30px (white version on dark).
