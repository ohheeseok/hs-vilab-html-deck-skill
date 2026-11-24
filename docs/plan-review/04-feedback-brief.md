# 논의 요청: hs-vilab-html-deck 샘플 6장에 대한 사용자 피드백 반영안

너는 `hs-vilab-html-deck` 스킬(논문 리뷰 발표자료를 PPT처럼 1920×1080 HTML로 만드는 독립 스킬)의 설계 검토자다.
앞서 너와 다른 검토자 한 명, Claude가 함께 계획(PLAN.md)을 세웠고, Claude가 Self-Flow 논문으로 샘플 6장을 만들었다.
사용자(연구실 교수, 실제 발표자)가 샘플을 보고 아래 피드백을 줬다. 반영 방식을 정하려 한다. 코드는 고치지 말고 의견만 써라.

## 이 폴더에 있는 것 (읽기 전용)
- `shots/` : 현재 슬라이드 캡처 (s01 표지, s02 요약, s03-vanilla·s03-dual 토글 두 상태, s04 T2I 결과, s05 ImageNet 표, s06 정리와 토론). **반드시 이미지를 직접 보고 판단하라.**
- `deck.css`, `deck.js` : 현재 엔진. `tokens.css` : 디자인 토큰(라이트 `:root`, 다크는 `[data-theme="dark"]` 블록).
- `deck.json` : 덱 IR, `dia_dual_timestep.svg` : 3번 슬라이드 도식, `PLAN.md` : 확정 계획.
- `rules/SKILL.md`, `rules/design-system.md` : 디자인 원천인 hs-vilab-frontend-design 규칙 (§6 Shape, §8 Motion, "Avoiding the defaults").

## 사용자 피드백 (원문 요지)
1. 2페이지(요약)와 6페이지(정리와 토론)는 **배경이 진하고 글씨가 연하게**(지금과 반대) 하면 좋겠다.
2. 표지에 **simple한 디자인 요소(얇은 라인 등)** 를 넣어도 되겠다.
3. 슬라이드 전환이나 표·그림 등에 **간단한 수준의 모션**을 넣자. PPT 대비 HTML의 장점이니까.
4. 기존 기술과 제안 기술을 **비교하는 인터랙션**(3번 슬라이드 토글)은 참 좋다.
5. 텍스트 box 등을 너무 strict하게 금지하기보다, **슬라이드 구역을 살짝 나누는 요소**가 들어가도 괜찮다.

## 규칙과 충돌하는 지점
- frontend-design: "No decorative saturated-navy full-bleed hero" — 단, "A dark canvas…, or the dark theme, is not this." `#032E6E`를 배경으로 쓰지 않는다. 다크 표면은 hue 216° 저채도 네이비-슬레이트(`#0E131B` bg, `#161D28` surface, `#12263D` surface-brand, `#1E2736` raised).
- Motion §8: 120/180/280ms, opacity + 2–4px translate만, bounce·spring·scale-in 금지. "자동 모션은 페이지당 최대 한 번의 연출". 행동에 대한 반응 모션은 환영. reduced-motion이면 제거.
- Shape §6: 카드는 독립적·반복 객체에만, 섹션은 여백으로 묶는다. 박스 중첩 금지, 왼쪽 색 띠 금지, 그림자 기본 0.

## Claude의 초안 (비판 대상)
**A. 진한 statement 슬라이드 (피드백 1)**
- 2·6번 슬라이드 `<section class="slide slide--statement" data-theme="dark">` — 다크 토큰을 슬라이드 범위로만 적용. 바탕 `--color-surface-brand`(다크 `#12263D`), 제목·리드 `#F1F5FA`, 본문 다크 `--color-text`, 불릿·강조 Sky 틴트.
- 하단 진행 표시줄·폴리오도 다크 토큰을 따르고 로고는 흰색 버전으로 교체.
- 수식 SVG는 currentColor라 그대로 따라감. "해석" 배지는 다크 info 토큰.
- 표지(1번)는 라이트 유지. 자동 규칙: `statement` 종류 = 다크, 덱마다 끌 수 있게 `meta.statementTheme`.

**B. 표지 라인 (피드백 2)**
- 제목 위 eyebrow 한 줄("한성대학교 VILAB 논문 리뷰 · 2026.11") + 그 아래 전체 폭 1px `--color-border-subtle` 선, 제목과 부제 사이 120×4px Sky 짧은 막대(액센트) 중 택1 또는 조합. 텍스트 열과 그림 사이 1px 세로선은 보류.

**C. 모션 (피드백 3)** — 전부 CSS, `prefers-reduced-motion`·인쇄·QA(`?motion=0`)·overview에서 끔.
- 슬라이드 전환: 앞으로 갈 때 들어오는 슬라이드 opacity 0→1 + translateX 4px→0, 280ms `--ease-out`. 뒤로 갈 때는 즉시 또는 opacity만. 키 입력을 막지 않는다(연타 시 즉시 완료).
- 도착 연출: 본문 블록(`.slide-body` 직계 자식)이 80ms 간격으로 opacity+translateY 4px, 최대 3단. 제목·푸터는 정지.
- 데이터 모션: 막대 그래프는 0에서 값까지 너비가 자라는 400ms(값 라벨은 막대가 다 자란 뒤 표시), 표는 Self-Flow 강조 행의 틴트가 슬라이드 도착 300ms 후 페이드인, 델타 숫자는 정지.
- 토글: 상태 전환 시 `[data-show]` 요소 180ms 교차 페이드, 수식 교차 페이드.
- 질문: 규칙의 "페이지당 한 번"을 "슬라이드당 한 번(도착 연출)"으로 해석해도 되는가?

**D. 비교 인터랙션 (피드백 4)**
- 방법 슬라이드의 대표 인터랙션을 "기존 vs 제안" 비교로 기본 권장(SKILL.md 지침). 형태 후보: (a) 지금 같은 상태 토글(구조 차이), (b) 이미지 출력 비교용 before/after 와이프 슬라이더, (c) 결과 표에서 baseline↔ours 행 하이라이트 전환.
- 시그니처 1개·인터랙티브 슬라이드 ≤ ⌊N×0.2⌋ 게이트는 유지할지, 비교형만 완화할지?

**E. 구역 나누기 (피드백 5)**
- 새 블록 `panel`: `--color-surface`(wash 위) 또는 `--color-surface-sunken`(흰 바탕 위), radius 6px, 1px `--color-border-subtle`, 그림자 0, 안쪽 여백 40–48px. 슬라이드당 최대 3개, 중첩 금지, 왼쪽 색 띠 금지, 패널 제목은 h3.
- 적용 예: 2번 방법/결과를 두 패널로, 6번 정리/토론을 두 패널로, 3번 토글 옆 readout을 패널로, 4·5번 델타 묶음을 패널 하나로.
- 다크 슬라이드에서는 `--color-surface-raised`(`#1E2736`) 패널.

## 요청 (한국어, 900단어 이내)
1. A–E 각각: 동의/수정/반대와 이유. 수정이면 **구체 값**(색 hex·대비비·ms·px·적용 대상)을 제시하라. 대비비는 계산해서 적고, 확신이 없으면 "추정"이라고 표시.
2. 캡처를 보고 각 피드백이 실제로 어느 슬라이드의 어떤 문제를 해결하는지, 그리고 반영 후 새로 생길 위험(예: 프로젝터에서 다크 슬라이드 대비, 모션이 클리커 연타와 충돌, 패널이 SaaS 카드처럼 보임)을 짚어라.
3. 1024×768 프로젝터·인쇄(PDF)·QA 캡처와의 상호작용에서 꼭 지켜야 할 조건.
4. 위 초안에 없는 더 나은 대안이 있으면 하나만.
5. 최종 권고를 "반영 순서 5줄"로 요약.
