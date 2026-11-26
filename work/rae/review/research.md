### 1. 공식 코드·체크포인트 저장소, 라이선스 및 학회 채택 여부
- 공식 코드 저장소는 `bytetriper/RAE`, 체크포인트 저장소는 Hugging Face `nyu-visionx/RAE-collections`, 프로젝트 페이지는 `rae-dit.github.io`이며, 코드·모델 모두 **MIT License**임 · https://github.com/bytetriper/RAE , https://huggingface.co/nyu-visionx/RAE-collections , https://rae-dit.github.io/ · README/LICENSE에서 직접 확인(검색 인덱싱 경유)
- 학회 채택 여부: **ICLR 2026 Poster** 채택 확인됨 · https://openreview.net/forum?id=0u1LigJaab , https://iclr.cc/virtual/2026 · 초록/채택 메타데이터에서 직접 확인(검색 경유)

---

### 2. RAE 이후(2025-10 이후) 후속 연구 5편 (arXiv 초록 기준)
- **MeanFlow Transformers with Representation Autoencoders** (arXiv:2511.13019, 2025-11): RAE 잠재공간에 MeanFlow를 결합(MF-RAE)해 학습을 안정화하고 적은 스텝·낮은 GFLOPS로 생성하도록 확장함 · https://arxiv.org/abs/2511.13019 · 초록에서 직접 확인(검색 경유)
- **VQRAE: Representation Quantization Autoencoders for Multimodal Understanding, Generation and Reconstruction** (arXiv:2511.23386, 2025-11): RAE에 벡터 양자화(VQ)를 도입해 멀티모달 이해용 연속 특징과 시각 생성·복원용 이산 토큰을 단일 토크나이저로 통합함 · https://arxiv.org/abs/2511.23386 · 초록에서 직접 확인(검색 경유)
- **Scaling Text-to-Image Diffusion Transformers with Representation Autoencoders** (arXiv:2601.16208, 2026-01): 동결 SigLIP-2 기반 RAE를 ImageNet에서 대규모 텍스트-이미지(T2I) 생성(0.5B–9.8B DiT)으로 확장해 기존 VAE 대비 빠른 수렴과 높은 품질을 보임 · https://arxiv.org/abs/2601.16208 · 초록에서 직접 확인(검색 경유)
- **Improving Reconstruction of Representation Autoencoder** (arXiv:2602.08620, 2026-02): RAE의 의미 특징이 색상·질감 등 저수준 정보를 버려 복원 병목과 잠재 섭동 민감도를 낳는다고 지적하고, 얕은 인코더로 저수준 변동을 보강한 LV-RAE와 노이즈 기반 디코더 정규화를 제안함 · https://arxiv.org/abs/2602.08620 · 초록에서 직접 확인(검색 경유)
- **Improved Baselines with Representation Autoencoders (RAEv2)** (arXiv:2605.18324, 2026-05): 인코더 마지막 $k$개 층의 합으로 미세조정 없이 복원을 개선하고, RAE와 REPA가 상호보완적임을 보이며, 원 RAE가 CFG에 취약해 별도 AutoGuidance 모델이 필요했던 한계를 REPA 기반 자가가이던스로 해소함(ImageNet-256 80 epoch gFID 1.06) · https://arxiv.org/abs/2605.18324 · 초록에서 직접 확인

---

### 3. DDT (Wang et al., 2025, "DDT: Decoupled Diffusion Transformer")
- arXiv 번호는 **arXiv:2504.05741**임 · https://arxiv.org/abs/2504.05741 · 초록에서 직접 확인
- 원 논문 보고 ImageNet 256×256 FID(CFG 있음) 및 epoch: **DDT-XL/2 (22En6De)** 기준 **256 epoch에서 FID 1.31**, **400 epoch에서 FID 1.26** · https://arxiv.org/abs/2504.05741 · 본문/초록에서 직접 확인(검색 경유)

---

### 4. REPA-E (Leng et al., ICCV 2025) 원 논문 ImageNet 256×256 FID 및 Table 14 비교
- 원 논문(arXiv:2504.10483) 보고 ImageNet 256×256 FID는 **guidance 있음(CFG) 1.26 / guidance 없음 1.83**으로, RAE 논문 Table 14의 "officially reported"(1.26 / 1.83) 수치와 **동일함**(참고: 확장/개정 설정에서 1.12 / 1.69도 보고됨) · https://arxiv.org/abs/2504.10483 , https://openaccess.thecvf.com/ · 초록/본문에서 직접 확인(검색 경유)
- 1.26 / 1.83이 달성된 **정확한 단일 epoch 수치** 및 RAE 논문 Table 14 표 원문 대조: **확인 못 함**(검색 결과에 80·400·800 epoch가 함께 언급되어 특정 수치의 정확한 epoch 매핑을 원표에서 직접 확인하지 못함) · https://arxiv.org/abs/2504.10483 , https://arxiv.org/abs/2510.11690 · 2차 자료

---

### 5. DINOv2 / DINOv2 with Registers의 LVD-142M과 ImageNet 포함 여부
- **포함함**: DINOv2 원 논문(arXiv:2304.07193) Section 3(*Data sources*) 및 Appendix Table 15에 LVD-142M 구축용 큐레이션 데이터셋이 **ImageNet-22k**와 **ImageNet-1k 학습 분할(train split)**, Google Landmarks 등을 포함한다고 명시됨 · https://arxiv.org/abs/2304.07193 · 본문에서 직접 확인
- **DINOv2 with Registers**(*Vision Transformers Need Registers*, Darcet et al., arXiv:2309.16588)는 DINOv2에 레지스터 토큰을 추가해 동일한 **LVD-142M** 데이터셋으로 학습함(단, 해당 논문 본문 내 ImageNet 포함 여부의 별도 재진술은 확인 못 함) · https://arxiv.org/abs/2309.16588 · 2차 자료(검색 요약)
