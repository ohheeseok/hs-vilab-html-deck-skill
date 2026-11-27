1. **arXiv 페이지(2501.06848)와 저자 코드 저장소**
- 코드 공개 URL: `https://github.com/zacharyhorvitz/Fk-Diffusion-Steering` · https://github.com/zacharyhorvitz/Fk-Diffusion-Steering · README/저장소에서 직접 확인
- 코드 저장소 라이선스: 저장소 루트에 별도 `LICENSE` 파일이나 명시적 소프트웨어 라이선스 표기가 확인되지 않음(확인 못 함; 참고로 OpenReview 논문 메타데이터는 CC BY 4.0) · https://github.com/zacharyhorvitz/Fk-Diffusion-Steering · README/저장소에서 직접 확인
- 학회 채택 표기: arXiv `Comments:` 필드의 채택 문구는 확인 못 함(https://arxiv.org/abs/2501.06848); 학회 공식 출판 페이지에서 **ICML 2025** 채택·출판(*PMLR* Vol. 267, pp. 55810–55827) 확인 · https://proceedings.mlr.press/v267/singhal25b.html · 학회 페이지에서 직접 확인

2. **표준 SMC의 adaptive resampling 규칙**
- ESS가 임계값보다 **작을 때(또는 이하일 때) resample**하고, 클 때 resample을 건너뛴다(대상 논문 App. C.3의 규칙과 반대). Naesseth, Lindsten, Schön(2019) *Elements of Sequential Monte Carlo*의 **Section 2.2.2("Effective Sample Size and Adaptive Resampling"), p. 31**(arXiv 판 기준)에서 $\widehat{\text{ESS}} \le \tau N$(또는 $<\text{threshold}$, 통상 $\tau=0.5$)일 때 리샘플링을 수행한다고 서술 · https://arxiv.org/abs/1903.04797 · 본문에서 직접 확인
- Chopin & Papaspiliopoulos(2020) *An Introduction to Sequential Monte Carlo*의 **Chapter 10, Section 10.2("Adaptive Resampling")**에서도 $\text{ESS} < \gamma N$(대표값 $\gamma=0.5$)일 때 리샘플링을 수행하나, 원문 정확한 쪽수는 확인 못 함 · https://chopin.github.io/particles/ · 2차 자료

3. **Twisted Diffusion Sampler (Wu et al., NeurIPS 2023, arXiv:2306.17775)**
- 첫 단계($t=T$) 가중치: **포함한다.** Algorithm 1에서 $x_k^T \sim p(x^T)$를 샘플링한 뒤 초기 가중치로 twisting function 값 $w_k \leftarrow \tilde{p}_\theta(y \mid x_k^T)$를 부여 · https://arxiv.org/abs/2306.17775 · 본문에서 직접 확인
- 점근적 정확성 조건: 입자 수 $K \to \infty$일 때 제안 분포가 목표 조건부 분포의 지지집합(support)을 덮고 SMC 가중치 보정이 적용되면 정확한 조건부 분포 $p_\theta(x^0 \mid y)$로 수렴한다는 취지이나, 원문 명제(Proposition)의 정확한 세부 정칙 조건 문구 전체는 확인 못 함 · https://arxiv.org/abs/2306.17775 · 2차 자료

4. **SVDD (Li et al., arXiv:2408.08252)**
- 초록 확인 사항: 사전학습된 연속·이산 확산 모델에서 파인튜닝이나 미분 가능한 프록시 없이, 중간 상태가 미래 보상으로 이어지는 정도를 예측하는 soft value function을 결합해 비미분 보상을 최적화하는 반복 샘플링 알고리즘(SVDD) 제안 · https://arxiv.org/abs/2408.08252 · 초록에서 직접 확인
- 매 단계 수행 내용(후보 수·선택 방식) 및 목표 분포: 매 디노이징 단계에서 다수($M$개)의 후보 상태를 샘플링한 뒤 soft value function으로 평가·선택하며, 목표 분포는 사전학습 분포에 대한 KL-정규화 보상 최대화 분포로 확인되나, 초록 원문 자체에 해당 후보 수·선택 방식·목표 분포가 명시되었는지는 초록 전문 미회수로 확인 못 함 · https://arxiv.org/abs/2408.08252 · 2차 자료

5. **2025년 이후 FK steering 관련 후속 연구 (초록 기준 관계 확인; 본문 참고문헌의 2501.06848 직접 인용 여부는 본문 미열람으로 확인 못 함)**
- *Discrete Diffusion Inference-Time Control with Nested Sequential Monte Carlo* (arXiv:2608.20123): 이산 확산 언어 모델의 Feynman-Kac steering을 위해 nested SMC(NSMC)와 fully-adapted NSMC(FA-NSMC)를 정식화하고, 기존 정식화의 편향 오류를 수정해 best-of-$n$과 bootstrap SMC를 일관되게 능가한다고 주장 · https://arxiv.org/abs/2608.20123 · 초록에서 직접 확인
- *Controllable protein design with particle-based Feynman-Kac steering* (arXiv:2511.09216): RFdiffusion에 ProteinMPNN과 구조 완화 기반 유도 포텐셜을 결합한 FK steering을 적용해, 비미분 목적함수에 대해 바인더 설계 가능성(designability)을 89.5% 높이고 인터페이스 에너지를 개선한다고 주장 · https://arxiv.org/abs/2511.09216 · 초록에서 직접 확인
- *Multi-property Feynman-Kac Steering of Crystal Diffusion Models* (arXiv:2610.24828): 결정 확산 모델의 연속·이산 채널을 함께 제어하기 위해 Feynman-Kac 입자 선택에 원자 재마스킹(re-masking)을 결합한 FK-ReMask를 제안해, 재학습 없이 다중 물성 목표 및 SUN 수율을 높인다고 주장 · https://arxiv.org/abs/2610.24828 · 초록에서 직접 확인

6. **Chatterjee & Diaconis (2018), "The sample size required in importance sampling"**
- 정확한 주장 형태(초록 기준): 측도 $\mu$에서 추출한 표본으로 목표 확률측도 $\nu$에 대한 기댓값을 정확히 추정하기 위해, 일반적인 설정에서 **약 $\exp(D(\nu \parallel \mu))$ 크기의 표본 수가 필요충분(necessary and sufficient)**하며(여기서 $D(\nu \parallel \mu)$는 $\nu$에 대한 $\mu$의 Kullback–Leibler divergence), 필요 표본 수는 로그 스케일에서 일종의 cut-off를 보인다고 서술 · https://arxiv.org/abs/1511.01437 (출판본 DOI: https://doi.org/10.1214/17-AAP1326) · 초록에서 직접 확인
