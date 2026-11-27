### 1. FK steering(arXiv:2501.06848)을 직접 인용하고 확장·비교한 후속 연구

- **Controllable protein design with particle-based Feynman-Kac steering** (arXiv:2511.09216): 참고문헌에서 Singhal 등(2025, arXiv:2501.06848)을 직접 인용하며, ProteinMPNN과 구조 완화(structural relaxation) 기반 유도 포텐셜을 도입해 RFdiffusion에 입자 기반 FK steering을 적용함으로써 예측 계면 에너지를 일관되게 개선하고 바인더 설계 가능성(binder designability)을 89.5% 높였다고 주장한다. · https://arxiv.org/abs/2511.09216 · 초록/본문에서 직접 확인
- **Discrete Feynman-Kac Correctors** (arXiv:2601.10403): 본문과 실험에서 Singhal 등(2025)의 FK steering을 보상 유도 이산 확산 기준선으로 직접 인용·비교하며, 추가 학습이나 미세조정 없이 마스킹된 이산 확산 모델에서 온도 어닐링·주변분포 곱·보상 틸팅 샘플링을 수행하는 SMC 기반 Discrete Feynman-Kac Correctors 프레임워크를 제안한다. · https://arxiv.org/abs/2601.10403 · 초록/본문에서 직접 확인
- **Composing and Steering Diffusion Models with Generalized Feynman-Kac Correctors** (arXiv:2610.40383): 참고문헌[24]과 본문에서 Singhal 등(2025)의 SMC 기반 가이던스를 단일 사전학습 모델용 추론 시점 기법으로 직접 인용·대비하며, 임의 초기 함수와 목표 함수 사이의 기하 보간이 닫힌 형태 포텐셜을 갖는 Feynman-Kac PDE를 만족함을 보여 재학습 없이 여러 사전학습 확산 모델의 합성과 보상 조향(steering)을 수행하는 Generalized Feynman-Kac Correctors를 제안한다. · https://arxiv.org/abs/2610.40383 · 초록/본문에서 직접 확인

### 2. Chatterjee & Diaconis (2018, arXiv:1511.01437)의 표본 크기 주장(초록 기준)

- 확률측도 $\mu$에서 추출한 크기 $n$의 무작위 표본으로 다른 확률측도 $\nu$에 대한 함수의 기댓값을 추정할 때, 상당히 일반적인 설정에서 중요도 샘플링의 정확한 추정을 위해 대략 $\exp(D(\nu\|\mu))$ 크기의 표본이 **필요충분(necessary and sufficient)**하며(여기서 $D(\nu\|\mu)$는 $\nu$에 대한 $\mu$의 쿨백-라이블러 발산, *Kullback–Leibler divergence of $\mu$ from $\nu$*), 특히 필요한 표본 크기가 로그 스케일에서 일종의 컷오프(cut-off)를 보인다고 진술한다. · https://arxiv.org/abs/1511.01437 · 초록/본문에서 직접 확인
