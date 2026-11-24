### 1. 초안 A–E 검토

**A. 진한 statement 슬라이드 (2·6번) — 수정**
- 방향(2·6번 다크, 표지 라이트, `meta.statementTheme` 옵션)에는 동의하나 **바탕을 `#12263D`가 아닌 `--color-bg` `#0E131B`로 변경**해야 합니다.
  - `#12263D` 위에 초안 E의 `--color-surface-raised`(`#1E2736`) 패널을 올리면 명도 대비가 **1.02:1**로 사라지고 채도도 충돌합니다. `--color-info-bg`(`#12263D`) 배지도 바탕에 묻힙니다.
  - `#0E131B` 바탕이면 제목 `#F1F5FA` **17.01:1**, 본문 `#D5DDE8` **13.60:1**, 보조 `#A8B5C8` **8.96:1**, 강조 `#4EB3F0` **8.01:1**로 프로젝터 대비 여유가 커지고, `#1E2736` 패널(**1.24:1**)+`#263142` 테두리(**1.42:1**) 및 "해석" 배지(`#12263D` 바탕, `#8FC8F5` 글자 **8.57:1**, `#3A7FB8` 테두리 **3.58:1**)가 정상 분리됩니다.
- **구현 보완**: [tokens.css](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/fb1/tokens.css#L237)의 다크 블록은 `:root[data-theme="dark"]`에만 걸려 있어 `<section data-theme="dark">`가 작동하지 않으므로 [deck.css](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/fb1/deck.css)에 `.slide[data-theme="dark"]` 스코프를 추가해야 합니다. 또한 `.progress`([deck.css](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/fb1/deck.css#L276))의 `--hs-sky-blue-30`(`#B4DDF4`)은 `#12263D` 위 **10.65:1**로 활성 색(`#4EB3F0`, 6.59:1)보다 밝아 역전되므로, 다크에서는 미진행 `#263142` / 완료 `#6B7D96` / 현재 `#4EB3F0`으로 교체하고 `.note-label` 글자도 `--color-info-fg`로 통일합니다.

**B. 표지 라인 (1번) — 수정**
- **eyebrow 반대**: `PLAN.md`·`design-system.md` §4/§6의 금지 항목(`A · B · C` 메타 라벨)이며, [s01.png](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/fb1/shots/s01.png) 우측 하단 `"한성대학교 VILAB 논문 리뷰"`와 중복됩니다.
- **라인 채택(수정)**: 부제와 `.cover-grid` 사이(`margin-top: 32px`)에 **전체 폭 1px `--color-border-subtle`(`#E4E5E5`, 1.26:1)** 구분선을 두고, 왼쪽 시작점에 **80×4px `--color-accent`(`#048DDB`, 3.60:1)** 막대를 겹쳐 앵커를 만듭니다. 제목부와 티저·메타 영역을 나누는 구조적 역할을 하면서 밝은 프로젝터에서도 살아남습니다. 세로선은 보류 유지.

**C. 모션 — 수정**
- "페이지당 한 번"을 **"슬라이드당 자동 모션 최대 1회"**로 번안하는 데 동의하나, 전환 + 3단 stagger + 데이터 지연이 겹치면 1슬라이드에 2~3회 연속 모션이 발생합니다.
- **3단 stagger 반대**: `design-system.md` §8의 "모든 섹션 fade-up 금지"에 정면 위배됩니다. 제거하십시오.
- **구체 값**:
  - 슬라이드 전환: 전진 시 **`180ms` `--ease-out`**, `opacity 0→1` + `translateX(4px→0)`. 후진은 **`0ms`(즉시)**.
  - 데이터 모션(전환과 동시 또는 단독 1회): 막대 그래프는 400ms 대신 **`280ms` `--ease-out`** `transform: scaleX(0→1)`(`transform-origin: left`), **값 라벨은 지연 없이 함께 표시**해 발표자 대기를 없앱니다. 표 강조 행 틴트는 300ms 지연 없이 **`0→80ms` 지연 후 `280ms` 페이드인**.
  - 토글 교차 페이드: **동의 (`180ms` `--ease-standard`, opacity만)**. `[data-state-panel]`은 `hidden`(`display:none`) 대신 grid 중첩+opacity 전환으로 바꿔야 실제로 페이드됩니다.

**D. 비교 인터랙션 — 부분 동의 (게이트 유지)**
- 방법 슬라이드의 기본 권장을 "기존 vs 제안 비교"로 잡는 데 동의합니다. v1은 **(a) 상태 토글**(주력)과 **(c) 표 baseline↔ours 행 강조**(경량 옵션)까지 허용하고, **(b) 와이프 슬라이더**는 마우스 드래그가 클리커 흐름을 끊고 정렬된 원본 크롭 확보가 드물어 `PLAN.md`대로 **v1.1 유지**를 권합니다.
- **게이트 유지**: `signature 0–1`, 인터랙티브 슬라이드 `≤ max(1, ⌊N×0.2⌋)`를 완화하면 PDF 펼침 쪽수가 불어나고 발표가 조작 시연으로 흐릅니다.

**E. 구역 나누기 `panel` — 수정**
- 도입 동의하되 SaaS 카드화·여백 압박을 막기 위해 아래로 조정합니다.
  - **상한**: 슬라이드당 **최대 2개**(3열 카드 배열 방지), 전체 덱의 **40% 이상은 패널 없음** 유지. 중첩·그림자·왼쪽 색 띠 금지.
  - **패딩**: `40–48px`은 [s03-dual.png](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/fb1/shots/s03-dual.png) 우측 열(하단 캡션과 간격 ~40px)을 넘치게 합니다. 기본 **`32px 36px`**, 사이드바(3·4·5번) **`24px 28px`**로 축소.
  - **표면**: wash(`#F3F4F4`) 위 `#FFFFFF`(1.10:1)+`#E4E5E5` 1px, 흰 바탕 위 `#F3F4F4`(1.10:1)+`#E4E5E5` 1px, 다크(`#0E131B`) 위 `#1E2736`(1.24:1)+`#263142` 1px, `radius: 6px`.

---

### 2. 캡처 기반 문제 진단 및 반영 후 리스크

| 슬라이드 | 캡처에서 확인된 현재 문제 | 피드백 해결 효과 | 반영 후 신규 리스크 |
|---|---|---|---|
| [s01.png](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/fb1/shots/s01.png) | 제목·부제 블록이 흰 여백에 떠 있고 하단 티저·바이라인과 시각적 경계가 약함 | B 라인이 헤더와 본문 그리드를 결속 | eyebrow 추가 시 우측 바이라인과 중복·템플릿 인상 |
| [s02.png](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/fb1/shots/s02.png)·[s06.png](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/fb1/shots/s06.png) | 옅은 `#E6F4FC`가 `#F3F4F4`·흰 바탕과 변별이 약해 시작·마무리 리듬 부재, 두 열이 허공에 뜸 | A 다크+E 2패널이 명확한 수미상관과 구역 분리 형성 | `#12263D` 유지 시 패널 소실(1.02:1); 밝은 강의실 프로젝터에서 어두운 배경 물빠짐 |
| [s03-vanilla.png](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/fb1/shots/s03-vanilla.png)·[s03-dual.png](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/fb1/shots/s03-dual.png) | 우측 동적 설명·수식과 하단 정적 캡션의 경계가 모호함 | E readout 패널로 변경 영역만 또렷이 구획, C 교차 페이드로 차이 강화 | 패딩 40–48px 적용 시 dual 상태에서 세로 넘침 위험 |
| [s04.png](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/fb1/shots/s04.png)·[s05.png](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/fb1/shots/s05.png) | 우측 델타 숫자가 표·차트 옆 여백에 흩어져 하단 공백이 커 보임 | E 단일 패널로 델타를 묶어 안정감 확보 | 델타마다 개별 패널로 쪼개면 SaaS KPI 카드화; 클리커 연타 시 400ms+지연 모션이 잔상 유발 |

---

### 3. 프로젝터(1024×768)·인쇄(PDF)·QA 캡처 필수 조건

- **1024×768 프로젝터(축소율 0.533)**: `--letterbox`를 `#0A0E14`로 낮춰 `#0E131B` 다크 슬라이드 경계를 확보하고, 1px 선은 서브픽셀 소실 위험이 있으므로 패널은 반드시 표면 명도차(`≥1.10:1`~`1.24:1`)를 동반합니다. 다크 본문은 순백 대신 `#D5DDE8`, 굵기 `500`을 유지해 번짐(halation)을 막습니다.
- **인쇄/PDF**: `@media print`에 `print-color-adjust: exact`를 강제하고(미적용 시 다크 배경 탈락으로 백색 글자 실종), 모든 `animation`/`transition`을 `none`, `opacity: 1`, `transform: none`으로 고정해 막대·강조 행이 최종 상태로 출력되게 합니다. `handout.html`은 항상 라이트를 유지합니다.
- **QA 캡처([deck.js](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/fb1/deck.js)·`qa_render.py`)**: `?motion=0`으로 모든 모션을 `0ms` 고정 후 캡처하고, 100ms 간격 연속 `ArrowRight` 입력 시 중간 투명 상태가 남지 않도록 연타 시 즉시 완료(`.is-rapid` 등)를 검증합니다. `scan_dom.py`에 `.slide[data-theme="dark"]` 실측 대비, `.panel .panel` 중첩 금지, 슬라이드당 패널 `≤ 2` 게이트를 추가합니다.

---

### 4. 더 나은 대안 (1건)

**결과 슬라이드(4·5번)의 "델타 패널 ↔ 차트·표 쌍(pair) 연동 포커스"**  
우측 델타 패널의 각 항목(`−0.31 FID`, `−0.19 FID` 등)에 마우스를 올리거나 클릭하면 좌측 차트·표에서 **비교 대상 두 항목(예: REPA와 Self-Flow)에만 2px `--color-accent` 테두리/마커가 반응(`120ms`)**하게 합니다. 클리커 진행과 PDF 페이지 수를 전혀 건드리지 않으면서, 피드백 3(HTML만의 반응 모션)·4(기존 vs 제안 비교)·5(델타 패널)를 하나의 학술적 장치로 통합합니다.

---

### 5. 최종 권고: 반영 순서 5줄

1. **다크 statement 토큰 고정**: `deck.css`에 `.slide[data-theme="dark"]` 스코프(`#0E131B` 바탕, `--letterbox: #0A0E14`)와 시맨틱 진행바·해석 배지·흰색 로고 및 `print-color-adjust: exact` 적용.
2. **`panel` 블록 추가**: `radius 6px`, 패딩 `32/36px`(사이드바 `24/28px`), 슬라이드당 최대 2개·중첩 금지 규칙으로 2·3·4·5·6번에 배치하고 3번 세로 여백 검증.
3. **표지 구분선 반영**: eyebrow 없이 부제 하단 1px `#E4E5E5` 전체 선 + 좌측 `80×4px` `#048DDB` 바 추가.
4. **절제된 CSS 모션 + QA 훅 구현**: 3단 stagger 제거, 전환 `180ms`/막대 `280ms`(`scaleX`)/토글 `180ms` 및 `?motion=0`·클리커 연타 즉시완료·`prefers-reduced-motion` 구현.
5. **지침·게이트 문서화**: `SKILL.md`에 비교형 인터랙션(토글·표 강조) 우선 권장 및 기존 수량 게이트 유지를 명시하고, 4·5번 델타↔차트/표 연동 포커스(선택) 검토 후 6장 재캡처 QA 실행.
