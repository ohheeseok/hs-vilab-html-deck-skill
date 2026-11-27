너는 자료조사자다. 웹을 검색해 아래 질문에 답하고, 답마다 출처 URL을 붙여라. 확인하지 못한 것은 "확인 못 함"이라고 써라. 추측하지 마라. 파일은 만들지 말고 결과만 출력하라. 한국어, 900단어 이내.

대상 논문: JB Kim, Byungwoo Jeon, Kyungmin Lee, Hyeonmo Kang, Cheonbok Park, Shinyoung Joo, Jinwoo Shin, Jeonghoon Kim, "Let Vision-Language Models Generate Images through Their Representations" (방법 이름 Integral), arXiv 2611.31237 (2026년 11월 23일), NAVER Cloud · KAIST. 프로젝트 페이지 https://thejb.ai/integral.

1. 프로젝트 페이지와 arXiv 페이지에서: 코드·체크포인트 공개 여부와 URL, 라이선스, 학회 채택 표기. 확인한 페이지로만.
2. Qwen3.5-9B(Qwen Team, 2026): 공식 모델 카드나 기술 보고서에서 vision encoder 구성(블록 수, patch size, hidden dim)과 language backbone 층 수. 논문 App. A.1은 vision encoder 27 블록·patch 16·d_h 1152, language backbone 32층이라고 한다 — 맞는지.
3. BAGEL(Deng et al., 2025, "Emerging properties in unified multimodal pretraining", arXiv 2505.14683): 전체 파라미터와 활성 파라미터, 생성 쪽 latent가 FLUX VAE인지, 이해 쪽 encoder(SigLIP2 등). 논문(Integral)은 BAGEL이 "FLUX.1-VAE와 약 7B의 생성 전용 파라미터"를 쓴다고 쓴다 — BAGEL 원문과 맞는지.
4. 이해·생성 표현 공유에 관한 선행·동시 연구: (a) Kang et al., "Transferability between understanding and generation in unified multimodal models"(ECCV 2026)의 주장 한 줄, (b) Harmon(Wu et al., 2025b, "Harmonizing visual representations...")의 주장 한 줄, (c) PS-VAE(Zhang et al., 2025a, "Both semantics and reconstruction matter", arXiv 2512.17909)의 주장 한 줄. arXiv 초록에서 확인한 내용만.
5. GenEval2(Kamath et al., 2025, "GenEval 2: Addressing benchmark drift", arXiv 2512.16853)가 원래 GenEval에 대해 지적하는 문제(포화, 판정 모델의 drift 등) 한두 줄, 그리고 WISE-Verified가 WISE와 어떻게 다른지(출처가 있으면).
6. MoT(Liang et al., 2025, "Mixture-of-Transformers")의 정의 한 줄과 arXiv 번호.

형식: 질문 번호별로 `- 사실 · 출처 URL · 확인 수준(초록/본문/README/모델 카드에서 직접 확인 | 2차 자료)`.
