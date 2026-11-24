# QA checklist — which gate owns each check

A clean build is not a correct render. Three gates, in this order.

## 1. Build gates (`build_deck.py` refuses to write)

- every non-cover slide has `title`, `message`, `cite`, a `section` that exists
- `meta.presenter.name`; `meta.paper.authors` when `meta.paper` is present
- figure ledger (`meta.figures`): every entry exactly one of `use` / `cut`; a `use` slide cites it
- `provenance` on every `bars`, `table`, `deltas`, toggle state and stepper
- a delta's `pair` names rows or bars drawn on the same slide
- panels ≤ 2 per slide, none nested, none on dark slides, ≥ 40% of slides panel-free
- interactive slides ≤ ⌊N × 0.2⌋, at most one `signature`; each has `reveals`, `start`, `print`
- `note` blocks ≤ max(2, ⌈content slides / 4⌉)
- the last slide is an `ending`
- slide count = `meta.target_slides`; `time` sum within ±10% of `meta.target_minutes`
- every referenced file (figure, diagram, state image) exists

## 2. Mechanical gate (`qa_render.py`, run at 1920×1080 and 1024×768)

Per slide and per toggle state, in Chromium over `file://` with every non-file request blocked:

| key | fails when |
|---|---|
| `overflow` | anything leaves the 1920×1080 stage |
| `spill` | content leaves its band (a direct child of the slide) or two bands overlap — catches a figure pushing past its column, a caption touching the footer, buttons wrapping out |
| `collide` | two visible text lines (from different blocks), or text and an image, overlap anywhere — catches what `spill` cannot see inside one column (in the full run: a figure caption run over by the toggle caption because a flex item shrank) |
| `small` | any rendered text below 24 stage px |
| `clipped` | text cut by an `overflow:hidden` ancestor |
| `contrast` | HTML text below 4.5:1 against its rendered background |
| `titleWrap` | a slide title on more than one line |
| faces | a glyph drawn in a fallback font (only Geomini / Gmarket Sans pass) |
| console, external, failed | a script error, a network request, a missing file |
| burst | six PageDowns 60ms apart do not land on one finished slide |

Run it on `deck/` while iterating and on the bundled `<slug>.html` (copied alone) before delivery.
Fix upstream (deck.json or the engine), never by raising a threshold.

## 2b. PDF render check (`export_pdf.py`)

The HTML is the deliverable; the PDF only proves the deck survives printing. Every figure is frozen
at its screen size before each page prints, then each page is read back: text lines from different
blocks must not overlap, no line may cross the footer's progress bar, nothing beyond the page edge.

## 3. Visual gate (agy, `delegate.py vision`; the current AI when agy is missing — say so)

Send the captures of both viewports, the rules, and a short brief of what changed. Ask for what
only the eye sees, by severity (P0 misreads / P1 visible defect / P2 polish), with 1920
coordinates and a concrete fix. Run a second round on the fixed captures with the first round's
findings and triage attached — round 2 checks the fixes and the regressions they caused
(in the sample run: a changed label also renamed a table header, `FID ↓ ↓`).

Look for:
- hierarchy: what the eye lands on first; message → evidence in that order
- alignment and rhythm across slides: left edge, column tops, gaps; empty or crowded regions
- consistency: captions start with `**Fig. n**` + a space, deltas against the same baseline, one
  arrow convention, the same block looks the same everywhere
- 1024×768 legibility: table numbers, bar labels, axis labels and legends inside paper figures,
  second-level subscripts
- dark slides on a projector: unfinished progress segments, badge borders
- Korean line breaks: a word split mid-syllable, one-word orphans, a number split from its unit
  (fix with U+00A0, not by shrinking)

## Delivery

Report: the files (`deck/index.html`, `deck/script.html`, `deck.pdf`), slide count and planned
time, the figures and tables taken from the paper, QA status at both viewports, who filled each
role and every fallback, and what was not done.
