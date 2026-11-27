## Ledger

- Fig. 1 — use: 1(구조 도식), 14(GenEval 학습 곡선)
- Fig. 2 — use: 13(Saturn 생성, 베네치아 카니발 가면 편집)
- Fig. 3 — use: 6(Joint와 AF, 층별 CKA, 학습 곡선)
- Fig. 4 — use: 5(도식 재구성), 7(AF 구조), 8(두 출력 경로)
- Fig. 5 — use: 5(도식 재구성), 9(Full·Block-wise MoT와 timestep 조건 비교)
- Fig. 6 — use: 14·15(6a), 16(6b의 조건별 Δ)
- Fig. 7 — use: 18(백본 크기별 학습 곡선)
- Fig. 8 — use: 19(AF 융합 방식 비교)
- Fig. 9 — use: 19(Block-wise MoT와 MMDiT 비교)
- Table 1 — use: 11(재구성), 14(PSNR 비교)
- Table 2 — use: 11(이해 성능 유지율과 개별 벤치마크)
- Table 3 — use: 12(최종 모델의 이해·생성 성능)
- Table 4 — use: 12(ImgEdit-Bench Overall)
- Table 5 — use: 13(WISE-Verified, CoT 조건별 비교)
- Table 6 — use: 13(KRIS-Bench, 지식 범주별 비교)
- Fig. 10 — use: 17(의미 감독 제거 후 생성 성능)
- Table 7 — use: 10(단계별 학습 step과 해상도)
- Table 8 — use: 18(2B 이해 성능 유지율)
- Table 9 — use: 15(SigLIP2-AF 재구성·분류), 18(2B 재구성)
- Table 11 — use: 17(의미 감독 제거 후 재구성 품질)
- Table 12 — use: 20(AF의 이해 추론 비용)
- Table 13 — use: 20(Full·Block-wise MoT의 생성 성능과 추론 비용)

## Sections

- `summary`: 요약 (2장, 0:40)
- `background`: 배경 (3–5장, 2:10)
- `method`: 방법 (6–10장, 4:40)
- `results`: 결과 (11–13장, 2:50)
- `analysis`: 분석 (14–20장, 7:40)
- `discussion`: 정리와 토론 (21–22장, 1:40)

1920×1080 HTML 덱 기준. 표지 0:20을 포함해 20분으로 배분한다. 21장에서 토론 질문을 소개하고, 22장 이후 토론을 진행한다. 구간은 하단 진행 표시줄에 표시한다.

## Slides

### 1. Integral의 공유 시각 표현

- section: none
- message: 오늘은 Integral의 통제 실험을 따라가며 이해와 생성에 같은 시각 토큰을 쓰는 효과를 살펴보겠습니다.
- on-slide facts: 원제 *Let Vision-Language Models Generate Images through Their Representations* / JB Kim 외 / NAVER Cloud·KAIST / VILAB 논문 세미나 / 발표자 `[이름]`
- source: p. 1, 제목·저자·소속, Fig. 1
- block: `split 48:52` 왼쪽 `lead`와 발표 정보 / 오른쪽 `figure`
- assets: Fig. 1의 Integral 구조 도식 크롭
- interaction: none

### 2. Integral 한눈에 보기

- section: `summary`
- message: Integral은 사전학습 VLM을 동결한 채 이해와 생성이 같은 시각 토큰 \(z\)를 쓰도록 확장합니다.
- on-slide facts: 한 문장 요지 — 동결 VLM을 공유 시각 토큰 기반의 이미지 생성 모델로 확장. 기여 3개 — AF의 계층 특징 융합과 이해·재구성용 \(z\) / Block-wise MoT의 경계별 조건 주입과 생성 전용 0.89B 파라미터 / AF·분리형 tokenizer의 50K-step 생성 통제 비교
- source: Abstract, §1 Contributions, pp. 1–3, §§2.2–2.3, §3.4
- block: 어두운 statement 레이아웃 / `lead` 한 문장 요지 / `groups` 기여 3열
- assets: none
- interaction: none

### 3. 통합 멀티모달 모델의 갈래

- section: `background`
- message: 기존 통합 모델은 이해와 생성을 한 시스템에 두되 계산 경로와 시각 표현을 서로 다른 방식으로 공유합니다.
- on-slide facts: 이산 토큰과 autoregressive 통합 — Chameleon, Emu3 / 연속 표현과 diffusion·flow 결합 — Transfusion, Show-o2 / 이해·생성 경로 분리 또는 특화 — Janus의 인코더 분리, BAGEL의 MoT, MetaQuery의 사전학습 VLM 연결. 화면 마지막 줄의 발표 질문 — 이해와 생성이 같은 시각 표현을 쓰면 재구성 품질이 비슷한 조건에서 생성 학습은 어떻게 달라지는가?
- source: §4, pp. 10–11, §3.2 Baselines, p. 7
- block: `groups` 3열 / 하단 `callout` 발표 질문
- assets: none
- interaction: none

### 4. 시각 이해와 재구성의 간극

- section: `background`
- message: 논문이 다루는 문제는 VLM의 이해에 필요한 의미 정보와 이미지 재구성에 필요한 세부 정보를 같은 토큰에 담는 것입니다.
- on-slide facts: 사전학습 vision encoder의 고수준 특징 / pixel reconstruction에 필요한 세부 정보 / FLUX.1-VAE처럼 생성 latent를 별도로 두는 설계 / 최종 encoder 표현을 재구성에 맞춰 공동 학습할 때 관측된 의미 보존과 재구성의 trade-off
- source: §1, pp. 1–3, §2.1, pp. 3–4, Fig. 3c
- block: `split 55:45` 왼쪽 `compare` 이해용 표현과 재구성용 latent / 오른쪽 `bullets` 공동 학습에서 맞춰야 하는 조건
- assets: 두 표현 경로의 개념 카드
- interaction: none

### 5. Integral의 정보 흐름

- section: `background`
- message: 입력 이미지를 표현하는 토큰과 생성되는 이미지 토큰이 같은 AF 공간에 놓이고, VLM의 조건 정보는 블록 경계에서 생성 경로로 전달됩니다.
- on-slide facts: 입력 이미지 \(x\), 동결 vision encoder, AF, \(z\), semantic projector, 동결 VLM, 경계 K/V, noisy latent \(z_t\), Block-wise MoT·DDT, pixel decoder, 출력 이미지
- source: Fig. 1, p. 1, §2.2, pp. 4–5, Fig. 4, Eq. (2), §2.3, pp. 5–6, Fig. 5b, Eqs. (4)–(5)
- block: `animation` 전체 폭 SVG 도식 / 입력·이해 경로는 위, 생성 경로는 아래
- assets: Fig. 1·4·5b를 바탕으로 다시 그린 SVG 한 장
- interaction: animation — 대표 인터랙션 — reveals: 이해 경로가 소비하는 \(z\)와 생성 경로가 모델링하는 토큰의 공간이 같고, 두 경로 사이에서 전달되는 값은 VLM 경계의 K/V임을 화살표로 확인 ; states/beats: 시작 화면은 노드 배치만 표시. 클리커 한 번마다 아래 연결 하나를 추가하고, 마지막 상태 다음 입력에 6장으로 이동.
  1. 동결 encoder의 여러 깊이에서 나온 특징이 AF에 모여 \(z\)로 합쳐짐 — §2.2, Fig. 4, Eq. (1), p. 4.
  2. \(z\)가 semantic projector를 거쳐 VLM의 시각 입력으로 들어감 — §2.2, Eq. (2), pp. 4–5.
  3. VLM 블록 경계에서 생성 블록으로 K/V 화살표가 연결됨 — §2.3, Fig. 5b, Eq. (4), pp. 5–6.
  4. 생성 경로에서 \(z_t\)가 DDT의 velocity 예측을 따라 생성 토큰으로 이동함 — §2.3, Eq. (5)와 flow matching, p. 6.
  5. 생성 토큰이 pixel decoder를 지나 이미지로 나타남 — §2.2, Fig. 4, Eq. (2), pp. 4–5.

### 6. Propagation bottleneck 가설

- section: `method`
- message: 저자들은 공동 학습에서 깊은 층이 초기층과 더 비슷해지는 관측이 propagation bottleneck 가설과 일치한다고 해석합니다.
- on-slide facts: 가설 — 최종층으로 재구성할 때 초기층의 세부 정보를 깊은 층까지 유지해야 해 추상화가 제약될 수 있음 / Fig. 3b 관측 — Joint에서 초기층 대비 깊은 층의 CKA 상승, 의미 감독 강화 시 상승 폭 감소 / Fig. 3c 관측 — 최대 20K tokenizer step에서 강한 의미 감독을 둔 Joint의 PSNR 저하, AF의 semantic cosine은 Frozen에 근접
- source: §2.1, pp. 3–4, Fig. 3a–c
- block: `split 40:60` 왼쪽 `figureNumbered` Joint·AF 도식과 가설 표시 / 오른쪽 `figure` CKA 및 학습 곡선, 축·범례 유지
- assets: Fig. 3a–c 크롭
- interaction: none

### 7. Abstraction Fusion의 토큰 구성

- section: `method`
- message: AF는 같은 공간 위치에서 encoder의 여러 깊이에 걸친 표현을 모아 하나의 시각 토큰으로 압축합니다.
- on-slide facts: 동결 Qwen3.5-9B vision encoder 27블록, patch size \(16\times16\), \(d_h=1152\) / patch embedding 포함 표현 28개 / 고정 층별 정규화 통계는 ImageNet 학습 이미지 50K장으로 산출 / 연속한 표현 4개씩 projection해 위치당 feature 7개 / 층 방향 16-head self-attention과 linear pooler로 \(d_f=1152\) / diagonal Gaussian bottleneck으로 \(d_z=256\), 학습 시 샘플링·추론 시 posterior mean
- source: §2.2, p. 4, Fig. 4, Eq. (1), 부록 A.1, p. 18
- block: `split 40:60` 왼쪽 `figure` AF 크롭 / 오른쪽 `process` 28개 표현 → 7개 feature → attention·pooling → \(z\)
- assets: Fig. 4의 AF 내부 크롭, 차원과 위치 인덱스를 붙인 흐름도
- interaction: none

### 8. AF의 두 출력과 학습 목표

- section: `method`
- message: AF의 같은 \(z\)에는 VLM의 기존 시각 embedding을 맞추는 손실과 픽셀을 복원하는 손실이 함께 걸립니다.
- on-slide facts: semantic projector — \(2\times2\) 토큰 병합, MLP 출력 \(d_s=4096\), 감독 표적은 기존 VLM 시각 embedding \(s\) / pixel decoder — RAE ViT-XL, 28층, 폭 1152 / \(\mathcal L_{\mathrm{AF}}=\mathcal L_{\mathrm{rec}}+\lambda_{\mathrm{sem}}\mathcal L_{\mathrm{sem}}+\beta_{\mathrm{KL}}\mathcal L_{\mathrm{KL}}\) / \(\mathcal L_{\mathrm{rec}}=\ell_1+\mathrm{LPIPS}\), KL 표적은 표준 Gaussian / Eq. (6)의 원본 MSE와 토큰별 RMS 정규화 MSE 혼합, \(r=0.3\), \(\lambda_{\mathrm{sem}}=5.0\), \(\beta_{\mathrm{KL}}=10^{-6}\)
- source: §2.2, pp. 4–5, Fig. 4, Eqs. (2)–(3), 부록 A.1–A.2, p. 18, Eq. (6)
- block: `split 43:57` 왼쪽 `diagram` \(z\)에서 갈라지는 두 출력 / 오른쪽 `equation` Eqs. (3), (6)과 기호 설명
- assets: Fig. 4의 두 decoder 경로를 단순화한 SVG, Eqs. (3), (6) LaTeX
- interaction: none

### 9. Block-wise MoT의 조건 전달

- section: `method`
- message: Block-wise MoT는 생성 스트림의 query가 블록 경계에서 두 스트림의 K/V를 참조하도록 설계합니다.
- on-slide facts: Qwen3.5-9B language backbone 32층, 4층 간격으로 generation block 8개 / \(z_t\)는 2층 MLP를 통해 생성 스트림에만 입력 / attention QKV 차원은 VLM에 맞추고 나머지 연산 폭은 \(d_g=2048\) / 블록마다 adaLN-single로 timestep 주입 / DDT head 2블록, 폭 3072, velocity 예측 / 생성 전용 0.89B 파라미터 / Fig. 5d의 최대 50K-step 비교에서 adaLN-single의 GenEval이 입력 timestep embedding보다 높음
- source: §2.3, pp. 5–6, Fig. 5a–b·d, Eqs. (4)–(5), §3, p. 6, 부록 A.1, p. 18
- block: `split 52:48` 왼쪽 `figureNumbered` Full·Block-wise MoT 배선 / 오른쪽 `groups` 블록·head 규격과 `figure` timestep ablation 크롭
- assets: Fig. 5a–b·d, Eq. (4)의 Q/K/V 배선 표기
- interaction: none

### 10. Integral의 학습 단계

- section: `method`
- message: Integral은 먼저 AF 토큰 공간을 학습하고, 그 공간을 고정한 뒤 이미지 생성과 편집을 단계적으로 학습합니다.
- on-slide facts: Qwen3.5-9B VLM 동결 / tokenizer — 256² AF 200K → 256–512 dynamic-resolution 400K → 256²에서 pixel decoder만 adversarial fine-tuning 50K / generation — 256² text-to-image 200K → 최대 512² interleaved pretraining 50K → 최대 512² interleaved SFT 350K / SFT 과제는 생성·편집·multi-reference·interleaved reasoning / 생성 표적은 표준화한 AF posterior mean, flow matching 표적 velocity는 \(\epsilon-z\), logit-normal timestep의 time shift는 4.0
- source: §2.3, p. 6, §3.1, p. 6, 부록 A.2, pp. 18–19, Table 7
- block: `split 50:50` tokenizer와 generation의 `process` 각 3단계 / 하단 `equation` \(z_t=(1-t)z+t\epsilon\)
- assets: Table 7의 Training steps·Resolution 행, §2.3의 noisy latent 식
- interaction: none

### 11. AF의 재구성과 이해 평가

- section: `results`
- message: Qwen3.5-9B에 적용한 AF는 ImageNet 재구성 품질과 사전학습 모델의 이해 성능을 함께 유지할 수 있는 토큰을 제공합니다.
- on-slide facts: ImageNet-1k 256² 재구성, 순서 rFID↓ / PSNR↑(dB) / SSIM↑ — Qwen3.5-9B+AF `0.15 / 32.2 / 0.942`, FLUX.1-VAE `0.17 / 31.1 / —`, PS-VAE `0.20 / 28.8 / 0.817`, VA-VAE `0.28 / 28.0 / 0.790` / Qwen3.5-9B 대비 AF 적용 후 20개 이해 벤치마크 평균 유지율 99.8% / 개별 점수 변화 — POPE 0.0, MMB −0.9, MMMU +0.3, OCRBench −0.8
- source: §2.2, pp. 4–5, Tables 1–2, 부록 B.1, pp. 19–20
- block: `split 58:42` 왼쪽 `table` 재구성 지표 3개 / 오른쪽 `lead` 평균 유지율과 `deltas` MMB·MMMU·OCRBench
- assets: Tables 1–2의 선택 행·열
- interaction: none

### 12. 이해·생성과 이미지 편집

- section: `results`
- message: 최종 Integral은 Qwen3.5-9B에 가까운 이해 점수를 유지하면서 조합적 생성과 일반 이미지 편집에서 비교 모델들과 경쟁합니다.
- on-slide facts: Table 3 선택 열 Params / MMMU / OCRBench / GenEval / GenEval++ / DPG — Qwen3.5-9B `9B / 73.2 / 88.1 / — / — / —`, Integral `9.8B / 73.5 / 87.3 / 0.88 / 0.743 / 84.76`, BAGEL `14B / 55.3 / 73.3 / 0.82 / 0.371 / —`, TUNA-2 `12B / 50.7 / 79.7 / 0.87 / — / 86.54` / ImgEdit-Bench Overall, GPT-4.1 평가 — Integral 3.50, BAGEL 3.20, OmniGen2 3.43, GPT-4o 4.20
- source: §3.2, pp. 6–8, Tables 3–4
- block: `split 66:34` 왼쪽 `table` 이해·생성 지표 / 오른쪽 `bars` ImgEdit-Bench Overall 4모델
- assets: Tables 3–4의 선택 행·열
- interaction: none

### 13. 세계 지식이 필요한 생성과 편집

- section: `results`
- message: Integral은 지식이 필요한 생성·편집 평가에서 BAGEL보다 높은 점수를 얻었고, WISE-Verified에서는 CoT를 추가했을 때 점수가 더 높았습니다.
- on-slide facts: WISE-Verified Overall, 직접 생성 / 명시적 CoT — Integral 9.8B `0.5560 / 0.7877`(Δ +0.2317), BAGEL 14B `0.3520 / 0.6280` / 직접 생성 비교의 FLUX.2-dev 56B `0.5650` / KRIS-Bench, GPT-4o 평가, 순서 Factual / Conceptual / Procedural / Overall — Integral `65.35 / 59.27 / 56.58 / 60.79`, BAGEL `60.26 / 55.86 / 51.55 / 56.40`(Overall Δ +4.39) / Fig. 2 예시 — 고리로 알려진 행성을 Saturn으로 구체화, 편집 지시의 베네치아 카니발 가면을 교체 대상으로 구체화
- source: §3.3, pp. 8–9, Tables 5–6, Fig. 2, p. 2
- block: `split 44:56` 왼쪽 `figureNumbered` 생성 1건과 편집 전후 1건 / 오른쪽 `table` WISE-Verified 조건별 비교와 KRIS-Bench 범주별 비교
- assets: Fig. 2의 Saturn 및 Venetian Carnival 크롭, Tables 5–6의 선택 행·열
- interaction: none

### 14. AF와 FLUX.1-VAE 비교

- section: `analysis`
- message: 같은 VLM 조건과 생성 학습 설정에서 PSNR 차이가 1.1 dB인 두 tokenizer의 50K-step GenEval은 0.23 차이가 났습니다.
- on-slide facts: Qwen3.5-9B VLM conditioning, 생성 아키텍처·학습 설정 동일 / ImageNet-1k 256² PSNR — AF 32.2 dB, FLUX.1-VAE 31.1 dB(Δ +1.1 dB) / 50K-step text-to-image GenEval — AF 0.41, FLUX.1-VAE 0.18(Δ +0.23) / 저자 해석 — 비슷한 PSNR에서 관측된 격차는 표현 공유의 생성 학습 이득을 시사
- source: Fig. 1, p. 1, Table 1, p. 4, §3.4, p. 9, Fig. 6a
- block: `split 60:40` 왼쪽 `figure` Fig. 1의 GenEval 학습 곡선 / 오른쪽 `deltas` PSNR과 GenEval을 지표별로 표시 / `note` 저자 해석
- assets: Fig. 1 우측 그래프 크롭, Fig. 6a 및 Table 1의 비교값
- interaction: none

### 15. 외부 인코더 SigLIP2-AF

- section: `analysis`
- message: 같은 AF 구조를 외부 의미 인코더에 적용해도, 이 비교에서는 조건을 주는 Qwen VLM의 자체 인코더를 쓴 AF가 더 높은 GenEval에 도달했습니다.
- on-slide facts: Qwen3.5-9B VLM conditioning과 생성 설정 동일, 두 tokenizer에 같은 AF 아키텍처 적용 / 50K-step text-to-image GenEval — Qwen AF 0.41, SigLIP2-AF 0.31(Δ +0.10) / ImageNet 256² PSNR — Qwen AF 32.20 dB, SigLIP2-AF 34.08 dB / SigLIP2 ImageNet zero-shot accuracy — AF 적용 전후 0.83 / 비교와 함께 바뀐 요소 — vision encoder
- source: §3.4, p. 9, Fig. 6a, 부록 B.2, p. 20, Table 9
- block: `split 60:40` 왼쪽 `figure` Fig. 6a 전체 곡선에서 두 AF 계열에 표시 / 오른쪽 `deltas` GenEval 차이와 `compare` 두 tokenizer의 재구성 조건
- assets: Fig. 6a 크롭, Table 9의 Qwen3.5-9B·SigLIP2 행
- interaction: none

### 16. VLM과 LLM 조건 비교

- section: `analysis`
- message: text-only LLM 조건을 VLM 조건으로 바꿨을 때 GenEval 상승 폭은 FLUX.1-VAE보다 AF에서 컸습니다.
- on-slide facts: Qwen3.5-9B 설정, 50K-step text-to-image 통제 비교 / 동일 tokenizer 안에서 \(\Delta=\mathrm{GenEval}_{\mathrm{VLM}}-\mathrm{GenEval}_{\mathrm{LLM}}\) / AF +0.13, FLUX.1-VAE +0.01 / 저자 해석 — AF가 사전학습 VLM의 조건 정보를 생성에 더 잘 활용했을 가능성
- source: §3.4, p. 9, Fig. 6b
- block: `split 47:53` 왼쪽 `compare` 두 conditioning 경로, tokenizer별 비교 기준 표시 / 오른쪽 `deltas` tokenizer별 GenEval 상승 폭 / `note` 저자 해석
- assets: Fig. 6b에서 본문이 보고한 두 Δ를 옮긴 수치 블록
- interaction: none

### 17. AF의 의미 감독 제거

- section: `analysis`
- message: 같은 AF 구조에서 의미 감독을 제거하면 재구성 점수는 좋아지지만 동일한 단기 생성 학습의 세 지표는 낮아집니다.
- on-slide facts: Qwen3.5-9B AF tokenizer 구조와 기타 학습 설정 유지, semantic alignment objective 제거 / Table 11 재구성 — AF → AF w/o sem.에서 PSNR 32.2 → 33.7 dB(Δ +1.5 dB), rFID 0.15 → 0.13(Δ −0.02) / 50K-step text-to-image 학습 곡선에서 AF w/o sem.의 GenEval·DPG-Bench·WISE-Verified가 AF보다 낮음
- source: 부록 C.1, pp. 20–21, Table 11, Fig. 10a–c
- block: `split 30:70` 왼쪽 `table` PSNR·rFID / 오른쪽 `figure` 생성 지표 곡선 3개, 축·범례 유지
- assets: Table 11, Fig. 10a–c
- interaction: none

### 18. Qwen3.5-2B의 공유 표현

- section: `analysis`
- message: 2B 백본의 AF는 같은 50K-step 예산에서 9B FLUX.1-VAE 기준을 앞섰고, 9B AF보다는 낮았습니다.
- on-slide facts: 50K-step text-to-image GenEval — AF 2B 0.26, FLUX.1-VAE 9B 0.18(Δ +0.08), AF 9B 0.41(AF 2B 대비 +0.15) / Qwen3.5-2B+AF의 ImageNet 256² PSNR 32.33 dB, 해당 2B 백본 대비 이해 벤치마크 20개 평균 유지율 99.2% / Fig. 7에서 보고된 조합은 AF 2B, AF 9B, FLUX.1-VAE 9B
- source: §§3.4–3.5, pp. 9–10, Fig. 7, 부록 B.1–B.2, pp. 19–20, Tables 8–9
- block: `split 60:40` 왼쪽 `figure` Fig. 7 / 오른쪽 `deltas` 두 GenEval 간격과 `bullets` 2B 적용 조건
- assets: Fig. 7 크롭, Tables 8–9의 2B 행
- interaction: none

### 19. AF와 MoT의 구성 비교

- section: `analysis`
- message: 표현을 공유하는 설정에서도 특징 융합 방식과 VLM 조건을 받는 구조에 따라 결과가 달라졌습니다.
- on-slide facts: 20K-step tokenizer 비교 — AF가 MLS보다 PSNR +6.27 dB, semantic cosine은 Frozen에 근접, attention pooling 곡선도 함께 표시 / 50K-step text-to-image 비교 — 동일 AF tokenizer·DDT predictor·학습 설정에서 Block-wise MoT가 MMDiT보다 높은 GenEval 곡선 / 생성 전용 파라미터 891M 대 962M(Δ −71M)
- source: §3.6, p. 10, Figs. 8–9
- block: `split 55:45` 왼쪽 `figure` Fig. 8의 PSNR·cosine과 PSNR Δ / 오른쪽 `figure` Fig. 9와 파라미터 Δ
- assets: Figs. 8–9 크롭, 각 그래프의 축·범례
- interaction: none

### 20. 검증 범위와 추론 비용

- section: `analysis`
- message: 공유 표현의 이득을 적용할 때는 단기 통제 비교가 다룬 범위와 이해·생성 경로의 추론 비용을 함께 봐야 합니다.
- on-slide facts: 공유 효과의 생성 통제 비교 — 주로 50K-step text-to-image, Qwen3.5 계열 / AF 이해 추론, 9B·800×800 이미지 1장·텍스트 100토큰 — prefill 42.6 → 54.9 ms, end-to-end latency +2.1%, peak 17.7 → 19.0 GiB / 같은 AF, 50K-step 생성에서 Block-wise 8블록 vs Full 31블록 — GenEval `0.41 / 0.39`, WISE-Verified `0.39 / 0.41`, denoising latency/batch `858 / 2659 ms`, compute `387.6 / 970.7 TFLOPs` / 적용 범위 — 최종 학습 일정까지 이어진 tokenizer 간 통제 비교와 Qwen3.5 밖의 conditioning VLM 검증은 미보고
- source: §§3.1, 3.4–3.6, pp. 6, 9–10, 부록 C.2–C.3, pp. 21–22, Tables 12–13
- block: `split 42:58` 왼쪽 `table` AF 이해 추론 비용 / 오른쪽 `table` MoT 생성 품질과 비용 / 하단 `callout` 통제 비교 범위
- assets: Tables 12–13의 선택 지표
- interaction: none

### 21. 정리와 토론

- section: `discussion`
- message: 이 논문의 근거는 재구성 PSNR 외에도 토큰이 조건 VLM의 표현과 어떻게 정렬되는지가 단기 생성 학습에 중요하다는 해석을 뒷받침합니다.
- on-slide facts: 정리 — 비슷한 PSNR의 AF·FLUX 비교 / 외부 인코더·조건 경로·의미 감독 통제 / 50K-step 및 Qwen3.5 계열의 검증 범위. 토론 포인트 4개
  1. **근거 · latent 통제** — SigLIP2-AF 비교에서 encoder도 바뀐다. 같은 encoder에서 VLM 정렬만 조절하고 latent 분포와 PSNR을 맞추면 GenEval 격차가 얼마나 남을까? [§3.4, Fig. 6a, Table 9]
  2. **근거 · 의미 지표** — semantic alignment로 학습한 뒤 cosine으로 보존을 평가한다. 본문은 cosine distance, 부록은 RMS 정규화 MSE로 기술한다. 두 표현의 관계와 손실 스케일을 확인하면 어떤 독립적인 평가가 더 필요할까? [§2.2, Fig. 3c, 부록 A.2, Eq. (6)]
  3. **근거 · 규모와 학습량** — 2B×FLUX.1-VAE를 추가하고 전체 생성 학습 일정까지 맞추면 백본 크기별 공유 이득은 어떻게 달라질까? [§§3.1, 3.4–3.5, Fig. 7, Table 7]
  4. **대가 · 해석** — AF는 특정 VLM의 층별 특징과 시각 입력 차원에 맞춘다. 백본 교체 때 AF와 projector를 다시 맞추는 비용을 포함하면 생성 학습의 이득은 어느 정도 활용 규모에서 회수될까? [부록 A.1–A.2, Table 7]
- source: §§2.2, 3.1, 3.4–3.5, pp. 4–6, 9–10, Figs. 3c, 6–7, 부록 A.1–A.2, pp. 18–19, Eq. (6), Tables 7, 9
- block: 어두운 statement 레이아웃 / 상단 `lead` 정리 / 하단 `groups` 토론 질문 2열
- assets: none
- interaction: none

### 22. 감사합니다 · Q&A

- section: `discussion`
- message: 감사합니다, 이제 질문과 토론을 받겠습니다.
- on-slide facts: 감사합니다 · Q&A / 발표자 `[이름]` · VILAB / [논문 arXiv:2611.31237v1](https://arxiv.org/abs/2611.31237v1) / [Integral 프로젝트](https://thejb.ai/integral)
- source: p. 1, arXiv ID와 Project Page
- block: `lead` 중앙 정렬 / 아래에 발표자와 링크 두 줄
- assets: none
- interaction: none