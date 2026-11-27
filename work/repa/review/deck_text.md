# Deck text — Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think

## Slide 1 — Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think
[1.subtitle] Diffusion transformer의 중간 표현을 외부 인코더에 정렬하는 REPA
[1.figure.alt] Fig. 1 오른쪽. ImageNet 256×256에서 학습 step에 따른 FID-50K. SiT-XL/2 + REPA가 400K step에 vanilla SiT-XL/2의 7M step FID에 도달하며 17.5x faster로 표시된다.
[1.figure.caption] **Fig. 1** ImageNet 256×256, no CFG. 학습 step별 FID-50K
[1.notes.0] 오늘 소개할 REPA는 KAIST·고려대·Scaled Foundations·NYU 연구진의 ICLR 2025 oral 논문입니다.
[1.notes.1] 오른쪽 그림은 학습 step에 따른 생성 FID를 보여 줍니다. vanilla SiT와 REPA를 적용한 SiT의 FID가 왜 다른지 알아보기 위해 먼저 vanilla SiT가 어떤 표현을 배우는지 보겠습니다.

## Slide 2 — REPA 요약
[2.title] REPA 요약
[2.message] REPA는 noisy latent를 받는 SiT의 중간 표현을 같은 이미지의 clean DINOv2 표현에 patch마다 정렬하는 정규화다.
[2.body.0.text] noisy latent를 받는 SiT의 중간 층(XL/2는 8층) 표현을 같은 이미지의 clean 인코더 표현에 patch마다 정렬한다.
[2.body.1.items.0.title] 진단
[2.body.1.items.0.text] Vanilla SiT는 DINOv2-g보다 linear probe 정확도가 낮고, DINOv2-g와의 정렬도 DINO-B·MoCov3-B보다 낮다 (Fig. 2)
[2.body.1.items.1.title] 처방
[2.body.1.items.1.text] $\mathcal{L}=\mathcal{L}_{\mathrm{velocity}}+\lambda\,\mathcal{L}_{\mathrm{REPA}}$. 인코더와 MLP는 학습 때만 쓴다
[2.body.1.items.2.title] 결과
[2.notes.0] REPA는 noisy latent를 받는 SiT의 중간 층을 학습할 때 같은 이미지의 clean patch 표현을 학습 신호로 씁니다.
[2.notes.1] 저자들은 먼저 vanilla SiT의 표현이 DINOv2보다 약하다는 점을 확인하고, 그 격차를 줄이려고 기존 loss에 정렬 loss를 더합니다.
[2.notes.2] 대표 결과를 보면, ImageNet 256×256에서 CFG 없이 평가했을 때 REPA를 쓴 SiT-XL/2의 400K step FID가 vanilla의 7M step FID보다 낮았습니다.

## Slide 3 — REPA의 연구 배경
[3.title] REPA의 연구 배경
[3.message] REPA와 관련된 연구 주제는 세 가지다. denoising transformer, 확산 모델이 배운 표현을 다른 과제에 쓰는 방법, 외부 표현을 써서 생성하는 방법이다.
[3.body.0.groups.0.items.1] transformer를 확산·flow 모델의 backbone으로
[3.body.0.groups.1.heading] 확산 모델의 내부 표현
[3.body.0.groups.1.items.1] 확산 모델이 배운 표현을 다른 과제에 사용
[3.body.0.groups.2.heading] 외부 표현을 쓰는 생성
[3.body.0.groups.2.items.1] 의미 표현을 먼저 만든 뒤 생성에 사용
[3.body.1.text] 외부 인코더를 생성 모델에 직접 붙이지 않고, 학습 신호로만 쓸 수 있는가?
[3.notes.0] U-ViT, DiT, SiT는 transformer를 denoising backbone으로 쓰는 모델입니다.
[3.notes.1] RepFusion과 DreamTeacher는 확산 모델에서 배운 표현을 다른 과제에 씁니다. Würstchen과 RCG는 의미 표현을 먼저 만든 뒤 생성에 씁니다.
[3.notes.2] REPA는 외부 표현을 생성 모델에 붙이지 않고 학습 신호로만 씁니다. 그 신호가 SiT의 어디에 더해지는지 다음 장에서 보겠습니다.

## Slide 4 — REPA가 SiT 학습에 더하는 것
[4.title] REPA가 SiT 학습에 더하는 것
[4.message] REPA는 SiT를 앞 8개 block과 뒤 20개 block으로 보고, 8번째 block의 출력을 같은 이미지의 깨끗한 DINOv2 패치 표현에 맞춘다. 이 정렬은 학습 때만 쓴다.
[4.body.0.reveals] 한 덩어리였던 SiT가 8층에서 나뉘고 그 출력에 정렬 경로가 붙는 것을 따라가면, REPA가 모델 구조는 그대로 두고 학습 신호 하나를 더한다는 것이 보인다.
[4.body.0.beats.0.text] 잡음 섞인 latent에서 velocity를 예측하며 표현도 함께 배운다
[4.body.0.beats.1.title] 깨끗한 이미지의 표현
[4.body.0.beats.1.text] 같은 이미지를 고정 DINOv2-B에 넣은 패치 표현. 입력이 다르다
[4.body.0.beats.2.title] 8층에 정렬
[4.body.0.beats.2.text] block 1–8 출력을 패치 표현에 맞춘다. 학습 때만 쓴다
[4.body.0.beats.3.title] 두 질문
[4.body.0.beats.3.text] ① 무엇을, 어느 층에 맞추나 ② 수렴과 생성 품질이 얼마나 바뀌나
[4.body.0.caption] **Fig. 1** 왼쪽과 Sec. 1·3.1·3.3을 바탕으로 그림. SiT-XL/2, 막대 길이는 block 수에 비례
[4.notes.0] 원래 SiT의 학습입니다. 이미지를 VAE로 압축하고 잡음을 섞은 latent를 28개 block에 통과시켜 velocity를 예측합니다. 생성에 쓰는 표현도 이 denoising 학습만으로 배웁니다.
[4.notes.1] [1] REPA는 같은 이미지를 깨끗한 상태로 고정된 DINOv2-B에 넣어 패치 표현을 얻습니다. 다만 DINOv2는 깨끗한 이미지를, SiT는 잡음 섞인 latent를 받습니다. 입력이 달라서 이 인코더를 SiT에 그대로 붙이기는 어렵습니다.
[4.notes.2] [2] 그래서 저자들은 SiT를 앞부분과 뒷부분으로 나눠 봅니다. XL/2에서는 8번째 block의 출력을 이 패치 표현에 맞추는 loss를 더합니다. 이 경로는 학습 때만 쓰고, 생성할 때는 원래 SiT 그대로입니다.
[4.notes.3] [3] 이 발표에서 볼 질문은 두 가지입니다. 무엇을 어느 층에 맞추는지, 그리고 수렴과 생성 품질이 얼마나 달라지는지입니다. 먼저 정렬하기 전의 SiT 표현이 DINOv2와 얼마나 다른지 보겠습니다.

## Slide 5 — Vanilla SiT 표현의 분류 성능
[5.title] Vanilla SiT 표현의 분류 성능
[5.message] 7M step 학습한 vanilla SiT-XL/2도 분류에 쓸 표현을 배우지만, 가장 좋은 층도 DINOv2-g에 못 미친다.
[5.body.0.left.0.alt] Fig. 2(a). 층 번호에 따른 vanilla SiT-XL/2의 linear probe 정확도. t=0, 0.25, 0.5 세 곡선이 20층 부근에서 최고점을 찍고 내려가며, 모두 위쪽 DINOv2-g 점선보다 낮다.
[5.body.0.left.0.caption] **Fig. 2(a)** Vanilla SiT-XL/2, 7M step. 층별 ImageNet linear probe
[5.body.0.right.0.items.0] probe에서 층 출력을 공간 방향으로 평균한 뒤 linear classifier 학습
[5.body.0.right.0.items.1] $t$ = 0, 0.25, 0.5 모두 20층 부근에서 정확도가 가장 높고 이후 낮아짐
[5.body.0.right.0.items.2] 모든 층이 DINOv2-g 기준선 아래
[5.body.0.right.1.text] 곡선에서 확인한 정확도 추이 (표 수치 없음)
[5.notes.0] 각 층의 hidden state를 공간 방향으로 평균하고 linear classifier를 학습해 표현을 평가합니다.
[5.notes.1] vanilla SiT의 정확도는 20층 부근에서 가장 높고 이후 떨어집니다. 저자들은 뒤쪽 층이 고주파 세부를 만드는 데 더 집중하기 때문이라고 봅니다.
[5.notes.2] 그래도 가장 좋은 층이 DINOv2-g의 정확도에 크게 못 미칩니다. 논문은 이것을 semantic gap이라고 부릅니다.

## Slide 6 — SiT와 DINOv2의 표현 정렬
[6.title] SiT와 DINOv2의 표현 정렬
[6.message] Vanilla SiT는 모델이 크고 학습 step이 많을수록 DINOv2-g와의 정렬이 높다. 7M step의 XL/2도 다른 자기지도 인코더 수준에는 못 미친다.
[6.body.0.left.0.left.0.alt] Fig. 2(b). 층별 CKNNA. SiT의 t=0, 0.25, 0.5 곡선이 20층 부근에서 가장 높고, MAE-L 점선은 넘지만 DINO-B와 MoCov3-B 점선보다 낮다.
[6.body.0.left.0.left.0.caption] **Fig. 2(b)** 층별 CKNNA
[6.body.0.left.0.right.0.alt] Fig. 2(c). 학습 step에 따른 CKNNA. SiT-B/2와 SiT-XL/2 모두 step이 늘수록 조금씩 높아지며 7M의 SiT-XL/2 점도 DINO-B 점선 아래에 있다.
[6.body.0.left.0.right.0.caption] **Fig. 2(c)** 학습 step별 CKNNA
[6.body.0.right.0.items.0] CKNNA: 공통 최근접 이웃 $k$ = 10개로 정렬 측정, ImageNet val 10,000장
[6.body.0.right.0.items.1] 일부 층은 MAE-L보다 높고, DINO-B·MoCov3-B보다 낮다
[6.body.0.right.0.items.2] 모델이 크고 학습 step이 많을수록 CKNNA가 높다 (B/2는 400K까지)
[6.body.0.right.1.text] 기준 표현은 clean DINOv2-g. 표 수치 없이 곡선에서 읽은 서술
[6.notes.0] CKNNA는 두 표현 공간의 공통 최근접 이웃을 세어 정렬을 측정합니다. 기준은 clean 이미지에서 얻은 DINOv2-g 표현입니다.
[6.notes.1] 왼쪽 그림에서 SiT 일부 층의 CKNNA는 MAE-L보다 높지만 DINO-B와 MoCov3-B보다 낮습니다. 오른쪽 그림에서는 모델이 크고 학습 step이 많을수록 정렬이 높아집니다. 그래도 7M step의 XL/2는 DINO-B보다 낮습니다.
[6.notes.2] 7M step을 학습해도 정렬은 이 수준에 머뭅니다. 앞에서 본 입력 차이 때문에 저자들은 인코더를 직접 붙이지 않고 정규화로 정렬합니다. 다음 장에서 그 학습 경로를 자세히 보겠습니다.

## Slide 7 — REPA의 학습 경로
[7.title] REPA의 학습 경로
[7.message] REPA는 SiT 8층 표현을 투영 MLP로 옮겨 같은 이미지의 clean patch token에 정렬한다. 추론에서는 인코더와 MLP를 쓰지 않는다.
[7.body.0.reveals] 단계를 넘기면 정렬 loss가 어느 층에 붙는지, 학습에만 쓰는 경로(인코더·MLP·REPA loss)와 추론 경로가 어떻게 다른지 보인다.
[7.body.0.steps.0.title] 두 경로
[7.body.0.steps.0.text] 위는 DINOv2-B의 $y_*$, 아래는 noisy latent가 block 1–8을 지난 $h_t$
[7.body.0.steps.1.title] 8층 정렬
[7.body.0.steps.1.text] SiLU 3층 MLP $h_\phi$로 투영, patch별 유사도
[7.body.0.steps.2.title] 나머지 층과 loss
[7.body.0.steps.2.text] block 9–28에서 velocity를 예측하고 두 loss를 함께 줄임
[7.body.0.steps.3.title] 추론
[7.body.0.steps.3.text] 인코더·MLP 없이 sampling → VAE decoder
[7.body.0.caption] **Fig. 1** 왼쪽을 다시 그림 · SiT-XL/2(28층)
[7.notes.0] [1] 앞 장에서 본 두 경로입니다. 위쪽은 clean 이미지를 고정된 DINOv2-B에 넣어 얻은 patch token으로, 정렬 목표입니다. 아래쪽은 같은 이미지의 VAE latent에 noise를 섞어 첫 여덟 block을 지난 8층 hidden state입니다. 256×256 이미지에서 token은 256개입니다.
[7.notes.1] [2] 8층의 token을 3층 MLP로 인코더 차원에 투영하고, 같은 위치의 patch끼리 유사도를 높입니다. [3] 나머지 block에서 기존 방식대로 velocity를 예측하고, 학습할 때는 두 loss를 함께 줄입니다.
[7.notes.2] [4] 생성할 때는 인코더와 MLP를 호출하지 않습니다. 추론 비용은 vanilla SiT와 같습니다.

## Slide 8 — REPA loss와 학습 목적
[8.title] REPA loss와 학습 목적
[8.message] REPA는 대응 patch의 유사도를 높이는 항에 λ를 곱해 기존 denoising loss에 더한다.
[8.body.0.symbols.0.1] clean 이미지의 $n$번째 patch token (인코더 출력)
[8.body.0.symbols.1.1] noisy 입력의 정렬 층(XL/2는 8층) token을 MLP로 투영
[8.body.0.symbols.2.1] cosine similarity 또는 NT-Xent
[8.body.0.symbols.3.1] SiT의 velocity 예측 loss (Eq. 4)
[8.body.0.symbols.4.1] 정렬 가중치. 기본 SiT 실험은 0.5
[8.body.1.text] DiT는 Improved DDPM 목적에 같은 항을 더한다 (Sec. 3.3)
[8.notes.0] 첫 식에서는 대응하는 patch마다 유사도를 구하고 평균에 음의 부호를 붙여 loss를 계산합니다. 이 loss를 줄이면 유사도가 높아집니다.
[8.notes.1] 두 번째 식처럼 이 항에 λ를 곱해 velocity loss에 더합니다. SiT 실험에서는 λ를 0.5로 둡니다.
[8.notes.2] 유사도 함수는 cosine similarity와 NT-Xent 두 가지를 비교했고, DiT에서는 Improved DDPM 목적에 같은 항을 더합니다.

## Slide 9 — ImageNet 실험 설정
[9.title] ImageNet 실험 설정
[9.message] 주 실험은 ImageNet 256×256에서 같은 VAE latent와 batch 256을 쓰고, 정렬 층과 target은 모델 크기에 따라 다르다.
[9.body.0.left.0.columns.0.label] 모델
[9.body.0.left.0.columns.1.label] 층
[9.body.0.left.0.columns.4.label] 정렬 층
[9.body.0.left.0.columns.5.label] target · 목적
[9.body.0.left.1.text] **Table 1 · 7** 구조는 DiT·SiT와 같다. target · 목적은 Table 7의 표기
[9.body.0.right.0.groups.0.heading] 공통
[9.body.0.right.0.groups.1.heading] 평가
[9.notes.0] 주 실험은 ImageNet 256×256에서 Stable Diffusion VAE latent와 batch 256을 공통으로 씁니다.
[9.notes.1] 정렬 loss는 B/2의 4층, L/2와 XL/2의 8층에 적용합니다. target과 유사도 함수는 Table 7에 적힌 대로입니다.
[9.notes.2] 기본 평가에서는 SDE sampler를 250 step 실행하고, 이미지 5만 장으로 FID를 계산합니다.

## Slide 10 — REPA 적용 후 표현 지표
[10.title] REPA 적용 후 표현 지표
[10.message] 8층에 REPA를 적용한 SiT-XL/2는 평가한 6–24층 모두에서 linear probe 정확도가 높고, DINOv2-g 정렬은 8층 부근에서 크게 높아진다.
[10.body.0.reveals] 패널을 하나씩 확대해 vanilla와 REPA를 같은 축에서 보면, 분류 정확도와 정렬이 어느 층에서 달라지는지 보인다.
[10.body.0.states.0.label] 분류
[10.body.0.states.0.alt] Fig. 3(a). 층별 linear probe 정확도. SiT-XL/2 + REPA(빨강)의 정확도는 8층에서 약 73%로 가장 높고 이후 조금씩 내려가며, 모든 층에서 vanilla SiT-XL/2(파랑)보다 높다.
[10.body.0.states.0.title] 층별 linear probe
[10.body.0.states.0.text] 평가한 6–24층 모두에서 REPA의 정확도가 vanilla보다 높다. DINOv2-g와의 격차가 줄어든다.
[10.body.0.states.1.label] 정렬
[10.body.0.states.1.alt] Fig. 3(b). DINOv2-g와의 층별 CKNNA. REPA는 8층에서 약 0.53으로 가장 높고 이후 낮아져 20–22층에서는 vanilla보다 낮고 24층에서는 다시 높다.
[10.body.0.states.1.title] DINOv2-g와의 CKNNA
[10.body.0.states.1.text] 8층 부근에서 가장 높다. 20–22층에서는 vanilla보다 낮고, 24층에서는 다시 높다.
[10.body.0.states.2.alt] Fig. 3(c). 가로축 validation 정확도, 세로축 FID-50K. REPA 궤적이 vanilla보다 오른쪽 아래에 있다.
[10.body.0.states.2.title] FID와 분류 정확도 비교
[10.body.0.states.2.text] 같은 학습 step에서 REPA는 vanilla보다 validation Acc.가 높고 FID가 낮다.
[10.body.0.mediaCaption] **Fig. 3** REPA: SiT-XL/2, 8층, DINOv2-B target. (a)(b) 1M step 층별 평가, (c) 학습 step 진행
[10.body.0.caption] 패널마다 원래 축. CKNNA 축 범위는 Fig. 2(b) 0–0.3, Fig. 3(b) 0–0.6
[10.notes.0] Fig. 3은 앞서 본 진단 그림에 REPA 모델의 결과를 추가한 그림입니다. 각 패널에서 vanilla와 REPA의 결과를 같은 축에 표시했습니다.
[10.notes.1] [1] 그림에 표시된 모든 층에서 REPA의 linear probe 정확도가 더 높습니다. [2] CKNNA는 정렬을 적용한 8층 부근에서 크게 높아지지만, 20–22층에서는 vanilla보다 낮고 24층에서는 다시 높습니다. 학습 target은 DINOv2-B이고, 평가 기준은 DINOv2-g입니다.
[10.notes.2] [3] 같은 학습 step에서 보면 분류 정확도와 생성 FID가 함께 좋아집니다. 참고로 CKNNA 축 범위는 Fig. 2와 다르니, Fig. 2와는 숫자로 비교해 주십시오.

## Slide 11 — SiT-XL/2의 학습 곡선
[11.title] SiT-XL/2의 학습 곡선
[11.message] ImageNet 256×256에서 CFG 없이 평가했을 때 SiT-XL/2 + REPA의 400K step FID는 vanilla의 7M step FID보다 낮다.
[11.body.0.left.0.alt] Fig. 1 오른쪽. 학습 step에 따른 FID-50K. SiT-XL/2 + REPA(빨강)가 400K에서 7.9로, vanilla SiT-XL/2의 7M 값 8.3보다 낮다. 17.5x faster 화살표.
[11.body.0.right.0.items.0.label] 학습 step
[11.body.0.right.1.items.1] REPA는 1M에 6.4, 4M에 5.9
[11.notes.0] 두 모델은 모두 675M 파라미터의 SiT-XL/2이고 CFG 없이 평가했습니다.
[11.notes.1] Vanilla 7M step의 FID는 8.3, REPA 400K step의 FID는 7.9입니다. 17.5배는 이 두 checkpoint의 학습 step 비율입니다.
[11.notes.2] REPA 모델을 더 학습하면 FID는 1M에 6.4, 4M에 5.9까지 내려갑니다.

## Slide 12 — DiT·SiT의 400K step 비교
[12.title] DiT·SiT의 400K step 비교
[12.message] 학습량을 400K step으로 맞추면 Table 3의 DiT·SiT 다섯 모델 모두 REPA 쪽 FID가 낮다.
[12.body.0.left.0.columns.0.label] 모델
[12.body.0.right.0.groups.0.heading] 다른 checkpoint 비교
[12.body.0.right.0.groups.0.items.0] DiT-XL/2: vanilla 7M과 REPA 850K 모두 FID 9.6
[12.body.0.right.0.groups.0.items.1] step 비율 약 8.2×
[12.notes.0] 여기서는 모든 모델의 학습량을 400K step으로 맞췄습니다.
[12.notes.1] 다섯 모델 모두 REPA를 쓰면 FID가 낮고, SiT-XL/2에서는 9.3 내려갑니다.
[12.notes.2] DiT-XL/2에서는 vanilla 7M과 REPA 850K의 FID가 9.6으로 같습니다. 이 경우 step 비율은 약 8.2배입니다.

## Slide 13 — 초기 학습의 생성 예시
[13.title] 초기 학습의 생성 예시
[13.message] 같은 초기 noise로 생성한 두 SiT-XL/2의 100K–400K 출력을 클래스마다 확대해 비교한다.
[13.body.0.reveals] 같은 noise·sampler 조건에서 클래스별로 보면, REPA 출력에서 물체 형태가 어느 step부터 갖춰지는지 비교할 수 있다.
[13.body.0.states.0.label] 앵무새
[13.body.0.states.0.alt] Fig. 4 일부. 앵무새. 위 SiT-XL/2, 아래 SiT-XL/2 + REPA, 열은 100K·200K·400K.
[13.body.0.states.0.title] 앵무새
[13.body.0.states.0.text] vanilla에서는 200K까지 머리 형태가 제대로 나오지 않는다. REPA에서는 100K부터 눈과 부리가 있는 머리가 나온다.
[13.body.0.states.1.label] 열기구
[13.body.0.states.1.alt] Fig. 4 일부. 열기구. 위 SiT-XL/2, 아래 SiT-XL/2 + REPA, 열은 100K·200K·400K.
[13.body.0.states.1.title] 열기구
[13.body.0.states.1.text] vanilla에서는 400K에도 풍선 아래에 형체가 뚜렷하지 않은 구조가 남는다. REPA에서는 200K에 온전한 열기구 형태가 나온다.
[13.body.0.states.2.label] 햄버거
[13.body.0.states.2.alt] Fig. 4 일부. 햄버거. 위 SiT-XL/2, 아래 SiT-XL/2 + REPA, 열은 100K·200K·400K.
[13.body.0.states.2.title] 햄버거
[13.body.0.states.2.text] vanilla는 400K에도 빵 두 덩이에 가깝다. REPA는 400K에 번·패티·감자튀김이 구분된다.
[13.body.0.mediaCaption] **Fig. 4** 같은 noise·sampler·step 수, no CFG. 클래스마다 원 그림을 잘라 다시 배치
[13.body.0.side.0.text] 저자가 고른 생성 예시에 대한 발표자의 해석
[13.notes.0] 두 모델은 같은 초기 noise, 같은 sampler와 step 수로 생성했고 CFG는 쓰지 않았습니다. 위가 vanilla, 아래가 REPA입니다.
[13.notes.1] [1] 앵무새는 vanilla에서 200K까지 머리 모양이 제대로 나오지 않습니다. REPA에서는 100K부터 눈과 부리가 있는 머리가 나옵니다. [2] 열기구는 vanilla에서 400K에도 풍선 아래에 형태를 알아보기 어려운 구조가 남습니다. REPA에서는 200K에 온전한 열기구 형태가 나옵니다.
[13.notes.2] [3] 햄버거는 400K에서 REPA 쪽에만 번과 패티, 감자튀김이 구분됩니다. 다만 이 관찰은 제 해석입니다. 저자가 고른 예시라는 점도 감안해 주십시오.

## Slide 14 — ImageNet CFG 시스템 비교
[14.title] ImageNet CFG 시스템 비교
[14.message] 같은 800 epochs REPA checkpoint에서 guidance interval은 일반 CFG보다 FID가 낮고 sFID는 높다.
[14.body.0.left.0.columns.0.label] 모델
[14.body.0.left.0.groups.0.label] Latent diffusion · 다른 방법
[14.body.0.left.1.text] **Table 4** ImageNet 256×256, CFG. * 추가 CFG 스케줄(REPA*는 guidance interval). 800 epochs = 4M step (batch 256)
[14.body.0.right.1.text] 같은 checkpoint에서 sampling 설정만 바꾼 결과 (Table 9·10)
[14.notes.0] 표는 CFG를 쓴 시스템 비교이고, 별표는 추가 guidance 스케줄을 뜻합니다.
[14.notes.1] Vanilla SiT-XL/2는 1,400 epochs에 FID 2.06이고, REPA는 200 epochs에 1.96입니다. 800 epochs, batch 256 기준 4M step의 REPA는 일반 CFG에서 1.80, guidance interval을 쓰면 1.42입니다.
[14.notes.2] 같은 checkpoint인데 FID는 0.38 내려가고 sFID는 0.20 올라갑니다. 두 지표의 순위가 갈린다는 점은 토론에서 다시 다루겠습니다.

## Slide 15 — Target 인코더의 종류와 크기
[15.title] Target 인코더의 종류와 크기
[15.message] SiT를 정렬한 뒤 분류 정확도가 높게 나온 target일수록 FID가 낮다. DINOv2 크기에 따른 FID 차이는 0.3 이내다.
[15.body.0.left.0.alt] Fig. 5(a). 가로축 정렬된 SiT의 validation 정확도, 세로축 FID-50K. MAE-L, MoCov3-L, DINO-B, I-JEPA-H, CLIP-L, SigLIP-L, DINOv2-L 일곱 점이 오른쪽 아래 방향으로 분포한다.
[15.body.0.right.0.groups.0.heading] DINOv2 크기 (FID)
[15.body.0.right.0.groups.0.items.1] vanilla SiT-L/2는 18.8
[15.body.0.right.0.groups.1.heading] ImageNet 없이 학습한 인코더
[15.body.0.right.0.groups.1.items.1] 가장 좋은 DINOv2(LVD-142M)의 학습 데이터에 ImageNet-1K 포함
[15.body.0.right.1.text] **Table 2 · 6** 같은 조건. 가로축은 인코더가 아니라 정렬된 SiT의 probe 정확도
[15.notes.0] 가로축은 인코더 자체의 정확도가 아니라, 정렬한 뒤 SiT의 linear probe 정확도입니다. 정확도가 높은 target일수록 FID가 낮아지는 경향입니다.
[15.notes.1] DINOv2만 놓고 크기를 B, L, g로 바꾸면 FID는 9.7에서 10.0 사이로 차이가 작습니다. 저자들은 세 모델이 모두 DINOv2-g에서 증류되었기 때문이라고 봅니다.
[15.notes.2] ImageNet을 쓰지 않은 CLIP과 SigLIP도 vanilla보다 FID가 크게 낮습니다. 다만 가장 좋은 DINOv2의 학습 데이터에는 ImageNet이 들어 있습니다.

## Slide 16 — 정렬 층
[16.title] 정렬 층
[16.message] SiT-L/2에서 FID는 8층에 정렬을 적용했을 때 가장 낮다. 정렬한 층의 linear probe 정확도는 16층에 정렬을 적용했을 때 가장 높다.
[16.body.0.left.0.columns.0.label] 정렬 층
[16.body.0.left.1.text] **Table 2** SiT-L/2, 400K, DINOv2-L, NT-Xent, $\lambda$ = 0.5, no CFG. 행마다 따로 학습
[16.body.0.right.0.items.0.small] 8층 → 16층에서 FID 악화
[16.body.0.right.0.items.1.small] 8층 → 16층
[16.body.0.right.1.items.0] 저자의 가설: 나머지 층이 고주파 세부에 집중한다
[16.notes.0] 표의 각 행은 서로 다른 층에 정렬 loss를 적용해 따로 학습한 모델에 해당합니다.
[16.notes.1] 정렬 층을 8층에서 16층으로 바꾸면 분류 정확도는 3.0 퍼센트포인트 오르지만 FID도 2.1 올라갑니다. 분류 성능이 가장 좋은 정렬 층과 생성 성능이 가장 좋은 정렬 층이 다릅니다.
[16.notes.2] 저자들은 앞쪽만 정렬하면 나머지 층이 고주파 세부에 집중할 수 있기 때문이라고 가설을 세웁니다.

## Slide 17 — 정렬 목적 함수와 λ
[17.title] 정렬 목적 함수와 λ
[17.message] 400K step에서 cosine과 NT-Xent의 FID 차이는 0.1이고, λ를 0.5보다 키울 때 FID는 최대 0.1 더 낮아진다.
[17.body.0.left.0.columns.0.label] 목적
[17.body.0.left.1.text] **Table 2** SiT-L/2, 400K, DINOv2-L, 8층, no CFG. 50–100K에서는 NT-Xent가 유리하며 이후 실험에서는 cosine 사용 (Sec. 4.2)
[17.body.0.right.1.text] **Table 5** SiT-XL/2, 400K, no CFG (Table 8과 같은 조건)
[17.notes.0] 왼쪽은 SiT-L/2에서 유사도 함수만 바꾼 결과입니다. 400K에서 cosine의 FID가 0.1 낮고, sFID는 NT-Xent가 낮습니다. 저자들은 50K에서 100K 사이에는 NT-Xent가 유리했다고 적고, 이후 실험에는 cosine을 씁니다.
[17.notes.1] 오른쪽은 SiT-XL/2의 별도 실험입니다. λ를 0.25에서 0.5로 올리면 FID가 0.7 내려가고, 그 뒤로는 0.1만 더 내려갑니다.

## Slide 18 — SiT 크기별 수렴
[18.title] SiT 크기별 수렴
[18.message] 같은 DINOv2-B target에서 SiT가 클수록 REPA 모델이 더 이른 step에 더 낮은 FID에 도달한다.
[18.body.0.left.0.alt] Fig. 5(b). 학습 step에 따른 FID-50K. SiT-B/2, L/2, XL/2 + REPA 세 곡선과 각 vanilla의 400K FID 수평선. 큰 모델일수록 vanilla 수평선에 더 일찍 닿는다.
[18.body.0.left.0.caption] **Fig. 5(b)** REPA 곡선. 수평선은 vanilla 400K FID
[18.body.0.right.0.alt] Fig. 5(c). 가로축 validation 정확도, 세로축 FID. 세 모델의 50K–400K 궤적이 오른쪽 아래로 내려가며 큰 모델의 기울기가 가파르다.
[18.notes.0] 왼쪽의 수평선은 vanilla 모델별 400K FID이고, 곡선은 REPA 모델 세 개입니다. 큰 모델일수록 vanilla의 400K 수준에 더 일찍 닿습니다.
[18.notes.1] 오른쪽에는 같은 checkpoint의 분류 정확도와 FID를 함께 그렸습니다. 모델이 클수록 분류 정확도가 더 빨리 높아지고 FID는 더 빨리 낮아집니다.
[18.notes.2] 200K에서 FID는 B/2가 33.2, L/2가 14.0, XL/2가 11.1입니다.

## Slide 19 — noise 수준별 표현 격차
[19.title] noise 수준별 표현 격차
[19.message] 시험한 세 timestep 모두에서 REPA를 쓴 SiT-XL/2의 linear probe 정확도와 최대 CKNNA가 vanilla보다 높다.
[19.body.0.alt] Fig. 7. t=0, 0.25, 0.5에서 vanilla SiT-XL/2(파랑)와 REPA(빨강)의 linear probe 정확도와 최대 CKNNA 막대. 모든 timestep에서 빨강이 높다.
[19.body.0.caption] **Fig. 7** SiT-XL/2. (a) linear probe (b) DINOv2-g와의 최대 CKNNA. 막대·곡선에서 읽은 서술, 비교 checkpoint의 step은 적혀 있지 않다
[19.body.1.items.0] $t$ = 0, 0.25, 0.5 모두 REPA가 높다
[19.body.1.items.1] Fig. 8: MoCov3-L·MAE-L을 target으로 써도 8층 부근 CKNNA가 높다. 후반 층으로 갈수록 낮아져 MoCov3-L은 vanilla 기준선 아래
[19.notes.0] 입력 noise 수준을 세 가지로 바꿔 표현을 평가했습니다. 세 timestep 모두에서 REPA 모델의 분류 정확도와 최대 CKNNA가 높습니다.
[19.notes.1] Fig. 8에서 다른 인코더를 target으로 써도 정렬 층 부근의 CKNNA는 높아지고, 뒤쪽 층으로 갈수록 낮아집니다. MoCov3-L은 vanilla 기준선 아래로 내려가고 MAE-L은 마지막 층에서 기준선 부근에 닿습니다. Fig. 8의 정렬 모델은 SiT-L/2이고 vanilla 기준은 SiT-XL/2입니다.

## Slide 20 — 해상도와 text-to-image 확장
[20.title] 해상도와 text-to-image 확장
[20.message] 부록에서 REPA는 ImageNet 512×512와 MS-COCO text-to-image에서도 FID를 낮추지만, 512×512의 일부 지표는 나아지지 않는다.
[20.body.0.items.0.text] SiT-XL/2, CFG $w$ = 1.35. FID 2.62(vanilla 600 ep) → 2.32(REPA 100 ep) → 2.08(200 ep). 200 ep의 sFID 4.19·Pre. 0.83은 vanilla 4.18·0.84보다 나쁘다
[20.body.0.items.1.text] MMDiT, 둘 다 150K step, SDE NFE 250, CFG $w$ = 2.0. FID 5.30 → 4.14
[20.body.1.text] **Table 11 · 12** pixel-space diffusion, video, 대규모 text-to-image는 후속 과제로 남김 (App. M)
[20.notes.0] ImageNet 512×512에서는 REPA 100 epochs의 FID가 2.32로, vanilla 600 epochs의 2.62보다 낮습니다.
[20.notes.1] 부록 본문은 네 지표가 모두 좋아졌다고 쓰지만, 200 epochs에서 sFID와 precision은 vanilla보다 조금 나쁩니다.
[20.notes.2] MS-COCO에서는 같은 150K step을 학습한 MMDiT끼리 비교해 FID가 5.30에서 4.14로 내려갑니다.

## Slide 21 — 정리와 토론
[21.title] 정리와 토론
[21.message] 학습 step 기준으로 비교하면 REPA는 FID를 크게 낮췄다. 다만 무엇을 어느 층에 정렬할지, 정렬을 언제까지 유지할지, 보고한 수치의 근거와 비용은 더 따져 볼 수 있다.
[21.body.0.groups.0.heading] 정리
[21.body.0.groups.0.items.0] Vanilla SiT의 표현은 DINOv2보다 linear probe 정확도와 정렬이 낮다
[21.body.0.groups.0.items.1] 깨끗한 이미지의 인코더 표현에 SiT 8층 출력을 patch마다 맞춘다
[21.body.0.groups.0.items.2] ImageNet 256×256, CFG 없이: 400K step으로 vanilla 7M step보다 낮은 FID
[21.body.0.groups.1.heading] 토론
[21.body.0.groups.1.items.0] **정렬 층**: 8층 대신 16층에 정렬하면 분류 정확도는 오르고 FID는 나빠진다. 생성에는 무엇을 정렬해야 하나?
[21.body.0.groups.1.items.1] **수치 선택**: 1.42는 Table 10의 설정 가운데 FID가 가장 낮은 것이다. 설정을 고른 데이터와 결과를 보고한 데이터가 같아도 되나?
[21.body.0.groups.1.items.2] **표 기록**: Table 3의 SiT-L/2 400K 수치(9.7)는 Table 2의 DINOv2-B 행과 같은데, Table 7은 DINOv2-L로 적는다. 어느 설정인가?
[21.body.0.groups.1.items.3.text] **비용**: 학습 중 인코더 forward 비용이 들고, 학습 후반에 REPA가 정체한다는 보고가 있다. 정렬은 언제까지 유지해야 하나?
[21.notes.0] 저자들은 vanilla SiT의 표현이 약하다는 진단을 바탕으로 clean 인코더 표현을 SiT의 중간 층에 정렬했습니다. ImageNet 256×256에서 같은 FID까지 필요한 학습 step은 훨씬 적었습니다.
[21.notes.1] 토론 주제는 네 가지입니다. 첫째, 정렬 층을 비교한 실험에서 분류 정확도는 좋아지고 FID는 나빠졌습니다. 작년 12월에 나온 iREPA 논문은 target의 전역 성능보다 공간 구조가 생성 성능을 좌우한다고 보고했습니다. 그렇다면 무엇을 정렬하는 게 가장 중요할까요?
[21.notes.2] 둘째, Table 10은 guidance interval과 w의 조합마다 FID를 보고하고, Table 4에는 그중 가장 낮은 1.42를 실었습니다. 이때 sFID는 4.50에서 4.70으로 나빠집니다. 셋째, Table 3의 SiT-L/2 400K 수치 9.7은 Table 2의 DINOv2-B 행과 같고, Table 7은 DINOv2-L로 적습니다. 어느 설정으로 얻은 수치인지 확인해야 합니다.
[21.notes.3] 넷째는 제 해석입니다. 논문에서 학습 중 인코더 forward 비용과 관련해 보고한 수치는 처리량 하나뿐입니다. 뒤쪽 층의 정렬은 떨어지고, HASTE는 학습 후반에 REPA가 정체한다고 보고했습니다. 학습 시간을 같게 두고 비교할 때 정렬을 언제까지 유지할지 의견을 듣고 싶습니다.

## Slide 22 — 감사합니다
[22.title] 감사합니다
[22.links.1] 코드 · github.com/sihyun-yu/REPA (MIT)
[22.notes.0] 들어 주셔서 감사합니다. 논문과 코드 링크를 화면에 두었습니다. 질문과 의견을 받겠습니다.

