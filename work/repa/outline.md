## Ledger

- Fig. 1 — use: 6, 9. 왼쪽 방법 도식과 오른쪽 수렴 곡선을 각각 크롭.
- Fig. 2 — use: 4, 5. Linear probe는 4번, CKNNA와 학습 진행 곡선은 5번.
- Fig. 3 — use: 13.
- Fig. 4 — use: 11.
- Fig. 5 — use: 14, 18. 인코더 비교는 14번, SiT 크기별 비교는 18번.
- Fig. 6 — cut: CFG \(w=4.0\)의 선별 샘플이며, 대응하는 vanilla 샘플이 있는 Fig. 4를 정성 비교에 사용.
- Fig. 7 — use: 19.
- Fig. 8 — use: 19.
- Table 1 — use: 8.
- Table 2 — use: 14, 15, 16.
- Table 3 — use: 9, 10.
- Table 4 — use: 12, 21.
- Table 5 — use: 17.
- 부록 Table 7 — use: 7, 8, 13.
- 부록 Table 8 — use: 18.
- 부록 Table 9 — use: 12. Vanilla SiT-XL/2의 CFG scale 확인.
- 부록 Table 10 — use: 12, 21. Guidance interval 설정과 지표 비교.
- 부록 Table 11 — use: 20, 21.
- 부록 Table 12 — use: 20.

## Sections

1920×1080 HTML · 클리커 진행 · 하단 진행 표시줄 · 표지와 ending을 포함해 22장, 내용 20장 · 총 20:00

- S1 — 요약 (2번, 0:55)
- S2 — 배경 (3–5번, 2:40)
- S3 — 방법 (6–8번, 3:00)
- S4 — 결과 (9–12번, 4:30)
- S5 — 분석 (13–19번, 6:10)
- S6 — 정리와 토론 (20–22번, 2:10. Ending 0:15 포함)

표지 1번은 구간 없이 0:35.

## Slides

### 1. 생성 모델을 위한 표현 정렬

- section: none
- message: 오늘은 REPA 논문을 바탕으로 확산 transformer가 학습하는 표현과 그 표현을 외부 인코더에 정렬했을 때의 변화를 살펴봅니다.
- on-slide facts: *Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think* · Sihyun Yu et al. · ICLR 2025 · VILAB 논문 세미나 · [발표자 이름]
- source: p. 1, 논문 제목·저자·학회 정보
- block: `split 65:35` · 왼쪽 `lead` · 오른쪽 `groups`로 논문 정보와 세미나 정보
- assets: none
- interaction: none

### 2. REPA 한눈에 보기

- section: S1
- message: REPA는 noisy latent를 처리하는 확산 transformer의 중간 표현을 clean image에서 얻은 외부 표현에 정렬하고, 이 정규화가 학습에 미치는 효과를 검증합니다.
- on-slide facts: ① Vanilla SiT와 DINOv2-g의 표현 격차 진단 · ② 중간 hidden state에 patch 단위 정렬 손실 추가 · ③ ImageNet 256×256, SiT-XL/2, no CFG에서 400K step의 FID 7.9와 vanilla 7M step의 8.3 비교
- source: 초록, p. 1 · §1, pp. 2–3 · Fig. 2 · Eq. (8)–(9) · Table 3
- block: 어두운 statement · `split 40:60` · 왼쪽 `lead`에 방법의 한 줄 요약 · 오른쪽 `cards` 3개
- assets: none
- interaction: none

### 3. REPA의 연구 배경

- section: S2
- message: REPA는 denoising transformer, 확산 모델의 내부 표현 연구, 외부 표현을 쓰는 생성 모델 연구가 만나는 지점에 있습니다.
- on-slide facts:
  - Denoising transformer — U-ViT, DiT, SiT
  - 확산 모델 표현의 활용 — RepFusion, DreamTeacher
  - 외부 표현을 이용한 생성 — Würstchen, RCG
  - 마지막 줄 — 외부 표현 정렬은 확산 transformer의 수렴 속도와 생성 품질을 얼마나, 어떤 조건에서 바꾸는가?
- source: §5, p. 10 · App. I, p. 39
- block: `split 60:40` · 왼쪽 `groups`에 연구 갈래와 모델명 · 오른쪽 하단 `callout`에 발표 질문
- assets: none
- interaction: none

### 4. SiT 표현의 분류 성능

- section: S2
- message: ImageNet에서 7M step을 학습한 vanilla SiT-XL/2는 분류에 쓸 수 있는 표현을 배우지만, 최고 linear probe 정확도도 DINOv2-g 기준보다 낮습니다.
- on-slide facts: 7M step vanilla SiT-XL/2 · globally pooled hidden state의 ImageNet validation linear probe · \(t=0,\ 0.25,\ 0.5\) · layer 20 부근의 최고점과 이후 하락 · DINOv2-g 기준선
- source: §3.2, p. 5 · Fig. 2a, p. 2 · App. C.1, p. 21
- block: `split 70:30` · 왼쪽 `figureNumbered`에 ① SiT 최고점 ② DINOv2-g 기준선 · 오른쪽 `bullets`에 probe 조건
- assets: Fig. 2a 크롭, 축·범례 포함
- interaction: none

### 5. SiT와 DINOv2의 정렬

- section: S2
- message: Vanilla SiT의 DINOv2-g 정렬은 모델 크기와 학습 step이 늘수록 높아지며, 7M step에서도 MoCov3-B 기준에 못 미칩니다.
- on-slide facts: CKNNA의 기준 표현은 clean DINOv2-g · ImageNet validation 10,000장, 공통 최근접 이웃 \(k=10\) · 7M SiT-XL/2의 일부 층은 MAE-L 기준선 상회 · SiT-B/2와 XL/2의 학습 진행 곡선 및 MoCov3-B 기준선 · 입력 차이 — clean RGB와 noisy VAE latent
- source: §1, p. 2 · §3.2, p. 5 · Fig. 2b–c · App. C.1, pp. 20–21
- block: `split 72:28` · 왼쪽 `figure` 2개 · 오른쪽 `bullets`에 CKNNA 조건과 입력 차이
- assets: Fig. 2b–c 크롭, 축·범례 포함
- interaction: none

### 6. REPA의 두 입력 경로

- section: S3
- message: REPA는 같은 이미지에서 얻은 clean patch 표현을 noisy latent의 중간 hidden state가 예측하도록 학습합니다.
- on-slide facts: Clean RGB \(x_*\) → pretrained visual encoder → target patch tokens \(y_*\) · 같은 이미지 → Stable Diffusion VAE → noisy latent \(z_t\) → DiT/SiT hidden state \(h_t\) · 학습 가능한 3층 SiLU MLP projector · 대응 patch 단위 비교 · projector는 학습 때만 사용
- source: §3.1, p. 4 · §3.3, p. 6 · Fig. 1, p. 1 · App. B, p. 20 · App. D, p. 23
- block: `split 68:32` · 왼쪽 `figureNumbered`에 ① clean target ② noisy hidden state ③ MLP와 정렬 지점 · 오른쪽 `groups`에 두 경로와 projector
- assets: Fig. 1 왼쪽 방법 도식 크롭, 화살표와 loss 라벨 포함
- interaction: none

### 7. 정렬 손실과 학습 목적

- section: S3
- message: REPA는 패치별 유사도를 높이는 손실을 기존 denoising objective에 가중합으로 추가합니다.
- on-slide facts:
  - 정렬 손실 \(\displaystyle \mathcal L_{\mathrm{REPA}}=-\mathbb E_{x_*,\epsilon,t}\!\left[\frac1N\sum_{n=1}^{N}\mathrm{sim}\!\left(y_*^{[n]},h_\phi(h_t^{[n]})\right)\right]\)
  - SiT 전체 손실 \(\displaystyle \mathcal L=\mathcal L_{\mathrm{velocity}}+\lambda\mathcal L_{\mathrm{REPA}}\)
  - \(n\)은 patch index, \(N\)은 patch 수, \(h_\phi\)는 projector · SiT는 linear stochastic interpolant와 velocity prediction · DiT는 Improved DDPM objective · 주요 SiT 비교의 \(\lambda=0.5\)
- source: §2, pp. 3–4 · §3.3, p. 6, Eq. (8)–(9) · App. D, Table 7
- block: `split 65:35` · 왼쪽 `equation` 2개 · 오른쪽 `groups`에 기호와 모델별 학습 목적
- assets: Eq. (8)–(9) LaTeX
- interaction: none

### 8. ImageNet 실험 설정

- section: S3
- message: 주 비교는 ImageNet 256×256에서 같은 latent 입력과 batch size를 쓰며, REPA를 거는 층과 target 설정은 SiT 크기에 따라 달라집니다.
- on-slide facts:
  - B/2 · 12층 · hidden dim 768 · 12 heads · layer 4 정렬
  - L/2 · 24층 · hidden dim 1,024 · 16 heads · layer 8 정렬
  - XL/2 · 28층 · hidden dim 1,152 · 16 heads · layer 8 정렬
  - Table 3의 SiT 설정 — B/2·XL/2는 DINOv2-B + cosine similarity, L/2는 DINOv2-L + NT-Xent
  - 공통 설정 — Stable Diffusion VAE latent \(32\times32\times4\), patch size 2, batch 256 · 생성 평가 50,000장, SDE Euler–Maruyama, 기본 NFE 250
- source: §4.1, pp. 6–7 · Table 1 · App. D, Table 7, p. 23
- block: `split 55:45` · 왼쪽 `table`에 아키텍처와 정렬 층 · 오른쪽 `groups`에 target·학습·평가 설정
- assets: Table 1과 Table 7의 해당 행 재구성
- interaction: none

### 9. SiT-XL/2의 학습 곡선

- section: S4
- message: ImageNet 256×256의 no-CFG 비교에서 SiT-XL/2 + REPA는 400K step에 vanilla 7M step의 FID를 넘어섭니다.
- on-slide facts: SiT-XL/2 675M · FID-50K · vanilla 7M 8.3, REPA 400K 7.9, \(\Delta\mathrm{FID}=-0.4\) · 비교 checkpoint의 학습 step 비율 \(7\mathrm M/400\mathrm K=17.5\times\) · REPA 1M 6.4, 4M 5.9
- source: §4.3, p. 9 · Fig. 1, p. 1 · Table 3
- block: `split 68:32` · 왼쪽 `figureNumbered`에 두 SiT checkpoint 표시 · 오른쪽 `deltas`에 학습 step 비율과 FID 차이
- assets: Fig. 1 오른쪽 수렴 곡선 크롭, 축·범례 포함 · Table 3 checkpoint 수치
- interaction: none

### 10. DiT·SiT의 400K 비교

- section: S4
- message: 학습량을 400K step으로 맞추면 Table 3의 DiT·SiT 다섯 모델 모두 REPA를 쓴 쪽의 FID가 더 낮습니다.
- on-slide facts: ImageNet 256×256, 400K step, no CFG, FID-50K · DiT-L/2 23.3→15.6 \((−7.7)\) · DiT-XL/2 19.5→12.3 \((−7.2)\) · SiT-B/2 33.0→24.4 \((−8.6)\) · SiT-L/2 18.8→9.7 \((−9.1)\) · SiT-XL/2 17.2→7.9 \((−9.3)\)
- source: §4.3, p. 9 · Table 3
- block: `split 78:22` · 왼쪽 `bars`에 5개 모델의 vanilla/REPA 짝막대 · 오른쪽 `groups`에 공통 조건과 같은 모델 대비 Δ
- assets: Table 3의 400K 비교 수치로 막대그래프 구성
- interaction: none

### 11. 초기 checkpoint의 생성 예시

- section: S4
- message: Fig. 4는 같은 초기 노이즈에서 출발한 두 SiT-XL/2의 생성 결과가 첫 400K step 동안 어떻게 달라지는지 보여 줍니다.
- on-slide facts: Fig. 4 왼쪽 위 예시의 vanilla/REPA 대응 행 · ① 100K의 초기 출력 쌍 · ② 200K의 중간 출력 쌍 · ③ 400K의 마지막 출력 쌍 · 각 열은 동일 step에서 비교, 각 행은 같은 모델의 시간 경과 비교 · 두 모델의 초기 노이즈·sampler·sampling step 동일, no CFG
- source: Fig. 4, p. 5 · §4.3, p. 9
- block: `split 75:25` · 왼쪽 `figureNumbered`에 세 checkpoint 열 · 오른쪽 `bullets`에 비교 방향과 통제 조건
- assets: Fig. 4의 대응 행과 100K·200K·400K 라벨 크롭
- interaction: none

### 12. CFG와 guidance interval

- section: S4
- message: 4M step을 학습한 SiT-XL/2 + REPA의 FID는 일반 CFG에서 1.80, guidance interval 설정에서 1.42이며 두 설정의 sFID 순위는 반대입니다.
- on-slide facts:
  - ImageNet 256×256, SiT-XL/2 · 표의 지표 순서 FID / sFID / IS
  - Vanilla, 1,400 epochs, \(w=1.50\) · 2.06 / 4.50 / 270.3
  - REPA, 200 epochs, CFG · 1.96 / 4.49 / 264.0
  - REPA, 800 epochs, \(w=1.35\) · 1.80 / 4.50 / 284.0
  - REPA, 800 epochs, interval \([0,0.7]\), \(w=1.80\) · 1.42 / 4.70 / 305.7
  - 같은 800-epoch checkpoint의 두 sampling 설정 비교 · \(\Delta\mathrm{FID}=-0.38\), \(\Delta\mathrm{sFID}=+0.20\)
- source: §4.3, p. 9 · Table 4 · App. G, Tables 9–10, p. 25
- block: `split 68:32` · 왼쪽 `table`에 네 설정과 세 지표 · 오른쪽 `deltas`에 800-epoch 설정 간 지표 변화
- assets: Table 4의 SiT 행과 Tables 9–10의 guidance 설정
- interaction: none

### 13. 정렬 후 표현 지표

- section: S5
- message: Layer 8에 REPA를 적용한 SiT-XL/2는 vanilla보다 높은 linear probe 정확도와 DINOv2-g 정렬을 보이며, Fig. 3c의 같은 학습 step 비교에서는 FID도 낮습니다.
- on-slide facts: REPA 모델 — SiT-XL/2, 1M step, DINOv2-B target, layer 8, cosine similarity, \(\lambda=0.5\) · ① layer별 ImageNet linear probe · ② layer별 CKNNA의 평가 기준은 DINOv2-g · ③ 대응 학습 step의 validation accuracy와 FID-50K · 한 REPA 모델의 여러 층을 읽은 평가
- source: §1, p. 3 · Fig. 3a–c · App. D, Table 7
- block: `split 72:28` · 왼쪽 `figureNumbered`에 세 패널 · 오른쪽 `groups`에 학습 target과 평가 기준
- assets: Fig. 3a–c 크롭, 축·범례 포함
- interaction: none

### 14. 인코더 종류와 크기

- section: S5
- message: 인코더 계열에 따라 FID 차이가 컸으며, 같은 DINOv2 계열의 B·L·g를 바꿨을 때는 차이가 작았습니다.
- on-slide facts:
  - ImageNet 256×256, SiT-L/2, 400K step, no CFG, layer 8, NT-Xent, \(\lambda=0.5\)
  - FID / 정렬된 SiT 표현의 linear probe Acc. (%) — MAE-L 12.5 / 57.3, DINO-B 11.9 / 59.3, MoCov3-L 11.9 / 63.0, I-JEPA-H 11.6 / 62.1, CLIP-L 11.0 / 67.2, SigLIP-L 10.2 / 68.8, DINOv2-L 10.0 / 68.1
  - Vanilla FID 18.8 · DINOv2-L의 \(\Delta\mathrm{FID}=-8.8\)
  - DINOv2 크기별 FID — B 9.7, L 10.0, g 9.8 · 최대 차이 0.3
- source: §4.2, pp. 7–8 · Table 2 · Fig. 5a
- block: `split 60:40` · 왼쪽 `table`에 FID·Acc. · 오른쪽 `figure`에 Fig. 5a와 `groups`에 DINOv2 크기 비교
- assets: Table 2의 인코더 종류·크기 행 · Fig. 5a 크롭, 축·범례 포함
- interaction: none

### 15. 정렬 깊이

- section: S5
- message: SiT-L/2 깊이 실험에서는 layer 8의 FID가 가장 낮고, layer 16의 linear probe 정확도가 가장 높습니다.
- on-slide facts:
  - ImageNet 256×256, SiT-L/2, 400K step, no CFG, DINOv2-L, NT-Xent, \(\lambda=0.5\)
  - 정렬 층별 FID / Acc. (%) — 6층 10.3 / 66.2, 8층 10.0 / 68.1, 10층 10.5 / 68.6, 12층 11.2 / 69.4, 14층 11.6 / 70.0, 16층 12.1 / 71.1
  - Layer 8→16 · \(\Delta\mathrm{FID}=+2.1\), \(\Delta\mathrm{Acc.}=+3.0\) pp
- source: §4.2, p. 8 · Table 2 · App. M, p. 43
- block: `split 63:37` · 왼쪽 `table`에 두 지표와 최저·최고 셀 표시 · 오른쪽 `deltas`에 layer 8 대비 layer 16
- assets: Table 2의 depth 비교 행
- interaction: none

### 16. 정렬 목적 함수

- section: S5
- message: 400K step에서 cosine과 NT-Xent의 FID 차이는 0.1이며, sFID는 NT-Xent 쪽이 더 낮습니다.
- on-slide facts: ImageNet 256×256, SiT-L/2, 400K step, no CFG, DINOv2-L, layer 8, \(\lambda=0.5\) · FID / sFID / IS / Acc. (%) · NT-Xent 10.0 / 5.09 / 106.6 / 68.1 · cosine 9.9 / 5.34 / 111.9 / 68.2 · §4.2가 서술한 50–100K 구간의 NT-Xent 우세 · 후속 실험에 cosine 채택
- source: §4.2, p. 8 · Table 2, p. 7
- block: `split 65:35` · 왼쪽 `table`에 400K 측정값 · 오른쪽 `groups`에 초기 구간의 본문 관찰과 후속 선택
- assets: Table 2의 objective 비교 행
- interaction: none

### 17. 정규화 가중치 λ

- section: S5
- message: SiT-XL/2의 400K step 실험에서 \(\lambda\)를 0.25에서 0.5로 올릴 때 FID가 0.7 낮아지고, 이후 시험한 값에서는 0.1만 더 낮아집니다.
- on-slide facts: ImageNet 256×256, SiT-XL/2, 400K step · \(\lambda\)별 FID / IS — 0.25에서 8.6 / 118.6, 0.5에서 7.9 / 122.6, 0.75에서 7.8 / 124.4, 1.0에서 7.8 / 124.8 · 실험 범위 0.25–1.0 · timestep별 가중치는 부록의 후속 과제
- source: §4.4, p. 10 · Table 5 · App. M, p. 43
- block: `split 60:40` · 왼쪽 `table`에 FID와 IS · 오른쪽 `deltas`에 0.25→0.5와 0.5→0.75의 ΔFID
- assets: Table 5 수치
- interaction: none

### 18. SiT 크기별 수렴

- section: S5
- message: Fig. 5의 크기 비교에서 SiT가 클수록 REPA 모델의 FID가 더 빠르게 낮아지며, 같은 200K step에서 linear probe 정확도도 더 높습니다.
- on-slide facts: ImageNet 256×256, no CFG · Fig. 5b의 vanilla/REPA 수렴 곡선 · Fig. 5c의 50K·100K·200K·400K checkpoint · 200K의 FID / Acc. (%) — B/2 33.2 / 50.9, L/2 14.0 / 66.3, XL/2 11.1 / 67.3 · DINOv2-B와 cosine으로 통일한 부록 비교 · 정렬 층은 B/2 layer 4, L/2·XL/2 layer 8
- source: §4.2, p. 8 · Fig. 5b–c · App. G, Table 8, p. 25
- block: `split 66:34` · 왼쪽 `figure`에 수렴과 FID–Acc. 패널 · 오른쪽 `table`에 200K 단면과 정렬 층
- assets: Fig. 5b–c 크롭, 축·범례 포함 · Table 8의 200K 행
- interaction: none

### 19. 노이즈와 정렬 대상

- section: S5
- message: 시험한 세 timestep에서 REPA 모델의 표현 지표가 개선됐고, MoCov3-L과 MAE-L을 target으로 쓴 실험에서도 각 target과의 정렬이 높아졌습니다.
- on-slide facts: Fig. 7 — \(t=0,\ 0.25,\ 0.5\)에서 vanilla와 REPA SiT-XL/2의 ImageNet linear probe 및 DINOv2-g 기준 최대 CKNNA · Fig. 8 — MoCov3-L 또는 MAE-L과 정렬한 SiT-L/2의 layer별 CKNNA, 각각 해당 target으로 평가 · Fig. 8 범례의 vanilla 비교 모델은 SiT-XL/2
- source: §4.4, p. 9 · Fig. 7–8, p. 10
- block: `split 50:50` · 왼쪽 `figure`에 Fig. 7 두 패널 · 오른쪽 `figure`에 Fig. 8 두 패널과 모델 크기 표기
- assets: Fig. 7a–b 및 Fig. 8a–b 크롭, 축·범례 포함
- interaction: none

### 20. 적용 범위와 학습 비용

- section: S6
- message: 부록은 ImageNet 512×512와 MS-COCO에서 추가 적용 사례를 보여 주며, 실제 학습시간을 비교하려면 같은 장비에서 측정한 baseline 처리량이 더 필요합니다.
- on-slide facts:
  - ImageNet 512×512, SiT-XL/2, CFG \(w=1.35\) · vanilla 600 epochs → REPA 100 epochs · FID 2.62→2.32, precision 0.84→0.84, recall 0.57→0.56
  - MS-COCO validation, MMDiT 150K step, SDE NFE 250, CFG \(w=2.0\) · FID 5.30→4.14, \(\Delta=-1.16\)
  - 보고된 학습 환경 · H100 80GB 8장, batch 256, 약 5.4 step/s · 대응 vanilla 처리량 미제시
  - App. M의 후속 적용 범위 · pixel-space diffusion, video, 대규모 text-to-image 학습
- source: App. D, p. 23 · App. J, Table 11, p. 40 · App. K, Table 12, pp. 41–42 · App. M, p. 43
- block: `split 60:40` · 왼쪽 `cards` 2개에 추가 벤치마크 · 오른쪽 `groups`에 비용과 남은 적용 범위
- assets: Tables 11–12의 대응 비교 행
- interaction: none

### 21. 정리와 토론

- section: S6
- message: REPA의 step 대비 FID 개선을 출발점으로 삼아, 깊이 선택의 근거와 평가 설정, 외부 인코더 비용을 토론하겠습니다.
- on-slide facts:
  - **정리** — Vanilla SiT의 표현 격차 · 중간 patch 표현 정렬 · ImageNet 256×256에서의 step 대비 FID 개선
  - **근거 · 깊이** — 깊은 층의 probe Acc. 상승과 FID 악화, 후반 층이 고주파 세부를 담당한다는 해석을 검증할 주파수별 측정
  - **근거 · 평가 지표** — 같은 4M checkpoint에서 guidance interval의 FID 1.42 / sFID 4.70과 일반 CFG의 1.80 / 4.50, 설정 선택과 최종 평가에 같은 FID를 쓸 때의 검증 기준
  - **근거 · 부록 서술** — App. J의 네 지표 개선 서술과 Table 11의 100-epoch precision 동률(0.84), 200-epoch sFID·precision 열세
  - **대가 · 해석** — 학습 중 target encoder forward에 드는 연산과 feature 사전 계산에 드는 저장 공간·I/O의 교환
- source: Fig. 2 · Table 2 · Tables 3–4 · §4.2, p. 8 · App. D, p. 23 · App. G, Table 10 · App. J, Table 11
- block: 어두운 statement · `split 35:65` · 왼쪽 `lead`와 `groups`에 정리 · 오른쪽 `cards` 4개에 토론점
- assets: Tables 4·10의 CFG 수치와 Table 11의 100·200-epoch 수치 발췌
- interaction: none

### 22. 감사합니다 · Q&A

- section: S6
- message: 질문과 토론을 받겠습니다.
- on-slide facts: [발표자 이름] · VILAB · [논문](https://arxiv.org/abs/2410.06940) · [코드](https://github.com/sihyun-yu/REPA) · [프로젝트 페이지](https://sihyun.me/REPA)
- source: p. 1, arXiv ID·프로젝트 페이지 · p. 11, 구현 공개 명시. GitHub 주소는 제공 본문에 직접 표기되지 않아 미확인.
- block: `split 65:35` · 왼쪽 `lead`에 감사와 Q&A · 오른쪽 `groups`에 발표자와 링크
- assets: none
- interaction: none