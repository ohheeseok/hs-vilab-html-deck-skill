너는 자료조사자다. 웹을 검색해 아래 질문에 답하고, 답마다 출처 URL을 붙여라. 확인하지 못한 것은 "확인 못 함"이라고 써라. 추측하지 마라. 파일은 만들지 말고 결과만 출력하라. 한국어, 800단어 이내.

대상 논문: Sihyun Yu, Sangkyung Kwak, Huiwon Jang, Jongheon Jeong, Jonathan Huang, Jinwoo Shin, Saining Xie, "Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think" (REPA), arXiv 2410.06940, ICLR 2025.

1. 공식 코드·체크포인트 저장소 URL과 라이선스. ICLR 2025에서의 발표 형식(oral / spotlight / poster) — OpenReview 페이지로 확인.
2. REPA 이후(2025–2026) REPA를 직접 확장하거나 한계를 지적한 후속 연구 3–6편: 제목, arXiv 번호, 그 논문이 REPA에 대해 주장하는 것 한 줄(예: 학습 후반에 정렬이 오히려 해가 된다, VAE까지 end-to-end로 정렬한다, 외부 인코더 없이 표현을 배운다). 이름만 들지 말고 arXiv 초록에서 확인한 내용만 써라.
3. REPA의 학습 시간 대가(외부 인코더 forward, feature 사전 계산)를 정량으로 보고한 자료가 있는가(공식 저장소 README나 후속 논문).
4. REPA의 ImageNet 256×256 수치(예: SiT-XL/2 + REPA FID 1.42, 800 epochs)를 후속 연구가 baseline으로 재인용할 때 같은 값을 쓰는가, 다른 값을 쓰는가.

형식: 질문 번호별로 `- 사실 · 출처 URL · 확인 수준(초록/본문/README에서 직접 확인 | 2차 자료)`.
