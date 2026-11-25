## Ledger

- Fig. 1 — use: 1, 6, 10. 1·10번은 오른쪽 FID 곡선, 6번은 왼쪽 구조를 바탕으로 다시 그린 SVG.
- Fig. 2 — use: 4, 5. 4번은 (a), 5번은 (b)·(c).
- Fig. 3 — use: 9. (a)·(b)·(c)를 각각 전폭 탭으로 표시. 20번 토론에서도 (b) 인용.
- Fig. 4 — use: 12. 앵무새·열기구·햄버거 예시를 클래스별 탭으로 표시.
- Fig. 5 — use: 14, 17. 14번은 (a), 17번은 (b)·(c).
- Fig. 6 — cut: CFG \(w=4.0\)을 적용한 선별 샘플. Vanilla와 같은 조건으로 대조할 수 있는 Fig. 4에 발표 시간 배정.
- Fig. 7 — use: 18. (a)·(b)를 한 장에 표시.
- Fig. 8 — use: 18, 20. 18번은 한 줄 요약, 20번은 후반 층 토론의 근거로 인용.
- Table 1 — use: 8. 아키텍처 열 재구성.
- Table 2 — use: 8, 14, 15, 16, 20. 설정 대조, 인코더 크기 수치, 깊이·목적 함수 표, 토론 근거.
- Table 3 — use: 2, 8, 10, 11, 17, 20. Checkpoint 수치, 400K 비교 막대, 설정 기록과 기준선 확인.
- Table 4 — use: 13, 20. CFG 시스템 비교와 지표 선택 토론.
- Table 5 — use: 16. \(\lambda\)별 FID·IS 표.
- 부록 Table 6 — use: 14. Target 인코더의 사전학습 데이터 확인.
- 부록 Table 7 — use: 8. 표 재구성. 6·7·9·13·20번은 설정 인용.
- 부록 Table 8 — use: 16, 17. 16번은 no-CFG 대응 행, 17번은 200K 수치와 크기 비교 설정 인용.
- 부록 Table 9 — use: 13. 일반 CFG의 \(w\)와 대응 지표 확인.
- 부록 Table 10 — use: 13, 20. Guidance interval 설정과 FID 탐색 근거.
- 부록 Table 11 — use: 19. ImageNet 512×512 비교와 부록 서술 대조.
- 부록 Table 12 — use: 19. MS-COCO 동일 step·sampler 비교.

## Sections

1920×1080 HTML · 클리커 진행 · 하단 진행 표시줄 · 표지와 ending을 포함해 **21장, 20:00**. 인터랙션은 6·9·12번이며, 대표 인터랙션은 6번. 전 슬라이드 패널 0개.

- S1: 요약 (2번, 0:55)
- S2: 배경 (3–5번, 2:50)
- S3: 방법 (6–8번, 3:20)
- S4: 결과 (9–13번, 5:10)
- S5: 분석 (14–19번, 5:00). 성분·조건 분석 14–18번, 적용 범위와 한계 19번.
- S6: 정리와 토론 (20–21번, 2:15). Ending 0:15 포함.

표지 1번은 구간 없이 0:30. 수정 로그의 장별 시간 합계는 19:05이므로 6·7·9·12번에 각각 10초, 20번에 15초를 더했다. 슬라이드 순서와 주 블록은 목표 구조를 따랐다.

## Slides

### 1. 생성 모델의 표현 정렬

- section: none
- message: REPA 논문을 통해 diffusion transformer의 표현 격차를 어떻게 진단했고 외부 표현 정렬이 생성 학습을 얼마나 바꿨는지 살펴봅니다.
- on-slide facts: 논문 원제 *Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think* · Sihyun Yu et al. · ICLR 2025 · Oral (`external`, arXiv 표기) · VILAB 논문 세미나 · [발표자 이름]
- source: p. 1, 제목·저자·학회·Fig. 1 · `external` [arXiv 논문 기록](https://arxiv.org/abs/2410.06940)
- block: `cover` · `split 54:46` · 왼쪽 `lead`와 발표 정보 · 오른쪽 `figure`
- assets: Fig. 1 오른쪽 FID-50K 곡선 크롭, 축·범례 포함
- interaction: none
- time: 30초
- notes: 오늘 발표할 논문은 Sihyun Yu 연구진의 REPA입니다. 오른쪽 그림은 학습 step에 따른 생성 FID를 보여 줍니다. 이 차이를 설명하기 위해 먼저 vanilla SiT가 어떤 표현을 학습하는지부터 보겠습니다.

### 2. REPA 개요

- section: S1
- message: REPA는 noisy latent를 처리하는 transformer의 중간 patch 표현을 clean image에서 얻은 외부 표현에 맞추고, 그 정렬이 학습과 생성에 미치는 영향을 검증합니다.
- on-slide facts: 기여 3개 · ① Vanilla SiT와 DINOv2-g의 표현 격차 측정 · ② 중간 hidden state의 patch 단위 정렬 손실 · ③ ImageNet 256×256, no CFG, SiT-XL/2의 FID 8.3 → 7.9 비교, vanilla 7M step → REPA 400K step
- source: 초록, p. 1 · §1, pp. 2–3 · Fig. 2 · Eq. (8)–(9) · Table 3
- block: 어두운 `statement` · `split 42:58` · 왼쪽 `lead`에 방법 한 줄 분량 · 오른쪽 `cards` 3개
- assets: none
- interaction: none
- time: 55초
- notes: REPA는 같은 이미지의 clean patch 표현을 noisy latent의 중간 층에 학습 신호로 제공합니다. 논문은 먼저 vanilla SiT의 표현 격차를 측정하고, 그 격차를 줄이도록 정렬 손실을 추가합니다. 대표 비교에서는 REPA를 적용한 SiT-XL/2가 400K step에서 vanilla의 7M step보다 낮은 FID를 기록합니다. 이 비교는 ImageNet 256×256에서 CFG 없이 평가한 결과입니다.

### 3. REPA의 연구 배경

- section: S2
- message: REPA는 denoising transformer, 확산 모델 내부 표현의 활용, 외부 표현을 이용한 생성이라는 세 연구 갈래에 걸쳐 있습니다.
- on-slide facts:
  - Denoising transformer · U-ViT, DiT, SiT
  - 확산 모델 내부 표현의 활용 · RepFusion, DreamTeacher
  - 외부 표현을 이용한 생성 · Würstchen, RCG
  - 마지막 줄에 배치할 발표 질문 · 외부 표현 정렬은 수렴 속도와 생성 품질을 얼마나, 어떤 조건에서 바꾸는가?
- source: §5, p. 10 · App. I, p. 39
- block: 전폭 `groups` 3열 · 하단 `callout`에 발표 질문
- assets: none
- interaction: none
- time: 55초
- notes: U-ViT, DiT, SiT는 transformer를 denoising backbone으로 쓰는 흐름에 속합니다. RepFusion과 DreamTeacher는 확산 모델에서 배운 표현을 downstream task에 활용합니다. Würstchen과 RCG는 외부 표현을 생성 과정에 사용하며, REPA는 외부 표현을 denoiser의 학습 신호로 사용합니다. 이 발표에서는 그 정렬이 수렴 속도와 생성 품질을 얼마나 바꾸는지, 어떤 조건에서 그 효과가 달라지는지 보겠습니다.

### 4. SiT 표현의 분류 성능

- section: S2
- message: ImageNet에서 7M step을 학습한 vanilla SiT-XL/2는 분류에 쓸 수 있는 표현을 배우지만, 가장 높은 linear probe 정확도도 DINOv2-g에 못 미칩니다.
- on-slide facts: Vanilla SiT-XL/2, 7M step · globally pooled hidden state · ImageNet validation linear probe · \(t=0,\ 0.25,\ 0.5\) · layer 20 부근 최고점과 이후 하락, DINOv2-g 기준선과의 격차 모두 **곡선 근거**
- source: §3.2, p. 5 · Fig. 2a, p. 2 · App. C.1, p. 21
- block: `split 73:27` · 왼쪽 `figure` · 오른쪽 `bullets`에 probe 입력, timestep, 비교 기준 · `tone: wash`
- assets: Fig. 2a 크롭, 축·범례·DINOv2-g 기준선 포함
- interaction: none
- time: 55초
- notes: 각 층의 hidden state를 공간 방향으로 평균한 뒤 linear classifier를 학습합니다. Vanilla SiT의 분류 정확도는 layer 20 부근에서 가장 높고 이후 떨어집니다. 시험한 timestep에서 SiT의 가장 높은 값도 DINOv2-g 기준에 못 미칩니다. 이 그림은 분류에 활용할 수 있는 정보의 차이를 보여 줍니다.

### 5. SiT와 DINOv2의 표현 정렬

- section: S2
- message: Vanilla SiT의 DINOv2-g 정렬은 모델 크기와 학습 step에 따라 높아지는 추세지만, 7M step의 XL/2도 DINO-B와 MoCov3-B 기준에 못 미칩니다.
- on-slide facts: CKNNA 기준 표현은 clean DINOv2-g · ImageNet validation 10,000장, 두 표현 공간에 공통인 \(k=10\) 최근접 이웃 · XL/2의 일부 층은 MAE-L 기준 상회 · B/2는 400K까지, XL/2는 7M까지 표시 · 크기·step 추세와 기준선 비교는 **곡선 근거** · 입력 조건 차이, clean RGB와 noisy VAE latent
- source: §1, p. 2 · §3.2, p. 5 · Fig. 2b–c · App. C.1, pp. 20–21, Eq. (23)–(24)
- block: `split 77:23` · 왼쪽 `figure` 2개를 가로로 배치 · 오른쪽 `bullets`에 측정 조건과 두 패널의 비교 축 · `tone: wash`
- assets: Fig. 2b–c 크롭, 축·범례·수평 기준선 포함
- interaction: none
- time: 60초
- notes: CKNNA는 두 표현 공간에서 공통으로 가까운 샘플을 중심으로 표현의 정렬을 측정합니다. 왼쪽에서 XL/2의 일부 층은 MAE-L 기준을 넘습니다. 오른쪽에서 B/2는 400K까지만 제시되며, XL/2는 7M까지 가도 DINO-B와 MoCov3-B 기준에 못 미칩니다. 논문은 clean RGB에서 얻은 표현과 noisy latent에서 얻은 표현을 바로 결합하기 어려운 점을 짚고, 중간 표현에 학습 신호를 주는 방식을 제안합니다.

### 6. REPA의 두 입력 경로

- section: S3
- message: REPA는 같은 이미지의 clean patch tokens를 SiT layer 8에 연결된 projector의 학습 target으로 사용합니다.
- on-slide facts: ImageNet 256×256, SiT-XL/2 · clean RGB \(x_*\) → pretrained DINOv2-B → \(y_*\) · Stable Diffusion VAE latent \(32\times32\times4\), patch size 2 → \(N=256\)개 토큰 · layer 8 hidden dim 1,152 · target 차원 \(D\)로 투영하는 학습 가능 3층 SiLU MLP · \(v_\theta=g_\theta\circ f_\theta\) · patch 수 조정용 encoder positional embedding 보간 · 추론 경로에는 SiT와 VAE decoder
- source: §3.1, p. 4 · §3.3, p. 6 · §4.1, p. 6 · Fig. 1 · App. B, p. 20 · App. D, p. 23, Table 7
- block: `split 75:25` · 왼쪽 `diagram` SVG · 오른쪽 `stepper` 라벨과 읽기 칸
- assets: Fig. 1 왼쪽 방법 도식을 바탕으로 새로 그릴 SVG
- interaction: `stepper` · `signature: true` · `start: Clean` · `print: expand` · `reveals:` 정렬 손실의 분기 위치와 학습·추론 경로의 차이 · `states:`
  1. `label: Clean` · **화면** — \(x_*\) 썸네일, DINOv2-B 상자, \(y_*\) patch 격자와 화살표 공개. · **읽기 칸** — “DINOv2-B는 clean RGB 이미지에서 target patch tokens를 계산합니다.” · **출처** — Fig. 1, §3.3, Table 7.
  2. `label: Noisy` · **화면** — 같은 \(x_*\)에서 아래쪽 VAE 분기, \(z_*\) 격자, \(\epsilon,t\) 입력, \(z_t\), patchify, SiT blocks 1–8 괄호 \(f_\theta\), \(h_t\) 격자 공개. \(16\times16\)과 hidden dim 1,152 표시. · **읽기 칸** — “ImageNet 256×256 설정에서 patch size 2를 쓰면 SiT의 \(32\times32\) latent는 256개 토큰이 됩니다.” · **출처** — §2·§3.1·§4.1, Table 7.
  3. `label: 정렬` · **화면** — \(h_t\)에서 3층 SiLU MLP로 빠지는 연결, \(D\)차원 출력 격자, 위아래 대응 patch 강조, cosine similarity와 \(\mathcal L_{\mathrm{REPA}}\) 상자 공개. 위쪽 encoder에 positional embedding 보간 표식 추가. · **읽기 칸** — “Layer 8의 토큰을 MLP로 투영한 뒤 대응하는 clean patch와 cosine similarity를 계산합니다.” · **출처** — §3.3, Eq. (8), App. D, Table 7.
  4. `label: Velocity` · **화면** — \(h_t\)에서 계속 이어지는 blocks 9–28 괄호 \(g_\theta\), velocity 출력, \(\mathcal L_{\mathrm{velocity}}\) 상자와 두 손실의 가중합 공개. · **읽기 칸** — “Layer 8 이후의 SiT 블록은 velocity를 예측하고, 학습에는 velocity loss와 REPA loss를 함께 씁니다.” · **출처** — §3.1, Eq. (4)·(9), Fig. 1.
  5. `label: 추론` · **화면** — RGB target 경로, encoder, MLP와 손실 상자를 숨김. 가우시안 latent에서 시작하는 SiT sampling loop와 VAE decoder를 표시. · **읽기 칸** — “추론에서는 외부 target encoder와 REPA projector를 호출하지 않습니다.” · **출처** — §2·§3.3, Fig. 1, App. B·D.
- time: 85초
- notes: [1] 위쪽 경로는 clean RGB에서 정렬에 사용할 patch tokens를 만듭니다. [2] 아래쪽에서는 같은 이미지의 VAE latent에 노이즈를 섞고 SiT의 첫 여덟 블록을 통과시킵니다. [3] Layer 8에서 분기한 MLP가 각 토큰을 target 차원으로 옮겨 대응 patch와 비교합니다. [4] 주 경로는 계속 이어져 velocity를 예측하고, 두 손실을 함께 최적화합니다. [5] 생성할 때 호출하는 것은 기존 SiT sampling 경로와 VAE decoder입니다.

### 7. REPA 손실과 학습 목적

- section: S3
- message: REPA는 대응 patch의 유사도를 높이는 항을 기존 denoising loss에 \(\lambda\)로 가중해 더합니다.
- on-slide facts:
  - Eq. (8) \(\displaystyle \mathcal L_{\mathrm{REPA}}=-\mathbb E_{x_*,\epsilon,t}\left[\frac1N\sum_{n=1}^{N}\operatorname{sim}\!\left(y_*^{[n]},h_\phi(h_t^{[n]})\right)\right]\)
  - Eq. (9) \(\displaystyle \mathcal L=\mathcal L_{\mathrm{velocity}}+\lambda\mathcal L_{\mathrm{REPA}}\)
  - 기호 설명에 포함할 Eq. (4)의 latent 표기 · \(\mathcal L_{\mathrm{velocity}}=\mathbb E\|v_\theta(z_t,t)-(\dot\alpha_t z_*+\dot\sigma_t\epsilon)\|^2\) · SiT의 \(\alpha_t=1-t,\ \sigma_t=t\)
  - \(\operatorname{sim}\) 선택 · cosine similarity / NT-Xent 목적 · Table 7의 SiT 설정 \(\lambda=0.5\) · DiT의 기본 목적은 Improved DDPM
- source: §2, pp. 3–4, Eq. (1)·(4) · §3.3, p. 6, Eq. (8)–(9) · §4.2, p. 8 · App. D, Table 7
- block: `split 66:34` · 왼쪽 `equation`에 Eq. (8)·(9) · 오른쪽 `groups`에 patch 기호, velocity target, similarity 선택
- assets: Eq. (8)·(9) LaTeX, Eq. (4)의 latent 표기
- interaction: none
- time: 70초
- notes: 첫 식은 대응하는 patch마다 유사도를 구해 평균하는 손실입니다. Cosine 설정에서는 앞에 붙은 음의 부호 때문에 이 손실을 줄일수록 유사도가 높아집니다. 두 번째 식은 정렬 손실을 velocity loss에 더하며, SiT의 linear interpolant에서는 velocity의 회귀 target이 \(\epsilon-z_*\)입니다. DiT에서는 Improved DDPM 목적에 같은 방식으로 정렬 항을 추가합니다.

### 8. ImageNet 실험 설정

- section: S3
- message: ImageNet 256×256 실험은 latent와 batch size를 공유하며, 정렬 깊이와 target 설정은 SiT 모델과 실험에 따라 달라집니다.
- on-slide facts:
  - 열 순서 · 모델 / 전체 층 / hidden dim / heads / 정렬 층 / target·목적 / Table 7의 checkpoint
  - SiT-B/2 · 12 / 768 / 12 / 4 / DINOv2-B·cosine / 400K
  - SiT-L/2 · 24 / 1,024 / 16 / 8 / DINOv2-L·NT-Xent / 700K
  - SiT-XL/2 · 28 / 1,152 / 16 / 8 / DINOv2-B·cosine / 4M
  - 공통 · Stable Diffusion VAE \(32\times32\times4\), patch size 2, batch 256, Table 7의 \(\lambda=0.5\) · 생성 지표 50,000장, 기본 SDE Euler–Maruyama NFE 250
  - 설정 기록 · Table 3의 SiT-L/2 400K FID 9.7은 Table 2의 DINOv2-B·NT-Xent 행과 일치, DINOv2-L·NT-Xent는 10.0 · Table 7에 DiT 설정 없음
- source: §4.1, pp. 6–7, Table 1 · Tables 2–3, pp. 7·9 · App. D, p. 23, Table 7
- block: `split 73:27` · 왼쪽 `table` 재구성 · 오른쪽 `groups`에 공통 조건과 설정 주석 · `tone: wash`
- assets: Tables 1·7의 해당 행, Tables 2·3의 SiT-L/2 확인 수치
- interaction: none
- time: 45초
- notes: 주 실험은 Stable Diffusion VAE와 batch size 256을 공유합니다. 정렬은 B/2의 layer 4, L/2와 XL/2의 layer 8에 겁니다. 표에 적은 target과 목적은 Table 7의 표기이며, L/2 열의 checkpoint는 700K입니다. Table 3의 L/2 400K FID 9.7은 Table 2의 DINOv2-B 행과 일치하므로, 700K 설정을 400K 행에도 적용했다고 해석하기는 어렵습니다.

### 9. REPA 적용 후 표현 지표

- section: S4
- message: Layer 8에 REPA를 건 SiT-XL/2는 표시된 모든 층에서 linear probe 정확도가 높고, DINOv2-g 정렬의 차이는 layer 8 부근에서 가장 큽니다.
- on-slide facts: REPA 모델 · SiT-XL/2, 1M step, layer 8, DINOv2-B target, cosine, \(\lambda=0.5\) · 한 모델의 여러 층을 평가 · CKNNA 평가 기준은 DINOv2-g · Fig. 3a–b의 vanilla 학습 step과 평가 \(t\) 미명시
- source: §1, p. 3, Fig. 3a–c · App. D, p. 23, Table 7
- block: 전폭 `toggle` + 상태별 `figure` 하나 · 하단 읽기 칸 · `tone: wash`
- assets: Fig. 3a, 3b, 3c 개별 크롭. 패널별 원본 축·범례 보존
- interaction: `toggle` · `start: 분류` · `print: expand` · `reveals:` 동일 패널의 공통 축에서 vanilla/REPA를 비교하며 분류 정확도와 정렬의 층별 차이 확인 · `states:`
  1. `label: 분류` · **화면** — Fig. 3a 전폭, layer index·validation Acc. 축, DINOv2-g 기준선. · **읽기 칸** — “표시된 layer 4–24에서 REPA 모델의 linear probe 정확도가 vanilla보다 높습니다.” · **출처** — Fig. 3a, **곡선 근거**.
  2. `label: 정렬` · **화면** — Fig. 3b 전폭, 원본 CKNNA 축, MoCov3-L·MAE-L 기준선, layer 8 부근과 20–24 구간 표시. · **읽기 칸** — “REPA의 CKNNA는 layer 8 부근에서 가장 높고, layer 20–24에서는 vanilla와 비슷하거나 낮습니다.” · **출처** — Fig. 3b, **곡선 근거**.
  3. `label: FID–Acc.` · **화면** — Fig. 3c 전폭, x축 validation Acc., y축 FID-50K, 두 모델의 진행 궤적. · **읽기 칸** — “Fig. 3c의 대응 학습 step 비교에서 REPA 쪽의 validation Acc.가 높고 FID가 낮습니다.” · **출처** — Fig. 3c와 캡션, **곡선 근거**.
- time: 80초
- notes: [1] 먼저 linear probe를 보면, layer 8에 REPA를 적용한 모델의 정확도가 표시된 전 층에서 더 높습니다. [2] CKNNA는 정렬을 건 layer 8 부근에서 크게 높아지지만, 후반 층에서는 vanilla와 비슷하거나 낮아집니다. 학습 target은 DINOv2-B이고, 이 패널의 평가 기준은 DINOv2-g입니다. [3] 같은 학습 step의 생성 결과까지 보면 FID와 분류 정확도가 함께 개선되는 방향이 나타납니다. 패널마다 원래 축을 유지해 각 그래프 안에서 두 모델을 비교합니다.

### 10. SiT-XL/2의 학습 곡선

- section: S4
- message: ImageNet 256×256의 no-CFG 비교에서 SiT-XL/2 + REPA는 400K step에 vanilla의 7M step보다 낮은 FID를 기록합니다.
- on-slide facts: SiT-XL/2 675M, FID-50K · vanilla 7M 8.3 vs REPA 400K 7.9 · \(\Delta\mathrm{FID}=-0.4\) · 두 checkpoint의 step 비율 \(7\mathrm M/400\mathrm K=17.5\times\) · REPA 1M 6.4, 4M 5.9
- source: §4.3, p. 9, Table 3 · Fig. 1, p. 1
- block: `split 72:28` · 왼쪽 `figure`에 두 checkpoint 표시 · 오른쪽 `deltas`에 step 비율과 ΔFID를 각각 배치 · `tone: wash`
- assets: Fig. 1 오른쪽 크롭, 축·범례 포함 · Table 3의 checkpoint 수치
- interaction: none
- time: 55초
- notes: 두 모델은 모두 675M 파라미터의 SiT-XL/2이며 CFG 없이 평가했습니다. Vanilla 7M step의 FID는 8.3이고, REPA 400K step의 FID는 7.9입니다. 17.5배는 이 두 checkpoint의 학습 step 비율입니다. REPA의 FID는 1M의 6.4에서 4M의 5.9까지 더 낮아집니다.

### 11. DiT·SiT의 400K 비교

- section: S4
- message: 400K step으로 학습량을 맞추면 Table 3에 실린 DiT·SiT 다섯 모델 모두에서 REPA의 FID가 낮습니다.
- on-slide facts:
  - 공통 · ImageNet 256×256, 400K step, no CFG, FID-50K
  - Vanilla → REPA와 \(\Delta\mathrm{FID}\) · DiT-L/2 23.3→15.6 (−7.7) · DiT-XL/2 19.5→12.3 (−7.2) · SiT-B/2 33.0→24.4 (−8.6) · SiT-L/2 18.8→9.7 (−9.1) · SiT-XL/2 17.2→7.9 (−9.3)
  - 별도 checkpoint 비교 · DiT-XL/2 675M, 같은 벤치마크와 no CFG에서 vanilla 7M과 REPA 850K 모두 FID 9.6 · step 비율 약 \(8.2\times\)
- source: §4.3, p. 9, Table 3
- block: `split 78:22` · 왼쪽 `bars`에 vanilla/REPA 짝막대와 각 Δ · 오른쪽 `groups`에 공통 조건과 DiT-XL/2 checkpoint 비교 · `tone: wash`
- assets: Table 3의 400K 행 10개로 구성한 막대그래프
- interaction: none
- time: 50초
- notes: 여기서는 모든 막대의 학습량을 400K step으로 맞췄습니다. 다섯 모델 모두 REPA를 적용했을 때 FID가 낮았고, SiT-XL/2에서는 9.3 낮아졌습니다. 별도로 DiT-XL/2에서는 vanilla 7M과 REPA 850K의 FID가 모두 9.6입니다. 이 경우 두 checkpoint의 step 비율은 약 8.2배입니다.

### 12. 초기 생성 과정 비교

- section: S4
- message: Fig. 4는 초기 노이즈와 sampling 조건을 공유하는 두 SiT-XL/2의 출력을 100K, 200K, 400K checkpoint에서 짝지어 보여 줍니다.
- on-slide facts: ImageNet 256×256, no CFG · 같은 초기 노이즈·sampler·sampling step 수 · 행은 vanilla/REPA, 열은 100K/200K/400K · 클래스별 이미지 읽기는 **해석**
- source: Fig. 4 및 캡션, p. 5 · §4.3, p. 9 · 검토 로그 C5·C7의 클래스 식별과 앵무새 관찰
- block: 전폭 `toggle` + 클래스별 `figure` 2행×3열 · 하단 읽기 칸 · `tone: wash`
- assets: Fig. 4에서 클래스별 비교 쌍 3개 크롭. 모델과 checkpoint 라벨 보존
- interaction: `toggle` · `start: 앵무새` · `print: expand` · `reveals:` 동일 checkpoint의 두 출력과 한 모델의 시간 경과를 클래스별로 구분해 비교 · `states:`
  1. `label: 앵무새` · **화면** — 앵무새 예시 두 행과 세 checkpoint. · **읽기 칸** — “두 모델의 앵무새 예시를 100K부터 400K까지 같은 열에서 비교합니다.” · **해석** — 검토 로그의 이미지 판독 기준으로, 100K REPA 쪽에서 새의 자세와 깃털 외곽을 더 일찍 식별할 수 있는지 확인. · **출처** — Fig. 4, 검토 로그 C7.
  2. `label: 열기구` · **화면** — 열기구 예시 두 행과 세 checkpoint. · **읽기 칸** — “열기구 예시에서도 같은 초기 노이즈에서 시작한 두 모델의 출력을 checkpoint별로 비교합니다.” · **해석** — 풍선 외곽과 바구니를 구분할 수 있는 시점에 초점. · **출처** — Fig. 4, 검토 로그 C5.
  3. `label: 햄버거` · **화면** — 햄버거 예시 두 행과 세 checkpoint. · **읽기 칸** — “햄버거 예시의 세 열은 100K, 200K, 400K checkpoint입니다.” · **해석** — 번과 속재료의 층이 구분되는 시점에 초점. · **출처** — Fig. 4, 검토 로그 C5.
- time: 65초
- notes: [1] 같은 열에서 vanilla와 REPA를 비교할 수 있도록 초기 노이즈와 sampling 조건을 맞췄습니다. 앵무새에서는 100K 시점부터 자세와 깃털 외곽을 비교합니다. [2] 열기구에서는 풍선 외곽과 바구니가 어떻게 구분되는지 봅니다. [3] 햄버거에서는 번과 속재료의 경계를 따라 세 checkpoint를 비교합니다. 이 예시들은 개별 샘플의 변화 과정을 읽는 정성 비교입니다.

### 13. ImageNet CFG 시스템 비교

- section: S4
- message: 같은 4M step SiT-XL/2 + REPA checkpoint에서 guidance interval 설정은 일반 CFG보다 FID가 낮고 sFID는 높습니다.
- on-slide facts:
  - ImageNet 256×256, CFG · SiT-XL/2, batch 256 기준 800 epochs ↔ 4M step, 1,400 epochs ↔ 7M step
  - 열 순서 · 모델 / epochs / FID↓ / sFID↓ / IS↑
  - MaskDiT · 1,600 / 2.28 / 5.67 / 276.6
  - DiT-XL/2 · 1,400 / 2.27 / 4.60 / 278.2
  - MDTv2-XL/2* · 1,080 / 1.58 / 4.52 / 314.7
  - Vanilla SiT-XL/2, \(w=1.50\) · 1,400 / 2.06 / 4.50 / 270.3
  - SiT-XL/2 + REPA, CFG · 200 / 1.96 / 4.49 / 264.0
  - SiT-XL/2 + REPA, \(w=1.35\) · 800 / 1.80 / 4.50 / 284.0
  - SiT-XL/2 + REPA*, interval \([0,0.7]\), \(w=1.80\) · 800 / 1.42 / 4.70 / 305.7
  - * 추가 CFG scheduling. REPA*에는 guidance interval 적용 · 800-epoch 두 설정의 \(\Delta\mathrm{FID}=-0.38\), \(\Delta\mathrm{sFID}=+0.20\)
- source: §4.3, p. 9, Table 4 · App. D, Table 7 · App. G, p. 25, Tables 9–10
- block: `split 75:25` · 왼쪽 `table`에 외부 비교 모델과 SiT 행 · 오른쪽 `deltas`에 FID·sFID 변화 각각 표시 · `tone: wash`
- assets: Table 4의 해당 행 재구성, Tables 7·9·10의 checkpoint 및 sampling 설정
- interaction: none
- time: 60초
- notes: 표는 ImageNet 256×256의 CFG 시스템 비교이며 별표는 추가 guidance scheduling을 뜻합니다. Vanilla SiT-XL/2는 1,400 epochs에서 FID 2.06이고, REPA를 쓴 200-epoch 모델은 1.96입니다. 800-epoch REPA checkpoint에서는 논문 본표의 일반 CFG가 1.80, guidance interval 설정이 1.42입니다. 이때 sFID는 4.50에서 4.70으로 올라가므로 두 지표의 순위가 갈립니다.

### 14. Target 인코더의 종류와 크기

- section: S5
- message: 시험한 인코더 계열에 따라 FID 차이가 나타났고, DINOv2 계열 안에서 B·L·g를 바꿨을 때의 차이는 0.3 이내였습니다.
- on-slide facts:
  - 공통 · ImageNet 256×256, SiT-L/2, 400K, layer 8, NT-Xent, \(\lambda=0.5\), no CFG, NFE 250
  - Fig. 5a · 7개 target 계열, x축은 **정렬된 SiT**의 linear probe Acc., y축은 FID-50K · 정확도와 FID의 전반적 동행, 순위 역전 사례 SigLIP-L 68.8%·10.2 vs DINOv2-L 68.1%·10.0
  - DINOv2 크기별 FID · B 9.7 / L 10.0 / g 9.8 · vanilla SiT-L/2 18.8 대비 DINOv2-B \(\Delta=-9.1\)
  - 사전학습 데이터 · CLIP의 WIT-400M, SigLIP의 WebLi-4B는 ImageNet-1K 미포함, FID 11.0·10.2 · 비교한 DINOv2의 LVD-142M은 ImageNet-1K 포함
- source: §4.2, pp. 7–8, Table 2·Fig. 5a · App. C.3, p. 22, Table 6
- block: `split 77:23` · 왼쪽 `figure`에 Fig. 5a 확대 · 오른쪽 `groups`에 DINOv2 크기와 사전학습 데이터 · `tone: wash`
- assets: Fig. 5a 크롭, 축·인코더 라벨 포함 · Tables 2·6의 확인 수치
- interaction: none
- time: 60초
- notes: 가로축은 target encoder 자체의 정확도가 아니라 정렬 후 SiT의 linear probe 정확도입니다. 정확도가 높을수록 FID가 낮아지는 경향이 있지만, SigLIP-L과 DINOv2-L의 순위는 두 지표에서 다릅니다. DINOv2 계열만 놓고 보면 세 크기의 FID 범위는 9.7에서 10.0입니다. Table 6에 따르면 ImageNet-1K가 사전학습에 포함되지 않은 CLIP과 SigLIP도 vanilla SiT-L/2보다 낮은 FID를 기록했습니다.

### 15. REPA의 정렬 깊이

- section: S5
- message: SiT-L/2의 깊이 실험에서 FID는 layer 8에서 가장 낮고, 정렬한 층의 linear probe 정확도는 layer 16에서 가장 높습니다.
- on-slide facts:
  - ImageNet 256×256, SiT-L/2, 400K, DINOv2-L, NT-Xent, \(\lambda=0.5\), no CFG, NFE 250
  - 정렬 층 / FID↓ / Acc.↑ (%) · 6 / 10.3 / 66.2 · 8 / 10.0 / 68.1 · 10 / 10.5 / 68.6 · 12 / 11.2 / 69.4 · 14 / 11.6 / 70.0 · 16 / 12.1 / 71.1
  - Layer 8→16 · \(\Delta\mathrm{FID}=+2.1\) · \(\Delta\mathrm{Acc.}=+3.0\) pp · 각 행은 정렬 위치가 다른 학습 모델
- source: §4.2, pp. 7–8, Table 2 · App. M, p. 43
- block: `split 64:36` · 왼쪽 `table`에 FID 최저와 Acc. 최고 표시 · 오른쪽 `deltas`에 두 지표를 각각 표시 · `tone: wash`
- assets: Table 2의 alignment depth 행
- interaction: none
- time: 55초
- notes: 이 표의 각 행은 정렬 손실을 붙인 위치가 다른 모델입니다. Layer 8에서 layer 16으로 옮기면 분류 정확도는 3.0퍼센트포인트 오르지만 FID도 2.1 올라갑니다. 따라서 이 조건에서는 가장 높은 linear probe 정확도를 주는 깊이와 가장 낮은 FID를 주는 깊이가 다릅니다. 저자들은 나머지 층이 고주파 세부에 집중할 수 있다고 해석하며, 깊이 선택의 추가 분석을 후속 과제로 남깁니다.

### 16. 정렬 목적 함수와 λ

- section: S5
- message: 두 400K ablation에서 cosine과 NT-Xent의 FID 차이는 0.1이며, \(\lambda\)를 0.5보다 높였을 때의 추가 FID 개선도 최대 0.1입니다.
- on-slide facts:
  - 목적 함수 · ImageNet 256×256, SiT-L/2, 400K, DINOv2-L, layer 8, \(\lambda=0.5\), no CFG, NFE 250 · 열 순서 FID↓ / sFID↓ / IS↑ / Acc.↑ (%) · NT-Xent 10.0 / 5.09 / 106.6 / 68.1 · cosine 9.9 / 5.34 / 111.9 / 68.2
  - \(\lambda\) · ImageNet 256×256, SiT-XL/2, 400K, no CFG 조건은 Table 8 대응 행 기준 · 열 순서 FID↓ / IS↑ · 0.25: 8.6 / 118.6 · 0.5: 7.9 / 122.6 · 0.75: 7.8 / 124.4 · 1.0: 7.8 / 124.8
  - 50–100K의 NT-Xent 우세는 §4.2 본문 서술 · 후속 실험은 cosine 채택 · timestep별 \(\lambda\)는 미실험
- source: §4.2, p. 8, Table 2 · §4.4, p. 10, Table 5 · App. G, Table 8 · App. M, p. 43
- block: `split 54:46` · 왼쪽 `table`에 목적 함수 · 오른쪽 `table`에 \(\lambda\) · 두 표 위에 각 모델과 비교 조건 표시 · `tone: wash`
- assets: Table 2 objective 행, Table 5, Table 8의 \(\lambda=0.5\) 대응 수치
- interaction: none
- time: 50초
- notes: 왼쪽은 SiT-L/2에서 목적 함수만 바꾼 결과입니다. 400K에서 cosine의 FID가 0.1 낮고 sFID는 NT-Xent가 더 낮습니다. 저자들은 50K에서 100K 사이에는 NT-Xent가 유리했다고 서술합니다. 오른쪽은 SiT-XL/2의 별도 실험이며, \(\lambda\)를 0.25에서 0.5로 올릴 때 FID가 0.7 낮아지고 그 이후에는 최대 0.1 더 낮아집니다.

### 17. SiT 크기별 수렴

- section: S5
- message: DINOv2-B를 공통 target으로 쓴 비교에서 큰 SiT + REPA 모델이 표시된 초기 checkpoint에서 더 낮은 FID에 도달합니다.
- on-slide facts:
  - ImageNet 256×256, no CFG · DINOv2-B, cosine, \(\lambda=0.5\) · B/2 layer 4, L/2·XL/2 layer 8
  - Fig. 5b · REPA 세 모델의 50K–400K 수렴 곡선 · vanilla 수평선은 모델별 400K FID 기준, B/2 33.0 / L/2 18.8 / XL/2 17.2는 Table 3 수치
  - Fig. 5c · 50K·100K·200K·400K의 validation Acc.–FID 궤적 · 모델 크기에 따른 진행 차이는 **곡선 근거**
  - 200K, FID / Acc. (%) · B/2 33.2 / 50.9 · L/2 14.0 / 66.3 · XL/2 11.1 / 67.3 · 수치는 Table 8
- source: §4.2, p. 8, Fig. 5b–c · Table 3, p. 9 · App. G, p. 25, Table 8
- block: `split 52:48` · 왼쪽 `figure`에 Fig. 5b · 오른쪽 `figure`에 Fig. 5c · 하단에 200K 확인 수치 · `tone: wash`
- assets: Fig. 5b–c 크롭, 축·범례 포함 · Tables 3·8의 기준값과 checkpoint 수치
- interaction: none
- time: 50초
- notes: 왼쪽의 수평선은 vanilla 모델별 400K FID이고, 학습 진행을 잇는 곡선은 REPA 모델 세 개입니다. 이 구성은 앞서 본 400K 단면에 초기 수렴 경로를 더합니다. 200K에서 B/2, L/2, XL/2의 FID는 각각 33.2, 14.0, 11.1이며, 같은 시점의 probe 정확도도 모델 크기 순으로 높습니다. Target encoder와 목적 함수는 공통이고 정렬 층은 B/2와 나머지 두 모델에서 다릅니다.

### 18. 노이즈 수준별 표현 격차

- section: S5
- message: Fig. 7에서 REPA를 적용한 SiT-XL/2는 시험한 세 timestep 모두에서 vanilla보다 높은 linear probe 정확도와 최대 CKNNA를 보입니다.
- on-slide facts:
  - Fig. 7 · \(t=0,\ 0.25,\ 0.5\) · SiT-XL/2 vanilla/REPA · ImageNet validation Acc.와 clean DINOv2-g 기준 최대 CKNNA · 우세 방향은 **막대 근거**
  - Fig. 8 한 줄 · SiT-L/2의 MoCov3-L·MAE-L target별 CKNNA는 layer 8 부근에서 높고 후반 층에서 vanilla SiT-XL/2 수평 기준선 아래로 하락, **곡선 근거**
  - Fig. 7–8 비교 checkpoint의 학습 step 미명시
- source: §4.4, pp. 9–10, Fig. 7a–b·Fig. 8a–b
- block: `split 80:20` · 왼쪽 `figure`에 Fig. 7 두 패널 · 오른쪽 `bullets`에 timestep, 평가 기준, Fig. 8 한 줄 · `tone: wash`
- assets: Fig. 7a–b 크롭, 축·범례 포함
- interaction: none
- time: 45초
- notes: 이 실험은 입력 노이즈 수준을 세 가지로 바꾸어 표현을 평가합니다. 세 timestep 모두에서 REPA 모델의 linear probe 정확도와 최대 CKNNA가 vanilla보다 높습니다. Fig. 8에서 다른 encoder를 target으로 썼을 때도 정렬 층 부근의 CKNNA는 높지만, 후반 층에서는 vanilla 기준선 아래로 내려갑니다. Fig. 8의 정렬 모델은 SiT-L/2이고 vanilla 기준은 SiT-XL/2입니다.

### 19. 해상도와 조건 입력의 확장

- section: S5
- message: 부록에서 REPA는 ImageNet 512×512와 MS-COCO text-to-image에서도 FID를 낮췄으며, 512×512의 일부 생성 지표는 개선되지 않았습니다.
- on-slide facts:
  - **ImageNet 512×512** · SiT-XL/2, CFG \(w=1.35\) · 열 순서 FID / sFID / IS / Pre. / Rec. · vanilla 600 epochs: 2.62 / 4.18 / 252.2 / 0.84 / 0.57 · REPA 100 epochs: 2.32 / 4.16 / 255.7 / 0.84 / 0.56 · REPA 200 epochs: 2.08 / 4.19 / 274.6 / 0.83 / 0.58
  - **MS-COCO validation** · MMDiT, 양쪽 150K step, batch 256, SDE NFE 250, CFG \(w=2.0\) · FID 5.30→4.14, \(\Delta=-1.16\)
  - 적용 범위 · pixel-space diffusion, video, 대규모 text-to-image 학습은 App. M의 후속 과제
- source: App. J, p. 40, Table 11 · App. K, pp. 41–42, Table 12 · App. M, p. 43
- block: 전폭 `cards` 2개에 벤치마크별 결과 · 하단 한 줄에 적용 범위
- assets: Table 11의 SiT 세 행과 Table 12의 SDE 두 행 수치
- interaction: none
- time: 40초
- notes: ImageNet 512×512에서는 REPA 100 epochs의 FID가 2.32로 vanilla 600 epochs의 2.62보다 낮습니다. 부록은 네 지표의 개선을 서술하지만, 100 epochs의 precision은 동률이고 200 epochs에서는 sFID와 precision이 vanilla보다 나쁩니다. MS-COCO에서는 양쪽 MMDiT를 150K step 학습하고 같은 SDE 설정으로 평가했을 때 FID가 5.30에서 4.14로 내려갑니다. Pixel-space diffusion, video, 대규모 text-to-image는 논문이 후속 과제로 남긴 범위입니다.

### 20. 정리와 토론

- section: S6
- message: REPA의 step 대비 FID 개선을 바탕으로, 정렬 깊이와 지속 시간, 지표 선택, 학습 비용을 토론합니다.
- on-slide facts:
  - **정리** · Vanilla SiT의 표현 격차 → clean patch target을 이용한 중간 층 정렬 → ImageNet 256×256 no-CFG의 step 대비 FID 개선
  - **근거 · 정렬 깊이** · SiT-L/2, 400K, layer 8→16에서 Acc. \(+3.0\) pp와 FID \(+2.1\) · 저자의 고주파 세부 가설과 iREPA의 공간 구조 결과(`external`) · 층별 주파수·공간 구조를 어떻게 측정할 것인가?
  - **근거 · 평가 설정** · 같은 SiT-XL/2 + REPA 4M checkpoint에서 ADM FID-50K로 interval 후보를 비교하고 최저 FID 1.42를 보고 · 일반 CFG FID/sFID 1.80/4.50, 선택한 interval 1.42/4.70 · 설정 선택과 최종 보고를 어떻게 검증할 것인가?
  - **근거 · 설정 기록** · Table 3의 SiT-L/2 400K FID 9.7은 Table 2의 DINOv2-B·NT-Xent와 일치 · Table 7이 명시한 L/2 700K 설정은 DINOv2-L·NT-Xent이며, Table 2에서 이 조합의 400K FID는 10.0 · 400K 행의 설정을 어떻게 재현할 것인가?
  - **대가 · 해석** · target encoder forward와 feature 사전 계산의 저장·I/O 비용 · 논문에서 사전 계산한 것은 VAE latent · 보고 처리량 약 5.4 step/s, H100 80GB 8장·batch 256, 측정 모델 크기·해상도와 대응 vanilla 처리량 미제시 · Fig. 3b·8의 후반 **층** 정렬 하락과 HASTE의 후반 **학습** 정체·저하(`external`) · REPA 논문의 no-CFG SiT-XL/2는 1M→4M에서 FID 6.4→5.9 · 동일 wall-clock에서 정렬 손실 유지 기간을 어떻게 비교할 것인가?
- source: Fig. 2·3b·8 · §4.2, Table 2 · Tables 3–4 · App. D, p. 23, Table 7 · App. E, p. 24 · App. G, Table 10 · `external` [iREPA 초록](https://arxiv.org/abs/2512.10794), [HASTE 초록](https://arxiv.org/abs/2505.16792)
- block: 어두운 `statement` · `split 27:73` · 왼쪽 `lead`와 `groups`에 정리 · 오른쪽 `cards` 4개를 2×2 배치 · 대가 카드에 `note: 해석`
- assets: Tables 2·3·4·7·10의 토론용 수치 발췌
- interaction: none
- time: 120초
- notes: 정리하면 vanilla SiT의 표현 격차를 진단한 뒤 clean patch target을 중간 층에 정렬했고, ImageNet 256×256에서 step 대비 FID 개선을 확인했습니다. 깊이 실험에서는 probe 정확도와 FID가 반대 방향으로 움직이므로, 저자의 고주파 세부 가설과 iREPA가 제기한 공간 구조의 역할을 층별로 어떻게 측정할지 토론할 수 있습니다. Guidance interval은 보고 지표와 같은 FID로 후보를 비교했고 sFID의 순위는 달랐으므로, 설정 선택과 최종 평가의 기준도 논의할 수 있습니다. 재현할 때는 Table 7이 제시한 700K 설정과 Table 3의 400K 결과를 연결할 근거가 더 필요합니다. 마지막으로 Fig. 3b와 Fig. 8의 후반 층 정렬 하락, HASTE의 후반 학습 정체 보고, REPA 논문의 1M 이후 FID 개선을 함께 놓고, encoder 비용까지 포함한 학습시간 기준으로 정렬 손실을 언제까지 유지할지 토론하겠습니다.

### 21. 감사합니다 · Q&A

- section: S6
- message: 질문과 토론을 받겠습니다.
- on-slide facts: 감사합니다 · Q&A · [발표자 이름] · VILAB · 논문 · 프로젝트 페이지 · 공식 코드, MIT License (`external`)
- source: p. 1, arXiv ID·프로젝트 페이지 · p. 11, 구현 공개 문구 · `external` 공식 저장소 및 MIT License는 제공된 `research_verified.md`의 확인 기록. [논문](https://arxiv.org/abs/2410.06940) · [프로젝트 페이지](https://sihyun.me/REPA) · [공식 코드](https://github.com/sihyun-yu/REPA)
- block: `ending` · `split 65:35` · 왼쪽 `lead`에 감사와 Q&A · 오른쪽 `groups`에 발표자와 링크 3줄
- assets: none
- interaction: none
- time: 15초
- notes: 들어 주셔서 감사합니다. 논문과 프로젝트 페이지, 공식 코드 링크를 화면에 두었습니다. 질문과 의견을 받겠습니다.

## Not applied

- **C1·C2의 압축 제안.** 18–19장이나 분석 4장 이내로 줄이는 원안은 채택하지 않았다. 수용 로그의 최종 구조에 따라 21장, 분석 5장과 적용 범위 1장으로 구성했다. 400K 동일 step 비교와 SiT 크기별 수렴 비교는 각각 11번과 17번에 두었다.
- **C5·C6의 부록 Fig. 38 토글 및 Fig. 10 추가.** 수용 로그에 따라 Fig. 38을 제외했다. Fig. 10의 DiT 진단도 이번 발표에서는 생략하고 DiT를 11번 생성 성능 비교에 포함했다.
- **C7의 Fig. 4 클래스별 시각 차이 확정.** 지정 폴더 접근 오류로 Fig. 4 원본 이미지를 직접 확인하지 못했다. 앵무새는 검토 로그의 이미지 판독을 해석으로 표시했고, 열기구와 햄버거는 화면에서 비교할 구체적인 시각 요소까지 지정했다.
- **C8·V1의 GitHub 링크 삭제.** 제공된 조사 기록에서 공식 저장소와 MIT License를 확인했으므로 `external`을 붙여 ending에 유지했다. R4의 REPA-E와 SRA는 토론 시간 배분을 위해 생략했다.