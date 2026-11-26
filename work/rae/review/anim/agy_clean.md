비평가 입장에서 5개 항목을 번호 붙인 지적으로 정리한다. 각 지적은 심각도(`must` / `should`)와 근거 파일·위치를 명시했다.

---

### 1. 연구실 세미나(20분·클리커·프로젝터)에서 "연구 내용 전 애니메이션 overview 1–3장"의 득실과 조건

1. **must "PowerPoint와 차별화"라는 매체 동기가 "논문을 더 잘 드러내는가"라는 스킬 헌장을 침범할 위험이 크다.**
   - 근거: context.md, interaction-rules.md, interaction-rules.md
   - 세미나 청중이 얻는 것은 **연속 변환·병목·데이터 흐름의 공간적 직관**과 **시선 동기화**다. 정적 도식(fig2_vae_rae.png)이나 이산적 `stepper`(deck.js의 `is-off` 토글)는 상태 A와 B를 나란히 놓거나 차례로 켤 뿐, **하나의 파이프라인이 어떻게 변형되고 어디서 병목이 터지는지**를 연속적으로 보여 주지 못한다.
   - 반대로 잃는 것은 세 가지다: **(a) 시간·본론 밀도 잠식**, **(b) 선행 스포일러와 본론 중복**, **(c) 이전 상태를 눈으로 대조할 수 없는 일시성(transient information) 및 발표자 음성과의 시선 경쟁**.

2. **must 20분 세미나에서 연구 내용 앞 "2–3장" 추가는 서사 균형을 깨뜨린다.**
   - 근거: deck.json, deck.json, deck.json, narrative-rules.md
   - 현재 RAE 덱은 21장·정확히 1,200초(20분)로 짜여 있고, 본론(5장)에 닿기 전 1–4장(표지 25초 + 요약 50초 + 배경 55초 + 두 통념 50초)이 이미 **3분(15%)**을 쓴다. 여기에 애니메이션 overview 2–3장(약 2–3.5분)을 덧붙이면 5–6분이 지나서야 첫 실험(Table 1)이 나오고, 연구실 세미나의 핵심인 분석·토론(20장, 135초)이 깎인다.

3. **should 정적 overview / 기존 `stepper`보다 나은 조건과 나쁜 조건을 스킬 판단 기준으로 명문화해야 한다.**
   - 근거: interaction-rules.md, shots/s03.png, shots/s04.png, shots/s13-step3.png
   - **애니메이션이 더 나은 조건**: (1) 구조 변형·신호 흐름·차원의 팽창/압축·노이즈 주입/제거처럼 **연속 과정 자체가 논문의 메커니즘**일 때, (2) 하나의 공간 위에서 기준선(기존 방법)이 제안 방법으로 바뀌며 **문제가 생기는 위치**를 짚어 줄 때, (3) 기존 정적 슬라이드를 **대체**하면서 1장으로 끝낼 때.
   - **정적 슬라이드나 `stepper`가 더 나은 조건**: (1) 문헌 3갈래 분류(shots/s03.png)나 목차·맵핑처럼 **이산 분류·위치 안내**일 때, (2) 정량 수치 비교·누적 실험 사다리(shots/s13-step3.png)처럼 **이전 막대와 현재 막대를 동시에 대조**해야 할 때, (3) 뒤 본론 슬라이드의 그림을 미리 요약 반복해 감흥을 깎을 때.

---

### 2. 지휘자 초안(context.md 1–6) 각 항목에 대한 판단과 구체적 수정안

1. **must 초안 1(정적 SVG + `.anim.js`) — 방향은 옳으나, 전역 ID 충돌·초기 깜박임·단일 HTML 인라인·과도기 요소 숨김 규칙이 빠져 있다.**
   - 근거: context.md, context.md, handover/HANDOVER.md
   - 정적 SVG에 요소를 미리 두는 방식은 글꼴 게이트·정적 폴백 면에서 핸드오버의 `el()` 동적 생성보다 덱에 훨씬 맞다. 그러나 다음 4가지를 반드시 고쳐야 한다:
     1. **ID 대신 `data-anim` + `<defs>` 자동 접두어**: 단일 HTML에 여러 SVG가 인라인되면 `id`가 충돌한다. 스크립트 참조는 `svg.querySelector('data-anim="..."')`로 한정하고, `<clipPath>`/`<mask>`/`<filter>`의 `id`와 `url(#...)`는 `build_deck.py`가 슬라이드별 접두어(`a04-`)로 자동 네임스페이스화한다.
     2. **과도기 요소의 기본 상태**: SVG 파일 자체를 "완성 도식"으로 두면서 이동 점·노이즈 오버레이·경고 링 같은 과도기 요소를 함께 넣으면 JS 미작동·정적 열람 시 완성 그림 위를 덮는다. 과도기 요소는 정적 SVG에서 `opacity="0"` + `data-anim-transient`로 두어야 한다.
     3. **인라인 번들**: `figures/<name>.anim.js`는 외부 `<script src>`가 아니라 `build_deck.py`가 단일 HTML 안에 인라인 번들해야 `file://` 단일 파일 원칙이 유지된다.
     4. **진입 전 선렌더**: `deck.js`의 cross-fade(`is-entering`, deck.js) 중 완성 도식이 번쩍이지 않도록, 진입 직전 동기적으로 `render(beats0)`를 호출한 뒤 슬라이드를 표시한다.

2. **must 초안 2(클리커 beats) — 클리커 박자 원칙은 맞지만, "진입 시 `0 → beats1` 자동 재생", "1–3초 구간", "재생 중 다음 키 동작" 세 군데에 설계 결함이 있다.**
   - 근거: context.md, deck.js
   - **결함 A (진입 자동 재생과 인덱스 충돌)**: `deck.js`의 `stepper`는 진입이 `step 0`(`#/n`), 첫 다음 키가 `step 1`(`#/n/1`)이고, 뒤 슬라이드에서 `prev()`로 돌아올 때 마지막 단계(`stepCount`)로 착지한다(deck.js). 진입하자마자 `0 → beats1`을 자동 재생하면 (1) 앞 180–420ms가 슬라이드 cross-fade에 묻히고, (2) 발표자가 도입 문장을 꺼내기도 전에 화면이 움직여 버리며, (3) `#/n`이 `beat 0`인지 `beat 1`인지 모호해진다.
     - **수정**: **진입 시에는 정적 시작 상태(`beats0`, `k=0`, `#/n`)로 안정 착지**하고, 첫 클리커로 `beats0 → beats1`(`k=1`, `#/n/1`)을 재생하라.
   - **결함 B (1–3초는 발표 무대에서 과도하게 길다)**: 3초는 발표자가 말을 멈추고 기다려야 하는 시간이다.
     - **수정**: beat당 순수 모션은 **0.6–1.5초(상한 1.8초)**로 줄여라.
   - **결함 C (`deck.js`의 "두 번째 키 즉시 종료" 오독)**: 현재 deck.js는 `next()` 호출 시 `settle()`로 이전 모션을 끝내며 **곧바로 다음 슬라이드/단계로 진행한다**. 초안처럼 재생 중 다음 키가 "현재 beat 끝에서 멈추기만" 하면, 발표자가 안 넘어간 줄 알고 연타하다 다음 beat까지 건너뛸 위험이 있다.
     - **수정**: 진행률 **< 80%일 때만 현재 beat 끝으로 스냅**, **≥ 80%면 스냅 후 곧바로 다음 beat 재생**(또는 완료로 간주하고 진행)하는 임계치 규칙을 두고, `prev()`는 초안대로 역재생 없이 앞 beat 끝 프레임으로 즉시 스냅한다. Q&A용 재재생은 키보드 `R` 키(현재 beat `beatsk-1 → beatsk` 다시 재생)로 분리한다.

3. **must 초안 3(`?motion=0`·PDF·QA·개요) — 개요(G)의 표시 상태와 QA 중간 프레임·`window.__deck` 훅이 빠졌다.**
   - 근거: context.md, deck.js, deck.js, deck.js
   - **수정 1 (개요 G)**: `setOverview(true)` 시 모든 `animation` 슬라이드는 반드시 **완성 도식(`beatslast`)**으로 `seek`해야 한다(`beat 0`이면 썸네일이 미완성 그림으로 보인다). 개요를 닫을 때 현재 슬라이드만 원래 `k`로 복원한다.
   - **수정 2 (QA 훅 확장)**: 현재 `window.__deck`에는 `toggle`용 `states(i)`만 있다. `beats(i)`, `seekBeat(i, k)`, `seekTime(i, t)`를 추가해 `qa_render.py`가 모든 beat 끝(`sNN-beat<k>.png`)과 각 구간의 중간 시각(선택 검사)에서 24px 글자 하한·겹침·넘침을 자동 검증하게 해야 한다.
   - **수정 3 (PDF 분량 제어)**: `print: "expand"` 외에 `print: "default"`(마지막 완성 그림 1쪽)와 `print: "endpoints"`(시작·끝 2쪽)를 지원해 불필요한 PDF 페이지 폭발을 막아야 한다.

4. **should 초안 4(`side` 누적 목록) — 애니메이션 무대를 좁히고 시선을 분산시킨다. 풀폭 + 하단 단일 readout을 기본으로 두라.**
   - 근거: context.md, interaction-rules.md, shots/s13-step3.png
   - `stepper`의 우측 누적 목록은 막대가 누적되는 차트(shots/s13-step3.png)엔 맞지만, 가로형 파이프라인(Fig. 2류)에 `cols: 3, 2` 옆 글을 붙이면 SVG 폭이 ~1,000px로 쪼그라들어 24px 글자 하한을 지키기 어렵다.
   - **수정**: 기본 레이아웃을 **풀폭 SVG + 하단 고정 높이 1–2줄 readout(현재 beat의 제목·한 문장, `aria-live`)**으로 두고, `side` 누적 목록을 쓸 때는 과거 beat를 흐려(`is-past`) 현재 beat만 강조하라.

5. **must 초안 5(예산 1–3장, 요약 뒤에만, 상호작용 예산 포함 미정) — 예산에 반드시 포함하고, 상한을 줄이며, 위치는 완화하라.**
   - 근거: context.md, interaction-rules.md, interaction-rules.md
   - **상호작용 예산에 반드시 포함(`must`)**: `Interactive slides ≤ ⌊N × 0.2⌋`(21장이면 최대 4장)에 `animation`을 포함해야 절제 규칙이 산다. 별도 예산으로 3장을 얹으면 21장 중 5장(24%)이 인터랙티브가 되어 과잉이 된다.
   - **상한 축소 및 0장 허용(`must`)**: "1–3장"이 아니라 **20분 이하 세미나는 0–1장(장기 발표 포함 최대 2장, 연속 2장 초과 금지)**으로 못 박고, `reveals` 게이트를 통과 못 하면 0장을 강제한다.
   - **위치 규칙 완화(`should`)**: "요약 뒤에만"으로 블록 자체를 묶지 말고, **Overview 목적은 요약 뒤–본론 진입부**, `animation` 블록 자체는 `reveals`와 총 예산을 지키는 한 방법론 핵심 슬라이드에도 허용한다.
   - **`interaction-rules.md` 개정(`must`)**: L53의 금지 목록은 `auto-advancing / looping animation`으로 좁히고, `clicker-paced animation`을 `toggle`·`stepper`와 동급의 3번째 블록으로 편입해 `reveals`·`start`·`print`·`provenance`를 동일하게 요구하라.

6. **must 초안 6(RAE 후보 가·나) — (가)만 살리고 (나)는 폐기하라.**
   - 근거: context.md, shots/s02.png, shots/s04.png, shots/s13-step3.png
   - (나) "두 통념과 네 가지 변경이 덱의 어느 부분에서 다뤄지는지 보여 주는 지도"는 이미 하단 진행 표시줄·2장 요약·4장 두 통념이 하는 **목차 안내**에 불과하며, 네 변경을 미리 나열해 13장 stepper와 겹친다. 상세 설계는 아래 3번에 제시한다.

---

### 3. RAE 덱에서 overview 애니메이션이 보여 줄 최적의 내용, 출처, beat 설계, 중복 방지, 2–4장과의 관계

1. **must 20분 RAE 덱에서는 단 1장 — 「SD-VAE에서 RAE로: 압축 latent 제거와 고차원 확산의 병목 지도」 — 만 넣어라.**
   - 근거: paper.txt, paper.txt, paper.txt, paper.txt, fig2_vae_rae.png, shots/s05.png
   - **논문 출처**: Fig. 2(SD-VAE U-Net 135/310 GFLOPs·4채널 압축 vs RAE ViT 22/106 GFLOPs·768채널 비압축, 256토큰 동일) + Sec. 1(두 통념과 3가지 적응 + DiT^DH) + Sec. 4–5(폭·노이즈 schedule·디코더·DDT head의 위치).
   - **왜 가장 좋은가**: 현재 shots/s05.png 하단에 `height: 315`로 눌려 있는 `fig2_vae_rae.png`는 `4-dim latent`·`768-dim latent` 세로 글자가 너무 작아 읽히지 않고, "토큰 수(256)는 같은데 채널만 48배 두꺼워져 DiT 시퀀스 연산량은 유지되되 세 곳에서 병목이 생긴다"는 핵심 구조 변화를 보여 주지 못한다. 이 변화를 **한 무대 위에서 변형(morph)하며 두 통념의 발생 지점을 찍어 주는 1장**이 정적 도식과 `stepper`가 못 하는 일을 정확히 해낸다.

2. **must Beat 분할(총 4상태 = 진입 정지 `k=0` + 클리커 3회, 각 구간 0.9–1.3초):**
   - 근거: paper.txt, paper.txt, paper.txt, paper.txt
   - **`k=0` (진입 정지 그림 — 기존 SD-VAE + DiT)**: 왼쪽에서 오른쪽으로 `256² 이미지 → U-Net 인코더(135 GFLOPs, 깔때기 축소) → 32²×4 저차원 latent → DiT(patch 2, 256 토큰) → U-Net 디코더(310 GFLOPs)`. *(도입: 기존 잠재 확산의 압축 구조)*
   - **`k=1` (클리커 1, ~1.2초 — RAE 교체와 통념 ① 위치)**: U-Net 깔때기가 일정 높이의 고정 ViT 인코더(DINOv2-B, 22 GFLOPs, 잠금 표시)와 ViT 디코더(106 GFLOPs)로 전환되고, 가운데 latent 묶음이 얇은 회색 4채널에서 **두꺼운 파란 768채널(256 토큰 유지, 원소 48×)**로 팽창한다. 인코더→디코더 직결 경로에 **`① 복원 가능한가?`** 마커가 뜬다.
   - **`k=2` (클리커 2, ~1.2초 — 고차원 확산 진입과 통념 ②의 3병목 위치)**: 768차원 토큰에 노이즈가 섞여 DiT(patch 1, 256 토큰 유지)로 들어가며, 파이프라인의 세 지점이 짧은 stagger(0.2초)로 웜 액센트 점등: **(a) DiT 내부 폭(`d ≥ n`)**, **(b) 노이즈 주입 화살표(`schedule shift`)**, **(c) DiT 출력→디코더 경계(`노이즈 증강`)**. 상단에 **`② 고차원 확산 가능한가?`** 마커가 뜬다.
   - **`k=3` (클리커 3, ~1.0초 — DiT^{DH} Head 부착 및 완성 도식)**: DiT 뒤에 얕고 넓은 2층 `DDT head` 블록이 내려와 붙고(`poke`), 노이즈 토큰이 디코더를 거쳐 깨끗한 출력으로 통과하며 종료. 마지막 그림 한 장이 **RAE + DiT^{DH} 전체 구조와 ①·② 검증 범위가 모두 보이는 완성 도식**이 된다.

3. **must 13장 `stepper`(gFID 사다리)와 겹치지 않게 하는 원칙: "구조·위치(What/Where)" vs "정량 효과(How much)"의 완전 분리.**
   - 근거: deck.json, shots/s13.png, shots/s13-step3.png
   - Overview 애니메이션에는 **gFID 수치(23.08, 4.81, 4.28, 2.16), rFID 수치, Table 번호, 수식을 일절 넣지 않는다.** 오직 파이프라인 위의 **어느 블록·경계에 문제가 있고 무엇을 바꾸는지**만 공간적으로 각인시킨다.
   - 13장 `stepper`는 7–12장에서 개별 검증을 마친 뒤, 그 변경들이 **실제로 gFID를 얼마나 떨어뜨렸는지(특히 schedule shift −18.27의 지배력, SD-VAE 7.13 돌파 시점, 마지막 단계의 최적화 혼재)**를 정량적으로 결산하는 자리로 완전히 분리된다.

4. **must 기존 2–4장과의 관계: 2장·3장은 유지하고, 기존 4장(`claims`)을 이 애니메이션 1장으로 대체하라.**
   - 근거: narrative-rules.md, deck.json, deck.json, shots/s04.png, shots/s05.png
   - **2장(`tldr`) 유지**: TL;DR 2장 고정 규칙(narrative-rules.md) 준수.
   - **3장(`background`) 유지**: 관련 연구 3갈래와 모델명(shots/s03.png)은 15분 이상 발표의 필수 배경 슬라이드(narrative-rules.md)이며 애니메이션이 대체할 수 없다.
   - **4장(`claims`) 대체**: 현재 4장(shots/s04.png)은 2단 텍스트 불릿뿐인 가장 얇은 슬라이드(50초)다. 위 애니메이션이 두 통념 ①·②를 파이프라인 위에서 직접 제기하므로 4장을 대체하면 **총 21장·20분 예산이 전혀 늘지 않는다**(65초 배정, 2장·3장에서 각 5–10초 조정).
   - **5장(`rae`) 연쇄 개선(`should`)**: 4장 애니메이션 캡션에 "Fig. 2를 다시 그림"을 명시하고(design-system-deck.md) figure ledger의 Fig. 2를 4장으로 옮기면, 5장은 찌그러졌던 `fig2_vae_rae.png`(shots/s05.png)를 덜어내고 구현 상세(patch 14→16, CLS/REG 제거, L1+LPIPS+GAN)와 Table 1b에 집중할 수 있다.
   - **만약 2장을 꼭 쓰고 싶을 때의 조건부 2안(`should`)**: 지휘자 초안의 (나) 대신, **7장(`dit-fails`)과 9장(`theorem`) 사이(② 고차원 확산 진입부)**에 「고차원 노이즈의 폭 병목(`d < n`일 때 구형 노이즈 잔여 분산 손실) + 48배 차원에 따른 schedule shift(`t=0.5 → 0.87`)」 직관 애니메이션 1장을 두는 것이 학술적으로 훨씬 낫다. 단 20분 덱에서는 총 인터랙티브가 4장(4장 anim + 9장 anim + 13장 stepper + 15장 toggle)으로 예산 한계에 꽉 차므로 기본값은 **4장 1장만** 권고한다.

---

### 4. 스킬에 넣어야 할 애니메이션 디자인 규칙 & 핸드오버 규칙 중 덱에 맞지 않는 것

#### A. 스킬에 추가해야 할 애니메이션 디자인 규칙

1. **must 속도와 멈춤: 1 beat 0.6–1.5초(상한 1.8초), 슬라이드당 2–4 beats, 끝 패딩 `STILL` 금지.**
   - 근거: context.md, handover/HANDOVER.md, handover/HANDOVER.md
   - 클리커 대기가 곧 멈춤이다. beat 끝자락에 `STILL = 1.0` 같은 빈 대기 구간을 두면 화면은 멈췄는데 엔진은 "아직 재생 중"으로 판정해 다음 클리커를 먹어 버린다. `beatsk`는 마지막 시각 변화가 끝나는 정확한 시각에 맞춘다.

2. **must 글자 크기 하한 24px: 1:1 무대 `viewBox` 강제, `scale` 축소 중 24px 미만·세로 텍스트 금지.**
   - 근거: design-system-deck.md, handover/examples/02-techniques/techniques.html, fig2_vae_rae.png
   - SVG `viewBox`를 실제 배치 픽셀과 1:1(예: `1680×720`)로 맞춰 `font-size ≥ 24`(굵기 500/700, 번들 폰트 Geomini + Gmarket Sans)를 그대로 쓰게 하라. `techniques.html`의 `zoom`처럼 축소 후 9px로 만드는 트릭과 `fig2_vae_rae.png`의 세로 회전 글자는 금지한다.

3. **must 색의 의미와 표면 규칙: 토큰 색 고정, 장식 그라디언트·그림자 금지(개념 스펙트럼·마스크만 예외).**
   - 근거: design-system-deck.md, handover/examples/01-minimal/minimal.html
   - 중립 회색(기존 방법/비활성), HSU Dark Blue(제목·구조), Sky Blue(제안 방법·현재 활성 흐름), Warm Accent(병목·주의·대조 마커, 텍스트 금지)로 색 의미를 고정한다. `minimal.html` L59-61의 장식용 배경 그라디언트와 `explainer-page.html` L29의 `box-shadow`는 금지한다.

4. **must 시작/끝 그림 규칙: 시작은 "빈 화면 금지(의미 있는 출발 상태)", 끝은 "단독 판독 가능한 완성 도식".**
   - 근거: handover/HANDOVER.md, context.md
   - 핸드오버처럼 "시작 = 끝"으로 같을 필요는 없다(오히려 비교 전환의 의미를 약화한다). 대신 시작(`beats0`)은 기준선(기존 파이프라인)이나 뼈대여야 하고, 끝(`beatslast`)은 개요(G)·PDF에서 혼자 보여도 주장 전체가 읽히는 완성 도식이어야 한다.

5. **must 동시 움직임 예산과 흐림 하한: 1 beat당 초점 사건 1개, 흐려진 요소는 `opacity ≥ 0.25` 또는 완전 `0`.**
   - 근거: handover/HANDOVER.md, handover/examples/02-techniques/techniques.html
   - 서로 무관한 두 영역을 동시에 움직이지 않는다(한 묶음의 stagger 0.15–0.25초는 1개 사건으로 허용).
   - 핸드오버의 `FAR = 0.07–0.08`은 프로젝터에서 지저분한 잔상으로 보이거나 증발한다. 맥락 유지용 흐림은 **`0.25–0.35`**, 치울 요소는 깔끔하게 **`0`**으로 이원화하라. 선 굵기는 1920×1080 기준 **≥ 2.5px**(프로젝터 53% 축소 대비).

6. **must 필터 비용 규칙: `feTurbulence` 매 프레임 `seed` 변경 및 실시간 블러 애니메이션 금지.**
   - 근거: handover/HANDOVER.md, handover/examples/01-minimal/minimal.html
   - 노이즈가 필요하면 고정 `seed` 필터의 `opacity`만 보간하거나 정적 점/격자 벡터 그룹을 사용한다.

#### B. 핸드오버 규칙 중 덱에 맞지 않아 제거·교체해야 하는 것

7. **must 재생 컨트롤 바·타임라인 슬라이더·호버 표시·그림 클릭 토글 제거.**
   - 근거: handover/HANDOVER.md, handover/template/animation-template.html, interaction-rules.md
   - 슬라이더와 호버 UI는 스킬에서 명시적 금지 사항이며, 그림 클릭 토글은 클리커 상태 기계와 충돌한다.

8. **must `IntersectionObserver`·무한 반복(`clock % length`)·독립 `<iframe>`·전역 `window.seek` 제거.**
   - 근거: handover/HANDOVER.md, handover/HANDOVER.md, handover/template/animation-template.html, handover/examples/02-techniques/techniques.html
   - `IntersectionObserver`는 개요(G) 모드에서 전 슬라이드를 동시에 재생시키는 버그를 낸다. `<iframe>`은 단일 HTML·글꼴 상속·클리커 포커스·PDF 인쇄를 모두 깨뜨린다. 제어는 `deck.js` 라이프사이클과 슬라이드별 `DeckAnim` 인스턴스로 일원화한다.

9. **must `prefers-reduced-motion` 직접 조회·Google Fonts·모바일 330px(10px) 기준·다크모드 `light-dark()` 제거.**
   - 근거: handover/HANDOVER.md, handover/HANDOVER.md, handover/HANDOVER.md, handover/template/animation-template.html, handover/examples/02-techniques/techniques.html, deck.js
   - 강의실 Windows PC는 OS 애니메이션 효과가 꺼져 있는 경우가 많아, 템플릿의 `prefers-reduced-motion`을 그대로 쓰면 무대에서 애니메이션이 꺼진다. 반드시 `deck.js`의 `still()`(`meta.motion: "on"` 우선)을 써야 한다.

---

### 5. 무대 실패 지점과 대책

1. **must 프로젝터(1024×768 53% 축소·저명암비·30Hz 출력): 가는 선·흐린 요소 증발 및 프레임 튐.**
   - 근거: design-system-deck.md, handover/examples/01-minimal/minimal.html, handover/examples/02-techniques/techniques.html
   - **대책**: 선 굵기 ≥ 2.5px, 흐림 하한 ≥ 0.25(또는 0), `qa_render.py --viewport 1024x768`로 모든 beat 끝 프레임 검증, rAF 시간 계산 시 경과 시간(`performance.now()`) 기반 + 단일 프레임 delta 상한(`Math.min(0.05, dt)`)으로 30Hz/지연 환경에서도 순간 점프를 방지.

2. **must 저사양 강의실 노트북: SVG 필터 재래스터화 버벅임 및 OS 설정으로 인한 무음 비활성화.**
   - 근거: handover/HANDOVER.md, interaction-rules.md, deck.js
   - **대책**: 동적 `feTurbulence` 금지 + `render(t)`에 dirty-check(값이 바뀐 속성만 DOM 쓰기) 적용. 현장 PC가 버벅이면 즉시 `?motion=0` 또는 라이브 단축키(`M`)로 모션을 꺼 **beat별 즉시 전환(stepper 폴백)**으로 발표를 끊김 없이 이어가도록 엔진에 비상 스위치를 둔다.

3. **must PDF 내보내기: Chromium 인쇄 엔진의 SVG `<mask>`/`<filter>` 깨짐, 빈 초기 프레임 출력, 페이지 폭증.**
   - 근거: context.md, handover/examples/02-techniques/techniques.html
   - **대책**: 가급적 `<mask>`/`<filter>` 대신 그룹 `opacity`·`clipPath`·`transform`을 우선 쓰고, `@media print`에서는 노이즈 필터를 숨긴다. `export_pdf.py`가 `animation` 슬라이드의 `print` 설정(`expand` / `endpoints` / `default`)에 따라 `seekBeat` 후 인쇄하고, 생성된 PDF 페이지를 이미지로 렌더해 육안/자동 점검하는 단계를 넣는다.

4. **must 발표자 말 속도와 화면 불일치(클리커 연타·박자 망각·Q&A 복귀 오작동).**
   - 근거: context.md, deck.js, deck.js, interaction-rules.md
   - **실패 양상**: 풀폭 애니메이션에서는 발표자가 "다음 클릭이 beat 3인지 다음 슬라이드인지" 잊기 쉽고, 긴 구간(2–3초) 도중 연타하면 beat를 건너뛰며, Q&A에서 뒤로 돌아왔을 때 자동 재생이 시작되면 발언을 방해한다.
   - **대책**:
     1. 푸터 folio 옆에 **미세한 beat 진행 점(예: `● ● ○ ○`)**을 표시해 발표자가 남은 클리커 횟수를 눈끝으로 확인하게 한다.
     2. 1 beat를 **0.6–1.5초**로 짧게 제한하고, 진입 시 정지(`k=0`) → 첫 클리커로 시작한다.
     3. `notes`에 `beat 1`, `beat 2` 클릭 큐를 강제해 `script.html`에서 리허설 박자를 맞춘다.
     4. 애니메이션 슬라이드 안에 focusable 컨트롤을 두지 않아 클리커 입력이 가로채이지 않게 하고, `prev()` 복귀 시에는 항상 자동 재생 없이 정지 프레임(`beatsk-1` 또는 뒤 슬라이드에서 돌아올 때 `beatslast`)으로 스냅한다.
