# hs-vilab-html-deck

한성대학교 VILAB의 논문 리뷰·세미나 발표자료를 PPT 대신 **HTML 덱**으로 만드는 스킬입니다.
1920×1080 무대를 브라우저 창에 맞춰 축소·확대해 보여 주고, 노트북 화면과 1024×768 프로젝터에서 같은 배치로 보입니다.
`file://`로 바로 열리고 외부 서버나 웹폰트가 필요 없습니다.

- 디자인: hs-vilab-frontend-design의 토큰·글꼴·규칙(HSU 색, Geomini + Gmarket Sans, 글자 크기 사다리 80/56/48/40/36/32/28/24px, 24px 하한)
- 제작 흐름과 내용 규칙: hs-vilab-deck(PPT판)을 HTML로 옮긴 것

> **상태: 0.2.0.** 논문 한 편을 21장 덱으로 끝까지 만들어 본 첫 실행을 마쳤습니다([work/self-flow-full](work/self-flow-full)).
> 스킬 본문은 [hs-vilab-html-deck/SKILL.md](hs-vilab-html-deck/SKILL.md), 변경 내역은 [CHANGELOG.md](hs-vilab-html-deck/CHANGELOG.md)에 있습니다.
> 읽기용 handout(세로 흐름 문서)과 `deck.json` 스키마 파일은 아직 없습니다.

## 샘플

- [work/self-flow-full](work/self-flow-full) — *Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis*(Chefer et al., 2026) 20분 세미나 21장. 이 스킬의 첫 전체 실행입니다.
  - codex가 개요를 쓰고, agy가 비평·검증·자료조사·시각 검수를 맡았습니다. Claude는 조율했습니다.
  - 지적과 처리 기록은 `review/log.md`, `review/visual_triage_r1.md`에 있습니다.
  - **최종본은 [self-flow-full.html](work/self-flow-full/self-flow-full.html) 한 파일**입니다. 글꼴·그림이 모두 들어 있어 이 파일만 옮겨도 열립니다. 대본은 `self-flow-full-script.html`입니다.
  - PDF는 배포용 렌더링 확인에만 씁니다(`export_pdf.py`).
- [work/self-flow](work/self-flow) — 같은 논문의 디자인 샘플입니다(6장 + 마무리). 엔진과 표지를 정할 때 썼습니다. 최종본은 `self-flow.html`입니다.

| 키 | 동작 |
|---|---|
| PageDown · → · Space | 다음 (토글이 있으면 상태부터) |
| PageUp · ← | 이전 |
| Home / End | 처음 / 끝 |
| 1–9 | 현재 슬라이드 토글 상태 선택 |
| G | 전체 보기 |
| F | 전체 화면 |
| Esc | 돌아가기 |

주소 뒤에 `?motion=0`을 붙이면 모든 모션이 꺼집니다. `?motion=1`을 붙이면 OS의 '동작 줄이기' 설정과 상관없이 모션이 켜집니다.

샘플의 논문 그림 조각(`deck/assets/fig/`)은 리뷰 목적으로 인용한 것이고, 저작권은 논문 저자에게 있습니다. 논문 PDF는 저장소에 넣지 않습니다.

## 구성

```
hs-vilab-html-deck/          스킬 본체
  assets/
    tokens.css fonts.css base.css fonts/   디자인 토큰·글꼴 (hs-vilab-frontend-design)
    engine/deck.css deck.js                무대 엔진 (의존성 없는 바닐라 JS)
    brand/                                 HSU 영문 가로 시그니처 SVG
  scripts/
    preflight.py       환경 점검(Python, Playwright, TeX, 글꼴, codex·agy)
    delegate.py        codex·agy에 한 단계씩 넘기고 결과 파일을 받음(없으면 대체를 알림)
    extract_figures.py 논문 텍스트·그림 목록·영역 크롭(400 dpi)
    build_deck.py      deck.json → deck/ + 최종본 <slug>.html(단일 파일), 게이트 위반 시 아무것도 쓰지 않음
    bundle_html.py     글꼴·CSS·JS·그림을 넣은 단일 HTML(빌드가 호출)
    make_equations.py  LaTeX → 인라인 SVG (Arev Sans 수식, dvisvgm)
    qa_render.py       Playwright 캡처 + 기계 QA (넘침, 띠 이탈, 글자 겹침, 24px 하한, 대비, 글꼴)
    export_pdf.py      배포용 렌더링 확인 PDF(토글 상태는 쪽을 나눠 펼침) + 쪽별 겹침 검사
    deck_text.py · apply_text_edits.py   한국어 편집 표를 뽑고 적용(숫자 바뀌는 행은 거부)
    brand_ai2svg.py    윤곽선 .ai → 여백 없는 SVG
  SKILL.md  VERSION  CHANGELOG.md  NOTICE
  references/          내러티브 규칙·역할, 블록, 인터랙션, 디자인, QA, 한국어 편집
docs/
  PLAN.md              확정 계획과 변경 기록
  plan-review/         codex·agy 검토와 시각 검수 기록
work/self-flow-full/   전체 실행: deck.json, outline, review/ 기록, 빌드 결과
work/self-flow/        디자인 샘플 6장
```

## 빌드와 QA

필요한 것은 아래와 같습니다.
- Python 3.10 이상
- `latex`와 `dvisvgm`(MiKTeX 또는 TeX Live)
- QA용 `playwright`와 Chromium
- 로고 변환용 `pymupdf`(로고를 바꿀 때만)

```
python hs-vilab-html-deck/scripts/build_deck.py work/self-flow
python hs-vilab-html-deck/scripts/qa_render.py work/self-flow
python hs-vilab-html-deck/scripts/qa_render.py work/self-flow --viewport 1024x768
```

QA 캡처는 `work/self-flow/qa/`에 생기고, 저장소에는 넣지 않습니다.

## 라이선스

코드와 문서는 [MIT 라이선스](LICENSE)입니다.

다음은 MIT 라이선스에 포함되지 않고 각자의 조건을 따릅니다. 출처와 조건은 [hs-vilab-html-deck/NOTICE](hs-vilab-html-deck/NOTICE)에 있습니다.
- 함께 넣은 글꼴(Geomini, Gmarket Sans): SIL Open Font License 1.1
- HSU 시그니처: 한성대학교 소유의 학교 로고
- 샘플의 논문 그림 조각: 저작권이 논문 저자에게 있음
