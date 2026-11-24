## 1. 치명적 문제

1. **`file://` 오프라인 실행과 발표자 보기(`P`)·`--single`의 구조적 파탄**
   - 초안은 외부 CDN 금지(오프라인 발표장)와 `P` 키 새 창 + `BroadcastChannel` 동기화, `--single` 단일 HTML을 동시에 넣었다. 그러나 로컬에서 `index.html`을 직접 여는 `file://` 환경은 브라우저가 opaque origin(`null`)으로 취급해 `BroadcastChannel`이 창 간 통신에 실패한다. `--single`에서는 별도 `presenter.html` 파일 자체가 존재할 수 없다.
   - 근거: 초안「출력물·런타임」; [hs-vilab-frontend-design/SKILL.md](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/ref/hs-vilab-frontend-design/SKILL.md) §3(오프라인 제약).

2. **`dvisvgm` 수식 SVG와 다크모드(`T`)·인라인 ID 충돌**
   - `dvisvgm`은 `#000` 고정 `<path>`와 전역 `<defs>` ID(`g0-1` 등)를 출력한다. `<img src>`로 넣으면 다크모드(`--color-bg: #0E131B`)에서 수식이 배경에 묻히고, 여러 슬라이드에 그대로 인라인 삽입하면 서로 다른 수식의 `<defs>` ID가 덮어씌워져 글리프가 깨진다.
   - 근거: [hs-vilab-frontend-design/SKILL.md](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/ref/hs-vilab-frontend-design/SKILL.md) §11, [design-system.md](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/ref/hs-vilab-frontend-design/references/design-system.md) §9.2(테마 연동 SVG는 인라인 + `currentColor`/토큰 필수).

3. **`eyebrow`·`label`·`note` 좌측 바의 미해소 디자인 충돌**
   - `hs-vilab-deck`은 30분 미만 발표의 섹션 표기를 대문자 `eyebrow`(`STAGE 1 · PRETRAINING`)와 대문자·자간 확장 `label`, 좌측 띠 `note`에 의존한다. 반면 `frontend-design`은 모든 제목 위 eyebrow, all-caps/자간 확장 소형 라벨, `A · B · C` 메타 문자열, 카드·콜아웃·행 좌측 색 띠를 금지한다. 초안 충돌표에 이 항목이 통째로 빠져 있다.
   - 근거: [deck.schema.json](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/ref/hs-vilab-deck-skill/hs-vilab-deck/schema/deck.schema.json)(`slides.eyebrow`, `x-blockOptions.label`), [narrative-rules.md](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/ref/hs-vilab-deck-skill/hs-vilab-deck/references/narrative-rules.md) §1 vs [hs-vilab-frontend-design/SKILL.md](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/ref/hs-vilab-frontend-design/SKILL.md) §4·§7, [design-system.md](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/ref/hs-vilab-frontend-design/references/design-system.md) §4·§6.

4. **폰트 가중치(`400 → GmarketSans Light`) 단순 복사로 인한 프로젝터 판독 실패**
   - 초안은 `frontend-design`의 `fonts.css`를 그대로 복사한다. 그러나 `fonts.css`는 웹 근거리 열람용으로 `400 → GmarketSans Light`를 매핑한다. 1920×1080 강의실 프로젝터에서는 `Light` 한글 획이 날아간다(`hs-vilab-deck`은 `Medium`/`Bold`만 사용).
   - 근거: [design-system.md](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/ref/hs-vilab-frontend-design/references/design-system.md) §4 vs [hs-vilab-deck/SKILL.md](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/ref/hs-vilab-deck-skill/hs-vilab-deck/SKILL.md) 3b·3c.

5. **독립 실행 위반 및 필수 검증 게이트 누락**
   - `hs-vilab-deck`의 한국어 편집(1d)은 외부 스킬 `heeseok-korean-anti-slop`과 `scan_slop.py`를 pass/fail 게이트로 사용한다. 초안은 `korean-style.md`만 두고 스캐너 번들을 빠뜨려 독립 실행 시 기계적 슬롭 탐지가 사라진다.
   - 또한 초안 파이프라인은 `1a′`의 `research_verified.md` 교차검증 게이트, `4.5` 2차 리뷰(Q4), 그리고 **인터랙티브 상태 내부 텍스트·수치의 `provenance` 기록 및 1e Verifier 재검증**을 누락했다.
   - 근거: [hs-vilab-deck/SKILL.md](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/ref/hs-vilab-deck-skill/hs-vilab-deck/SKILL.md) 1a′·1c·1d·1e·4.5, [narrative-roles.md](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/ref/hs-vilab-deck-skill/hs-vilab-deck/references/narrative-roles.md) step 2·6, [narrative-rules.md](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/ref/hs-vilab-deck-skill/hs-vilab-deck/references/narrative-rules.md) §2·§3.

6. **상호 배타적 인터랙티브 상태와 "기본 상태 = 모든 단계 공개" 규칙의 모순**
   - `stepper`, `toggle`, `slider`, `metricSwitch`는 상태가 상호 배타적이라 "모든 단계를 한 화면에 동시 공개"할 수 없다. 초안대로 기본 상태 1개만 PDF로 인쇄하면 나머지 상태의 핵심 정보(비교 모드 B, 후반 스텝, 타 지표)가 배포본 `deck.pdf`에서 통째로 소실된다.
   - 근거: 초안「런타임·블록 어휘」.

7. **인터랙티브 절제 원칙 부재 ("슬라이드당 최대 1개"만으로는 과잉)**
   - 슬라이드당 1개만 제한하면 18장 덱에 10개 이상의 인터랙션이 들어갈 수 있다. 이는 한 곳에 집중하고 나머지를 조용히 두라는 디자인 원칙을 깨며, 발표 중 조작 부담을 키운다.
   - 근거: [hs-vilab-frontend-design/SKILL.md](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/ref/hs-vilab-frontend-design/SKILL.md) §5, [design-system.md](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/ref/hs-vilab-frontend-design/references/design-system.md) §9.1.

---

## 2. 열린 질문 8개에 대한 답

1. **1920×1080 고정 scale vs 반응형**
   - **권고**: **1920×1080 고정 무대 + `transform: scale()` (레터박스)**.
   - **이유**: 슬라이드는 페이지 단위 줄바꿈·그림 비율·기계 QA(넘침·겹침)가 결정적이어야 한다. 반응형으로 풀면 프로젝터 해상도마다 레이아웃이 달라져 사전 시각 QA가 무효화된다.

2. **statement 슬라이드 구분 방법**
   - **권고**: **`--color-surface-brand`(`#E6F4FC`/다크 `#12263D`) 바탕 + 대형 디스플레이 타입(52–64px) + 상·하단 2px `--color-primary` rule**. (본문 `light`는 `--color-bg`, 결과 `wash`는 `--color-surface-sunken`).
   - **이유**: 남색 풀블리드 금지와 `tokens.css` 대비 기준(`--color-text-muted`도 brand tint 위 5.29:1)을 지키면서 `light / wash / statement` 3단 리듬을 그대로 보존한다.

3. **인터랙티브 블록 목록 및 슬라이드당 1개 제한**
   - **권고**: **`reveal`은 별도 블록에서 빼고 `table`/`figureNumbered` 옵션으로 통합**, 5종(`stepper`, `toggle`, `slider`, `metricSwitch`, `figureZoom`)만 유지. 제한은 **"슬라이드당 ≤1 + 덱 전체 ≤4장(또는 전체의 25% 이하)"**.
   - **이유**: `reveal`은 기존 블록과 스키마가 중복되고, 인터랙션이 덱의 1/4을 넘으면 강연이 아니라 UI 데모 조작이 된다.

4. **수식 렌더링**
   - **권고**: **`dvisvgm` 사전 렌더(인라인 `<svg>`, `fill="currentColor"` 치환 + ID 네임스페이싱) 기본**, TeX 미설치 환경용 **로컬 번들 KaTeX 폴백**. MathML 제외.
   - **이유**: MiKTeX가 이미 있고 사전 SVG는 PDF·오프라인·브라우저 일관성이 완벽하다. MathML은 브라우저별 행렬·분수 정렬 편차가 크다.

5. **단일 HTML 파일 vs 폴더 기본값**
   - **권고**: **폴더(`deck/index.html` + `assets/`)를 기본**, `--single`은 후속 배포 옵션.
   - **이유**: [4] 수정 루프가 빠르고, 에셋/폰트 검증이 쉬우며, `--single`은 폰트 서브셋·발표자 보기 제약이 크다.

6. **발표 대본 형식 (`script.html` vs `docx`)**
   - **권고**: **`script.html`(인쇄/PDF CSS 포함) 단독**으로 충분.
   - **이유**: `python-docx` 의존성을 제거하면서도 수식 SVG·타이밍 합산 경고·태블릿 열람·PDF 인쇄를 한 소스로 해결한다.

7. **HTML 특유의 QA 게이트 추가 항목**
   - **권고**: ① 라이트·다크 양 테마 대비 및 수식 SVG 가시성 ② `file://` 직접 로드 시 외부 HTTP 요청 0건 및 깨진 리소스 ③ 모든 인터랙티브 상태 순회 시 오버플로·CLS·콘솔 에러 ④ `document.fonts` 실제 로드 및 한글 fallback 여부 ⑤ `@media print` 출력 페이지 수 검증.
   - **이유**: HTML 결함은 초기 정적 화면이 아니라 테마 전환·상태 전환·인쇄·오프라인 로딩에서 침묵 속에 터진다.

8. **PPT판에서 버릴 것 vs 반드시 가져올 것**
   - **버릴 것**: PowerPoint COM/AppleScript(`ppt_com.py`, `ppt_mac.py`), `postfont.py`/`fontgate.py`/`glyph_faces.py`, `langtag.py`·`weldKorean()`, `pptxgenjs` 수동 높이 추정(`MEA.txt`/`MEA.spc`), LibreOffice 렌더, `make_script_docx.py`, Okabe-Ito 및 그림 내부 serif 강제.
   - **가져올 것**: `[0]` 논문 선독 후 ≤4질문, `[1]` 역할 분리 팀+`review/log.md`+`research_verified.md`+1e 재검증, `deck.json` 단일 IR과 하드 게이트(`meta.figures` ledger·`provenance`·`cite`·`message`·`note` 상한·경고=빌드에러), `extract_figures.py`(300dpi 크롭)·`apply_text_edits.py`(숫자 변경 차단)·`detect_ai.py`(비전 프로브), `CONVENTIONS` 프리앰블(HTML 규칙으로 갱신)과 폴백 투명 보고.

---

## 3. 빠진 것

- **발표 현장 리모컨(클리커) 키 충돌 프로토콜**: 리모컨은 `PageDown`/`ArrowRight`만 보낸다. `slider`/`toggle`에 포커스가 남아 있으면 화살표가 슬라이드 전환을 가로채 발표가 멈춘다. `stepper`만 `ArrowRight`/`PageDown`으로 내부 스텝을 순차 진행(`#/7/1`→`#/7/2`)하고, 나머지 컨트롤은 숫자키(`1`–`4`)·클릭·`Esc` 포커스 해제로 분리해야 한다.
- **PDF 인쇄용 인터랙티브 전개 정책(`printMode`)**: 상호 배타적 블록은 `deck.json`에 `"default" | "expand"`를 지정해, `expand` 시 `export_pdf.py`가 핵심 상태(예: toggle A/B)를 연속 페이지로 캡처하게 해야 한다.
- **발표자 대본의 인터랙션 큐(`notes.interaction_cue`)**: 발표자가 어느 문장에서 어떤 버튼/단계를 눌러야 하는지 대본과 발표자 노트에 연동되지 않으면 인터랙션이 흐름을 끊는다.
- **1920×1080 프로젝터용 최소 글자 크기 및 그림 축소율 게이트**: `frontend-design`의 12px 하한은 웹용이다. 1920×1080 무대에서는 본문 24–28px, 표/캡션 18–20px, 출처 16px 하한이 필요하다. 또한 CSS `object-fit: contain`은 넘침 없이 그림을 조용히 축소하므로, [block-vocabulary.md](file:///C:/Users/hansung-vilab/AppData/Local/Temp/claude/fb94f9fa00318b9f/880bbcc3-01f2-4525-afc1-78d99856ea91/scratchpad/ref/hs-vilab-deck-skill/hs-vilab-deck/references/block-vocabulary.md) 규칙 3(`MEA.img` 90% 폭 규칙)을 DOM 비율 검사로 옮겨야 한다.
- **오프라인·폰트 서브셋 안전장치**: Playwright `request` 훅으로 외부 요청 0건을 강제하고, 추후 서브셋 시 인터랙티브 숨김 상태의 문자열·수학 기호까지 추출 대상에 포함해야 한다.
- **OS 다크모드 자동 추종 방지**: `tokens.css`의 `@media (prefers-color-scheme: dark)`를 그대로 두면 발표장 PC OS 설정 때문에 의도치 않게 다크로 열려 빔프로젝터 가독성이 깨진다. 덱은 `data-theme="light"`를 기본 고정하고 명시적 전환(`T`)만 허용해야 한다.
- **Q0–Q작업 질문 수 관리**: 초안은 인터랙티브 정도를 추가할지 물었으나 기존 4개 질문이 이미 상한(≤4)이다. 질문을 늘리지 말고 기본값(핵심 2–4장 자동 배치)으로 두고 필요 시 `Q-작업` 체크박스에 1항목으로 흡수하라.

---

## 4. 덜어낼 것

- **`--single` 단일 HTML + `fontTools` 폰트 서브셋(v1 제외)**: 가변폰트 Geomini 서브셋, 숨김 상태 문자 수집, 단일 파일 내 발표자 보기 문제로 v1 복잡도만 폭증한다. v1은 폴더 출력 + `deck.pdf`로 충분하다.
- **별도 창 `presenter.html` + `BroadcastChannel`(v1 제외)**: `file://`에서 동작하지 않는다. v1은 `script.html`(인쇄·태블릿용) + 슬라이드 화면 내 `N` 키 노트 오버레이로 단순화하고, 듀얼 모니터 동기화는 로컬 HTTP 런처가 붙는 v2로 미룬다.
- **자유형 마우스 돋보기 `figureZoom`**: 프로젝터/키보드 발표에서 마우스 추적 돋보기는 조작이 불안정하다. v1에서는 2–3개 지정 영역을 숫자키/버튼으로 확대하는 프리셋 크롭으로 축소하거나 제외하라.
- **일반 bullet의 단계 공개(`fragment`)**: 개조식 목록을 한 줄씩 띄우면 발표 템포가 끊기고 PDF·개요와 어긋난다. 단계 공개는 `stepper`와 `table`/`figureNumbered` 강조에만 허용하라.

---

## 5. 첫 샘플 6장 구성 제안 (Self-Flow 기준)

디자인·토큰·타이포·수식·인터랙션 2종(절제 원칙 반영)을 한 번에 검증하기 위한 6장 구성이다(수치·그림은 `paper.pdf` 추출 실데이터로 채운다).

| 장 | 역할 (`kind` / `tone`) | 블록 구성 | 인터랙션 | 눈으로 검증할 항목 |
|---|---|---|---|---|
| **1** | 표지 (`title`) | Dark Blue 대형 제목 + 부제 + 저자(BFL)·발표 메타 + 얇은 rule + Fig. 1 teaser(흰 매트) | 없음 | 남색 풀블리드 없는 브랜드 인상, Geomini+GmarketSans(Medium/Bold) 혼용 |
| **2** | TL;DR (`statement`) | `--color-surface-brand` 바탕 + `lead`(한 문장 요약) + `cards`(3개: 문제 / Dual-Timestep / 멀티모달 확장) | 없음 | 남색 대체 `statement` 위계, `--radius-panel`(6px), 좌측 바 없음 |
| **3** | 핵심 방법 (`content` / `light`) | 좌측 인라인 SVG 파이프라인 도식 + 우측 `equation`(`dvisvgm` 인라인 SVG + `notation`) + `aria-live` 상태 설명 | **`toggle`** (`1`/`2`키: 표준 Flow Matching ↔ Self-Flow Dual-Timestep + EMA teacher 전환) | 인라인 SVG 토큰 연동, 수식 `currentColor`·ID 충돌 없음, 선택 버튼 대비 |
| **4** | 핵심 결과 차트 (`content` / `wash`) | `--color-surface-sunken` 바탕 + 인라인 SVG 수평 `bars`(Self-Flow만 `--chart-highlight` 강조, 직접 값 라벨) + `callout`(1개) + `cite` | **`metricSwitch`** (논문 주요 벤치마크/지표 전환 시 막대 재정렬·강조 갱신) | `wash` 표면 리듬, `--chart-*` 색+패턴 이중 인코딩, `tabular-nums` |
| **5** | 정량 표 + 정성 그림 (`content` / `wash`) | `table`(외부 인코더 기반 대비 비교, Self-Flow 행 `highlight`, 최고치 700, 무줄무늬) + `figureSide`(논문 원본 크롭, `--color-media-mat`) | 없음(또는 `table` 행 강조 `reveal` 옵션) | 표 최소 글자(≥18px), 원본 그림 90% 스케일·다크모드 흰 매트 |
| **6** | 정리·토론 (`statement`) | `--color-surface-brand` 바탕 + 좌측 핵심 요약(`bullets`) + 우측 논문 근거 토론 질문 3–4개(evidence + consequence) + `note`(interpretation 표기) | 없음 | 세미나 마무리 구도, `note` 표현, `deck.pdf`·`script.html` 연동 |
