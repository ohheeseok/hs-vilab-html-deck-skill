# Narrative rules

Copied from `hs-vilab-deck` (the PowerPoint skill, same lab, same author) because the content rules
do not depend on the medium. **Where the HTML deck differs, this box wins over the text below it.**

| PowerPoint text below says | In the HTML deck |
|---|---|
| section in each slide's `eyebrow` (`RESULTS · T2I`) | **no eyebrows** (the design system bans them). Each slide has a `section`; the footer progress bar shows the section names and where the talk is. Section dividers are not used at any length. |
| title "one line, beside its eyebrow" | one line, measured: `qa_render.py` fails a wrapping title. Korean ≈ 22–26 characters. |
| `metrics`, `delta`, `highlight` | `deltas` (one big number per metric, signed, `derived`), table/bar row `focus` |
| `note` at most one per four content slides | same, counted on `note` blocks by the build; an item can also carry `"note": true` (the 해석 label) |
| `cards` with an accent stripe, `callout` as a filled box | `cards` are ruled columns, `callout` is large bold text; the only filled surface is a `panel` (≤ 2 per slide, ≥ 40% of slides without one) |
| `notes` fields (`symbols`, `derivation`, …) and `script.docx` | `notes` is a list of spoken paragraphs (합쇼체); `[1]`, `[2]` mark where to press a toggle state. The build writes `deck/script.html`. |
| one dark navy statement slide | `layout: "statement"` (TL;DR, discussion) renders dark when `meta.statementTheme` is `dark` |
| `wash` tone for the results stretch | `tone: "wash"` on slides whose evidence is a chart or table drawn by the build |

Interactions (toggle, stepper) are an HTML-only addition: `interaction-rules.md`.

---


Read before stage [1]. This is what the deck is allowed to say and how it is
allowed to say it. The design frame is not negotiable and neither is this.

---

## 0. Who the talk is for — decide before the outline

[0.7.0] A deck of the MMaDA paper built under the Slides artifact type was
judged better than ours, and the decisive differences were not design. It
opened with a TL;DR and closed on four discussion questions — reward hacking,
an abstract that contradicts its own table, a speed claim with no wall-clock
measurement, and how the method could apply to the lab's own work. It did
that because it knew the occasion: a lab seminar. Ours knew only the length.

So the occasion is part of the brief, and the questions about it come from
the paper, not from a form:

- **Where is it given, and what should the room do afterwards?** Lab seminar
  → discuss and critique; class → understand; conference → remember one
  result; committee → judge. This decides the ending.
- **What leads?** When a paper makes three claims of similar weight, ask which
  one the talk is about — and name the three, from the paper.

If nobody can be asked, default to a lab seminar (this skill's usual case)
and say so in one line.

## 1. Structure

Default order, adjusted to the paper rather than forced onto it:

> cover → **TL;DR** → problem and the gap → background needed → method →
> results → analysis → limits → **takeaways and discussion** → closing

- **TL;DR comes second, always.** A `statement` slide: one sentence saying
  what the paper does, and a card row of its two to four contributions. The
  room should know where the talk is going before it starts going there.
- **Background names the landscape, then asks the talk's question.** [0.7.2]
  One slide, before the problem: the lines of work the paper sits between,
  each with its representative models **by name, from the paper's own related
  work** (understanding: LLaVA-style encoder→LLM; generation: diffusion and
  AR; unified: external-diffusion vs single-transformer — whatever the paper
  draws), and a last line that is the question the talk will answer. The
  Slides-artifact deck of Janus did this in one slide; ours had squeezed it
  into a three-row table beside the problem, and the room never saw where the
  paper stood. Problem and background are separate slides from 15 minutes up.
- **The ending fits the occasion.** For a seminar, a `statement` slide with
  takeaways beside three or four discussion points. Each point is grounded in
  the paper, and comes from one of two kinds:
  - **evidence** — an inconsistency between its own sections, a claim it
    does not measure, a metric it both optimises and reports, an ablation it
    does not run;
  - **consequence** [0.7.2] — what the design costs that the paper does not
    discuss, derived from its own description (Janus keeps two image
    representations, so an image it generates must be re-encoded by SigLIP
    before the model can understand it). Marked as interpretation.
  Mix the two; four evidence points in a row read as an audit. "How would this
  apply to our work" belongs there only when the user has said what their
  work is.
- **Section dividers only for long talks.** At 30 minutes and up they earn
  their slide. Below that, the section lives in each slide's `eyebrow` —
  `STAGE 1 · PRETRAINING`, `RESULTS · T2I` — at no cost in slides.
- **Results get the `wash` tone** for as long as the evidence lasts, so the
  room can see where the argument ends and the evidence begins.

A stage the paper does not have is skipped, not invented.

**One key message per slide.** `message` in the IR is that sentence, and the
build refuses a content slide without one.

### Titles

[0.7.0] The old rule — "the titles are the argument" — produced titles that
deliver the verdict: *Text-to-Image: Best on CLIP, ImageReward, WISE and GenEval
Overall*. That is the speaker's punchline written on the slide, and the Slides
type's craft guide names it as a tell of generated decks.

- **A title introduces the slide.** Either a short topic (`통합 멀티모달 모델의
  설계 공간`) or a topic and a short claim (`멀티모달 이해: 통합 모델 중
  최상위권`). One grammar for the whole deck.
- **One line, beside its eyebrow.** The build measures it and refuses a title
  that wraps; it is never shrunk. In Korean that is roughly 22–26 characters.
- **No dramatic construction.** No "X가 아니라 Y", no "…, Not Y", no "But…",
  no faux-insight titles.
- **Language** follows `meta.titleLang` (`ko` | `en`). Korean titles keep proper
  nouns and technical terms in English (`UniGRPO`, `discrete diffusion`).

Read the titles in order with nothing else. The talk should still follow — as a
table of contents, not as a list of conclusions.

### The figure ledger

[0.7.0] The MMaDA deck dropped the paper's Figure 1 — its hero qualitative
figure, the one an audience remembers — and no step noticed, because "do not
omit a figure that carries the argument" was left to judgement.

`meta.figures` lists **every** figure and table in the main body — and any
appendix figure the deck uses, which is then ledgered like the rest (Janus's
Fig. 6, in Appendix A, is the only picture of the ablation's baseline):
`{ "ref": "Fig. 1", "use": 14 }` or `{ "ref": "Fig. 5", "cut": "<reason>" }`.
The build refuses a deck without it, an entry with neither, an entry whose
slide never cites the figure, and — [0.7.1] — a "use" on a slide that cites a
figure but shows none (a figure there needs an image block; a table needs a
table, `bars`, `delta`, `metrics` or an image of it). Cutting is allowed; not deciding is not.

Figure 1 of an ML paper is usually the teaser — read it first and cut it only
with a reason you could say out loud.

### Concrete, on the slide

The lab's brief asks for worked numbers in the **script**. The slides need
concreteness too, and the deck that read better had it everywhere:

- **Method slides carry facts, not only the abstraction.** Beside the loss,
  the tokenizer, the codebook size, the token count, the schedule, the data —
  whatever the paper states that makes the method a thing someone built.
- **Use the paper's own examples.** If the paper shows the actual output of
  two variants (a one-sentence answer against a detailed one), show that, not
  a list of their settings.
- **Against one baseline, show the change.** When the honest comparison is
  "the same backbone, before and after", a `delta` row (`ARC-C +9.5`,
  `TruthfulQA −3.3`) says it at a glance. The values are `derived` provenance.
- **One metric across many models is a chart.** [0.7.2] Four or more models
  on one number (GenEval Overall over a dozen models) is a `bars` block —
  sorted, the paper's model in the focus colour, the others grouped (e.g.
  generation-only vs unified). A table is for several metrics at once.
- **One big number, one metric.** [0.7.2] A `metrics` value or `delta` tile
  states exactly one metric on one comparison. The artifact deck put "+41%"
  over "MME 948→1338, GQA 48.7→59.1" — the 41% is MME's; GQA's is 21%.
- **A qualitative figure gets read for the room.** Name what each example
  shows (`기하 문제 — 비교 모델은 52°로 오답, MMaDA는 38°`), beside the figure.

### Less text, more structure

- Parallel items are a `cards` row, not bullets in columns.
- Comparisons are a `table`; the row the talk is about is `highlight`ed.
- A headline number is `metrics`; a change against a baseline is `delta`.
- The one thing to look at on a slide is a `callout` — at most one per slide.
- `note` is for marking **interpretation** and nothing else, at most one per
  four content slides (the build counts). A left-barred aside on every other
  slide is not emphasis, and Anthropic's shared content rules name that shape
  as an AI-slop trope.
- A slide whose body still looks thin after the build spreads it is thin —
  add the paper's concrete facts, or merge it with its neighbour. Do not pad.

The script carries the explanation; the slide carries the structure. If a
slide reads like the script, the script is on the slide.

---

## 2. Sourcing — how "no invented numbers" is enforced

Every claim on a slide gets a `provenance` entry:

| `kind` | Means | On the slide |
|---|---|---|
| `verbatim` | the paper's own words or numbers | plain |
| `derived` | computed from the paper's numbers | plain, with the basis stated |
| `interpretation` | the deck author's reading | **marked** — a `note` block |
| `external` | from outside the paper | **attributed** to its source |

Rules that follow from this:

- Numbers carry their comparison, condition, unit and setting. `28.4 BLEU` alone
  is not a result; `28.4 BLEU, newstest2014, single model` is. The `metrics`
  block warns when a figure has no condition, because a bare number is the most
  common way a deck overstates a paper.
- A result that holds under specific conditions is never phrased as a general
  conclusion.
- Causal links that the paper does not make are not made here.
- The paper's own limits, applicability conditions and counterexamples appear in
  the deck. A deck that omits them is not a shorter version of the paper.
- Where the paper is genuinely ambiguous, do not resolve it. Put the ambiguity in
  the script as a caution.

Every content slide carries a `cite` — page, figure or table number. The build
refuses without it.

---

## 3. Style gate

The lab's brief makes this mandatory at synthesis time, so it is a pass/fail
check on `deck.json` (the Korean editor, `SKILL.md` 1d), not a polish step
afterwards.

### 명사형·개조식
Slide text ends in noun form or bulleted phrases, not full-sentence verbs.
The **script** is different — it is spoken prose and reads as speech.

### AI slop — do not write these

Padding verbs and adjectives with no content:
> ~을 활용하여 · ~을 통해 · 혁신적인 · 강력한 · 효과적으로 · 다양한 ·
> 핵심적인 역할을 한다 · 중요한 의미를 가진다 · 주목할 만한

Empty connective moves:
> 이는 곧 ~을 의미한다 · ~라고 할 수 있다 · 결론적으로 말하면 ·
> 살펴보면 다음과 같다 · 크게 세 가지로 나눌 수 있다 (when there are not
> naturally three)

Structural tics:
- three items because three feels complete, rather than because there are three
- a rhetorical question the paper never asks
- restating the slide title as the first bullet
- the mirrored pair ("단순히 X가 아니라 Y이다") used for rhythm
- an adjective the paper did not earn ("놀라운", "압도적인")

English equivalents count: *leverage, robust, seamless, delve into, it is worth
noting that, plays a crucial role*.

### The Korean editor — `korean-style.md`

[0.7.2] After synthesis, every Korean string in the deck — titles, messages,
block text, captions, and the speaker script — goes through the **Korean
editor** role (`narrative-roles.md`) with `references/korean-style.md`: this
skill's own rules (no coined labels, who does what, summary and discussion
items as sentences, slide references that follow the slides) and, condensed
for decks, the rules of `heeseok-korean-anti-slop` 1.3.0 (fake contrast,
"함께 봅니다" with no purpose, decorated abstractions, demonstratives with no
referent, stock noun phrases, importance announcements, vague "~에 가깝다",
reflex three-item lists; its L1–L3 layers). Both the rules and the scanner
(`scripts/scan_slop.py`) are bundled; no other skill is needed. The editor works on
the output of `scripts/deck_text.py` and returns a table — location, original,
edit, rule — and the conductor applies it to `deck.json`; numbers, names,
hedges and the claim's strength never change.

### Terminology
One term per concept for the whole deck. If the paper says *self-attention*, the
deck says *self-attention* on every slide — never alternating with *어텐션 기법*
for variety. Variety in terminology is a defect, not style.

### Language (Q2)

Two settings, chosen separately:

- **Slide body** — `en`, or `ko+en` (Korean explanation, English proper nouns
  and technical terms).
- **Titles** — `meta.titleLang`: `ko` or `en`. [0.7.0] Korean titles were
  chosen for the MMaDA comparison and read more naturally to a Korean room;
  they keep technical terms in English (`UniGRPO: diffusion을 위한 policy
  gradient`).

In-figure text is always the figure's own. The script is Korean unless the
user says otherwise.

---

## 4. What goes in the script instead

Anything that cannot be said in the time the slide is on screen. The script is
not a summary of the slide — it is what a presenter who does not know this paper
reads in order to understand it and then explain it.

Per slide, only the fields that slide actually needs
(`schema/deck.schema.json` → `notes`):

background · point_first · figure_order · figure_key · symbols · derivation ·
algorithm · script · pitfalls · why · bridge

Equation slides get `symbols` and `derivation`: what the equation computes, what
each symbol denotes, what the leading and trailing terms mean, what assumption it
starts from, how the final form is reached, and a small worked number where one
helps. Algorithm slides get `algorithm`: why the procedure is needed, what the
inputs mean, what each loop handles, why each condition exists, how candidates
are judged, and what comes out.

Transition and summary slides get a short `script` and nothing else. Do not fill
every field on every slide — a mechanically complete script is unreadable.

Budget the length against `meta.target_minutes`: the build refuses a Korean script outside
3.0–5.5 characters (no spaces) a second. An equation slide's `symbols`, `derivation` and a worked
number fit in that budget only if the slide's other asides go — the FK deck's first script put every
inconsistency the reviewers found into the notes and ran 7.8/s.
