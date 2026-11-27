## Ledger

- Fig. 1 — use: 1(왼쪽 구조도), 5(구조도 재구성), 14(오른쪽 GenEval 곡선)
- Fig. 2 — use: 13(Saturn 생성, 베네치아 카니발 가면 편집)
- Fig. 3 — use: 6(Joint·AF 도식, 층별 CKA, cosine·PSNR 곡선)
- Fig. 4 — use: 5(구조도 재구성), 7(AF 내부), 8(\(z\)의 두 출력 경로)
- Fig. 5 — use: 5(a–b 구조 재구성), 9(a–b 구조와 d의 관측 한 줄) / cut: c는 18장의 Table 13에서 동일 비교의 생성 지표와 추론 비용을 함께 제시
- Fig. 6 — use: 15(a 외부 vision encoder, b 조건 모델), 16·20(b의 비교 결과 인용)
- Fig. 7 — use: 15(2B 상태), 16(백본 크기 비교 인용)
- Fig. 8 — use: 17(융합 방식별 cosine·PSNR 곡선)
- Fig. 9 — use: 18(MMDiT 비교 곡선), 9(891M 규격 인용)
- Table 1 — use: 11(최종 재구성), 14(AF·FLUX.1-VAE의 PSNR)
- Table 2 — use: 11(20개 이해 벤치마크 평균 유지율과 개별 변화)
- Table 3 — use: 12(이해·생성 시스템 비교)
- Table 4 — use: 12(ImgEdit-Bench Overall 막대그래프)
- Table 5 — use: 13(WISE-Verified의 직접 생성·CoT)
- Table 6 — use: 13(KRIS-Bench 지식 범주별 점수)
- Fig. 10 — use: 15(a GenEval 곡선, b–c 발표 메모), 16(a–c 결과 인용)
- Fig. 11 — cut: 제거 깊이와 남는 feature 수가 함께 바뀌어 깊이별 역할을 분리하기 어려움
- Table 7 — use: 10(학습 일정·GPU), 14·19·20(통제 비교의 학습 예산)
- Table 8 — use: 15(2B의 이해 성능 유지율)
- Table 9 — use: 15(SigLIP2-AF와 2B AF), 16(비교 조건)
- Table 10 — use: 17(20K-step AF 구성요소 비교), 19(의미 보존 평가 범위)
- Table 11 — use: 15·16(의미 감독 제거와 재구성)
- Table 12 — use: 19(AF 이해 추론 비용), 20(prefill 비용 인용)
- Table 13 — use: 18(Full MoT의 생성 성능·추론 비용)

## Sections

- `summary` — 요약 (2)
- `background` — 배경 (3–5)
- `method` — 방법 (6–10)
- `results` — 결과 (11–13)
- `analysis` — 분석 (14–19)
- `discussion` — 정리와 토론 (20–21)

1920×1080 HTML 덱. 21장, 1,200초. 슬라이드 순서와 블록은 목표 구조를 따르고, 통제 비교가 **8:55**에 시작하도록 시간 배분을 조정했다. 20장에 **2:30**을 배정하고 21장은 토론 중 띄워 둔다. 구간은 하단 진행 표시줄로 표시한다. 인터랙션은 5·13·15장, 대표 인터랙션은 15장이다. 클리커의 다음 입력은 현재 장의 beat 또는 상태를 먼저 넘긴다.

## Slides

### 1. Integral의 공유 시각 표현

- section: none
- time: 20초
- message: 오늘은 Integral의 통제 실험을 따라가며 이해와 생성이 같은 시각 토큰을 쓸 때 어떤 이득이 관측되는지 살펴보겠습니다.
- on-slide facts: 원제 *Let Vision-Language Models Generate Images through Their Representations* / JB Kim 외 · NAVER Cloud, KAIST / arXiv:2611.31237v1, preprint(`external`) / 발표자 오희석(VILAB, 한성대학교)
- source: p. 1 제목·저자·소속, Fig. 1. `external` [arXiv 논문 정보](https://arxiv.org/abs/2611.31237)
- block: 표지, `split 48:52` 왼쪽 `lead`와 발표 정보 / 오른쪽 `figure`
- assets: Fig. 1 왼쪽 Integral 구조도
- interaction: none
- notes: 안녕하십니까, 한성대학교 VILAB 오희석입니다. 오늘 소개할 논문은 사전학습 VLM에 이미지 생성을 붙인 Integral입니다. 같은 시각 표현을 썼을 때 생긴 차이를 통제 실험 중심으로 보겠습니다.

### 2. Integral 한눈에 보기

- section: `summary`
- time: 35초
- message: Integral은 동결된 사전학습 VLM을 이해와 생성이 시각 토큰 \(z\)를 공유하는 모델로 확장합니다.
- on-slide facts: 한 문장 요지 — Integral은 동결 VLM을 공유 시각 토큰 기반의 이미지 생성 모델로 확장합니다. / 기여 3개 — AF의 계층 특징 융합과 공유 \(z\) / Block-wise MoT의 경계별 조건 전달과 생성 전용 0.89B / 동일 생성 설정에서 공유·분리 tokenizer를 비교한 256² T2I 50K-step GenEval 실험
- source: Abstract, §1 Contributions, pp. 1–3, §§2.2–2.3, pp. 4–6, §3.4, p. 9
- block: 어두운 statement / `lead` 요지 / `groups` 기여 3열
- assets: none
- interaction: none
- notes: AF는 동결된 vision encoder의 여러 층에서 특징을 모아 이해와 생성이 사용하는 토큰을 만듭니다. Block-wise MoT는 VLM의 블록 경계에서 생성 경로에 조건을 전달합니다. 저자들은 재구성 품질이 비슷한 두 tokenizer의 생성 격차를 표현 공유의 이득으로 해석합니다.

### 3. 통합 멀티모달 모델의 갈래

- section: `background`
- time: 40초
- message: 통합 멀티모달 모델은 시각 표현을 어떻게 정의하고 이해와 생성에 어디까지 공유하는지에 따라 갈립니다.
- on-slide facts:
  - 표의 열 `갈래 | 대표 모델 | 시각 표현·경로` — 이산 autoregressive / Chameleon, Emu3 / 이산 토큰
  - autoregressive와 diffusion·flow 결합 / Transfusion, Show-o2 / 연속 시각 표현과 별도 생성 objective
  - 연속 시각 표현 공유 / Harmon, Ming-UniVision / 이해·생성이 연속 표현을 공유
  - 경로 특화 / Janus-Pro, BAGEL, MetaQuery / 시각 인코딩 분리, 생성 expert, 사전학습 VLM에 생성 경로 연결
  - 화면 마지막 줄 — 재구성 품질이 비슷할 때, 같은 시각 표현을 쓰면 생성 학습이 어떻게 달라지는가?
- source: §3.2 Baselines, p. 7, §4, pp. 10–11
- block: `table` 연구 갈래 4행 / 하단 `callout` 발표 질문
- assets: §3.2·§4의 모델 분류를 옮긴 표
- interaction: none
- notes: 논문은 이산 토큰으로 통합하는 계열과 연속 표현에 diffusion이나 flow를 결합하는 계열을 소개합니다. Janus-Pro, BAGEL, MetaQuery처럼 이해와 생성의 일부 경로를 나누는 방법도 있습니다. Harmon과 Ming-UniVision은 Integral에 가까운 연속 표현 공유 계열입니다. 이 발표에서는 재구성 품질이 비슷할 때 표현 공유가 생성 학습에 어떤 차이를 만드는지 묻겠습니다.

### 4. 이해용 표현과 생성용 latent

- section: `background`
- time: 30초
- message: Integral이 풀려는 문제는 기존 VLM이 사용하는 의미 표현과 픽셀 복원에 필요한 세부 정보를 같은 토큰에 담는 것입니다.
- on-slide facts: 이해 경로 — 사전학습 vision encoder의 고수준 특징과 VLM 시각 embedding / 생성 경로 — FLUX.1-VAE와 같은 재구성 지향 latent / 설계 질문 — 동결된 VLM의 입력을 유지하면서 이미지로 복원할 수 있는 표현을 어떻게 만드는가?
- source: §1, pp. 1–3, §§2.1–2.2, pp. 3–5
- block: `compare` 이해용 표현과 생성용 latent / 하단 `lead` 설계 질문
- assets: 두 표현 경로의 개념 도식
- interaction: none
- notes: 이해 경로에서는 VLM이 읽을 수 있는 의미 표현이 필요합니다. 생성 경로에서는 결과를 픽셀로 복원할 수 있도록 세부 정보도 담아야 합니다. Integral은 이 두 요구를 같은 토큰에 걸고, 기존 VLM이 그 토큰을 읽는 경로를 설계합니다.

### 5. Integral의 정보 흐름

- section: `background`
- time: 50초
- message: Integral은 생성 latent를 VLM과 공유하는 \(z\)로 바꾸고, VLM 조건을 생성 스트림에 전달하는 연결을 블록 경계에 둡니다.
- on-slide facts: 동결 VLM / 별도 FLUX.1-VAE latent / AF의 융합 표현 \(f\)와 공유 \(z\) / semantic projector / 생성 query와 경계 K/V / pixel decoder
- source: Fig. 1, p. 1, §2.2와 Fig. 4, Eqs. (1)–(2), pp. 4–5, §2.3과 Fig. 5a–b, Eqs. (4)–(5), pp. 5–6, §3.2, p. 7
- block: 전폭 `animation` / 이해 경로 위, 생성·디코딩 경로 아래 / 상태 전환 시 노드와 연결을 같은 캔버스에서 교체
- assets: Fig. 1·4·5a–b를 바탕으로 다시 그릴 SVG 한 장
- interaction: animation — reveals: 두 latent 경로가 \(z\)를 중심으로 어떻게 연결되고, VLM의 K/V가 어디에서 생성 스트림에 들어가는지 확인
  - beat 0 — `title` 분리된 생성 공간 / `text` BAGEL식 기존 설계에서 동결 VLM의 시각 입력과 별도 FLUX.1-VAE latent를 나란히 두고, Full MoT의 층별 생성 expert 연결을 표시. / 출처 §3.2, Fig. 5a, pp. 5, 7
  - beat 1 — `title` AF와 공유 \(z\) / `text` 별도 VAE latent 자리를 다층 특징 → AF의 \(f\) → bottleneck의 \(z\)로 교체하고, \(z\) 공간을 VLM 입력 projector와 생성·pixel decoder 경로에 연결. / 출처 Figs. 1·4, §2.2, Eqs. (1)–(2), pp. 1, 4–5
  - beat 2 — `title` 블록 경계의 조건 전달 / `text` 층마다 짝지은 expert를 32층 VLM의 4층 간격 생성 블록 8개로 재배치하고, VLM K/V가 들어오는 경계만 표시. / 출처 §2.3, Fig. 5b, Eq. (4), App. A.1, pp. 5–6, 18
  - beat 3 — `title` 분석에서 답할 질문 / `text` 공유 표현의 생성 이득에 재구성 품질 외 어떤 요인이 관여하는가? 그 이득은 어떤 모델과 학습 조건에서 확인됐는가? / 출처 §§3.4–3.5, App. C.1, pp. 9–10, 20–21
- notes: 먼저 VLM의 시각 입력과 생성 latent가 나뉘고 층마다 생성 expert가 연결되는 설계를 보겠습니다. [1] Integral에서는 여러 층의 특징이 AF와 bottleneck을 지나 \(z\)가 되며, 이 공간을 VLM 입력과 이미지 생성에 함께 씁니다. [2] 생성 스트림이 VLM으로부터 받는 값은 네 층마다 들어오는 K/V입니다. [3] 이제 재구성 품질 외에 무엇이 이득과 관련되는지, 어느 조건까지 확인됐는지를 두 질문으로 남겨 두겠습니다.

### 6. Propagation bottleneck 가설

- section: `method`
- time: 55초
- message: 저자들은 공동 학습에서 깊은 층이 초기층과 더 비슷해지는 관측이 propagation bottleneck 가설과 일치한다고 해석합니다.
- on-slide facts:
  - 저자 가설 — 최종층만으로 픽셀을 복원하도록 학습하면 깊은 층이 초기층의 세부 정보를 유지하게 되어 의미 추상화가 제약될 수 있음
  - Fig. 3b — Joint의 깊은 층에서 초기층 대비 CKA 상승, 강한 의미 감독에서 상승 폭 감소 / **CKA는 층 간 상관 근거, 가설의 인과 개입 검증 미보고**
  - Fig. 3c, 20K tokenizer step — AF cosine ≈0.971, Frozen ≈0.972 / 강한 의미 감독 Joint의 PSNR은 학습 중 상승하되 20K에서 ≈23.2 dB, 일반 Joint ≈26.3 dB보다 낮음 / 모두 곡선 근거
- source: §2.1, pp. 3–4, Fig. 3a–c
- block: 전폭 `figure` / Fig. 3a–c의 축·범례 유지 / 하단 `bullets` 3개
- assets: Fig. 3a–c
- interaction: none
- notes: 저자들은 최종층에서 픽셀을 복원하려면 초기층의 세부 정보가 깊은 층까지 유지되어야 할 수 있다고 봅니다. Fig. 3b에서 Joint의 깊은 층은 초기층과의 CKA가 높고, 의미 감독을 강화한 경우에는 그 상승 폭이 줄어듭니다. 오른쪽 곡선에서 강한 의미 감독을 둔 Joint의 PSNR도 학습 중 올라가지만 일반 Joint보다 낮습니다. CKA가 보여 주는 것은 층 간 유사도이며, 이 가설의 인과 경로는 직접 검증되지 않았습니다.

### 7. Abstraction Fusion의 토큰 구성

- section: `method`
- time: 40초
- message: AF는 같은 이미지 위치에서 vision encoder의 여러 층이 내놓은 특징을 모아 하나의 시각 토큰으로 압축합니다.
- on-slide facts: 동결 Qwen3.5-9B vision encoder 27블록, \(16\times16\) patch, \(d_h=1152\) / patch embedding을 포함한 표현 28개 / ImageNet 학습 이미지 50K장으로 구한 고정 층별 정규화 통계 / 연속 4개 표현씩 공동 projection해 위치당 feature 7개 / 층 방향 16-head self-attention과 linear pooler의 출력 \(f\), \(d_f=1152\) / diagonal Gaussian bottleneck의 출력 \(z\), \(d_z=256\), 학습 시 샘플링·추론 시 posterior mean
- source: §2.2, p. 4, Fig. 4, Eq. (1), App. A.1, p. 18
- block: `split 40:60` 왼쪽 `figure` / 오른쪽 `process` 28개 표현 → 7개 feature → attention·pooling → \(f\) → \(z\)
- assets: Fig. 4의 AF·bottleneck 크롭, Eq. (1)의 차원 표기
- interaction: none
- notes: Qwen3.5-9B의 27개 블록 출력에 patch embedding을 더하면 표현이 28개입니다. 각 이미지 위치에서 연속한 네 표현씩 묶고, 일곱 feature에 층 방향 attention을 적용합니다. Eq. 1이 정의하는 융합 출력은 \(f\)입니다. 이 \(f\)가 variational bottleneck을 지나면 256차원 토큰 \(z\)가 됩니다.

### 8. AF의 두 출력과 학습 목표

- section: `method`
- time: 45초
- message: AF는 같은 \(z\)에서 기존 VLM의 시각 embedding을 예측하고 픽셀을 복원하도록 학습합니다.
- on-slide facts: semantic projector — \(2\times2\) 이웃 토큰 병합, MLP 출력 \(d_s=4096\), 표적 \(s\)는 사전학습 VLM의 시각 embedding / pixel decoder — RAE ViT-XL, 28층, 폭 1152 / \(\mathcal L_{\mathrm{rec}}=\ell_1+\mathrm{LPIPS}\), KL 표적은 표준 Gaussian / \(\lambda_{\mathrm{sem}}=5.0,\ \beta_{\mathrm{KL}}=10^{-6},\ r=0.3\) / Eq. (6)의 토큰별 RMS 정규화 MSE는 \(2(1-\cos(\hat s,s))\)(계산), 본문 §2.2의 cosine-distance 항에 해당
- source: §2.2, Fig. 4, Eqs. (2)–(3), pp. 4–5, App. A.1–A.2, Eq. (6), p. 18
- block: `split 43:57` 왼쪽 `diagram` \(z\) → \(\hat s,\hat x\) / 오른쪽 `equation` Eqs. (3), (6)과 기호 설명
- assets: Fig. 4의 출력 경로를 단순화한 SVG, Eqs. (3), (6) LaTeX
- interaction: none
- notes: 위쪽 projector는 이웃 토큰 네 개를 합쳐 기존 VLM의 4096차원 시각 입력을 맞춥니다. 아래쪽 ViT-XL decoder는 같은 \(z\)에서 이미지를 복원합니다. 의미 손실은 원본 embedding의 MSE와 토큰별 RMS 정규화 MSE를 섞습니다. 정규화된 두 벡터의 평균 제곱 차를 전개하면 cosine distance의 두 배가 됩니다.

### 9. Block-wise MoT의 조건 전달

- section: `method`
- time: 45초
- message: Block-wise MoT는 생성 스트림의 query가 VLM 블록 경계에서 두 스트림의 K/V를 참조하도록 설계합니다.
- on-slide facts:
  - Qwen3.5-9B language backbone 32층 / 4층 간격으로 생성 블록 8개 / \(z_t\)는 2층 MLP를 거쳐 생성 스트림에만 입력
  - attention QKV 차원은 VLM에 맞춤 / 나머지 연산 폭 \(d_g=2048\) / 블록마다 adaLN-single로 timestep 주입
  - DDT head 2블록, 폭 3072, velocity 예측 / 생성 전용 0.89B(891M, Fig. 9)
  - Fig. 5d — 50K-step T2I에서 adaLN-single의 GenEval이 입력 timestep embedding 방식보다 높음(곡선 근거)
- source: §2.3, Fig. 5a–b·d, Eqs. (4)–(5), pp. 5–6, §3.6와 Fig. 9, p. 10, App. A.1, p. 18, App. C.2와 Table 13, pp. 21–22
- block: `split 54:46` 왼쪽 `figure` Fig. 5a–b / 오른쪽 `groups` 조건 전달과 생성 규격 / 하단 Fig. 5d 관측 한 줄
- assets: Fig. 5a–b 크롭, Eq. (4)의 Q/K/V 표기
- interaction: none
- notes: 생성 query가 참조하는 것은 생성 스트림 자신의 K/V와 해당 경계의 동결 VLM K/V입니다. 각 생성 블록에는 adaLN-single로 시간을 넣고, 마지막 DDT head가 velocity를 예측합니다. 입력에 timestep embedding을 더하는 방식보다 adaLN-single의 GenEval 곡선이 높습니다. 발표 메모로 남길 점은 App. A.1의 32층과 App. C.2의 Full MoT 31블록 표기 차이이며, 논문은 그 관계를 설명하지 않습니다.

### 10. 학습 단계와 규모

- section: `method`
- time: 30초
- message: Integral은 tokenizer를 먼저 학습해 latent 공간을 고정하며, 50K-step 통제 비교는 본 모델의 생성 첫 단계 안에 해당합니다.
- on-slide facts:
  - 표의 열 `단계 | step | 해상도 | H100` — tokenizer 1: 200K / 256² / 8장, tokenizer 2: 400K / 256–512 동적 해상도 / 8장, tokenizer 3: pixel decoder adversarial fine-tuning 50K / 256² / 8장
  - 생성 1: T2I pretraining 200K / 256² / 32장, 생성 2: interleaved pretraining 50K / 최대 512² / 48장, 생성 3: interleaved SFT 350K / 최대 512² / 48–64장
  - 50K 생성 통제 예산 = Stage 1의 \(1/4\), 전체 생성 일정 600K step(계산) / SFT 데이터 예시: GPT-Image-Edit-1.5M, Echo-4o-Image, Zebra-CoT
  - 생성 표적 — 채널별 표준화한 AF posterior mean / flow matching velocity 표적 \(\epsilon-z\) / logit-normal timestep, time shift 4.0
- source: §§2.3, 3.1, 3.4, pp. 6, 9, App. A.2, pp. 18–19, Table 7
- block: `table` tokenizer·생성 각 3행 / 하단 `callout` 50K의 위치
- assets: Table 7의 Training steps·Resolution·GPUs 행
- interaction: none
- notes: 먼저 tokenizer를 학습하고, 마지막에는 latent 공간을 고정한 채 pixel decoder만 미세조정합니다. 생성 학습은 256 해상도의 T2I부터 시작해 interleaved pretraining과 SFT까지 이어집니다. 이후 분석에서 볼 생성 50K는 첫 단계 200K의 4분의 1이며, tokenizer 구조를 비교하는 20K는 별도 예산입니다.

### 11. AF의 재구성과 이해 유지

- section: `results`
- time: 35초
- message: 최종 AF tokenizer는 ImageNet에서 높은 재구성 품질을 보이며 Qwen3.5-9B의 20개 이해 벤치마크 점수를 평균 99.8% 유지합니다.
- on-slide facts:
  - ImageNet-1k 256² 재구성, 열 순서 `rFID↓ | PSNR↑(dB) | SSIM↑` — Qwen3.5-9B+AF `0.15 | 32.2 | 0.942`, FLUX.1-VAE `0.17 | 31.1 | —`, PS-VAE `0.20 | 28.8 | 0.817`, VA-VAE `0.28 | 28.0 | 0.790`
  - Qwen3.5-9B → Qwen3.5-9B+AF, 이해 20개 벤치마크 평균 유지율 `100.0% → 99.8%`
  - 같은 기준 대비 점수 Δ(계산) — MMB −0.9, MMMU +0.3, OCRBench −0.8
- source: §2.2, pp. 4–5, Tables 1–2, App. B.1, pp. 19–20
- block: `split 58:42` 왼쪽 `table` 재구성 지표 3개 / 오른쪽 `deltas` 이해 지표 3개 / 평균 유지율 숫자 1개
- assets: Tables 1–2 선택 행·열
- interaction: none
- notes: 왼쪽의 32.2 dB는 전체 tokenizer 학습과 pixel decoder 미세조정 뒤의 재구성 결과입니다. 이해 성능은 원래 Qwen3.5-9B를 기준으로 20개 벤치마크에서 평균 99.8%를 유지합니다. 개별 지표에서는 MMMU가 소폭 오르고 MMB와 OCRBench는 소폭 내립니다.

### 12. 이해·생성 시스템 비교

- section: `results`
- time: 50초
- message: 최종 Integral은 기반 VLM에 가까운 이해 점수와 함께 생성·편집 시스템으로서 여러 비교 모델에 견줄 만한 결과를 냅니다.
- on-slide facts:
  - Table 3 선택 열 `Params | MMMU | OCRBench | GenEval | GenEval2 | GenEval++ | DPG` — Qwen3.5-9B `9B | 73.2 | 88.1 | — | — | — | —`, Integral `9.8B | 73.5 | 87.3 | 0.88 | 39.56§ | 0.743 | 84.76`, BAGEL `14B | 55.3 | 73.3 | 0.82 | 23.1§ | 0.371 | —`, TUNA-2 `12B | 50.7 | 79.7 | 0.87 | — | — | 86.54` / §는 CoT 사용
  - ImgEdit-Bench Overall, GPT-4.1 평가 — BAGEL 3.20, OmniGen2 3.43, Integral 3.50, GPT-4o 4.20 / Integral의 BAGEL 대비 Δ +0.30(계산)
  - **최종 시스템 비교, 백본·학습 데이터 비통제** / 기반 Qwen3.5-9B MMMU 73.2, BAGEL 시스템 55.3 / Integral SFT 데이터는 App. A.2 참조
- source: §3.2, pp. 6–8, Tables 3–4, App. A.2, p. 19
- block: `split 66:34` 왼쪽 `table` 이해·생성 지표 / 오른쪽 `bars` ImgEdit-Bench Overall 4모델 / 하단 비교 조건
- assets: Tables 3–4 선택 행·열
- interaction: none
- notes: 최종 Integral의 GenEval은 0.88이고, 편집의 ImgEdit-Bench Overall은 3.50입니다. 지표에 따라 순위가 달라지며, 예를 들어 DPG에서는 TUNA-2가 Integral보다 높습니다. 이해 점수는 Integral이 출발한 Qwen3.5-9B부터 BAGEL과 차이가 있습니다. 이 표의 비교에는 각 시스템의 백본과 학습 데이터 차이가 포함됩니다.

### 13. 세계 지식이 필요한 생성과 편집

- section: `results`
- time: 60초
- message: 세계 지식 평가에서 Integral의 성능은 문장이 가리키는 대상을 이미지로 만들거나 입력 이미지의 일부를 지식에 맞춰 바꾸는 과제로 드러납니다.
- on-slide facts: 두 상태 공통 — 최종 시스템 비교, 백본·데이터 비통제 / 상태별 예시 하나와 해당 벤치마크 결과
- source: §3.3, pp. 8–9, Tables 5–6, Fig. 2, p. 2, App. A.2, p. 19
- block: `toggle` 2상태 / 상태마다 `split 58:42` 왼쪽 `figureNumbered`, 오른쪽 생성은 `compare`, 편집은 `table` / 공통 하단에 시스템 비교 조건
- assets: Fig. 2 Saturn 생성 크롭, Venetian Carnival 편집 전후 크롭, Tables 5–6 선택 행·열
- interaction: toggle — reveals: 세계 지식이 생성에서는 대상 식별에, 편집에서는 입력 이미지의 교체 대상과 결과를 해석하는 데 쓰이는 과제 차이
  - [1] `label` 지식 생성 / `title` 고리로 알려진 행성 / `text` 바꾼 것 — 모델별 직접 생성↔명시적 CoT. 고정한 것 — WISE-Verified Overall과 각 모델 내 백본. 결과 — Integral 9.8B `0.5560 → 0.7877`(Δ +0.2317, 계산), BAGEL 14B `0.3520 → 0.6280`, FLUX.2-dev 56B 직접 생성 `0.5650`. Fig. 2는 행성 이름 없이 주어진 단서를 Saturn 이미지로 구체화한 예. 지우는 설명 — Integral과 BAGEL의 점수 차이가 한쪽에만 CoT를 허용해서 생겼다는 설명. / 출처 §3.3, Table 5, Fig. 2, pp. 2, 8–9
  - [2] `label` 지식 편집 / `title` 베네치아 카니발 가면 / `text` 바꾼 것 — 생성에서 입력 이미지가 있는 편집 과제로 전환하고 편집 시스템을 비교. 고정한 것 — KRIS-Bench의 지식 범주와 보고된 GPT-4o 평가 기준, 기준 점수는 공식 리더보드. 결과 — `Fact. | Concept. | Proc. | Overall` 순서로 Integral `65.35 | 59.27 | 56.58 | 60.79`, BAGEL `60.26 | 55.86 | 51.55 | 56.40`(Overall Δ +4.39, 계산). Fig. 2는 입력 이미지에서 가면을 베네치아 카니발 양식으로 교체한 예. 지우는 설명 — Overall 격차가 세 지식 범주 중 한 범주에만 있다는 설명. / 출처 §3.3, Table 6, Fig. 2, pp. 2, 8–9
- notes: [1] Saturn 예시는 행성 이름 없이 고리라는 단서로 대상을 특정해야 합니다. WISE-Verified에서는 두 모델 모두 CoT를 붙였을 때 점수가 오르고, 직접 생성에서는 FLUX.2-dev가 Integral보다 조금 높습니다. [2] 편집 예시에서는 입력 이미지가 주어지고, 지시가 가리키는 베네치아 카니발 가면으로 바꾸어야 합니다. KRIS-Bench에서 Integral과 BAGEL의 차이는 세 지식 범주 모두에서 나타나며, 여전히 서로 다른 시스템을 비교한 결과입니다.

### 14. AF와 FLUX.1-VAE 50K 비교

- section: `analysis`
- time: 85초
- message: 같은 VLM과 생성 설정에서 두 tokenizer의 최종 재구성 PSNR은 1.1 dB 차이였고 50K-step GenEval은 0.23 차이였습니다.
- on-slide facts:
  - 통제 — 동일 Qwen3.5-9B VLM conditioning, 생성 아키텍처·학습 설정 / 256² T2I, 50K step
  - 최종 tokenizer의 ImageNet-1k 256² PSNR — 전체 학습 AF 32.2 dB, 별도 사전학습 FLUX.1-VAE 31.1 dB, Δ +1.1 dB(계산)
  - 50K-step GenEval — AF 0.41, FLUX.1-VAE 0.18, Δ +0.23(계산), §3.4 본문 보고값
  - 남는 변수 — latent 차원·토큰 수·분포의 매칭 미보고
- source: Fig. 1, p. 1, Table 1, p. 4, §3.4, p. 9, App. A.2, Table 7, pp. 18–19
- block: `split 60:40` 왼쪽 `figure` / 오른쪽 `deltas` PSNR과 GenEval 각각 하나 / 하단 측정 조건
- assets: Fig. 1 오른쪽 GenEval 곡선 크롭, Table 1의 PSNR 및 §3.4 본문 수치
- interaction: none
- notes: 이 비교에서 VLM과 생성 학습 설정은 같고, 생성하는 latent를 AF와 FLUX.1-VAE 사이에서 바꿉니다. PSNR 두 값은 각 tokenizer의 최종본으로 ImageNet을 재구성한 결과입니다. 생성 모델은 별도로 256 해상도에서 50K step을 학습했고, 그때 GenEval 차이는 0.23입니다. 저자들은 이 간격을 표현 공유가 생성 학습에 이득을 준다는 근거로 해석합니다. 다음 비교에서는 의미 표현 자체, 조건 모델, 의미 감독, 백본 크기가 각각 어디까지 설명하는지 살펴보겠습니다.

### 15. 통제 비교 네 가지

- section: `analysis`
- time: 165초
- message: 네 비교는 공유 표현의 이득을 좁혀 가며, 특히 LLM 조건에서도 남는 AF의 우위와 VLM 조건에서 추가로 커지는 차이를 보여 줍니다.
- on-slide facts: 전 상태 공통 — 256² T2I 50K-step GenEval, x축 10K–50K / y축 0 기준, 0.4 눈금까지 공통 / Fig. 6a·6b·7의 상단은 ≈0.45(곡선 근거), Fig. 10a의 원본 y축 범위 0–0.43은 상태 캡션에 표시 / 논문 본문값과 곡선 판독값을 구분
- source: §§3.4–3.5, Figs. 6a–b·7, pp. 9–10, App. B.1–B.2, Tables 8–9, pp. 19–20, App. C.1, Table 11, Fig. 10a–c, pp. 20–21
- block: 전폭 `toggle` 4상태, 대표 인터랙션 / 동일 위치에 `figure`, 아래에 조건과 비교 결과 / 원본 축·범례 보존
- assets: Fig. 6a, Fig. 6b, Fig. 10a, Fig. 7 / Tables 8–9·11의 선택 수치
- interaction: toggle — reveals: 같은 생성 예산에서 한 비교씩 바꾸며, 각 결과가 배제하는 설명과 함께 바뀐 변수를 확인
  - [1] `label` SigLIP2-AF / `title` 외부 의미 표현의 효과 / `text` 바꾼 것 — vision encoder를 `siglip2-so400m-patch16-256`으로 바꾸면서 정렬 표적도 변경, ImageNet 256² PSNR `32.20 → 34.08 dB`. 고정한 것 — AF 아키텍처, Qwen3.5-9B VLM conditioning, 생성 설정. 결과 — 50K GenEval Qwen AF 0.41 대 SigLIP2-AF 0.31(Δ +0.10, 계산), SigLIP2의 ImageNet zero-shot 정확도는 AF 전후 0.83. 지우는 설명 — 의미를 보존하는 외부 tokenizer도 이 설정에서 Qwen AF와 같은 생성 성능을 낸다는 설명. / 출처 §3.4, Fig. 6a, App. B.2, Table 9, pp. 9, 20
  - [2] `label` LLM 조건 / `title` 조건 모델과 latent의 효과 / `text` 바꾼 것 — Qwen3.5-9B VLM↔text-only LLM, 비교 LLM의 모델명·규모 미보고. 고정한 것 — 각 조건 쌍 안에서 tokenizer와 생성 학습 예산. 결과 — VLM으로 바꿀 때 GenEval Δ는 AF +0.13, FLUX.1-VAE +0.01(§3.4 보고값). 50K의 LLM+AF ≈0.28 > VLM+FLUX.1-VAE ≈0.18, 20K 이후 이 순서 유지(곡선 근거). 지우는 설명 — 조건 VLM만으로 AF·FLUX.1-VAE의 격차가 생긴다는 설명. / 출처 §3.4, Fig. 6b, p. 9
  - [3] `label` 의미 정렬 제거 / `title` 의미 감독과 재구성의 분리 / `text` 바꾼 것 — AF의 semantic alignment objective 제거. 고정한 것 — Qwen3.5-9B AF 구조와 기타 tokenizer 학습 설정, 생성 비교 예산. 결과 — Table 11의 PSNR `32.2 → 33.7 dB`(Δ +1.5 dB, 계산), rFID `0.15 → 0.13`(Δ −0.02, 계산), 50K T2I에서 제거 조건의 GenEval 곡선이 낮음(곡선 근거). 지우는 설명 — 이 AF 비교에서 PSNR과 rFID 개선만으로 생성 성적도 좋아진다는 설명. / 출처 App. C.1, Table 11, Fig. 10a, pp. 20–21
  - [4] `label` 2B 백본 / `title` 작은 백본에서의 적용 범위 / `text` 바꾼 것 — AF를 Qwen3.5-9B에서 같은 계열의 2B 백본으로 옮김. 고정한 것 — 256² T2I 평가 설정과 50K 생성 step 예산. 결과 — 2B AF 0.26, 9B FLUX.1-VAE 0.18(Δ +0.08, 계산), 9B AF 0.41(2B AF 대비 Δ +0.15, 계산). 2B AF의 ImageNet 256² PSNR 32.33 dB, 2B 기준 이해 20개 평균 유지율 99.2%. 지우는 설명 — 9B 백본에서만 이 적용이 가능하다는 설명. 동일 크기의 2B×FLUX.1-VAE 비교는 미보고. / 출처 §3.5, Fig. 7, App. B.1–B.2, Tables 8–9, pp. 9–10, 19–20
- notes: [1] 같은 AF 구조를 쓴 SigLIP2가 재구성 PSNR은 더 높지만 50K GenEval은 낮고, 10K에서는 SigLIP2-AF가 오히려 앞서다가 20K 근처에서 두 곡선이 만납니다(곡선 근거). [2] LLM 조건과 VLM 조건을 교차하면 VLM을 넣었을 때 AF의 상승 폭이 더 큰 동시에, LLM+AF도 20K 이후 VLM+FLUX.1-VAE를 앞섭니다(곡선 근거). [3] 의미 감독을 제거한 AF는 PSNR과 rFID가 좋아지지만, GenEval과 부록의 DPG-Bench·WISE-Verified 곡선은 낮아집니다(곡선 근거). [4] 2B AF는 9B FLUX.1-VAE 기준을 앞서고 9B AF에는 뒤지며, Fig. 7에는 2B FLUX.1-VAE 조합이 없습니다.

### 16. 지운 설명과 남은 설명

- section: `analysis`
- time: 100초
- message: 이 비교들은 PSNR만으로 생성 순위를 설명하기 어렵다는 점을 보여 주지만, VLM과의 공유 효과를 latent 자체의 효과와 분리할 근거는 남아 있습니다.
- on-slide facts:

  | 대안 설명 | 이를 겨눈 비교 | 결과(조건 포함) | 지워졌나 |
  |---|---|---|---|
  | 재구성 PSNR만으로 생성 순위를 설명 | AF↔FLUX.1-VAE, AF↔AF w/o sem. | 최종 ImageNet-1k 256² PSNR: AF 32.2, FLUX.1-VAE 31.1, AF w/o sem. 33.7 dB. 256² T2I 50K GenEval: AF 0.41 대 FLUX.1-VAE 0.18, w/o sem.은 AF보다 낮음(곡선 근거). | **지움** — PSNR 단독 설명. latent 차원·토큰 수·분포의 영향은 남음. |
  | 의미 표현이면 어느 vision encoder든 충분 | Qwen AF↔SigLIP2-AF | 동일 VLM 조건, 256² T2I 50K GenEval `0.41 ↔ 0.31`. AF 구조 동일, vision encoder·정렬 표적·PSNR 변화. | **일부** — 이 외부 encoder에서는 격차가 남았고, encoder 용량과 정렬 표적의 효과는 분리되지 않음. |
  | 조건 모델의 차이만으로 설명 | tokenizer별 VLM↔LLM 교차 | 256² T2I 50K GenEval의 VLM 조건 Δ `+0.13 / +0.01`. LLM+AF ≈0.28 > VLM+FLUX.1-VAE ≈0.18(곡선 근거). | **일부** — latent 자체의 이득과 조건 VLM과의 공유 효과를 따로 추정하기 어려움. |
  | 의미 정렬 항의 효과가 잠재분포 변화와 독립적 | AF↔AF w/o sem. | AF 구조를 유지하고 의미 목적함수를 제거하자 256² T2I 50K에서 생성 지표가 하락(곡선 근거), 재구성은 개선. | **남음** — 의미 감독 제거의 효과는 관측. 학습된 latent의 분포를 맞춘 비교는 미보고. |
  | 9B 백본 규모가 결과를 결정 | 2B AF↔9B AF·9B FLUX.1-VAE | 256² T2I 50K GenEval `0.26 / 0.41 / 0.18`. | **일부** — 2B 적용 결과 확보. 2B×FLUX.1-VAE와 전체 생성 일정의 tokenizer 비교는 미보고. |

- source: §§3.4–3.5, pp. 9–10, Figs. 6–7, Tables 1, 7, 9, 11, App. C.1과 Fig. 10, pp. 20–21
- block: 전폭 `table` 4열·5행 / 하단 `callout` 256²·50K·GenEval 중심의 판단 범위
- assets: Figs. 6–7·10, Tables 1·9·11의 판정 근거를 요약한 표
- interaction: none
- notes: PSNR만으로 순위를 설명하는 가설은 의미 감독 제거 결과와 맞지 않습니다. SigLIP2 비교는 같은 AF 구조를 사용했지만, vision encoder와 정렬 표적도 함께 바뀌었습니다. Fig. 6b에서 VLM 조건의 추가 상승이 AF에 더 큰 것은 사실이고, 그 차이를 전부 표현 공유의 몫으로 배분하기는 어렵습니다. 검사 범위는 주로 256 해상도의 50K-step GenEval이며, 2B에서 tokenizer를 바꾼 짝 비교도 남아 있습니다.

### 17. AF 융합 방식 비교

- section: `analysis`
- time: 50초
- message: 20K-step tokenizer 비교에서 AF의 전체 융합 구성은 더 단순한 방식보다 재구성에 유리하면서 Frozen에 가까운 cosine을 유지합니다.
- on-slide facts:
  - Fig. 8, 20K tokenizer step — AF의 PSNR이 MLS보다 +6.27 dB(§3.6 보고값), AF cosine은 Frozen에 근접(곡선 근거) / 5K cosine에서는 MLS가 AF보다 소폭 높음(곡선 근거)
  - Table 10, 동일 20K tokenizer step, 열 순서 `PSNR↑(dB) | rFID↓ | Sem.↑` — AF `26.67 | 2.26 | 0.971`, 층별 norm·projection을 공유 방식으로 대체 `26.36 | 2.77 | 0.964`, self-attention 제거 `26.15 | 2.38 | 0.968`, attention pooling으로 교체 `21.92 | 13.12 | 0.953`
  - 재구성 참조 조건 — Table 10의 26.67 dB는 20K 비교, Table 1의 32.2 dB는 전체 tokenizer 학습 및 adversarial decoder 미세조정 후
- source: §3.6, Fig. 8, p. 10, App. C.1, Table 10, p. 20, Table 1, p. 4
- block: `split 58:42` 왼쪽 `figure` cosine·PSNR 원본 두 패널 / 오른쪽 `table` AF 구성요소 4행
- assets: Fig. 8 축·범례 포함, Table 10
- interaction: none
- notes: 왼쪽은 MLS와 attention pooling을 포함한 융합 방식 비교이고, 오른쪽은 AF의 구성요소를 바꾼 실험입니다. 20K에서 AF가 MLS보다 PSNR이 6.27 dB 높으며, 초기 5K에는 cosine에서 MLS가 소폭 앞섭니다. 구성요소를 바꾼 표에서도 온전한 AF의 세 지표가 가장 높거나 낮은 방향으로 모두 우세합니다. 20K의 26.67 dB는 앞에서 본 최종 tokenizer의 32.2 dB와 학습 시점이 다릅니다.

### 18. MMDiT·Full MoT와 구조 비교

- section: `analysis`
- time: 55초
- message: 같은 AF 공간을 쓰는 생성기끼리 비교하면 Block-wise MoT는 이 50K-step 설정에서 생성 성능과 추론 비용 사이의 절충을 보여 줍니다.
- on-slide facts:
  - Fig. 9, 동일 AF tokenizer·DDT predictor·256² T2I pretraining 설정 — Block-wise MoT 891M(0.89B), MMDiT 962M, 생성 전용 Δ −71M(계산) / 10K–50K에서 Block-wise MoT의 GenEval이 높음(곡선 근거)
  - Table 13, 동일 AF와 50K-step T2I, 열 순서 `Blocks | GenEval↑ | WISE-Verified↑ | DPG↑ | latency/step↓ | latency/batch↓ | compute↓` — Block-wise `8 | 0.41 | 0.39 | 72.95 | 16.1 ms | 858 ms | 387.6 TFLOPs`, Full `31 | 0.39 | 0.41 | 72.02 | 52.0 ms | 2659 ms | 970.7 TFLOPs`
  - Full/Block-wise — compute 2.50×, latency/batch 3.10×(계산) / 동일 생성 설정, 배치 크기·denoising step 수 미보고
- source: §3.6, Fig. 9, p. 10, App. C.2–C.3, pp. 21–22, Table 13
- block: `split 42:58` 왼쪽 `figure` Fig. 9 / 오른쪽 `table` Block-wise·Full의 성능 및 비용 / 하단 배수와 측정 조건
- assets: Fig. 9 축·범례 포함, Table 13
- interaction: none
- notes: MMDiT와 비교할 때는 AF tokenizer와 DDT predictor를 맞췄고, Block-wise MoT의 GenEval 곡선이 비교 구간에서 더 높습니다. Full MoT와 비교하면 GenEval과 DPG는 Block-wise가 앞서고 WISE-Verified는 Full이 앞섭니다. 같은 생성 설정에서 측정한 denoising 비용은 Full MoT 쪽이 compute 기준 2.50배, 배치 지연 기준 3.10배입니다. 논문에는 배치 크기와 denoising step 수가 보고되지 않았습니다.

### 19. 검증 범위와 추론 비용

- section: `analysis`
- time: 60초
- message: 공유 표현의 이득이 확인된 범위는 주로 Qwen3.5의 단기 T2I 실험이며, 이를 실제 VLM에 붙일 때의 비용은 이해 추론 단계별로 다르게 나타납니다.
- on-slide facts:
  - **검증 범위** — 256²·생성 50K step·Qwen3.5 계열 conditioning 중심 / 전체 600K 일정의 tokenizer 통제 비교, 다른 계열의 conditioning VLM, 멀티턴 \(z\) 직접 재사용 효과는 미보고
  - **평가** — 20K AF ablation의 의미 지표는 학습 정렬 표적과 관련된 cosine, 해당 ablation 설정의 VLM 이해 유지율 미보고. 최종 AF는 별도로 이해 벤치마크 평가. WISE-Verified 판정 모델 Qwen3.5-35B-A3B와 Integral 백본 Qwen3.5-9B가 같은 계열(`external`).
  - **비용** — Qwen3.5-9B → +AF, 800×800 이미지 1장 및 **생성 텍스트 100토큰**. Prefill `42.6 → 54.9 ms`(+28.9%, 계산), text generation `1837 → 1865 ms`, end-to-end +2.1%(논문 보고), peak `17.7 → 19.0 GiB`(+7.3%, 논문 보고).
- source: §§2.2, 3.4–3.6, pp. 4–5, 9–10, Tables 2, 7–8, 10, App. C.3와 Table 12, pp. 21–22. `external` [WISE-Verified 평가 설정](https://github.com/PKU-YuanGroup/WISE)
- block: `groups` 3열 — 검증 범위 / 평가 / 비용
- assets: Table 12 선택 지표
- interaction: none
- notes: 50K 비교는 초기 생성 학습을 보여 주며 전체 일정을 돌렸을 때 tokenizer 간 순위가 유지되는지는 보고되지 않았습니다. 의미 감독을 건 20K 구조 비교의 cosine은 최적화 표적과 관련돼 있으므로, 실제 VLM 과제의 유지율은 최종 AF 평가를 따로 봐야 합니다. 외부 WISE-Verified 설정에서 판정 모델과 Integral 백본은 같은 Qwen3.5 계열이며, 이 관계가 점수에 미친 영향은 측정되지 않았습니다. 비용은 100토큰 생성 조건에서 text generation이 대부분을 차지해 전체 지연 증가율이 2.1%이고, prefill만 보면 28.9%입니다. 생성 답변이 더 짧은 과제에서는 prefill 비중이 커질 수 있지만 해당 지연은 별도로 측정되지 않았습니다.

### 20. 정리와 토론

- section: `discussion`
- time: 150초
- message: 저자들은 재구성 품질을 넘어 VLM과 정렬된 표현을 공유하는 데서 단기 생성 학습의 이득이 생긴다고 해석합니다.
- on-slide facts:
  - 정리 — 비슷한 최종 PSNR, 다른 50K-step GenEval / 외부 vision encoder·LLM 조건·의미 감독 비교 / 2B 적용과 아직 남은 통제 조건
  - **1. 무엇이 이득을 만드나** — `kind` 근거  
    사실 — 256² T2I 50K에서 LLM+AF ≈0.28 > VLM+FLUX.1-VAE ≈0.18(곡선 근거). AF에 VLM 조건을 넣을 때 GenEval +0.13(§3.4 보고값).  
    질문 — AF latent 자체의 이득과 VLM과의 공유에서 생기는 추가 이득을 어떻게 분리해 측정할 수 있을까요?
  - **2. 짧은 학습의 GenEval** — `kind` 근거  
    사실 — tokenizer 간 생성 통제 비교는 256² 50K step, 최종 생성 일정은 600K step(계산). GenEval 2 저자들은 GenEval이 포화됐다고 주장합니다(`external`).  
    질문 — 같은 비교를 전체 일정과 추가 지표로 반복하면, 수렴 속도의 차이와 최종 품질의 차이를 어떻게 구별할 수 있을까요?
  - **3. 측정하지 않은 효과** — `kind` 근거  
    사실 — 저자들은 다음 턴에 \(z\)를 바로 재사용하면 디코딩·재인코딩 손실을 피할 수 있다고 봅니다. 멀티턴 재사용 실험은 미보고이며, propagation bottleneck의 CKA는 상관 근거입니다.  
    질문 — 여러 턴에서 \(z\) 직접 재사용과 픽셀 경유 입력을 비교한다면, 어떤 정보의 보존을 어떻게 측정할까요?
  - **4. 백본에 맞추는 비용** — `kind` 대가(해석)  
    사실 — 생성 전용 0.89B 외에 시각 입력 경로 `456.0M → 582.1M`(+126.1M), prefill +28.9%(계산, Table 12 조건), pixel decoder 475.1M. 9B의 tokenizer 전체 일정은 650K step(계산).  
    질문 — 다른 VLM에 이 설계를 옮길 때 어떤 부분을 재사용할 수 있고, 백본에 맞춰 다시 드는 학습·추론 비용까지 포함하면 공유의 이득은 어느 조건에서 유지될까요?
- source: §§2.1–2.2, 3.4, pp. 3–5, 9, Figs. 3·6b, App. A.2, Table 7, pp. 18–19, App. C.3, Table 12, pp. 21–22. `external` [GenEval 2 초록](https://arxiv.org/abs/2512.16853)
- block: 어두운 statement / 상단 `lead` 정리 / 하단 `groups` 토론 4항목을 2열로 배치
- assets: none
- interaction: none
- notes: 저자들은 비슷한 재구성 품질에서도 AF가 더 높은 단기 생성 성능을 보인 결과를 표현 공유의 이득으로 해석합니다. 첫째, LLM+AF의 우위와 VLM을 붙였을 때 추가로 오른 점수를 각각 무엇에 귀속할 수 있을지 묻고 싶습니다. 둘째, GenEval 중심의 50K 비교를 전체 학습 일정으로 이어 가면 수렴 속도와 최종 품질을 어떻게 구분할 수 있겠습니까? 셋째, 멀티턴에서 \(z\)를 직접 재사용할 때 실제로 보존되는 정보는 무엇인지 측정할 수 있겠습니까? 마지막으로, 백본별 tokenizer 학습과 시각 입력 경로의 비용까지 포함하면 이 설계가 어떤 조건에서 유리할지 토론하고 싶습니다.

### 21. 감사합니다 · Q&A

- section: `discussion`
- time: 0초
- message: 감사합니다, 질문과 토론을 받겠습니다.
- on-slide facts: 감사합니다 · Q&A / 오희석(VILAB, 한성대학교) / [논문 arXiv:2611.31237v1](https://arxiv.org/abs/2611.31237v1) · [Integral 프로젝트](https://thejb.ai/integral) / `external` [코드](https://github.com/the-jb/integral) · [체크포인트](https://huggingface.co/the-jb/Integral-9B)
- source: p. 1의 arXiv ID·Project Page, `external` [Integral 코드 저장소](https://github.com/the-jb/integral) · [Integral-9B 모델 카드](https://huggingface.co/the-jb/Integral-9B)
- block: `lead` 중앙 정렬 / 아래에 발표자와 링크 두 줄
- assets: none
- interaction: none
- notes: 들어주셔서 감사합니다. 질문과 의견을 받겠습니다. 논문과 프로젝트, 코드, 체크포인트 링크를 화면에 띄워 두겠습니다.

## Not applied

- **C3의 일부 제안.** Fig. 5b의 블록 간격은 개념도이므로 토론에서 제외했다. App. A.1의 32층과 App. C.2의 Full MoT 31블록 표기 차이는 9장 발표 메모에 뒀다. Cosine과 RMS 정규화 MSE의 관계는 8장에서 계산으로 제시하고, 20K ablation의 독립 평가 문제는 19장에 뒀다.
- **C9의 Fig. 11 사용 제안.** 층을 제거할수록 남는 feature 수도 줄어드는 실험이라 깊이별 효과를 분리하기 어렵다. 구성요소별 효과는 17장의 Table 10으로 다룬다.