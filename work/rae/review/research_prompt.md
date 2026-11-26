너는 자료조사자다. 웹을 검색해 아래 질문에 답하고, 답마다 출처 URL을 붙여라. 확인하지 못한 것은 "확인 못 함"이라고 써라. 추측하지 마라. 파일은 만들지 말고 결과만 출력하라. 한국어, 800단어 이내.

대상 논문: Boyang Zheng, Nanye Ma, Shengbang Tong, Saining Xie, "Diffusion Transformers with Representation Autoencoders" (RAE), arXiv 2510.11690 (2025년 10월), New York University. 프로젝트 페이지 rae-dit.github.io.

1. 공식 코드·체크포인트 저장소 URL과 라이선스(프로젝트 페이지 또는 GitHub에서 확인). 이 논문이 학회에 채택됐는지(OpenReview 등) — 확인한 페이지로만.
2. RAE 이후(2025-10 이후) RAE를 직접 확장하거나 한계를 지적한 후속 연구 2–5편: 제목, arXiv 번호, 그 논문이 RAE에 대해 주장하는 것 한 줄(예: 텍스트-이미지로 확장, 고차원 잠재공간의 다른 해법, 인코더를 미세조정). arXiv 초록에서 확인한 내용만.
3. 논문이 비교 대상으로 쓴 DDT(Wang et al., 2025, "Decoupled Diffusion Transformer")의 arXiv 번호, 그리고 DDT 원 논문이 보고한 ImageNet 256×256 FID(guidance 있음)와 epoch.
4. REPA-E(Leng et al., ICCV 2025)가 원 논문에서 보고한 ImageNet 256×256 FID(guidance 있음/없음, epoch) — RAE 논문 Table 14의 "officially reported"(1.26 / 1.83)와 같은가.
5. DINOv2 with Registers(Darcet et al.)와 DINOv2의 사전학습 데이터(LVD-142M 규모)가 ImageNet 이미지를 포함하는지 — DINOv2 논문에서 확인.

형식: 질문 번호별로 `- 사실 · 출처 URL · 확인 수준(초록/본문/README에서 직접 확인 | 2차 자료)`.
