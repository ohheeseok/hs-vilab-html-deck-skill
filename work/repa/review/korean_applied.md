| location | original | edit | rule |
|---|---|---|---|
| 1.notes.0 | 오늘 소개할 논문은 KAIST와 NYU 연구진의 REPA입니다. ICLR 2025 oral 논문입니다. | 오늘 소개할 REPA는 KAIST와 NYU 연구진의 ICLR 2025 oral 논문입니다. | L1-8 |
| 1.notes.1 | 오른쪽 그림은 학습 step에 따른 생성 FID입니다. 이 차이가 어디서 오는지 보기 위해, 먼저 vanilla SiT가 어떤 표현을 배우는지부터 보겠습니다. | 오른쪽 그림은 학습 step에 따른 생성 FID를 보여 줍니다. vanilla SiT와 REPA를 적용한 SiT의 FID가 왜 다른지 알아보기 위해 먼저 vanilla SiT가 어떤 표현을 배우는지 보겠습니다. | L1-11, L1-8 |
| 2.message | REPA는 noisy latent를 받는 SiT의 중간 표현을 같은 이미지의 clean DINOv2 표현에 patch마다 맞추는 정규화다. | REPA는 noisy latent를 받는 SiT의 중간 표현을 같은 이미지의 clean DINOv2 표현에 patch마다 정렬하는 정규화다. | L1-8 |
| 2.body.0.text | noisy latent를 받는 SiT의 layer 8 표현을, 같은 이미지의 clean 인코더 표현에 patch마다 맞춘다. | noisy latent를 받는 SiT의 8층 표현을 같은 이미지의 clean 인코더 표현에 patch마다 정렬한다. | L1-8 |
| 2.notes.0 | REPA는 같은 이미지의 clean patch 표현을 noisy latent를 받는 SiT의 중간 층에 학습 신호로 줍니다. | REPA는 noisy latent를 받는 SiT의 중간 층을 학습할 때 같은 이미지의 clean patch 표현을 학습 신호로 씁니다. | L3-2 |
| 2.notes.1 | 논문은 먼저 vanilla SiT 표현이 DINOv2보다 약하다는 것을 측정하고, 그 격차를 줄이는 정렬 손실을 기존 손실에 더합니다. 인코더와 projector는 학습 때만 씁니다. | 저자들은 먼저 vanilla SiT와 DINOv2의 표현을 평가해 vanilla SiT의 표현이 더 약하다는 점을 확인합니다. 그 격차를 줄이기 위해 기존 loss에 정렬 loss를 더합니다. 인코더와 projector는 학습 때만 씁니다. | L3-2, L1-8 |
| 2.notes.2 | 대표 결과는 CFG 없이 평가한 ImageNet 256×256에서, REPA를 쓴 SiT-XL/2가 400K step에 vanilla의 7M step보다 낮은 FID를 기록한 것입니다. | 대표 결과를 보면, ImageNet 256×256에서 CFG 없이 평가했을 때 REPA를 쓴 SiT-XL/2의 400K step FID가 vanilla의 7M step FID보다 낮았습니다. | L1-8 |
| 3.message | REPA는 denoising transformer, 확산 모델 표현의 활용, 외부 표현을 쓰는 생성이라는 세 갈래가 만나는 곳에 있다. | REPA와 관련된 연구 주제는 세 가지다. denoising transformer, 확산 모델이 배운 표현을 다른 과제에 쓰는 방법, 외부 표현을 써서 생성하는 방법이다. | L2-2, L1-8 |
| 3.body.0.groups.1.items.1 | 확산 모델이 배운 표현을 다른 과제에 활용 | 확산 모델이 배운 표현을 다른 과제에 사용 | L1-8 |
| 3.body.0.groups.2.items.1 | 의미 표현을 먼저 만들고 그 위에서 생성 | 의미 표현을 먼저 만든 뒤 생성에 사용 | L2-1 |
| 3.notes.0 | U-ViT, DiT, SiT는 transformer를 denoising backbone으로 쓰는 흐름입니다. | U-ViT, DiT, SiT는 transformer를 denoising backbone으로 쓰는 모델입니다. | L3-2 |
| 3.notes.1 | RepFusion과 DreamTeacher는 확산 모델에서 배운 표현을 다른 과제에 씁니다. Würstchen과 RCG는 의미 표현을 먼저 만들고 그 위에서 생성합니다. | RepFusion과 DreamTeacher는 확산 모델에서 배운 표현을 다른 과제에 씁니다. Würstchen과 RCG는 의미 표현을 먼저 만든 뒤 생성에 씁니다. | L2-1 |
| 3.notes.2 | REPA는 외부 표현을 생성 모델의 학습 신호로 씁니다. 이 발표에서는 그 정렬이 수렴 속도와 생성 품질을 얼마나, 어떤 조건에서 바꾸는지 보겠습니다. | REPA는 외부 표현을 생성 모델의 학습 신호로 씁니다. 외부 표현에 정렬하면 수렴 속도와 생성 품질이 얼마나 달라집니까? 어떤 조건에서 달라집니까? | L1-16, L3-4 |
| 4.body.0.left.0.alt | Fig. 2(a). 층 번호에 따른 vanilla SiT-XL/2의 linear probe 정확도. t=0, 0.25, 0.5 세 곡선이 layer 20 부근에서 최고점을 찍고 내려가며, 모두 위쪽 DINOv2-g 점선보다 낮다. | Fig. 2(a). 층 번호에 따른 vanilla SiT-XL/2의 linear probe 정확도. t=0, 0.25, 0.5 세 곡선이 20층 부근에서 최고점을 찍고 내려가며, 모두 위쪽 DINOv2-g 점선보다 낮다. | L1-8 |
| 4.body.0.right.0.items.0 | probe: 층 출력을 공간 평균한 뒤 linear classifier | probe에서 층 출력을 공간 방향으로 평균한 뒤 linear classifier 학습 | L3-3 |
| 4.body.0.right.0.items.1 | $t$ = 0, 0.25, 0.5 모두 layer 20 부근이 최고, 그 뒤 하락 | $t$ = 0, 0.25, 0.5 모두 20층 부근에서 정확도가 가장 높고 이후 낮아짐 | L1-8, L3-3 |
| 4.body.0.right.1.text | 곡선을 읽은 서술이다 (표 수치 없음) | 곡선에서 확인한 정확도 추이 (표 수치 없음) | L2-6, L1-16 |
| 4.notes.0 | 각 층의 hidden state를 공간 방향으로 평균하고 linear classifier를 학습해 표현을 봅니다. | 각 층의 hidden state를 공간 방향으로 평균하고 linear classifier를 학습해 표현을 평가합니다. | L3-2 |
| 4.notes.1 | vanilla SiT의 정확도는 layer 20 부근에서 가장 높고 이후 떨어집니다. 저자들은 뒤쪽 층이 고주파 세부를 만드는 쪽으로 옮겨 가기 때문이라고 봅니다. | vanilla SiT의 정확도는 20층 부근에서 가장 높고 이후 떨어집니다. 저자들은 뒤쪽 층이 고주파 세부를 만드는 데 더 집중하기 때문이라고 봅니다. | L1-8, L2-1 |
| 5.message | Vanilla SiT의 DINOv2-g 정렬은 크고 오래 학습할수록 높아지지만, 7M step의 XL/2도 다른 자기지도 인코더 수준에 못 미친다. | Vanilla SiT는 모델이 크고 학습 step이 많을수록 DINOv2-g와의 정렬이 높다. 7M step의 XL/2도 다른 자기지도 인코더 수준에는 못 미친다. | L3-3 |
| 5.body.0.left.0.left.0.alt | Fig. 2(b). 층별 CKNNA. SiT의 t=0, 0.25, 0.5 곡선이 layer 20 부근에서 약 0.14로 가장 높고, MAE-L 점선은 넘지만 DINO-B와 MoCov3-B 점선보다 낮다. | Fig. 2(b). 층별 CKNNA. SiT의 t=0, 0.25, 0.5 곡선이 20층 부근에서 약 0.14로 가장 높고, MAE-L 점선은 넘지만 DINO-B와 MoCov3-B 점선보다 낮다. | L1-8 |
| 5.body.0.right.0.items.2 | 크기와 step이 늘면 높아진다 (B/2는 400K까지) | 모델이 크고 학습 step이 많을수록 CKNNA가 높다 (B/2는 400K까지) | L3-3 |
| 5.body.0.right.1.text | 기준 표현은 clean DINOv2-g. 곡선 근거 | 기준 표현은 clean DINOv2-g. 표 수치 없이 곡선에서 읽은 서술 | L3-3 |
| 5.notes.0 | CKNNA는 두 표현 공간에서 공통으로 가까운 이웃을 세어 정렬을 측정합니다. 기준은 clean 이미지의 DINOv2-g입니다. | CKNNA는 두 표현 공간의 공통 최근접 이웃을 세어 정렬을 측정합니다. 기준은 clean 이미지에서 얻은 DINOv2-g 표현입니다. | L1-8, L3-3 |
| 5.notes.1 | 왼쪽에서 SiT의 일부 층은 MAE-L보다 높지만 DINO-B와 MoCov3-B에는 못 미칩니다. 오른쪽에서 모델이 크고 학습이 길수록 정렬이 높아지지만, 7M step의 XL/2도 여전히 낮습니다. | 왼쪽 그림에서 SiT 일부 층의 CKNNA는 MAE-L보다 높지만 DINO-B와 MoCov3-B보다 낮습니다. 오른쪽 그림에서는 모델이 크고 학습 step이 많을수록 정렬이 높아집니다. 그래도 7M step의 XL/2는 DINO-B보다 낮습니다. | L3-3 |
| 5.notes.2 | 논문은 여기서 두 가지 어려움을 짚습니다. 인코더는 clean 이미지를, 확산 모델은 noisy latent를 받는다는 입력 차이입니다. 그래서 인코더를 그대로 붙이는 대신 정규화로 표현을 끌어오는 방법을 택합니다. | 논문은 두 가지 어려움을 짚습니다. 그중 하나는 입력 차이입니다. 인코더는 clean 이미지를 받고 확산 모델은 noisy latent를 받습니다. 그래서 인코더를 직접 결합하는 대신 정규화로 SiT의 표현을 인코더 표현에 정렬합니다. | L2-1, L3-3 |
| 6.message | REPA는 같은 이미지의 clean patch token을 SiT layer 8에 붙인 MLP의 학습 목표로 쓰고, 추론에서는 그 경로를 떼어 낸다. | REPA는 SiT 8층의 MLP를 학습할 때 같은 이미지의 clean patch token을 목표로 쓴다. 추론에서는 인코더와 MLP를 사용하지 않는다. | L2-1, L1-8 |
| 6.body.0.reveals | 정렬 손실이 어느 층에서 갈라져 나가는지, 학습에만 쓰는 경로(인코더·MLP·REPA loss)와 추론 경로가 어떻게 다른지 | 정렬 loss를 적용하는 층. 학습에만 쓰는 경로(인코더·MLP·REPA loss)와 추론 경로의 차이 | L2-7, L3-4, L1-8 |
| 6.body.0.steps.2.title | Layer 8 정렬 | 8층 정렬 | L1-8 |
| 6.body.0.steps.2.text | SiLU 3층 MLP $h_\phi$로 투영, 같은 patch끼리 유사도 | SiLU 3층 MLP $h_\phi$로 투영한 뒤 같은 위치의 patch끼리 유사도 계산 | L3-3 |
| 6.body.0.steps.3.text | block 9–28이 velocity 예측, 두 loss를 함께 | block 9–28에서 velocity를 예측하고 두 loss를 함께 줄임 | L3-3 |
| 6.notes.0 | [1] 위쪽 경로는 clean 이미지를 고정된 DINOv2-B에 넣어 patch token을 만듭니다. 이것이 정렬 목표입니다. | [1] 위쪽 경로에서는 clean 이미지를 고정된 DINOv2-B에 넣어 patch token을 만듭니다. 이 token이 정렬 목표입니다. | L2-5, L1-11 |
| 6.notes.1 | [2] 아래쪽은 원래의 확산 학습입니다. 같은 이미지의 VAE latent에 noise를 섞어 SiT에 넣고, 첫 여덟 block을 지나 layer 8의 hidden state를 얻습니다. 256×256 이미지에서 token은 256개입니다. | [2] 아래쪽은 원래의 확산 학습입니다. 같은 이미지의 VAE latent에 noise를 섞어 SiT에 넣고, 첫 여덟 block을 지나 8층의 hidden state를 얻습니다. 256×256 이미지에서 token은 256개입니다. | L1-8 |
| 6.notes.2 | [3] Layer 8의 token을 3층 MLP로 인코더 차원에 투영하고, 같은 위치 patch끼리 유사도를 높입니다. [4] 나머지 block은 그대로 velocity를 예측하고, 두 loss를 함께 줄입니다. | [3] 8층의 token을 3층 MLP로 인코더 차원에 투영하고, 같은 위치의 patch끼리 유사도를 높입니다. [4] 나머지 block에서 기존 방식대로 velocity를 예측하고, 학습할 때는 두 loss를 함께 줄입니다. | L1-8, L3-2 |
| 7.title | REPA 손실과 학습 목적 | REPA loss와 학습 목적 | L1-8 |
| 7.message | REPA는 대응 patch의 유사도를 높이는 항을 기존 denoising loss에 λ로 가중해 더한다. | REPA는 대응 patch의 유사도를 높이는 항에 λ를 곱해 기존 denoising loss에 더한다. | L3-2 |
| 7.body.0.symbols.1.1 | noisy 입력의 layer 8 token을 MLP로 투영 | noisy 입력의 8층 token을 MLP로 투영 | L1-8 |
| 7.notes.0 | 첫 식은 대응하는 patch마다 유사도를 구해 평균한 값에 음의 부호를 붙인 손실입니다. 손실을 줄이면 유사도가 높아집니다. | 첫 식에서는 대응하는 patch마다 유사도를 구하고 평균에 음의 부호를 붙여 loss를 계산합니다. 이 loss를 줄이면 유사도가 높아집니다. | L3-2, L1-8 |
| 7.notes.1 | 두 번째 식처럼 이 항을 velocity loss에 λ배 해서 더합니다. SiT 실험은 λ를 0.5로 씁니다. | 두 번째 식처럼 이 항에 λ를 곱해 velocity loss에 더합니다. SiT 실험에서는 λ를 0.5로 둡니다. | L3-2 |
| 8.notes.1 | 정렬은 B/2에서 layer 4, L/2와 XL/2에서 layer 8에 겁니다. target과 유사도 함수는 Table 7에 적힌 대로입니다. | 정렬 loss는 B/2의 4층, L/2와 XL/2의 8층에 적용합니다. target과 유사도 함수는 Table 7에 적힌 대로입니다. | L2-1, L1-8 |
| 8.notes.2 | 평가는 5만 장의 FID와 SDE sampler 250 step이 기본입니다. | 기본 평가에서는 SDE sampler를 250 step 실행하고, 이미지 5만 장으로 FID를 계산합니다. | L3-3 |
| 9.message | Layer 8에 REPA를 건 SiT-XL/2는 모든 층에서 linear probe가 높고, DINOv2-g 정렬은 layer 8 부근에서 크게 높아진다. | 8층에 REPA를 적용한 SiT-XL/2는 vanilla보다 모든 층에서 linear probe 정확도가 높다. DINOv2-g와의 정렬은 8층 부근에서 크게 높아진다. | L2-1, L3-3, L1-8 |
| 9.body.0.reveals | 같은 축에 그린 vanilla와 REPA를 패널마다 크게 보며, 분류 정확도와 정렬이 층별로 어디서 달라지는지 | 패널마다 같은 축에 그린 vanilla와 REPA를 확대해 분류 정확도와 정렬이 달라지는 층을 비교 | L3-3 |
| 9.body.0.states.0.alt | Fig. 3(a). 층별 linear probe 정확도. SiT-XL/2 + REPA(빨강)가 layer 8에서 약 73%로 가장 높고 이후 조금씩 내려가며, 모든 층에서 vanilla SiT-XL/2(파랑)보다 높다. | Fig. 3(a). 층별 linear probe 정확도. SiT-XL/2 + REPA(빨강)의 정확도는 8층에서 약 73%로 가장 높고 이후 조금씩 내려가며, 모든 층에서 vanilla SiT-XL/2(파랑)보다 높다. | L1-8, L3-2 |
| 9.body.0.states.0.text | layer 4–24 전 구간에서 REPA가 vanilla보다 높다. DINOv2-g와의 격차가 줄어든다. | 4–24층 전 구간에서 REPA의 정확도가 vanilla보다 높다. DINOv2-g와의 격차가 줄어든다. | L1-8, L3-3 |
| 9.body.0.states.1.alt | Fig. 3(b). 층별 DINOv2-g CKNNA. REPA는 layer 8에서 약 0.53으로 솟았다가 내려가 layer 20 이후에는 vanilla와 비슷하다. | Fig. 3(b). DINOv2-g와의 층별 CKNNA. REPA의 CKNNA는 8층에서 약 0.53으로 크게 높아졌다가 낮아져 20층 이후에는 vanilla와 비슷하다. | L2-7, L1-8 |
| 9.body.0.states.1.text | layer 8 부근에서 가장 높고, layer 20–24에서는 vanilla와 비슷하거나 낮다. | 8층 부근에서 가장 높고, 20–24층에서는 vanilla와 비슷하거나 낮다. | L1-8 |
| 9.body.0.states.2.title | 생성과 분류를 함께 | FID와 분류 정확도 비교 | L1-13 |
| 9.body.0.states.2.text | 같은 학습 step에서 REPA가 validation Acc.는 높고 FID는 낮다. | 같은 학습 step에서 REPA는 vanilla보다 validation Acc.가 높고 FID가 낮다. | L3-2 |
| 9.body.0.mediaCaption | **Fig. 3** REPA: SiT-XL/2, layer 8, DINOv2-B target, 1M step. 한 모델의 층별 평가 | **Fig. 3** REPA: SiT-XL/2, 8층, DINOv2-B target, 1M step. 한 모델의 층별 평가 | L1-8 |
| 9.body.0.caption | 패널마다 원래 축. CKNNA 축은 Fig. 2(b)가 0–0.3, Fig. 3(b)가 0–0.6이다 | 각 패널은 원래 축을 유지한다. CKNNA 축 범위는 Fig. 2(b)가 0–0.3, Fig. 3(b)가 0–0.6이다 | L3-3 |
| 9.notes.0 | 진단에서 본 그림을 REPA 모델로 다시 그린 것이 Fig. 3입니다. 각 패널 안에 vanilla와 REPA가 같은 축으로 그려져 있습니다. | Fig. 3은 앞서 본 진단 그림에 REPA 모델의 결과를 추가한 그림입니다. 각 패널에서 vanilla와 REPA의 결과를 같은 축에 표시했습니다. | L1-8, L1-2 |
| 9.notes.1 | [1] Linear probe는 표시된 모든 층에서 REPA가 높습니다. [2] CKNNA는 정렬을 건 layer 8 부근에서 크게 높아지지만, 뒤쪽 layer 20 이후에는 vanilla와 비슷하거나 조금 낮습니다. 학습 target은 DINOv2-B이고, 평가 기준은 DINOv2-g입니다. | [1] 그림에 표시된 모든 층에서 REPA의 linear probe 정확도가 더 높습니다. [2] CKNNA는 정렬을 적용한 8층 부근에서 크게 높아지지만, 20층 이후에는 vanilla와 비슷하거나 조금 낮습니다. 학습 target은 DINOv2-B이고, 평가 기준은 DINOv2-g입니다. | L2-1, L1-8, L3-3 |
| 9.notes.2 | [3] 같은 학습 step에서 보면 분류 정확도와 생성 FID가 함께 좋아집니다. 참고로 CKNNA 축 범위는 Fig. 2와 다르니, Fig. 2와는 숫자로 비교해 주십시오. | [3] 같은 학습 step에서 REPA의 분류 정확도는 더 높고 생성 FID는 더 낮습니다. Fig. 2와는 CKNNA 축 범위가 다르니 수치를 기준으로 비교해 주십시오. | L3-2, L1-8 |
| 10.message | CFG 없이 평가한 ImageNet 256×256에서 SiT-XL/2 + REPA는 400K step에 vanilla 7M step보다 낮은 FID를 기록한다. | ImageNet 256×256에서 CFG 없이 평가했을 때 SiT-XL/2 + REPA의 400K step FID는 vanilla의 7M step FID보다 낮다. | L3-2, L3-3 |
| 10.notes.2 | REPA는 더 학습하면 1M에 6.4, 4M에 5.9까지 내려갑니다. | REPA 모델을 더 학습하면 FID는 1M에 6.4, 4M에 5.9까지 내려갑니다. | L3-2 |
| 12.message | 같은 초기 noise에서 출발한 두 SiT-XL/2의 100K–400K 출력을 클래스마다 크게 비교한다. | 같은 초기 noise로 생성한 두 SiT-XL/2의 100K–400K 출력을 클래스마다 확대해 비교한다. | L3-2 |
| 12.body.0.reveals | 같은 noise·sampler에서 REPA 쪽 물체 형태가 몇 step에 갖춰지는지를 클래스별로 | 같은 noise·sampler 조건에서 REPA 출력의 물체 형태가 갖춰지는 학습 step을 클래스별로 비교 | L3-3 |
| 12.body.0.states.0.text | vanilla는 200K까지 머리 형태가 무너져 있다. REPA는 100K부터 눈과 부리가 있는 머리. | vanilla에서는 200K까지 머리 형태가 제대로 나오지 않는다. REPA에서는 100K부터 눈과 부리가 있는 머리가 나온다. | L2-1, L3-3 |
| 12.body.0.states.1.text | vanilla는 400K에도 풍선 아래 형체 없는 구조가 남는다. REPA는 200K에 하나의 열기구. | vanilla에서는 400K에도 풍선 아래에 형체가 뚜렷하지 않은 구조가 남는다. REPA에서는 200K에 하나의 열기구 형태가 나온다. | L3-3 |
| 12.body.0.side.0.text | 탭의 관찰은 발표자가 그림을 읽은 것이다. 저자가 고른 예시 | 저자가 고른 생성 예시에 대한 발표자의 해석 | L2-6, L1-16 |
| 12.notes.1 | [1] 앵무새는 vanilla가 200K까지 머리 모양이 무너져 있는데, REPA는 100K부터 눈과 부리가 있는 머리가 나옵니다. [2] 열기구는 vanilla가 400K에도 풍선 아래에 정체 모를 구조가 남고, REPA는 200K에 하나의 열기구가 됩니다. | [1] 앵무새는 vanilla에서 200K까지 머리 모양이 제대로 나오지 않습니다. REPA에서는 100K부터 눈과 부리가 있는 머리가 나옵니다. [2] 열기구는 vanilla에서 400K에도 풍선 아래에 형태를 알아보기 어려운 구조가 남습니다. REPA에서는 200K에 하나의 열기구 형태가 나옵니다. | L2-1, L3-2 |
| 12.notes.2 | [3] 햄버거는 400K에서 REPA 쪽에만 번과 패티, 감자튀김이 구분됩니다. 다만 이것은 제가 그림을 읽은 것이고, 저자가 고른 예시라는 점을 감안해 주십시오. | [3] 햄버거는 400K에서 REPA 쪽에만 번과 패티, 감자튀김이 구분됩니다. 다만 이 관찰은 제 해석입니다. 저자가 고른 예시라는 점도 감안해 주십시오. | L2-6 |
| 14.message | 정렬된 SiT의 분류 정확도가 높은 target일수록 FID가 낮고, DINOv2의 크기를 바꾼 차이는 0.3 이내다. | SiT를 정렬한 뒤 분류 정확도가 높게 나온 target일수록 FID가 낮다. DINOv2 크기에 따른 FID 차이는 0.3 이내다. | L3-3 |
| 14.body.0.right.0.groups.1.items.1 | 가장 좋은 DINOv2(LVD-142M)는 ImageNet-1K를 포함 | 가장 좋은 DINOv2(LVD-142M)의 학습 데이터에 ImageNet-1K 포함 | L3-3 |
| 15.title | 정렬 깊이 | 정렬 층 | L1-8 |
| 15.message | SiT-L/2에서 FID는 layer 8에 정렬할 때 가장 낮고, 정렬한 층의 linear probe는 layer 16에서 가장 높다. | SiT-L/2에서 FID는 8층에 정렬을 적용했을 때 가장 낮다. 정렬한 층의 linear probe 정확도는 16층에 정렬을 적용했을 때 가장 높다. | L1-8, L3-3 |
| 15.body.0.right.0.items.0.small | layer 8 → 16, 나빠짐 | 8층 → 16층에서 FID 악화 | L1-8, L3-3 |
| 15.notes.0 | 이 표의 각 행은 정렬 손실을 붙인 층이 다른, 따로 학습한 모델입니다. | 표의 각 행은 서로 다른 층에 정렬 loss를 적용해 따로 학습한 모델에 해당합니다. | L2-1, L1-8 |
| 15.notes.1 | Layer 8에서 16으로 옮기면 분류 정확도는 3.0 퍼센트포인트 오르지만 FID도 2.1 올라갑니다. 분류에 가장 좋은 깊이와 생성에 가장 좋은 깊이가 다릅니다. | 정렬 층을 8층에서 16층으로 바꾸면 분류 정확도는 3.0 퍼센트포인트 오르지만 FID도 2.1 올라갑니다. 분류 성능이 가장 좋은 정렬 층과 생성 성능이 가장 좋은 정렬 층이 다릅니다. | L1-8, L3-3 |
| 16.body.0.left.1.text | **Table 2** SiT-L/2, 400K, DINOv2-L, layer 8, no CFG. 50–100K에서는 NT-Xent가 유리, 이후 실험은 cosine (Sec. 4.2) | **Table 2** SiT-L/2, 400K, DINOv2-L, 8층, no CFG. 50–100K에서는 NT-Xent가 유리하며 이후 실험에서는 cosine 사용 (Sec. 4.2) | L1-8, L3-3 |
| 17.notes.1 | 오른쪽은 같은 checkpoint에서 분류 정확도와 FID를 함께 그린 것으로, 큰 모델일수록 둘이 더 빨리 좋아집니다. | 오른쪽에는 같은 checkpoint의 분류 정확도와 FID를 함께 그렸습니다. 모델이 클수록 분류 정확도가 더 빨리 높아지고 FID는 더 빨리 낮아집니다. | L3-2 |
| 18.title | Noise 수준별 표현 격차 | noise 수준별 표현 격차 | L1-8 |
| 18.message | 시험한 세 timestep 모두에서 REPA를 쓴 SiT-XL/2의 linear probe와 최대 CKNNA가 vanilla보다 높다. | 시험한 세 timestep 모두에서 REPA를 쓴 SiT-XL/2의 linear probe 정확도와 최대 CKNNA가 vanilla보다 높다. | L3-3 |
| 18.body.0.right.0.items.1 | Fig. 8: MoCov3-L·MAE-L을 target으로 써도 layer 8 부근 CKNNA는 높다. 후반 층은 vanilla 기준선 아래 | Fig. 8에서 MoCov3-L·MAE-L을 target으로 써도 8층 부근의 CKNNA는 높다. 후반 층의 CKNNA는 vanilla 기준선보다 낮다. | L1-8, L3-3 |
| 18.body.0.right.1.text | 막대·곡선 근거. 비교 checkpoint의 step은 적혀 있지 않다 | 막대·곡선에서 읽은 서술. 비교 checkpoint의 step은 적혀 있지 않다 | L3-3 |
| 18.notes.1 | Fig. 8에서 다른 인코더를 target으로 써도 정렬 층 부근은 높아지지만, 뒤쪽 층은 vanilla 기준선 아래로 내려갑니다. Fig. 8의 정렬 모델은 SiT-L/2이고 vanilla 기준은 SiT-XL/2입니다. | Fig. 8에서 다른 인코더를 target으로 써도 정렬 층 부근의 CKNNA는 높아지지만, 뒤쪽 층에서는 vanilla 기준선보다 낮습니다. Fig. 8의 정렬 모델은 SiT-L/2이고 vanilla 기준은 SiT-XL/2입니다. | L3-3 |
| 20.message | REPA는 step 대비 FID를 크게 줄였다. 무엇을, 어느 층에, 언제까지 정렬할지와 평가·비용의 근거는 더 따져 볼 수 있다. | REPA는 학습 step을 기준으로 비교했을 때 FID를 크게 낮췄다. 정렬 대상, 정렬 층, 정렬을 유지할 기간, 평가와 비용의 근거는 더 따져 볼 수 있다. | L3-2, L3-4 |
| 20.body.0.groups.0.items.1 | clean 인코더 표현을 layer 8에 patch마다 정렬 | clean 인코더 표현을 8층에 patch마다 정렬 | L1-8 |
| 20.body.0.groups.0.items.2 | ImageNet 256×256, no CFG: 400K step에 vanilla 7M 수준 | ImageNet 256×256, no CFG. 400K step에서 vanilla 7M step 수준의 FID | L3-3 |
| 20.body.0.groups.1.items.0 | 깊이: layer 8→16에서 Acc. +3.0 pp, FID +2.1. iREPA는 전역 성능보다 공간 구조가 생성을 좌우한다고 보고했다. 무엇을 정렬해야 하나? | 정렬 층을 8층에서 16층으로 바꾸면 Acc. +3.0 pp, FID +2.1. iREPA는 전역 성능보다 공간 구조가 생성 성능을 좌우한다고 보고했다. 무엇을 정렬해야 하나? | L1-8, L3-3 |
| 20.body.0.groups.1.items.3.text | 비용: 인코더 forward가 늘지만 처리량은 5.4 step/s 하나뿐이다. 후반 층 정렬은 떨어지고(Fig. 3b·8), HASTE는 학습 후반 정체를 보고했다. 정렬은 언제까지 유지해야 하나? | 인코더 forward가 늘지만 보고된 처리량은 5.4 step/s 한 값뿐이다. 후반 층에서 정렬이 낮아지고(Fig. 3b·8), HASTE는 학습 후반의 정체를 보고했다. 정렬은 언제까지 유지해야 하나? | L3-3 |
| 20.notes.0 | 정리하면, 논문은 vanilla SiT의 표현이 약하다는 진단에서 출발해 clean 인코더 표현을 중간 층에 정렬했고, ImageNet 256×256에서 같은 FID에 훨씬 적은 step으로 도달했습니다. | 저자들은 vanilla SiT의 표현이 약하다는 진단을 바탕으로 clean 인코더 표현을 SiT의 중간 층에 정렬했습니다. ImageNet 256×256에서 같은 FID까지 필요한 학습 step은 훨씬 적었습니다. | L2-1, L1-6 |
| 20.notes.1 | 토론 주제는 네 가지입니다. 첫째, 깊이 실험에서 분류 정확도와 FID가 반대로 움직입니다. 작년 12월의 iREPA는 target의 전역 성능보다 공간 구조가 생성 성능을 좌우한다고 보고했습니다. 그렇다면 무엇을 정렬하는 것이 핵심인지 다시 물을 수 있습니다. | 토론 주제는 네 가지입니다. 첫째, 정렬 층을 비교한 실험에서 분류 정확도는 좋아지고 FID는 나빠졌습니다. 작년 12월에 나온 iREPA 논문은 target의 전역 성능보다 공간 구조가 생성 성능을 좌우한다고 보고했습니다. 그렇다면 무엇을 정렬하는 게 가장 중요할까요? | L1-4, L3-2, L3-4 |
| 20.notes.2 | 둘째, guidance interval은 보고하는 지표와 같은 FID로 골랐고, sFID는 오히려 나빠졌습니다. 셋째, Table 3의 SiT-L/2 400K 수치가 Table 2에서 DINOv2-B 행과 같아, 어느 설정이 보고된 것인지 확인이 필요합니다. | 둘째, guidance interval을 고를 때도 결과를 보고할 때와 같은 지표인 FID를 썼고, sFID는 오히려 나빠졌습니다. 셋째, Table 3의 SiT-L/2 400K 수치가 Table 2의 DINOv2-B 행에 나온 값과 같습니다. 어느 설정으로 얻은 수치인지 확인해야 합니다. | L3-2, L3-3 |
| 20.notes.3 | 넷째는 제 해석입니다. 학습 중 인코더 forward 비용은 처리량 하나로만 보고되었습니다. 뒤쪽 층의 정렬은 떨어지고, HASTE는 학습 후반에 REPA가 정체한다고 보고했습니다. 같은 학습 시간 기준으로 정렬을 언제까지 유지할지 의견을 듣고 싶습니다. | 넷째는 제 해석입니다. 논문에서 학습 중 인코더 forward 비용과 관련해 보고한 수치는 처리량 하나뿐입니다. 뒤쪽 층의 정렬은 떨어지고, HASTE는 학습 후반에 REPA가 정체한다고 보고했습니다. 학습 시간을 같게 두고 비교할 때 정렬을 언제까지 유지할지 의견을 듣고 싶습니다. | L1-2, L3-3 |

### 고치지 않은 스캐너 후보와 이유

- **L1-5 · `14.body.0.right.1.text`, `14.notes.0`** — 인코더 자체의 정확도와 정렬 후 SiT의 정확도를 구별해야 가로축을 정확히 해석할 수 있다.
- **L1-7 · 연결어미 뒤 쉼표** — `4.message`의 쉼표는 두 비교 내용을 나누고, `5.body.0.left.0.left.0.alt`의 쉼표는 최고점 설명과 기준선 비교를 나눈다. 이런 쉼표는 다른 표현을 고친 줄에서도 살렸다.
- **L2-5 · `12.body.0.reveals`의 ‘형태가 갖춰지다’** — 생성 이미지에서 관찰한 상태 변화다. ‘갖춰지다’는 살리고 빠진 서술어와 비교 대상을 보완했다.
