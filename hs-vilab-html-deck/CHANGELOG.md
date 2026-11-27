# Changelog

## 0.6.0 — 2026-11-26

**A fourth paper, with the overview planned from the start.** Integral ("Let Vision-Language Models
Generate Images through Their Representations", arXiv 2611.31237; `work/vlm-repgen`, 21 slides,
1200 s): a 20-minute lab seminar whose thread is the paper's central claim — sharing the visual
representation between understanding and generation helps generative learning beyond what
reconstruction quality explains — followed through its controlled comparisons to what they rule out.
codex drafted and revised, agy critiqued, verified (outline and `deck.json`), researched and
reviewed the captures twice; codex did the Korean edit; Claude conducted.

The deck
- 5: overview animation — a VLM with a separate VAE latent and a generation expert at every layer
  (Fig. 5a and Sec. 3.2's BAGEL), the latent swapped for AF's shared token z, the links thinned to
  every fourth layer (Block-wise MoT), two questions. The brief asked codex for its slot and beats;
  the critic turned the draft's "empty stage plus one arrow per press" into a change of shape.
- 15 (signature): a four-state toggle over Fig. 6a, 6b, 10a, 7 — one axis, each state saying what
  changed and which explanation it aims at. 16: a table of the alternative explanations and whether
  each comparison removes them. Both reviewers found the same point: under text-only LLM conditioning
  the AF latent already beats FLUX.1-VAE under VLM conditioning, so part of the gain may come from the
  latent itself — the first discussion question.
- External, checked at the source: WISE-Verified is judged by Qwen3.5-35B-A3B, the backbone's family
  (benchmark README); GenEval 2's authors consider GenEval saturated (abstract); code and checkpoint
  links from the model card. Three related-work summaries were not opened and not used.
- The critic struck a discussion point resting on two losses that are the same up to a factor
  (RMS-normalised MSE = 2(1 − cos)); the second verification caught synthesis merging GPT-4o-Image
  and GPT-4o, a baseline family miscounted, and a text value written as a curve reading.

Engine
- Table columns: a range (`256–512`, `48–64`), a bound (`≤ 512`) and a `B` suffix (`9.8B`) count as
  numbers and align right (Table 7's step, resolution and GPU columns had aligned left).
- A measurement stays with its unit: `54.9 ms`, `32.2 dB`, `19.0 GiB`, `387.6 TFLOPs`.
- Image-tab toggles: the media column takes its content's height, so the caption sits under a short
  figure instead of at the foot of the slide; `valign: center` now centres a toggle as it does a split.
  Checked by rebuilding Self-Flow with the new engine (both viewports clean, tall tabs unchanged).
- A caption right after a table sits 16 px under it, not 40 px (or 32 px in a split column).

Docs
- `handoff-narrative.md`: the brief template is now the Integral brief — it asks for the overview's
  slot, beats and `reveals`, lists `animation` among the blocks, and ends on an `ending` slide.
- `animation.md`: Integral as a worked example (its SVG is written by `make_overview_integral.py`);
  beat 0 is the design the paper argues against, built from its own words with the source in the
  caption; a counting label changes with what it counts; a link's label sits beside the link; a
  two-line SVG label is two foreignObjects (the build escapes markup).
- `interaction-rules.md`, `narrative-roles.md`, `block-vocabulary.md`: the Integral run's lessons.

## 0.5.0 — 2026-11-26

**Overview animations.** A diagram drawn as a function of time — `render(t)` sets every moving
attribute from t alone, adapted from a handover that analysed a paper project page's SVG explainers —
paced by the clicker: the slide opens still on beat 0, each next key plays one beat (≤ 2.0 s) and
stops, a key during a beat finishes it, previous jumps back, **M** turns motion off on the spot.
Designed with codex (engine and storyboard) and agy (critique), blind to each other
(`work/rae/review/anim/`); codex then reviewed the code (13 findings, 12 taken, 1 rejected).

RAE (`work/rae`, now 22 slides, 1200 s): the text-only "two beliefs" slide became two animations —
SD-VAE's latent becoming RAE's (Fig. 2 redrawn: the 2×2 patch becomes a token, the 256 tokens
stretch 16 → 768 channels, the two questions drop onto the pipeline), then reconstruction and
generation on RAE with the width, schedule shift, decoder noise augmentation and DDT head placed
where they act. Fig. 2 moved there from the RAE slide. No gFID in the overview (the ladder keeps it).

REPA (`work/repa`, now 22 slides, 1200 s): one overview added before the diagnosis slides, from a
second codex/agy round (`work/repa/review/anim/log.md`) — vanilla SiT as one bar of 28 blocks; the
same image, clean, through a frozen DINOv2-B and the input mismatch marked; the bar splits after
block 8 and an alignment line rises from it (training only); two questions. The authors' "later
layers learn details" stays a hypothesis for the discussion slide, not a fact in the picture. The
method stepper now opens on both paths (5 → 4 steps), its later blocks sit on one line with the
first and its inference veil is .62, not .88; two agy visual rounds (`visual_anim_triage_r*.md`). The
user's call: adding 1–2 slides for an overview is fine (`animation.md`, SKILL.md step 6).

Self-Flow (`work/self-flow-full`, now 22 slides, 1200 s): one overview after the encoder-scaling
slide, from a third codex/agy round (`work/self-flow-full/review/anim/log.md`) — REPA-style alignment
first, then the external encoder swapped for the model's EMA teacher with the alignment line
re-routed from the student's middle layer to the teacher's deep one, then the two inputs' noise
levels part; two questions. No "training only" label: App. A.3 evaluates the EMA copy. The related
work slide now asks what Fig. 2(a) answers; the teacher slide's notes attribute the "infer the
noisy tokens" explanation to the authors. Two agy visual rounds (`visual_anim_triage_r*.md`).
`animation.md` gains two rules: place the overview after the slide whose subject it takes apart,
and mark "training only" only where the paper says so.

Engine
- `animation` block: `figures/<name>.svg` (the finished picture: no script, PDF, overview grid) +
  `figures/<name>.anim.js` (`DeckAnim.define(name, (svg, lib) => ({beats, render}))`); beats share the
  stepper's `data-steps`, so the hash `#/n/k`, QA captures and PDF `expand` work unchanged. `side:
  "below"` puts one column per beat under a diagram that spans the slide.
- `lib`: `ramp`, `smooth`, `lerp`, `css`, `mix`, `along`, `set`, `node`, `fade` (opacity, and hidden at
  0 — the PDF check found a swapped-out label still in the text layer).
- A script that is missing, never defines, returns bad beats or throws in `render` gives the slide
  back as a static one (the SVG as drawn, every beat's text) instead of stalling the clicker.
- The overview grid keeps animations finished; a step past the end is clamped; M flips what is in
  effect (OS reduced motion included) and ignores key repeat; a number key moves a toggle's focus
  with its choice.
- Ids in an inlined animation SVG get a per-slide prefix (real `id` attributes and references to
  them only).

Gates and QA
- Build: ≤ 3 animations; one interaction per slide; 3–5 beats with titles; `reveals`, `print`,
  `provenance`; the script calls `DeckAnim.define(name)` and keeps no clock, reads no OS setting,
  listens for no input, writes no text, reaches no network (comments excluded); every `node("key")`
  is drawn in the SVG; one name, one pair of files.
- `qa_render.py`: every stop and the middle of every beat captured and measured
  (`sNN-beat<k>-mid.png`); a beat over 2.0 s fails; each stop and mid-beat time drawn after playing
  from 0 and after a jump must match (attributes compared in name order); an animation that did not
  bind fails.

Visual review (agy, two rounds on the captures, mid-beat frames included): 14 findings, then 3 new
ones from the fixes. Two of round 1's partial rejections were wrong and round 2 said why: the token
bars read as a dotted line because of their **height**, not their length (8 px high now; the 8 : 384
length ratio is the point and stays), and block names can swap in place **inside** the blocks as
well as under them. Lessons in `animation.md`: stagger a stack that grows and it reads as a funnel;
an arrowhead fading in with its line arrives before the line; a line that a later piece crosses is
cut into pieces so only the crossed piece fades (no seam).

Docs: `references/animation.md` (when, how it plays, files, writing one, techniques, QA);
`interaction-rules.md` (animation in the budget; "animation that plays by itself" stays out);
`block-vocabulary.md`, `qa-checklist.md`, SKILL.md; starter files in `assets/templates/`.

## 0.4.0 — 2026-11-25

Third paper: RAE (Diffusion Transformers with Representation Autoencoders, arXiv 2510.11690), a
20-minute, 21-slide seminar deck (`work/rae`) built on "two beliefs, refuted one at a time":
① semantic encoders cannot reconstruct, ② diffusion fails in high-dimensional latents. Signature
stepper: the gFID ladder as each fix is added (23.08 → 4.81 → 4.28 → 2.16, SD-VAE 7.13 drawn as
the baseline); Fig. 6a/6b as image tabs. Everything below was found by running it.

Process
- **The researcher was fenced off the web.** Given `--dir`, `delegate.py` appended "do not use the
  web" to every role, research included; the first research call answered "확인 못 함" five times.
  Research now always searches the web, and a folder is extra reading.
- A reviewer's correction of a curve reading was wrong again (Fig. 6a: it read a label's position
  as the point, 2.6 for ≈ 2.36). `narrative-roles.md`: corrections of curve readings are checked
  on the zoomed figure too.
- A reported ICLR acceptance could not be opened (OpenReview asked for a bot challenge) and was
  not used; two follow-ups by overlapping authors became discussion points.

Engine
- **Build gate: every stage character is in the bundled fonts** (fontTools; preflight reports it).
  ✓/✗ in a table fell back to Segoe UI Symbol and Noto Sans KR. Diagram SVG labels are checked too.
- **`^{sup}` in the inline syntax**: `DiT^{DH}-XL` renders as a superscript and never splits.
- A table column with `—` ("not reported") rows is still a number column (it aligned left beside a
  right-aligned gFID column).
- `valign: center` and statement slides centre with `safe center`: content taller than the body
  starts at the top instead of being pushed up under the title (slide 16, after Fig. 1 moved there).
- `build_deck.py`, `qa_render.py` print UTF-8 (Korean paths came out garbled on a cp949 console).

QA
- `overflow` now includes the side margins: a four-column table ran 94px into the right margin
  while staying on the stage, and passed. SVG children are left to the SVG viewport.
- PDF check: a text-shadow halo prints the same glyphs twice at one place; that copy is no longer
  reported as overlapping text.

Layout lessons (deck.json, not engine): two figures side by side at one `height` need split
columns in the ratio of their aspects, or one of them is held by its width; a tall figure in a
toggle is sized by its height, so the media column should be only as wide as the figure.

## 0.3.1 — 2026-11-24

- **Motion plays by default.** Opening the file with no address parameter used to follow the OS,
  and a presenter PC with Windows animation effects off showed no motion unless `?motion=1` was
  added. The build writes `meta.motion` (default `on`; `auto` follows the OS, `off` never
  animates) into `<html data-motion>`; `?motion=0|1|auto` in the address still wins.

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
from the official vector, two agy visual rounds on a 6-slide sample (`work/self-flow`, removed
from the repo after 0.4.0; the full Self-Flow run is `work/self-flow-full`).
