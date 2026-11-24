## Ledger

- Fig. 1 — use: 1(b)의 앵무새 비교를 표지 티저로 사용, 10에서 (a)의 FID 도달 step 비교를 캡션으로 인용.
- Fig. 2 — use: 4(a), 6(b).
- Fig. 3 — use: 7의 고양이 토큰 도식 참고, 8의 전폭 학습 흐름.
- Fig. 4 — use: 16(b). cut: (a)의 RAE 곡선은 9의 Table 1 두 행으로 압축.
- Fig. 5 — cut: 모달리티별 종료점은 10–11의 Tables 2–4에 제시.
- Fig. 6 — use: 15의 두 탭에서 (a), (b)를 각각 전폭 표시.
- Fig. 7 — cut: rollout을 투사 화면에서 판독하기 어려워 과제별 성공률을 Fig. 8(b)로 제시.
- Fig. 8 — use: 13(b). cut: (a)의 역축 radar는 12의 Table 6 기반 Δ 표로 교체.
- Fig. 9 — use: 14의 `Typography` 탭, 비교 한 쌍.
- Fig. 10 — use: 14의 `Vespa` 탭에 (a), `춤` 탭에 (b).
- Fig. 11 — use: 17(a), 18(b).
- Table 1 — use: 9, SiT-XL/2 참조 행과 RAE 두 행 포함.
- Table 2 — use: 10, FID 막대·REPA 대비 Δ·sFID 캡션.
- Table 3 — use: 11, FVD와 framewise FID.
- Table 4 — use: 11, Table 5와 통합한 오디오 표의 step과 FAD.
- 부록 Table 5 — use: 11, 방법별 trainshift·sampleshift·\(R_M\).
- 부록 Table 6 — use: 12, 다섯 가중치 조합의 세 모달리티별 Δ.
- 부록 Fig. 14 — cut: trainshift 라벨이 없어 동일 trainshift 비교에 쓸 수 없음. 20에서 근거 범위만 인용.
- 부록 Fig. 15(c, d) — cut: 18에서 App. C의 혼합 규칙과 FVD·framewise FID 변화 방향만 인용.
- 부록 Fig. 17 — cut: 1M step 조건만 12에 인용. 종료점 비교는 Table 6 사용.
- 부록 Fig. 20 — cut: (a)의 2M–4M 순위 교차와 (b)의 FLUX.2 AE 비교 방향만 9에 인용.
- 부록 Fig. 21 — cut: 층 선택 곡선은 생략. 8의 기본 층 번호는 App. H에서 인용.

## Sections

- `summary` — 요약 (2장) · 0:45
- `background` — 배경 (3–4장) · 1:50
- `method` — 방법 (5–8장) · 4:25
- `results` — 결과 (9–14장) · 6:20
- `analysis` — 분석 (15–19장) · 4:20
- `discussion` — 정리와 토론 (20–21장) · 2:00

표지 0:20 포함 **총 20:00**. 1920×1080, 2–21장 하단에 구간 진행 표시줄. 인터랙션은 6·14·15장에만 배치한다. 클리커의 다음·이전 키로 탭을 바꾸고, 마지막 탭에서 다음 키를 누르면 다음 슬라이드로 이동한다.

## Slides

### 1. Self-Flow의 표현 학습

- section: `none`
- time: 20초
- message: 오늘은 Self-Flow가 생성 모델 안에서 어떤 표현 학습 신호를 만들고, 그 효과를 어디까지 검증했는지 살펴봅니다.
- on-slide facts: 논문 원제 *Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis* · Hila Chefer, Patrick Esser 외 · Black Forest Labs / MIT · PDF 표지 날짜 2026년 3월 4일 · VILAB 논문 세미나.
- source: p. 1, 서지 정보와 Fig. 1(b).
- block: `split 40:60` · 좌 `lead` 서지 정보 · 우 `figure` 앵무새 비교 티저, 모델 라벨 유지.
- assets: Fig. 1(b) 앵무새 비교 크롭.
- interaction: none

### 2. Self-Flow의 핵심 구성

- section: `summary`
- time: 45초
- message: Self-Flow의 학습 신호는 같은 샘플에서 noise 수준을 달리한 두 입력의 표현을 맞추는 데서 나옵니다.
- on-slide facts:
  - 논문이 하는 일 — Self-Flow는 외부 표현 encoder 없이, 서로 다른 noise 수준의 두 입력을 이용해 flow matching 안에서 표현을 학습한다.
  - 기여 3개 — 토큰별로 두 timestep을 배정하는 Dual-Timestep Scheduling · 더 깨끗한 입력을 본 EMA teacher로 self-distillation · 이미지·비디오·오디오의 개별 학습과 공유 backbone 실험.
- source: Abstract p. 1, §3.3–3.4 pp. 3–4, §4.1–4.2 pp. 5–7.
- block: 어두운 `statement` · 상단 `lead` 한 문장 · 하단 `cards` 기여 3개.
- assets: none
- interaction: none

### 3. 생성 모델의 표현 정렬

- section: `background`
- time: 60초
- message: 네 방법을 비교할 때는 정렬 목표를 어느 모델에서 가져오는지와 그 목표를 만들 때 입력의 noise를 어떻게 주는지를 보면 됩니다.
- on-slide facts:
  - 연구 갈래 — 표현 사전학습의 SimCLR·DINO·MAE · 외부 표현 정렬의 REPA·DINOv2 · 내부 표현 정렬의 SRA·LayerSync · semantic latent를 사용하는 RAE.
  - 비교표 열 — 방법 / student 표현 → 정렬 목표 / teacher / 외부 정렬 모델.
    - REPA — 생성 모델 중간층 → 사전학습 encoder 특징 / 고정 DINOv2 등 / 있음.
    - SRA — noise가 더 큰 입력의 앞쪽 층 → noise가 더 작은 입력의 뒤쪽 층 / EMA teacher / 없음. 입력·층 관계는 `external` R4.
    - LayerSync — 상대적으로 약한 층 → 같은 모델의 의미 정보가 더 강한 중간층 / 자체 중간층, EMA 없음 / 없음. 정렬 대상은 `external` R5.
    - Self-Flow — 두 timestep을 섞은 student 중간층 → 모든 토큰에 더 낮은 timestep을 준 teacher의 깊은 층 / EMA teacher / 없음.
  - 마지막 줄 — **Self-Flow는 왜 작동하며, 그 설명은 어디까지 실험으로 뒷받침되는가?**
- source: §2 pp. 2–3, §3.1 Eq. (3) p. 3, §3.4 p. 4, App. A.5 p. 18. [R4 · SRA](https://arxiv.org/abs/2505.02831), [R5 · LayerSync](https://arxiv.org/abs/2510.12581)
- block: 상단 `groups` 연구 갈래 · 중앙 전폭 `table` 네 방법 · 표 아래 `equation` 공통 정렬 loss Eq. (3)의 기호 · 마지막 줄 `lead` 발표 질문.
- assets: Eq. (3), 논문 설명과 R4·R5를 바탕으로 구성한 비교표.
- interaction: none

### 4. 외부 encoder 크기와 생성 FID

- section: `background`
- time: 50초
- message: 이 REPA 실험에서는 외부 encoder의 표현 성능을 높이는 선택이 생성 FID 개선으로 이어지지 않았습니다.
- on-slide facts: class-conditional ImageNet 256×256 · SiT-XL, SD-VAE, no CFG · 200K–600K step · 같은 REPA 설정에서 DINOv2-B, DINOv2-L, DINOv3-B, DINOv3-H+ 교체 · DINOv2-B의 FID가 가장 낮고 DINOv3-H+가 가장 높음 · 고정된 외부 표현과 생성 목표의 불일치는 저자의 설명.
- source: §3.1–3.2 및 Fig. 2(a) p. 3, §4 p. 5, App. A.2–A.4 pp. 16–18.
- block: `split 68:32` · 좌 `figure` FID 학습 곡선 · 우 `compare` 두 극단의 encoder와 FID 순위.
- assets: Fig. 2(a), 축·범례 포함.
- interaction: none

### 5. Rectified Flow와 토큰 규격

- section: `method`
- time: 55초
- message: 기본 rectified flow에서는 길이와 차원이 다른 latent sequence에도 샘플마다 공통 timestep 하나를 적용합니다.
- on-slide facts:
  - \(x_0\in\mathbb R^{N\times C}\), \(x_1\sim\mathcal N(0,I)\) · \(t=0\)은 clean data, \(t=1\)은 pure noise · 선형 보간과 velocity target \(x_1-x_0\) · 기본 추론 경로 \(t=1\rightarrow0\).
  - 이미지 256×256 — 256토큰, 토큰 차원 SD-VAE 16 / FLUX.2 AE 128 / RAE 768.
  - 비디오 45프레임·192p — Wan2.2 AE, 약 3K토큰, 차원 48.
  - 오디오 10초 — Songbloom AE, 250토큰, 차원 64.
- source: §3.1 Eq. (1)–(2) p. 3, App. A.2 pp. 16–17.
- block: `split 50:50` · 좌 `equation` 보간과 flow loss · 우 `table` 모달리티별 \(N\), \(C\), AE.
- assets: Eq. (1)–(2), App. A.2의 토큰 규격.
- interaction: none

### 6. 토큰별 noise 배치 네 방식

- section: `method`
- time: 80초
- message: Fig. 2(b)에서는 토큰마다 서로 다른 timestep을 주는 규칙 가운데 두 timestep을 공유하는 방식만 vanilla보다 낮은 FID를 보였습니다.
- on-slide facts: Fig. 2(b)의 200K–600K step FID 궤적 · 같은 토큰 격자와 noise 색상 척도 · full masking과 diffusion forcing의 열화에 대한 저자의 설명은 모든 토큰에 같은 timestep을 주는 추론 조건과의 차이.
- source: §3.3 pp. 3–4, Fig. 2(b) p. 3.
- block: 대표 `toggle` · `split 46:54` · 좌 `diagram` 토큰 격자와 읽기 칸 · 우 `figure` 동일 FID 곡선에서 선택한 방법과 vanilla 강조.
- assets: Fig. 2(b), 축·범례 포함 · 네 배정 규칙을 그린 동일 규격 토큰 격자.
- interaction: `toggle` — **대표 인터랙션**. `reveals:` timestep을 몇 개 뽑고 어느 토큰이 공유하는지에 따라 Fig. 2(b)의 FID 궤적이 어떻게 달라지는지 비교.
  - `label: Vanilla` · 화면: 전 토큰에 같은 \(t\), vanilla 곡선 강조 · 읽기: “Vanilla는 샘플의 모든 토큰에 같은 timestep을 주며 Fig. 2(b)의 비교 기준입니다.” · 출처: §3.3, Fig. 2(b).
  - `label: Full masking` · 화면: 선택한 토큰 \(t=1\), 나머지 토큰 공통 \(t\) · 읽기: “일부 토큰을 pure noise로 바꾸는 full masking은 vanilla보다 FID가 악화됐습니다.” · 출처: §3.3, Fig. 2(b).
  - `label: Diffusion forcing` · 화면: 각 토큰에 독립적으로 뽑은 \(t_i\) · 읽기: “Diffusion forcing과 유사하게 토큰마다 timestep을 독립적으로 뽑는 방식도 vanilla보다 FID가 악화됐습니다.” · 출처: §3.3, Fig. 2(b).
  - `label: Dual-Timestep` · 화면: 같은 격자에 \(t\)와 \(s\) 두 색 · 읽기: “두 timestep을 토큰 사이에 나누면 representation loss를 추가하기 전에도 vanilla보다 FID가 소폭 개선됐습니다.” · 출처: §3.3, Fig. 2(b).

### 7. Dual-Timestep Scheduling

- section: `method`
- time: 55초
- message: 같은 분포에서 뽑은 두 timestep을 토큰 사이에 나누면 토큰별 주변분포를 유지하면서 한 입력 안에 noise 수준 차이를 만들 수 있습니다.
- on-slide facts: \(t,s\sim p(t)\) · \(u_i\sim U(0,1)\), \(u_i<R_M\)이면 토큰 \(i\)에 \(s\), 그 외에는 \(t\) · \(R_M\leq0.5\) · \(R_M\)은 두 번째 timestep 배정 확률 · 이미지 0.25 / 비디오 0.10 / 오디오 0.50 · student conditioning을 scalar에서 토큰별 벡터 \(\tau\in\mathbb R^N\)로 확장.
- source: §3.3 Eq. (4)–(5), Fig. 3 p. 4, App. A.3 p. 17.
- block: `split 55:45` · 좌 `diagram` Fig. 3의 고양이 예시에서 student 토큰 배정 · 우 `equation` \(\tau_i\)와 \(x_\tau\), 하단 모달리티별 \(R_M\).
- assets: Fig. 3의 고양이 예시를 단순화한 정적 토큰 도식, Eq. (4)–(5).
- interaction: none

### 8. EMA teacher와 학습 loss

- section: `method`
- time: 75초
- message: Student는 두 timestep이 섞인 입력에서 velocity를 예측하면서 더 깨끗한 입력을 본 EMA teacher의 깊은 층 표현을 맞춥니다.
- on-slide facts: teacher 전 토큰에 \(\min(t,s)\) · student 중간층의 MLP projection과 teacher 깊은 층 간 cosine 정렬 · teacher stop-gradient · EMA decay 0.9999 · \(\gamma=0.8\) · 기본 층 \(l=0.3D,\ k=0.7D\), ImageNet SiT-XL 약 675M에서 \(l=8,\ k=20\) · FLUX.2 backbone 약 625M, Self-Flow와 REPA 계열의 projection 약 10M 추가.
- source: §3.4 Fig. 3 및 Eq. (6)–(7) p. 4, App. A.3 p. 17, App. H p. 24.
- block: 상단 전폭 `figure` 두 forward·stop-gradient·EMA 화살표 · 하단 `split 62:38` · 좌 `equation` \(\mathcal L_{\rm rep}\)와 전체 loss · 우 `groups` 층과 학습 설정.
- assets: Fig. 3, Eq. (6)–(7).
- interaction: none

### 9. ImageNet 256×256 비교

- section: `results`
- time: 65초
- message: ImageNet에서 Self-Flow는 SD-VAE의 4M step 비교와 RAE의 1M step 비교에서 각각 FID를 낮췄고, 4M step의 지표별 순위는 달랐습니다.
- on-slide facts:
  - class-conditional ImageNet 256×256 · SiT-XL 약 675M · no CFG · SD-VAE 250 SDE steps · RAE plateau-logit-normal 학습, 추론 50 steps.
  - `모델 | 학습 step | FID↓ | sFID↓ | IS↑ | Precision↑ | Recall↑`
    - SD-VAE · SiT-XL/2 | 7M | 8.3 | 6.30 | 130.57 | 0.69 | 0.67
    - SD-VAE · SRA | 4M | 7.27 | 5.87 | 143.06 | 0.69 | 0.68
    - SD-VAE · REPA | 4M | 5.89 | 5.73 | 157.66 | 0.70 | 0.69
    - SD-VAE · Self-Flow | 4M | 5.70 | 4.97 | 151.40 | 0.72 | 0.67
    - RAE | 1M | 3.24 | 6.73 | 218.53 | 0.83 | 0.54
    - RAE + Self-Flow | 1M | 2.95 | 5.50 | 222.34 | 0.84 | 0.56
  - 같은 AE·step 기준 FID Δ — SD-VAE에서 REPA 대비 **−0.19**, RAE에서 RAE 기준 모델 대비 **−0.29** · SD-VAE의 REPA와 Self-Flow FID 순위는 2M–4M 사이 교차.
  - 별도 AE 확인 — FLUX.2 AE를 쓴 T2I 약 625M·no CFG, Fig. 20(b)의 200K–600K 구간에서 같은 AE의 Vanilla FM 대비 낮은 FID.
- source: §4.1 및 Table 1 p. 5, App. A.2–A.4 pp. 17–18, App. G.1–G.2 및 Fig. 20 pp. 22–24.
- block: 전폭 `table` · SD-VAE 4M 비교, 7M 참조 행, RAE 1M 비교를 구분 · 하단에 FID Δ와 두 부록 관찰을 캡션으로 표시.
- assets: Table 1의 열과 행을 유지한 재구성 표.
- interaction: none

### 10. Text-to-image 생성 지표

- section: `results`
- time: 65초
- message: 이 T2I 설정에서 Self-Flow는 DINOv2를 정렬 목표로 쓰는 REPA보다 FID와 FD-DINO가 낮았고 CLIP score는 높았습니다.
- on-slide facts:
  - 내부 T2I 20M 페어 · FLUX.2 backbone 약 625M, SD-VAE · 1M step · uniform \(p(t)\) · no CFG, 50 ODE steps, sampleshift 1.78.
  - FID↓ — Vanilla FM **4.08**, REPA–SigLIP 2 **3.97**, REPA–DINOv2 **3.92**, SRA **3.70**, Self-Flow **3.61**.
  - Self-Flow − REPA–DINOv2 — FID **−0.31** · FD-DINO **−5.37** (173.35 → 167.98) · CLIP **+0.21** (30.67 → 30.88).
  - sFID↓ 캡션 — SRA 8.05 · REPA–SigLIP 2 8.13 · Self-Flow 8.14.
  - Fig. 1(a) 캡션 — REPA의 1M step FID **3.92** 도달 기준, 논문 보고 약 **2.8×**의 학습 step 차이 · **해석:** step 비교에는 teacher forward의 연산 비용이 반영되지 않음.
- source: Fig. 1(a) p. 1, §4 및 §4.1 pp. 5–6, Table 2 p. 6, App. A.2–A.4 pp. 17–18.
- block: `split 60:40` · 좌 `bars` 1M step FID 다섯 방법 · 우 `deltas` 지표별 한 숫자씩 · 하단 sFID와 Fig. 1(a) 캡션, 비용 해석에 `note`.
- assets: Table 2의 해당 열로 재작성한 막대와 Δ, Fig. 1(a)의 도달 step 주석.
- interaction: none

### 11. 비디오와 오디오 생성 지표

- section: `results`
- time: 80초
- message: 논문이 선정한 설정에서는 Self-Flow의 비디오·오디오 지표가 모두 가장 낮았고, 외부 encoder의 결과는 지표와 encoder에 따라 달랐습니다.
- on-slide facts:
  - 공통 — FLUX.2 backbone 약 625M · no CFG · 50 ODE steps.
  - 비디오 — 내부 6M 영상, Wan2.2 AE, 45프레임·192p, 600K step, sampleshift 15.0 · 학습 timestep의 5%를 \([0.95,1.00]\) 균일분포에서 추출.
  - `비디오 모델 | FVD↓ | framewise FID↓` — Vanilla FM 50.95 / 9.28 · SRA 49.75 / 9.02 · Self-Flow **47.81 / 8.92** · REPA–DINOv2 49.59 / 9.39 · REPA–Depth Anything 3 51.52 / 9.85 · REPA–V-JEPA 2 53.55 / 9.91.
  - 비디오 Self-Flow − Vanilla FM — FVD **−3.14**, framewise FID **−0.36** · low-SNR 혼합을 빼면 Self-Flow의 framewise FID 악화.
  - 오디오 — FMA 10초 클립, 1M 학습 규모·20K 검증셋, Songbloom AE, 350K step · 공통 sampleshift 6.93.
  - `오디오 모델 | FAD(CLAP)↓ | FAD(CLAP-M)↓ | FAD(CLAP-A)↓ | trainshift` — Vanilla FM 148.874 / 0.1695 / 0.1059 / 0.75 · SRA 147.215 / 0.1664 / 0.1034 / 0.75 · Self-Flow **145.645 / 0.1634 / 0.1001 / 1.0** · REPA–MERT 148.883 / 0.1677 / 0.1040 / 0.75.
  - 오디오 설정 선정 — logit-normal trainshift 탐색 · Self-Flow \(R_M\in\{0.05,0.10,0.25,0.50\}\) 중 0.50 선정 · MERT는 Vanilla FM 대비 CLAP에서 악화, CLAP-M·CLAP-A에서 개선.
- source: §4.1 및 Tables 3–4 pp. 5–6, App. A.1–A.4 pp. 16–18, App. B 및 Table 5 p. 19, App. C 및 Fig. 15(d) pp. 19–20.
- block: `split 47:53` · 비디오와 오디오 `table` 각 하나 · 비디오 Δ와 오디오 공통 조건은 각 표 아래 캡션.
- assets: Table 3, Tables 4–5의 통합 오디오 표.
- interaction: none

### 12. 공유 backbone과 loss 가중치

- section: `results`
- time: 55초
- message: 공유 backbone 실험에서는 시험한 다섯 가중치 모두에서 Self-Flow의 이미지 FID, 비디오 FVD, 오디오 FAD가 같은 가중치의 Vanilla FM보다 낮았습니다.
- on-slide facts:
  - 약 625M, 1M step, no CFG · 모달리티별 입출력 층과 공유 backbone · T2I에 FLUX.2 AE와 전체 200M 이미지 사용 · 이미지/비디오/오디오 배치 추출 확률 57% / 30% / 13%.
  - `가중치 (이미지, 비디오, 오디오) | 이미지 ΔFID | 비디오 ΔFVD | 오디오 ΔFAD(CLAP)` · \(\Delta=\text{Self-Flow}-\text{FM}\), 표에 인쇄된 값의 차이.
    - (0.067, 0.319, 0.614) | −0.35 | −6.6 | −3.2
    - (0.105, 0.506, 0.389) | −0.26 | −3.8 | −1.2
    - (0.131, 0.628, 0.241) | **−0.16** | **−4.7** | **−2.7**
    - (0.196, 0.079, 0.725) | −0.08 | −4 | −4.8
    - (0.308, 0.123, 0.569) | −0.09 | −4.3 | −3.8
  - 강조 행의 FM → Self-Flow — 이미지 FID 3.35 → 3.19 · 비디오 FVD 62.7 → 58 · 오디오 FAD(CLAP) 160.1 → 157.4.
- source: §4.2 p. 7, App. A.1–A.3 pp. 16–17, App. D, Table 6 및 Fig. 17 pp. 20–21.
- block: 전폭 `table` 5행×3 Δ · video-weighted 행 강조 · 하단 캡션에 해당 행의 원값.
- assets: Table 6의 FID·FVD·FAD(CLAP) 열로 계산한 Δ 표.
- interaction: none

### 13. Joint Video-Action 전이

- section: `results`
- time: 55초
- message: 같은 RT-1 fine-tuning을 거친 뒤에도 Self-Flow 초기화의 이점은 두 물체를 배치하거나 동작 순서를 따라야 하는 과제에서 남았습니다.
- on-slide facts:
  - video-weighted 625M checkpoint · 동일한 RT-1 fine-tuning 73.5K episodes · SIMPLER 성공률, 30K와 100K step 비교.
  - 30K — Self-Flow가 네 과제에서 앞섬 · Vanilla FM의 `Open and Place` 성공률 0%.
  - 100K — `Pick Up Coke Can`은 비슷한 성공률로 수렴(그림 표기 73%) · `Open/Close Drawer`는 FM이 소폭 앞섬(FM 78%) · `Move Near`는 Self-Flow 50%, 격차 확대 · `Open and Place`는 Self-Flow 29%, 격차 유지.
  - 과제별 평가 — `Pick Up Coke Can` 15회 · `Open/Close Drawer` 18회 · `Move Near` 10회 · `Open and Place` 7회 · checkpoint마다 전체 과제 목록 2회 반복.
- source: §4.2 및 Fig. 8(b) p. 7, App. E pp. 21–22.
- block: 전폭 `figure` 과제별 성공률 막대 · 하단 `compare` 30K와 100K에서 달라진 과제별 순위.
- assets: Fig. 8(b), 과제명·범례·그림에 직접 표기된 성공률 유지.
- interaction: none

### 14. 생성 샘플의 정성 비교

- section: `results`
- time: 60초
- message: 논문은 글자의 판독성, 물체의 형태, 프레임 간 신체 일관성을 서로 다른 생성 예시로 보여 줍니다.
- on-slide facts: 같은 prompt 내 방법 비교 · 정성 샘플 추론 50 steps · CFG 이미지 3.5 / 비디오 5 · 예시별 모델 규모와 관찰 지점은 탭에 표시.
- source: §4 및 §4.3 pp. 5, 7–9, Figs. 9–10, App. A.3 p. 17, App. I p. 24.
- block: `toggle` · 상태마다 전폭 `figureNumbered` 하나 · 모델 라벨과 짧은 읽기 칸 유지.
- assets: Fig. 9의 첫 비교쌍, Fig. 10(a)의 파란 Vespa, Fig. 10(b)의 춤추는 여성 프레임 띠.
- interaction: `toggle` — `reveals:` 사례별로 무엇을 비교해야 하는지 글자·물체·시간 축에서 한 번씩 확인.
  - `label: Typography` · 화면: Fig. 9의 Vanilla FM/Self-Flow 한 쌍과 글자 영역 확대 · 읽기: “4B multi-modal 모델의 고해상도 100K step 설정에서 같은 문구의 철자와 판독성을 비교합니다.” · 출처: Fig. 9 p. 8, §4.3 p. 9, App. I p. 24.
  - `label: Vespa` · 화면: Vanilla·REPA·SRA·Self-Flow 네 이미지, 차체 윤곽과 세부 묘사 표시 · 읽기: “내부 20M 페어로 1M step 학습한 약 625M SD-VAE T2I 모델의 파란 Vespa 예시에서 논문은 Self-Flow의 차체 형태와 세부 묘사를 강조합니다.” · 출처: §4 p. 5, §4.3 및 Fig. 10(a) p. 9.
  - `label: 춤` · 화면: 네 방법의 춤 프레임 띠 전폭 표시, 같은 시간 열과 팔·다리 관찰 지점 표시 · 읽기: “내부 6M 영상으로 학습한 약 625M 모델의 춤 예시에서 일부 baseline 프레임의 팔다리가 사라지는 현상이 관찰됩니다.” · 출처: §4.3 및 Fig. 10(b) p. 9.

### 15. 모델 크기와 학습 FLOPs

- section: `analysis`
- time: 55초
- message: 논문의 T2I sweep에서는 모델 크기가 커질수록 Self-Flow와 REPA의 CLIP score 격차가 벌어졌습니다.
- on-slide facts: 내부 T2I 20M 페어, SD-VAE, no CFG · 290M / 420M / 625M / 1B에 대응하는 층 수 8 / 14 / 21 / 28 · step 비교는 최대 1M step · 두 상태 모두 세로축은 CLIP score.
- source: §4 p. 5, §4.1 Scaling Behavior 및 Fig. 6(a, b) p. 6, App. A.3 p. 17.
- block: `toggle` · 상태별 전폭 `figure` 한 장 · 축·범례 유지, 625M Self-Flow와 1B REPA 곡선 강조.
- assets: Fig. 6(a, b).
- interaction: `toggle` — `reveals:` 같은 T2I sweep에서 비교의 가로축을 학습 step에서 논문이 보고한 training FLOPs로 바꿔 곡선의 관계를 확인.
  - `label: Steps` · 화면: Fig. 6(a), 가로축 Training Steps · 읽기: “625M Self-Flow는 1M step에서 1B REPA보다 높은 CLIP score를 기록했습니다.” · 출처: §4.1, Fig. 6(a) p. 6.
  - `label: FLOPs` · 화면: Fig. 6(b), 가로축 Training FLOPs · 읽기: “논문에 표시된 FLOPs 축에서도 625M Self-Flow 곡선이 1B REPA보다 높은 CLIP score에 도달합니다.” · 출처: §4.1, Fig. 6(b) p. 6.

### 16. 층별 ImageNet linear probe

- section: `analysis`
- time: 45초
- message: Self-Flow의 ImageNet top-1 정확도 이점은 앞쪽과 중간층에서 관찰됐고, 뒤쪽 층에서는 순위가 뒤집혔습니다.
- on-slide facts: ImageNet, SiT-XL 약 675M, 2M step · Vanilla FM과 Self-Flow의 층별 linear probe top-1 · 측정한 4·8·12·16층에서 Self-Flow 우세 · 20·24·28층에서 Vanilla FM 우세 · 측정 대상은 이미지 클래스의 linear separability.
- source: §4.1 및 Fig. 4(b) p. 5, App. A.3 p. 17.
- block: 전폭 `figure` · 하단 `compare` 4–16층과 20–28층의 순위.
- assets: Fig. 4(b), 축·범례·층 눈금 포함.
- interaction: none

### 17. Self-Flow 구성요소 ablation

- section: `analysis`
- time: 60초
- message: 이 ImageNet ablation에서 가장 큰 FID 열화는 representation loss를 뺐을 때 나타났고, 두 timestep을 제한하거나 mask를 제거해도 성능이 떨어졌습니다.
- on-slide facts:
  - ImageNet class-to-image, SiT-XL 약 675M, no CFG · Fig. 11(a)의 학습 곡선 200K–600K step.
  - §4.4의 전체 설정 대비 FID 열화 요약 — \(\mathcal L_{\rm rep}\) 제거 시 4점 초과 · representation loss를 유지하고 mask를 제거하면 1점 초과 · 정확한 종료점 표와 두 차이의 측정 step 표기 없음.
  - \(s\)를 \(t\)보다 최대 0.2만큼 더 깨끗한 범위로 제한 — mask 제거에 가까운 열화.
  - cosine을 \(\ell_1\)로 변경 — 후반 FID 하락 정체와 전체 설정 대비 격차 확대 · feature norm 증가와 수치 불안정은 저자의 설명.
- source: §4.4 pp. 9–10, Fig. 11(a) p. 9, Eq. (6) p. 4, App. A.3 p. 17.
- block: `split 65:35` · 좌 `figure` ablation FID 궤적 · 우 `bullets` 변경 조건 네 가지와 관측 결과, 두 부등호는 일반 크기 주석.
- assets: Fig. 11(a), 축·범례 포함.
- interaction: none

### 18. Timestep 분포와 low-SNR

- section: `analysis`
- time: 55초
- message: Self-Flow의 FID 이점은 T2I의 timestep 분포와 비디오의 high-noise 구간 표본 추출에 따라 달라졌습니다.
- on-slide facts:
  - T2I — 내부 20M 페어, 약 625M, SD-VAE, no CFG, 최대 1M step · uniform과 logit-normal trainshift \(\alpha=1.78\) 비교 · uniform에서 두 방법 모두 FID 개선, Self-Flow와 REPA의 격차 확대.
  - 비디오 — Wan2.2 AE, 45프레임·192p, 약 625M, no CFG, 최대 600K step · 기본 logit-normal trainshift 2.95 · 학습 timestep의 5%를 \([0.95,1.00]\) 균일분포에서 추출해 low-SNR 구간 보강.
  - 비디오 혼합 유무 — 혼합을 빼면 Self-Flow의 framewise FID 악화 · FVD는 두 조건 모두 비교군 중 가장 낮음 · SRA의 변화는 작음 · Dual-Timestep이 샘플 전체의 SNR을 평균 쪽으로 모을 수 있다는 저자의 가설.
- source: §5 p. 10, Fig. 11(b) p. 9, App. A.2 pp. 16–17, App. B–C 및 Fig. 15(c, d) pp. 19–20.
- block: `split 57:43` · 좌 `figure` T2I 분포별 FID · 우 `compare` 비디오 low-SNR 혼합 유무와 지표별 변화 방향.
- assets: Fig. 11(b), 축·범례 포함.
- interaction: none

### 19. 한계와 검증 범위

- section: `analysis`
- time: 45초
- message: 논문의 결론을 다른 조건으로 옮길 때는 각 실험에서 공유한 대조군, 평가 지표, 데이터 범위를 구분해야 합니다.
- on-slide facts:
  - **대조군** — 공유 backbone·로봇 전이·4B typography·RAE/FLUX.2 AE 조합의 대조군은 Vanilla FM 계열. 이 설정에서 SRA·REPA와의 비교 없음.
  - **측정 범위** — scaling은 T2I의 REPA 대비 CLIP score 비교, FID와 SRA 비교 없음 · 구성요소·층 ablation과 linear probe는 ImageNet · \(\gamma\) sweep과 모달리티 간 통제된 \(R_M\) ablation 미보고, 오디오 \(R_M\)은 별도 설정 탐색.
  - **비용과 재현** — 학습에 EMA teacher forward 추가 · Fig. 6(b)의 FLOPs 산정식과 teacher/DINOv2 forward 포함 여부 미기재 · T2I·T2V 평가는 내부 데이터 · `external` R2 공식 코드는 ImageNet 256×256 추론용, 학습 스크립트 미공개.
- source: §4.1–4.4 pp. 5–10, §5 p. 10, App. A.1 p. 16, App. B p. 19, App. G–H pp. 22–24. [R2 · 공식 저장소](https://github.com/black-forest-labs/Self-Flow)
- block: 전폭 `groups` 3열 · 대조군 / 측정 범위 / 비용과 재현.
- assets: none
- interaction: none

### 20. 근거 정리와 토론

- section: `discussion`
- time: 105초
- message: 생성 결과와 ablation은 두 timestep과 self-distillation을 결합한 설정을 지지하지만, 이득이 생기는 경로와 같은 시간 예산에서의 효과는 추가 비교가 필요합니다.
- on-slide facts:
  - **정리** — 토큰별 두 timestep과 더 깨끗한 EMA teacher 목표 · 여러 생성 지표의 개선과 ImageNet 초기·중간층 probe 개선 · 분포와 평가 조건에 따른 이득 변화.
  - **근거 · timestep 통제** — App. A.3의 학습 전 공통 \(p(t)\) 설명과 App. B의 방법별 사후 선정. 세 baseline의 trainshift는 0.75, Self-Flow는 1.0이며 Fig. 14에는 trainshift 라벨이 없음. **같은 trainshift에서 세 FAD 차이는 얼마나 남는가?**
  - **근거 · 선정과 평가** — FMA 20K 검증셋에서 보고한 세 FAD의 순위 중앙값으로 설정 선정. **설정 선정과 최종 평가에 서로 다른 데이터를 쓰면 순위가 재현되는가?**
  - **근거 · 작동 기전** — ImageNet linear probe는 클래스 분리도를 측정. `external` R3에서 Jiang et al.은 다른 noise 수준의 토큰 간 attention을 차단해도 성능이 유지되거나 개선됐다고 보고. **이득은 cross-token 정보 활용과 noise 축 data augmentation에 각각 얼마나 의존하는가?**
  - **대가 · 해석** — 추가 teacher forward와 입력 길이 차이. 256×256 이미지는 256토큰, 45프레임·192p 비디오는 약 3K토큰. **각 과제에서 같은 wall-clock 예산으로 어느 정도의 FID 개선을 얻는가?**
- source: Fig. 4(b) p. 5, Fig. 11(a) p. 9, §5 p. 10, App. A.1–A.3 pp. 16–17, App. B와 Fig. 14 p. 19. [R3 · Jiang et al., *From SRA to Self-Flow*](https://arxiv.org/abs/2607.02508)
- block: 어두운 `statement` · `split 33:67` · 좌 `lead`와 takeaway 3항목 · 우 `groups` 토론 질문 4개, 비용 질문에 `note`로 해석 표시.
- assets: none
- interaction: none

### 21. 질의응답

- section: `discussion`
- time: 15초
- message: 먼저 어떤 비교가 Self-Flow의 작동 기전을 가장 잘 가려낼 수 있을지 논의해 보겠습니다.
- on-slide facts: *Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis* · Chefer, Esser 외 · `external` R1 arXiv:2603.06507, preprint v1 제출 2026년 3월 6일 · `external` R2 ImageNet 256×256 추론 코드와 `Hila/Self-Flow`의 `selfflow_imagenet256.pt` · 공식 프로젝트 페이지.
- source: 논문 p. 1. [R1 · arXiv](https://arxiv.org/abs/2603.06507), [R2 · 공식 저장소](https://github.com/black-forest-labs/Self-Flow), [프로젝트 페이지](https://bfl.ai/research/self-flow)
- block: `split 60:40` · 좌 `lead` 질의응답 · 우 `groups` 논문과 프로젝트 / 추론 코드와 체크포인트.
- assets: none
- interaction: none

## Not applied

- 수용된 지적은 모두 반영했다. C1·C10에서 기각된 19장 안팎의 축소안과 Table 6 스위처는 적용하지 않았다. 목표 구조의 21장과 정적 5행×3 Δ 표를 유지했다.
- 6장의 `toggle`은 개정 지시에서 지정한 네 방식을 각각 보여 주기 위해 일반 블록 지침의 2–3상태를 한 장에서만 초과한다.
- 공통 정렬식 Eq. (3)은 네 방법의 정렬 대상을 비교하는 3장에 배치했다. 5장의 수식은 rectified flow의 경로와 flow loss에 해당하는 Eq. (1)–(2)로 구성했다.
- 그래프에서 추정한 점수·step은 제외했다. Fig. 1(a)의 약 2.8×는 논문이 직접 보고한 배율이며, 13장의 성공률 숫자는 Fig. 8(b)에 직접 인쇄된 값이다. RAE의 sampleshift는 App. A.4와 App. G.2의 표기가 달라 단일 수치로 적지 않았다.