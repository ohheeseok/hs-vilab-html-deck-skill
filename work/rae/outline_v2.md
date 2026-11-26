## Ledger

- Fig. 1 — use: 2 · 대표 그림. ImageNet 256×256 FID 연표에서 VAE 계열과 RAE 계열의 위치
- Fig. 2 — use: 5 · SD-VAE와 DINOv2-B RAE의 구조 및 이미지당 연산량
- Fig. 3 — use: 8 · 같은 손실 축에서 폭과 깊이를 비교한 단일 이미지 과적합 실험
- Fig. 4 — use: 14 · 학습 epoch에 따른 RAE DiT-XL의 수렴
- Fig. 5 — use: 12 · noisy latent와 backbone 출력이 DDT head로 들어가는 경로
- Fig. 6 — use: 15 · (a) backbone 크기별 학습 GFLOPs, (b) 누적 학습 GFLOPs에 따른 수렴. cut: (c)는 모델 FLOPs까지 별도 척도로 읽어야 하며, 이 장의 비교는 (a)·(b)와 Table 6으로 제시
- Fig. 7 — use: 17 · ImageNet 512×512 AutoGuidance 생성 예시
- Table 1 — use: 5, 6 · (b) 디코더 비용, (a)·(c)·(d) 복원 및 linear probe
- Table 2 — use: 7, 13 · 기본 DiT의 RAE·SD-VAE 비교 및 stepper 기준선
- Table 3 — use: 9 · 인코더 토큰 차원과 DiT 폭을 교차한 과적합 손실 3×3
- Table 4 — use: 10, 13 · schedule shift 전후 gFID
- Table 5 — use: 11, 13 · 디코더 노이즈 증강 전후 gFID·rFID 및 stepper 값
- Table 6 — use: 13, 15, 18 · DDT head 적용 결과와 DINOv2 크기별 gFID
- Table 7 — use: 16, 17 · ImageNet 512×512 guidance 결과 및 직접 생성 비교점
- Table 8 — use: 2, 12, 14, 16, 20 · 대표 결과, 파라미터 수, 수렴 그림의 비교점 대조, 벤치마크 및 평가 프로토콜
- Table 9 — use: 17 · 512×512 직접 생성과 디코더 업샘플링
- Table 10 — use: 19, 20 · SD-VAE에서의 DDT head 반례와 최적화 비교
- Table 11 — use: 19, 20 · 토큰 형태를 맞춘 픽셀·RAE 비교와 최적화 비교
- 부록 Fig. 8 — use: 6 · 앵무새와 버스 입력에 대한 인코더별 복원
- 부록 Fig. 10 — cut: Fig. 7에서 생성 예시를 제시하고, 같은 메시지를 위한 `golden retriever` 그리드는 생략
- 부록 Fig. 13 — cut: Fig. 7에서 생성 예시를 제시하고, 같은 메시지를 위한 `macaw` 그리드는 생략
- 부록 Table 12 — use: 5 · 디코더 학습 기간, 손실, frozen DINO-S/8 판별자
- 부록 Table 13 — use: 9, 12 · 폭 값만 인용
- 부록 Table 14 — use: 20 · random·balanced sampling에 따른 gFID 및 guided 순위 변화
- 부록 Table 15 — use: 11, 18 · (c) \(\tau\) 비교, (a)·(b) 인코더 종류·크기별 비교
- 부록 Table 16 — use: 12 · DDT head의 깊이·폭·GFLOPs·gFID

## Sections

- `none` — 표지 (1장, 0:25)
- `summary` — 요약·배경 (2–4장, 2:35)
- `claim1` — ① 복원 (5–6장, 2:00)
- `claim2` — ② 고차원 확산 (7–13장, 7:05)
- `results` — 결과 (14–17장, 3:35)
- `scope` — 범위 (18–19장, 1:50)
- `discussion` — 정리와 토론 (20–21장, 2:30)

1920×1080 HTML 기준, 2–21장 하단에 구간 진행 표시줄을 배치합니다. 총 21장, 내용 19장, 합계 1,200초입니다. 클리커로 장을 넘기며, 13장에서만 다음 키로 막대를 하나씩 공개합니다.

## Slides

### 1. 표현 인코더를 쓰는 DiT

- section: `none`
- time: 25
- message: 이 논문은 사전학습한 시각 표현을 이미지 복원과 확산 모델 학습에 함께 쓸 수 있는지 검증합니다.
- on-slide facts: *Diffusion Transformers with Representation Autoencoders* · Boyang Zheng, Nanye Ma, Shengbang Tong, Saining Xie · New York University · arXiv:2510.11690v1, 2025년 10월 · VILAB 논문 세미나 · 오희석(VILAB, 한성대학교)
- source: p. 1, 제목·저자·arXiv 표기
- block: `lead` 중앙, 원제와 저자 정보 아래에 발표자
- assets: none
- interaction: none
- notes: 오늘 다룰 논문은 *Diffusion Transformers with Representation Autoencoders*입니다. 저자들은 사전학습한 시각 인코더의 출력을 복원과 확산 모델 학습에 함께 사용합니다. 두 용도에서 무엇을 검증했고 어떤 조건에서 결과가 달라졌는지 살펴보겠습니다.

### 2. RAE와 DiT^DH 한눈에

- section: `summary`
- time: 50
- message: 논문은 동결한 표현 인코더에 ViT 디코더를 붙이고, 그 토큰을 직접 모델링하도록 확산 학습과 DiT 구조를 조정합니다.
- on-slide facts:
  1. **RAE 복원** · DINOv2-B, SigLIP2-B, MAE-B와 ViT 디코더
  2. **고차원 확산 설정** · 토큰 차원 이상의 폭, 차원 의존 schedule shift, 디코더 노이즈 증강
  3. **DiT^DH** · wide DDT head · DINOv2-B, XL, ImageNet 256×256, 800 epoch, 무가이던스, class-balanced FID-50K에서 gFID **1.51**
- source: 초록·Fig. 1, p. 1 · §3–5, pp. 3–9 · Table 8, p. 9 · App. D–E, p. 24
- block: 밝은 배경 · 상단 `lead`, 중앙 `cards` 3개, 하단 전폭 `figure`에 Fig. 1의 연도·FID 축과 범례
- assets: Fig. 1 전체, Table 8의 DiT^DH-XL 800 epoch 행
- interaction: none
- notes: 연구의 첫 단계는 동결한 표현 인코더의 토큰에서 이미지를 복원하는 것입니다. 두 번째는 그 토큰의 차원에 맞게 확산 학습을 조정하는 것이고, 세 번째는 넓은 head를 붙여 연산량 대비 생성 성능을 높이는 것입니다. 대표 수치인 1.51은 DINOv2-B를 쓰는 XL 모델을 800 epoch 학습한 뒤, 클래스당 같은 수의 이미지를 guidance 없이 생성해 얻은 gFID입니다. 아래 연표에서는 AutoGuidance를 쓴 점이 별도로 표시되어 있습니다.

### 3. 잠재 확산과 표현 학습의 갈래

- section: `summary`
- time: 55
- message: 이 논문은 압축 latent에서 확산을 학습하는 연구와 사전학습 표현을 복원 및 생성에 활용하는 연구가 만나는 지점에 있습니다.
- on-slide facts: ① **압축 latent에서의 확산** · LDM, DiT, SiT ② **복원용 tokenizer의 표현 학습** · VA-VAE, MAETok, DC-AE 1.5 ③ **생성 모델에 표현 도입** · REPA, DDT, REG, ReDi  
  **발표 질문** · 동결한 표현의 복원 충실도와 고차원 확산의 성립 조건은?
- source: §1–2, pp. 1–3 · App. A, pp. 19–20
- block: 전폭 `groups` 3열, 마지막 줄에 질문 `callout`
- assets: none
- interaction: none
- notes: LDM과 DiT, SiT 계열은 autoencoder가 만든 압축 latent에서 확산을 학습합니다. VA-VAE와 MAETok은 복원용 tokenizer를 학습할 때 표현 정렬이나 masked modeling을 활용합니다. REPA와 DDT는 생성 모델 학습에 표현 정렬을 쓰고, ReDi는 VAE latent와 DINOv2 특징을 함께 생성합니다. 이 논문을 읽으면서 동결한 표현이 얼마나 충실하게 복원되고, 그 위에서 확산을 학습하려면 무엇이 필요한지 보겠습니다.

### 4. 논문이 겨냥한 두 통념

- section: `summary`
- time: 50
- message: 표현 토큰에 복원할 정보가 남아 있는지와 DiT가 그 토큰의 분포를 학습할 수 있는지는 따로 검증해야 합니다.
- on-slide facts: **① 의미 중심 인코더의 픽셀 복원 한계** → 인코더 동결, 디코더 학습, SD-VAE 대비 rFID와 동일 입력 복원 비교 · **② 고차원 latent에서의 확산 성능 저하** → 기본 DiT 비교, 폭 병목의 손실 하한, 처방 전후 gFID
- source: §1, p. 2 · §3, Table 1, pp. 3–4 · §4, Table 2, Theorem 1, pp. 4–7
- block: 전폭 `compare` 2열 · 왼쪽에 통념 ①·②, 오른쪽에 각 통념의 검증 방법
- assets: none
- interaction: none
- notes: 첫 번째 통념은 의미를 잘 담는 인코더가 경계나 질감처럼 복원에 필요한 세부 정보를 잃는다는 것입니다. 두 번째는 그렇게 얻은 토큰의 차원이 높아서 확산 학습에 불리하다는 것입니다. 앞의 통념은 같은 입력을 복원한 결과로, 뒤의 통념은 기본 DiT와 수정한 DiT가 생성한 샘플로 검증합니다.

### 5. RAE의 인코더와 ViT 디코더

- section: `claim1`
- time: 60
- message: RAE는 사전학습한 ViT의 patch token을 동결한 채, 그 토큰을 픽셀로 되돌리는 디코더를 학습합니다.
- on-slide facts:
  - ImageNet 256×256 · DINOv2-B with Registers는 224×224로 보간, encoder patch 14, decoder patch 16 · SigLIP2-B·MAE-B는 encoder/decoder patch 16 · 세 모델 모두 **256토큰 × 768채널**
  - 인코더의 [CLS]·[REG] 제외, patch token별 정규화 · ViT 디코더 16 epoch, L1 + LPIPS + GAN · 판별자 frozen DINO-S/8
  - DINOv2-B 고정, ImageNet-1K val **rFID / 디코더 GFLOPs** · ViT-B 0.58 / 22.2 · ViT-L 0.50 / 78.1 · ViT-XL 0.49 / 106.7 · SD-VAE 기준 0.62 / 310.4
  - Fig. 2의 256×256 이미지당 인코더 GFLOPs · SD-VAE 135 · DINOv2-B 22
- source: §3, Fig. 2, Table 1b, pp. 3–4 · App. C.1–C.2, Table 12, pp. 22–23
- block: `split 46:54` · 왼쪽 `figure`, 오른쪽 토큰·학습 설정 `bullets`와 rFID·GFLOPs `table`
- assets: Fig. 2, Table 1b, Table 12의 디코더 설정
- interaction: none
- notes: DINOv2는 patch 크기가 14이므로 입력을 224×224로 보간해 16×16 격자의 토큰을 얻습니다. 디코더는 토큰마다 한 변이 16픽셀인 patch를 복원해 원래 해상도를 맞춥니다. 인코더는 동결하고, frozen DINO-S/8 판별자와 함께 ViT 디코더를 학습합니다. DINOv2-B를 고정한 비교에서 ViT-B 디코더도 SD-VAE보다 낮은 rFID를 얻었고, 기본 설정인 ViT-XL은 디코더 연산량 106.7 GFLOPs에서 rFID 0.49를 기록했습니다.

### 6. 세 인코더의 복원과 Linear Probe

- section: `claim1`
- time: 60
- message: 세 frozen encoder에 ViT 디코더를 붙인 RAE는 모두 ImageNet에서 SD-VAE보다 낮은 복원 rFID를 얻습니다.
- on-slide facts:
  - ImageNet-1K val, RAE 디코더 ViT-XL · **rFID / linear-probe Top-1** · DINOv2-B 0.49 / 84.5% · SigLIP2-B 0.53 / 79.1% · MAE-B 0.16 / 68.0% · SD-VAE 0.62 / 8.0%
  - MAE-B의 SD-VAE 대비 ΔrFID −0.46(계산) · DINOv2-S/B/L rFID 0.52 / 0.49 / 0.52 · rFID의 단위는 복원 이미지 집합의 분포 비교
  - Fig. 8 · 입력 → DINOv2-B → SigLIP2-B → MAE-B → SD-VAE · 위 행의 앵무새 눈·깃털, 아래 행의 버스 전면·창틀
  - ①의 검증 범위 · ImageNet 복원 · 18번에서 비교할 항목 · rFID 순위와 gFID 순위
- source: §3, Table 1a/c/d, p. 4 · App. C.3, Fig. 8, p. 23 · App. G.1, Table 15a, p. 25
- block: `split 48:52` · 왼쪽 `table`과 DINOv2 크기별 rFID 한 줄, 오른쪽 `figureNumbered`에 원본 2행과 관찰 지점
- assets: Table 1a/c/d, 부록 Fig. 8
- interaction: none
- notes: 세 RAE 모두 복원 집합의 rFID가 SD-VAE보다 낮고, 그중 MAE-B의 rFID가 가장 낮습니다. 그림에서는 같은 앵무새의 눈과 깃털, 같은 버스의 전면과 창틀을 열마다 비교해 볼 수 있습니다. rFID는 복원 이미지 집합의 분포를 재므로 개별 이미지의 픽셀 오차와는 측정 대상이 다릅니다. 이 실험은 첫 번째 통념을 ImageNet 복원에서 반박하며, 복원이 좋은 인코더가 생성에서도 좋은지는 18번에서 확인하겠습니다.

### 7. 고차원 RAE의 기본 DiT

- section: `claim2`
- time: 55
- message: 같은 수의 토큰을 처리해도 기본 DiT 설정에서는 DINOv2-B RAE의 gFID가 SD-VAE보다 높습니다.
- on-slide facts:
  - ImageNet 256×256, 80 epoch, 무가이던스 FID-50K, 50-step Euler · DINOv2-B RAE DiT patch 1, SD-VAE DiT patch 2 · 두 입력 모두 256토큰 · RAE shift·디코더 노이즈 증강 적용 전
  - **RAE / SD-VAE gFID** · DiT-S 215.76 / 51.74, Δ +164.02 · DiT-XL 23.08 / 7.13, Δ +15.95 · Δ는 RAE−SD-VAE(계산)
  - 후속 가설 3개 · 토큰 차원 대비 DiT 폭 · noise schedule의 기준 차원 · 디코더 학습 latent와 생성 latent의 차이
- source: §4, Table 2, pp. 4–5 · App. D, pp. 23–24
- block: `split 56:44` · 왼쪽 `table`과 `deltas` 2개, 오른쪽 가설 `cards` 3개
- assets: Table 2
- interaction: none
- notes: RAE에는 patch 1을, SD-VAE에는 patch 2를 써서 DiT가 처리하는 토큰 수를 256개로 맞췄습니다. 기본 설정에서 RAE의 gFID는 DiT-S에서 215.76이고, XL로 키워도 23.08로 SD-VAE의 7.13보다 높습니다. 저자들은 이 결과에서 출발해 모델의 폭, 노이즈를 섞는 시간 분포, 디코더가 학습한 입력 분포를 차례로 살펴봅니다.

### 8. 한 이미지 과적합의 폭과 깊이

- section: `claim2`
- time: 60
- message: DINOv2-B 토큰의 차원인 768에 폭이 도달하면 단일 이미지 복원이 개선되며, 폭 384에서 깊이만 늘린 실험의 손실은 0.5 부근에 머뭅니다.
- on-slide facts:
  - Fig. 3 두 패널의 공통 손실 눈금 0–0.5 · DINOv2-B 토큰 차원 \(n=768\)
  - 왼쪽 · 깊이 12 고정, 폭 384·512·640·768·896 · 폭 768 이상에서 낮아지는 손실과 앵무새의 윤곽·색 영역 재현
  - 오른쪽 · 폭 384 고정, 깊이 4·12·16·24 · 이론선 0.5 부근의 관측 손실(곡선 근거), 24층에서도 남는 앵무새 예시의 아티팩트
  - 256×256 대상 3장 × 이미지당 독립 실행 3회 평균 · 한 번에 한 이미지 과적합 · attention head 4개, 학습 1,200 step, Euler 25 step · 붉은 이론선은 9번의 손실 하한
- source: §4.1, Fig. 3, p. 5 · App. F, pp. 24–25
- block: 전폭 정적 `figure` · Fig. 3 두 패널의 공통 손실 눈금, 범례, 생성 예시 유지
- assets: Fig. 3 전체
- interaction: none
- notes: 한 번에 목표 이미지 한 장만 과적합하게 하고, 논문은 세 이미지에서 각각 세 번 실행한 손실을 평균합니다. 왼쪽에서는 깊이를 고정하고 폭을 768까지 늘렸을 때 앵무새 예시의 윤곽과 색 영역이 더 선명하게 재현됩니다. 오른쪽에서는 폭 384를 유지한 채 24층까지 늘려도 관측 손실이 이론선 0.5 부근에 머뭅니다. 다음 장에서 그 이론선이 어디서 나오는지 보겠습니다.

### 9. Theorem 1과 DiT의 폭

- section: `claim2`
- time: 80
- message: Theorem 1은 선형 출력 투영을 쓰는 모델의 폭이 토큰 차원보다 작으면 velocity 예측 손실에 하한이 생긴다고 설명합니다.
- on-slide facts:
  - \(x_t=(1-t)x+t\epsilon\), 독립인 \(\epsilon\sim\mathcal N(0,I_n)\) · \(g(x_t,t)=Bf(Ax_t,t)\) · \(A,B\)는 선형 투영, 출력은 \(\operatorname{Im}(B)\)에 제한, \(\operatorname{rank}(B)\le d\) · App. B.1의 증명에서 \(\mathbb E[x]=0\)으로 중심화
  - \(d<n\)일 때 \(\mathcal L(g)\ge\sum_{i=d+1}^{n}\lambda_i\) · \(\lambda_i\)는 \(\epsilon-x\)의 공분산 고유값 내림차순 · 단일 이미지의 차원당 하한 \((n-d)/n\), \(n=768,d=384\)에서 0.5(계산) · \(d\ge n\)이면 정리의 함수족에 최적 예측기 포함
  - **단일 이미지 과적합 손실** · 열은 DiT-S/B/L, 폭 \(d=384/768/1024\). ✓·✗는 논문의 수렴 표기를 유지
    - DINOv2-S, \(n=384\) · \(3.6\times10^{-2}\) ✓ / \(1.0\times10^{-3}\) ✓ / \(9.7\times10^{-4}\) ✓
    - DINOv2-B, \(n=768\) · \(5.2\times10^{-1}\) ✗ / \(2.4\times10^{-2}\) ✓ / \(1.3\times10^{-3}\) ✓
    - DINOv2-L, \(n=1024\) · \(6.5\times10^{-1}\) ✗ / \(2.7\times10^{-1}\) ✗ / \(2.2\times10^{-2}\) ✓
- source: §4.1, Theorem 1, Eq. (1)–(2), Table 3, p. 6 · App. B.1, Eq. (3)–(5), pp. 20–21 · App. D, Table 13, p. 23
- block: `split 54:46` · 왼쪽 `equation` 2개와 기호·단일 이미지 하한, 오른쪽 Table 3 전체 3×3 행렬
- assets: Eq. (1)–(2), Table 3 전체, Table 13의 S·B·L 폭
- interaction: none
- notes: 출력 투영 \(B\)의 rank가 \(d\) 이하이므로 모델이 예측하는 velocity는 고정된 저차원 부분공간 안에 있습니다. 학습 목표인 \(\epsilon-x\)에는 독립 Gaussian noise가 들어가므로, 그 부분공간이 담지 못하는 방향의 분산이 손실 하한으로 남습니다. 한 이미지에 대해 폭 384와 토큰 차원 768을 대입하면 앞 그림의 차원당 하한인 0.5가 나옵니다. 오른쪽 아홉 조합에서 논문이 수렴으로 표기한 칸은 모두 \(d\ge n\)입니다. 이 정리는 함수족의 표현 가능성에 관한 결과이며, 실제 생성 gFID는 뒤의 실험에서 확인합니다.

### 10. 차원 의존 Schedule Shift

- section: `claim2`
- time: 50
- message: 토큰 수와 채널 수를 함께 반영한 schedule shift를 적용하면 같은 RAE DiT-XL의 gFID가 23.08에서 4.81로 낮아집니다.
- on-slide facts:
  - \(t_m=\dfrac{\alpha t_n}{1+(\alpha-1)t_n}\), \(\alpha=\sqrt{m/n}\) · 기준 입력 차원 \(n=4{,}096\) · RAE 전체 입력 차원 \(m=256\times768=196{,}608\)(계산)
  - \(\alpha=\sqrt{48}\approx6.93\)(계산) · \(t_n=0.5\rightarrow t_m\approx0.87\)(계산) · \(t=1\)은 순수 노이즈
  - DINOv2-B RAE DiT-XL, ImageNet 256×256, 80 epoch, 디코더 노이즈 증강 전, 무가이던스 50-step Euler · gFID 23.08 → 4.81, **Δ −18.27**(계산)
- source: §4.2, pp. 6–7 · Table 4, p. 7 · App. D, p. 24 · App. J, p. 27
- block: `split 58:42` · 왼쪽 `equation`과 0.5→0.87 계산 예시, 오른쪽 `deltas` 1개
- assets: §4.2의 shift 식, Table 4
- interaction: none
- notes: 앞 장에서 \(n\)은 토큰 하나의 차원이었고, 여기서 \(n\)은 schedule의 기준이 되는 전체 입력 차원입니다. DINOv2-B RAE의 전체 차원을 넣으면 기준 timestep 0.5가 약 0.87로 이동해 더 많은 노이즈가 섞입니다. 디코더 증강을 적용하기 전, 같은 DiT-XL에서 이 변경으로 gFID가 18.27 낮아졌습니다.

### 11. RAE의 노이즈 증강 디코더

- section: `claim2`
- time: 50
- message: 디코더 학습에 latent 노이즈를 더하면 생성 gFID는 낮아지고 깨끗한 입력의 복원 rFID는 높아집니다.
- on-slide facts:
  - \(z'=z+\eta\), \(\eta\mid\sigma\sim\mathcal N(0,\sigma^2I)\), \(\sigma\sim|\mathcal N(0,\tau^2)|\) · \(z\)는 frozen encoder 출력, \(\tau\)는 디코더 학습용 노이즈 강도 설정
  - DINOv2-B RAE, shift 적용 DiT-XL, ImageNet 256×256, 80 epoch, 무가이던스 50-step Euler · **\(\tau\) / gFID / rFID** · 0.0 / 4.81 / 0.49 · 0.5 / 4.39 / 0.54 · **0.8 / 4.28 / 0.57** · 1.0 / 4.20 / 0.60
  - 기본값 \(\tau=0.8\), 무증강 대비 **ΔgFID −0.53**(계산), ΔrFID +0.08(계산)
- source: §4.3, Table 5, p. 7 · App. G.2, Table 15c, pp. 25–26
- block: `split 43:57` · 왼쪽 `equation`, 오른쪽 \(\tau\) 4행 `table`과 gFID `deltas` 1개
- assets: §4.3의 노이즈 정의, Table 5, 부록 Table 15c
- interaction: none
- notes: 증강은 디코더를 학습할 때 인코더가 출력한 latent에 적용합니다. 저자들의 설명은 생성된 latent가 깨끗한 학습 latent에서 조금 벗어날 수 있으니, 디코더가 그 주변에서도 복원하도록 학습하자는 것입니다. 표에서 \(\tau\)를 높이면 gFID가 낮아지는 동안 rFID는 높아집니다. 논문의 기본값 0.8에서는 무증강 대비 gFID가 0.53 낮아지고 rFID가 0.08 높아집니다.

### 12. DiT^DH의 Wide DDT Head

- section: `claim2`
- time: 55
- message: DiT^DH는 noisy latent를 직접 받는 얕은 DDT head에 큰 폭을 배치합니다.
- on-slide facts:
  - XL backbone 폭 1,152 · \(z_t=M(x_t\mid t,y)\), \(v_t=H(x_t\mid z_t,t)\) · head에 noisy latent \(x_t\), backbone 조건 \(z_t\), timestep \(t\) 입력
  - DINOv2-B RAE, DiT-XL backbone, ImageNet 256×256, 80 epoch, 무가이던스 50-step Euler · **head 깊이 × 폭 / head GFLOPs / gFID** · 6×1,152 / 25.65 / 2.36 · 4×2,048 / 53.14 / 2.31 · **2×2,048 / 26.78 / 2.16**
  - Table 8의 전체 생성 모델 파라미터 · DINOv2-B DiT^DH-XL 839M · DiT baseline 675M
- source: §5, Fig. 5, p. 8 · Table 8, p. 9 · App. D, Table 13, pp. 23–24 · App. G.3, Table 16, p. 26
- block: `split 48:52` · 왼쪽 `figure`에 \(x_t\)와 \(z_t\)의 경로 표시, 오른쪽 `table`과 전체 모델 파라미터 한 줄
- assets: Fig. 5, Table 13의 XL 폭, Table 16, Table 8의 파라미터 열
- interaction: none
- notes: backbone이 만든 \(z_t\)는 DDT head의 조건으로 들어가고, noisy latent도 head에 직접 들어갑니다. 이 구조는 backbone 전체를 넓힐 때 드는 연산량을 피하면서 velocity를 예측하는 부분의 폭을 키우려는 설계입니다. XL backbone을 고정한 비교에서 2층·폭 2,048 head가 시험한 세 설정 중 가장 낮은 gFID를 얻었습니다. 표의 GFLOPs는 head만의 값이고, 839M과 675M은 벤치마크에 보고된 전체 모델 파라미터입니다.

### 13. 처방을 하나씩 더한 gFID

- section: `claim2`
- time: 75
- message: 같은 80 epoch 비교에서 schedule shift를 적용한 단계의 gFID 하락이 가장 크고, 디코더 증강과 DiT^DH 적용 단계에서도 gFID가 더 낮아집니다.
- on-slide facts: 네 막대 공통 · DINOv2-B RAE, ImageNet 256×256, 80 epoch, guidance 없음, 50-step Euler, FID-50K · 선형 gFID 축 0–25 · SD-VAE DiT-XL 7.13 점선 고정 · 0단계의 Δ는 SD-VAE 대비, 1–3단계의 Δ는 직전 막대 대비(계산) · 마지막 단계는 DiT^DH 전용 최적화 포함
- source: §4, Table 2, p. 5 · §4.2–4.3, Tables 4–5, p. 7 · §5, Table 6, p. 8 · App. D, p. 24
- block: 전폭 `bars` SVG + `stepper` · 상단 공통 조건, 중앙 막대와 점선, 하단 현재 단계의 Δ와 출처
- assets: 기존 `rae_ladder.svg`(작업 폴더 루트, 덱 참조명 `figures/rae_ladder.svg`) · Tables 2, 4, 5, 6
- interaction: 대표 `stepper` — reveals: 같은 축과 SD-VAE 기준선을 유지한 채 어느 단계에서 기준선을 넘고 이후 얼마나 개선되는지 공개 · states:
  - **0** · `title` 기본 DiT-XL · `text` gFID 23.08, SD-VAE DiT-XL 7.13 대비 Δ +15.95 · DINOv2-B RAE, ImageNet 256×256, 80 epoch, 무가이던스, 50-step Euler · `source` Table 2
  - **1** · `title` + Schedule Shift · `text` gFID 4.81, 직전 대비 Δ −18.27 · DINOv2-B RAE, ImageNet 256×256, 80 epoch, 무가이던스, 50-step Euler · `source` Table 4
  - **2** · `title` + 노이즈 증강 · `text` gFID 4.28, 직전 대비 Δ −0.53, \(\tau=0.8\) · DINOv2-B RAE, ImageNet 256×256, 80 epoch, 무가이던스, 50-step Euler · `source` Table 5, 부록 Table 15c
  - **3** · `title` + DDT Head · `text` DiT^DH-XL gFID 2.16, 직전 대비 Δ −2.12, 전용 최적화 포함 · DINOv2-B RAE, ImageNet 256×256, 80 epoch, 무가이던스, 50-step Euler · `source` Table 6, App. D
- notes: 네 막대는 모두 ImageNet 256×256에서 80 epoch 학습한 DINOv2-B RAE의 무가이던스 결과이고, 점선은 같은 조건의 SD-VAE DiT-XL입니다. [1] 폭 1,152의 XL에서 schedule shift를 적용하면 23.08에서 4.81로 내려가며 점선 아래로 들어옵니다. [2] 노이즈 증강 디코더를 쓰면 4.28까지 더 낮아집니다. [3] DDT head와 전용 최적화를 적용한 DiT^DH-XL의 값은 2.16입니다. head의 효과를 따로 추정하려면 어떤 비교가 필요한지 마지막에 돌아오겠습니다.

### 14. 학습 Epoch에 따른 수렴

- section: `results`
- time: 50
- message: 폭 조건, schedule shift, 디코더 증강을 적용한 RAE DiT-XL은 Fig. 4에서 SiT-XL과 REPA-XL의 비교 FID에 더 적은 학습 epoch로 도달합니다.
- on-slide facts:
  1. ImageNet 256×256, 무가이던스 FID-50K, DINOv2-B RAE DiT-XL · 80 epoch 4.28 · 720 epoch 2.39(곡선 근거, §4.3 본문에도 명시)
  2. SiT-XL 기준점 8.26 · Fig. 4에 표시된 도달 epoch 비율 47×(곡선 근거)
  3. REPA-XL 기준점 5.90 · Fig. 4에 표시된 도달 epoch 비율 16×(곡선 근거)
- source: §4.3, Fig. 4, p. 7 · 비교 프로토콜 대조는 Table 8, p. 9 및 App. E, Table 14, pp. 24–25
- block: 전폭 `figure` 하나와 읽기 `bullets` 3개 · epoch 축, FID 축, 기준선, 화살표 유지
- assets: Fig. 4, 발표자 notes용 Table 8·14 비교값
- interaction: none
- notes: 이 곡선의 RAE 모델은 wide head를 붙이기 전의 DiT-XL입니다. 47배와 16배는 Fig. 4의 기준 FID에 도달하기까지 걸린 epoch의 비율입니다. 같은 모델은 80 epoch에서 4.28, 720 epoch에서 2.39를 기록했습니다. Fig. 4에 표시된 SiT-XL 8.26과 REPA-XL 5.90은 balanced sampling 재평가를 다루는 Table 8의 표시값인 8.61과 5.78과 다르므로, 여기서는 Fig. 4에 적힌 기준점을 사용합니다.

### 15. DiT^DH의 연산량과 인코더 크기

- section: `results`
- time: 50
- message: DiT^DH는 DINOv2-B에서 연산량 대비 낮은 gFID를 보이고, XL끼리 비교하면 시험한 DINOv2 인코더 세 크기에서 모두 gFID를 낮춥니다.
- on-slide facts:
  - Fig. 6a · DINOv2-B RAE의 DiT^DH-S/B/L/XL을 **DiT-XL 한 점**과 비교 · ImageNet 256×256, 80 epoch, 무가이던스 50-step Euler · 논문 본문의 DiT^DH-S 6.07, B 3.38, XL 2.16 · DiT^DH-B 학습 FLOPs는 DiT-XL의 약 40%(§5 본문)
  - Fig. 6b · 가로축 누적 diffusion 학습 GFLOPs · DiT^DH-XL의 수렴 곡선과 VAE 계열 baseline의 최종 보고점 비교(곡선 근거)
  - Table 6 · 같은 벤치마크·80 epoch·무가이던스 · **DINOv2 S / B / L** · DiT-XL **3.50 / 4.28 / 6.09** · DiT^DH-XL **2.42 / 2.16 / 2.73**
- source: §5, Fig. 6a/b, Table 6, p. 8 · §5.1, pp. 9–10 · App. D, p. 24
- block: `split 64:36` · 왼쪽 `figure` 한 영역에 Fig. 6a·b를 나란히 배치하고 각각 축·범례 유지, 오른쪽에 Table 6의 XL 모델 2종 × 인코더 3종 비교
- assets: Fig. 6a·b 크롭, Table 6 원값
- interaction: none
- notes: 왼쪽 첫 그래프는 DINOv2-B를 고정하고 DiT^DH의 backbone 네 크기를 기본 DiT-XL 한 점과 비교합니다. 논문 본문에 따르면 DiT^DH-B는 그 DiT-XL 학습 FLOPs의 약 40%를 쓰면서 gFID 3.38을 얻었습니다. 두 번째 그래프는 누적 학습 GFLOPs에 따른 곡선이며, 여러 baseline은 최종 보고점으로 표시되어 있습니다. 오른쪽 표는 backbone을 XL로 고정하고 인코더 크기만 바꾼 비교입니다.

### 16. ImageNet 256·512 벤치마크

- section: `results`
- time: 70
- message: DiT^DH-XL은 class-balanced ImageNet 평가에서 256×256 무가이던스 gFID 1.51, 두 해상도의 AutoGuidance gFID 1.13을 기록합니다.
- on-slide facts: class-conditional FID-50K · 논문의 RAE 생성은 class-balanced sampling, 클래스당 50장, 기본 50-step Euler · 표의 각 값은 **gFID / IS**

  | 해상도·모델 | Epoch | Params | 무가이던스 | Guidance |
  |---|---:|---:|---:|---:|
  | 256×256 · REPA-E | 800 | 675M | 1.70 / 217.3 | 1.15 / 304.0 |
  | 256×256 · DiT-XL, DINOv2-S | 800 | 676M | 1.87 / 209.7 | 1.41 / 309.4 |
  | 256×256 · DiT^DH-XL, DINOv2-B | 800 | 839M | 1.51 / 242.9 | 1.13 / 262.6 |
  | 512×512 · EDM2 | — | — | — | 1.25 / — |
  | 512×512 · DiT^DH-XL, DINOv2-B | 400 | — | — | 1.13 / 259.6 |

  - DINOv2-S DiT-XL guidance · CFG with interval · DINOv2-B DiT^DH-XL · AutoGuidance, guide DiT^DH-S · 256×256은 14 epoch checkpoint·scale 1.42, 512×512는 20 epoch checkpoint·scale 1.5
  - DiT^DH-XL의 ΔgFID(계산) · 256 REPA-E 대비 무가이던스 −0.19, guided −0.02 · 512 EDM2 대비 guided −0.12
- source: §5.1, Tables 7–8, pp. 9–10 · App. D–E, p. 24 · App. I, p. 27
- block: 전폭 `table` · 해상도·guidance 열을 분리하고 하단에 guide 설정과 ΔgFID
- assets: Table 8의 REPA-E 및 RAE 두 행, Table 7의 EDM2·DiT^DH-XL 행, App. I
- interaction: none
- notes: 256×256에서 REPA-E와 RAE 두 모델은 모두 800 epoch 결과이고, 파라미터 수는 표에 따로 표시했습니다. DINOv2-B DiT^DH-XL은 REPA-E 대비 무가이던스 gFID가 0.19, guided gFID가 0.02 낮습니다. DINOv2-S DiT-XL의 guided 결과에는 CFG with interval을 쓰고, DINOv2-B DiT^DH-XL에는 작은 DiT^DH-S로 AutoGuidance를 적용합니다. 512×512의 1.13은 400 epoch 결과이며, 256×256에서 같은 gFID를 얻은 경우와 guide checkpoint 및 scale이 다릅니다.

### 17. 512×512 샘플과 업샘플링

- section: `results`
- time: 45
- message: 256×256 확산 모델을 재사용해 512×512로 출력할 수 있으며, 1,024토큰으로 직접 생성한 비교군이 더 낮은 gFID와 rFID를 얻습니다.
- on-slide facts:
  - Fig. 7 · 직접 학습한 DINOv2-B DiT^DH-XL, ImageNet 512×512, AutoGuidance scale 1.5 · 흰 앵무새의 자세와 배경, 거북의 수중·지상 장면, 등대의 시점·조명, 버거의 재료·구도
  - Table 9 · DINOv2-B DiT^DH-XL, ImageNet 512×512, 두 경로 모두 400 epoch, guidance 적용 비교 · **경로 / 토큰 / gFID / rFID** · Direct 1,024 / 1.13 / 0.53 · Upsample 256 / 1.61 / 0.97
  - Upsample · 256×256 확산 모델 재사용, 출력 patch 한 변 2배인 디코더로 교체 · Direct 대비 토큰 수 ¼, ΔgFID +0.48, ΔrFID +0.44(계산)
- source: §5.1, Fig. 7, p. 10 · §6.1, Table 9, pp. 10–11 · Table 7, p. 9 · App. I, p. 27
- block: `split 58:42` · 왼쪽 `figureNumbered`에 Fig. 7 한 장과 네 소재의 관찰 지점, 오른쪽 Table 9와 경로·차이 표기
- assets: Fig. 7, Table 9, 조건 대조용 Table 7
- interaction: none
- notes: 왼쪽은 512×512에서 직접 학습한 모델의 예시입니다. 같은 소재 안에서도 거북은 수중과 지상 장면으로, 등대는 서로 다른 시점과 조명으로 나타납니다. 오른쪽의 업샘플링 경로는 256토큰을 쓰는 확산 모델을 재사용하고 디코더의 출력 patch를 키웁니다. 이 경로는 직접 생성보다 토큰을 4분의 1만 쓰고, 표에서 gFID와 rFID는 각각 0.48과 0.44 높습니다.

### 18. 인코더 선택과 토큰 차원

- section: `scope`
- time: 60
- message: 이 비교에서는 가장 낮은 rFID를 얻은 인코더와 가장 낮은 gFID를 얻은 인코더가 다르고, DINOv2의 토큰 차원을 키운다고 gFID가 계속 낮아지지도 않습니다.
- on-slide facts:
  - **인코더 종류** · ImageNet 256×256, shift 적용 DiT-XL, 80 epoch, 무가이던스 50-step Euler · 증강 전 → 후, **gFID / rFID**
    - DINOv2-B · 4.81 → 4.28 / 0.49 → 0.57
    - SigLIP2-B · 6.69 → 4.93 / 0.53 → 0.82
    - MAE-B · 16.14 → 8.38 / 0.16 → 0.28
  - **DINOv2 크기** · 같은 생성 평가에서 노이즈 증강 디코더 사용, 기본 DDT head · **인코더(토큰 차원) / DiT-XL gFID / DiT^DH-XL gFID / ΔgFID**
    - S(384) · 3.50 / 2.42 / −1.08
    - B(768) · 4.28 / 2.16 / −2.12
    - L(1,024) · 6.09 / 2.73 / −3.36
  - §G.1의 판단 · 낮은 rFID만으로 좋은 생성용 tokenizer를 보장하기 어려움 · §5의 크기별 이점 · 개선폭은 L이 최대, DiT^DH-XL의 절대 gFID는 B가 최저
- source: §3, p. 4 · §5, Table 6, p. 8 · App. D, p. 24 · App. G.1–G.2, Table 15a/b, pp. 25–26 · 발표자 notes의 [external R6 — LV-RAE](https://arxiv.org/abs/2602.08620)
- block: `split 50:50` · 왼쪽 Table 15a의 gFID·rFID `table`, 오른쪽 Table 6·15b의 폭·gFID·Δ `table` · B의 절대값과 L의 개선폭에 각각 표시
- assets: 부록 Table 15a/b, Table 6
- interaction: none
- notes: 6번에서 rFID가 가장 낮았던 MAE-B는 노이즈 증강 뒤에도 세 인코더 중 생성 gFID가 가장 높습니다. 그래서 논문은 낮은 rFID만으로 생성용 tokenizer를 고르기 어렵다고 판단합니다. 저자들이 인코더가 커질수록 DiT^DH의 이점이 커진다고 한 것은 DiT-XL 대비 개선폭으로 확인할 수 있으며, 최종 gFID는 L의 2.73보다 B의 2.16이 낮습니다. 후속 연구인 LV-RAE는 의미 특징에서 색과 질감 정보가 부족해지는 현상을 복원의 병목으로 지적했습니다(external R6).

### 19. 입력별 DDT Head 비교

- section: `scope`
- time: 50
- message: DiT^DH 적용 후 SD-VAE에서는 gFID가 높아지고, 픽셀에서는 gFID가 낮아져도 같은 크기의 RAE 토큰과 큰 차이가 남습니다.
- on-slide facts: ImageNet 256×256, 80 epoch, 무가이던스 50-step Euler · **측정값은 gFID**, Δ는 DiT^DH-XL−DiT-XL(계산)

  | 항목 | SD-VAE | 픽셀 | DINOv2-B RAE |
  |---|---:|---:|---:|
  | DiT patch | 2 | 16 | 1 |
  | 토큰 수 × 차원 | \(256\times16\) | \(256\times768\) | \(256\times768\) |
  | DiT-XL | 7.13 | 51.09 | 4.28 |
  | DiT^DH-XL | 11.70 | 30.56 | 2.16 |
  | ΔgFID | +4.57 | −20.53 | −2.12 |

  - SD-VAE 토큰 차원 \(2\times2\times4=16\), 픽셀 토큰 차원 \(16\times16\times3=768\)(계산) · DiT와 DiT^DH에 서로 다른 최적화 레시피 적용
- source: §3, p. 3 · §6.2–6.3, Tables 10–11, p. 11 · App. D, p. 24
- block: 전폭 `table` 3개 데이터 열 · 하단 `note`에 DiT와 DiT^DH의 최적화 조건 차이
- assets: Tables 10–11, App. D의 patch·최적화 설정
- interaction: none
- notes: SD-VAE에서는 DiT^DH의 gFID가 7.13에서 11.70으로 높아집니다. 픽셀과 DINOv2-B RAE의 토큰 수와 차원을 맞추면 픽셀에서도 DiT^DH가 기본 DiT보다 낮은 gFID를 얻지만, 같은 DiT^DH에서 픽셀은 30.56이고 RAE는 2.16입니다. 따라서 이 실험에서 토큰 형태를 맞추는 것만으로는 RAE의 생성 성능을 재현할 수 없습니다. 표의 모델 간 차이에는 head와 함께 바뀐 최적화 설정도 포함됩니다.

### 20. 정리와 토론

- section: `discussion`
- time: 135
- message: 두 통념은 논문이 검증한 ImageNet 설정에서 반박되며, 평가 프로토콜과 설계 비용을 따져 보면 그 결과를 다른 설정에 적용할 범위가 드러납니다.
- on-slide facts:
  - **정리 ①** · 세 frozen encoder의 ImageNet 복원 · ViT 디코더 학습 후 SD-VAE보다 낮은 rFID
  - **정리 ②** · 고차원 DINOv2 RAE 확산 · 폭 조건, schedule shift, 디코더 증강, DiT^DH · 인코더와 입력 공간에 따라 달라지는 gFID
  1. **FID 프로토콜** · `kind: 근거`  
     Table 8 캡션의 재평가 baseline 상승 서술, Table 14의 짝지어진 random→balanced gFID 하락. ImageNet 256×256 무가이던스에서 SiT 8.61→8.54, REPA 5.90→5.78, REPA-E 1.83→1.70. Table 8의 SiT 8.61은 random 값. 800 epoch guided random에서는 DiT^DH-XL 1.28, REPA-E 1.26으로 balanced의 1.13 대 1.15와 순위가 바뀜.  
     **질문** · 두 모델을 동일 sampling 프로토콜로 반복 평가하면 guided 순위는 얼마나 안정적입니까?
  2. **Guidance 선택과 평가** · `kind: 근거`  
     ImageNet 256×256의 gFID 1.13 설정 · scale 1.42, guide DiT^DH-S 14 epoch checkpoint · FID를 설정 탐색과 최종 보고에 사용 · interval 없이 첫 step부터 CFG 적용 시 FID 악화.  
     `external` RAEv2는 원래 RAE의 CFG 적용이 어렵고 AutoGuidance에 더 약한 별도 diffusion 모델 학습이 필요하다고 보고. [R5 — RAEv2](https://arxiv.org/abs/2605.18324)  
     **질문** · scale과 guide checkpoint를 고정한 뒤 독립 샘플로 재평가해도 0.02의 gFID 차이가 유지됩니까?
  3. **Head와 최적화의 교차 비교** · `kind: 근거`  
     Tables 6·10·11의 DiT^DH 전용 설정 · learning rate \(2\times10^{-4}\)→\(2\times10^{-5}\) linear decay, 40 epoch warmup, EMA 0.9995, gradient clipping 1.0 · 기본 DiT는 constant learning rate \(2\times10^{-4}\), EMA 0.9999.  
     `external` 일부 저자가 겹치는 SigLIP-2 RAE text-to-image 후속 연구(0.5B–9.8B DiT)에서는 차원 의존 schedule이 여전히 중요했고, 큰 규모에서 wide head와 노이즈 증강 디코더의 이득은 미미하다고 보고. [R4 — Scaling Text-to-Image DiTs with RAE](https://arxiv.org/abs/2601.16208)  
     **질문** · head 유무와 두 최적화 레시피를 교차한 2×2 실험에서 각각의 gFID 효과는 얼마입니까?
  4. **Latent 캐시와 전송** · `kind: 대가` · 해석  
     256×256 이미지당 DINOv2-B RAE \(256\times768=196{,}608\) 원소, SD-VAE \(32\times32\times4=4{,}096\) 원소, 동일 정밀도·비압축 기준 48배(계산) · 캐시 용량·읽기·전송 비용 실측 부재.  
     `external` 원 DINOv2의 LVD-142M 구축에는 ImageNet-1k train split이 포함됨. **해석** · 동결 인코더의 사전학습 데이터도 ImageNet 결과를 해석할 때 고려할 조건. [R9 — DINOv2 §3](https://arxiv.org/abs/2304.07193)  
     **질문** · 인코더를 동결하고 latent를 캐시하는 실제 학습에서 저장·전송까지 합친 비용은 어떻게 달라집니까?
- source: §3–7, pp. 3–11 · Tables 6, 8, 10–11, pp. 8–11 · App. D–E, Table 14, pp. 24–25 · App. I, p. 27 · 각 항목의 `external` 출처
- block: 어두운 `statement` · 전폭 상단에 정리 2개, 하단 `cards` 2×2 · 비용 카드의 `note`에 해석 표시
- assets: Tables 8·14의 sampling 비교값, Tables 6·10·11의 모델 비교, App. D·I 설정
- interaction: none
- notes: 첫 번째 통념은 세 frozen encoder의 ImageNet 복원으로, 두 번째는 조건을 조정한 고차원 RAE 확산으로 반박했습니다. 토론의 첫 지점은 평가 프로토콜입니다. guided 결과의 순위가 random과 balanced에서 바뀌고, guidance 설정을 고를 때도 최종 보고와 같은 FID를 사용했습니다. 다음으로 head 유무와 최적화 레시피를 교차하면 어느 변경이 이득을 만드는지 살펴볼 수 있습니다. 끝으로 이미지당 latent 원소 수의 48배 차이가 실제 캐시 읽기와 전송을 포함한 학습 비용에서 어떻게 나타날지 토론하고 싶습니다.

### 21. 감사합니다 / Q&A

- section: `discussion`
- time: 15
- message: 두 통념을 검증한 실험과 그 적용 범위에 대해 질문받겠습니다.
- on-slide facts: 오희석(VILAB, 한성대학교) · [논문 arXiv:2510.11690v1](https://arxiv.org/abs/2510.11690v1) · `external` [프로젝트 페이지](https://rae-dit.github.io/) · `external` [공식 코드 · bytetriper/RAE](https://github.com/bytetriper/RAE)
- source: 논문 p. 1 · Research R1–R2
- block: 밝은 ending · 중앙 `lead`, 하단에 발표자와 링크
- assets: none
- interaction: none
- notes: 들어주셔서 감사합니다. 앞 장의 네 토론점이나 실험 설정에 대해 질문받겠습니다. 논문과 프로젝트, 공식 코드 링크는 화면에 남겨 두겠습니다.

## Not applied

- C3의 13·16번 `toggle` 제안은 적용하지 않았습니다. Fig. 4의 가로축은 epoch이고 Fig. 6b는 누적 학습 GFLOPs이므로 각각 14번과 15번에서 축을 유지합니다. 클리커로 조작하는 대표 인터랙션은 13번 `stepper` 한 개입니다.
- C5의 `split` 추가 축소는 목표 구조에 지정된 범위까지 반영했습니다. 3·4·13·20번은 전폭으로 배치했고, 10·11번은 수식과 대응 수치를 한 화면에서 읽도록 지정된 분할 배치를 유지했습니다.
- 초안의 Fig. 6c와 부록 Fig. 10·13은 제외했습니다. 15번은 Fig. 6a·b와 Table 6, 17번은 Fig. 7과 Table 9로 각 비교를 마칩니다.