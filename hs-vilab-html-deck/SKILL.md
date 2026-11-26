---
name: hs-vilab-html-deck
description: >
  Turn an AI/CV paper into a finished 한성대/VILAB presentation as an HTML deck — a 1920×1080
  stage that runs from file:// with a clicker, a speaker script page and a vector PDF. Use when
  the user gives a paper (PDF, arXiv id or link) and wants slides, a deck, a presentation,
  발표자료 or a 논문 리뷰/세미나 발표 as HTML (or "PPT 대신"). Runs a narrative team (codex
  drafts, agy critiques, verifies and researches), builds, measures every slide in Chromium,
  has agy review the captures, and revises. Works without other skills installed.
---

# hs-vilab-html-deck

**Version: see `VERSION`.** `CHANGELOG.md` says what changed and why.

A paper becomes a deck in stages; each stage reads a file and writes a file. `$S` is this skill's
directory, `$W` is `work/<slug>/`.

```
[−1] intake        paper -> $W/source/paper.pdf, paper.txt, figlist.txt
[0]  ask (≤4)      the only place the user is consulted
[0.5] preflight    blocking
[1]  narrative     codex draft -> agy critic + agy verifier (blind) + agy research
                   -> log.md -> codex revision -> gate -> deck.json (you)
                   -> Korean editor -> verifier again on deck.json
[2]  render        figure crops, diagrams -> build_deck.py -> deck/ + <slug>.html, <slug>-script.html
[3]  QA            qa_render.py at 1920×1080 and 1024×768 -> agy visual review
[4]  revise        deck.json (or the engine) -> back to [2]; visual round 2
[5]  deliver       <slug>.html (self-contained, written by the build) ; PDF render check
```

Design follows `references/design-system-deck.md` (from hs-vilab-frontend-design); content and
production follow `references/narrative-rules.md` (from hs-vilab-deck). Both are bundled — this
skill calls no other skill.

## [−1] Intake

```bash
mkdir -p $W/source $W/review $W/deck/assets/fig $W/figures
cp <paper.pdf> $W/source/paper.pdf
python $S/scripts/extract_figures.py $W/source/paper.pdf text -o $W/source/paper.txt
python $S/scripts/extract_figures.py $W/source/paper.pdf list > $W/source/figlist.txt
```

`paper.txt` breaks table rows: check every number against the rendered page.
`source/` and `brief*.md` hold the paper's text and stay out of version control.

## [0] Ask first, then do not interrupt again

Read the abstract, contributions and figure list first: the questions come from the paper, not
from a form. Ask once, in one go (one `AskUserQuestion` call), at most four questions; after that
the pipeline runs to completion without checking in. (Same four as hs-vilab-deck.)

**Q0. 발표 시간이 몇 분입니까?** Derive the slide count; do not ask for it.
`slides = minutes × 1.0–1.5` — nearer 1.0 when the paper is equation- or algorithm-heavy, nearer
1.5 for concept- and result-driven work. Sets `meta.target_minutes` (the script is timed against
it) and `meta.target_slides` (a build gate).

**Q-자리. 어디서, 누구에게, 발표 후 무엇을 기대하는 발표입니까?** Lab seminar (discuss and
critique), class (understand), conference (remember one result), committee (judge). This decides
the ending — a seminar closes on discussion points grounded in the paper. When the paper makes
several claims of similar weight, name them from the paper and offer the leading thread inside
this question. Sets `meta.occasion`.

**Q2. 언어 — 본문과 제목을 각각 어떻게 할까요?** Body `en` or `ko+en` (`meta.lang`), titles `ko`
or `en` (`meta.titleLang`). Korean titles keep technical terms in English. Default `ko+en`, `ko`.

**Q-작업. 작업 방식 (복수 선택)** — four boxes, each one setting:

| box | checked | unchecked |
|---|---|---|
| 개요 초안을 codex에 | codex writes `outline.md` and its revision | an author subagent writes them |
| 자료조사를 agy에 | the researcher runs (step [1].2–3) | no research; the deck says only what the paper says |
| 시각 검수를 agy에 | agy reviews the captures ([3]) | you review the captures yourself |
| 2차 검수 | a second visual round after the fixes ([4]) | one round of [3]–[4] |

Critic and verifier always run, blind to each other (agy, or subagents when agy is missing).
Which AI fills which role is fixed (table below), not asked. The presenter (`meta.presenter`) is
not a question: reuse the last deck's, and ask only if there is none.

Nobody to ask, or the user says go: 20-minute lab seminar, `ko+en` body, `ko` titles, all four
boxes — stated in one line.

## [0.5] Preflight

```bash
python $S/scripts/preflight.py --strict
python $S/scripts/delegate.py which
```

Python 3.10+, PyMuPDF, Pillow, Playwright + Chromium, LaTeX + dvisvgm + arev (math has one render
path, no fallback), bundled fonts; codex and agy are optional — a missing one means that role
falls back (`delegate.py` says so) and the delivery names it.

## [1] Narrative — a team, one output

Read `references/narrative-rules.md` and `references/narrative-roles.md` first. **You conduct; you
do not draft, and nobody reviews their own work.**

| role | delegate |
|---|---|
| author (draft, one revision) | codex — `delegate.py text` |
| critic · verifier (blind to each other) · researcher | agy — `delegate.py review` / `research` |
| Korean editor | codex with the anti-slop rules (`references/korean-style.md`) |
| visual reviewer | agy — `delegate.py vision` |

1. **Draft.** Build `$W/brief.md` from `references/handoff-narrative.md` with `paper.txt` inline;
   `delegate.py text --prompt-file $W/brief.md --dir $W/source --out $W/outline.md`.
2. **Review.** Put `outline.md`, `paper.txt`, `paper.pdf` and `references/narrative-rules.md` in
   `$W/review/ref/`; run critic and verifier as two separate agy calls on that folder, and the
   researcher on 3–6 specific questions taken from the draft (`delegate.py research`: it searches
   the web; a `--dir` is extra reading, never a fence).
3. **Check research at the source** → `review/research_verified.md` (fact, URL, what disagreed).
   Only that file feeds a slide, marked `external`.
4. **Answer every finding** in `review/log.md`; end it with the target slide list.
5. **Revise once** with codex (`narrative-roles.md` step 5), then **gate** the revision:
   - titles in order read as a table of contents; each introduces, none concludes; one line
   - one message per slide; TL;DR second; no two slides make the same point
   - every main-body figure and table in the ledger, `use` or `cut` with a reason
   - no claim, number or causal link absent from the paper; every number with its condition
   - the paper's limits and conditions present; a seminar ends on discussion points found in the
     paper (evidence and cost kinds, interpretation marked)
   - slide count and per-slide `time` match the talk
   - the deck ends on an `ending` slide (감사합니다 / Q&A, presenter, a few links)
6. **Synthesise `deck.json`** — blocks (`references/block-vocabulary.md`), copy, `notes` (spoken
   script, 합쇼체, `[n]` toggle cues), `provenance` for every claim (`verbatim`, `derived`,
   `interpretation`, `external`), the figure ledger in `meta.figures`. Interactions per
   `references/interaction-rules.md`. Before the first research section, 1–3 **overview
   animations** (`references/animation.md`): the paper's machinery as one diagram that changes
   shape, one beat per clicker press — what a PDF cannot show. Adding 1–2 slides for them is fine
   (keep the total time); replace a slide only when the animation says what it said. They count in
   the interaction budget.
7. **Korean editor** (`references/korean-style.md`), applied with `apply_text_edits.py`.
8. **Verifier again on `deck.json`** — answer it in `review/log.md`, fix `deck.json`.

## [2] Render

```bash
# paper figures: crop the REGION at 400 dpi (axes, legend), caption left out
python $S/scripts/extract_figures.py $W/source/paper.pdf crop --page 3 --bbox 307,66,422,181 \
       --name fig2a -o $W/deck/assets/fig --dpi 400
python $S/scripts/build_deck.py $W          # gates first; writes nothing if any fails
```

Locate a vector figure's bbox by rendering the page (`pymupdf` at 144 dpi: pt = px / 2). Diagrams
you draw go in `$W/figures/*.svg` (token colours via CSS variables, `role="img"`, `<title>`; math
through `<foreignObject>` with `$…$`). An illustration re-drawn from a paper figure says so in its
caption. Equations are TeX in `deck.json`; the build renders them (`make_equations.py`, cached in
`deck/assets/math`).

A diagram's `viewBox` width is about the width it is shown at (a 3:2 stepper: 1000), so its 24px
labels stay at or above the floor; QA reports a label that runs past its `<foreignObject>`. An image
never grows past its own pixel width: a figure shown wider than about 1000 stage px (a chart across
the slide, one class of a sample grid as image tabs) is cut at 800 dpi, or it sits small in a white
mat. When you re-assemble part of a figure, keep the paper's row and column labels, give the
parts of one toggle the same aspect, and say so in the caption.

An animation is two files beside it: `figures/<name>.svg` draws the finished picture (the last
beat — what prints and what stays without script) and `figures/<name>.anim.js` moves its
`data-anim` elements from t alone (`references/animation.md`). Write the storyboard at the top of
the script before any coordinates.

**The build refuses while any gate fails** (`references/qa-checklist.md` §1). The fix is upstream —
cut a line, change the block, split the slide. Never shrink type, never raise a threshold.

## [3] QA — mechanical first, then the eye

```bash
python $S/scripts/qa_render.py $W                       # -> $W/qa/s<NN>[-state].png, scan.json
python $S/scripts/qa_render.py $W --viewport 1024x768   # projector
```

Both must print `QA: no mechanical defects`. Then look at every capture yourself — for an
animation also the mid-beat captures (`sNN-beat<k>-mid.png`): QA does not compare SVG labels with
each other — and send the captures of both viewports with the rules to agy:

```bash
python $S/scripts/delegate.py vision --prompt-file $W/review/visual_brief.md --dir <bundle> --out $W/review/visual_r1.md
```

The bundle holds `shots/1920`, `shots/1024`, `rules/` (`design-system-deck.md`,
`block-vocabulary.md`), `deck.css`, `deck.json`, and the brief: what changed, what is settled and
not to be re-argued, what to look for (`qa-checklist.md` §3), output format (ID · slide · P0/P1/P2 ·
what is seen at 1920 coordinates · why · concrete fix). Triage every finding into
`review/visual_triage_r1.md`: adopted, partly, rejected with the reason.

## [4] Revise

Edit `deck.json` — or the engine, when a defect would recur on any deck (alignment, a gate, a
fit rule): those fixes are the point of running this skill. Rebuild, re-run both QA passes, then a
**second visual round** with round 1's findings and triage attached: it checks the fixes and finds
the regressions they caused.

## [5] Deliver — the HTML is the final version

The build writes the deliverable itself: **`$W/<slug>.html`**, one self-contained file at the top of
the work folder (fonts, styles, engine, figures and brand marks inlined; large figures re-encoded
as WebP). It opens from a mail attachment or a USB stick with nothing next to it and no network.
`$W/<slug>-script.html` is the speaker script, the same way — printable, never on the stage.
`deck/` is the build's working copy (QA reads it); do not hand it out.

Run QA on the delivered file too, copied alone into an empty folder:

```bash
python $S/scripts/qa_render.py $W --html <empty-dir>/<slug>.html
python $S/scripts/qa_render.py $W --html <empty-dir>/<slug>.html --viewport 1024x768
```

The PDF is not a version of the deck; it only checks that the deck still renders when it is
printed for distribution:

```bash
python $S/scripts/export_pdf.py $W     # deck.pdf, toggle states expanded (6a, 6b, …), then a page check
```

It must end with `PDF check: no overlapping text`. Chromium's paginated layout once grew fitted
figures and pushed their captions over the footer on five pages while the screen was clean;
`export_pdf.py` now freezes every figure at its screen size before printing and checks each page
for overlapping lines and text crossing the progress bar.

Keys: PageDown/→/Space, PageUp/←, Home/End, 1–9 toggle state, G overview, F fullscreen, M motion off/on,
`?notes=1` rehearsal notes, `?motion=0` no motion (motion is on by default — `meta.motion`). Report only:

1. the file — `<slug>.html` (and `<slug>-script.html`); the PDF only if asked for
2. slide count and planned time
3. the figures and tables taken from the paper
4. QA status at 1920×1080 and 1024×768 on the delivered file, the PDF check, the visual rounds
5. who filled each role, and every fallback to a subagent or to you
6. what was not done

## References

| file | read it when |
|---|---|
| `references/narrative-rules.md` | before [1] — structure, titles, sourcing, style |
| `references/narrative-roles.md` | before [1] — the team, the loop, each reviewer's brief |
| `references/handoff-narrative.md` | building `brief.md` for codex |
| `references/korean-style.md` | the Korean editor pass |
| `references/block-vocabulary.md` | writing `deck.json` |
| `references/interaction-rules.md` | before adding a toggle, stepper or animation |
| `references/animation.md` | writing an animation: storyboard, `render(t)`, the library, design rules, QA |
| `references/design-system-deck.md` | the design authority on the stage |
| `references/qa-checklist.md` | before [3] — every gate and who owns it |
| `assets/engine/deck.css`, `deck.js` | the stage engine — change it when a defect is general |
