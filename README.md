# hs-vilab-html-deck

한성대학교 VILAB의 논문 리뷰·세미나 발표자료를 PPT 대신 **HTML 덱**으로 만드는 스킬입니다.
1920×1080 무대를 브라우저 창에 맞춰 축소·확대해 보여 주고, 노트북 화면과 1024×768 프로젝터에서 같은 배치로 보입니다.
`file://`로 바로 열리고 외부 서버나 웹폰트가 필요 없습니다.

- 디자인: hs-vilab-frontend-design의 토큰·글꼴·규칙(HSU 색, Geomini + Gmarket Sans, 글자 크기 사다리 80/56/48/40/36/32/28/24px, 24px 하한)
- 제작 흐름과 내용 규칙: hs-vilab-deck(PPT판)을 HTML로 옮긴 것

> **상태: 개발 중.** 무대 엔진, 빌드, 수식, QA와 6장짜리 샘플 덱까지 만들었습니다.
> `SKILL.md`, 스키마, 나머지 블록, handout·script·PDF 내보내기는 아직 없습니다. 진행 계획은 [docs/PLAN.md](docs/PLAN.md) §9에 있습니다.

## 샘플

[work/self-flow](work/self-flow)는 *Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis*(Chefer et al., 2026) 리뷰 6장입니다.
표지, 다크 요약, 토글 인터랙션 도식, 막대 차트, 표, 정리와 토론으로 구성했습니다.
`work/self-flow/deck/index.html`을 브라우저로 열면 됩니다.

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
    build_deck.py      deck.json → deck/index.html, 게이트 위반 시 아무것도 쓰지 않음
    make_equations.py  LaTeX → 인라인 SVG (Arev Sans 수식, dvisvgm)
    qa_render.py       Playwright 캡처 + 기계 QA (넘침, 24px 하한, 대비, 글꼴, 구역 겹침)
    brand_ai2svg.py    윤곽선 .ai → 여백 없는 SVG
  NOTICE
docs/
  PLAN.md              확정 계획과 변경 기록
  plan-review/         codex·agy 검토와 시각 검수 기록
work/self-flow/        샘플: deck.json, 손으로 그린 도식 SVG, 빌드 결과
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

포함한 글꼴과 HSU 시그니처의 출처·조건은 [hs-vilab-html-deck/NOTICE](hs-vilab-html-deck/NOTICE)에 있습니다.
