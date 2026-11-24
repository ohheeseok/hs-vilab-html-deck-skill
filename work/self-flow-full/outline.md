## Ledger

- Fig. 1 — use: 1. 대표 그림은 앵무새, `LOVE` 손톱, 팔굽혀펴기 프레임이 있는 (b). (a)의 약 2.8× 수렴 수치는 비교 기준 FID를 제공된 텍스트에서 특정하기 어려워 생략.
- Fig. 2 — use: 4(a), 6(b).
- Fig. 3 — use: 7의 토큰 도식 참고, 8의 원본 학습 흐름.
- Fig. 4 — use: 16(a), 18(b).
- Fig. 5 — use: 10(b). (a), (c), (d)는 10–12장의 종료점 비교로 압축.
- Fig. 6 — use: 17(a, b).
- Fig. 7 — use: 14. `Move Near`와 서랍에 사과를 넣는 rollout.
- Fig. 8 — use: 13(a), 14(b).
- Fig. 9 — use: 15. 4B mixed-modality 모델의 typography 비교 한 쌍.
- Fig. 10 — use: 15. (a)의 Vespa와 (b)의 춤추는 여성.
- Fig. 11 — use: 19(a), 20(b).
- Table 1 — use: 9의 4M step 비교, 16의 RAE 비교.
- Table 2 — use: 10. FID 막대그래프와 보조 지표.
- Table 3 — use: 11. FVD와 framewise FID.
- Table 4 — use: 12. 세 CLAP 기반 FAD.
- 부록 Table 5 — use: 12, 21. 방법별 오디오 설정과 선정 기준.
- 부록 Table 6 — use: 13. 같은 loss weight에서의 모달리티별 Δ.
- 부록 Fig. 20 — use: 9(a), 16(b).
- 부록 Fig. 21 — use: 8. ImageNet의 student·teacher 기본 층 번호 출처.

## Sections

- `summary` — 요약 (2장) · 0:50
- `background` — 배경 (3–4장) · 1:50
- `method` — 방법 (5–8장) · 4:30
- `results` — 결과 (9–16장) · 6:45
- `analysis` — 분석 (17–20장) · 4:40
- `discussion` — 정리와 토론 (21–22장) · 1:05

표지 0:20을 포함해 총 20:00. 1920×1080 기준으로 2–22장 하단에 구간 진행 표시줄을 둔다.

## Slides

### 1. Self-Flow의 표현 학습

- section: `none`
- message: 오늘은 Self-Flow가 생성 모델 안에서 표현을 어떻게 학습시키고 그 효과를 어디까지 검증했는지 살펴봅니다.
- on-slide facts: 논문 원제 · Hila Chefer, Patrick Esser 외 · Black Forest Labs / MIT · 2026년 3월 4일 preprint · VILAB 논문 세미나. 대표 크롭의 관찰 지점은 앵무새의 형태, 손톱의 `LOVE` 철자, 팔굽혀펴기 프레임 간 자세.
- source: p. 1 제목·저자·Fig. 1(b), §1 p. 2
- block: `split 36:64` · 좌 `lead` 발표명과 서지 정보 · 우 `figureNumbered` 대표 비교, `Time`과 모델 라벨 유지
- assets: Fig. 1(b)
- interaction: none

### 2. Self-Flow 한눈에 보기

- section: `summary`
- message: Self-Flow의 핵심은 입력의 noise 차이를 이용해 flow loss와 함께 쓸 표현 학습 신호를 만드는 데 있습니다.
- on-slide facts: **논문이 하는 일** — Self-Flow는 같은 샘플의 mixed-noise 입력과 더 깨끗한 입력을 이용해 flow matching 안에서 표현을 학습한다. **기여 3개** — 두 timestep의 토큰별 배정 · EMA teacher 표현에 대한 self-distillation · 이미지·비디오·오디오와 공유 backbone 실험.
- source: Abstract p. 1, §3.3–3.4 pp. 3–4, §4 pp. 5–7
- block: 어두운 `statement` · `split 58:42` · 좌 `lead` 논문이 하는 일 · 우 `cards` 기여 3개
- assets: none
- interaction: none

### 3. 생성 모델의 표현 학습 계보

- section: `background`
- message: Self-Flow는 표현 사전학습에서 쓰인 masking과 teacher 학습을 생성 모델의 내부 정렬 문제에 가져옵니다.
- on-slide facts: **표현 사전학습** — SimCLR의 view 정렬, DINO의 momentum teacher, MAE의 masked reconstruction. **외부 표현 활용** — REPA의 DINOv2 feature 정렬, RAE의 semantic latent. **내부 표현 정렬** — SRA와 LayerSync의 층간 feature 정렬.  
  **발표 질문** — flow matching 안에서 표현을 어떻게 강화하고, 그 효과를 무엇으로 검증할 수 있는가?
- source: §2 pp. 2–3, §3.1 p. 3, App. A.5 p. 18
- block: `split 72:28` · 좌 `groups` 연구 갈래 3개 · 우 `cards` 대표 모델의 역할 · 하단 `lead` 발표 질문
- assets: none
- interaction: none

### 4. 외부 encoder 선택의 공백

- section: `background`
- message: REPA에서 더 강한 외부 encoder가 더 낮은 생성 FID를 보장하지 않았다는 관찰이 논문의 출발점입니다.
- on-slide facts: Fig. 2(a)의 200K–600K step 구간 · 동일한 REPA 방식에서 DINOv2-B, DINOv2-L, DINOv3-B, DINOv3-H+ 교체 · DINOv2-B의 FID가 가장 낮고 DINOv3-H+가 가장 높음 · 생성 목표와 고정 teacher 표현 간 불일치는 저자의 설명.
- source: §1 pp. 1–2, §3.2 및 Fig. 2(a) p. 3
- block: `split 65:35` · 좌 `figure` FID 학습 곡선 · 우 `compare` 가장 낮은 FID와 가장 높은 FID의 encoder
- assets: Fig. 2(a), 축·범례 포함
- interaction: none

### 5. Rectified Flow의 학습 경로

- section: `method`
- message: 기본 rectified flow는 같은 timestep을 모든 토큰에 적용한 뒤 noise와 clean sample 사이의 velocity를 맞춥니다.
- on-slide facts: \(x_0\)는 clean token sequence, \(x_1\sim\mathcal N(0,I)\)는 noise · \(t=0\)은 데이터, \(t=1\)은 noise · velocity target \(x_1-x_0\) · 추론은 \(t=1\)에서 \(t=0\)으로 ODE 적분.
- source: §3.1 p. 3, Eq. (1)–(2)
- block: `split 60:40` · 좌 `equation` 보간 경로와 flow loss · 우 `process` noise 부여 → velocity 예측 → 역방향 ODE 샘플링
- assets: Eq. (1)–(2), 기호 범례
- interaction: none

### 6. 토큰별 noise 배치 방식

- section: `method`
- message: 논문의 scheduler 비교에서는 토큰을 완전히 가리거나 timestep을 제각각 뽑는 방식보다 두 timestep을 공유하는 방식의 FID가 낮았습니다.
- on-slide facts: Fig. 2(b)의 200K–600K step 학습 궤적 · vanilla의 공통 \(t\), full masking의 일부 토큰 \(t=1\), diffusion forcing 방식의 토큰별 독립 timestep, Dual-Timestep의 두 시점 공유 · Dual-Timestep만 적용한 vanilla 학습에서도 소폭 개선 · full masking과 diffusion forcing의 열화에 대한 저자 설명은 균일 noise 추론과의 차이.
- source: §3.3 pp. 3–4, Fig. 2(b)
- block: `split 64:36` · 좌 `figure` FID 곡선 · 우 `cards` 네 방식의 토큰 배치
- assets: Fig. 2(b), 축·범례 포함
- interaction: none

### 7. Dual-Timestep Scheduling

- section: `method`
- message: 같은 분포에서 뽑은 두 timestep을 토큰 사이에 나누면 토큰별 주변분포를 유지하면서 한 입력 안에 noise 수준 차이를 만들 수 있습니다.
- on-slide facts: \(t,s\sim p(t)\) · mask \(M\) 안은 \(s\), 밖은 \(t\) · \(R_M\)은 두 번째 timestep의 배정 확률이며 \(R_M\leq0.5\) · 보고된 \(R_M\)은 이미지 0.25, 비디오 0.10, 오디오 0.50 · student의 조건 입력은 scalar에서 토큰별 벡터로 확장.
- source: §3.3 p. 4, Fig. 3, Eq. (4)–(5), App. A.3 p. 17
- block: `split 60:40` · 좌 `diagram` 같은 토큰 격자에 timestep 배정 · 우 `equation` 토큰별 timestep과 noising
- assets: Eq. (4)–(5), Fig. 3을 참고한 토큰 격자 SVG 명세
- interaction: stepper — reveals: 두 번의 timestep 추출이 student와 teacher의 입력 차이로 이어지는 과정 ; states: ① 같은 분포에서 \(t,s\) 추출 ② mask에 따라 student 토큰에 \(t,s\) 배정 ③ 같은 격자 아래에 teacher의 전체 토큰 \(\min(t,s)\) 배정 표시. 대표 인터랙션, 클리커 다음 키 사용.

### 8. EMA teacher와 학습 손실

- section: `method`
- message: Student는 mixed-noise 입력에서 velocity를 예측하면서, 더 깨끗한 입력을 본 EMA teacher의 깊은 층 표현을 맞춥니다.
- on-slide facts: teacher 입력은 전 토큰에 \(\min(t,s)\) · student 중간층의 MLP projection과 teacher 깊은 층 간 cosine 정렬 · teacher stop-gradient와 EMA decay 0.9999 · \(\gamma=0.8\) · 기본 층 위치 \(l=0.3D,\ k=0.7D\), ImageNet SiT-XL 약 675M에서 \(l=8,\ k=20\).
- source: §3.4 p. 4, Fig. 3, Eq. (6)–(7), App. A.3 p. 17, App. H 및 Fig. 21 p. 24
- block: `split 56:44` · 좌 `figure` 두 forward와 EMA 화살표 · 우 `equation` 정렬 손실과 총손실, 기호·설정값 병기
- assets: Fig. 3, Eq. (6)–(7), Fig. 21 기본 설정 라벨
- interaction: none

### 9. ImageNet 256×256 비교

- section: `results`
- message: ImageNet에서는 Self-Flow가 약 3M step 뒤 REPA를 FID에서 앞서지만, 4M step에서의 순위는 지표마다 다릅니다.
- on-slide facts: class-conditional ImageNet 256×256, SiT-XL 약 675M, SD-VAE, 4M step · SRA / REPA / Self-Flow 순으로 FID **7.27 / 5.89 / 5.70**, sFID **5.87 / 5.73 / 4.97**, IS **143.06 / 157.66 / 151.40**, Recall **0.68 / 0.69 / 0.67** · Self-Flow의 FID Δ **−0.19** vs REPA.
- source: §4.1, Table 1 p. 5, App. A.3–A.4 pp. 17–18, App. G.1 및 Fig. 20(a) pp. 22–23
- block: `split 54:46` · 좌 `table` 4M step의 여러 지표 · 우 `figure` 약 3M step 전후의 FID 궤적
- assets: Table 1의 4M step 행, Fig. 20(a)의 축·범례
- interaction: none

### 10. Text-to-image의 FID와 정렬

- section: `results`
- message: 1M step의 T2I 실험에서 Self-Flow는 FID가 가장 낮았고, DINOv2 feature로 측정한 거리에서도 REPA를 앞섰습니다.
- on-slide facts: 내부 T2I 20M 페어, FLUX.2 backbone 약 625M, SD-VAE, 1M step · FID는 Vanilla 4.08, SigLIP 2 3.97, REPA 3.92, SRA 3.70, Self-Flow 3.61 · Self-Flow vs REPA의 FID Δ **−0.31**, FD-DINOv2 **173.35 → 167.98**(Δ **−5.37**) · sFID는 SRA 8.05, Self-Flow 8.14.
- source: §4 구현 설정 및 §4.1 pp. 5–6, Table 2, Fig. 5(b)
- block: `split 55:45` · 좌 `bars` 1M step FID 5개 · 우 `figure` FD-DINOv2 학습 궤적과 두 종료값 · 하단 `compare` SRA와 Self-Flow의 sFID
- assets: Table 2의 FID·sFID·FD-DINO 열, Fig. 5(b)의 축·범례
- interaction: none

### 11. Text-to-video의 FVD와 FID

- section: `results`
- message: 이 비디오 설정에서 Self-Flow는 두 지표를 모두 개선했고, 비디오와 깊이 정보를 제공하는 두 외부 encoder는 두 지표를 모두 악화시켰습니다.
- on-slide facts: 내부 영상 6M, 약 625M, Wan2.2 AE, 600K step · FVD / framewise FID는 Vanilla 50.95 / 9.28, SRA 49.75 / 9.02, DINOv2 49.59 / 9.39, Depth Anything 3 51.52 / 9.85, V-JEPA 2 53.55 / 9.91, Self-Flow 47.81 / 8.92 · Self-Flow Δ vs Vanilla는 FVD **−3.14**, framewise FID **−0.36**.
- source: §4.1 p. 5, Table 3 p. 6, App. A.4 p. 18
- block: `split 70:30` · 좌 `table` 두 지표와 6개 방법 · 우 `deltas` Vanilla 기준, 지표별 숫자 하나씩
- assets: Table 3
- interaction: none

### 12. Text-to-audio의 FAD 비교

- section: `results`
- message: 방법별로 설정을 고른 오디오 실험에서 Self-Flow의 FAD가 세 변형 모두 가장 낮았고, MERT의 결과는 지표마다 달랐습니다.
- on-slide facts: FMA 10초 클립, 약 625M, Songbloom AE, 350K step · FAD의 CLAP / CLAP-M / CLAP-A 순으로 Vanilla 148.874 / 0.1695 / 0.1059, SRA 147.215 / 0.1664 / 0.1034, MERT 148.883 / 0.1677 / 0.1040, Self-Flow 145.645 / 0.1634 / 0.1001 · 선택된 logit-normal trainshift는 Self-Flow 1.0, 나머지 0.75 · sampleshift는 모두 6.93.
- source: §4.1 및 Table 4 p. 6, App. A.1 p. 16, App. B 및 Table 5 p. 19
- block: `split 72:28` · 좌 `table` FAD 3종 · 우 `compare` 선택된 trainshift와 공통 sampleshift
- assets: Tables 4–5
- interaction: none

### 13. 공유 backbone과 loss weight

- section: `results`
- message: 하나의 backbone을 공유한 mixed-modality 실험에서 Self-Flow는 시험한 다섯 loss weight 조합 모두에서 세 모달리티의 지표를 개선했습니다.
- on-slide facts: 이미지·비디오·오디오별 입출력 층과 공유 backbone · Fig. 8(a)는 세 가지 강조 설정, Table 6은 다섯 조합 · video-weighted 설정 \((w_I,w_V,w_A)=(0.131,0.628,0.241)\)에서 FM 대비 이미지 FID **3.35 → 3.19**(Δ **−0.16**), 비디오 FVD **62.7 → 58.0**(Δ **−4.7**), 오디오 FAD(CLAP) **160.1 → 157.4**(Δ **−2.7**).
- source: §4.2 및 Fig. 8(a) pp. 6–7, App. D 및 Table 6 pp. 20–21
- block: `split 57:43` · 좌 `figure` 역축 radar chart와 세 weight 설정 · 우 `deltas` 같은 video-weighted 조건에서 지표별 Δ
- assets: Fig. 8(a)의 축·범례, Table 6의 video-weighted 행
- interaction: none

### 14. Joint Video-Action 전이

- section: `results`
- message: 같은 RT-1 fine-tuning 조건에서 Self-Flow 초기화의 이점은 100K step까지 복수 물체나 동작 순서가 필요한 과제에서 남았습니다.
- on-slide facts: video-weighted 625M checkpoint, RT-1 73.5K episodes, SIMPLER 평가 · 30K step에서 FM의 `Open and Place` 성공률 0% · 100K step에서 `Pick Up Coke Can`과 `Open/Close Drawer` 격차 축소, `Move Near`와 `Open and Place` 격차 유지 · rollout 관찰 지점은 두 물체 간 거리와 서랍 열기 → 사과 넣기 순서.
- source: §4.2, Figs. 7·8(b) p. 7, App. E pp. 21–22
- block: `split 54:46` · 좌 `figure` 과제별 30K·100K 성공률 · 우 `figureNumbered` 두 rollout의 관찰 지점
- assets: Figs. 7·8(b), 과제명·축·범례 포함
- interaction: none

### 15. 생성 샘플의 세 가지 비교

- section: `results`
- message: 논문의 정성 비교에서는 글자 판독성, 물체 형태, 프레임 사이의 신체 일관성을 샘플에서 직접 확인할 수 있습니다.
- on-slide facts: Fig. 9의 typography 한 쌍 — 4B mixed-modality 모델에서 글자 누락·왜곡과 판독성 확인 · Fig. 10(a)의 파란 Vespa — Vanilla·REPA·SRA·Self-Flow의 차체 형태와 세부 묘사 · Fig. 10(b)의 춤추는 여성 — 프레임 간 팔다리 유지 여부, 비디오 모델 약 625M·6M 학습 영상 · 정성 샘플은 50 inference steps, CFG는 이미지 3.5 / 비디오 5.
- source: §4.3 pp. 7–9, Figs. 9·10, App. A.3 p. 17
- block: `split 34:66` · 좌 `figureNumbered` typography 한 쌍 · 우 `figureNumbered` Vespa와 춤 영상의 프레임 스트립
- assets: Fig. 9 한 쌍, Fig. 10(a)의 Vespa, Fig. 10(b)의 춤추는 여성, 모델 라벨 포함
- interaction: none

### 16. Semantic Autoencoder와의 조합

- section: `results`
- message: RAE와 FLUX.2 AE 실험에서도 같은 autoencoder를 쓰는 기준 모델에 Self-Flow를 더했을 때 FID가 낮아졌습니다.
- on-slide facts: ImageNet 256×256, SiT-XL, RAE, 1M step에서 FID **3.24 → 2.95**(Δ **−0.29**) · FLUX.2 AE를 사용한 T2I에서는 Fig. 20(b)의 200K–600K step 비교 구간에서 Self-Flow가 Vanilla보다 낮은 FID · 각 곡선의 비교 기준은 같은 task와 같은 AE.
- source: §4.1, Table 1 및 Fig. 4(a) p. 5, App. G.2 및 Fig. 20(b) pp. 23–24
- block: `split 50:50` · 좌 `figure` RAE 학습 곡선과 `deltas` FID 한 개 · 우 `figure` FLUX.2 AE 학습 곡선
- assets: Fig. 4(a), Table 1의 RAE 두 행, Fig. 20(b), 각 축·범례 포함
- interaction: none

### 17. 모델 크기와 학습 FLOPs

- section: `analysis`
- message: 논문의 T2I sweep에서는 모델 크기가 커질수록 Self-Flow와 REPA의 CLIP score 격차가 벌어졌습니다.
- on-slide facts: 290M·420M·625M·1B에 대응하는 depth 8·14·21·28 · 최대 1M step까지의 CLIP score 궤적과 training FLOPs 기준 궤적 · 보고된 곡선에서 Self-Flow 625M이 REPA 1B보다 높은 CLIP score · 근거 범위는 T2I 네 규모의 CLIP score 비교.
- source: §4.1 Scaling Behavior 및 Fig. 6(a, b) p. 6
- block: `split 50:50` · 좌 `figure` step 축 · 우 `figure` FLOPs 축 · 두 곡선의 625M Self-Flow와 1B REPA 강조
- assets: Fig. 6(a, b), 축·범례 포함
- interaction: none

### 18. 층별 ImageNet Linear Probe

- section: `analysis`
- message: 2M step의 linear probe는 Self-Flow의 초기·중간층 feature에서 ImageNet 클래스 정보가 더 잘 읽힌다는 근거를 제공합니다.
- on-slide facts: ImageNet, SiT-XL 약 675M, 2M step · Vanilla와 Self-Flow의 layer별 top-1 accuracy · 초기·중간층에서 개선 · 측정 대상은 이미지 클래스의 linear separability, 토큰 간 문맥 사용과 비디오·오디오 표현은 별도 검증 대상.
- source: §4.1 및 Fig. 4(b) p. 5, App. A.3 p. 17
- block: `split 67:33` · 좌 `figure` layer별 top-1 곡선 · 우 `compare` probe의 관측량과 논문이 제안한 학습 기전
- assets: Fig. 4(b), 축·범례 포함
- interaction: none

### 19. Self-Flow 구성요소 Ablation

- section: `analysis`
- message: ImageNet ablation에서 representation loss 제거의 FID 열화가 가장 컸고, 두 번째 timestep의 표본 범위도 결과에 영향을 줬습니다.
- on-slide facts: ImageNet class-to-image, SiT-XL 약 675M, Fig. 11(a)의 200K–600K step 궤적 · §4.4의 전체 설정 대비 FID 열화 요약은 \(\mathcal L_{\rm rep}\) 제거 **+4점 초과**, mask 제거 **+1점 초과** · \(s\)를 \(t\)보다 최대 0.2만큼 낮은 범위에 제한하면 mask 제거에 가까운 열화 · cosine을 \(\ell_1\)로 바꾸면 후반 FID 상승.
- source: §4.4 pp. 9–10, Fig. 11(a), Eq. (6), App. A.3 p. 17
- block: `split 64:36` · 좌 `figure` 설정별 FID 학습 궤적 · 우 `deltas` 제거 실험 두 개와 `compare` 범위 제한·손실 교체
- assets: Fig. 11(a), 축·범례 포함
- interaction: none

### 20. Noise 분포와 학습 비용

- section: `analysis`
- message: Self-Flow를 적용할 때는 timestep 분포에 따라 달라지는 이득과 teacher forward에 드는 추가 학습 연산을 함께 봐야 합니다.
- on-slide facts: T2I 약 625M, 최대 1M step · uniform과 logit-normal \(\alpha=1.78\) 비교 · uniform에서 REPA와 Self-Flow의 FID가 모두 개선되고 두 방법의 차이가 커짐 · Self-Flow는 학습에서 EMA teacher forward 추가 · Fig. 6(b)의 비용 축은 T2I training FLOPs.
- source: §5 p. 10, Fig. 11(b) p. 9, Fig. 6(b) p. 6, App. A.2 pp. 16–17
- block: `split 63:37` · 좌 `figure` scheduler별 FID 궤적 · 우 `groups` 분포에 따른 변화와 비용의 측정 범위
- assets: Fig. 11(b), 축·범례 포함
- interaction: none

### 21. 근거 정리와 토론

- section: `discussion`
- message: 실험은 두 timestep과 self-distillation을 결합한 설정의 생성 이득을 뒷받침하고, 그 이득의 기전과 비용은 별도의 검증 문제로 남깁니다.
- on-slide facts:
  - **정리** — Dual-Timestep과 EMA feature target · 생성 지표, ImageNet linear probe, 구성요소 ablation · scheduler와 평가 지표에 따른 결과 차이.
  - **근거 · 절 간 불일치** — App. A.3은 baseline의 \(p(t)\)가 같다고 설명하고, App. B는 오디오의 선택된 trainshift를 1.0 대 0.75로 보고한다. 동일 trainshift에서 세 FAD 차이는 각각 얼마나 남는가?
  - **근거 · 선정 지표** — 오디오 설정 선정과 최종 보고에 같은 세 FAD 변형을 사용한다. 선정용 평가와 최종 평가를 분리해도 순위가 재현되는가?
  - **근거 · 미측정 기전** — ImageNet linear probe의 개선은 cleaner token을 실제로 얼마나 활용하는지 보여 주는가? 고노이즈 토큰을 고정하고 주변 문맥을 가리면 어떤 차이가 나는가?
  - **대가 · 해석** — Teacher forward를 추가하는 설계에서, 256토큰의 256×256 이미지와 약 3K 토큰의 45프레임·192p 비디오는 같은 wall-clock 예산에서 각각 언제 이득을 보이는가?
- source: Fig. 4(b) p. 5, Fig. 11(a) p. 9, §5 p. 10, App. A.2–A.3 p. 17, App. B 및 Table 5 p. 19
- block: 어두운 `statement` · `split 38:62` · 좌 `lead`와 정리 3항목 · 우 `groups` 토론 4개 · 비용 질문에만 `note`로 **해석** 표시
- assets: none
- interaction: none

### 22. 질의응답

- section: `discussion`
- message: 이제 가장 설득력 있었던 비교와 후속 실험이 필요한 지점을 함께 논의하겠습니다.
- on-slide facts: *Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis* · Chefer, Esser 외 · 2026년 3월 4일 preprint · 프로젝트 페이지.
- source: p. 1 서지 정보 및 프로젝트 주소
- block: `split 70:30` · 좌 `lead` 질의응답 · 우 서지 정보와 프로젝트 링크
- assets: [Self-Flow 프로젝트 페이지](https://bfl.ai/research/self-flow)
- interaction: none