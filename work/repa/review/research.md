### 1. 공식 코드·체크포인트 저장소, 라이선스, ICLR 2025 발표 형식

- 공식 코드 저장소는 `sihyun-yu/REPA`이며 라이선스는 MIT License이다 · https://github.com/sihyun-yu/REPA · README에서 직접 확인
- 별도의 공식 체크포인트 호스팅 저장소 URL은 확인 못 함(README는 `eval.py` 실행 시 `--ckpt` 미지정이면 SiT-XL/2 4M iteration 체크포인트가 자동 다운로드되며, DINOv2·CLIP은 자동 다운로드, 기타 인코더는 원본 저장소에서 수동 다운로드하도록 안내함) · https://github.com/sihyun-yu/REPA · README에서 직접 확인
- OpenReview 페이지에서는 ICLR 2025 채택(Conference Paper)까지만 확인되었고, OpenReview 페이지 내 발표 형식(oral/spotlight/poster) 명시는 확인 못 함 · https://openreview.net/forum?id=DJSZGGZYVi · 2차 자료
- 공식 GitHub README와 arXiv 페이지에는 **ICLR 2025 Oral**로 표기되어 있다 · https://github.com/sihyun-yu/REPA, https://arxiv.org/abs/2410.06940 · README에서 직접 확인

### 2. REPA 이후(2025–2026) 후속 연구 6편

- **U-REPA: Aligning Diffusion U-Nets to ViTs** (arXiv:2503.18414): REPA는 DiT에만 검증되었고 U-Net에 적용 시 블록 기능 차이·다운샘플링 공간 불일치·토큰 단위 정렬 격차가 발생하므로, 중간 스테이지 정렬·MLP 후 업샘플링·manifold loss로 해결한다 · https://arxiv.org/abs/2503.18414 · 초록에서 직접 확인
- **REPA-E: Unlocking VAE for End-to-End Tuning with Latent Diffusion Transformers** (arXiv:2504.10483): 표준 diffusion loss로는 불가능했던 VAE와 잠재 확산 모델의 end-to-end 공동 학습을 REPA 손실로 가능하게 하여 REPA 대비 17배 이상 빠른 학습과 VAE 잠재 공간 개선을 달성한다 · https://arxiv.org/abs/2504.10483 · 초록에서 직접 확인
- **No Other Representation Component Is Needed: Diffusion Transformers Can Provide Representation Guidance by Themselves** (SRA, arXiv:2505.02831): 외부 사전학습 기반 모델 없이 확산 트랜스포머 내부의 고노이즈 초기 층 표현을 저노이즈 후기 층 표현에 자기 증류로 정렬한다 · https://arxiv.org/abs/2505.02831 · 초록에서 직접 확인
- **REPA Works Until It Doesn't: Early-Stopped, Holistic Alignment Supercharges Diffusion Training** (HASTE, arXiv:2505.16792): REPA는 초기 수렴을 가속하지만 학습 후반에는 교사-학생 용량 불일치로 성능이 정체·저하되므로, 특징·어텐션 전체 정렬 후 일정 시점에 정렬 손실을 중단한다 · https://arxiv.org/abs/2505.16792 · 초록에서 직접 확인
- **Diffuse and Disperse: Image Generation with Representation Regularization** (Dispersive Loss, arXiv:2506.09027): REPA와 달리 사전학습 모델·추가 파라미터·외부 데이터 없이 은닉 표현을 분산시키는 자기 완결적 정규화 손실만으로 확산 모델을 개선한다 · https://arxiv.org/abs/2506.09027 · 초록에서 직접 확인
- **What matters for Representation Alignment: Global Information or Spatial Structure?** (iREPA, arXiv:2512.10794): REPA의 생성 성능 향상은 전역 의미 정보가 아니라 패치 간 공간 구조가 주도하며, MLP 투영을 합성곱으로 교체하고 공간 정규화를 추가하면 수렴이 일관되게 빨라진다 · https://arxiv.org/abs/2512.10794 · 초록에서 직접 확인

### 3. REPA의 학습 시간 대가 정량 보고 여부

- 공식 저장소 README와 원 논문·OpenReview에서는 최적화 스텝 기준 17.5배 가속만 보고할 뿐, 외부 인코더 forward나 feature 사전 계산에 드는 wall-clock 학습 시간 대가(초/스텝, GPU 시간 등)의 정량 수치는 확인 못 함 · https://github.com/sihyun-yu/REPA, https://arxiv.org/abs/2410.06940, https://openreview.net/forum?id=DJSZGGZYVi · README에서 직접 확인
- 후속 논문 HASTE의 OpenReview 논의에서는 온라인 DINOv2-B(224×224, XFormers 미사용) forward 연산량을 **23.19 GFLOPs**, 로컬 배치 32 기준 REPA의 최대 CUDA 메모리를 **27,818.01 MB**로 정량 보고했다(스텝당 wall-clock 시간이나 feature 사전 계산 시간 수치는 확인 못 함) · https://openreview.net/forum?id=HK96GI5s7G · 본문에서 직접 확인
- 후속 논문 SRA(Appendix H Table 7)와 SRA 2 / VAE-REPA는 REPA의 외부 인코더 연산·메모리·사전 계산 부담을 지적하지만, SRA Table 7은 SiT/DiT와 +SRA의 에폭당 시간·메모리만 보고하고 SRA 2는 자사 기법의 추가 연산량(~4% GFLOPs)만 제시해 REPA 자체의 정량적 wall-clock 시간·사전 계산 비용은 확인 못 함 · https://arxiv.org/abs/2505.02831, https://arxiv.org/abs/2601.17830 · 본문에서 직접 확인

### 4. 후속 연구의 REPA ImageNet 256×256 baseline 수치 재인용

- 원 논문은 800 epochs(4M iter) SiT-XL/2 + REPA에 대해 평가 설정별로 **5.9**(CFG 미사용), **1.80**(표준 CFG), **1.42**(CFG+guidance interval) 세 수치를 보고했다 · https://arxiv.org/abs/2410.06940 · 본문에서 직접 확인
- **같은 값을 쓰는 경우**: U-REPA, HASTE, SRA, REPA-E(Table 9)는 CFG+guidance interval 기준 **FID 1.42(800 epochs)**를 그대로 인용하고, REPA-E(Table 1)와 REG는 CFG 미사용 기준 **5.90 / 5.9**를 그대로 인용한다 · https://arxiv.org/abs/2503.18414, https://arxiv.org/abs/2505.16792, https://arxiv.org/abs/2505.02831, https://arxiv.org/abs/2504.10483, https://arxiv.org/abs/2507.01467 · 본문에서 직접 확인
- **다른(또는 다른 설정의) 값을 쓰는 경우**: Diffuse and Disperse(Table 6)는 guidance interval 없는 표준 CFG 비교를 위해 1.42 대신 원 논문의 **FID 1.80**을 인용한다 · https://arxiv.org/abs/2506.09027 · 2차 자료
- 또한 REPA-E는 Table 1에서 800 epochs CFG 미사용 gFID를 **5.90**으로 표기한 반면, Table 9에서는 **5.84**로 보고해 표 간 소폭 차이가 확인된다 · https://arxiv.org/abs/2504.10483 · 본문에서 직접 확인
