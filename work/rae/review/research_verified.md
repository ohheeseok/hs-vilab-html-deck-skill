# 자료조사 확인 (출처에서 직접)

조사 agy `research.md`(웹 허용으로 재실행: 첫 실행은 `delegate.py`가 `--dir`과 함께 "웹 금지" 규칙을 붙여 다섯 질문 모두 "확인 못 함"). 아래는 조율자가 출처를 직접 열어 확인한 것만. 덱에서는 `external`로 표시한다.

| # | 사실 | 출처 | 확인 방법 | 조사 결과와 다른 점 |
|---|---|---|---|---|
| R1 | 공식 코드 `github.com/bytetriper/RAE`, MIT License, 설명 "Official PyTorch Implementation of …" | https://github.com/bytetriper/RAE | GitHub API(license 필드) | 같음 |
| R2 | 프로젝트 페이지 rae-dit.github.io가 위 저장소로 링크 | https://rae-dit.github.io/ | 페이지 HTML | 같음 |
| R3 | ICLR 2026 채택 | — | OpenReview가 봇 확인(챌린지)을 요구해 열지 못함 | **확인 못 함 → 덱에 쓰지 않는다** (표지는 "arXiv 2510.11690 v1, 2025-10") |
| R4 | "Scaling Text-to-Image Diffusion Transformers with Representation Autoencoders", arXiv 2601.16208(2026-01), 저자에 Tong, Zheng, Ma, Xie 포함: SigLIP-2 RAE로 T2I(0.5B–9.8B DiT)로 확장, "dimension-dependent noise scheduling remains critical", "wide diffusion heads and noise-augmented decoding offer negligible benefits at scale", FLUX VAE보다 일관되게 우수 | https://arxiv.org/abs/2601.16208 | arXiv API 초록 | 같음. 저자가 겹친다는 점 추가 |
| R5 | "Improved Baselines with Representation Autoencoders"(RAEv2), arXiv 2605.18324(2026-05), 저자 Singh, Zheng, …, Xie: 마지막 k층 합으로 복원 개선, RAE와 REPA가 상호보완, "the original RAE struggles with classifier-free guidance (CFG) and requires training a second, weaker diffusion model for AutoGuidance", ImageNet-256 80 epoch gFID 1.06 | https://arxiv.org/abs/2605.18324 | arXiv API 초록 | 같음 |
| R6 | "Improving Reconstruction of Representation Autoencoder"(LV-RAE), arXiv 2602.08620: 의미 특징에 색·질감 같은 저수준 정보가 부족해 복원이 병목, 고차원 latent에서 디코더가 섭동에 민감 | https://arxiv.org/abs/2602.08620 | arXiv API 초록 | 같음 |
| R7 | MeanFlow-RAE(arXiv 2511.13019), VQRAE(arXiv 2511.23386) — RAE 잠재공간 위의 확장 | arXiv 초록 | arXiv API | 같음(덱에는 이름만, 필요하면) |
| R8 | DDT: arXiv 2504.05741 | https://arxiv.org/abs/2504.05741 | arXiv API | 수치(1.26 @ 400 epoch)는 초록에 없음 → 덱에서는 RAE 논문 Table 8의 값만 쓴다 |
| R9 | DINOv2의 큐레이션 데이터에 ImageNet-22k와 **ImageNet-1k train split** 포함(LVD-142M 구축) | https://arxiv.org/abs/2304.07193 (v2 PDF §3 "Data sources") | PDF 본문 | 같음. DINOv2 with Registers의 데이터는 원문 미확인 → "DINOv2(LVD-142M)"까지만 쓴다 |
| R10 | REPA-E 원 논문 수치 1.26 / 1.83 | — | 원문 표 미확인 | **쓰지 않는다** (RAE Table 14의 "officially reported" 값으로만) |

덱에 쓸 곳: R1·R2 → ending 링크. R4·R5 → 20번 토론(head와 노이즈 증강의 효과가 규모에서 사라진다는 후속 결과, CFG 한계를 저자 그룹이 다음 논문에서 인정). R6 → 18번 notes(복원 병목을 후속 연구가 지적). R9 → 20번 대가 항목(동결 인코더가 ImageNet-1k train을 이미 본 상태 — 해석으로 표시).
