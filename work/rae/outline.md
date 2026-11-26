## Ledger

- Fig. 1 — use: 2 · 대표 그림. ImageNet 256×256 FID 연표와 RAE 계열 모델의 위치
- Fig. 2 — use: 5 · SD-VAE와 DINOv2-B RAE의 구조 및 연산량
- Fig. 3 — use: 8 · 한 이미지 과적합에서 폭과 깊이를 각각 바꾼 비교
- Fig. 4 — use: 13 · DiT-XL에 세 처방을 적용한 뒤의 epoch별 수렴
- Fig. 5 — use: 12 · noisy latent와 backbone 출력이 DDT head로 들어가는 경로
- Fig. 6 — use: 13, 14 · (b) 학습 연산량 대비 수렴, (a, c) backbone 크기와 모델 연산량 비교
- Fig. 7 — use: 16 · DiT^DH-XL의 512×512 AutoGuidance 생성 예시
- Table 1 — use: 5, 6 · (b) 디코더 크기별 비용, (a, c, d) 복원 및 linear probing
- Table 2 — use: 7 · 기본 DiT에서 RAE와 SD-VAE 비교
- Table 3 — use: 9 · 인코더 토큰 차원과 DiT 폭을 교차한 과적합 실험
- Table 4 — use: 10 · schedule shift 전후 gFID
- Table 5 — use: 11 · 노이즈 증강 전후 gFID와 rFID
- Table 6 — use: 14 · DINOv2-S/B/L에서 DiT^DH의 gFID 변화
- Table 7 — use: 15 · ImageNet 512×512 guidance 결과
- Table 8 — use: 15, 20 · ImageNet 256×256 결과와 FID 평가 프로토콜 논점
- Table 9 — use: 17 · 512×512 직접 생성과 디코더 업샘플링
- Table 10 — use: 18 · SD-VAE에서 wide head를 붙였을 때의 반례
- Table 11 — use: 19 · 토큰 수와 차원을 맞춘 픽셀·RAE 비교
- 부록 Fig. 8 — use: 6 · 동일 입력에 대한 인코더별 복원 예시
- 부록 Fig. 10 — use: 16 · `golden retriever` 클래스의 선별하지 않은 샘플
- 부록 Fig. 13 — use: 16 · `macaw` 클래스의 선별하지 않은 샘플
- 부록 Table 12 — use: 5 · ViT 디코더 학습 설정
- 부록 Table 13 — use: 7, 8, 9, 12 · DiT의 모델 크기별 폭과 깊이
- 부록 Table 14 — use: 20 · 동일 모델의 random·balanced sampling 비교
- 부록 Table 15 — use: 11 · 인코더별 노이즈 증강과 \(\tau\) 비교
- 부록 Table 16 — use: 12 · DDT head의 폭·깊이·GFLOPs 비교

## Sections

- `summary` — 요약 (2장, 0:40)
- `background` — 배경 (3–4장, 1:35)
- `method` — 방법 (5–12장, 8:30)
- `results` — 결과 (13–16장, 4:00)
- `analysis` — 분석 (17–19장, 3:05)
- `discussion` — 정리와 토론 (20–21장, 1:45)

표지 0:25를 포함해 총 20:00. 1920×1080 HTML 화면 하단에 구간 진행 표시줄 배치. 21장은 21장에 포함되는 ending이며 내용 장수는 20장. 슬라이드 8의 대표 인터랙션은 클리커의 다음 키로 한 단계 진행.

## Slides

### 1. Representation Autoencoder와 DiT

- section: none
- message: 이 논문은 사전학습한 시각 표현을 이미지 복원과 확산 학습에 함께 쓸 수 있는지 검증합니다.
- on-slide facts: 원제 *Diffusion Transformers with Representation Autoencoders* · Boyang Zheng, Nanye Ma, Shengbang Tong, Saining Xie · New York University · VILAB 논문 세미나 · 발표자 [이름]
- source: p. 1, 제목 및 저자 정보
- block: `lead` 제목 중앙, 하단에 논문·세미나 정보
- assets: none
- interaction: none

### 2. RAE와 DiT^DH 개요

- section: `summary`
- message: 이 논문은 동결된 표현 인코더에 ViT 디코더를 붙이고, 그 고차원 잠재공간에 맞춰 확산 학습과 DiT 구조를 조정합니다.
- on-slide facts: 기여 3개 · ① 세 종류의 frozen encoder를 사용한 RAE 복원 검증 · ② 폭 조건, schedule shift, 디코더 노이즈 증강 · ③ wide DDT head와 ImageNet 256×256 무가이던스 gFID 1.51, DiT^DH-XL 800 epoch
- source: 초록 및 Fig. 1, p. 1 · §4–5 · Table 8, p. 9
- block: 어두운 `statement` · `split 43:57`, 왼쪽 `lead`와 `bullets` 3개, 오른쪽 `figure`에 Fig. 1과 축·범례
- assets: Fig. 1 전체, Table 8의 대표 수치
- interaction: none

### 3. 표현 학습과 잠재 확산

- section: `background`
- message: 관련 연구는 잠재공간의 압축 방식을 바꾸거나 외부 표현을 복원과 생성에 도입해 왔습니다.
- on-slide facts: ① 압축 잠재공간의 확산 — LDM, DiT, SiT · ② 복원용 표현 학습 — VA-VAE, MAETok, DC-AE 1.5 · ③ 생성용 표현 정렬·결합 — REPA, DDT, REG, ReDi · 마지막 줄의 발표 질문 — **고정된 표현의 복원 충실도와 고차원 확산의 성립 조건은?**
- source: §1–2, pp. 1–3 · 부록 §A, pp. 19–20
- block: `groups` 3열, 발표 질문을 하단 `callout`에 배치
- assets: none
- interaction: none

### 4. 복원과 확산의 두 가정

- section: `background`
- message: 표현 인코더가 복원에 필요한 정보를 보존하는지와 DiT가 그 표현의 분포를 학습할 수 있는지는 서로 다른 검증 문제입니다.
- on-slide facts: ① 의미 중심 사전학습과 픽셀 복원 충실도에 관한 가정 → frozen encoder, 디코더 학습, rFID · ② 고차원 latent와 확산 성능에 관한 가정 → 기본 DiT 비교, 폭 병목 정리, 학습 설정 변경 후 gFID
- source: §1, p. 2 · §3–4, pp. 3–7
- block: `split 50:50`의 `compare`, 각 열에 가정과 검증 기준
- assets: none
- interaction: none

### 5. RAE의 토큰과 디코더

- section: `method`
- message: RAE는 동결된 ViT의 patch token을 그대로 받아 이미지로 되돌리는 디코더를 학습합니다.
- on-slide facts: ImageNet 256×256 기준 · 기본 DINOv2-B with Registers는 입력을 224×224로 보간하고 encoder patch 14, decoder patch 16 사용 → 256토큰 × 768채널 · SigLIP2-B와 MAE-B는 encoder patch 16, 256토큰 × 768채널 · [CLS]·[REG] 제외, patch token 정규화 · 디코더 학습 16 epoch, L1 + LPIPS + GAN · 디코더 rFID / GFLOPs: ViT-B 0.58 / 22.2, ViT-L 0.50 / 78.1, ViT-XL 0.49 / 106.7, SD-VAE 0.62 / 310.4 · Fig. 2의 encoder 연산량은 한 이미지당 SD-VAE 135, DINOv2-B 22 GFLOPs
- source: §3, pp. 3–4 · Fig. 2, p. 3 · Table 1b, p. 4 · §C.1–C.2, Table 12, p. 22
- block: `split 55:45`, 왼쪽 `figure`와 토큰·patch 주석, 오른쪽 `table`과 디코더 학습 설정
- assets: Fig. 2, Table 1b, Table 12의 디코더 설정
- interaction: none

### 6. 세 인코더의 복원 품질

- section: `method`
- message: 동결된 DINOv2-B, SigLIP2-B, MAE-B에 디코더를 학습시키면 세 RAE 모두 ImageNet에서 SD-VAE보다 낮은 rFID를 얻습니다.
- on-slide facts: ImageNet-1K 검증 세트 rFID / linear-probe Top-1 · DINOv2-B 0.49 / 84.5%, SigLIP2-B 0.53 / 79.1%, MAE-B 0.16 / 68.0%, SD-VAE 0.62 / 8.0% · RAE 디코더 ViT-XL · SD-VAE 대비 MAE-B ΔrFID −0.46 · DINOv2-S/B/L의 rFID 0.52/0.49/0.52 · Fig. 8의 입력, DINOv2-B, SigLIP2-B, MAE-B, SD-VAE 순서 유지, 같은 영역의 경계·질감 확대 비교 · rFID는 복원 이미지 집합의 분포 지표
- source: §3, Table 1a/c/d, p. 4 · §C.3, Fig. 8, p. 23
- block: `split 48:52`, 왼쪽 `table`과 `deltas` 1개, 오른쪽 `figure`에 Fig. 8의 동일 입력 행과 확대 영역
- assets: Table 1a/c/d, Fig. 8
- interaction: none

### 7. 기본 DiT의 RAE 학습

- section: `method`
- message: 기존 DiT 설정을 그대로 쓰면 토큰 수가 같아도 RAE에서 SD-VAE보다 생성 성능이 크게 떨어집니다.
- on-slide facts: ImageNet 256×256, 80 epoch, 무가이던스 FID-50K, Euler 50 step · 두 입력 모두 DiT에서 256토큰 · DiT-S 폭 384, SD-VAE 51.74 → RAE 215.76, ΔgFID +164.02 · DiT-XL 폭 1152, SD-VAE 7.13 → RAE 23.08, ΔgFID +15.95 · 후속 검증 항목 3개 — 토큰 차원 대비 폭, noise schedule, 디코더의 입력 분포
- source: §4, Table 2, pp. 4–5 · §D, Table 13 및 Compute·Sampling, pp. 23–24
- block: `split 55:45`, 왼쪽 `compare`와 `deltas` 2개, 오른쪽 `cards` 3개
- assets: Table 2, Table 13의 S·XL 설정
- interaction: none

### 8. 한 이미지 과적합 실험

- section: `method`
- message: DINOv2-B로 인코딩한 한 이미지를 과적합할 때 폭을 768까지 키우면 손실이 크게 줄지만, 폭을 384로 고정하고 층을 늘리면 개선 폭이 작습니다.
- on-slide facts: DINOv2-B 토큰 차원 \(n=768\) · Fig. 3 왼쪽의 DiT 폭 \(384,512,640,768,896\), 고정 깊이 12 · \(d<768\)의 생성 아티팩트와 \(d\ge768\)의 입력 재현 예시 · 오른쪽의 고정 폭 384, 깊이 \(4,12,16,24\), 12→24층에서도 남는 아티팩트 · 한 번에 목표 이미지 1장, 부록의 대상 이미지 3장으로 반복 · 학습 1,200 step, Euler 25 step
- source: §4.1, Fig. 3, p. 5 · §F, pp. 24–25 · 폭·깊이의 값은 Fig. 3의 축 기준
- block: `split 50:50`의 `figureNumbered` 두 패널과 `stepper`. 축·범례와 생성 예시 유지
- assets: Fig. 3의 폭·깊이 패널, 이론선, 생성 예시
- interaction: stepper — 대표 인터랙션 · reveals: 같은 토큰 차원에서 폭 변경과 깊이 변경이 손실 및 이미지 재현에 미치는 차이 ; states: ① 고정 깊이에서 폭 변화 표시 ② 폭 패널을 유지한 채 고정 폭에서 깊이 변화 공개

### 9. Theorem 1의 폭 조건

- section: `method`
- message: Theorem 1은 선형 출력 투영을 거치는 모델의 폭이 토큰 차원보다 작을 때 velocity 예측 손실에 하한이 생기는 이유를 설명합니다.
- on-slide facts: 독립 표준 Gaussian noise \(\epsilon\), 선형 보간 \(x_t=(1-t)x+t\epsilon\) · \(g(x_t,t)=Bf(Ax_t,t)\), \(\operatorname{rank}(B)\le d\) · \(d<n\)에서 \(\mathcal L(g)\ge\sum_{i=d+1}^{n}\lambda_i\), \(\lambda_i\)는 \(\epsilon-x\) 공분산 고유값의 내림차순 · 단일 이미지에서 차원당 하한 \((n-d)/n\), \(n=768,d=384\)이면 0.5 · Table 3의 DINOv2-L \(n=1024\): DiT-B \(d=768\)에서 손실 0.27, DiT-L \(d=1024\)에서 0.022 · \(d\ge n\)에서 정리의 함수족에 최적 예측기 포함. 실제 DiT의 학습과 생성 품질은 별도 실험 범위
- source: §4.1, Theorem 1, Eq. (1)–(2), Table 3, p. 6 · §B.1, Eq. (3)–(5), pp. 20–21 · Table 13, p. 23
- block: `split 60:40`, 왼쪽 `equation` 2개와 기호 설명, 오른쪽 `compare`에 단일 이미지 하한과 Table 3 사례
- assets: Eq. (1)–(2), Table 3의 DINOv2-L 행, Table 13의 B·L 폭
- interaction: none

### 10. 차원에 따른 schedule shift

- section: `method`
- message: 저자들은 토큰 수와 채널 수를 함께 반영해 timestep을 바꾸고, 같은 DiT-XL에서 큰 gFID 개선을 확인합니다.
- on-slide facts: \(t_m=\alpha t_n/[1+(\alpha-1)t_n]\), \(\alpha=\sqrt{m/n}\) · 기준 차원 \(n=4096\), DINOv2-B RAE의 전체 입력 차원 \(m=256\times768=196{,}608\), \(\alpha\approx6.93\) · \(t=1\)은 순수 노이즈 · ImageNet 256×256, RAE DiT-XL, 80 epoch, 무가이던스 Euler 50 step · shift 전후 gFID 23.08 → 4.81, Δ −18.27
- source: §4.2, pp. 6–7 · Table 4, p. 7 · §J, p. 27
- block: `split 58:42`, 왼쪽 `equation` 2개와 \(n,m\) 설명, 오른쪽 `deltas` 1개
- assets: §4.2 shift 식, Table 4
- interaction: none

### 11. 디코더의 노이즈 증강

- section: `method`
- message: 디코더 학습 때 latent에 노이즈를 더하면 생성 gFID가 낮아지는 대신 복원 rFID는 상승합니다.
- on-slide facts: 학습 데이터의 clean latent 주변을 Gaussian noise로 증강 · \(z'=z+\eta\), \(\eta\mid\sigma\sim\mathcal N(0,\sigma^2I)\), \(\sigma\sim|\mathcal N(0,\tau^2)|\) · DINOv2-B RAE, shifted schedule의 DiT-XL, ImageNet 256×256, 80 epoch, 무가이던스 Euler 50 step · \(\tau=0,0.5,0.8,1.0\)에서 gFID/rFID 각각 4.81/0.49, 4.39/0.54, 4.28/0.57, 4.20/0.60 · 기본 \(\tau=0.8\)의 ΔgFID −0.53, ΔrFID +0.08 · 증강 설정에서 MAE-B rFID 0.28·gFID 8.38, DINOv2-B rFID 0.57·gFID 4.28
- source: §4.3, Table 5, p. 7 · §G.1–G.2, Table 15a/c, pp. 25–26
- block: `split 45:55`, 왼쪽 `equation`과 clean latent·증강 latent `compare`, 오른쪽 `table`과 `deltas` 2개
- assets: §4.3 노이즈 정의, Table 5, Table 15a/c
- interaction: none

### 12. DiT^DH의 wide DDT head

- section: `method`
- message: DiT^DH는 noisy latent를 직접 받는 얕은 DDT head에 큰 폭을 배치합니다.
- on-slide facts: backbone \(M\)은 \(x_t,t,y\)에서 조건 \(z_t\) 생성, head \(H\)는 \(x_t,z_t,t\)에서 velocity \(v_t\) 예측 · 기본 head는 2층, 폭 2048 · XL backbone은 28층, 폭 1152 · DINOv2-B RAE, ImageNet 256×256, 80 epoch 기준 head 깊이×폭 / GFLOPs / gFID: 6×1152 / 25.65 / 2.36, 4×2048 / 53.14 / 2.31, 2×2048 / 26.78 / 2.16
- source: §5, Fig. 5, p. 8 · §D, Table 13, pp. 23–24 · §G.3, Table 16, p. 26
- block: `split 50:50`, 왼쪽 `figure`에 noisy latent와 조건 입력 경로 표시, 오른쪽 `table`에 head 비교
- assets: Fig. 5, Table 13의 XL 설정, Table 16
- interaction: none

### 13. 학습 epoch와 연산량

- section: `results`
- message: 세 처방을 적용한 RAE DiT-XL은 wide head를 붙이기 전에도 SiT-XL과 REPA-XL보다 더 적은 epoch에서 비교 FID에 도달합니다.
- on-slide facts: ImageNet 256×256, 무가이던스 FID-50K · Fig. 4의 DINOv2-B RAE DiT-XL 80 epoch gFID 4.28, 720 epoch 2.39 · 저자가 Fig. 4에 표시한 FID 도달 epoch 비율: SiT-XL 대비 47×, REPA-XL 대비 16× · Fig. 6b의 가로축은 누적 diffusion 학습 GFLOPs, 주요 기존 모델은 보고된 최종점으로 표시
- source: §4.3, Fig. 4, p. 7 · §5.1, Fig. 6b, pp. 8–9
- block: `split 54:46`, 왼쪽 `figure` Fig. 4, 오른쪽 `figure` Fig. 6b. 두 그래프의 가로축 단위와 범례 유지
- assets: Fig. 4, Fig. 6b
- interaction: none

### 14. DiT^DH의 크기별 비교

- section: `results`
- message: wide head를 붙인 모델은 논문이 비교한 backbone 크기와 DINOv2 인코더 크기에서 기본 DiT보다 나은 연산량 대비 gFID를 보입니다.
- on-slide facts: ImageNet 256×256, 80 epoch 기준, 무가이던스 Euler 50 step · Fig. 6a의 DiT^DH-B는 DiT-XL 학습 GFLOPs의 약 40%, gFID 3.38 대 4.28 · DINOv2-B에서 DiT^DH-S 6.07, DiT^DH-XL 2.16 · Fig. 6c의 버블 면적은 모델 FLOPs · Table 6의 DiT-XL 대비 DiT^DH-XL ΔgFID: DINOv2-S −1.08, B −2.12, L −3.36
- source: §5, Fig. 6a/c, Table 6, pp. 8–9 · §D, p. 24
- block: `split 52:48`의 `figure` 2개, 하단 `deltas` 3개. Fig. 6c의 버블 크기 범례 유지
- assets: Fig. 6a/c, Table 6
- interaction: none

### 15. ImageNet 생성 벤치마크

- section: `results`
- message: DiT^DH-XL은 ImageNet에서 256×256 무가이던스 gFID 1.51을 기록하고, AutoGuidance를 쓰면 두 해상도에서 1.13을 기록합니다.
- on-slide facts: class-conditional FID-50K, RAE 샘플링 기본 Euler 50 step · DINOv2-B DiT^DH-XL의 gFID / IS / precision / recall: 256 무가이던스 800 epoch 1.51 / 242.9 / 0.79 / 0.63, 256 AutoGuidance 800 epoch 1.13 / 262.6 / 0.78 / 0.67, 512 AutoGuidance 400 epoch 1.13 / 259.6 / 0.80 / 0.63 · 비교 gFID: REPA-E 256 무가이던스 1.70, guidance 1.15, 두 조건 모두 800 epoch · EDM2 512 guidance 1.25 · 해당 기준 대비 ΔgFID −0.19, −0.02, −0.12
- source: §5.1, Tables 7–8, pp. 9–10 · §D, p. 24 · §I, p. 27
- block: `split 72:28`, 왼쪽 `table`에 해상도·guidance·epoch와 네 지표, 오른쪽 `deltas` 3개에 각각 비교 기준 표기
- assets: Table 7의 DiT^DH-XL·EDM2 행, Table 8의 DiT^DH-XL·REPA-E 행
- interaction: none

### 16. 512×512 생성 예시

- section: `results`
- message: 논문의 512×512 샘플은 서로 다른 클래스의 구성과 같은 클래스 안에서 달라지는 외형을 보여 줍니다.
- on-slide facts: DINOv2-B DiT^DH-XL, ImageNet 512×512, AutoGuidance · ① Fig. 7 전체 그리드 — 클래스 간 소재·구성 · ② Fig. 10 `golden retriever` — 같은 클래스 안의 개체·자세 비교 · ③ Fig. 13 `macaw` — 같은 클래스 안의 색과 깃털 표현 비교 · 부록 두 예시는 선별하지 않은 샘플, AutoGuidance scale 1.5
- source: §5.1, Fig. 7, p. 10 · §M, Fig. 10, p. 29 · Fig. 13, p. 30
- block: `split 58:42`, 왼쪽 `figureNumbered`에 Fig. 7, 오른쪽에 클래스별 원본 샘플 열과 번호별 관찰 지점
- assets: Fig. 7, 부록 Fig. 10 및 Fig. 13
- interaction: none

### 17. 고해상도와 디코더 업샘플링

- section: `analysis`
- message: 256토큰으로 512×512를 출력하면 기존 확산 모델을 재사용할 수 있고, 1,024토큰으로 직접 생성할 때보다 FID가 높아집니다.
- on-slide facts: 같은 토큰 격자에서 decoder 출력 patch의 한 변을 2배로 확대 · 256×256용 diffusion 모델 재사용, 업샘플링 디코더 교체 · ImageNet 512×512, 두 비교 모델 모두 400 epoch · Direct 1,024토큰, gFID/rFID 1.13/0.53 · Upsample 256토큰, 1.61/0.97 · Direct 대비 ΔgFID +0.48, ΔrFID +0.44 · Table 9의 토큰 수 비교와 FID 수치
- source: §6.1, pp. 10–11 · Table 9, p. 11 · DINOv2 patch 구현은 §C.1, p. 22
- block: `split 53:47`, 왼쪽 `diagram`으로 직접 생성과 디코더 업샘플링의 토큰 격자 비교, 오른쪽 `table`과 `deltas` 2개
- assets: §6.1의 두 경로를 그린 SVG, Table 9
- interaction: none

### 18. SD-VAE에서의 wide head

- section: `analysis`
- message: SD-VAE의 저차원 latent에서는 wide head가 연산을 추가하면서 gFID도 높이는 반례가 나옵니다.
- on-slide facts: ImageNet 256×256, 80 epoch, 무가이던스 Euler 50 step · SD-VAE의 원래 latent \(32\times32\times4\), DiT patch 2 → 256토큰 × 16차원 · SD-VAE DiT-XL 7.13 → DiT^DH-XL 11.70, ΔgFID +4.57 · DINOv2-B RAE 256토큰 × 768차원, 4.28 → 2.16, ΔgFID −2.12
- source: §3, p. 3 · §6.2, Table 10, p. 11 · §D, p. 24
- block: `split 50:50`의 `compare`, 각 열에 토큰 형태와 `deltas` 1개
- assets: Table 10
- interaction: none

### 19. 같은 차원의 픽셀과 RAE

- section: `analysis`
- message: 토큰 수와 차원을 DINOv2-B RAE에 맞춘 픽셀 입력에서도 wide head는 도움이 되지만, 생성 gFID에는 큰 격차가 남습니다.
- on-slide facts: ImageNet 256×256, 80 epoch, 무가이던스 Euler 50 step · 픽셀 patch 16 → \(16\times16\times3=768\)차원, 픽셀과 RAE 모두 256토큰 · 픽셀 DiT-XL 51.09 → DiT^DH-XL 30.56, ΔgFID −20.53 · DiT^DH-XL의 RAE gFID 2.16 · 비교에서 맞춘 항목은 토큰 수와 차원, 두 경로의 입력 변환과 디코딩은 서로 다름
- source: §6.3, Table 11, p. 11 · §D, p. 24
- block: `split 50:50`의 `compare`, 왼쪽 픽셀 patch와 head 추가 효과, 오른쪽 RAE 토큰과 동일 head에서의 비교값
- assets: Table 11, 두 입력의 토큰 형태를 보여 주는 간단한 `diagram`
- interaction: none

### 20. 두 가정의 검증 범위와 토론

- section: `discussion`
- message: 실험은 동결된 표현의 복원 가능성과 고차원 RAE 확산의 성립 조건을 보여 주며, head의 독립 효과와 작은 FID 차이의 해석은 토론에 남습니다.
- on-slide facts: 정리 2개 · ① 세 frozen encoder의 ImageNet 복원 rFID · ② RAE 확산의 폭·schedule·decoder 조건과 SD-VAE·픽셀 반례. 토론 4개
  1. **근거 · FID 재평가 방향.** Table 8 캡션의 재평가 baseline 상승 서술과 Table 14의 balanced gFID 하락. SiT 256 무가이던스는 Table 8의 8.61, Table 14의 random 8.61 / balanced 8.54. 비교 기준과 표에 반영된 값 확인
  2. **근거 · guidance 탐색과 평가.** 256×256 gFID 1.13의 scale 1.42 및 14 epoch guide checkpoint 선택. FID로 설정을 탐색한 뒤 동일 지표로 보고한 결과의 별도 샘플 반복 여부
  3. **근거 · head와 최적화의 교차 ablation.** DiT와 DiT^DH 사이의 learning-rate schedule, EMA, gradient clipping 차이. 같은 최적화 설정에서 head 유무를 바꾼 교차 비교
  4. **대가 · 해석.** 같은 정밀도로 latent를 캐시할 경우 DINOv2-B RAE의 이미지당 원소 수가 SD-VAE의 48배 \((256\times768)/(32\times32\times4)\). 캐시 용량과 읽기 비용의 실측 부재
- source: §3–7, pp. 3–11 · Table 8, p. 9 · §D–E, p. 24 · Table 14, p. 25 · §I, p. 27
- block: 어두운 `statement` · `split 35:65`, 왼쪽 `lead`에 정리, 오른쪽 `cards` 4개. 비용 항목에 `note`로 해석 표시
- assets: Table 8과 Table 14의 SiT 비교값, §D 최적화 설정, §I AutoGuidance 설정
- interaction: none

### 21. 감사합니다 / Q&A

- section: `discussion`
- message: 두 가정을 검증한 실험과 각 반박이 성립하는 범위에 대해 질문받겠습니다.
- on-slide facts: 발표자 [이름] · VILAB · 논문 [arXiv:2510.11690v1](https://arxiv.org/abs/2510.11690v1) · 코드 [논문 프로젝트 페이지 경유](https://rae-dit.github.io/)
- source: p. 1, arXiv 식별자 및 프로젝트 주소
- block: `lead` 중앙, 하단에 발표자와 링크. 밝은 배경
- assets: none
- interaction: none