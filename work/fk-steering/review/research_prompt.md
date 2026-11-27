너는 자료조사자다. 웹을 검색해 아래 질문에 답하고, 답마다 출처 URL을 붙여라. 확인하지 못한 것은 "확인 못 함"이라고 써라. 추측하지 마라. 파일은 만들지 말고 결과만 출력하라. 한국어, 900단어 이내.

대상 논문: Raghav Singhal, Zachary Horvitz, Ryan Teehan, Mengye Ren, Zhou Yu, Kathleen McKeown, Rajesh Ranganath, "A General Framework for Inference-time Scaling and Steering of Diffusion Models" (방법 이름 Feynman-Kac steering, FK steering), arXiv 2501.06848 (v5, 2025년 7월 18일), NYU · Columbia.

1. arXiv 페이지(https://arxiv.org/abs/2501.06848)와 저자 코드 저장소: 코드 공개 URL, 라이선스, 학회 채택 표기(arXiv comments 또는 학회 페이지에서 직접 확인한 것만).
2. 표준 SMC의 adaptive resampling 규칙: Naesseth, Lindsten, Schön, "Elements of Sequential Monte Carlo"(2019) 또는 Chopin & Papaspiliopoulos, "An Introduction to Sequential Monte Carlo"(2020)에서 ESS가 임계값보다 작을 때 resample하는지, 클 때 resample하는지. 원문 문장 위치(절·쪽)를 적어라. (대상 논문 App. C.3은 "If ESS_t < k/2, then we skip the resampling step"이라고 쓴다.)
3. Twisted Diffusion Sampler(Wu, Trippe, Naesseth, Blei, Cunningham, "Practical and asymptotically exact conditional sampling in diffusion models", NeurIPS 2023, arXiv 2306.17775): 첫 단계(t = T) 가중치에 twisting function을 포함하는지, 그리고 TDS가 증명한 점근적 정확성의 조건 한 줄.
4. SVDD(Li et al., "Derivative-free guidance in continuous and discrete diffusion models with soft value-based decoding", arXiv 2408.08252): 매 단계 무엇을 하는지(후보 수, 선택 방식)와 목표 분포 한 줄, 초록 기준.
5. FK steering을 직접 인용하고 확장하거나 비교한 2025년 이후 후속 연구 2–3편: 제목, arXiv 번호, 초록에서 확인한 주장 한 줄. (예: diffusion 추론 시 확장, particle/tree search 기반 diffusion 샘플링.) 초록에서 FK steering 또는 SMC 기반 steering과의 관계가 확인되는 것만.
6. Chatterjee & Diaconis, "The sample size required in importance sampling"(Annals of Applied Probability, 2018): 필요한 표본 수가 KL divergence의 지수(exp(KL))에 비례한다는 주장의 정확한 형태 한 줄, 초록 기준.

형식: 질문 번호별로 `- 사실 · 출처 URL · 확인 수준(초록/본문/README에서 직접 확인 | 2차 자료)`.
