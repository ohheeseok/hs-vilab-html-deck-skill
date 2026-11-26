아래 비평은 지정된 참고 폴더의 문서·소스·캡처·논문 본문만 근거로 작성했다. 엔진 설계는 전제로 두고 논의하지 않는다.

---

## 1. 후보 (가)·(나)·(다) 비평 및 권고안

### 1.1 후보 (가) — 「두 입력, 한 표현」: 그대로 쓰면 6장 stepper와 중복되고 저자 가설을 사실로 과장한다 `[must]`
- **근거**: [context.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/context.md#L41-L45), [repa_stepper.svg](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/repa_stepper.svg#L17-L64), [s06-step3.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s06-step3.png), [paper.txt](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/paper.txt#L318-L320) (Sec. 3.1), [paper.txt](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/paper.txt#L777-L782) (Sec. 4.2), [paper.txt](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/paper.txt#L2778-L2780) (App. M), [narrative-rules.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/narrative-rules.md#L190-L194), [interaction-rules.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/interaction-rules.md#L42)
- **청중이 얻는 것**: REPA가 외부 인코더를 직접 결합하지 못하고 병렬 정규화를 택하는 이유(clean RGB vs noisy latent의 입력 불일치, Sec. 1)와, 하나의 SiT를 앞·뒤 함수 합성($v_\theta = g_\theta \circ f_\theta$, Sec. 3.1)으로 보는 관점을 전달할 수 있다.
- **청중이 잃는 것 및 결함**:
  1. **저자 가설의 사실화(과장)**: 끝 그림을 "정렬된 앞 층 / 세부를 맡는 뒤 층"으로 못 박는 것은 논문 근거를 넘는다. 논문은 Sec. 3.2에서 *"suggesting that ..."*, Sec. 4.2에서 *"We hypothesize that this enables the remaining layers to concentrate on capturing high-frequency details"*라고 가설로 적었고, App. M에서도 정렬 깊이 메커니즘 분석을 후속 과제로 남겼다. 이미 덱 15장([deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/deck.json#L1300))은 이를 "저자의 가설"로 표기하고 20장 토론 1([s20.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s20.png))에서 비판적으로 묻는다. overview에서 이를 확정 도식으로 그려 버리면 [narrative-rules.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/narrative-rules.md#L190-L194) 위반이자 20장 토론의 전제를 훼손한다.
  2. **6장 stepper와의 직접 중복**: "clean 이미지 → 인코더", "noisy latent → SiT 앞쪽 층 → patch token 정렬 → 나머지 층"은 6장 `repa_stepper.svg`(step 1–4)가 그대로 그리는 내용이다. 20분 발표에서 같은 2경로 도식을 애니메이션과 stepper로 두 번 클리커로 넘기면 [interaction-rules.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/interaction-rules.md#L42)의 거절 사례(뒷장 도식을 재진술하는 인터랙션)와 같은 실패가 난다.
  3. **논문에 없는 그림 위험**: "앞쪽 몇 층의 token이 인코더 patch token 쪽으로 당겨진다"를 임베딩 공간의 점 이동·군집으로 시각화하면 논문에 없는 기하학을 발명하게 된다(논문은 patch별 cosine similarity / NT-Xent, Eq. 8만 정의).

### 1.2 후보 (나) — 「덱 지도」: 스킬 규칙이 명시적으로 금지한 목차형 애니메이션이며 즉시 기각 대상 `[must]`
- **근거**: [context.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/context.md#L46-L47), [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/animation.md#L16-L19), [interaction-rules.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/interaction-rules.md#L63-L65), [s02.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s02.png), [overview_map.svg](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/overview_map.svg#L1-L70)
- **청중이 얻는 것**: 발표 순서 재확인 외에 논문 메커니즘에 대한 새 시각 정보가 없다.
- **청중이 잃는 것 및 결함**:
  1. **명시적 금지 규칙 위반**: [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/animation.md#L18-L19)는 목차·결과 사다리를 애니메이션 부적합으로 규정했고, [interaction-rules.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/interaction-rules.md#L64-L65)는 *"a 'map' of which slides cover what (a table of contents — the progress bar does it)"*를 RAE 논의에서 이미 거절했다.
  2. **RAE 5장의 오독**: RAE 5장([s05-step3.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/s05-step3.png))은 장 번호 목차가 아니라 **복원·생성 이중 파이프라인 위에서 아키텍처·학습 수정 4곳의 물리적 위치**를 찍는 기계 구조도다. REPA는 정규화 항 하나를 붙이는 방법이라 "진단→처방→결과→분석"을 늘어놓으면 순수 목차가 된다.
  3. **2장·진행 바와의 완전 중복**: 2장 TL;DR([s02.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s02.png))이 이미 `1 진단 / 2 처방 / 3 결과` 3단 카드를 보여 주고, 하단 진행 바가 6개 섹션 비중을 상시 표시한다.

### 1.3 후보 (다) — 「층 축 위의 의미 품질」: 깊이 축의 직관은 좋으나 곡선을 그리면 4장·9장과 겹치고 규칙을 깬다 `[must]`
- **근거**: [context.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/context.md#L48-L49), [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/animation.md#L21-L22), [s04.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s04.png), [s09-probe.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s09-probe.png), [fig2a.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/fig/fig2a.png), [fig3a.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/fig/fig3a.png)
- **청중이 얻는 것**: 6장 stepper(`block 1–8`과 `block 9–28`을 같은 크기 상자 2개로 그림)에서 빠져 있는 **28층 깊이(depth) 축에서의 개입 위치 감각**(왜 전체가 아니라 앞쪽 8층인가)을 살릴 수 있다.
- **청중이 잃는 것 및 결함**:
  1. **4장(Fig. 2a)·9장(Fig. 3 toggle)과의 직접 중복**: vanilla probe 곡선과 REPA 개입 후 곡선을 overview에 그리면 4장([s04.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s04.png))과 9장([s09-probe.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s09-probe.png))의 스포일러가 되며, [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/animation.md#L21-L22)의 **"Where, not how much"** 원칙을 깬다.
  2. **논문에 없는 보간 위험**: Fig. 2(a)와 Fig. 3(a)는 **6–24층만** 측정했고(1–5층·25–28층 값 없음), Fig. 2(a)는 7M step에 $t=0, 0.25, 0.5$ 세 곡선, Fig. 3(a)는 1M step REPA vs 7M step vanilla를 그린다. 이를 28층 전체 축 위의 단일 개략 곡선으로 뭉개면 측정하지 않은 층을 임의 보간하게 된다.
  3. **입력 불일치 누락**: 층 축 그래프만 그리면 REPA가 왜 외부 인코더를 직접 결합하지 못하는지(clean RGB vs noisy latent, Sec. 1)가 빠진다.

### 1.4 권고안 — 제4안: 「Vanilla SiT의 병목에서 REPA의 개입 위치로」 (1장, (가)+(다)의 장점만 결합하고 겹침·과장 제거) `[must]`
- **근거**: [paper.txt](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/paper.txt#L144-L168) (Sec. 1), [paper.txt](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/paper.txt#L315-L333) (Sec. 3.1), [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/animation.md#L15-L22)
- **핵심 아이디어**: 세 후보를 그대로 쓰지 말고, **현재 덱 어디에도 없는 "Vanilla SiT(28층 한 덩어리) → REPA 개입으로 앞·뒤 분할"이라는 구조 변형**을 1장으로 만든다.
  - **(가)에서 가져올 것**: `clean RGB vs noisy latent`의 **입력 불일치**와 SiT의 **$f_\theta \circ g_\theta$ 분할**(Sec. 3.1). 단, **"고주파 세부 전담" 가설과 patch·MLP 세부 배선은 뺀다**.
  - **(다)에서 가져올 것**: **28층 가로 비율 축**(전체 28층 중 앞쪽 8층의 상대 위치가 길이로 드러남). 단, **probe/CKNNA 곡선과 수치는 뺀다**.
  - **역할 분리**: 이 overview는 **왜(Vanilla 병목·입력 불일치) + 어디(28층 중 앞쪽 8층 분할) + 무엇을 따질지(질문 마커 2개)**만 맡는다. 구체적 patch 대응·3층 MLP·수식·추론 절단은 6장 stepper에, 층별 정량 곡선은 4·5·9장에 온전히 남긴다.

---

## 2. 권고안의 구체 설계 (Beat 구성 · 끝 그림 · 옆 글 · 위치)

### 2.1 위치(지금 번호 기준): 3장(연구 배경) 뒤, 4장(Fig. 2a 진단) 앞 (= 새 4장) `[must]`
- **근거**: [context.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/context.md#L36-L37), [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/animation.md#L15-L16), [s04.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s04.png), [s05.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s05.png), [s06.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s06.png)
- **판단 이유**:
  - 현재 4–5장(Fig. 2a·b·c)은 섹션 라벨만 `배경`일 뿐, 내용상 논문 Sec. 3.2의 **첫 실증 연구(저자의 진단 실험)**이자 이미 `tone: wash`다. RAE처럼 관련 연구(3장) 뒤, 첫 연구(4장) 앞에 두어야 진짜 overview가 된다.
  - 반대로 5장 뒤(6장 앞)에 두면 **애니메이션(4 beat) 직후에 6장 stepper(5 step)가 연달아 붙어** 클릭 피로와 도식 중복이 극대화된다. 새 4장에 두면 진단 2장(기존 4–5장)이 완충 역할을 하고, 청중이 "왜 28층의 층별 표현을 진단하는가"의 맥락을 안 채로 Fig. 2를 읽게 된다.

### 2.2 레이아웃 및 제목 규격 `[should]`
- **근거**: [block-vocabulary.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/block-vocabulary.md#L61), [narrative-rules.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/narrative-rules.md#L98-L103), [s04-step3.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/s04-step3.png)
- **레이아웃**: `side: "below"` (가로 28층 비율을 1696px 전체 폭으로 펼치고, 하단에 4열 번호 설명 배치 → 6장 stepper의 `side: "right"`와 시각적 변주 확보).
- **제목 예시**: `SiT 학습의 병목과 REPA의 개입 위치` (공백 포함 21자, 한 줄, 결론 미포함).
- **캡션**: `Sec. 1 · 3.1 · 3.3을 바탕으로 그림 · SiT-XL/2(28층) 기준 비율. 진단·성능 수치는 뒤 장에서 제시`

### 2.3 Beat 구성 (4 beat = 4 정지점, 3개 전환 구간, 한 구간에 사건 하나) `[must]`
- **근거**: [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/animation.md#L78-L101), [paper.txt](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/paper.txt#L144-L168), [paper.txt](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/paper.txt#L315-L333), [paper.txt](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/paper.txt#L437-L439)

| Beat (시간) | 화면 변화 (사건 하나) | 옆 글 (`side: "below"`, 4열) |
|---|---|---|
| **Beat 0** (`t=0`, 진입 정지) | **Baseline 한 줄**: `noisy latent z_t` → 회색으로 하나로 이어진 긴 막대 `SiT (28개 block)`(얇은 28칸 눈금) → `velocity 예측 v_θ`. 막대 위 회색 보조 문구 `denoising만으로 표현까지 학습`. | **1. Vanilla SiT**<br>noisy latent에서 denoising만으로 내부 표현과 생성을 함께 학습 |
| **Beat 1** (`0 → 1.2s`) | **위쪽 외부 경로 등장 + 입력 불일치 표시**: 위쪽에 `clean 이미지 x_*` → `고정 인코더 (DINOv2)` → `clean token y_*`(하늘색)가 왼→오른쪽으로 그려지고, 왼쪽 두 입력(`x_*` vs `z_t`) 사이에 주황색 양방향 마커 `입력 불일치`가 나타남. | **2. 입력 불일치**<br>외부 인코더는 clean 이미지, SiT는 noisy latent를 받아 직접 결합이 어렵다 |
| **Beat 2** (`1.2 → 2.6s`) | **SiT 28층 분할 + 8층 정렬 다리 연결**: 하나의 회색 `SiT (28개 block)` 막대가 **8/28 지점에서 좌우로 갈라짐**. 앞쪽 `block 1–8 (f_θ)`(폭 약 2/7)이 하늘색으로 물들고, 뒤쪽 `block 9–28 (g_θ)`(폭 약 5/7)이 진한 남색으로 전환. 8층 경계에서 위쪽 `y_*`로 하늘색 정렬 선이 그려지며 `정렬 loss (학습 전용)`이 꽂힘. (`입력 불일치` 마커와 Beat 0 보조 문구는 사라짐.) | **3. 앞쪽 층 정렬**<br>SiT를 앞·뒤로 나누어 8층(XL/2) 표현을 clean token에 정규화로 정렬 |
| **Beat 3** (`2.6 → 3.7s`) | **두 질문 마커가 구조 위치에 내려앉음**: 위쪽 `고정 인코더–8층 정렬` 구간 위에 주황 브래킷 `① 무엇을, 어느 층에 맞출 것인가`, 아래쪽 `block 9–28 → v_θ` 아래에 주황 밑줄 `② 수렴과 생성이 얼마나 바뀌는가`가 내려앉아 끝 그림 완성. | **4. 이 발표의 질문**<br>① 인코더·정렬 층 선택<br>② 수렴 속도와 생성 품질 변화 |

### 2.4 끝 그림(Beat 3 = 인쇄·개요·폴백 단일 SVG)의 모양 검증 `[must]`
- **근거**: [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/animation.md#L46-L50), [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/animation.md#L84-L85), [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/animation.md#L94-L95)
- **위 행(하늘색, 학습 전용)**: `clean 이미지 x_*` → `고정 인코더 (DINOv2)` → `clean token y_*`
- **아래 행(SiT 본체, 가로 28층 비례)**: `noisy latent z_t` → **`[block 1–8 (f_θ)]`**(하늘색, 약 2/7 폭) —*(8층 경계에서 위로 연결되는 하늘색 정렬 선 `정렬 loss · 학습 전용`)*→ **`[block 9–28 (g_θ)]`**(진한 남색, 약 5/7 폭) → `velocity v_θ`
- **주황색 마커 2개**(선은 `--color-warm`, 글자는 `--color-text-heading`, [design-system-deck.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/design-system-deck.md#L22-L23) 준수): 위쪽 정렬 구간 브래킷 `①`, 아래쪽 뒤층–생성 출력 밑줄 `②`.
- **검증**: 끝 그림 한 장만 단독 인쇄(PDF `default`)되어도 "두 입력 → 28층 중 앞쪽 8층만 학습 시 외부 인코더에 정렬 → 뒤쪽 20층은 velocity 예측 → 두 검증 질문"이 완결적으로 읽히며, 가설 단정("고주파 세부"), 결과 수치(FID·17.5×), 논문에 없는 그림(임베딩 군집·미측정 층 곡선)이 일절 없다.

---

## 3. 상호작용 예산(≤ 4), 슬라이드 수(1–2장 중 선택), 1200초 준수 방안

### 3.1 추가 장수: 1장(총 22장)이 맞다 — 2장(23장)은 예산 초과이자 구조적 과잉 `[must]`
- **근거**: [context.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/context.md#L31-L33), [interaction-rules.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/interaction-rules.md#L10-L12), [deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/deck.json#L405-L442), [deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/deck.json#L648-L687), [deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/deck.json#L891-L935)
- **예산 계산**:
  - 현재 21장: 예산 $\lfloor 21 \times 0.2 \rfloor = 4$, 사용 3(6장 stepper, 9장 Fig. 3 toggle, 12장 Fig. 4 toggle).
  - **1장 추가(22장)**: 예산 $\lfloor 22 \times 0.2 \rfloor = 4$, 사용 **4**(기존 3 + 애니메이션 1) → **기존 상호작용을 하나도 깎지 않고 게이트 통과**.
  - **2장 추가(23장)**: 예산 $\lfloor 23 \times 0.2 \rfloor = 4$, 사용 **5** → **게이트 실패**.
- **2장을 위해 기존 toggle을 정적으로 바꾸면 안 되는 이유**:
  - 12장 Fig. 4 toggle([s12-parrot.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s12-parrot.png))은 3개 클래스×6장(18개 이미지)의 정성 비교다. 한 장에 합치면 1024×768 프로젝터에서 형태 디테일이 뭉개져 [design-system-deck.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/design-system-deck.md#L42-L44) 및 [interaction-rules.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/interaction-rules.md#L38-L39)에 정면 위배된다.
  - 9장 Fig. 3 toggle([s09-probe.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s09-probe.png)~[s09-fidacc.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s09-fidacc.png))도 축과 범례가 다른 3개 플롯을 한 번에 크게 읽기 위한 정당한 toggle이다. REPA는 RAE와 달리 방법 자체가 정규화 항 하나이므로, 2장짜리 overview를 넣으려고 잘 작동하는 9장 또는 12장 toggle을 죽이는 것은 주객전도다.

### 3.2 1200초(20분) 준수를 위한 구체적 시간 재배분 `[must]`
- **근거**: [deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/deck.json#L153) 외 전 슬라이드 `time` 합계 = 1200초, [block-vocabulary.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/block-vocabulary.md#L24)
- 새 4장 overview(4 beat)에 **60초**를 배정하고, overview 도입으로 중복 설명이 줄어드는 장과 여유가 큰 장에서 **정확히 60초를 회수**한다(이미 40–45초로 빠듯한 8장 `setup`, 18장 `noise`, 19장 `scope`는 건드리지 않는다):

| 대상 슬라이드(현 번호) | 현재 | 조정 | 증감 | 감축 근거 |
|---|---:|---:|---:|---|
| **새 4장 overview (추가)** | 0s | **60s** | **+60s** | 4 beat 모션(~3.7s) + 정지점별 발화 ~14s |
| 2장 `tldr` (요약) | 55s | **45s** | −10s | 처방·구조 풀이를 새 4장에 넘기고 3카드 헤드라인만 전달 |
| 3장 `background` (연구 배경) | 55s | **45s** | −10s | 3갈래 이름 + 브릿지 질문 1줄뿐인 경량 슬라이드([s03.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s03.png)) |
| 5장 `cknna` (Fig. 2b·c) | 60s | **55s** | −5s | 끝 문단의 "입력 차이" 반복 설명 삭제(아래 5.4 참고) |
| 6장 `method` (stepper) | 85s | **70s** | −15s | 두 경로 도입을 줄이고 patch·MLP·loss·추론 절단에 집중(아래 5.5 참고) |
| 9장 `fig3` (toggle) | 80s | **70s** | −10s | 3개 패널 모두 텍스트 2줄로 간결([s09-probe.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s09-probe.png)) |
| 20장 `discussion` (정리와 토론) | 120s | **110s** | −10s | 화두 4개 제시용(실제 토론은 21장 Q&A 이후 진행) |
| **합계 (22장)** | **1200s** | **1200s** | **0s** | **20분 0초 정확 일치** |

---

## 4. `rae_example/`에서 옮기면 안 되는 것 vs 그대로 가져올 것

### 4.1 REPA로 옮기면 안 되는 것
1. **2장 연속 overview 구성(`overview_latent` + `overview_map`) `[must]`**
   - **근거**: [s04-step3.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/s04-step3.png), [s05-step3.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/s05-step3.png), [paper.txt](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/paper.txt#L466-L470) (Sec. 4.1)
   - RAE는 ① autoencoder 교체(Sec. 3)와 ② 고차원 확산 4개 수정(Sec. 4–5)이라는 독립된 두 축이 있어 2장이 필요했다. REPA는 VAE latent와 SiT 구조를 그대로 두고 정규화 항 하나만 붙이므로 2장 틀을 옮기면 억지 분할과 예산 초과를 부른다.
2. **인코더·디코더 교체(swap) 및 토큰 막대 폭 확장 메타포 `[must]`**
   - **근거**: [overview_latent.svg](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/overview_latent.svg#L32-L80), [overview_latent.anim.js](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/overview_latent.anim.js#L39-L58), [s04-beat2-mid.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/s04-beat2-mid.png), [paper.txt](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/paper.txt#L1644-L1653) (App. B)
   - RAE 4장은 SD-VAE를 DINOv2+ViT 디코더로 교체하고 토큰 차원이 16→768로 48배 늘어나는 변형이 핵심이다. REPA에서 DINOv2는 SD-VAE를 대체하지 않고 **학습 시 병렬 보조 타깃**으로만 서며, latent 크기($32\times 32\times 4$, 256 token)도 바뀌지 않는다. 교체(swap) 연출을 옮기면 청중이 REPA를 RAE처럼 VAE 교체 방법으로 오해한다.
3. **인코더·디코더 GFLOPs 비교 라벨 `[must]`**
   - **근거**: [overview_latent.svg](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/overview_latent.svg#L36-L40), [overview_latent.svg](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/overview_latent.svg#L99-L103), [deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/deck.json#L1651)
   - REPA 논문에는 이런 encoder/decoder GFLOPs 비교표가 없고(추론 시 DINOv2·MLP 미사용), 학습 시 인코더 forward 비용은 처리량(throughput) 한 항목만 보고한다. 없는 GFLOPs를 넣으면 근거 위반이다.
4. **`overview_map`의 다중 구조 수정 마커(주황 테두리 3–4곳) `[must]`**
   - **근거**: [overview_map.svg](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/overview_map.svg#L42-L68), [s05-step2.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/s05-step2.png)
   - REPA는 아키텍처를 여러 곳 고치는 논문이 아니다. `인코더 종류`, `λ`, `유사도 함수`, `모델 크기` 같은 ablation 변수를 RAE 5장의 구조 변경 마커처럼 파이프라인 곳곳에 꽂으면 개념이 혼동된다.
5. **RAE 5장의 "순수 잡음(점만 있는 회색 상자)"을 REPA 학습 입력 자리에 그대로 쓰는 것 `[should]`**
   - **근거**: [overview_map.svg](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/overview_map.svg#L30), [s05-step1.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/s05-step1.png), [paper.txt](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/paper.txt#L401-L408) (Sec. 3.3)
   - RAE 5장 아래 행은 생성(추론) 시작점인 순수 잡음이지만, REPA 학습의 아래 행 입력 $z_t$는 **위 행과 같은 이미지 $x_*$의 VAE latent에 noise를 섞은 상태**다. 순수 잡음 아이콘을 그대로 옮기면 "같은 이미지의 clean과 noisy를 짝짓는다"는 핵심 전제가 깨진다(산+해 아이콘에 점/격자 노이즈를 겹치거나, 6장과 시각 층위를 구분한 latent 격자+노이즈 표현을 써야 한다).

### 4.2 REPA로 그대로 가져올 것
1. **`side: "below"` 전체 폭 파이프라인 + 하단 4열 번호 beat 카드 `[must]`**
   - **근거**: [s04-step3.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/s04-step3.png), [s05-step3.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/s05-step3.png), [block-vocabulary.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/block-vocabulary.md#L61)
   - 28층 비례 막대와 2경로를 넓게 펼칠 수 있고, 6장 stepper(`side: "right"`)와 레이아웃이 겹치지 않는다.
2. **Beat 0을 "기존 baseline의 완결된 정지 그림"으로 여는 서사 구조 `[must]`**
   - **근거**: [s04.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/s04.png), [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/animation.md#L84-L85)
   - 빈 화면에서 시작하지 않고 회색 Vanilla SiT 파이프라인 위에서 발표자가 말문을 연 뒤 클릭으로 변형시키는 리듬이 20분 클리커 세미나에 가장 안정적이다.
3. **고정 토큰 색 의미 체계와 Beat 3 주황 질문 브래킷/밑줄 패턴 `[must]`**
   - **근거**: [overview_latent.svg](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/overview_latent.svg#L9-L12), [overview_latent.svg](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/overview_latent.svg#L89-L92), [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/animation.md#L94-L95)
   - 회색(baseline) → 하늘색(REPA 정렬 경로·앞쪽 층) → 진한 남색(SiT 나머지 구조) → 주황색(질문·불일치 마커, 텍스트 금지)의 역할을 그대로 유지하면 덱 전체의 색 언어가 일관된다.
4. **RAE 구현에서 검증된 시각·PDF 방어 기법 일체 `[must]`**
   - **근거**: [overview_latent.anim.js](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/overview_latent.anim.js#L26-L31), [overview_map.anim.js](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/overview_map.anim.js#L19-L29), [overview_map.anim.js](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/overview_map.anim.js#L50-L55), [s05-beat3-mid.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/s05-beat3-mid.png), [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/animation.md#L67-L70), [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/animation.md#L90-L101)
   - `lib.fade`(opacity 0일 때 `visibility="hidden"`, PDF 텍스트 레이어 유령 겹침 방지), 같은 자리 라벨의 순차 교체(`swap()`), 선이 끝점에 닿을 때 화살표 등장(`stroke-dashoffset` + `arrow` 지연 등장), 덮이는 선분 분할, 뒤로 물러나는 행의 opacity ≥ 0.35(`BACK = 0.5`) 유지.

---

## 5. 이 overview가 들어올 때 현재 2–6장에서 겹치거나 고칠 곳

### 5.1 현재 3장 (`background`, 연구 배경): callout 질문이 새 4장 Beat 3과 바로 겹친다 `[must]`
- **근거**: [deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/deck.json#L249-L261), [s03.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s03.png)
- **문제**: 3장의 callout(*"외부 표현에 정렬하면 수렴 속도와 생성 품질이 얼마나, 어떤 조건에서 바뀌는가?"*)이 새 4장 Beat 3의 질문 ②와 두 장 연속으로 겹친다.
- **수정**: 3장 callout을 앞선 세 갈래(특히 Würstchen·RCG처럼 외부 표현을 직접 생성 입력으로 쓰는 갈래)에서 새 4장으로 넘기는 **구조적 질문**으로 바꾼다(예: *"외부 인코더를 직접 결합하지 않고, denoising transformer의 학습 신호로만 쓸 수 있는가?"*). `time`은 55s → 45s.

### 5.2 현재 5장 (`cknna`, Fig. 2b·c): 대본 마지막 문단의 "입력 차이" 설명이 새 4장 Beat 1과 중복된다 `[must]`
- **근거**: [deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/deck.json#L384)
- **문제**: 5장 `notes` 3번째 문단(*"그중 하나는 입력 차이입니다. 인코더는 clean 이미지를 받고 확산 모델은 noisy latent를 받습니다. 그래서 인코더를 직접 결합하는 대신 정규화로..."*)이 새 4장 Beat 1에서 이미 시각적으로 설명한 내용을 처음 꺼내는 것처럼 반복한다.
- **수정**: 새 설명 대신 **회수(callback) + 다음 장 브릿지**로 고친다(예: *"7M step을 학습해도 정렬이 이 수준에 머뭅니다. 앞서 본 입력 불일치 때문에 정규화로 8층에 정렬을 걸 때, 구체적인 학습·추론 배선이 어떻게 되는지 다음 장에서 보겠습니다."*). `time`은 60s → 55s.

### 5.3 현재 6장 (`method`, `repa_stepper.svg`): Step 1–2가 새 4장과 겹치므로 진입 상태와 단계를 압축해야 한다 `[must]`
- **근거**: [deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/deck.json#L404-L449), [repa_stepper.svg](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/repa_stepper.svg#L17-L76), [s06.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s06.png), [s06-step4.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s06-step4.png)
- **문제**: 새 4장에서 이미 clean 경로와 noisy 경로의 존재를 본 청중에게, 6장 첫 화면([s06.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s06.png))에서 `Clean target` 하나만 띄우고 다시 5번 클릭하며 두 경로를 처음부터 조립하는 것은 중복이다.
- **수정**:
  1. **Step 1(`Clean target`)과 Step 2(`Noisy 입력`)를 합쳐 4단계 stepper로 압축**한다: 진입 상태에 위(clean → DINOv2-B → $y_*$)·아래(noisy $z_t$ → block 1–8 → $h_t$) 두 경로가 함께 놓인 상태에서 출발 → 클릭 1(**같은 위치 patch 대응 + 3층 SiLU MLP $h_\phi$ → $\mathcal{L}_{\text{REPA}}$**) → 클릭 2(**block 9–28 $g_\theta$ → $v_\theta$와 합산 loss**) → 클릭 3(**추론: 인코더·MLP 제거**). 이로써 6장은 overview에 없던 구현 디테일에만 클릭을 쓰게 되고, `time`도 85s → 70s로 자연스럽게 줄어든다.
  2. *(추가 시각 정합성, `[should]`)*: [repa_stepper.svg](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/repa_stepper.svg#L68-L71) Step 5의 흰 덮개 `opacity=".88"`은 위쪽 경로를 실질 투명도 0.12로 만들어 [s06-step4.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s06-step4.png)에서 프로젝터 가독성 기준(≥ 0.25, [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/animation.md#L90))보다 지나치게 흐리다. 덮개 불투명도를 `.70` 안팎으로 낮춰 새 4장과 톤을 맞춘다.
  3. *(추가 예산 규칙, `[should]`)*: `signature: true`는 덱 전체에 최대 1개([interaction-rules.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/interaction-rules.md#L11))다. 6장 `stepper`에 유지할지 새 4장 `animation`으로 옮길지 하나만 지정해야 하며 중복 지정은 금지된다.

### 5.4 현재 2장 (`tldr`, 요약): 슬라이드 본문은 유지하되 대본의 메커니즘 설명을 줄인다 `[should]`
- **근거**: [deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/deck.json#L175-L207), [s02.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s02.png)
- **문제**: 2장 `notes` 첫·둘째 문단이 처방 구조를 풀어 설명해 새 4장 overview와 발화가 겹친다.
- **수정**: 슬라이드의 3단 카드(진단·처방·결과)는 유지하고, 대본만 핵심 결론 3문장으로 압축해 55s → 45s로 줄인다.

### 5.5 현재 4장 (`probe`, Fig. 2a) 및 섹션 진행 바 구획: 도입 연결 + `요약·배경` / `진단` 재구획 검토 `[should]`
- **근거**: [deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/deck.json#L34-L59), [deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/deck.json#L265-L315), [s04.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/shots/s04.png), [s04-step3.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/s04-step3.png)
- **문제**:
  1. 새 4장 바로 뒤에 기존 4장(`probe`)이 오므로, `probe`의 대본 첫 문장이 새 4장의 Vanilla SiT 병목과 이어져야 한다.
  2. 기존 섹션 구성을 그대로 두고 새 4장을 `배경`에 넣으면 `배경`이 4장(연구 배경 + overview + Fig. 2 진단 2장)으로 `방법`(3장)보다 길어지고, 실증 실험(`tone: wash`)이 `배경`에 섞인 채 남는다.
- **수정**: RAE 덱의 하단 진행 바([s04-step3.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/anim/ref/rae_example/s04-step3.png): `요약·배경`)처럼 1장짜리 `요약`을 **`요약·배경`(2장 TL;DR, 3장 연구 배경, 새 4장 overview)**으로 묶고, 기존 4–5장(Fig. 2a·b·c)을 **`진단`** 섹션으로 분리하면 "배경·overview → 첫 연구 섹션(진단)" 경계가 하단 진행 바에서도 선명해진다.
