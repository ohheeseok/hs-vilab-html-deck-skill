# hs-vilab-html-deck — 계획 (확정 전 검토본)

논문 하나를 받아 **한성대/VILAB 브랜드의 HTML 발표자료**를 만드는 스킬.

- **디자인**은 `hs-vilab-frontend-design`을 따른다: 토큰·색 역할, Geomini + GmarketSans, 역할별 반경, 모션, 인터랙티브 시그니처, SVG 도식·차트, 한국어 카피, 접근성.
- **제작 과정과 내용 채우기**는 `hs-vilab-deck`(PPTX판)을 따른다: 논문 먼저 읽기 → 질문 4개 → preflight → 내러티브 팀 → `deck.json` → 렌더 → 기계 QA + 시각 QA → 수정 → 납품 보고.
- **PPT와 다른 점**: 인터랙티브 요소. 단, 절제한다(§4).
- **독립 실행**: 다른 스킬을 부르지 않는다. 토큰·폰트·한국어 편집 규칙·스캐너·검토 지시문은 스킬 안에 복사·번안해 둔다. codex·agy는 스킬이 아니라 선택적 외부 CLI이며, 없으면 역할별로 입력을 나눈 서브에이전트로 대신하고 그 사실을 납품 보고에 적는다.

논의 기록: `docs/plan-review/` (Claude 초안 → codex·agy 1차 → v2 → codex·agy 2차).

---

## 1. 두 원본이 부딪히는 곳과 결정

| 쟁점 | frontend-design | hs-vilab-deck (PPT) | 결정 |
|---|---|---|---|
| 적용 대상 | "슬라이드용 아님" | PPT 전용 | 사용자 지시 우선. 웹 원칙을 16:9 무대에 번안한 `references/design-system-deck.md`를 새로 씀 |
| 제목 영역 | 흰 바탕, 장식용 남색 풀블리드·그라디언트 금지 | 남색 그라디언트 밴드, 남색 statement 슬라이드 | 밴드 폐기. 흰 바탕 + Dark Blue 제목. TL;DR·정리 = `--color-surface-brand` 바탕 + 큰 타입, 결과 구간 = `--color-surface-sunken` |
| 구간 표시 | 대문자 eyebrow·자간 라벨·`A · B · C` 금지 | 대문자 eyebrow로 구간 표시 | 하단 진행 표시줄에 구간 이름(sentence case)과 위치. 구조가 실제 정보를 담음 |
| 해석 표시 `note` | 왼쪽 색 띠 금지 | 왼쪽 바 | "해석" 단어 라벨로 표시, 띠 없음 |
| 반경 | 역할별 4/6/8, 미디어 2 | 전부 0 | frontend-design |
| 차트·도식 색 | `--chart-*` 토큰, 강조 한 계열 | Okabe-Ito, 그림 속 serif | 우리가 그리는 SVG는 토큰. 논문 원본 그림은 크롭 그대로 흰 매트 위에 |
| 서체 굵기 | 본문 400 (한글 Light) | Medium/Bold만 | 무대 본문 500 (Geomini 500 + Gmarket Medium), 제목 700. 매핑 표는 그대로 두고 쓰는 단계만 고름. Light는 프로젝터에서 획이 날아감 |
| 크기 | 웹 스케일 12–72px | 40/28/24/20/18/16/12pt | 1920×1080 무대 기준 px 래더 (§3) |
| 테마 | 라이트·다크 둘 다 | 흰 바탕 | v1은 라이트 고정(`data-theme="light"`), OS 다크 자동 추종 안 함. 다크는 v1.1 |

## 2. 출력물

```
work/<slug>/
  deck.json          원본 IR — 고치는 곳은 여기뿐
  deck/index.html    발표용 16:9 무대 (+ assets/: 폰트, 그림, 수식 SVG)
  deck/script.html   발표 대본 — 별도 창·태블릿용, 조작 큐 포함, 인쇄 가능
  deck/handout.html  읽기용 — 같은 IR에서 생성한 세로 흐름 문서, 320px부터 재배치
  deck.pdf           배포용 — 슬라이드당 1쪽, 인터랙션 상태를 펼친 쪽은 7a/7b
  qa/                슬라이드 × 상태 스크린샷, scan.json, report.md
  review/            log.md, critic.md, verify.md, korean.md
```

- 폴더가 기본. 압축 해제 후 `index.html` 더블클릭(`file://`), 네트워크 없이 열리는 것이 납품 기준. 외부 CDN 없음.
- 단일 HTML(`--single`)과 폰트 서브셋은 v1 제외.
- 발표 화면에는 대본을 띄우지 않는다(화면 공유 중 노출 위험). 리허설용 노트 오버레이는 `?notes=1`일 때만.

## 3. 무대 엔진 (스킬에 번들, 바닐라 JS 1파일 + CSS)

- 1920×1080 논리 무대를 뷰포트에 맞춰 축소(레터박스). 무대 밖 넘침은 빌드 에러.
- **타입 래더** (무대 px): 80 표지 제목 / 56 슬라이드 제목 / 48 핵심 메시지 / 40 / 36 / 32 본문 / 28 표 본문 / 24 캡션·출처. 24px 미만 금지.
- **키**: PageDown·→·Space 다음, PageUp·← 이전, Home/End, `G` 개요(그리드), `F` 전체화면. 방향키를 쓰는 위젯에 키보드 포커스가 있을 때만 그 위젯이 방향키를 받는다. 마우스 클릭 후에는 포커스를 풀어 클리커가 막히지 않게 하고, 키보드 사용자는 포커스를 유지한다. Esc는 무대로 복귀.
- `stepper`는 "다음" 키로 내부 단계를 먼저 넘긴 뒤 다음 슬라이드로 간다. 해시 `#/7/2`.
- 한성 시그니처 로고: 표지·마무리, 하단 진행 표시줄에 작게.

## 4. 블록과 인터랙션

PPT판 블록을 HTML로 번안: `lead`, `bullets`, `cards`, `callout`(슬라이드당 1), `delta`, `bars`(SVG), `note`, `compare`, `figure`, `figureSide`, `figureNumbered`, `equation`, `table`, `process`, `metrics`.

**인터랙티브 블록 (v1)**: `toggle`(모드 비교 — 한 SVG 도식을 다시 그림), `stepper`(순서가 있는 절차). `metricSwitch`, `slider`(before/after)는 v1.1. `table`·`figureNumbered`에는 행·영역 순차 강조 옵션.

**절제 규칙** (빌드가 검사):
- 대표 인터랙션 0–1개, 인터랙티브 슬라이드 합계 ≤ ⌊슬라이드 수 × 0.2⌋.
- 각 인터랙티브 블록의 필수 필드: `reveals`(조작하면 논문에 대해 무엇이 드러나는가), `start`(발표 시작 상태), `print`(`default` | `expand`), 상태별 수치·캡션의 `provenance`. 결론에 필요한 상태는 PDF·handout에 모두 실린다.
- 키보드로 조작되고, 현재 상태를 보이는 글자 + `aria-live`로 알리며, 스크립트 없이도 의미 있는 기본 상태를 보인다. 감속 모션을 따른다.
- 대본에는 조작 큐(어느 문장에서 무엇을 누르는지)와 시간이 모자랄 때 건너뛸 문장.

## 5. 수식·그림

- 수식: LaTeX → dvisvgm → SVG를 파싱해 기본 전경색만 `currentColor`로, `<defs>` id를 수식별로 바꾸고 내부 참조도 함께 갱신 → 인라인. TeX가 없으면 preflight에서 알림. KaTeX 폴백은 넣지 않음(렌더 경로를 하나로 유지).
- 그림: PDF 영역을 300dpi로 크롭(축·범례 보존, 캡션 제외), 흰 매트 위. 축소 검사는 제약 축 기준 `max(렌더폭/슬롯폭, 렌더높이/슬롯높이) ≥ 0.85`.
- 우리가 그리는 도식·차트는 인라인 SVG, 토큰 색, `role="img"` + `<title>`, 값은 표나 텍스트로도 제공.

## 6. 파이프라인 (PPT판 단계 유지)

[−1] intake → [0] 질문 ≤4 (시간·자리·언어·작업 방식. 인터랙션 수는 묻지 않고 규칙대로) → [0.5] preflight (Python, Playwright+Chromium, TeX, codex·agy 탐지와 비전 프로브) → [1] 내러티브 팀: 작성자(codex 또는 서브에이전트) → 비평가·검증자(서로 모르게) + 조사자(agy, 출처 확인 후 `research_verified.md`만 사용) → `review/log.md`에 모든 지적 수용·기각 → 1회 수정 → 게이트 → `deck.json` → 한국어 편집(번들 규칙 + 스캐너, 숫자 바뀌는 편집은 거부) → 검증자 재검토 → [2] 렌더 → [3] QA → [4] `deck.json`만 고쳐 재빌드 → (Q4) 2차 리뷰 → [5] 납품 보고.

내용 게이트는 그대로: figure ledger(본문 그림·표 전부 use/cut), 슬라이드별 `message`·`cite`, 주장별 `provenance`, `note` 상한, 경고 = 빌드 에러.

## 7. QA (Playwright, Chromium)

**기계 게이트** — 슬라이드 × 인터랙션 상태마다: 무대 넘침, 의도하지 않은 요소 겹침, 글자 크기 하한, 그림 축소율, 렌더된 색으로 계산한 대비, 실제 그려진 글꼴(CDP `CSS.getPlatformFontsForNode`로 한글은 GmarketSans, 라틴은 Geomini인지), `file://` 로드 시 외부 요청 0건과 깨진 리소스 0, 콘솔 에러 0, 키보드만으로 끝까지 진행, 숨은 슬라이드로 탭 이동 안 됨, 감속 모션. PDF는 쪽 수·순서·빈 쪽·잘림. handout은 320px과 200% 확대에서 가로 스크롤 없음.

**시각 게이트** — 스크린샷을 HTML판 디자인 규약(CONVENTIONS)과 함께 agy 비전에 보냄. 1024×768 레터박스 스크린샷에서 표 숫자와 원본 그림 속 라벨까지 읽히는지 본다. agy를 쓸 수 없으면 현재 AI가 보고 납품 보고에 적는다.

**버리는 것**: PowerPoint COM·AppleScript, postfont·fontgate·langtag, pptxgenjs 높이 추정, LibreOffice 렌더, script.docx. 브라우저가 실제로 그린 것을 직접 재므로 대부분 필요 없어짐.

## 8. 스킬 폴더 구조

`hs-vilab-deck-skill`과 같은 형태: 저장소 루트에 README, 스킬은 하위 폴더.

```
hs-vilab-html-deck-skill/
  README.md  docs/PLAN.md  docs/plan-review/
  hs-vilab-html-deck/
    SKILL.md  VERSION  CHANGELOG.md  NOTICE  LICENSES/
    assets/
      tokens.css fonts.css base.css fonts/      frontend-design에서 복사
      engine/deck.css deck.js                   무대 엔진
      brand/                                    한성 시그니처
    references/
      design-system-deck.md   block-vocabulary.md   interaction-rules.md
      narrative-rules.md  narrative-roles.md  handoff-narrative.md
      korean-style.md  qa-checklist.md  platform-notes.md
    schema/deck.schema.json  deck.example.json
    scripts/
      preflight.py detect_ai.py delegate.py extract_figures.py make_equations.py
      build_deck.py qa_render.py scan_dom.py export_pdf.py
      deck_text.py apply_text_edits.py scan_slop.py
```

## 9. 진행 순서

1. **디자인 샘플 6장** (이번 확인용) — 엔진과 블록 몇 개만으로, 전체 파이프라인 전에. 실제 `file://` 폰트 로드도 이 단계에서 확인.
2. 사용자 확인 → 디자인 수정.
3. 나머지 블록, 스키마·빌드 게이트, QA 스크립트, 위임 스크립트, handout·script·PDF.
4. Self-Flow로 전체 덱 1회 끝까지 실행, 결함을 스킬에 반영.

### 첫 샘플 (Self-Flow, 6장)

| # | 슬라이드 | 블록 | 확인할 것 |
|---|---|---|---|
| 1 | 표지 | 제목·저자·소속(Black Forest Labs, MIT)·preprint 날짜(2026-03-04), Fig. 1 teaser(흰 매트), 시그니처 | 남색 밴드 없는 브랜드 인상, 혼용 서체 |
| 2 | TL;DR | statement 바탕, `lead` 한 문장 + 기여를 카드 대신 여백 기반 2열로 | statement 위계 |
| 3 | Dual-Timestep Scheduling | **대표 인터랙션 `toggle`**: Fig. 3을 번안한 토큰 격자 SVG — vanilla FM(모든 토큰 같은 t) ↔ Dual-Timestep(마스크 토큰 s, 나머지 t; teacher는 τ_min = min(t,s)). 식은 Eq. 7 하나 | 인라인 SVG·토큰 색, 수식 SVG, 선택 상태, aria-live |
| 4 | Text-to-image 결과 | 정적 `bars`: Table 2 FID (Vanilla 4.08, SRA 3.70, Ours 3.61, REPA 3.92, SigLIP 2 3.97; 1M steps) | wash 바탕, 차트 규칙, 직접 라벨 |
| 5 | ImageNet 256×256 | `table` 단독: Table 1, Ours 행 강조, 최고치 굵게 | 표 28px, 강조 행 |
| 6 | 정리와 토론 | statement, takeaways + 논문 근거 토론 질문(근거형·대가형, 해석 표시) | 마무리 구도 |

## 10. 샘플 피드백 반영 (2026-11-23)

사용자 피드백 5개를 codex·agy와 논의해 반영했다. 결정과 근거는 `plan-review/05-claude-feedback-synthesis.md`.
statement 슬라이드 다크(`meta.statementTheme`), 표지 선, `panel`·`divider` 블록(슬라이드당 패널 ≤ 2, 덱 40% 이상 패널 없음),
슬라이드당 자동 연출 1개(전환 180ms, 막대 280ms, 강조 행 180ms, 토글 페이드 180ms, 연타 즉시 완료,
`?motion=0` 끔 / `?motion=1` OS의 동작 줄이기 설정을 무시하고 켬), 델타 ↔ 비교쌍 마커.

브랜드 로고: 옛 시그니처 PNG(296×113)를 HSU UI 영문 가로 조합 벡터로 바꿨다(사용자 제공 `.ai` → `scripts/brand_ai2svg.py`로 SVG).
`assets/brand/hsu-signature-en.svg`(HSU 파랑 `#003C90` + 회색, 라이트), `-white.svg`(다크), `-blue.svg`(단색, 예비).
비율 5.73:1. 표지 높이 48px, 푸터 30px. 표지 열이 flex column이라 `align-self:flex-start`가 없으면 로고가 열 폭으로 늘어났다.

표지 발표자: `meta.presenter`(`name` 필수, `affiliation` 문자열 또는 줄 배열)를 표지 오른쪽 열에 둔다(이름 40px, 소속 28px, 그 아래 `meta.event`·`meta.date`, 로고).
리뷰하는 논문의 저자·소속·게재는 부제 아래 24px 회색 두 줄(`cover-credit`)로 내렸다. 자기 연구 발표는 `meta.paper`를 빼거나 `meta.coverCredit: false`.
표지 그림은 남은 높이에 맞춰 줄어든다. QA에 `spill` 검사 추가: 슬라이드 직계 자식(띠) 밖으로 나간 내용, 띠끼리 겹침.

시각 검수 1회차(agy): 13건 중 반영 8, 일부 3, 기각 2. 처리 근거는 `plan-review/07-claude-visual-triage.md`.
엔진에 남은 것: 토글 상태 패널은 큰 상태 높이를 유지, wash 위 차트 격자선 grey-40 + 값 라벨 후광, 다크 진행 표시줄 미진행·지난 구간 색, 표지 여백 축소.

시각 검수 2회차(agy): 1회차 반영 11건 모두 확인, 새 지적 5건(P2) 전부 반영, V02 기각 유지. 처리 근거는 `plan-review/09-claude-visual-triage-r2.md`.
엔진에 남은 것: 진행 표시줄 `flex-basis:0`(구간 길이 = 장 수 비례, 라벨 폭 무관), 토글 패널의 수식 위 8px.

저장소 분리(2026-11-24): 이 폴더를 독립 git 저장소로 만들었다. 논문 PDF와 QA 캡처는 커밋하지 않는다(`.gitignore`).
NOTICE는 이 패키지 기준으로 다시 썼다(글꼴 2종, HSU 시그니처). frontend-design(Apache-2.0)에서 옮긴 글이 아직 없어 해당 항목과 `LICENSES/Apache-2.0.txt`를 뺐다.
`SKILL.md`나 references에 그 글을 옮겨 오면 hs-vilab-frontend-design의 NOTICE 1항과 라이선스 사본을 다시 넣는다.
