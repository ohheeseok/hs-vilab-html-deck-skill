너는 이 덱 엔진의 코드 검토자다. 읽을 폴더의 `decisions.md`(지난 논의의 결정), `engine.diff`(이번 변경: deck.js, deck.css,
build_deck.py, qa_render.py), `deck.js`(변경 후 전체), 애니메이션 두 개(`overview_latent.svg/.anim.js`, `overview_map.svg/.anim.js`)를 읽어라.

찾을 것 — 실제로 망가지는 경우만, 재현 조건과 함께:
1. deck.js 재생 상태 기계: 진입, 다음/이전(재생 중 포함), 해시 이동, 개요(G), M 키, `?motion=0`, 숫자 키, 토글이 있는 슬라이드,
   빠른 연타, 슬라이드를 떠날 때 rAF가 남는 경우, `render(t)`가 예외를 던질 때, 스크립트가 로드되지 않을 때.
2. build_deck.py: `prefix_ids`가 틀리게 바꾸는 경우(부분 일치, href, aria), 게이트가 막아야 할 것을 놓치거나 정상을 막는 경우,
   번들(bundle_html.py는 `<script src=… defer>`를 문서 순서대로 인라인함)과의 순서 문제.
3. qa_render.py: 결정성 검사(DETERMINISM)가 놓치는 경우나 잘못 실패하는 경우.
4. 두 애니메이션 스크립트: 어떤 t에서든 이전 상태에 의존하는 부분, beat 경계에서 튀는 값, 마지막 beat 시각 이후에도 움직이는 것.

번호 붙인 지적(심각도 must/should, 파일:줄, 재현, 고칠 방법)으로 한국어로 답하라. 문제가 없으면 없다고 하라.
