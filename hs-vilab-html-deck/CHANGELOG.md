# Changelog

## 0.1.0 — 2026-11-24

First end-to-end run: the Self-Flow paper as a 20-minute, 21-slide lab-seminar deck
(`work/self-flow-full`), with codex as author and Korean editor, agy as critic, verifier,
researcher and visual reviewer, Claude conducting.

Added
- `SKILL.md` and `references/` (narrative rules and roles, the codex brief, Korean editing,
  block vocabulary, interaction rules, design system on the stage, QA checklist).
- Blocks: `bullets`, `cards` (ruled columns, not boxes), `callout`, `equation` (display, tags,
  symbol key), `process`, `compare`, `figureNumbered`, `diagram`, `stepper`; toggles over paper
  figures (one image per state) and extra blocks beside the readout (`side`); figure `height`.
- Build gates: slide count = `meta.target_slides`; summed `time` within ±10% of the talk;
  `note` blocks ≤ max(2, ⌈content slides / 4⌉); stepper and image-toggle file checks.
- `deck/script.html`: the speaker script with per-slide time, running total, key sentence and
  toggle cues.
- `export_pdf.py`: vector PDF, one page per slide, toggle states expanded (6a–6d).
- `preflight.py`, `delegate.py` (codex/agy routing with fallback that is always reported),
  `extract_figures.py`, `deck_text.py`, `apply_text_edits.py` (from hs-vilab-deck, adapted).

Fixed — found by running the whole pipeline
- Tables right-aligned word columns: number columns now align right, word columns left
  (detected per column).
- An image toggle let its figure grow to the column width and push past the stage: the image now
  fits the remaining height.
- Four toggle buttons wrapped onto two lines: four or more states use compact buttons, labels
  never wrap.
- `extract_figures.py` crashed printing to a cp949 console.
- QA `collide`: overlapping text lines (or text and an image) anywhere on a slide. The first
  visual round found a caption overlap (P0) that the band check could not see; a figure beside a
  toggle readout no longer shrinks, so a tall column now spills (caught) instead of overlapping.
- A toggle with four or more states puts its buttons on a row across both columns, so the visual
  and the readout can take any ratio; with three or fewer the readout still starts at the top.
- Figures sit on their column's left edge (the mat wraps the image); `valign: "center"` for
  sparse slides; a Korean particle stays on the math before it; a count stays with its unit; `약 625M` and
  `no CFG` do not split.
- `delegate.py`: a brief with the paper inline exceeds the Windows command line for agy; long
  prompts are written into the read folder instead.

Process lessons, written into `references/narrative-roles.md`
- The verifier caught a result written as a win that the figure contradicts (a robotics task
  where the baseline led at 100K).
- Research must be checked at the source: a reported conference acceptance and a baseline number
  were not on the pages cited, a follow-up paper was real and became a discussion point.
- Two verifiers disagreed about a curve (a linear probe "reversing" in late layers); the figure,
  zoomed, showed neither was right. Claims that rest on reading a curve are checked by the
  conductor on the figure.
- The Korean editor merged 표현 (representation, the concept) into "feature"; seven rows were
  rejected. Review the editor's table before applying it.

## Sample stage (before 0.1.0)

Engine, cover, toggle, bars, table, deltas, panels, dark statement slides, motion, HSU signature
from the official vector, two agy visual rounds on a 6-slide sample (`work/self-flow`).
