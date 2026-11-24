# Deck text — Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis

## Slide 1 — Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis
[1.subtitle] 외부 encoder 없이 flow matching 안에서 표현을 학습하는 Self-Flow
[1.figure.alt] Fig. 1. 왼쪽은 text-to-image FID 학습 곡선, 오른쪽은 vanilla flow matching과 Self-Flow로 생성한 앵무새, 손톱 글자, 팔굽혀펴기 영상 프레임.
[1.figure.caption] **Fig. 1** (a) Text-to-image FID (b) Vanilla flow matching과 Self-Flow의 생성 예시
[1.notes.0] 오늘은 Black Forest Labs의 Self-Flow를 소개합니다. 생성 모델이 외부 encoder 없이 스스로 표현을 배우게 하는 방법이고, 그 근거가 어디까지인지를 함께 보겠습니다.

## Slide 2 — Self-Flow 한눈에 보기
[2.title] Self-Flow 한눈에 보기
[2.message] Self-Flow의 학습 신호는 같은 샘플에서 noise 수준을 달리한 두 입력의 표현을 맞추는 데서 나온다.
[2.body.0.text] 외부 encoder 없이, noise 수준이 다른 두 입력의 표현을 맞춰 flow matching 안에서 표현을 학습한다.
[2.body.1.items.0.text] 토큰마다 두 timestep 중 하나를 배정
[2.body.1.items.1.text] 더 깨끗한 입력을 본 teacher의 깊은 층 feature를 목표로
[2.body.1.items.2.title] 이미지·비디오·오디오
[2.body.1.items.2.text] 모달리티별 학습과 공유 backbone 실험
[2.notes.0] 한 문장으로 말하면, 같은 이미지를 noise 수준이 다르게 두 번 보여 주고 두 표현을 맞추게 하는 방법입니다.
[2.notes.1] 기여는 세 가지입니다. 토큰마다 두 timestep 중 하나를 주는 Dual-Timestep Scheduling, 더 깨끗한 입력을 본 EMA teacher에 맞추는 self-distillation, 그리고 이미지·비디오·오디오에 걸친 실험입니다.

## Slide 3 — 생성 모델의 표현 정렬 방법
[3.title] 생성 모델의 표현 정렬 방법
[3.message] 네 방법은 정렬 목표를 어느 모델에서 가져오는지, 그 목표를 어떤 noise의 입력으로 만드는지가 다르다.
[3.body.0.columns.0.label] 방법
[3.body.0.columns.1.label] student 쪽 표현
[3.body.0.columns.2.label] 맞추는 목표
[3.body.0.columns.4.label] 외부 모델
[3.body.0.groups.0.rows.0.cells.1] 중간층
[3.body.0.groups.0.rows.0.cells.2] 외부 encoder feature
[3.body.0.groups.0.rows.0.cells.3] 고정된 DINOv2 등
[3.body.0.groups.0.rows.0.cells.4] 있음
[3.body.0.groups.0.rows.1.cells.1] 앞쪽 층, noise 큼
[3.body.0.groups.0.rows.1.cells.2] 뒤쪽 층, noise 작음
[3.body.0.groups.0.rows.1.cells.4] 없음
[3.body.0.groups.0.rows.2.cells.1] 약한 중간층
[3.body.0.groups.0.rows.2.cells.2] 의미가 강한 중간층
[3.body.0.groups.0.rows.2.cells.3] 모델 자신
[3.body.0.groups.0.rows.2.cells.4] 없음
[3.body.0.groups.0.rows.3.cells.1] 중간층, 두 timestep 입력
[3.body.0.groups.0.rows.3.cells.2] 깊은 층, $\tau_{\min}$ 입력
[3.body.0.groups.0.rows.3.cells.4] 없음
[3.body.1.text] SRA·LayerSync의 정렬 대상은 각 논문 abstract에서 확인했다(Jiang et al. 2025, Haghighi et al. 2025).
[3.body.2.text] 질문: Self-Flow는 왜 작동하고, 그 설명은 어디까지 실험으로 뒷받침되는가?
[3.notes.0] 생성 모델에 표현 학습을 붙이는 방법은 크게 두 갈래입니다. REPA는 DINOv2 같은 외부 encoder의 feature에 맞추고, SRA와 LayerSync는 외부 모델 없이 모델 자신의 다른 층에 맞춥니다.
[3.notes.1] Self-Flow는 후자에 속하지만, teacher 입력을 더 깨끗하게 만드는 방식이 다릅니다. 오늘은 이것이 왜 작동하고, 그 설명이 어디까지 실험으로 뒷받침되는지를 보겠습니다.

## Slide 4 — 외부 encoder 크기와 생성 FID
[4.title] 외부 encoder 크기와 생성 FID
[4.message] REPA 설정에서 외부 encoder를 더 강한 것으로 바꿔도 생성 FID는 좋아지지 않았다.
[4.body.0.left.0.alt] Fig. 2(a). REPA에서 DINOv2-B, DINOv2-L, DINOv3-B, DINOv3-H+를 쓴 FID 학습 곡선. DINOv2-B가 가장 낮고 DINOv3-H+가 가장 높다.
[4.body.0.left.0.caption] **Fig. 2(a)** REPA 설정: ImageNet 256×256, SiT-XL, SD-VAE, no CFG
[4.body.0.right.0.items.0] DINOv2-B → DINOv2-L → DINOv3-B → DINOv3-H+ 순으로 encoder 교체
[4.body.0.right.0.items.1] 200K–600K step 내내 DINOv2-B의 FID가 가장 낮고 DINOv3-H+가 가장 높음
[4.body.0.right.0.items.2.text] 저자 설명: 고정된 외부 표현이 생성 목표와 어긋나 병목이 된다
[4.notes.0] 논문의 출발점입니다. REPA에서 정렬할 encoder를 DINOv2-B에서 DINOv3-H+까지 점점 강한 것으로 바꿨더니, FID는 오히려 나빠졌습니다.
[4.notes.1] 저자들은 고정된 외부 표현이 생성 목표와 맞지 않아 병목이 된다고 설명합니다. 이 설명 자체는 실험으로 확인한 것이 아니라 해석이라는 점을 짚어 두겠습니다.

## Slide 5 — Rectified flow와 토큰 규격
[5.title] Rectified flow와 토큰 규격
[5.message] 기본 rectified flow는 길이와 차원이 다른 latent sequence에도 샘플마다 timestep 하나를 공통으로 쓴다.
[5.body.0.left.0.symbols.2.1] 0이면 데이터, 1이면 noise. 샘플마다 하나
[5.body.0.right.0.columns.0.label] 모달리티
[5.body.0.right.0.columns.2.label] 토큰 $N$
[5.body.0.right.0.columns.3.label] 차원 $C$
[5.body.0.right.0.groups.0.rows.0.cells.0] 이미지 256×256
[5.body.0.right.0.groups.0.rows.3.cells.0] 비디오 45프레임·192p
[5.body.0.right.0.groups.0.rows.3.cells.2] 약 3K
[5.body.0.right.0.groups.0.rows.4.cells.0] 오디오 10초
[5.body.0.right.1.text] **App. A.2** 이미지 AE는 2×2 patch로 한 변을 16배 압축
[5.notes.0] 기본 틀은 rectified flow입니다. 데이터와 noise를 직선으로 잇고, 그 사이의 velocity를 예측합니다.
[5.notes.1] 여기서 중요한 것은 timestep t가 샘플마다 하나라는 점입니다. 이미지 256토큰이든 비디오 약 3천 토큰이든 모든 토큰이 같은 noise 수준을 받습니다.

## Slide 6 — 토큰별 noise 배치 네 방식
[6.title] 토큰별 noise 배치 네 방식
[6.message] Fig. 2(b)에서 토큰마다 다른 timestep을 주는 규칙 가운데 두 timestep을 공유하는 방식만 vanilla보다 FID가 낮았다.
[6.body.0.reveals] 토큰마다 timestep을 몇 개 뽑고 어떻게 나누는지에 따라 Fig. 2(b)의 FID가 vanilla보다 나빠지거나 좋아진다
[6.body.0.states.0.alt] 36개 토큰이 모두 같은 noise로 섞인 앵무새 이미지
[6.body.0.states.0.title] 모든 토큰에 같은 $t$
[6.body.0.states.0.text] 샘플의 모든 토큰이 같은 noise 수준. Fig. 2(b)의 기준선.
[6.body.0.states.1.alt] 주황 테두리 토큰 9개는 완전한 noise, 나머지는 같은 noise
[6.body.0.states.1.title] 일부 토큰을 $t = 1$로
[6.body.0.states.1.text] 가린 토큰은 pure noise, 나머지는 공통 $t$. Vanilla보다 FID 악화.
[6.body.0.states.2.alt] 토큰마다 noise 수준이 제각각인 앵무새 이미지
[6.body.0.states.2.title] 토큰마다 독립된 $t_i$
[6.body.0.states.2.text] 토큰별로 timestep을 따로 뽑는다. Vanilla보다 FID 악화.
[6.body.0.states.3.alt] 주황 테두리 토큰 9개는 더 강한 noise, 나머지 27개는 약한 noise
[6.body.0.states.3.title] 두 timestep $t$, $s$를 나눔
[6.body.0.states.3.text] representation loss 없이도 vanilla보다 FID가 소폭 개선.
[6.body.0.side.0.alt] Fig. 2(b). 네 noise scheduler의 FID 학습 곡선. Diffusion forcing과 full masking은 vanilla보다 높고 Dual-Timestep이 가장 낮다.
[6.body.0.side.0.caption] **Fig. 2(b)** 200K–600K step FID. 열화 원인은 균일 noise 추론과의 차이(저자 설명)
[6.body.0.caption] 격자는 설명용 예시: Fig. 1의 Self-Flow 이미지에 픽셀 noise를 섞었다(실제 학습은 latent).
[6.notes.0] 같은 이미지에 noise를 넣는 네 가지 방식을 바꿔 보겠습니다. [1] 먼저 vanilla, 모든 토큰이 같은 t입니다.
[6.notes.1] [2] 일부 토큰을 완전히 가리는 full masking, [3] 토큰마다 timestep을 따로 뽑는 diffusion forcing 방식은 오른쪽 그래프에서 vanilla보다 FID가 나빠집니다. 저자들은 추론할 때는 모든 토큰이 같은 noise인데 학습만 다르게 하면 그 차이가 문제가 된다고 설명합니다.
[6.notes.2] [4] Dual-Timestep은 두 timestep만 뽑아 토큰 사이에 나눕니다. representation loss 없이 이것만으로도 FID가 조금 좋아졌습니다.

## Slide 7 — Dual-Timestep Scheduling
[7.message] 같은 분포에서 뽑은 두 timestep을 토큰 사이에 나누면 토큰별 주변분포를 유지하면서 한 입력 안에 noise 차이가 생긴다.
[7.body.0.left.0.alt] 36개 토큰 중 주황 테두리 9개에 두 번째 timestep s, 나머지에 t를 준 앵무새 이미지
[7.body.0.left.0.caption] 예시: $t$ = 0.3, $s$ = 0.8, 36개 중 9개에 $s$ (주황)
[7.body.0.right.0.steps.0.text] 같은 분포에서 두 번 뽑는다
[7.body.0.right.0.steps.2.title] $\tau_i = s$ ($i \in M$), 아니면 $t$
[7.body.0.right.1.columns.1.label] 이미지
[7.body.0.right.1.columns.2.label] 비디오
[7.body.0.right.1.columns.3.label] 오디오
[7.body.0.right.1.groups.0.rows.0.cells.0] 두 번째 timestep 비율
[7.body.0.right.2.text] timestep 조건은 scalar에서 토큰별 벡터 $\tau \in \mathbb{R}^N$로 확장. 비디오가 0.10인 것은 시간 중복 때문(App. A.3).
[7.notes.0] Dual-Timestep의 정의입니다. t와 s를 같은 분포에서 두 번 뽑고, 토큰마다 확률 R_M으로 s를, 나머지는 t를 줍니다.
[7.notes.1] 두 값이 같은 분포에서 나오므로 토큰 하나만 보면 timestep 분포는 vanilla와 같습니다. 그래서 추론 조건과 어긋나지 않으면서, 한 입력 안에 더 깨끗한 토큰과 더 흐린 토큰이 섞입니다. 비율은 이미지 0.25, 비디오 0.10, 오디오 0.50입니다.

## Slide 8 — EMA teacher와 학습 loss
[8.title] EMA teacher와 학습 loss
[8.message] Student는 섞인 입력에서 velocity를 예측하면서, 더 깨끗한 입력을 본 EMA teacher의 깊은 층 표현을 맞춘다.
[8.body.0.alt] Fig. 3. Student는 두 timestep이 섞인 입력을, EMA teacher는 모든 토큰에 더 낮은 timestep을 준 입력을 받고, student 중간층과 teacher 깊은 층의 feature를 cosine으로 맞춘다.
[8.body.0.caption] **Fig. 3** Self-Flow 학습 구조
[8.body.1.right.0.items.0] teacher 입력: 모든 토큰에 $\tau_{\min} = \min(t, s)$
[8.body.1.right.0.items.1] 층 $l = 0.3D$, $k = 0.7D$ (SiT-XL에서 8, 20)
[8.body.1.right.0.items.3] projection 약 10M 추가
[8.notes.0] 이제 이 noise 차이를 학습 신호로 바꿉니다. Student는 섞인 입력을 받고, EMA teacher는 모든 토큰을 더 낮은 timestep, 즉 더 깨끗한 입력으로 봅니다.
[8.notes.1] Student 중간층을 projection한 것이 teacher 깊은 층 feature와 cosine으로 가까워지도록 학습하고, 이 loss에 γ 0.8을 곱해 생성 loss에 더합니다. Student는 깨끗한 토큰을 단서로 흐린 토큰의 표현을 추론해야 합니다.

## Slide 9 — ImageNet 256×256 비교
[9.title] ImageNet 256×256 비교
[9.message] ImageNet에서 Self-Flow는 SD-VAE 4M step과 RAE 1M step 비교에서 각각 FID를 낮췄고, 지표별 순위는 달랐다.
[9.body.0.left.0.columns.0.label] 모델
[9.body.0.left.1.text] **Table 1** SiT-XL 약 675M, no CFG. 굵은 글씨는 같은 AE 안에서 가장 좋은 값. SD-VAE에서 REPA와의 FID 순위는 2M–4M step 사이에 바뀐다(Fig. 20a).
[9.notes.0] ImageNet 결과입니다. SD-VAE에서 4M step 기준 Self-Flow의 FID는 5.70으로, DINOv2에 정렬한 REPA의 5.89보다 0.19 낮습니다. 다만 IS와 Recall은 REPA가 더 높습니다.
[9.notes.1] RAE와 같은 semantic autoencoder 위에서도 FID가 3.24에서 2.95로 내려갔습니다. 모든 수치는 CFG 없이 잰 것입니다.

## Slide 10 — Text-to-image 생성 지표
[10.title] Text-to-image 생성 지표
[10.message] 이 T2I 설정에서 Self-Flow는 DINOv2에 정렬한 REPA보다 FID와 FD-DINO가 낮고 CLIP score가 높았다.
[10.body.0.left.0.title] Text-to-image FID, 1M step (낮을수록 좋음)
[10.body.0.left.0.items.0.sub] 외부 모델 없음
[10.body.0.left.0.items.1.sub] 외부 모델 없음
[10.body.0.left.0.items.2.sub] DINOv2에 정렬
[10.body.0.left.0.items.3.sub] SigLIP 2에 정렬
[10.body.0.left.0.items.4.sub] 정렬 없음
[10.body.0.left.1.text] **Table 2** 약 625M, 내부 20M 쌍, SD-VAE, no CFG, 50 ODE steps. sFID는 SRA 8.05, REPA–SigLIP 2 8.13, Self-Flow 8.14.
[10.body.0.right.1.text] Fig. 1(a)의 약 2.8배는 REPA의 1M step FID에 도달하는 step 수 비교다. teacher forward 비용은 들어 있지 않다.
[10.notes.0] Text-to-image에서도 Self-Flow의 FID가 3.61로 가장 낮습니다. 흥미로운 점은 DINOv2 feature로 잰 거리인 FD-DINO에서도 DINOv2에 직접 정렬한 REPA보다 낮다는 것입니다.
[10.notes.1] 표지에서 본 2.8배 빠른 수렴은 같은 FID에 도달하는 step 수의 비교입니다. Self-Flow는 매 step teacher forward를 한 번 더 하므로, 연산량 기준으로는 이보다 작아진다는 점은 제 해석입니다.

## Slide 11 — 비디오와 오디오 생성 지표
[11.title] 비디오와 오디오 생성 지표
[11.message] 논문이 고른 설정에서 Self-Flow의 비디오·오디오 지표가 모두 가장 낮았고, 외부 encoder의 효과는 encoder와 지표에 따라 달랐다.
[11.body.0.left.0.columns.0.label] 비디오
[11.body.0.left.1.text] **Table 3** 내부 6M 영상, Wan2.2 AE, 45프레임·192p, 600K step. FID는 프레임별. 학습 timestep의 5%를 [0.95, 1.00]에서 뽑는다(App. C).
[11.body.0.right.0.columns.0.label] 오디오 FAD
[11.body.0.right.1.text] **Table 4·5** FMA 10초, Songbloom AE, 350K step. 방법마다 trainshift를 골랐고(App. B), Self-Flow의 $R_M$ 0.50도 탐색으로 정했다. 모든 지표 no CFG.
[11.notes.0] 비디오에서는 Self-Flow가 FVD 47.81로 가장 낮고, 비디오 전용 encoder인 V-JEPA 2나 Depth Anything 3에 정렬한 REPA는 오히려 vanilla보다 나빴습니다.
[11.notes.1] 다만 비디오 학습에는 timestep의 5%를 아주 높은 noise 구간에서 뽑는 처치가 들어가 있고, 이것을 빼면 Self-Flow의 프레임 FID가 나빠집니다. 이 점은 분석에서 다시 보겠습니다.
[11.notes.2] 오디오는 세 FAD 모두 Self-Flow가 가장 낮습니다. 표 오른쪽 열처럼 trainshift가 Self-Flow만 1.0이라는 점은 토론에서 다시 다룹니다.

## Slide 12 — 공유 backbone과 loss 가중치
[12.title] 공유 backbone과 loss 가중치
[12.message] 공유 backbone 실험에서 시험한 다섯 가중치 모두 Self-Flow의 이미지 FID, 비디오 FVD, 오디오 FAD가 Vanilla FM보다 낮았다.
[12.body.0.columns.0.label] 가중치 (이미지, 비디오, 오디오)
[12.body.0.columns.1.label] 이미지 ΔFID
[12.body.0.columns.2.label] 비디오 ΔFVD
[12.body.0.columns.3.label] 오디오 ΔFAD (CLAP)
[12.body.1.text] **Table 6** Δ = Self-Flow − Vanilla FM, 음수가 좋음. 약 625M, 1M step, no CFG, 이미지는 FLUX.2 AE. 강조 행(video-weighted): FID 3.35 → 3.19, FVD 62.7 → 58, FAD 160.1 → 157.4. 이 실험의 대조군은 Vanilla FM뿐이다.
[12.notes.0] 하나의 backbone으로 세 모달리티를 함께 학습했습니다. loss 가중치를 다섯 가지로 바꿔도 세 지표 모두 Self-Flow가 vanilla보다 좋았습니다.
[12.notes.1] 강조한 행은 비디오에 가중치를 많이 준 설정으로, 다음 슬라이드의 로봇 실험이 이 checkpoint에서 시작합니다. 이 실험의 비교 대상은 vanilla뿐이라는 점도 기억해 두십시오.

## Slide 13 — Video-action 전이
[13.title] Video-action 전이
[13.message] 같은 RT-1 fine-tuning 뒤에도 Self-Flow 초기화의 이점은 두 물체를 다루거나 순서를 따라야 하는 과제에서 남았다.
[13.body.0.left.0.alt] Fig. 8(b). SIMPLER 네 과제의 성공률 레이더 차트. Self-Flow와 FM의 30K, 100K step 결과.
[13.body.0.left.0.caption] **Fig. 8(b)** SIMPLER 성공률. video-weighted 625M에서 RT-1(73.5K episode)로 fine-tuning
[13.body.0.right.0.items.0.items.0] 네 과제 모두 Self-Flow가 앞섬
[13.body.0.right.0.items.0.items.1] FM은 Open and Place 0%
[13.body.0.right.0.items.1.items.0] Pick Up Coke Can: 비슷하게 수렴
[13.body.0.right.0.items.1.items.1] Open/Close Drawer: FM이 소폭 앞섬
[13.body.0.right.0.items.1.items.2] Move Near: Self-Flow 50%, 격차 확대
[13.body.0.right.0.items.1.items.3] Open and Place: Self-Flow 29%, 격차 유지
[13.body.0.right.1.text] 과제별 평가 15·18·10·7회, checkpoint마다 2회 반복(App. E).
[13.notes.0] 멀티모달 checkpoint에서 시작해 로봇 데이터로 fine-tuning했습니다. 30K step에서는 네 과제 모두 Self-Flow가 앞서고, FM은 Open and Place를 한 번도 성공하지 못했습니다.
[13.notes.1] 100K step이 되면 Coke Can은 비슷해지고 Drawer는 오히려 FM이 조금 앞섭니다. 반면 두 물체를 다루는 Move Near와 순서가 있는 Open and Place에서는 차이가 남습니다. 다만 Open and Place는 평가가 7회뿐이라 숫자는 거칠게 보셔야 합니다.

## Slide 14 — 생성 샘플의 정성 비교
[14.title] 생성 샘플의 정성 비교
[14.message] 논문은 글자의 판독성, 물체의 형태, 프레임 사이 신체 일관성을 서로 다른 예시로 보여 준다.
[14.body.0.reveals] 정성 예시마다 무엇을 비교해야 하는지(글자, 형태, 시간 일관성)를 한 번에 하나씩 크게 본다
[14.body.0.states.0.label] 글자
[14.body.0.states.0.alt] Fig. 9 일부. 위는 vanilla flow matching, 아래는 Self-Flow가 그린 FLUX 문구 네 장.
[14.body.0.states.0.title] 같은 문구의 철자
[14.body.0.states.0.text] 위 vanilla, 아래 Self-Flow. 4B multi-modal 모델, 고해상도 100K step.
[14.body.0.states.1.label] 이미지
[14.body.0.states.1.alt] Fig. 10(a). Vanilla, REPA, SRA, Self-Flow의 Vespa, 인물, 바퀴, 원숭이 이미지.
[14.body.0.states.1.title] 물체 형태와 세부
[14.body.0.states.1.text] Vanilla · REPA · SRA · Self-Flow 순. 약 625M T2I.
[14.body.0.states.2.label] 비디오
[14.body.0.states.2.alt] Fig. 10(b). 네 방법의 자전거, 스키, 춤 영상 프레임.
[14.body.0.states.2.title] 프레임 사이 일관성
[14.body.0.states.2.text] 셋째 줄 춤 영상: baseline은 팔다리가 사라지는 프레임이 있다. 약 625M, 6M 영상.
[14.body.0.caption] 정성 샘플은 50 steps, CFG 이미지 3.5 / 비디오 5 (App. A.3).
[14.notes.0] 정성 결과는 탭으로 하나씩 보겠습니다. [1] 글자는 4B 모델의 결과로, 위가 vanilla, 아래가 Self-Flow입니다. 철자가 맞는지 보시면 됩니다.
[14.notes.1] [2] 이미지는 네 방법을 나란히 둔 것으로, Vespa의 차체 형태를 보시면 됩니다. [3] 비디오는 셋째 줄의 춤 영상에서 baseline의 팔다리가 사라지는 프레임이 있습니다. 모두 저자가 고른 예시라는 점은 감안해야 합니다.

## Slide 15 — 모델 크기와 학습 FLOPs
[15.title] 모델 크기와 학습 FLOPs
[15.message] 논문의 T2I sweep에서는 모델이 커질수록 Self-Flow와 REPA의 CLIP score 격차가 벌어졌다.
[15.body.0.reveals] 같은 sweep을 학습 step과 training FLOPs 두 가로축으로 바꿔 보아도 625M Self-Flow와 1B REPA의 관계가 같은지 확인한다
[15.body.0.states.0.alt] Fig. 6(a). 네 모델 크기에서 Self-Flow와 REPA의 학습 step별 CLIP score.
[15.body.0.states.0.title] 가로축: 학습 step
[15.body.0.states.0.text] 625M Self-Flow가 1M step에서 1B REPA보다 높은 CLIP score.
[15.body.0.states.1.alt] Fig. 6(b). 같은 결과를 training FLOPs 축으로 그린 그래프.
[15.body.0.states.1.title] 가로축: training FLOPs
[15.body.0.states.1.text] FLOPs 축에서도 625M Self-Flow가 1B REPA보다 높다. FLOPs 산정 방식은 본문에 없다.
[15.body.0.caption] 290M · 420M · 625M · 1B = 층 수 8 · 14 · 21 · 28. 내부 T2I 20M 쌍, SD-VAE, no CFG. 비교 지표는 CLIP score뿐이다.
[15.notes.0] 모델 크기를 290M에서 1B까지 키우면서 CLIP score를 비교했습니다. [1] step 축에서 625M Self-Flow가 1B REPA보다 높습니다.
[15.notes.1] [2] FLOPs 축으로 바꿔도 관계는 같습니다. 다만 FLOPs에 teacher forward가 어떻게 들어갔는지는 본문에 없고, 이 sweep은 CLIP score만 보고했습니다.

## Slide 16 — 층별 ImageNet linear probe
[16.title] 층별 ImageNet linear probe
[16.message] Self-Flow의 linear probe 정확도는 앞쪽과 중간 층에서 높았고, 뒤쪽 층에서는 vanilla보다 낮았다.
[16.body.0.left.0.alt] Fig. 4(b). 층별 ImageNet linear probe top-1 정확도. 4–16층은 Self-Flow가 높고 20–28층은 vanilla가 높다.
[16.body.0.left.0.caption] **Fig. 4(b)** ImageNet, SiT-XL 약 675M, 2M step
[16.body.0.right.0.items.0.heading] 4–16층
[16.body.0.right.0.items.0.items.0] Self-Flow가 높음
[16.body.0.right.0.items.0.items.1] 논문이 강조한 개선 구간
[16.body.0.right.0.items.1.heading] 20–28층
[16.body.0.right.0.items.1.items.0] vanilla가 높음
[16.body.0.right.0.items.1.items.1] 본문은 언급하지 않음
[16.body.0.right.1.text] linear probe가 재는 것은 클래스 분리도다. student가 깨끗한 토큰을 단서로 쓰는지는 직접 재지 않는다.
[16.notes.0] 표현이 실제로 좋아졌는지는 층별 linear probe로 확인했습니다. 4층부터 16층까지는 Self-Flow가 분명히 높습니다.
[16.notes.1] 그런데 그림을 보면 20층 이후에는 vanilla가 더 높고, 본문은 이 부분을 언급하지 않습니다. 또 linear probe는 클래스 분리도를 잴 뿐, 논문이 말하는 기전인 깨끗한 토큰 활용을 직접 재지는 않습니다.

## Slide 17 — Self-Flow 구성요소 ablation
[17.title] Self-Flow 구성요소 ablation
[17.message] ImageNet ablation에서 representation loss를 뺐을 때 FID가 가장 크게 나빠졌고, mask를 빼거나 두 번째 timestep을 제한해도 나빠졌다.
[17.body.0.left.0.alt] Fig. 11(a). Ablation 설정별 FID 학습 곡선. representation loss를 뺀 설정이 가장 높다.
[17.body.0.left.0.caption] **Fig. 11(a)** ImageNet, SiT-XL 약 675M, no CFG, 200K–600K step
[17.body.0.right.0.items.0] $\mathcal{L}_{\mathrm{rep}}$ 제거: FID 4점 넘게 악화
[17.body.0.right.0.items.1] mask 제거($\mathcal{L}_{\mathrm{rep}}$ 유지): 1점 넘게 악화
[17.body.0.right.0.items.2] $s$를 $t$보다 최대 0.2 깨끗한 범위로 제한: mask 제거와 비슷한 악화
[17.body.0.right.0.items.3] cosine 대신 $\ell_1$: 후반 FID가 내려가지 않음
[17.body.0.right.1.text] 수치는 §4.4 본문 서술. 측정 step과 표는 없다. $\ell_1$의 원인(feature norm 증가)은 저자 설명.
[17.notes.0] 구성요소를 하나씩 뺀 결과입니다. representation loss를 빼면 FID가 4점 넘게 나빠져 가장 큰 영향을 줍니다.
[17.notes.1] loss는 두고 mask만 빼도 1점 넘게 나빠지므로, 단순한 층간 정렬만으로는 부족하다는 것이 저자들의 주장입니다. 두 번째 timestep을 t와 거의 같게 제한해도 mask를 뺀 것만큼 나빠집니다. 이 ablation은 모두 ImageNet에서만 했습니다.

## Slide 18 — Timestep 분포와 low-SNR 구간
[18.title] Timestep 분포와 low-SNR 구간
[18.message] Self-Flow의 이점은 T2I의 timestep 분포와 비디오의 고noise 구간 샘플링에 따라 달라졌다.
[18.body.0.left.0.alt] Fig. 11(b). REPA와 Self-Flow를 logit-normal과 uniform 분포로 학습한 FID 곡선. uniform에서 둘 다 낮고 차이가 더 크다.
[18.body.0.left.0.caption] **Fig. 11(b)** T2I 약 625M, SD-VAE, no CFG, 최대 1M step. logit-normal은 trainshift 1.78
[18.body.0.right.0.items.0.items.0] uniform에서 두 방법 모두 FID 개선
[18.body.0.right.0.items.0.items.1] Self-Flow와 REPA의 차이도 커짐
[18.body.0.right.0.items.1.heading] 비디오
[18.body.0.right.0.items.1.items.0] timestep 5%를 [0.95, 1.00]에서 추출
[18.body.0.right.0.items.1.items.1] 빼면 Self-Flow의 프레임 FID 악화, FVD는 여전히 가장 낮음
[18.body.0.right.1.text] 저자 가설: Dual-Timestep이 샘플 전체의 SNR을 평균 쪽으로 모아 고noise 구간이 덜 학습된다.
[18.notes.0] Self-Flow의 이점은 noise 분포에 따라 달라집니다. T2I에서 uniform 분포로 바꾸면 두 방법 모두 좋아지고, 차이도 더 커졌습니다.
[18.notes.1] 비디오는 반대 방향의 주의점입니다. 기본 분포에서는 아주 높은 noise 구간이 거의 뽑히지 않아서, timestep의 5%를 그 구간에서 따로 뽑았습니다. 이것을 빼면 Self-Flow의 프레임 FID가 나빠집니다. 저자들은 Dual-Timestep이 SNR을 평균 쪽으로 모으기 때문이라고 추정합니다.

## Slide 19 — 한계와 검증 범위
[19.title] 한계와 검증 범위
[19.message] 결론을 다른 조건으로 옮길 때는 실험마다 대조군, 평가 지표, 데이터 범위가 다르다는 점을 구분해야 한다.
[19.body.0.groups.0.heading] 대조군
[19.body.0.groups.0.items.0] 멀티모달·로봇·4B 글자·RAE·FLUX.2 AE는 Vanilla FM하고만 비교
[19.body.0.groups.0.items.1] 이 설정들에 SRA·REPA 비교는 없다
[19.body.0.groups.1.heading] 측정 범위
[19.body.0.groups.1.items.0] scaling은 CLIP score만, FID와 SRA는 없다
[19.body.0.groups.1.items.1] 구성요소 ablation과 linear probe는 ImageNet만
[19.body.0.groups.1.items.2] $\gamma$ sweep과 모달리티별 $R_M$ ablation은 보고하지 않았다
[19.body.0.groups.2.heading] 비용과 재현
[19.body.0.groups.2.items.0] 학습마다 teacher forward 추가, FLOPs 산정식은 없다
[19.body.0.groups.2.items.1] T2I·T2V는 내부 데이터로 평가
[19.body.0.groups.2.items.2] 공개 코드는 ImageNet 추론뿐, 학습 코드는 없다
[19.notes.0] 지금까지의 결과를 옮겨 쓸 때 주의할 점을 세 가지로 묶었습니다.
[19.notes.1] 먼저 멀티모달, 로봇, 4B 모델 같은 큰 실험은 vanilla하고만 비교했습니다. 둘째로 ablation과 linear probe는 ImageNet에서만 했고, scaling은 CLIP score만 봤습니다. 셋째로 teacher forward 비용이 들고, 공개된 코드는 ImageNet 추론 코드뿐이라 학습을 그대로 재현하기는 어렵습니다.

## Slide 20 — 정리와 토론
[20.title] 정리와 토론
[20.message] 결과와 ablation은 두 timestep과 self-distillation의 결합을 지지하지만, 이득이 어디서 오는지와 같은 시간 예산에서의 효과는 더 비교해야 한다.
[20.body.0.groups.0.heading] 정리
[20.body.0.groups.0.items.0] 토큰별 두 timestep과 더 깨끗한 EMA teacher 목표
[20.body.0.groups.0.items.1] 이미지·비디오·오디오 생성 지표와 ImageNet 앞·중간층 probe 개선
[20.body.0.groups.0.items.2] 이득의 크기는 timestep 분포와 평가 조건에 따라 달라짐
[20.body.0.groups.1.heading] 토론
[20.body.0.groups.1.items.0] App. A.3은 모든 방법에 같은 $p(t)$라 하지만, 오디오는 Self-Flow만 trainshift 1.0이다. 같은 trainshift면 FAD 차이는 얼마나 남는가?
[20.body.0.groups.1.items.1] 오디오 설정을 고른 FAD로 최종 결과도 보고했다. 다른 검증 데이터로 골라도 순위가 같은가?
[20.body.0.groups.1.items.2.text] Jiang et al.(2026)은 noise가 다른 토큰 사이 attention을 막아도 성능이 유지된다고 보고했다. 이득은 cross-token 정보인가, noise 축 augmentation인가?
[20.body.0.groups.1.items.3.text] teacher forward가 추가된다. 256토큰 이미지와 약 3K 토큰 비디오에서, 같은 wall-clock이면 이득이 얼마나 남는가?
[20.notes.0] 정리하면, Self-Flow는 토큰별 두 timestep으로 만든 정보 차이를 EMA teacher 목표로 바꾸는 방법이고, 여러 모달리티에서 생성 지표가 좋아졌습니다.
[20.notes.1] 토론 거리를 네 가지 준비했습니다. 첫째, 부록 A.3은 모든 방법에 같은 noise 분포를 썼다고 하지만 오디오에서는 Self-Flow만 trainshift가 다릅니다. 둘째, 오디오 설정을 고른 지표로 최종 결과도 보고했습니다.
[20.notes.2] 셋째는 외부 연구입니다. SRA 저자들이 올해 7월에, noise가 다른 토큰 사이 attention을 막아도 성능이 유지된다고 보고했습니다. 그렇다면 이득이 정말 깨끗한 토큰 정보에서 오는지 다시 물어볼 수 있습니다. 넷째는 제 해석으로, 같은 학습 시간에서의 비교입니다.

## Slide 21 — 질의응답
[21.title] 질의응답
[21.message] 어떤 비교가 Self-Flow의 작동 기전을 가장 잘 가려낼 수 있을지 함께 논의한다.
[21.body.0.text] Self-Flow의 이득이 어디서 오는지 가려낼 실험은 무엇일까?
[21.body.1.groups.0.heading] 논문
[21.body.1.groups.1.heading] 코드와 가중치
[21.body.1.groups.1.items.1] ImageNet 256×256 추론 코드, Hugging Face Hila/Self-Flow 체크포인트
[21.notes.0] 여기까지입니다. 특히 어떤 실험을 더 하면 Self-Flow의 이득이 어디서 오는지 가려낼 수 있을지 의견을 듣고 싶습니다.

