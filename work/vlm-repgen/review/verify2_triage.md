# deck.json 2차 검증 처리 (`verify2.md`, agy) · 한국어 편집 (`korean.md`, codex)

## 한국어 편집
94행 중 92행 적용(`korean_applied.md`). 제외 2행:
- 5.body.0.beats.3.text — "① 표현을 공유할 때 생성 성능이 좋아지는 이유는 무엇인가?": SVG의 질문 문구와 어긋나고, 이득이 있다는 것을 전제로 깐다. 원문 유지.
- 14.notes.1 — 도구가 거부(숫자 변경).

## 2차 검증 (14건, 모두 수용)
| ID | 처리 |
|---|---|
| W1 | 2번 카드: "27블록과 patch embedding, 28개 표현" |
| W2 | 3번 표를 Sec. 3.2의 여섯 갈래로(BAGEL은 MoT 행), 대본 "여섯 갈래" |
| W3 | 5번 기존 설계의 출처를 Fig. 5a(Full MoT) + Sec. 3.2(BAGEL)로 나눠 derived. beat 1 "이해 입력은 z에서 만들고, 생성은 z의 공간에서" |
| W4 | 6번 alt의 Fig. 3b 값(강한 sem. Joint 끝층 약 0.15) |
| W5·W6 | 10번 callout "생성 통제 비교(Sec. 3.4–3.6)는 … step 수로 1/4, 1/12", 대본에 tokenizer 비교 20K 별도 |
| W7 | 12번 GPT-4o-Image(Table 3)와 GPT-4o(Table 4)를 합치지 않음. GPT-4o 4.20은 캡션으로, 굵게 = 보인 행 중 최고 |
| W8·W9 | 15번: 본문값과 곡선값 구분(0.18은 본문값), Fig. 10 패널, PSNR·유지율 조건, alt의 20K 겹침 |
| W10 | 16번 3행 근거를 같은 LLM 조건끼리(AF 약 0.28 > FLUX.1-VAE 약 0.17), 캡션 "‘약’ = 곡선, 나머지 본문값" |
| W11 | 18번 step당 지연 3.23배, WISE-Verified, message에 50K |
| W12 | 19번 비용 조건(9B 이해 추론, 800×800 1장), Qwen3.5-35B-A3B |
| W13·W14 | 20번 토론 1의 0.18 본문값, 토론 2 "생성 1단계 설정의 50K step, 주로 GenEval", 토론 4 "9B는 650K step" |
