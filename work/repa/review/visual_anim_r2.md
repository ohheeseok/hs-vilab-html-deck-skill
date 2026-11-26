2차 시각 검수 결과입니다. **P0은 없으며**, 1차 수정에서 새로 생긴 지적은 **P1 1건 · P2 2건**입니다.

*(1920×1080 스테이지 px 기준, 4번 SVG `<g>` 원점 `(156, 190)` / 7번 SVG 원점 `(112, 184)` 환산)*

---

### 1. 1차 지적(V-01–V-10) 수정 확인

- **V-01**: **예** — beat 0에서 SiT 행이 중앙(`RAISE=125`)에 배치되어 상단 공백이 해소됨([s04.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1920/s04.png)). 단, beat 1 타이밍이 밀리며 중간 프레임에 부작용 발생(**V2-02**).
- **V-02**: **아니오(부분 수정)** — 정렬 선 상단 끊김(`y=196` 밀착)은 해결됐으나, 24px 틈의 연결 화살표가 파란 점에 삼켜져 보이지 않음(**V2-01**).
- **V-03**: **예** — ② 브래킷 형태가 ①과 통일되고 텍스트가 브래킷 정중앙(`x=549.1, w=1074.9`)에 정렬됨([s04-step3.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1920/s04-step3.png)).
- **V-04**: **예** — 2번(`고정 DINOv2-B`, `패치 표현`)과 3번(`패치 표현에`, `학습 때만 쓴다`) 줄바꿈·외톨이 글자 해소([s04-step1.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1920/s04-step1.png)–[s04-step3.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1920/s04-step3.png)).
- **V-05**: **아니오(부분 수정)** — 덮개 `.62`로 비활성 텍스트 가독성은 개선됐으나, 회색 화살표 두께(`2px`)는 그대로라 1024에서 상단 화살표 축이 여전히 옅고, 기각된 `h_t` 가림 사각형 결함이 그대로 남음(3번 참조).
- **V-06**: **예** — 눈금이 테두리 안쪽(`y=313..325, 395..407`, 두께 `3`)으로 들어가고 앞·뒤 색상이 분리되어 1024에서도 뚜렷함([1024/s04-step2.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1024/s04-step2.png), [1024/s04-step3.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1024/s04-step3.png)).
- **V-07**: **예** — 파란 막대 6개가 `y=84..196`(상하 4px 균등)으로 맞고 `패치 표현`이 수직 중앙(`y=140`)에 정렬됨.
- **V-08**: **예** — beat 2 길이가 `1.45s`로 줄어 정중앙([s04-beat2-mid.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1920/s04-beat2-mid.png))에서 새 라벨이 읽히며, `q1` 변위 `-4`로 상단 테두리 침범 해소.
- **V-09**: **예** — `velocity` / `예측` 두 줄 분리, 4번 설명 2행 정리, 막대 아래 `SiT-XL/2 · 28개 block` 유지가 반영됨. 단, 추가된 `SiT` 이름의 기준선·폭에 미세 결함 발생(**V2-03**).
- **V-10**: **예(텍스트) / 기각 유지(도식 높이)** — 3번 설명 `두 loss를` 줄바꿈 해소([s07-step3.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1920/s07-step3.png)). 높이 차이는 3번 참조.

---

### 2. 수정으로 새로 생긴 지적

| ID | 슬라이드 (캡처 이름) | 등급 | 1920 좌표로 본 것 | 왜 | 고칠 방법 |
|---|---|---|---|---|---|
| **V2-01** | 4번 ([s04-step2.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1920/s04-step2.png), [s04-step3.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1920/s04-step3.png), [1024/s04-step2.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1024/s04-step2.png), [1024/s04-step3.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1024/s04-step3.png)) | **P1** | `x=681–705, y=541–559` (SVG `x=525.1..549.1, y=351..369`) | 24px 틈 안에 넣은 연결 화살표(`link`, `x=527.1..547.1`, 화살촉 `540.1..547.1`) 위에 같은 파란색(`--color-accent`)의 지름 18px 원(`align-dot`, `r=9`, `x=528.1..546.1`)이 그대로 얹혀 화살표 축과 화살촉을 사실상 통째로 삼킴. 1920에서는 원 좌우로 1px 돌기만 보이고 1024에서는 화살표가 아예 보이지 않아 순방향 연결 표시가 무력화됨. | [overview_repa.svg](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/overview_repa.svg#L51-L68)와 [overview_repa.anim.js](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/overview_repa.anim.js#L25-L61)에서 틈을 40px로 확장(`front` `x=200, w=323.1`, `back` `x=563.1, w=816.9` — 폭 비 `0.396`으로 `8:20` 비례 유지, `q2` 좌단도 `563.1`·폭 `1060.9`로 연동). `link`는 다른 파이프라인 화살표와 같은 회색(`var(--color-text-muted)`, `stroke-width="3"`)의 `M526 360H558` + 화살촉 `M552 353L560 360L552 367`로 바꾸고, `align-dot`을 `r="6"`(`cx="537.1"`), `align` 하단을 `y="355"`로 줄여 점 오른쪽에 축 9px + 화살촉 8px가 온전히 보이게 함. |
| **V2-02** | 4번 ([s04-beat1-mid.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1920/s04-beat1-mid.png), [1024/s04-beat1-mid.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1024/s04-beat1-mid.png)) | **P2** | `x=284–346, y=323–337` (화살표) 및 `x=356–556, y=270–390` (`DINOv2-B` 상자) | `sit-row` 하강(`0.00–0.35s`)이 직렬로 붙으면서 위 경로 등장이 뒤로 밀려(beat 1 = `1.50s`), 정중앙 캡처(`t=0.75s`)에서 `sit-row`는 이미 내려와 있고 `top-a1` 화살표는 ~90% 진하게 떠 있는데 그 끝의 `DINOv2-B` 상자는 7.4% 투명도(`R(0.75, 0.7, 0.3)=0.074`)의 희미한 유령 윤곽으로만 보임(1024에서는 빈 공간을 가리키는 화살표처럼 보임). *(참고: 하강 중 `top-img`와의 겹침은 없음.)* | [overview_repa.anim.js](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/overview_repa.anim.js#L31-L48)에서 하강 후반과 위 경로 등장을 겹쳐 `top-img` `ENC+0.15(0.30)`(`t=0.15`에도 `cat_noisy` 상단 `y=224` > `cat_clean` 하단 `y=200`으로 겹침 없음), `top-a1` `+0.35(0.25)`, `enc` `+0.45(0.30)`, `top-a2` `+0.70(0.20)`, `tgt` `+0.80(0.30)`, `gap` `+1.00(0.30)`, `SPLIT=1.35`(`ASK=2.80, END=3.80`)로 조정해 정중앙(`t=0.675s`)에서 `DINOv2-B`가 ~84% 농도로 선명히 잡히게 함. |
| **V2-03** | 4번 ([s04-step2.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1920/s04-step2.png), [s04-step3.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1920/s04-step3.png), [1024/s04-step3.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1024/s04-step3.png)) | **P2** | `SiT-XL/2 · 28개 block` `x=356–711, y=608–648` (글자 실폭 `x=356–606`, SVG `x=200..555.1, y=418..458`); `잡음 섞인 latent` `y=618–658`; `②` 브래킷 좌단 `x=705, y=608–618` | 막대 아래 `SiT-XL/2 · 28개 block`의 실제 글자는 `②` 브래킷과 약 99px 떨어져 겹치지는 않으나, ① 바로 왼쪽 `잡음 섞인 latent`(`SVG y=428`)보다 **10px 위(`y=418`)**에 놓여 하단 기준선이 어긋나고 `block 1–8` 하단선(`y=411.5`)과 6.5px로 좁음. ② `<foreignObject>` 폭(`355.1`, 우단 `555.1`)이 `②` 브래킷 좌단(`549.1`)을 6px 침범하며, 브래킷 가로선(`y=428`)이 텍스트 높이를 가로지름. | [overview_repa.svg](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/overview_repa.svg#L57)의 `sit-name`을 `y="428"`로 내려 `잡음 섞인 latent`와 기준선을 맞추고(`block 1–8` 하단 여백 16.5px 확보), `width`를 `front` 폭(`323.1`, 현행 유지 시 `325.1`)으로 줄여 `②` 브래킷 영역과 DOM·시각 경계를 완전히 분리. |

---

### 3. 일부 기각에 대한 의견

- **V-05의 `h_t` 가림 사각형 기각 → 반대 (수정 권고, P1 유지)**
  - `stepper`가 누적 표시(`data-from-step`)이므로 4단계에서 주황 강조를 가리는 사각형 구조 자체를 유지하는 것은 타당합니다. 그러나 **현재 좌표([repa_stepper.svg](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/repa_stepper.svg#L72-L73))의 시각 결함이 실제 캡처에 그대로 보입니다.**
    1. 가림 사각형이 `y="348"`부터 시작해 격자 상단 외곽(`y=350`) 위로 **2–3px 하늘색 띠가 흰 배경으로 돌출**됩니다([s07-step3.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1920/s07-step3.png), 1920 좌표 `x=561–599, y=532–534`).
    2. 73행이 `M420 351H548`로 격자 상단선 전체와 2열 1행 칸 3면을 덧그려, 안티앨리어싱 중첩으로 **`h_t` 격자의 상단 테두리 전체와 해당 칸만 유독 굵고 진하게 보입니다**([1024/s07-step3.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1024/s07-step3.png)를 [1024/s07.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1024/s07.png)와 비교하면 뚜렷함).
  - **최소 수정(가림 방식 유지)**: 44–45행 주황 사각형을 격자선 안쪽(`x="455" y="34" / "354" width="26" height="26" stroke-width="4"`, 외곽 `453..483, 352..382`)으로 맞추면, 72행 가림 사각형을 칸 내부 `x="453" y="352" width="30" height="30"`으로 딱 맞출 수 있어 **73행 격자 재그리기를 통째로 삭제**할 수 있습니다. (여유가 되면 20·24행 상단 회색 화살표 `stroke-width`도 `2→2.5`로 키우면 1024 덮개 아래 시인성이 안정됩니다.)

- **V-10의 도식 높이 차이 기각 → 수용 가능(비차단 P2), 단 정렬 권고 근거는 유효**
  - `h_t` 격자(`y=351..479`) 우측에서 위쪽 정렬 경로(`y=375`)와 아래쪽 `block 9–28`(`y=445`) 분기를 70px 벌리려는 의도는 납득되며 판독을 막는 결함은 아닙니다.
  - 다만 4단계 추론([s07-step3.png](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/repa/review/vis_anim2/shots/1920/s07-step3.png))에서는 위 경로와 `MLP h_φ`가 덮여 **`z_t → block 1–8 → h_t → block 9–28 → v_θ`가 유일한 활성 흐름**이 되는데, 앞선 4번 슬라이드에서 한 줄로 설명한 같은 SiT(`f_θ → g_θ`)가 30px 아래로 꺾이고 `g_θ`(`y=496`)가 아래 수식(`y=548`)에 12px로 바짝 붙는 반면 `MLP h_φ` 아래(`y=290..400`)는 110px 비어 있습니다. `block 9–28`을 `y=370..460`(화살표 `y=415`)으로 올려도 두 출구 간격 40px·`MLP h_φ` 여백 80px가 남으므로, 여유가 있다면 수평 정렬을 권합니다.
