1. **대상 논문 기본 정보 (Self-Flow)**
   - **arXiv 번호:** `arXiv:2603.06507` (arXiv 제출일 2026-03-06, ICML 2026 채택) — https://arxiv.org/abs/2603.06507
   - **프로젝트 페이지:** https://bfl.ai/research/self-flow
   - **코드·가중치 공개 여부:** 추론·평가 코드는 GitHub에 공개됨(https://github.com/black-forest-labs/Self-Flow), 학습 코드 공개 여부는 확인 못 함(저장소는 추론 중심). ImageNet 256×256 사전학습 가중치(`selfflow_imagenet256.pt`, SiT-XL/2)는 Hugging Face에 공개됨(https://huggingface.co/Hila/Self-Flow), 비디오·오디오 등 멀티모달 가중치 공개 여부는 확인 못 함.

2. **2026-03 이후 후속 연구 (인용 또는 외부 인코더 없는 표현 정렬)**
   - **From SRA to Self-Flow: Data Augmentation or Self-Supervision?** (Jiang et al., 2026-07): Self-Flow의 이중 타임스텝 성능 향상이 교차 토큰 자기지도보다 노이즈 축 데이터 증강 효과에 기인함을 Attention Separation으로 분석했다. — https://arxiv.org/abs/2607.02508
   - **Representation by Design in Generation: Cross-View Class-Token Alignment in Diffusion Transformers** (Wu et al., 2026-09): 외부 인코더 없는 이중 타임스텝 확산 학습(Self-Flow 계열)에 EMA 교사 기반 교차 뷰 클래스 토큰 정렬을 더해 표현과 생성 성능을 함께 높였다. — https://arxiv.org/abs/2609.36348
   - **Beyond Distribution Matching: Self-Supervised Representation Forcing for Few-Step Video Generation** (Chen et al., 2026-10): 외부 특징 추출기 없이 학생과 EMA 교사에 서로 다른 노이즈 수준을 적용해 내부 표현을 예측·정렬하는 Self Flow Forcing($\text{SF}^2$)으로 소단계 비디오 증류를 개선했다. — https://arxiv.org/abs/2610.35594

3. **REPA (Yu et al.)**
   - **핵심 주장:** 노이즈가 섞인 확산 트랜스포머의 중간 은닉 상태를 사전학습된 외부 시각 인코더(예: DINOv2)의 깨끗한 표현에 정렬하면 학습 수렴을 대폭 가속하고 생성 품질을 높일 수 있다.
   - **SiT-XL/2 + REPA ImageNet 256×256 FID (CFG 없음, 4M step):** **5.9** (IS 157.8)
   - **출처:** https://arxiv.org/abs/2410.06940 , https://github.com/sihyun-yu/REPA

4. **SRA와 LayerSync의 정렬 대상**
   - **SRA** (*No Other Representation Component Is Needed: Diffusion Transformers Can Provide Representation Guidance by Themselves*): 높은 노이즈 조건의 초기 레이어 잠재 표현을 EMA 교사 모델의 낮은 노이즈 조건 후기 레이어 잠재 표현에 자기증류 방식으로 정렬한다. — https://arxiv.org/abs/2505.02831
   - **LayerSync** (*LayerSync: Self-aligning Intermediate Layers*): 외부 모델이나 EMA 교사 없이 확산 모델 내부의 의미가 풍부한 깊은 레이어 표현을 기준으로 얕고 약한 중간 레이어 표현을 자체 정렬한다. — https://arxiv.org/abs/2510.12581

5. **Diffusion Forcing (Chen et al., 2024)**
   - **목적:** 토큰마다 독립적인 노이즈 수준을 적용해 자기회귀 모델의 가변 길이·인과적 생성과 전체 시퀀스 확산 모델의 전역 궤적 가이던스 및 장기 롤아웃 안정성을 하나로 결합하기 위해서다. — https://arxiv.org/abs/2407.01392
