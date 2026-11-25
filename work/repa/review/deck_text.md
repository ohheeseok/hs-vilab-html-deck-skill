# Deck text — Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think

## Slide 1 — Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think
[1.subtitle] Diffusion transformer의 중간 표현을 외부 인코더에 정렬하는 REPA
[1.figure.alt] Fig. 1 오른쪽. ImageNet 256×256에서 학습 step에 따른 FID-50K. SiT-XL/2 + REPA가 400K step에 vanilla SiT-XL/2의 7M step FID에 도달하며 17.5x faster로 표시된다.
[1.figure.caption] **Fig. 1** ImageNet 256×256, no CFG. 학습 step별 FID-50K
[1.notes.0] 오늘 소개할 논문은 KAIST와 NYU 연구진의 REPA입니다. ICLR 2025 oral 논문입니다.
[1.notes.1] 오른쪽 그림은 학습 step에 따른 생성 FID입니다. 이 차이가 어디서 오는지 보기 위해, 먼저 vanilla SiT가 어떤 표현을 배우는지부터 보겠습니다.

## Slide 2 — REPA 요약
[2.title] REPA 요약
[2.message] REPA는 noisy latent를 받는 SiT의 중간 표현을 같은 이미지의 clean DINOv2 표현에 patch마다 맞추는 정규화다.
[2.body.0.text] noisy latent를 받는 SiT의 layer 8 표현을, 같은 이미지의 clean 인코더 표현에 patch마다 맞춘다.
[2.body.1.items.0.title] 진단
[2.body.1.items.0.text] Vanilla SiT의 표현은 DINOv2-g보다 linear probe 정확도와 정렬이 낮다 (Fig. 2)
[2.body.1.items.1.title] 처방
[2.body.1.items.1.text] $\mathcal{L}=\mathcal{L}_{\mathrm{velocity}}+\lambda\,\mathcal{L}_{\mathrm{REPA}}$. 인코더와 MLP는 학습 때만 쓴다
[2.body.1.items.2.title] 결과
[2.notes.0] REPA는 같은 이미지의 clean patch 표현을 noisy latent를 받는 SiT의 중간 층에 학습 신호로 줍니다.
[2.notes.1] 논문은 먼저 vanilla SiT 표현이 DINOv2보다 약하다는 것을 측정하고, 그 격차를 줄이는 정렬 손실을 기존 손실에 더합니다. 인코더와 projector는 학습 때만 씁니다.
[2.notes.2] 대표 결과는 CFG 없이 평가한 ImageNet 256×256에서, REPA를 쓴 SiT-XL/2가 400K step에 vanilla의 7M step보다 낮은 FID를 기록한 것입니다.

## Slide 3 — REPA의 연구 배경
[3.title] REPA의 연구 배경
[3.message] REPA는 denoising transformer, 확산 모델 표현의 활용, 외부 표현을 쓰는 생성이라는 세 갈래가 만나는 곳에 있다.
[3.body.0.groups.0.items.1] transformer를 확산·flow 모델의 backbone으로
[3.body.0.groups.1.heading] 확산 모델의 내부 표현
[3.body.0.groups.1.items.1] 확산 모델이 배운 표현을 다른 과제에 활용
[3.body.0.groups.2.heading] 외부 표현을 쓰는 생성
[3.body.0.groups.2.items.1] 의미 표현을 먼저 만들고 그 위에서 생성
[3.body.1.text] 외부 표현에 정렬하면 수렴 속도와 생성 품질이 얼마나, 어떤 조건에서 바뀌는가?
[3.notes.0] U-ViT, DiT, SiT는 transformer를 denoising backbone으로 쓰는 흐름입니다.
[3.notes.1] RepFusion과 DreamTeacher는 확산 모델에서 배운 표현을 다른 과제에 씁니다. Würstchen과 RCG는 의미 표현을 먼저 만들고 그 위에서 생성합니다.
[3.notes.2] REPA는 외부 표현을 생성 모델의 학습 신호로 씁니다. 이 발표에서는 그 정렬이 수렴 속도와 생성 품질을 얼마나, 어떤 조건에서 바꾸는지 보겠습니다.

## Slide 4 — Vanilla SiT 표현의 분류 성능
[4.title] Vanilla SiT 표현의 분류 성능
[4.message] 7M step 학습한 vanilla SiT-XL/2도 분류에 쓸 표현을 배우지만, 가장 좋은 층도 DINOv2-g에 못 미친다.
[4.body.0.left.0.alt] Fig. 2(a). 층 번호에 따른 vanilla SiT-XL/2의 linear probe 정확도. t=0, 0.25, 0.5 세 곡선이 layer 20 부근에서 최고점을 찍고 내려가며, 모두 위쪽 DINOv2-g 점선보다 낮다.
[4.body.0.left.0.caption] **Fig. 2(a)** Vanilla SiT-XL/2, 7M step. 층별 ImageNet linear probe
[4.body.0.right.0.items.0] probe: 층 출력을 공간 평균한 뒤 linear classifier
[4.body.0.right.0.items.1] $t$ = 0, 0.25, 0.5 모두 layer 20 부근이 최고, 그 뒤 하락
[4.body.0.right.0.items.2] 모든 층이 DINOv2-g 기준선 아래
[4.body.0.right.1.text] 곡선을 읽은 서술이다 (표 수치 없음)
[4.notes.0] 각 층의 hidden state를 공간 방향으로 평균하고 linear classifier를 학습해 표현을 봅니다.
[4.notes.1] vanilla SiT의 정확도는 layer 20 부근에서 가장 높고 이후 떨어집니다. 저자들은 뒤쪽 층이 고주파 세부를 만드는 쪽으로 옮겨 가기 때문이라고 봅니다.
[4.notes.2] 그래도 가장 좋은 층이 DINOv2-g의 정확도에 크게 못 미칩니다. 논문은 이것을 semantic gap이라고 부릅니다.

## Slide 5 — SiT와 DINOv2의 표현 정렬
[5.title] SiT와 DINOv2의 표현 정렬
[5.message] Vanilla SiT의 DINOv2-g 정렬은 크고 오래 학습할수록 높아지지만, 7M step의 XL/2도 다른 자기지도 인코더 수준에 못 미친다.
[5.body.0.left.0.left.0.alt] Fig. 2(b). 층별 CKNNA. SiT의 t=0, 0.25, 0.5 곡선이 layer 20 부근에서 약 0.14로 가장 높고, MAE-L 점선은 넘지만 DINO-B와 MoCov3-B 점선보다 낮다.
[5.body.0.left.0.left.0.caption] **Fig. 2(b)** 층별 CKNNA
[5.body.0.left.0.right.0.alt] Fig. 2(c). 학습 step에 따른 CKNNA. SiT-B/2와 SiT-XL/2 모두 step이 늘수록 조금씩 높아지며 7M의 SiT-XL/2 점도 DINO-B 점선 아래에 있다.
[5.body.0.left.0.right.0.caption] **Fig. 2(c)** 학습 step별 CKNNA
[5.body.0.right.0.items.0] CKNNA: 두 표현 공간의 공통 최근접 이웃($k$ = 10)으로 정렬을 잰다. ImageNet val 10,000장
[5.body.0.right.0.items.1] 일부 층은 MAE-L보다 높고, DINO-B·MoCov3-B보다 낮다
[5.body.0.right.0.items.2] 크기와 step이 늘면 높아진다 (B/2는 400K까지)
[5.body.0.right.1.text] 기준 표현은 clean DINOv2-g. 곡선 근거
[5.notes.0] CKNNA는 두 표현 공간에서 공통으로 가까운 이웃을 세어 정렬을 측정합니다. 기준은 clean 이미지의 DINOv2-g입니다.
[5.notes.1] 왼쪽에서 SiT의 일부 층은 MAE-L보다 높지만 DINO-B와 MoCov3-B에는 못 미칩니다. 오른쪽에서 모델이 크고 학습이 길수록 정렬이 높아지지만, 7M step의 XL/2도 여전히 낮습니다.
[5.notes.2] 논문은 여기서 두 가지 어려움을 짚습니다. 인코더는 clean 이미지를, 확산 모델은 noisy latent를 받는다는 입력 차이입니다. 그래서 인코더를 그대로 붙이는 대신 정규화로 표현을 끌어오는 방법을 택합니다.

## Slide 6 — REPA의 학습 경로
[6.title] REPA의 학습 경로
[6.message] REPA는 같은 이미지의 clean patch token을 SiT layer 8에 붙인 MLP의 학습 목표로 쓰고, 추론에서는 그 경로를 떼어 낸다.
[6.body.0.reveals] 정렬 손실이 어느 층에서 갈라져 나가는지, 학습에만 쓰는 경로(인코더·MLP·REPA loss)와 추론 경로가 어떻게 다른지
[6.body.0.steps.0.text] clean 이미지 → 고정된 DINOv2-B → $y_*$
[6.body.0.steps.1.title] Noisy 입력
[6.body.0.steps.2.title] Layer 8 정렬
[6.body.0.steps.2.text] SiLU 3층 MLP $h_\phi$로 투영, 같은 patch끼리 유사도
[6.body.0.steps.3.title] 나머지 층과 loss
[6.body.0.steps.3.text] block 9–28이 velocity 예측, 두 loss를 함께
[6.body.0.steps.4.title] 추론
[6.body.0.steps.4.text] 인코더와 MLP 없이 SiT sampling → VAE decoder
[6.body.0.caption] Fig. 1 왼쪽을 다시 그림 · SiT-XL/2(28층)
[6.notes.0] [1] 위쪽 경로는 clean 이미지를 고정된 DINOv2-B에 넣어 patch token을 만듭니다. 이것이 정렬 목표입니다.
[6.notes.1] [2] 아래쪽은 원래의 확산 학습입니다. 같은 이미지의 VAE latent에 noise를 섞어 SiT에 넣고, 첫 여덟 block을 지나 layer 8의 hidden state를 얻습니다. 256×256 이미지에서 token은 256개입니다.
[6.notes.2] [3] Layer 8의 token을 3층 MLP로 인코더 차원에 투영하고, 같은 위치 patch끼리 유사도를 높입니다. [4] 나머지 block은 그대로 velocity를 예측하고, 두 loss를 함께 줄입니다.
[6.notes.3] [5] 생성할 때는 인코더와 MLP를 호출하지 않습니다. 추론 비용은 vanilla SiT와 같습니다.

## Slide 7 — REPA 손실과 학습 목적
[7.title] REPA 손실과 학습 목적
[7.message] REPA는 대응 patch의 유사도를 높이는 항을 기존 denoising loss에 λ로 가중해 더한다.
[7.body.0.symbols.0.1] clean 이미지의 $n$번째 patch token (인코더 출력)
[7.body.0.symbols.1.1] noisy 입력의 layer 8 token을 MLP로 투영
[7.body.0.symbols.2.1] cosine similarity 또는 NT-Xent
[7.body.0.symbols.3.1] SiT의 velocity 예측 loss (Eq. 4)
[7.body.0.symbols.4.1] 정렬 가중치. SiT 실험은 0.5
[7.body.1.text] DiT는 Improved DDPM 목적에 같은 항을 더한다 (Sec. 3.3)
[7.notes.0] 첫 식은 대응하는 patch마다 유사도를 구해 평균한 값에 음의 부호를 붙인 손실입니다. 손실을 줄이면 유사도가 높아집니다.
[7.notes.1] 두 번째 식처럼 이 항을 velocity loss에 λ배 해서 더합니다. SiT 실험은 λ를 0.5로 씁니다.
[7.notes.2] 유사도 함수는 cosine similarity와 NT-Xent 두 가지를 비교했고, DiT에서는 Improved DDPM 목적에 같은 항을 더합니다.

## Slide 8 — ImageNet 실험 설정
[8.title] ImageNet 실험 설정
[8.message] 주 실험은 ImageNet 256×256에서 같은 VAE latent와 batch 256을 쓰고, 정렬 층과 target은 모델 크기에 따라 다르다.
[8.body.0.left.0.columns.0.label] 모델
[8.body.0.left.0.columns.1.label] 층
[8.body.0.left.0.columns.4.label] 정렬 층
[8.body.0.left.0.columns.5.label] target · 목적
[8.body.0.left.1.text] **Table 1 · 7** 구조는 DiT·SiT와 같다. target · 목적은 Table 7의 표기
[8.body.0.right.0.groups.0.heading] 공통
[8.body.0.right.0.groups.1.heading] 평가
[8.notes.0] 주 실험은 ImageNet 256×256에서 Stable Diffusion VAE latent와 batch 256을 공통으로 씁니다.
[8.notes.1] 정렬은 B/2에서 layer 4, L/2와 XL/2에서 layer 8에 겁니다. target과 유사도 함수는 Table 7에 적힌 대로입니다.
[8.notes.2] 평가는 5만 장의 FID와 SDE sampler 250 step이 기본입니다.

## Slide 9 — REPA 적용 후 표현 지표
[9.title] REPA 적용 후 표현 지표
[9.message] Layer 8에 REPA를 건 SiT-XL/2는 모든 층에서 linear probe가 높고, DINOv2-g 정렬은 layer 8 부근에서 크게 높아진다.
[9.body.0.reveals] 같은 축에 그린 vanilla와 REPA를 패널마다 크게 보며, 분류 정확도와 정렬이 층별로 어디서 달라지는지
[9.body.0.states.0.label] 분류
[9.body.0.states.0.alt] Fig. 3(a). 층별 linear probe 정확도. SiT-XL/2 + REPA(빨강)가 layer 8에서 약 73%로 가장 높고 이후 조금씩 내려가며, 모든 층에서 vanilla SiT-XL/2(파랑)보다 높다.
[9.body.0.states.0.title] 층별 linear probe
[9.body.0.states.0.text] layer 4–24 전 구간에서 REPA가 vanilla보다 높다. DINOv2-g와의 격차가 줄어든다.
[9.body.0.states.1.label] 정렬
[9.body.0.states.1.alt] Fig. 3(b). 층별 DINOv2-g CKNNA. REPA는 layer 8에서 약 0.53으로 솟았다가 내려가 layer 20 이후에는 vanilla와 비슷하다.
[9.body.0.states.1.title] DINOv2-g와의 CKNNA
[9.body.0.states.1.text] layer 8 부근에서 가장 높고, layer 20–24에서는 vanilla와 비슷하거나 낮다.
[9.body.0.states.2.alt] Fig. 3(c). 가로축 validation 정확도, 세로축 FID-50K. REPA 궤적이 vanilla보다 오른쪽 아래에 있다.
[9.body.0.states.2.title] 생성과 분류를 함께
[9.body.0.states.2.text] 같은 학습 step에서 REPA가 validation Acc.는 높고 FID는 낮다.
[9.body.0.mediaCaption] **Fig. 3** REPA: SiT-XL/2, layer 8, DINOv2-B target, 1M step. 한 모델의 층별 평가
[9.body.0.caption] 패널마다 원래 축. CKNNA 축은 Fig. 2(b)가 0–0.3, Fig. 3(b)가 0–0.6이다
[9.notes.0] 진단에서 본 그림을 REPA 모델로 다시 그린 것이 Fig. 3입니다. 각 패널 안에 vanilla와 REPA가 같은 축으로 그려져 있습니다.
[9.notes.1] [1] Linear probe는 표시된 모든 층에서 REPA가 높습니다. [2] CKNNA는 정렬을 건 layer 8 부근에서 크게 높아지지만, 뒤쪽 layer 20 이후에는 vanilla와 비슷하거나 조금 낮습니다. 학습 target은 DINOv2-B이고, 평가 기준은 DINOv2-g입니다.
[9.notes.2] [3] 같은 학습 step에서 보면 분류 정확도와 생성 FID가 함께 좋아집니다. 참고로 CKNNA 축 범위는 Fig. 2와 다르니, Fig. 2와는 숫자로 비교해 주십시오.

## Slide 10 — SiT-XL/2의 학습 곡선
[10.title] SiT-XL/2의 학습 곡선
[10.message] CFG 없이 평가한 ImageNet 256×256에서 SiT-XL/2 + REPA는 400K step에 vanilla 7M step보다 낮은 FID를 기록한다.
[10.body.0.left.0.alt] Fig. 1 오른쪽. 학습 step에 따른 FID-50K. SiT-XL/2 + REPA(빨강)가 400K에서 7.9로, vanilla SiT-XL/2의 7M 값 8.3보다 낮다. 17.5x faster 화살표.
[10.body.0.right.0.items.0.label] 학습 step
[10.body.0.right.1.items.1] REPA는 1M에 6.4, 4M에 5.9
[10.notes.0] 두 모델은 모두 675M 파라미터의 SiT-XL/2이고 CFG 없이 평가했습니다.
[10.notes.1] Vanilla 7M step의 FID는 8.3, REPA 400K step의 FID는 7.9입니다. 17.5배는 이 두 checkpoint의 학습 step 비율입니다.
[10.notes.2] REPA는 더 학습하면 1M에 6.4, 4M에 5.9까지 내려갑니다.

## Slide 11 — DiT·SiT의 400K step 비교
[11.title] DiT·SiT의 400K step 비교
[11.message] 학습량을 400K step으로 맞추면 Table 3의 DiT·SiT 다섯 모델 모두 REPA 쪽 FID가 낮다.
[11.body.0.left.0.columns.0.label] 모델
[11.body.0.right.0.groups.0.heading] 다른 checkpoint 비교
[11.body.0.right.0.groups.0.items.1] step 비율 약 8.2×
[11.notes.0] 여기서는 모든 모델의 학습량을 400K step으로 맞췄습니다.
[11.notes.1] 다섯 모델 모두 REPA를 쓰면 FID가 낮고, SiT-XL/2에서는 9.3 내려갑니다.
[11.notes.2] DiT-XL/2에서는 vanilla 7M과 REPA 850K의 FID가 9.6으로 같습니다. 이 경우 step 비율은 약 8.2배입니다.

## Slide 12 — 초기 학습의 생성 예시
[12.title] 초기 학습의 생성 예시
[12.message] 같은 초기 noise에서 출발한 두 SiT-XL/2의 100K–400K 출력을 클래스마다 크게 비교한다.
[12.body.0.reveals] 같은 noise·sampler에서 REPA 쪽 물체 형태가 몇 step에 갖춰지는지를 클래스별로
[12.body.0.states.0.label] 앵무새
[12.body.0.states.0.alt] Fig. 4 일부. 앵무새. 위 SiT-XL/2, 아래 SiT-XL/2 + REPA, 열은 100K·200K·400K.
[12.body.0.states.0.title] 앵무새
[12.body.0.states.0.text] vanilla는 200K까지 머리 형태가 무너져 있다. REPA는 100K부터 눈과 부리가 있는 머리.
[12.body.0.states.1.label] 열기구
[12.body.0.states.1.alt] Fig. 4 일부. 열기구. 위 SiT-XL/2, 아래 SiT-XL/2 + REPA, 열은 100K·200K·400K.
[12.body.0.states.1.title] 열기구
[12.body.0.states.1.text] vanilla는 400K에도 풍선 아래 형체 없는 구조가 남는다. REPA는 200K에 하나의 열기구.
[12.body.0.states.2.label] 햄버거
[12.body.0.states.2.alt] Fig. 4 일부. 햄버거. 위 SiT-XL/2, 아래 SiT-XL/2 + REPA, 열은 100K·200K·400K.
[12.body.0.states.2.title] 햄버거
[12.body.0.states.2.text] vanilla는 400K에도 빵 두 덩이에 가깝다. REPA는 400K에 번·패티·감자튀김이 구분된다.
[12.body.0.mediaCaption] **Fig. 4** 같은 noise·sampler·step 수, no CFG. 클래스마다 원 그림을 잘라 다시 배치
[12.body.0.side.0.text] 탭의 관찰은 발표자가 그림을 읽은 것이다. 저자가 고른 예시
[12.notes.0] 두 모델은 같은 초기 noise, 같은 sampler와 step 수로 생성했고 CFG는 쓰지 않았습니다. 위가 vanilla, 아래가 REPA입니다.
[12.notes.1] [1] 앵무새는 vanilla가 200K까지 머리 모양이 무너져 있는데, REPA는 100K부터 눈과 부리가 있는 머리가 나옵니다. [2] 열기구는 vanilla가 400K에도 풍선 아래에 정체 모를 구조가 남고, REPA는 200K에 하나의 열기구가 됩니다.
[12.notes.2] [3] 햄버거는 400K에서 REPA 쪽에만 번과 패티, 감자튀김이 구분됩니다. 다만 이것은 제가 그림을 읽은 것이고, 저자가 고른 예시라는 점을 감안해 주십시오.

## Slide 13 — ImageNet CFG 시스템 비교
[13.title] ImageNet CFG 시스템 비교
[13.message] 같은 800 epochs REPA checkpoint에서 guidance interval은 일반 CFG보다 FID가 낮고 sFID는 높다.
[13.body.0.left.0.columns.0.label] 모델
[13.body.0.left.0.groups.0.label] Latent diffusion · 다른 방법
[13.body.0.left.1.text] **Table 4** ImageNet 256×256, CFG. * 추가 CFG 스케줄(REPA*는 guidance interval). 800 epochs = 4M step (batch 256)
[13.body.0.right.1.text] 같은 checkpoint의 sampling 설정 차이 (Table 10)
[13.notes.0] 표는 CFG를 쓴 시스템 비교이고, 별표는 추가 guidance 스케줄을 뜻합니다.
[13.notes.1] Vanilla SiT-XL/2는 1,400 epochs에 FID 2.06이고, REPA는 200 epochs에 1.96입니다. 800 epochs, batch 256 기준 4M step의 REPA는 일반 CFG에서 1.80, guidance interval을 쓰면 1.42입니다.
[13.notes.2] 같은 checkpoint인데 FID는 0.38 내려가고 sFID는 0.20 올라갑니다. 두 지표의 순위가 갈린다는 점은 토론에서 다시 다루겠습니다.

## Slide 14 — Target 인코더의 종류와 크기
[14.title] Target 인코더의 종류와 크기
[14.message] 정렬된 SiT의 분류 정확도가 높은 target일수록 FID가 낮고, DINOv2의 크기를 바꾼 차이는 0.3 이내다.
[14.body.0.left.0.alt] Fig. 5(a). 가로축 정렬된 SiT의 validation 정확도, 세로축 FID-50K. MAE-L, MoCov3-L, DINO-B, I-JEPA-H, CLIP-L, SigLIP-L, DINOv2-L 일곱 점이 오른쪽 아래로 내려가는 점선 근처에 놓인다.
[14.body.0.right.0.groups.0.heading] DINOv2 크기 (FID)
[14.body.0.right.0.groups.0.items.1] vanilla SiT-L/2는 18.8
[14.body.0.right.0.groups.1.heading] ImageNet 없이 학습한 인코더
[14.body.0.right.0.groups.1.items.1] 가장 좋은 DINOv2(LVD-142M)는 ImageNet-1K를 포함
[14.body.0.right.1.text] **Table 2 · 6** 같은 조건. 가로축은 인코더가 아니라 정렬된 SiT의 probe 정확도
[14.notes.0] 가로축은 인코더 자체의 정확도가 아니라, 정렬한 뒤 SiT의 linear probe 정확도입니다. 정확도가 높은 target일수록 FID가 낮아지는 경향입니다.
[14.notes.1] DINOv2만 놓고 크기를 B, L, g로 바꾸면 FID는 9.7에서 10.0 사이로 차이가 작습니다. 저자들은 세 모델이 모두 DINOv2-g에서 증류되었기 때문이라고 봅니다.
[14.notes.2] ImageNet을 쓰지 않은 CLIP과 SigLIP도 vanilla보다 FID가 크게 낮습니다. 다만 가장 좋은 DINOv2의 학습 데이터에는 ImageNet이 들어 있습니다.

## Slide 15 — 정렬 깊이
[15.title] 정렬 깊이
[15.message] SiT-L/2에서 FID는 layer 8에 정렬할 때 가장 낮고, 정렬한 층의 linear probe는 layer 16에서 가장 높다.
[15.body.0.left.0.columns.0.label] 정렬 층
[15.body.0.left.1.text] **Table 2** SiT-L/2, 400K, DINOv2-L, NT-Xent, $\lambda$ = 0.5, no CFG. 행마다 따로 학습
[15.body.0.right.0.items.0.small] layer 8 → 16, 나빠짐
[15.body.0.right.1.items.0] 저자의 가설: 나머지 층이 고주파 세부에 집중한다
[15.notes.0] 이 표의 각 행은 정렬 손실을 붙인 층이 다른, 따로 학습한 모델입니다.
[15.notes.1] Layer 8에서 16으로 옮기면 분류 정확도는 3.0 퍼센트포인트 오르지만 FID도 2.1 올라갑니다. 분류에 가장 좋은 깊이와 생성에 가장 좋은 깊이가 다릅니다.
[15.notes.2] 저자들은 앞쪽만 정렬하면 나머지 층이 고주파 세부에 집중할 수 있기 때문이라고 가설을 세웁니다.

## Slide 16 — 정렬 목적 함수와 λ
[16.title] 정렬 목적 함수와 λ
[16.message] 400K step에서 cosine과 NT-Xent의 FID 차이는 0.1이고, λ를 0.5보다 키울 때 FID는 최대 0.1 더 낮아진다.
[16.body.0.left.0.columns.0.label] 목적
[16.body.0.left.1.text] **Table 2** SiT-L/2, 400K, DINOv2-L, layer 8, no CFG. 50–100K에서는 NT-Xent가 유리, 이후 실험은 cosine (Sec. 4.2)
[16.body.0.right.1.text] **Table 5** SiT-XL/2, 400K, no CFG (Table 8과 같은 조건)
[16.notes.0] 왼쪽은 SiT-L/2에서 유사도 함수만 바꾼 결과입니다. 400K에서 cosine의 FID가 0.1 낮고, sFID는 NT-Xent가 낮습니다. 저자들은 50K에서 100K 사이에는 NT-Xent가 유리했다고 적고, 이후 실험에는 cosine을 씁니다.
[16.notes.1] 오른쪽은 SiT-XL/2의 별도 실험입니다. λ를 0.25에서 0.5로 올리면 FID가 0.7 내려가고, 그 뒤로는 0.1만 더 내려갑니다.

## Slide 17 — SiT 크기별 수렴
[17.title] SiT 크기별 수렴
[17.message] 같은 DINOv2-B target에서 SiT가 클수록 REPA 모델이 더 이른 step에 더 낮은 FID에 도달한다.
[17.body.0.left.0.alt] Fig. 5(b). 학습 step에 따른 FID-50K. SiT-B/2, L/2, XL/2 + REPA 세 곡선과 각 vanilla의 400K FID 수평선. 큰 모델일수록 vanilla 수평선에 더 일찍 닿는다.
[17.body.0.left.0.caption] **Fig. 5(b)** REPA 곡선. 수평선은 vanilla 400K FID
[17.body.0.right.0.alt] Fig. 5(c). 가로축 validation 정확도, 세로축 FID. 세 모델의 50K–400K 궤적이 오른쪽 아래로 내려가며 큰 모델의 기울기가 가파르다.
[17.notes.0] 왼쪽의 수평선은 vanilla 모델별 400K FID이고, 곡선은 REPA 모델 세 개입니다. 큰 모델일수록 vanilla의 400K 수준에 더 일찍 닿습니다.
[17.notes.1] 오른쪽은 같은 checkpoint에서 분류 정확도와 FID를 함께 그린 것으로, 큰 모델일수록 둘이 더 빨리 좋아집니다.
[17.notes.2] 200K에서 FID는 B/2가 33.2, L/2가 14.0, XL/2가 11.1입니다.

## Slide 18 — Noise 수준별 표현 격차
[18.title] Noise 수준별 표현 격차
[18.message] 시험한 세 timestep 모두에서 REPA를 쓴 SiT-XL/2의 linear probe와 최대 CKNNA가 vanilla보다 높다.
[18.body.0.left.0.alt] Fig. 7. t=0, 0.25, 0.5에서 vanilla SiT-XL/2(파랑)와 REPA(빨강)의 linear probe 정확도와 최대 CKNNA 막대. 모든 timestep에서 빨강이 높다.
[18.body.0.left.0.caption] **Fig. 7** SiT-XL/2. (a) linear probe (b) DINOv2-g와의 최대 CKNNA
[18.body.0.right.0.items.0] $t$ = 0, 0.25, 0.5 모두 REPA가 높다
[18.body.0.right.0.items.1] Fig. 8: MoCov3-L·MAE-L을 target으로 써도 layer 8 부근 CKNNA는 높다. 후반 층은 vanilla 기준선 아래
[18.body.0.right.1.text] 막대·곡선 근거. 비교 checkpoint의 step은 적혀 있지 않다
[18.notes.0] 입력 noise 수준을 세 가지로 바꿔 표현을 평가했습니다. 세 timestep 모두에서 REPA 모델의 분류 정확도와 최대 CKNNA가 높습니다.
[18.notes.1] Fig. 8에서 다른 인코더를 target으로 써도 정렬 층 부근은 높아지지만, 뒤쪽 층은 vanilla 기준선 아래로 내려갑니다. Fig. 8의 정렬 모델은 SiT-L/2이고 vanilla 기준은 SiT-XL/2입니다.

## Slide 19 — 해상도와 text-to-image 확장
[19.title] 해상도와 text-to-image 확장
[19.message] 부록에서 REPA는 ImageNet 512×512와 MS-COCO text-to-image에서도 FID를 낮추지만, 512×512의 일부 지표는 나아지지 않는다.
[19.body.0.items.0.text] SiT-XL/2, CFG $w$ = 1.35. FID 2.62(vanilla 600 ep) → 2.32(REPA 100 ep) → 2.08(200 ep). 200 ep의 sFID 4.19·Pre. 0.83은 vanilla 4.18·0.84보다 나쁘다
[19.body.0.items.1.text] MMDiT, 둘 다 150K step, SDE NFE 250, CFG $w$ = 2.0. FID 5.30 → 4.14
[19.body.1.text] **Table 11 · 12** pixel-space diffusion, video, 대규모 text-to-image는 후속 과제로 남김 (App. M)
[19.notes.0] ImageNet 512×512에서는 REPA 100 epochs의 FID가 2.32로, vanilla 600 epochs의 2.62보다 낮습니다.
[19.notes.1] 부록 본문은 네 지표가 모두 좋아졌다고 쓰지만, 200 epochs에서 sFID와 precision은 vanilla보다 조금 나쁩니다.
[19.notes.2] MS-COCO에서는 같은 150K step을 학습한 MMDiT끼리 비교해 FID가 5.30에서 4.14로 내려갑니다.

## Slide 20 — 정리와 토론
[20.title] 정리와 토론
[20.message] REPA는 step 대비 FID를 크게 줄였다. 무엇을, 어느 층에, 언제까지 정렬할지와 평가·비용의 근거는 더 따져 볼 수 있다.
[20.body.0.groups.0.heading] 정리
[20.body.0.groups.0.items.0] Vanilla SiT 표현은 DINOv2보다 약하다
[20.body.0.groups.0.items.1] clean 인코더 표현을 layer 8에 patch마다 정렬
[20.body.0.groups.0.items.2] ImageNet 256×256, no CFG: 400K step에 vanilla 7M 수준
[20.body.0.groups.1.heading] 토론
[20.body.0.groups.1.items.0] 깊이: layer 8→16에서 Acc. +3.0 pp, FID +2.1. iREPA는 전역 성능보다 공간 구조가 생성을 좌우한다고 보고했다. 무엇을 정렬해야 하나?
[20.body.0.groups.1.items.1] 평가: guidance interval을 FID로 골라 FID 1.42를 보고했다. sFID는 4.50 → 4.70. 고르는 데이터와 보고하는 데이터를 나눠도 순위가 같은가?
[20.body.0.groups.1.items.2] 기록: Table 3의 SiT-L/2 400K FID 9.7은 Table 2의 DINOv2-B 행과 같다. Table 7은 DINOv2-L로 적는다(10.0).
[20.body.0.groups.1.items.3.text] 비용: 인코더 forward가 늘지만 처리량은 5.4 step/s 하나뿐이다. 후반 층 정렬은 떨어지고(Fig. 3b·8), HASTE는 학습 후반 정체를 보고했다. 정렬은 언제까지 유지해야 하나?
[20.notes.0] 정리하면, 논문은 vanilla SiT의 표현이 약하다는 진단에서 출발해 clean 인코더 표현을 중간 층에 정렬했고, ImageNet 256×256에서 같은 FID에 훨씬 적은 step으로 도달했습니다.
[20.notes.1] 토론 주제는 네 가지입니다. 첫째, 깊이 실험에서 분류 정확도와 FID가 반대로 움직입니다. 작년 12월의 iREPA는 target의 전역 성능보다 공간 구조가 생성 성능을 좌우한다고 보고했습니다. 그렇다면 무엇을 정렬하는 것이 핵심인지 다시 물을 수 있습니다.
[20.notes.2] 둘째, guidance interval은 보고하는 지표와 같은 FID로 골랐고, sFID는 오히려 나빠졌습니다. 셋째, Table 3의 SiT-L/2 400K 수치가 Table 2에서 DINOv2-B 행과 같아, 어느 설정이 보고된 것인지 확인이 필요합니다.
[20.notes.3] 넷째는 제 해석입니다. 학습 중 인코더 forward 비용은 처리량 하나로만 보고되었습니다. 뒤쪽 층의 정렬은 떨어지고, HASTE는 학습 후반에 REPA가 정체한다고 보고했습니다. 같은 학습 시간 기준으로 정렬을 언제까지 유지할지 의견을 듣고 싶습니다.

## Slide 21 — 감사합니다
[21.title] 감사합니다
[21.links.1] 코드 · github.com/sihyun-yu/REPA (MIT)
[21.notes.0] 들어 주셔서 감사합니다. 논문과 코드 링크를 화면에 두었습니다. 질문과 의견을 받겠습니다.

