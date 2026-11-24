# hs-vilab-html-deck — 초안 계획 (Claude 작성, codex·agy 검토용)

## 목표
논문(주로 AI/CV) 하나를 받아 **한성대/VILAB 브랜드의 HTML 발표자료**를 만드는 스킬.
- 디자인: `hs-vilab-frontend-design`의 지침(토큰, 서체, 색 역할, 반경, 모션, 인터랙티브 시그니처, SVG 도식/차트, 한국어 카피, 접근성 하한)을 따른다.
- 제작 과정·내용 채우기: `hs-vilab-deck`의 지침(논문 먼저 읽기 → 질문 ≤4개 → preflight → 내러티브 팀(작성자 codex, 비평가·검증자 서브에이전트, 조사자 agy, 한국어 편집자) → IR(deck.json) → 렌더 → 기계 QA + 시각 QA(agy) → 수정 루프 → 납품 보고)을 따른다.
- PPT와 다른 점: HTML이므로 인터랙티브 요소가 들어간다.
- **독립 실행**: 다른 스킬에 의존하지 않는다. 필요한 토큰·폰트·규칙·스크립트는 모두 스킬 안에 복사·번안해 둔다. (codex·agy는 "스킬"이 아니라 외부 CLI 위임이므로 선택 사항, 없으면 현재 AI로 대체하고 보고.)

## 두 원본 지침의 충돌과 해소안
| 쟁점 | frontend-design | hs-vilab-deck(PPT) | 해소안 |
|---|---|---|---|
| 적용 대상 | "슬라이드·PPT용 아님" | PPT 전용 | 사용자 지시가 우선. 웹 디자인 원칙을 16:9 고정 무대에 번안한 `design-system-deck.md`를 새로 쓴다 |
| 제목 영역 | 흰 바탕 기본, 장식용 남색 풀블리드 금지 | 남색 제목 밴드, statement 슬라이드는 남색 바탕 | 남색 밴드 폐기. 흰 바탕 + Dark Blue 제목 + 얇은 rule. statement(TL;DR·정리)는 `--color-surface-brand` 또는 큰 타입으로 구분(남색 풀블리드 X) |
| 반경 | 역할별(4/6/8, 미디어 2) | 전부 0 | frontend-design 따름 |
| 차트 색 | 토큰 `--chart-*`(잉크 우선, 강조 1개 Sky Blue) | Okabe-Ito, 그림 내부 serif | 우리가 그리는 차트·도식은 토큰. 논문 원본 그림은 크롭 그대로 흰 매트 위에 |
| 서체 크기 | 웹 스케일(12–72px) | 40/28/24/20…pt 래더 | 1920×1080 무대 기준 슬라이드용 스케일 별도 정의(최소 글자 크기 하한 포함) |
| 강조 | warm은 2–4px 마커만 | warm 카드 띠, callout 채움 | frontend-design 따름. callout은 슬라이드당 1개 규칙만 유지 |

## 출력물
```
work/<slug>/
  deck.json        원본(IR) — 수정은 여기서
  deck/index.html  발표용 (assets/ 폴더 동반)  + 옵션 --single 로 단일 HTML(폰트·이미지 인라인, 폰트는 사용 글자만 subset)
  deck.pdf         인쇄/배포용 (Playwright로 각 슬라이드 기본 상태 출력)
  script.html      발표 대본(인쇄 가능) — PPT판의 script.docx 대체
  qa/              슬라이드별 스크린샷(인터랙션 상태 포함) + scan.json + report.md
  review/          log.md, critic.md, verify.md, korean.md
```

## 런타임(덱 엔진) — 스킬에 번들
- 슬라이드는 1920×1080 논리 무대, 뷰포트에 맞춰 scale (레터박스). 무대 밖 넘침 = 빌드 에러.
- 키보드: ←/→/Space/PageUp/Down, Home/End, 숫자+Enter 이동, `O` 개요(그리드), `P` 발표자 보기(새 창, BroadcastChannel 동기화, 대본·다음 슬라이드·타이머), `T` 테마(라이트 기본/다크), `F` 전체화면.
- URL 해시 `#/7`, `#/7/2`(단계)로 딥링크. 인쇄 CSS: 한 장에 한 슬라이드, 인터랙티브는 기본 상태.
- 단계 공개(fragment): 허용하되 규칙 — 슬라이드 기본 상태(모든 단계 공개)가 인쇄·PDF·개요에서 의미가 있어야 함.
- 외부 CDN 금지(오프라인 발표장). JS는 의존성 없는 바닐라 1파일.

## 블록 어휘
PPT판의 블록을 HTML로 번안: lead, bullets, cards, callout, delta, bars(SVG), note, compare, figure, figureSide, figureNumbered, equation, table, process, metrics.
**인터랙티브 블록(신규)** — 슬라이드당 최대 1개, "조작하면 주제에 대해 무엇이 드러나는가"를 deck.json에 한 줄로 적어야 빌드 통과:
- `stepper` — 알고리즘/파이프라인을 단계별로 진행, 하나의 SVG 도식이 단계마다 다시 그려짐
- `toggle` — 모드 버튼(aria-pressed)으로 같은 도식/그림의 변형을 비교 (예: Flow Matching vs Self-Flow)
- `slider` — before/after 이미지 비교, 또는 연속 변수(시간 t, noise level) 스크러버
- `metricSwitch` — 지표 선택 시 막대차트 재정렬, 논문 모델 하이라이트
- `reveal` — 표의 행/그림의 영역을 순서대로 강조(발표 동선 지원)
- `figureZoom` — 원본 그림 확대(돋보기) — 복잡한 Figure의 부분 읽기
모든 인터랙티브: 키보드 조작, 현재 상태를 aria-live 텍스트로 표시, 스크립트 없이도 의미 있는 기본 상태, 감속 모션 존중.

## 수식
LaTeX → SVG(dvisvgm, MiKTeX/TeX Live) 사전 렌더. 없으면 KaTeX 번들을 폴백? (검토 필요)

## 파이프라인(PPT판 단계 유지)
[-1] intake → [0] 질문 ≤4 (시간/자리/언어/작업방식 — 인터랙티브 정도를 추가할지?) → [0.5] preflight(python, playwright+chromium, TeX, codex/agy 탐지·비전 프로브) → [1] 내러티브 팀 → outline.md → 리뷰 → deck.json(+ interactive 의도) → 한국어 편집(규칙을 스킬 안에 번들) → 검증자 재검토 → [2] 렌더(build_deck.py: deck.json → HTML) → [3] QA: (a) 기계 게이트 — Playwright로 각 슬라이드·각 인터랙션 상태를 열고 DOM 측정(무대 넘침, 요소 겹침, 최소 글자 크기, 폰트 실제 로드·글리프 fallback, 대비, 키보드 접근, 콘솔 에러), 스크린샷 (b) 시각 게이트 — agy 비전 → [4] 수정(deck.json만 고치고 재빌드) → [5] 납품 보고

## 스킬 폴더 구조(안)
```
hs-vilab-html-deck/
  SKILL.md, VERSION, CHANGELOG.md, README.md
  assets/
    tokens.css fonts.css base.css fonts/(woff2 + LICENSES)   ← frontend-design에서 복사
    engine/deck.css deck.js presenter.html                   ← 런타임
  references/
    design-system-deck.md   (frontend-design을 무대에 번안)
    narrative-rules.md narrative-roles.md handoff-narrative.md (deck에서 번안)
    block-vocabulary.md interactive-patterns.md qa-checklist.md korean-style.md
  schema/deck.schema.json deck.example.json
  scripts/
    preflight.py detect_ai.py delegate.py extract_figures.py make_equations.py
    build_deck.py qa_render.py (Playwright) scan_dom.py deck_text.py apply_text_edits.py export_pdf.py
```

## 검증 계획
1. 엔진+블록 몇 개로 샘플 5~6장(표지, TL;DR, 방법(인터랙티브), 결과 차트, 표, 정리·토론)을 self_flow.pdf로 만들어 사용자 눈으로 디자인 확인.
2. 승인 후 나머지 블록·QA·위임 스크립트 완성, 전체 덱 1회 end-to-end.

## 열린 질문 (검토자에게)
1. 무대 크기 1920×1080 고정 scale vs 반응형 — 발표용 HTML로 무엇이 맞나?
2. statement 슬라이드 구분 방법(남색 풀블리드 금지 아래에서)
3. 인터랙티브 블록 목록이 적절한가, 빠진 것/과한 것? 슬라이드당 1개 제한은 적절한가?
4. 수식: dvisvgm SVG vs KaTeX 번들 vs MathML
5. 단일 HTML 파일 vs 폴더 — 기본값
6. 발표 대본: script.html만으로 충분한가, docx도 필요한가
7. QA 게이트로 추가해야 할 HTML 특유의 결함
8. PPT판에서 버려도 되는 것(PowerPoint·폰트 스탬핑 관련 전부)과 반드시 가져와야 하는 것
