# research_verified.md — 출처 페이지에서 직접 확인한 외부 사실만

agy `research.md`의 답을 출처 페이지에서 다시 열어 확인했다(2026-11-24). 이 파일의 사실만 슬라이드에 쓰고, 슬라이드와 대본에 `external`로 표시한다.

| # | 사실 | URL | 다른 점 / 쓸 곳 |
|---|---|---|---|
| R1 | arXiv:2603.06507, 2026-03-06 제출(v1), 저자 8명(Chefer, Esser, Lorenz, Podell, Raja, Tong, Torralba, Rombach). 코멘트에 프로젝트 페이지 bfl.ai/research/self-flow | https://arxiv.org/abs/2603.06507 | agy가 말한 "ICML 2026 채택"은 arXiv 페이지에 없음(GitHub README에만 "ICML'26"). 덱에는 preprint로만 적는다. → 마무리 슬라이드 |
| R2 | 공식 저장소는 ImageNet 256×256 **추론 코드**만 있고, 체크포인트는 Hugging Face `Hila/Self-Flow`의 `selfflow_imagenet256.pt`. 학습 스크립트 없음. Apache-2.0 | https://github.com/black-forest-labs/Self-Flow | agy는 학습 코드 여부를 "확인 못 함"이라 했음 → "학습 코드 없음"으로 확정. → 마무리·토론(재현성) |
| R3 | Jiang et al., "From SRA to Self-Flow: Data Augmentation or Self-Supervision?" (2026-07-02). Dual-timestep 입력은 두고 noise 수준이 다른 토큰 사이의 attention을 막는 "Attention Separation"을 해도 성능이 떨어지지 않거나 오르므로, SRA→Self-Flow 개선은 주로 noise 축 data augmentation에서 온다고 주장 | https://arxiv.org/abs/2607.02508 | 저자: Dengyang Jiang, Mengmeng Wang, Harry Yang, Jingdong Wang(SRA 저자진). → 토론(기전) |
| R4 | SRA(ICLR 2026): 더 높은 noise의 앞쪽 층 표현을 더 낮은 noise의 뒤쪽 층 표현에 맞춤, 외부 인코더 없이 | https://arxiv.org/abs/2505.02831 | 논문 §2·App. A.5의 설명과 일치. → 배경 비교표 |
| R5 | LayerSync: 모델 자신의 더 의미적인 중간층으로 약한 층을 이끄는 정규화, 사전학습 모델·추가 데이터 없음 | https://arxiv.org/abs/2510.12581 | 논문 §2와 일치. → 배경 비교표 |

쓰지 않는 것: agy의 REPA "FID 5.9 (4M, no CFG)"는 abstract에서 확인되지 않음 — 덱은 Self-Flow Table 1의 REPA 5.89만 쓴다. 후속 연구 2·3번(2609.36348, 2610.35594)은 확인하지 않았으므로 쓰지 않는다.
