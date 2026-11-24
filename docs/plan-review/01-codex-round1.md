## 1. 치명적 문제

- **고정 무대를 모든 화면에 축소하면 디자인 원본의 접근성 하한을 어깁니다.** 1920px 무대를 320px에 맞추면 36px 본문이 6px로 보입니다. 발표 모드에는 16:9 무대를 쓰고, 같은 문서의 읽기 모드에는 320px부터 세로로 재배치되는 레이아웃을 적용하십시오. 자바스크립트 없이 열거나 200% 확대해도 본문과 표를 읽을 수 있어야 합니다. 근거는 frontend-design `SKILL.md` §1·§12, `design-system.md` §5, `ui-audit.md` §1·§5입니다.
- **블록마다 상호작용을 하나씩 허용하면 덱 전체가 조작 위주로 흐를 수 있습니다.** 원본은 주제에 고유한 대표 인터랙션 하나를 정하고, 구현 전에 배치와 읽기 순서를 검토하도록 합니다. 초안의 ‘의도 한 줄’은 입력 유무만 검사합니다. 덱 단위 설계안에서 대표 인터랙션, 조작으로 드러나는 차이, 조작 없이 전달할 결론을 먼저 정하십시오. 근거는 frontend-design `SKILL.md` §3–5, `design-system.md` §9.1입니다.
- **‘모든 단계 공개’와 ‘기본 상태 출력’은 서로 다른 규칙입니다.** 순차 공개는 한 장으로 합칠 수 있지만, 두 모드를 교체하는 도식이나 비교 슬라이더는 동시에 공개할 수 없습니다. 각 블록에 **발표 시작 상태**와 **배포용 정적 표현**을 정의하십시오. PDF·개요·무스크립트 읽기에서 최종 조작 상태와 무관하게 핵심 증거를 읽을 수 있어야 합니다. 근거는 frontend-design `design-system.md` §9.1·§9.3, deck `narrative-rules.md` §1–2입니다.
- **`deck.json`을 만든다는 설명만으로는 PPT판의 검증 절차가 보존되지 않습니다.** 본문 그림·표 전수 목록과 채택·제외 사유, 채택 항목의 실제 표시, 슬라이드별 `message`·`cite`, 주장별 `provenance`를 빌드에서 검사하십시오. PPT 스키마는 블록 옵션을 느슨하게 받으므로 HTML 인터랙션에는 별도 타입 검증이 필요합니다. 상태에 따라 바뀌는 수치·캡션도 같은 출처 검증과 한국어 편집 후 재검증을 거쳐야 합니다. 근거는 deck `SKILL.md` [1a]–[1e], `narrative-rules.md` §1–2, `deck.schema.json`의 `slides.items`와 `x-blockOptions`입니다.
- **독립 실행의 조건이 빠져 있습니다.** CLI가 없을 때 한 에이전트가 한 프롬프트에서 작성과 검증을 모두 맡으면 원본의 교차 검토가 사라집니다. 역할별 입력을 제한한 별도 세션이나 프롬프트를 쓰고, 수행 주체와 폴백을 기록하십시오. 외부 조사와 비전 위임은 선택 사항이며, 조사 결과는 원출처 확인 후에만 반영합니다. 설치된 다른 스킬의 경로 없이도 실행되도록 한국어 규칙·검토 지시문·폰트 라이선스·번안 고지를 번들하고, 깨끗한 Windows 환경에서 검증하십시오. 근거는 deck `SKILL.md` [0]·[1a′]·[1d], `narrative-roles.md`의 *The roles*·*The loop*, frontend-design `SKILL.md` 서두·§2입니다.
- **오프라인 납품과 발표자 창의 실행 방식이 정해지지 않았습니다.** `file://` 더블클릭과 HTTP 실행은 출처와 저장소 조건이 다릅니다. 로컬 파일 간 `BroadcastChannel` 동기화에 기대면 환경별로 발표자 보기가 실패할 수 있습니다. 기본 경로를 `file://` 단일 창으로 고정하고, 실제 납품 폴더를 네트워크를 끈 상태에서 열어 검증하십시오. 원본 근거는 frontend-design `SKILL.md` §2–3, deck `qa-checklist.md`의 *The visual pass*입니다. [WHATWG URL 표준](https://url.spec.whatwg.org/#origin), [WHATWG HTML 메시징 표준](https://html.spec.whatwg.org/multipage/web-messaging.html#broadcasting-to-other-browsing-contexts)

## 2. 열린 질문 8개에 대한 답

| 질문 | 권고와 이유 |
|---|---|
| 1. 고정 무대 vs 반응형 | **발표는 16:9, 열람은 반응형.** 1920×1080은 제작 좌표로 쓰고, 글자와 버튼의 하한은 축소 후 실제 화면에서 검사합니다. |
| 2. Statement 구분 | **브랜드 틴트 배경과 큰 왼쪽 정렬 문장.** TL;DR과 정리에만 같은 위계를 적용하고, 평행한 기여점은 여백으로 묶습니다. |
| 3. 인터랙티브 목록과 제한 | **v1은 `toggle`과 `stepper` 중 덱당 하나.** 한 번의 조작으로 비교나 인과 순서를 설명할 수 있는 장에 배치합니다. 확대는 공통 열람 기능으로 봅니다. |
| 4. 수식 | **dvisvgm SVG 사전 렌더.** 원본 LaTeX와 읽을 수 있는 수식 설명·기호 풀이를 함께 보존합니다. TeX는 수식 생성이 필요한 덱에서 검사합니다. |
| 5. 단일 HTML vs 폴더 | **폴더를 기본으로 하고 ZIP으로 전달.** 그림과 폰트를 개별 검증하기 쉽습니다. 압축 해제 후 더블클릭하는 경로를 납품 기준으로 삼습니다. |
| 6. 발표 대본 | **인쇄 가능한 `script.html`이면 충분합니다.** 같은 IR에서 슬라이드 번호, 설명 순서, 예상 시간, 조작 큐와 생략 멘트를 생성합니다. |
| 7. HTML QA | **실제 배포 경로별 합격 기준을 둡니다.** 발표·읽기·인쇄·무스크립트에서 내용과 탐색을 확인하고, 지원 브라우저·OS를 보고합니다. |
| 8. PPT판에서 가져올 것 | **내용 게이트와 실제 렌더 검수를 가져옵니다.** 채택 목록·출처·대본·편집 후 재검증·최종 빌드 재검수는 유지합니다. COM·폰트 스탬핑·절대좌표 배치는 브라우저 글리프 검사와 CSS 흐름 배치로 대체합니다. |

## 3. 빠진 것

- **발표 동선.** 클릭커의 PageUp/PageDown은 장 이동에 쓰고, 컨트롤에 포커스가 있을 때 방향키·Space는 해당 컨트롤에 맡깁니다. 다시 들어왔을 때의 상태와 잘못된 해시의 복구 규칙을 정하십시오. 대본에는 조작 한 번의 큐와 시간 부족 시 바로 넘길 멘트를 넣습니다.
- **실제 발표 환경.** 캐시 없는 오프라인 시작, 한글·공백 경로, 1024×768 프로젝터, 화면 공유 중 창 크기 변경, 전체화면 해제를 시험하십시오. 글꼴 로드 성공과 실제 한글·라틴·기호의 렌더링을 각각 확인합니다. 팝업과 저장소가 막혀도 본 발표와 PDF를 열 수 있어야 합니다.
- **브라우저·인쇄 QA.** 320px·200% 확대, Windows 강제 색상, 감속 모션, 숨긴 슬라이드의 탭 순서, 보이는 포커스, 상태 안내 중복을 확인하십시오. PDF는 쪽 수·순서·빈 페이지·그림 잘림을 검사합니다. DOM 겹침 검사에서는 의도한 오버레이를 명시하고, 레이아웃 결함은 CSS·엔진에서, 내용 결함은 IR에서 고친 뒤 최종본을 다시 검사합니다.

## 4. 덜어낼 것

v1에서는 발표자 팝업·동기화, 숫자 입력 점프, 범용 fragment, 연속 슬라이더, 단일 HTML 서브셋 패키징, 다중 수식 렌더러를 미루십시오. 6장 샘플에서 **그림·수식·차트·표·대표 인터랙션·읽기·PDF**까지 먼저 연결하면, 나머지 블록을 만들기 전에 발표와 배포에서 문제가 드러납니다.

## 5. Self-Flow 첫 샘플 6장

랩 세미나를 가정한 디자인 검토용 샘플입니다. 3장에서만 조작하고, 나머지는 클릭커로 진행합니다.

| 장 | 구성 |
|---|---|
| 1. **Self-Flow** | 제목·저자·발표처와 Fig. 1b의 정성 비교 한 쌍. `figureSide`로 원본 그림의 흰 매트와 혼합 서체를 확인합니다. [논문 Fig. 1](https://black-forest-labs.github.io/Self-Flow/self_flow.pdf#page=1), [ICML 논문 정보](https://proceedings.mlr.press/v306/chefer26a.html) |
| 2. **TL;DR** | 틴트 배경에 `lead` 한 문장과 두 기여점. 토큰별 두 timestep 배정과 EMA teacher를 이용한 표현 정렬을 구분합니다. [논문 §3.3–3.4](https://black-forest-labs.github.io/Self-Flow/self_flow.pdf#page=4) |
| 3. **Dual-Timestep Scheduling과 표현 정렬** | Fig. 3을 번안한 SVG `toggle`. 같은 입력의 단일 timestep과 두 timestep 배정을 비교합니다. 기본 화면과 PDF에는 student의 혼합 노이즈, teacher의 `min(t,s)`, Eq. 7의 두 손실을 함께 표시합니다. [논문 Fig. 3·Eq. 7](https://black-forest-labs.github.io/Self-Flow/self_flow.pdf#page=4) |
| 4. **텍스트-이미지 생성 FID** | `bars`로 Table 2의 1M step 모델 5종을 비교합니다. Self-Flow 3.61, REPA 3.92를 직접 표기하고 FID↓와 평가 조건을 붙입니다. [논문 Table 2](https://black-forest-labs.github.io/Self-Flow/self_flow.pdf#page=6) |
| 5. **ImageNet 지표 비교** | `table`로 ImageNet 256×256의 4M step Self-Flow와 REPA를 비교합니다. FID는 Self-Flow가, IS는 REPA가 앞서는 열을 함께 보여줍니다. [논문 Table 1](https://black-forest-labs.github.io/Self-Flow/self_flow.pdf#page=5) |
| 6. **학습 비용과 토론** | Statement에 `lead`와 토론 항목. EMA teacher의 추가 forward 비용과 noise scheduler 민감도를 짚고, 같은 학습 시간으로 맞추면 결론이 어떻게 달라질지 묻습니다. [논문 §5](https://black-forest-labs.github.io/Self-Flow/self_flow.pdf#page=10) |