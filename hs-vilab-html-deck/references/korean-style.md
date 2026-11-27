# Korean editor — the plain-Korean pass on deck.json

This file is the editor's whole rulebook; the skill needs nothing else installed. Part A is this
skill's own rules, learned from four decks. Part B condenses, for slide decks, the rules of
`heeseok-korean-anti-slop` **1.3.0** (https://github.com/ohheeseok/heeseok-korean-anti-slop, MIT,
same author); its rule IDs (L1-5, L3-3, …) are kept so the bundled scanner's hits line up. When
that skill gains a release, compare its `references/` with Part B and copy what applies, and copy
its `scripts/scan_slop.py` over `scripts/scan_slop.py` (keep the note at the top).

The editor is codex (`delegate.py text`) or a subagent. It never sees the paper; it edits prose and
returns a table, and the conductor applies it mechanically.

```bash
mkdir -p $W/review/kref
python $S/scripts/deck_text.py $W/deck.json -o $W/review/deck_text.md      # one line per string: [location] text
python $S/scripts/scan_slop.py $W/review/deck_text.md > $W/review/kref/scan.txt
cp $W/review/deck_text.md $S/references/korean-style.md $W/review/kref/     # kref/ = the text, the hits, this file
python $S/scripts/delegate.py text --prompt-file $W/review/kref/prompt.md --dir $W/review/kref --out $W/review/korean.md
python $S/scripts/apply_text_edits.py $W/deck.json $W/review/korean.md           # dry run
python $S/scripts/apply_text_edits.py $W/deck.json $W/review/korean.md --write
```

`apply_text_edits.py` applies a row only when the text at that location still equals `original`
(whitespace-normalised, so U+00A0 reads as a space) and refuses any row whose numbers differ. A row
replaces the whole string: a U+00A0 the original had is gone unless the edit has it too. Check every refused row: a
fixed slide reference or a value moved from the script is applied by hand, a changed number is not.
After applying, the verifier reads `deck.json` again.

## The prompt (`kref/prompt.md`)

- Read `korean-style.md` (this file) first; Part A before Part B.
- Lines whose location is `notes` are the spoken script: 합쇼체, spoken. Everything else (title,
  message, body, caption, alt) is on-screen copy: 개조식·명사형 or a short -다 sentence. Keep each
  register.
- Read the summary and discussion slides as someone in the room would: for every line, can you say
  what it claims and which experiment shows it? If not, it is the first thing to fix (A1–A3).
- Scanner hits are candidates, not orders (a comma after a connective ending is usually fine).
- One term per concept across the deck; English technical terms stay English.
- **Never change**: numbers, model and dataset names, technical terms, `$…$` math, `**…**`, hedges
  and attributions ("저자 해석", "해석", "약"), or what a sentence claims.
- Do not list lines that need no change. Do not force edits.
- Output one table `| location | original | edit | rule |` — location exactly as printed,
  original and edit as **whole** strings, no `|` inside cells — then the scanner hits kept and why.

## Part A — this skill's rules

The scanner found almost none of these: on the Integral deck it flagged 15 candidates outside the
commas and the presenter still could not follow slides 16 and 20. They come from the deck's own
making — synthesis compresses, and the writer coins labels for things only the writer has seen.

**A1. No coined labels.** A name the deck made up for its own argument is not a term the room
knows. Say what was done and what it showed.

| written | rewritten |
|---|---|
| 통제 비교 (18 times, never defined) | 비교 실험 — defined once on screen: "한 가지만 바꾸고 나머지는 같게 둔 실험" |
| 대안 설명 / 지움 · 일부 · 남음 | the alternative as a question ("재구성을 잘하는 latent라서?") and a plain verdict ("아니다", "일부만 확인", "가능성 남음", "확인 안 됨") |
| 공유의 몫과 latent 자체의 몫 | VLM과 같은 토큰을 쓴 효과와 AF latent 자체가 학습하기 쉬운 효과 |
| 0.89B 밖의 비용, 시각 경로 | 생성 전용 0.89B 외에 VLM 이미지 입력 모듈 교체, pixel decoder, VLM마다 tokenizer 재학습 |
| 공유 표현의 생성 이득은 무엇에서 오나 | AF 토큰으로 생성이 잘되는 이유는 무엇인가 |

A paper's own term (`generative stream`, `propagation bottleneck`) stays, glossed where it first
appears ("생성 stream(생성을 맡는 별도 transformer)").

**A2. Say who does what.** A condition shortened to a noun hides its actor: "VLM 조건" → "VLM이
조건을 줄 때"; "이해 입력" → "VLM이 읽는 이미지 입력"; "생성 latent" → "생성 모델이 만드는 latent".

**A3. Summary and discussion items are sentences.** No arrows or symbols as grammar ("폭 ≥ 토큰
차원, …, DDT head → 1.51", "복원 ≠ 생성"). A discussion item is the fact, then the question, and the
question asks about its own heading (REPA: "**깊이**: … 무엇을 정렬해야 하나?" asked about the
target under a heading about the layer). A fact the question rests on goes on the slide, not only in
the script (REPA: "어느 target 설정인가?" without the 9.7 and the two tables that disagree).

**A4. `reveals`, captions and readouts end in what is seen.** "설계 변경별 gFID 감소 폭과 SD-VAE
기준선보다 낮아지는 단계" → "막대를 하나씩 더하면 설계 변경마다 gFID가 얼마나 내려가는지, 어느 변경에서
SD-VAE 기준선 아래로 내려가는지 보인다."

**A5. The picture and the text say the same thing.** An animation's questions are written in the
SVG and in the beat text; change both (`make_overview_*.py` or the SVG's `foreignObject`).

**A6. Slide references follow the slides.** After a slide is added or removed, check every "n번",
"n장", "n–m장". RAE kept "(18번)" for 0.5.0's slide 19 and "6번에서" for slide 7 until this pass.
`apply_text_edits.py` refuses these rows (the number changes); apply them by hand.

**A7. A value keeps its source mark.** "약" only on a value read from a curve; a value printed in
the text or a table has none ("VLM + FLUX.1-VAE 0.18", not "약 0.18").

**A8. Keep pairs on one line.** U+00A0 after a circled number in a list ("① AF 토큰으로 …"),
inside "2B × FLUX.1-VAE", "LLM + AF", "456.0M → 582.1M". The build already keeps a measurement with
its unit and "Fig. 3", "FID 5.30", "= 9.6" together.

## Part B — from heeseok-korean-anti-slop 1.3.0, for decks

Meaning first: numbers, units, names, links, math; negation, contrast, cause, exception, scope,
order, hedges and modality; the register. Then the style. Do not add a cause, metric, experiment or
attribution the deck does not have; do not soften or strengthen a claim to make it read better.
Find what a vague word points to in the same slide, the table, or the slides around it; only when it
is not there, leave the line and say so under the table.

### Presentation copy — eight patterns

| pattern | example | rule | check |
|---|---|---|---|
| fake contrast | 단순히 A가 아니라 B다 | L1-5 | is anyone claiming A? Keep a real exclusion ("32층 전부가 아니라 네 층마다") |
| shared look with no purpose | A와 B를 함께 봅니다 | L1-13 | what is decided by looking at both? Do not supply "비교·종합" from nowhere |
| decorated abstraction | 맥락의 밀도를 더한다 | L2-10 | what changes? Not another abstraction |
| demonstrative with no referent | 이를 통해, 그 기준에 따라 | L1-11 | find it on the slide or before; do not invent one |
| stock noun phrase | 판단 기준, 작동 구조 | L1-3, L1-8 | name the actual criterion or action; keep a defined term |
| announcement for content | 중요한 것은 …, 핵심은 … | L1-6 | start with the claim |
| vague "~에 가깝다" | A보다 B에 가깝다 | L1-14 | keep the degree; do not turn it into "B다" |
| reflex three items | 기준, 방식, 그리고 메시지 | L1-15 | three only if three independent things |

### Layer 1 — structure

- **L1-1** wordy particles: "을 통해", "에 있어서", "에 의해", "와 관련하여" → the plain particle or verb.
- **L1-3, L1-8** abstract Sino-Korean chains and stock words (고도화, 제고, 방향성, 다양한, 활용, 해당,
  이러한): use the concrete noun or verb when the slide has it.
- **L1-4** genitive chains "A의 B의 C" → a verb or a clause.
- **L1-6** closing tags ("시사하는 바가 크다", "할 때입니다", "한계도 분명하다") and cleft sentences
  ("~하는 이유다", "핵심은 ~이다"): say the content; keep a real "따라서".
- **L1-7** a comma after a connective ending (고, 며, 지만) is usually fine; remove it only where it
  splits one clause.
- **L1-11** demonstratives: see the table above.
- **L1-16** meta-copy: "이 장에서는 ~을 살펴보겠습니다", "한눈에 정리", a title "주요 인사이트" → the
  content itself. Keep real directions ("실험 조건은 9번", "다음 장에서 Fig. 3으로").

### Layer 2 — metaphor and aphorism

- Physical or bodily metaphors for abstract work (손에 잡히는, 무게를 싣다, 지형을 바꾸다), aphorisms
  and number-contrast slogans, "A는 B다" metaphors, inanimate subjects acting like people: say the
  actual relation. A technical term with a metaphorical origin (병목, 노이즈 스케줄, 기울기장, 4층씩
  "묶는" projection that the paper describes) stays.
- **L2-9** do not characterise technical objects ("호라이즌 3형제", "분포가 살아남는다").

### Layer 3 — compression and collocation

- **L3-2** verbs translated from English that do not take this object ("실험을 돌린다" in a formal
  line, "가정을 남긴다" → 가정을 명시한다).
- **L3-3** three or more action nouns glued with 의 or · → restore the subject and the condition from
  the slide. Lists of names (VAE·VQ·FSQ) stay.
- **L3-5** table cells: one ending style per column; a noun ending shows the act or state
  ("~ 없음", "~ 확인", "~ 필요").
- **L3-6** keep modality: an ought stays an ought, a guess stays a guess.
- **L3-8** compliance register ("~할 것을 권장드립니다", "~에 한하여 허용") → plain verbs, same strength.
- **L3-9** an unspecific hedge: make its condition concrete from the slide; never just delete it.
- **L3-10** over-justification: praise of the method or the slide in place of the evidence.

### Technical explanation

- **L1-12** "한 번에 해결", "정확히 일대일", "구조적으로 보장", "별도 장치 없이": check the condition
  and the kind of claim (observation, the authors' explanation, our interpretation, a proven
  statement). Keep a proven statement; do not weaken an observation without a reason, and write the
  reason under the table. "X가 병목이다" as a refrain: say what is limited by what.
- A summary must not drop the conditions the body states (step, resolution, metric, model size).

## On-screen copy, in short

- Titles introduce (`토큰별 noise 배치 네 방식`), they do not conclude.
- Bullets are phrases or short -다 sentences, one idea each, 1–2 lines at the column width.
- Captions start with `**Fig. n**` / `**Table n**` and a space, then the conditions.
- Mark the deck author's reading with `note` or `"note": true` (해석), the authors' own explanation
  with "저자 해석", external facts with their source.
