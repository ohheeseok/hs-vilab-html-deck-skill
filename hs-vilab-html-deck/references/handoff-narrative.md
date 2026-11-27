# Handing the draft to codex — `brief.md`

`delegate.py text --prompt-file $W/brief.md --dir $W/source --out $W/outline.md`

Put the paper's text **inline** after `# Paper` (`extract_figures.py paper.pdf text`). The brief is
the delegate's only copy of the narrative rules: when `narrative-rules.md` changes, change this too.
Fill the `<…>` from the four answers in SKILL.md [0]. When the draft comes back, do not adopt it:
the review in [1] applies to it exactly as to one written here.

This is the brief used for the Integral run, with its talk-specific lines kept as the example. It asks
for the overview animation's slot and beats in the draft (Structure, Blocks): planned there, it is
reviewed with the rest of the outline instead of being bolted on after synthesis.

```markdown
# Task
아래 논문으로 발표 슬라이드 개요를 만들어라. 슬라이드 본문 문장은 쓰지 말고,
슬라이드마다 제목 / 핵심 메시지 한 줄 / 화면에 올릴 구체적 사실 / 근거 위치 / 블록을 적어라.
파일은 만들거나 고치지 말고 결과만 출력하라.

# The talk
- 자리: 연구실(VILAB) 논문 세미나. 발표 후 토론. 청중은 생성 모델을 공부하는 대학원생과 교수.
- 중심 줄기(표현 공유의 생성 이득): 논문의 핵심 주장 — 이해와 생성이 같은 시각 표현 공간(AF 토큰 z)을 쓰면, 재구성 품질만으로는 설명되지 않는 생성 학습 이득이 생긴다 — 을 세우고, 그 근거가 되는 통제 비교를 하나씩 따라가며 주장이 어디까지 성립하는지 본다. 근거 사슬: AF vs FLUX.1-VAE(비슷한 PSNR, GenEval 차이; Fig. 1, 6a), SigLIP2-AF(외부 의미 인코더에 같은 AF; Fig. 6a), VLM vs LLM 조건(Fig. 6b), AF w/o sem.(재구성은 더 좋은데 생성은 낮음; 부록 Tab. 11, Fig. 10), 2B 백본(Fig. 7). 그 공유 공간을 어떻게 만드는지(propagation bottleneck 가설과 AF, Fig. 3–4, Tab. 1–2)와 생성 쪽 구조(Block-wise MoT, Fig. 5)는 이 주장의 전제로 설명하고, 전체 성능(Tab. 3–6, Fig. 2)은 그 위에 놓는다. 가설(propagation bottleneck)과 저자 해석은 사실로 말하지 말고 귀속한다. 끝은 토론점.
- 시간: 20분, 목표 슬라이드 22장 (표지와 마지막 ending 슬라이드 포함).
- 제목 언어: ko. 한글 제목도 고유명사·기술 용어는 영어로 둔다. 본문은 한국어 + 영어 기술 용어.
- 형식: PPT가 아니라 1920×1080 HTML 덱. 발표자는 클리커로 넘긴다.

# Structure
cover → TL;DR → 배경 → 문제와 공백 → 방법 → 결과 → 분석 → 한계 →
정리와 토론 → ending. 논문에 없는 단계는 넣지 않는다.
- 마지막 슬라이드는 ending(감사합니다 / Q&A, 발표자, 논문·프로젝트 링크 몇 줄)이다. 내용 슬라이드로 세지 말고 22장에 포함하라.
- TL;DR은 2번째 슬라이드: 논문이 하는 일 한 문장 + 기여 2–4개.
- 배경 슬라이드는 논문이 놓인 연구 갈래를 보여 준다: 갈래마다 대표 모델을
  논문의 관련 연구에서 이름으로 들고, 마지막 줄은 이 발표가 답할 질문으로 끝낸다.
  15분 이상이므로 배경과 문제 제기를 서로 다른 슬라이드로 둔다.
- 방법 구간 앞(배경·문제 제기 끝)에 overview animation 1장 자리를 둬라: 논문의 구조를 도식 하나로 그리고,
  클리커를 누를 때마다 한 단계(beat)씩 모양이 바뀐다(3–5 beat, beat마다 사건 하나). PDF로는 못 보여 주는
  "무엇이 어디로 흐르는가"를 보여 준다. 결과 수치는 넣지 않는다. 제안할 때 beat 목록(beat마다 무엇이 바뀌는지와
  근거 위치)과 reveals를 적어라. 상호작용 예산에 들어간다.
- 마지막 앞 슬라이드는 정리(takeaways)와 토론 포인트 3–4개.
  토론 포인트는 두 종류를 섞는다.
  · 근거: 절 사이의 불일치, 측정하지 않은 주장, 최적화하면서 동시에 평가한
    지표, 돌리지 않은 ablation.
  · 대가: 논문이 다루지 않은 설계 선택의 비용을 논문의 설명에서 끌어낸 것
    (해석으로 표시).
- 구간 표시는 eyebrow가 아니라 하단 진행 표시줄이 한다. 슬라이드마다 `section`을 적어라.
  구간은 4–6개, 이름은 짧은 한국어(예: 요약 / 배경 / 방법 / 결과 / 분석 / 정리와 토론). 표지는 구간 없음.
  section divider 슬라이드는 쓰지 않는다.

# Titles
- 제목은 슬라이드를 소개한다. 결론을 선언하지 않는다.
  주제만(`Abstraction Fusion`) 또는 주제 + 짧은 주장(`GenEval: 50K step 통제 비교`).
- 한 줄. 한글 기준 22–26자 이내.
- "X가 아니라 Y", 수사 의문문, 과장 형용사 금지.

# Content
- 슬라이드당 핵심 메시지는 정확히 하나. message는 발표자가 말할 한 문장이고 화면 제목과 다르다.
- 방법 슬라이드에는 추상 설명만이 아니라 논문이 밝힌 구체적 사실을 올린다
  (인코더 블록 수·patch size·d_h, AF가 모으는 28개 표현과 4층씩 묶은 7개 feature, d_z = 256, 의미 projector의 2×2 병합과 d_s,
  손실과 λ_sem·β_KL·r, 디코더, generation block 8개·4층 간격·d_g, adaLN-single, DDT head, time shift, 0.89B, 학습 단계와 step 등).
- 논문 자신의 예시를 쓴다. 정성 그림은 각 예시가 무엇을 보여 주는지 짚는다.
- 같은 기준 모델 대비 변화는 수치 차이(Δ)로 보여 줄 수 있으면 그렇게 표시한다.
- 한 지표를 모델 4개 이상에 걸쳐 비교하면 막대그래프(`bars`). 여러 지표를 함께 볼 때만 표(`table`).
- 큰 숫자 하나는 지표 하나에만 붙인다. 두 지표를 한 숫자로 묶지 않는다.
- 논문에 없는 주장·수치·인과관계를 만들지 않는다. 숫자에는 조건(벤치마크, 설정, 모델 크기, step)을 붙인다.
  통제 비교(Sec. 3.4–3.6)는 50K step(토크나이저는 20K step) 같은 짧은 학습의 GenEval이다. 그 조건을 숫자와 함께 적는다.
- 한계, 적용 조건, 반례를 포함한다.

# Blocks (HTML 덱에서 쓸 수 있는 것)
슬라이드마다 `block:`에 하나 이상 적어라. 레이아웃은 `split`(좌우 2열, 비율 지정)으로 나눈다.
- `lead` 큰 문장 하나 · `bullets` 항목 3–5개 · `groups` 소제목이 붙은 항목 묶음 2–3열
- `cards` 병렬 항목 2–4개 · `callout` 강조 한 문장(슬라이드당 1) · `note` 해석 표시(덱 전체에서 아껴 쓴다)
- `deltas` 기준 대비 차이 큰 숫자 1–3개 · `bars` 한 지표 × 모델 4개 이상 · `table` 여러 지표
- `figure` 논문 그림 크롭(축·범례 포함, 캡션은 슬라이드가 씀) · `figureNumbered` 그림 위에 번호를 찍고 번호별 설명
- `equation` LaTeX 수식 1–2개와 기호 설명 · `process` 단계 3–5개의 흐름 · `compare` 두 방식 나란히
- `diagram` 우리가 새로 그리는 SVG 도식(논문 그림을 다시 그려 단순화할 때)
- `animation` overview animation(위 Structure 참고)
- `panel` 옅은 바탕 묶음. 슬라이드당 2개 이하, 덱의 40% 이상은 패널 없는 슬라이드.
- 인터랙티브: `toggle`(두세 상태를 바꿔 보며 같은 도식·그림을 다시 그림), `stepper`(다음 키로 단계가 하나씩 드러남), `animation`.
  덱 전체에서 인터랙티브 슬라이드 ≤ ⌊22 × 0.2⌋ = 4장(animation 포함), 그중 "대표 인터랙션"은 1개.
  인터랙티브를 제안하려면 `reveals:`(조작하면 논문에 대해 무엇이 드러나는가)와 상태 목록을 적어라. 정적 슬라이드로 충분하면 쓰지 마라.
- statement 슬라이드(어두운 바탕, 큰 글씨): TL;DR과 정리·토론에만.

# Figure ledger — 필수
본문의 모든 Figure와 Table(Fig. 1–9, Table 1–6)을 하나도 빠짐없이 나열하고, 각각
`use: <슬라이드 번호>` 또는 `cut: <잘라낸 이유>`를 적어라. 부록의 그림·표(Fig. 10–11, Table 7–13)를 쓰면
그것도 장부에 올린다. Figure 1은 대표 그림이다. 자를 거면 이유를 말할 수 있어야 한다.
주의: 추출한 텍스트는 표의 행을 한 칸씩 줄로 끊는다. 표 숫자는 열 순서대로 읽고, 확신이 없으면 쓰지 말고 "확인 필요"로 적어라.

# Output format
## Ledger
- Fig. 1 — use: <n> | cut: <reason>
- Table 1 — ...

## Sections
- <구간 id>: <이름> (슬라이드 번호 범위)

## Slides
### <번호>. <제목>
- section: <구간 id>
- message: <핵심 메시지 한 줄>
- on-slide facts: <화면에 올릴 구체적 사실·수치, 없으면 none>
- source: <§, p., Fig., Table, Eq.>
- block: <블록과 배치>
- assets: <필요한 Figure/Table/수식, 없으면 none>
- interaction: <none | toggle/stepper/animation — reveals: … ; states/beats: …>

# Paper
<논문 본문 텍스트(부록 포함)>
```
