# hs-vilab-html-deck

한성대학교 VILAB의 논문 리뷰·세미나 발표자료를 PPT 대신 **HTML 덱**으로 만드는 스킬입니다.
1920×1080 무대를 브라우저 창에 맞춰 축소·확대해 보여 주고, 노트북 화면과 1024×768 프로젝터에서 같은 배치로 보입니다.
`file://`로 바로 열리고 외부 서버나 웹폰트가 필요 없습니다.

- 디자인: hs-vilab-frontend-design의 토큰·글꼴·규칙(HSU 색, Geomini + Gmarket Sans, 글자 크기 사다리 80/56/48/40/36/32/28/24px, 24px 하한)
- 제작 흐름과 내용 규칙: hs-vilab-deck(PPT판)을 HTML로 옮긴 것
- 한국어 문장 규칙: heeseok-korean-anti-slop 1.3.0의 규칙을 덱용으로 줄여 담고, 네 덱에서 배운 규칙을 더한 것(`references/korean-style.md`, 검사기 `scripts/scan_slop.py`). 다른 스킬을 설치하지 않아도 됩니다.

> **상태: 0.7.0.** 논문 네 편을 덱으로 끝까지 만들었습니다([work/self-flow-full](work/self-flow-full), [work/repa](work/repa), [work/rae](work/rae), [work/vlm-repgen](work/vlm-repgen)). 0.5.0에서 연구 내용 앞의 **overview 애니메이션**(클리커를 누를 때마다 한 구간씩 움직이는 도식)을 넣었고, 0.6.0에서는 그것을 개요 단계부터 계획했고, 0.7.0에서는 한국어 편집 규칙과 검사기를 스킬 안에 담았습니다.
> 스킬 본문은 [hs-vilab-html-deck/SKILL.md](hs-vilab-html-deck/SKILL.md), 변경 내역은 [CHANGELOG.md](hs-vilab-html-deck/CHANGELOG.md)에 있습니다.
> 읽기용 handout(세로 흐름 문서)과 `deck.json` 스키마 파일은 아직 없습니다.

## 샘플

- [work/self-flow-full](work/self-flow-full) — *Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis*(Chefer et al., 2026) 20분 세미나 22장. 이 스킬의 첫 전체 실행입니다.
  - codex가 개요를 쓰고, agy가 비평·검증·자료조사·시각 검수를 맡았습니다. Claude는 조율했습니다.
  - 지적과 처리 기록은 `review/log.md`, `review/visual_triage_r1.md`·`visual_triage_r2.md`에 있습니다.
  - **5번은 overview 애니메이션**입니다. REPA식 외부 encoder 정렬에서 시작해 그 자리에 모델 자신의 EMA teacher가 들어오고, student와 teacher 입력의 noise 수준이 갈라집니다(`figures/overview_selfflow.*`, 논의는 `review/anim/log.md`, 시각 검수는 `review/visual_anim_triage_r1.md`·`r2.md`).
  - **최종본은 [self-flow-full.html](work/self-flow-full/self-flow-full.html) 한 파일**입니다. 글꼴·그림이 모두 들어 있어 이 파일만 옮겨도 열립니다. 대본은 `self-flow-full-script.html`입니다.
  - PDF는 배포용 렌더링 확인에만 씁니다(`export_pdf.py`).
- [work/repa](work/repa) — *Representation Alignment for Generation*(REPA, Yu et al., ICLR 2025) 20분 세미나 22장. 두 번째 전체 실행입니다.
  - 진단(확산 transformer의 표현 격차) → 처방(외부 인코더 정렬) 줄기. 7번은 학습 경로를 한 단계씩 보이는 stepper, 10·13번은 그림 탭입니다.
  - **4번은 overview 애니메이션**입니다. 28개 block의 SiT 하나에 깨끗한 이미지의 DINOv2 경로가 더해지고, SiT가 8층에서 나뉘어 그 출력이 패치 표현에 정렬됩니다(`figures/overview_repa.*`, 논의는 `review/anim/log.md`, 시각 검수는 `review/visual_anim_triage_r1.md`·`r2.md`).
  - 처리 기록은 `review/log.md`, `verify2_triage.md`, `visual_triage_r1.md`·`visual_triage_r2.md`에 있습니다.
  - **최종본은 [repa.html](work/repa/repa.html)**, 대본은 `repa-script.html`입니다.
- [work/rae](work/rae) — *Diffusion Transformers with Representation Autoencoders*(RAE, Zheng et al., 2025) 20분 세미나 22장. 세 번째 전체 실행입니다.
  - 논문이 겨냥한 두 통념(① 의미 인코더는 복원을 못 한다, ② 확산은 고차원 latent에서 안 된다)을 하나씩 따라가는 줄기. 14번은 설계 변경을 하나씩 더할 때의 gFID 막대 stepper, 16번은 그림 탭입니다.
  - **4·5번은 overview 애니메이션**입니다. 4번은 SD-VAE latent가 RAE latent로 바뀌는 과정(Fig. 2를 다시 그림), 5번은 RAE 위의 복원·생성 경로와 네 가지 변경이 붙는 곳입니다. 도식은 `figures/overview_*.svg`, 움직임은 `figures/overview_*.anim.js`에 있습니다.
  - 처리 기록은 `review/log.md`, `verify2_triage.md`, `visual_triage_r1.md`·`visual_triage_r2.md`, 애니메이션 논의는 `review/anim/log.md`에 있습니다.
  - **최종본은 [rae.html](work/rae/rae.html)**, 대본은 `rae-script.html`입니다.
- [work/vlm-repgen](work/vlm-repgen) — *Let Vision-Language Models Generate Images through Their Representations*(Integral, Kim et al., 2026) 20분 세미나 21장. 네 번째 전체 실행입니다.
  - 이해와 생성이 같은 시각 표현을 쓰면 재구성 품질로 설명되지 않는 생성 이득이 생긴다는 주장을 통제 비교로 따라가는 줄기. 13번은 지식 생성·편집 그림 탭, 15번은 통제 비교 네 가지를 같은 축으로 넘겨 보는 대표 toggle, 16번은 각 비교가 지운 설명과 남은 설명을 정리한 표입니다.
  - **5번은 overview 애니메이션**입니다. 별도 VAE latent와 층마다 붙은 생성 expert에서 시작해, latent 자리에 AF의 공유 토큰 z가 들어오고, 생성 stream이 VLM을 읽는 곳이 네 층마다로 줄어듭니다(`figures/overview_integral.*`, 생성 스크립트 `make_overview_integral.py`).
  - 처리 기록은 `review/log.md`, `verify2_triage.md`, `visual_triage_r1.md`·`visual_triage_r2.md`에 있습니다.
  - **최종본은 [vlm-repgen.html](work/vlm-repgen/vlm-repgen.html)**, 대본은 `vlm-repgen-script.html`입니다.

| 키 | 동작 |
|---|---|
| PageDown · → · Space | 다음 (stepper는 단계부터, 애니메이션은 한 구간씩 재생. 재생 중에 누르면 그 구간을 바로 끝냄) |
| PageUp · ← | 이전 |
| Home / End | 처음 / 끝 |
| 1–9 | 현재 슬라이드 토글 상태 선택 |
| G | 전체 보기 |
| M | 모션 끄기/켜기 (느린 PC에서는 애니메이션이 구간마다 바로 넘어감) |
| F | 전체 화면 |
| Esc | 돌아가기 |

모션은 기본으로 켜져 있습니다. OS에서 '애니메이션 효과'나 '동작 줄이기'를 꺼 둔 PC에서도 파일을 그냥 열면 모션이 나옵니다. 주소 뒤에 `?motion=0`을 붙이면 모션이 모두 꺼지고, `?motion=auto`를 붙이면 OS 설정을 따릅니다. 덱의 기본값은 `deck.json`의 `meta.motion`(`on` · `auto` · `off`)으로 바꿀 수 있습니다.

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
    scan_slop.py       한국어 문체 후보 검사기(heeseok-korean-anti-slop 1.3.0에서 그대로 가져옴)
    brand_ai2svg.py    윤곽선 .ai → 여백 없는 SVG
  SKILL.md  VERSION  CHANGELOG.md  NOTICE
  references/          내러티브 규칙·역할, 블록, 인터랙션, 디자인, QA, 한국어 편집
docs/
  PLAN.md              확정 계획과 변경 기록
  plan-review/         codex·agy 검토와 시각 검수 기록
work/self-flow-full/   전체 실행
  deck.json            슬라이드 내용(빌드의 입력)
  deck/assets/fig/     논문 그림 크롭과 토큰 격자(입력)
  outline*.md review/  개요와 codex·agy 검토·처리 기록
  self-flow-full.html  최종본(단일 파일) · self-flow-full-script.html 대본
work/repa/             두 번째 전체 실행(같은 구성, figures/에 새로 그린 도식)
work/rae/              세 번째 전체 실행(같은 구성, figures/에 overview 애니메이션 두 개)
work/vlm-repgen/        네 번째 전체 실행(같은 구성, figures/에 overview 애니메이션 하나)
```

`deck/assets/math/`는 수식 SVG 캐시입니다. 저장소에 두면 TeX 없이도 같은 최종본이 다시 빌드됩니다. `deck/`의 나머지(엔진·글꼴·로고 사본, `index.html`)는 빌드할 때마다 다시 생기므로 저장소에 넣지 않습니다.

## 빌드와 QA

필요한 것은 아래와 같습니다.
- Python 3.10 이상
- `latex`와 `dvisvgm`(MiKTeX 또는 TeX Live)
- `pillow`(최종본에 넣을 그림을 WebP로 압축)
- QA·PDF용 `playwright`와 Chromium
- 그림 추출·PDF 병합·로고 변환용 `pymupdf`

```
python hs-vilab-html-deck/scripts/preflight.py
python hs-vilab-html-deck/scripts/build_deck.py work/self-flow-full
python hs-vilab-html-deck/scripts/qa_render.py work/self-flow-full
python hs-vilab-html-deck/scripts/qa_render.py work/self-flow-full --viewport 1024x768
python hs-vilab-html-deck/scripts/qa_render.py work/self-flow-full --html work/self-flow-full/self-flow-full.html
python hs-vilab-html-deck/scripts/export_pdf.py work/self-flow-full
```

빌드는 `deck/`과 최종본 `self-flow-full.html`을 함께 다시 만듭니다. QA 캡처(`qa/`)와 PDF는 저장소에 넣지 않습니다.

## 라이선스

코드와 문서는 [MIT 라이선스](LICENSE)입니다.

다음은 MIT 라이선스에 포함되지 않고 각자의 조건을 따릅니다. 출처와 조건은 [hs-vilab-html-deck/NOTICE](hs-vilab-html-deck/NOTICE)에 있습니다.
- 함께 넣은 글꼴(Geomini, Gmarket Sans): SIL Open Font License 1.1
- HSU 시그니처: 한성대학교 소유의 학교 로고
- 샘플의 논문 그림 조각: 저작권이 논문 저자에게 있음
