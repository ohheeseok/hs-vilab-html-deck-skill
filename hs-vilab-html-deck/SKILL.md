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
[2]  render        figure crops, diagrams -> build_deck.py -> deck/index.html, script.html
[3]  QA            qa_render.py at 1920×1080 and 1024×768 -> agy visual review
[4]  revise        deck.json (or the engine) -> back to [2]; visual round 2
[5]  export        export_pdf.py -> deck.pdf ; delivery report
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

## [0] Ask once, at most four questions

Read the abstract, contributions and figure list first. Then ask, in one message:

1. **발표 시간** — slides = minutes × 1.0–1.5 (nearer 1.0 for equation-heavy papers). Sets
   `meta.target_minutes`, `meta.target_slides`.
2. **자리와 기대** — lab seminar (discuss, critique), class, conference, committee. Sets
   `meta.occasion` and the ending. Offer the leading thread when the paper has several claims.
3. **언어** — body `ko+en` or `en`, titles `ko` or `en`.
4. **발표자** — name and affiliation for the cover (`meta.presenter`), event and date.

Nobody to ask, or the user says go: a 20-minute lab seminar, `ko+en` body, `ko` titles — said in
one line. Who does which pass is not asked; it is fixed below.

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
   researcher on 3–6 specific questions taken from the draft.
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
6. **Synthesise `deck.json`** — blocks (`references/block-vocabulary.md`), copy, `notes` (spoken
   script, 합쇼체, `[n]` toggle cues), `provenance` for every claim (`verbatim`, `derived`,
   `interpretation`, `external`), the figure ledger in `meta.figures`. Interactions per
   `references/interaction-rules.md`.
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

**The build refuses while any gate fails** (`references/qa-checklist.md` §1). The fix is upstream —
cut a line, change the block, split the slide. Never shrink type, never raise a threshold.

## [3] QA — mechanical first, then the eye

```bash
python $S/scripts/qa_render.py $W                       # -> $W/qa/s<NN>[-state].png, scan.json
python $S/scripts/qa_render.py $W --viewport 1024x768   # projector
```

Both must print `QA: no mechanical defects`. Then look at every capture yourself, and send the
captures of both viewports with the rules to agy:

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

## [5] Export and deliver

```bash
python $S/scripts/export_pdf.py $W     # deck.pdf: one page per slide, toggle states expanded (6a, 6b, …)
```

`deck/` is the deliverable folder: `index.html` (present; keys: PageDown/→/Space, PageUp/←,
Home/End, 1–9 toggle state, G overview, F fullscreen, `?notes=1` rehearsal notes), `script.html`
(the speaker script, printable — never on the stage). Report only:

1. the files — `deck/index.html`, `deck/script.html`, `deck.pdf`
2. slide count and planned time
3. the figures and tables taken from the paper
4. QA status at 1920×1080 and 1024×768, and the visual rounds
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
| `references/interaction-rules.md` | before adding a toggle or stepper |
| `references/design-system-deck.md` | the design authority on the stage |
| `references/qa-checklist.md` | before [3] — every gate and who owns it |
| `assets/engine/deck.css`, `deck.js` | the stage engine — change it when a defect is general |
