# hs-vilab-html-deck — 계획 v2 (1차 검토 반영)

## 1차 검토에서 받아들인 것
- 출력은 폴더 기본(`deck/index.html` + `assets/`), 단일 HTML(`--single`)·폰트 서브셋은 v1 제외.
- 발표자 새 창 + BroadcastChannel은 v1 제외(file://에서 불안정). v1은 같은 창의 노트 오버레이(`N`) + 인쇄 가능한 `script.html`. v2에서 `window.open` 참조 + `postMessage`(origin 무관)로 발표자 창 검토.
- 테마는 라이트 고정이 기본(`data-theme="light"`), OS 다크 자동 추종 안 함. `T`로만 전환. 다크에서도 그림은 흰 매트.
- 수식: dvisvgm 사전 렌더 → 인라인 SVG, fill을 `currentColor`로 치환, `<defs>` id를 수식별로 네임스페이싱. TeX 없으면 preflight 실패로 알림(KaTeX 폴백은 v1 제외).
- 서체 굵기: 무대 본문은 500(Geomini 500 + GmarketSans Medium), 제목 700. 400(Light 매핑)은 무대에서 쓰지 않음 — frontend-design의 매핑 표를 바꾸지 않고 사용 단계만 고름.
- 무대 타입 래더(1920×1080 기준, PPT판 pt 래더를 px로 환산): 80 / 56(제목) / 48(핵심 메시지) / 40 / 36 / 32(본문) / 24(캡션·출처·표 하한). 24px 미만 금지 = 빌드 에러.
- eyebrow/label 충돌: 대문자 eyebrow·자간 라벨·`A · B · C` 금지(frontend-design). 구간 표시는 하단 진행 표시줄(구간 이름 sentence case + 위치)로 옮김 — 구조가 실제 정보(구간)를 인코딩. `note`의 왼쪽 띠 → "해석" 단어 라벨 + 별도 서체 굵기(왼쪽 색 띠 금지).
- statement(TL;DR·정리) = `--color-surface-brand` 바탕 + 큰 타입, 결과 구간 = `--color-surface-sunken`. 남색 풀블리드·그라디언트 밴드 없음. 한성 시그니처 로고는 표지·마무리와 하단 바에 작게.
- 인터랙티브 절제: 덱당 **대표 인터랙션 1개**(signature) + 보조 인터랙션 최대 2개(합계 ≤ 덱의 20%). 각 인터랙티브 블록은 deck.json에 `reveals`(조작하면 무엇이 드러나는가), `start`(발표 시작 상태), `print`(`"default"` | `"expand"` — expand면 상태별로 PDF 페이지를 나눔), 상태별 수치·캡션의 `provenance`를 필수로 가진다.
- v1 인터랙티브 블록: `toggle`(모드 비교, 도식 재작도), `stepper`(순서가 있는 절차/알고리즘), `metricSwitch`(지표 전환 막대 재정렬). `slider`(before/after)는 논문에 쌍 이미지가 있을 때만, v1 후반. `reveal`은 `table`/`figureNumbered` 옵션으로 흡수. `figureZoom`·자유 fragment 제외.
- 클리커 규칙: PageDown/→/Space = 다음. `stepper`는 다음 키로 내부 단계를 먼저 소진한 뒤 다음 슬라이드(해시 `#/7/2`). `toggle`·`metricSwitch`는 숫자키 1–4 또는 클릭. 컨트롤 조작 후 포커스는 덱으로 돌아가 클리커가 막히지 않음. Esc = 포커스 해제.
- 대본에 `cue`(어느 문장에서 무엇을 누르는지) + 시간 부족 시 건너뛸 문장.
- 내용 게이트 그대로 이식: figure ledger, `message`, `cite`, `provenance`, `note` 상한, 경고 = 빌드 에러, 1e 검증자 재검토, `research_verified.md`, Q4 2차 리뷰.
- 독립 실행: 한국어 편집 규칙과 슬롭 스캐너(`scan_slop.py`)를 사용자 소유 `heeseok-korean-anti-slop`에서 번안해 번들. 위임 CLI가 없으면 역할별로 입력을 제한한 별도 서브에이전트/프롬프트, 폴백은 납품 보고에 명시.
- 질문은 4개 유지(시간/자리/언어/작업 방식). 인터랙티브 수는 묻지 않고 규칙대로 자동 배치.

## HTML 특유 QA (Playwright, Chromium)
기계 게이트: 각 슬라이드 × 각 인터랙션 상태 × 라이트/다크에서 — 무대 넘침(scrollHeight/clientWidth), 요소 겹침(의도한 오버레이는 명시), 글자 크기 하한, 그림 축소율(선언 폭의 90% 미만이면 에러 — PPT판 MEA.img 규칙), 대비(렌더된 색으로 계산), `document.fonts` 로드 + 한글/라틴 실제 글리프 face 확인, 외부 요청 0건(file:// 로드), 콘솔 에러 0, 키보드만으로 전체 진행, 숨은 슬라이드의 탭 이동 차단, 감속 모션. PDF: 쪽 수 = 슬라이드 수 + expand 상태 수, 빈 페이지·잘림 없음.
시각 게이트: 스크린샷을 agy 비전에 HTML판 CONVENTIONS와 함께 보냄.
발표 환경: 1024×768·1366×768·1920×1080·2560×1440 레터박스, 한글·공백 경로, 네트워크 차단 시작.

## 열람 모드에 대한 미결정 (2차 검토 요청)
codex: 발표는 16:9, 같은 문서의 읽기 모드는 320px부터 재배치되는 반응형이어야 접근성 하한을 지킨다.
agy: 고정 무대 + scale만. 반응형은 QA를 무력화한다.
Claude 안: v1은 고정 무대 + PDF(배포용)로 끝내고, 반응형 읽기 모드는 v1.1로 미룬다. 근거: 발표 덱의 1차 과업은 발표, 2차는 PDF 배포. 단, 무대 안의 접근성(키보드, 포커스, 대비, 감속 모션, aria-live)은 v1에서 지킨다.

## 첫 샘플 (Self-Flow, 6장, 디자인 확인용 — 전체 파이프라인 전에 엔진·블록만으로)
1. 표지 — 제목·저자·소속·arXiv/발표 정보, Fig. 1 teaser(흰 매트), 한성 시그니처
2. TL;DR (statement) — lead 한 문장 + 기여 카드 2–3개
3. 방법 (signature, `toggle`) — Fig. 3을 번안한 인라인 SVG: 토큰 격자에서 vanilla FM(모든 토큰 같은 t) ↔ Dual-Timestep(마스크 M 토큰은 s, 나머지 t, teacher는 min(t,s)) 전환 + Eq. 4–7 수식 SVG + aria-live 상태 문구
4. 결과 차트 (wash, `bars`; 보조 인터랙션 `metricSwitch`는 표 2 지표가 여러 개일 때만) — 논문 Table 2 실제 값
5. 표 + 그림 (wash) — Table 1 ImageNet, 강조 행, Fig. 4b 등
6. 정리·토론 (statement) — takeaways + 논문 근거 토론 질문(근거형·대가형 섞어서), 해석 표시
