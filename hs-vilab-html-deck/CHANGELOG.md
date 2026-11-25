# Changelog

## 0.3.0 — 2026-11-24

Second paper: REPA (ICLR 2025), a 20-minute, 21-slide seminar deck (`work/repa`) with a stepper,
two image-tab toggles and the full team. Everything below was found by running it.

Process
- **[0] asks the same four questions as hs-vilab-deck**: 발표 시간 / 자리·중심 줄기 / 언어 /
  작업 방식 (four boxes: codex draft, agy research, agy visual review, second round). The
  presenter is reused from the last deck, not asked.
- **codex could not read a Google Drive folder.** Its Windows read-only sandbox denied every file
  on the G: drive: the Korean edit came back "access denied", the revision could not open a
  figure. `delegate.py` now stages the read folder on the local temp disk for codex.
- A curve read by a reviewer was wrong again (Fig. 3: layers 6–24, not 4–24; layer 24 above
  vanilla). `narrative-roles.md` keeps the rule: range + "곡선 근거" until the conductor has looked.

Engine
- Cover credit: the asterisk was always printed as "* 공동 1저자"; in REPA it marks equal
  advising. `meta.paper.authorNote` says what it marks; the build refuses `*` without it.
- `valign: "center"` did nothing on a slide whose body is a `split` (the split stretched).
- Deltas share one grid: every value and label starts on the same line.
- A toggle readout without a panel keeps the tallest state's height (the note under it jumped).
- A stepper caption sits under the diagram. A figure given a `height` keeps it.
- A nested split uses a 40px gap. Line keeping: `Fig. 3`, `Table 4`, `FID 5.30`, `= 9.6`, and a
  number after inline math (`$k$ = 10개로`).
- PDF: a stepper with `print: "expand"` gets a page per step — the fully revealed page showed only
  REPA's last step, which greys out the training path.

QA (`qa_render.py`) — three defects it could not see
- a block whose content runs into the next block (a caption pushed under the caption below it);
- a diagram label running past its `<foreignObject>` (SVG was skipped);
- stepper steps after the first were never captured or measured.

Scripts: `deck_text.py` no longer crashes on a cp949 console; `apply_text_edits.py` keeps the
file's indent (the diff shows only edited strings); `extract_figures.py` no longer suggests a
PPT-only block.

## 0.2.0 — 2026-11-24

- **The HTML is the final version.** The build writes one self-contained `<slug>.html` (and
  `<slug>-script.html`) at the top of the work folder — fonts, styles, engine, figures inlined,
  large figures re-encoded as WebP (the 21-slide deck: 8.1 MB). `bundle_html.py`; `qa_render.py
  --html` runs QA on the delivered file.
- **PDF captions ran past the page** on five pages (image toggles): Chromium's paginated layout
  resolves a figure fitted with `max-height:100%` differently from the screen. `export_pdf.py`
  freezes every figure at its screen size before printing and then checks each page (overlapping
  lines, text crossing the progress bar, text beyond the edge); the check was confirmed to catch
  all five pages on a PDF printed without the freeze. The PDF is a render check, not a deliverable.
- **Ending slide**: `layout: "ending"` (감사합니다 / Q&A, presenter, signature, links); the build
  requires the deck to end on one.
- A one-section progress segment never shrinks below its label (a one-slide 정리와 토론 clipped).

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
