# Block vocabulary — what goes in `slides[].body`

The stage is 1920×1080. Every block below is rendered by `scripts/build_deck.py` into HTML and
measured by `scripts/qa_render.py` in Chromium — what QA checks is what the room will see, not an
estimate. Pick a block by what the content **is**; three consecutive slides built from the same
single block read as a template.

Type ladder (stage px): 80 cover title · 56 slide title · 48 key message (`lead`) · 40 · 36 · 32
body · 28 table/secondary · 24 caption, the floor. **Nothing below 24px** — the fix for content
that does not fit is to cut, split or re-layout, never to shrink.

## Slide fields

| field | | |
|---|---|---|
| `id` | required | short slug, used in QA file names |
| `layout` | `content` (default) · `cover` · `statement` · `ending` | statement = TL;DR and discussion, dark when `meta.statementTheme` is `dark` |
| `section` | required except cover | an id from `meta.sections`; drives the footer progress bar |
| `title` | required | introduces the slide; one line (QA fails a wrap) |
| `message` | required except cover | the one key sentence; spoken, not printed on the slide |
| `cite` | required except cover | paper locations: `"Fig. 3"`, `"Table 1"`, `"Sec. 4.1"`, `"App. B"` |
| `tone` | `wash` | grey ground for slides whose evidence is a chart or table drawn by the build |
| `valign` | `center` | a sparse slide (a short table, an equation, two cards) sits on the optical centre instead of the top; a `split` keeps its content height |
| `time` | seconds | summed against `meta.target_minutes` (build gate ±10%) |
| `notes` | list of strings | the spoken script, 합쇼체; `[1]` `[2]` mark toggle-state cues |
| `provenance` | object | claim → `verbatim` / `derived` / `interpretation` / `external` + where |

Ending (the last slide, required by the build): `layout: "ending"`, `title` (default 감사합니다),
`subtitle` (default Q&A), `links` (a few short lines: paper, code). Presenter and signature come from
`meta.presenter` (an optional `contact` line); no footer, no section, no message.

Cover: `title`, `subtitle`, `figure` (`src`, `alt`, `caption`). The presenter block comes from
`meta.presenter`, the small paper credit from `meta.paper` — `authors`, `affiliations`, `venue`, and
`authorNote` saying what an asterisk marks (`* 공동 1저자`, `* 공동 지도`; the build refuses `*` without it) (omit it, or set `meta.coverCredit:
false`, for your own work).

## Blocks

| type | use when | fields | notes |
|---|---|---|---|
| `lead` | one sentence opens or closes the slide | `text`, `size: "sm"` | 48px (40 with `sm`) |
| `bullets` | plain enumeration, 3–5 items | `items`, `numbered`, `size` | an item may be `{"text", "note": true}` → 해석 label |
| `groups` | items under 2–3 short headings | `groups[{heading, items, numbered}]`, `columns`, `divider` | `divider` draws a rule between columns |
| `compare` | two (or three) approaches side by side | `items[{heading, items}]` | groups + divider |
| `cards` | two to four parallel things | `items[{title, text}]`, `numbered`, `columns` | ruled columns, **not boxes** |
| `callout` | the one thing to look at | `text` | at most one per slide |
| `note` | the deck author's reading, not the paper's | `text` | ≤ max(2, ⌈content slides / 4⌉) per deck (gate) |
| `caption` | condition line under a figure/table | `text` | starts with `**Fig. n**` / `**Table n**` |
| `deltas` | change against ONE named baseline | `items[{value, label, small, pair}]`, `provenance` | one big number per metric; `pair` names two rows drawn on the slide → hover/focus marks them (gate checks they exist) |
| `bars` | one metric across ≥ 4 models | `title`, `metric`, `better`, `items[{label, sub, value, focus}]`, `provenance` | SVG drawn by the build, sorted best first, `focus` = the paper's model |
| `table` | several metrics | `columns[{label, dir, align}]`, `groups[{label, rows[{cells, focus}]}]`, `provenance` | `**x**` = best; number columns align right, word columns left (auto); `focus` row tinted |
| `figure` | a paper figure | `src`, `alt`, `caption`, `height` | crop the REGION (axes, legend) at 400 dpi with `extract_figures.py`; caption written by the slide. With `height` the figure keeps that size (it does not shrink) |
| `figureNumbered` | a complex figure needing pointers | `src`, `marks[{x, y}]` (0–1), `items` | one item per mark |
| `diagram` | a figure we redraw as SVG | `svg` (path under the work dir), `caption` | token colours, `role="img"` + `<title>`; math in `<foreignObject>` via `$…$` |
| `equation` | an equation carries the slide | `lines` (TeX), `tags`, `symbols[[sym, meaning]]` | TeX → dvisvgm → inline SVG, Arev Sans |
| `process` | an ordered procedure, 3–5 steps | `steps[{title, text}]`, `direction: "vertical"` | numbered, joined by arrows |
| `split` | two columns | `cols: [a, b]`, `left`, `right` | the default layout tool; vary the ratio |
| `panel` | a bounded region | `body`, `heading`, `size: "sm"` | ≤ 2 per slide, none on dark slides, ≥ 40% of slides panel-free (gates) |
| `toggle` | compare states of one figure (see `interaction-rules.md`) | `states`, `start`, `print`, `reveals`, `svg` or per-state `src`, `side`, `mediaCaption`, `caption`, `panel`, `cols`, `signature` | `mediaCaption` sits under the visual, `caption` at the foot of the readout column |
| `stepper` | an ordered reveal of one diagram | `svg`, `steps[{title, text}]`, `print`, `reveals`, `provenance` | elements carry `data-from-step="k"` |

## Inline syntax (any text field)

`**bold**`, `$TeX$` (inline math, rendered at build time), `_{sub}`; hyphenated names
(`Self-Flow`, `SiT-XL/2`) never break, a Korean particle stays on the math before it
(`$\ell_1$에서`), and a count stays with its unit (`1M step`, `50 ODE steps`). Use U+00A0 to keep a short phrase on one line
(`DINOv2 feature`) and U+2007 (figure space) to align a decimal in a table column. The build also keeps
`Fig. 3`, `Table 4`, `FID 5.30`, `= 9.6` and `$k$ = 10개로` on one line.

## Choosing, with the Self-Flow deck as the example

- Background with several methods → a `table` of what each aligns to what (slide 3), not cards.
- One metric, five models → `bars` + a `panel` of `deltas` against the strongest baseline (10).
- Several metrics, two baselines → `table` with `focus` rows + `deltas` panel (9).
- Two modalities with different metrics → two tables in a `split` (11), not one merged table.
- A derived table (Δ per weighting) is fine when every cell is `derived` from printed values (12).
- A paper figure plus its reading → `split` with `figure` and `compare`/`bullets` (13, 16–18).
- Limits → `groups` in three ruled columns (19). Discussion → `statement` with numbered questions (20).
