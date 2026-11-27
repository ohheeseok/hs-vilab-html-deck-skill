### 1. Integral 프로젝트 페이지 및 arXiv 페이지
- **학회 채택 표기·논문 라이선스(arXiv)**: Comments에 `Preprint. Project page: https://thejb.ai/integral`만 기재되어 학회 채택 표기는 없으며(프리프린트), 논문 라이선스는 `arXiv.org perpetual non-exclusive license`임. arXiv 메타데이터 자체의 코드·체크포인트 URL 표기 여부는 확인 못 함 · https://arxiv.org/abs/2611.31237 · 초록(arXiv 메타데이터)에서 직접 확인
- **프로젝트 페이지(`https://thejb.ai/integral`) 직접 내용**: 페이지 본문은 검색 결과에서 직접 확인 못 함 · https://thejb.ai/integral · 확인 못 함
- **코드·체크포인트·모델 라이선스(공식 모델 카드 보충)**: 체크포인트 `the-jb/Integral-9B`(safetensors)가 공개되어 있고, 라이선스는 `apache-2.0`이며, 모델 카드 내에 코드 저장소 URL `https://github.com/the-jb/integral`이 안내됨(단, GitHub 저장소 자체 README·라이선스는 직접 확인 못 함) · https://huggingface.co/the-jb/Integral-9B · 모델 카드에서 직접 확인

### 2. Qwen3.5-9B 아키텍처 구성 검증
- 공식 `config.json`의 `vision_config`는 `depth: 27`(블록 수), `patch_size: 16`, `hidden_size: 1152`이며, `text_config`의 `num_hidden_layers`는 `32`임. 따라서 Integral 논문 App. A.1의 기술(vision encoder 27 블록·patch 16·$d_h$ 1152, language backbone 32층)과 모두 일치함(공식 기술 보고서 본문은 별도 확인 못 함) · https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/config.json · 모델 카드(공식 `config.json`)에서 직접 확인

### 3. BAGEL(arXiv:2505.14683) 아키텍처 및 Integral 논문 기술 대조
- **파라미터**: 전체 14B, 활성 7B이며 Qwen2.5-7B 기반 백본을 MoT(Mixture-of-Transformer-Experts)로 복제해 이해 전문가(7B)와 생성 전용 전문가(7B)로 분리함 · https://arxiv.org/abs/2505.14683 · 본문에서 직접 확인
- **생성 latent 및 이해 encoder**: 생성 측은 동결된 FLUX VAE(8× 다운샘플링·16채널, FLUX.1 계열) 위에서 Rectified Flow를 학습하고, 이해 측은 `SigLIP2-so400m/14`로 초기화한 ViT 인코더를 사용함. Integral 논문의 "FLUX.1-VAE와 약 7B의 생성 전용 파라미터" 서술은 BAGEL 원문과 일치함 · https://arxiv.org/abs/2505.14683 · 본문에서 직접 확인

### 4. 이해·생성 표현 공유 선행·동시 연구 (arXiv 초록 기준)
- **(a) Kang et al.(ECCV 2026, `arXiv:2607.04423`)**: 통합 멀티모달 모델의 교차 태스크 전이성은 완전 공유 트랜스포머 백본과 통합 시각 인코더 같은 아키텍처에 의존하며, 생성을 직접 미세조정하는 대신 대응 이해 태스크를 학습해 생성으로 전이시키면 분포 이동을 줄이면서 개수 세기·공간 관계·텍스트 등 생성 능력을 개선할 수 있음 · https://arxiv.org/abs/2607.04423 · 초록에서 직접 확인
- **(b) Harmon(Wu et al., `arXiv:2503.21979`)**: Masked Autoregressive(MAR) 인코더가 생성뿐 아니라 풍부한 의미 표현도 학습한다는 점에 착안해, 공유 MAR 인코더와 3단계 점진적 학습으로 시각 이해와 생성의 표현을 조화시킴 · https://arxiv.org/abs/2503.21979 · 초록에서 직접 확인
- **(c) PS-VAE(Zhang et al., `arXiv:2512.17909`)**: 표현 인코더 특징을 그대로 생성에 쓰면 비정규화로 인한 매니폴드 이탈과 약한 픽셀 복원이 발생하므로, KL 정규화 압축 잠재 공간(16×16 다운샘플링·96채널)에 픽셀 복원 목적을 결합해 의미 보존과 고품질 복원·T2I 생성·편집을 동시에 달성함 · https://arxiv.org/abs/2512.17909 · 초록에서 직접 확인

### 5. GenEval 2 및 WISE-Verified
- **GenEval 2(`arXiv:2512.16853`)**: 원래 GenEval 같은 정적 벤치마크는 T2I 모델이 발전하면서 포화(saturation)되고 인간 평가와의 정렬이 어긋나는 벤치마크 드리프트(benchmark drift)를 겪어 최신 모델에서 최대 17.7%의 절대 오차를 낸다고 지적하며, 조합성을 높인 GenEval 2와 시각 원시 요소별 판정을 결합한 Soft-TIFA를 제안함 · https://arxiv.org/abs/2512.16853 · 초록에서 직접 확인
- **WISE-Verified vs WISE**: 기존 WISE(`WISE_legacy`) 대비 ① 너무 쉽거나 폐쇄형 모델 안전 필터를 유발하던 수백 개 프롬프트를 수정·검증했고, ② 다축 WiScore를 0/1 이진 점수로 단순화했으며, ③ 판정 모델을 폐쇄형 GPT-4o에서 오픈소스 판정 모델(`Qwen3.5-35B-A3B`) 기반으로 전환함 · https://github.com/PKU-YuanGroup/WISE · README에서 직접 확인

### 6. MoT(Mixture-of-Transformers)
- **정의 및 arXiv 번호**: 멀티모달 파운데이션 모델의 사전학습 계산량을 줄이기 위해 FFN·어텐션 행렬·레이어 정규화 등 비임베딩 파라미터를 모달리티별로 분리하되, 전체 통합 시퀀스에 대한 전역 셀프 어텐션(global self-attention)은 공유하는 희소(sparse) 멀티모달 트랜스포머 아키텍처. arXiv 번호는 `2411.04996`(TMLR 2025 게재) · https://arxiv.org/abs/2411.04996 · 초록에서 직접 확인
