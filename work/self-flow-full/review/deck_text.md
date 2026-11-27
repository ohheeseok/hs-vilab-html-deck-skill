# Deck text — Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis

## Slide 1 — Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis
[1.subtitle] 외부 encoder 없이 flow matching 안에서 표현을 학습하는 Self-Flow
[1.figure.alt] Fig. 1. 왼쪽은 text-to-image FID 학습 곡선, 오른쪽은 vanilla flow matching과 Self-Flow로 생성한 앵무새, 손톱 글자, 팔굽혀펴기 영상 프레임.
[1.figure.caption] **Fig. 1** (a) Text-to-image FID (b) Vanilla flow matching과 Self-Flow의 생성 예시
[1.notes.0] 오늘은 Black Forest Labs의 Self-Flow를 소개합니다. 생성 모델이 외부 encoder 없이 스스로 표현을 배우게 하는 방법이고, 그 근거가 어디까지인지를 함께 보겠습니다.

## Slide 2 — Self-Flow의 학습 방식과 실험
[2.title] Self-Flow의 학습 방식과 실험
[2.message] Self-Flow는 같은 샘플의 noise 수준을 달리해 만든 두 입력의 feature를 맞춰 학습 신호를 얻는다.
[2.body.0.text] 외부 encoder 없이, noise 수준이 다른 두 입력의 표현을 맞춰 flow matching 안에서 표현을 학습한다.
[2.body.1.items.0.text] 토큰마다 두 timestep 중 하나를 배정
[2.body.1.items.1.text] noise가 더 적은 입력에서 얻은 teacher의 깊은 층 feature를 정렬 목표로 사용
[2.body.1.items.2.title] 이미지·비디오·오디오
[2.body.1.items.2.text] 모달리티별 학습과 공유 backbone 실험
[2.notes.0] 같은 샘플을 두 번 입력할 때 noise 수준을 달리하고, 두 입력의 feature를 맞추는 방법입니다.
[2.notes.1] 기여는 세 가지입니다. 토큰마다 두 timestep 중 하나를 배정하는 Dual-Timestep Scheduling, noise가 더 적은 입력에서 얻은 EMA teacher의 feature에 맞추는 self-distillation, 그리고 이미지·비디오·오디오 실험입니다.

## Slide 3 — 생성 모델의 표현 정렬 방법
[3.title] 생성 모델의 표현 정렬 방법
[3.message] 네 방법은 정렬 목표로 쓸 feature를 얻는 모델과 그 모델에 넣는 입력의 noise 수준이 다르다.
[3.body.0.columns.0.label] 방법
[3.body.0.columns.2.label] 정렬 목표
[3.body.0.columns.4.label] 외부 모델
[3.body.0.groups.0.rows.0.cells.1] 중간층
[3.body.0.groups.0.rows.0.cells.2] 외부 encoder feature
[3.body.0.groups.0.rows.0.cells.3] 고정된 DINOv2 등
[3.body.0.groups.0.rows.0.cells.4] 있음
[3.body.0.groups.0.rows.1.cells.1] 앞쪽 층, noise 큼
[3.body.0.groups.0.rows.1.cells.2] 뒤쪽 층, noise 작음
[3.body.0.groups.0.rows.1.cells.4] 없음
[3.body.0.groups.0.rows.2.cells.1] 중간층의 약한 feature
[3.body.0.groups.0.rows.2.cells.2] 의미 정보가 풍부한 중간층 feature
[3.body.0.groups.0.rows.2.cells.3] 모델 자신
[3.body.0.groups.0.rows.2.cells.4] 없음
[3.body.0.groups.0.rows.3.cells.1] 중간층, 두 timestep 입력
[3.body.0.groups.0.rows.3.cells.2] 깊은 층, 낮은 timestep 입력
[3.body.0.groups.0.rows.3.cells.4] 없음
[3.body.1.text] SRA·LayerSync의 정렬 대상은 각 논문 abstract에서 확인했다(Jiang et al. 2025, Haghighi et al. 2025).
[3.body.2.text] 질문: 외부 encoder를 더 강한 모델로 바꾸면 생성도 좋아지는가?
[3.notes.0] 생성 모델에 표현 학습을 추가하는 방법은 크게 두 갈래입니다. REPA는 DINOv2 같은 외부 encoder의 feature에 맞추고, SRA와 LayerSync는 외부 모델 없이 같은 모델의 다른 층에서 얻은 feature에 맞춥니다.
[3.notes.1] Self-Flow도 외부 모델을 쓰지 않고, 정렬 목표를 EMA teacher에서 얻습니다. 그 전에 외부 encoder를 쓰는 방법에서 encoder를 더 강한 것으로 바꾸면 무엇이 달라지는지부터 보겠습니다.

## Slide 4 — 외부 encoder 크기와 생성 FID
[4.title] 외부 encoder 크기와 생성 FID
[4.message] REPA 설정에서 외부 encoder를 더 강한 것으로 바꿔도 생성 FID는 좋아지지 않았다.
[4.body.0.left.0.alt] Fig. 2(a). REPA에서 DINOv2-B, DINOv2-L, DINOv3-B, DINOv3-H+를 쓴 FID 학습 곡선. DINOv2-B가 가장 낮고 DINOv3-H+가 가장 높다.
[4.body.0.left.0.caption] **Fig. 2(a)** REPA 설정: ImageNet 256×256, SiT-XL, SD-VAE, no CFG
[4.body.0.right.0.items.0] DINOv2-B → DINOv2-L → DINOv3-B → DINOv3-H+ 순으로 encoder 교체
[4.body.0.right.0.items.1] 200K–600K step 내내 DINOv2-B의 FID가 가장 낮고 DINOv3-H+가 가장 높음
[4.body.0.right.0.items.2.text] 저자 설명: 고정된 외부 표현이 생성 목표와 어긋나 병목이 된다
[4.notes.0] 논문의 출발점이 된 실험입니다. REPA에서 정렬에 쓰는 encoder를 DINOv2-B에서 DINOv3-H+까지 더 강한 모델로 차례로 바꿨더니, FID는 오히려 나빠졌습니다.
[4.notes.1] 저자들은 고정된 외부 표현이 생성 목표와 맞지 않아 병목이 된다고 설명합니다. 이 설명 자체는 실험으로 확인한 것이 아니라 해석이라는 점을 짚어 두겠습니다. 그러면 외부 encoder를 빼고 정렬 목표를 어디서 얻는지, 다음 그림으로 보겠습니다.

## Slide 5 — Self-Flow가 정렬 목표를 얻는 방식
[5.title] Self-Flow가 정렬 목표를 얻는 방식
[5.message] Self-Flow는 REPA의 외부 encoder 자리에 모델 자신의 EMA teacher를 두고, student 중간층 feature를 noise가 더 적은 입력을 받은 teacher의 깊은 층 feature에 맞춘다.
[5.body.0.reveals] 외부 encoder가 빠진 자리에 같은 모델의 EMA 사본이 들어오고 두 입력의 noise 수준이 갈라지는 것을 따라가면, Self-Flow가 정렬 목표를 모델 안에서 만든다는 것이 보인다.
[5.body.0.beats.0.title] REPA의 정렬
[5.body.0.beats.0.text] 고정 외부 encoder가 깨끗한 입력에서 만든 표현에 중간층을 맞춘다
[5.body.0.beats.1.title] EMA teacher로 교체
[5.body.0.beats.1.text] 목표를 모델 자신의 EMA 사본, 그 깊은 층 feature에서 얻는다
[5.body.0.beats.2.title] 두 noise 수준
[5.body.0.beats.2.text] student 입력은 두 수준, teacher 입력은 낮은 쪽만
[5.body.0.beats.3.title] 두 질문
[5.body.0.beats.3.text] ① 성능 향상은 어떤 구성 요소에서 오나 ② 모달리티와 모델 크기가 달라도 유지되나
[5.body.0.caption] Sec. 3.3–3.4와 **Fig. 3**을 바탕으로 그림. 막대 길이는 깊이 $D$에 비례. 16칸 중 4칸이 더 높은 noise
[5.notes.0] 앞 장의 REPA 구조부터 다시 보겠습니다. flow 모델은 noise latent에서 velocity를 예측하고, 고정된 외부 encoder가 깨끗한 입력에서 만든 표현에 중간층 feature를 맞춥니다.
[5.notes.1] [1] Self-Flow는 이 외부 encoder 자리에 모델 자신의 EMA 사본을 teacher로 둡니다. student의 중간층 feature를 teacher의 깊은 층 feature에 맞추는 loss를 더합니다.
[5.notes.2] [2] 두 입력은 noise 수준이 다릅니다. student 입력에서는 일부 토큰에 다른 timestep이 배정되어 두 수준이 섞이고, teacher 입력은 모든 토큰이 둘 중 낮은 수준입니다.
[5.notes.3] [3] 이 발표에서 볼 질문은 두 가지입니다. 성능 향상이 어떤 구성 요소에서 오는지, 그리고 모달리티와 모델 크기가 달라도 그 향상이 유지되는지입니다. 먼저 기본 rectified flow부터 보겠습니다.

## Slide 6 — Rectified flow와 토큰 규격
[6.title] Rectified flow와 토큰 규격
[6.message] 기본 rectified flow에서는 latent sequence의 길이와 차원이 달라도 샘플마다 모든 토큰에 같은 timestep을 쓴다.
[6.body.0.left.0.symbols.2.1] 0이면 데이터, 1이면 noise. 샘플마다 하나
[6.body.0.right.0.columns.0.label] 모달리티
[6.body.0.right.0.columns.2.label] 토큰 $N$
[6.body.0.right.0.columns.3.label] 차원 $C$
[6.body.0.right.0.groups.0.rows.0.cells.0] 이미지 256×256
[6.body.0.right.0.groups.0.rows.3.cells.0] 비디오 45프레임·192p
[6.body.0.right.0.groups.0.rows.3.cells.2] 약 3K
[6.body.0.right.0.groups.0.rows.4.cells.0] 오디오 10초
[6.body.0.right.1.text] **App. A.2** SD-VAE·FLUX.2 AE는 2×2 patch로 RAE와 같이 한 변을 16배 압축
[6.notes.0] 기본 틀은 rectified flow입니다. 데이터와 noise를 직선으로 잇고, 그 사이의 velocity를 예측합니다.
[6.notes.1] 샘플마다 timestep t를 하나만 씁니다. 이미지 256토큰이든 비디오 약 3천 토큰이든 모든 토큰의 noise 수준은 같습니다.

## Slide 7 — 토큰별 noise 배치 방식 네 가지
[7.title] 토큰별 noise 배치 방식 네 가지
[7.message] Fig. 2(b)에서 토큰마다 다른 timestep을 주는 규칙 가운데 두 timestep을 공유하는 방식만 vanilla보다 FID가 낮았다.
[7.body.0.reveals] Fig. 2(b)에서 timestep을 몇 개 뽑아 토큰에 어떻게 배정하느냐에 따라 FID가 vanilla보다 나빠지거나 좋아진다.
[7.body.0.states.0.alt] 36개 토큰에 모두 같은 수준의 noise를 적용한 앵무새 이미지
[7.body.0.states.0.title] 모든 토큰에 같은 $t$
[7.body.0.states.0.text] 샘플의 모든 토큰이 같은 noise 수준. Fig. 2(b)의 기준선.
[7.body.0.states.1.alt] 주황 테두리 토큰 9개는 완전한 noise, 나머지 토큰은 모두 같은 수준의 noise
[7.body.0.states.1.title] 일부 토큰을 $t = 1$로
[7.body.0.states.1.text] 가린 토큰은 pure noise, 나머지는 공통 $t$. Vanilla보다 FID 악화.
[7.body.0.states.2.alt] 토큰마다 noise 수준이 제각각인 앵무새 이미지
[7.body.0.states.2.title] 토큰마다 독립된 $t_i$
[7.body.0.states.2.text] 토큰별로 timestep을 따로 뽑는다. Vanilla보다 FID 악화.
[7.body.0.states.3.alt] 주황 테두리 토큰 9개의 noise 수준이 나머지 27개보다 높음
[7.body.0.states.3.title] 두 timestep $t$, $s$ 배정
[7.body.0.states.3.text] representation loss 없이도 vanilla보다 FID가 소폭 개선.
[7.body.0.side.0.alt] Fig. 2(b). 네 noise scheduler의 FID 학습 곡선. Diffusion forcing과 full masking은 vanilla보다 높고 Dual-Timestep이 가장 낮다.
[7.body.0.side.0.caption] **Fig. 2(b)** 200K–600K step FID. Full masking·diffusion forcing의 악화 원인은 학습과 추론의 noise 조건 차이(저자 설명).
[7.body.0.mediaCaption] 격자는 설명용 예시: Fig. 1의 Self-Flow 이미지에 픽셀 noise를 섞었다(실제 학습은 latent).
[7.notes.0] 앞 그림의 student 입력처럼 토큰마다 noise 수준을 다르게 주는 방법은 여러 가지입니다. 네 가지를 비교하겠습니다. [1] 먼저 vanilla입니다. 모든 토큰에 같은 t를 줍니다.
[7.notes.1] 오른쪽 그래프에서 [2] 일부 토큰을 완전히 가리는 full masking과 [3] 토큰마다 timestep을 따로 뽑는 diffusion forcing은 모두 vanilla보다 FID가 높습니다. 저자들은 추론할 때 모든 토큰의 noise 수준이 같은데 학습할 때만 다르게 주면 그 차이가 문제가 된다고 설명합니다.
[7.notes.2] [4] Dual-Timestep은 timestep을 두 개만 뽑아 토큰마다 둘 중 하나를 배정합니다. representation loss 없이도 이 방식만으로 FID가 조금 좋아졌습니다.

## Slide 8 — Dual-Timestep Scheduling
[8.message] 같은 분포에서 뽑은 두 timestep 중 하나를 토큰마다 배정하면 토큰별 주변분포가 유지되고, 한 입력에 noise 수준이 다른 토큰이 섞인다.
[8.body.0.left.0.alt] 36개 토큰 중 주황 테두리 9개에 두 번째 timestep s, 나머지에 t를 준 앵무새 이미지
[8.body.0.left.0.caption] 예시: $t$ = 0.3, $s$ = 0.8, 36개 중 9개에 $s$ (주황)
[8.body.0.right.0.steps.0.text] 같은 분포에서 timestep을 두 번 뽑는다
[8.body.0.right.0.steps.2.title] $\tau_i = s$ ($i \in M$), 아니면 $t$
[8.body.0.right.1.columns.1.label] 이미지
[8.body.0.right.1.columns.2.label] 비디오
[8.body.0.right.1.columns.3.label] 오디오
[8.body.0.right.1.groups.0.rows.0.cells.0] 두 번째 timestep 비율
[8.body.0.right.2.text] timestep 조건을 scalar에서 토큰별 벡터 $\tau \in \mathbb{R}^N$로 확장. 비디오에서는 시간 중복 때문에 두 번째 timestep 비율을 0.10으로 설정(App. A.3).
[8.notes.0] Dual-Timestep에서는 같은 분포에서 timestep을 두 번 뽑아 t와 s로 둡니다. 토큰마다 확률 R_M으로 s를 배정하고, 나머지 토큰에는 t를 줍니다.
[8.notes.1] 두 값이 같은 분포에서 나오므로 토큰 하나만 보면 timestep 분포는 vanilla와 같습니다. 논문은 이렇게 하면 토큰마다 따로 뽑는 방식보다 추론 조건과의 차이를 줄이면서 한 입력에 noise 수준이 다른 토큰을 섞을 수 있다고 설명합니다. 비율은 이미지 0.25, 비디오 0.10, 오디오 0.50입니다.

## Slide 9 — EMA teacher와 학습 loss
[9.title] EMA teacher와 학습 loss
[9.message] student는 두 timestep이 섞인 입력에서 velocity를 예측하면서, 자신의 feature를 noise가 더 적은 입력으로 얻은 EMA teacher의 깊은 층 feature에 맞춘다.
[9.body.0.alt] Fig. 3. student에는 두 timestep이 섞인 입력을 주고, EMA teacher에는 모든 토큰에 더 낮은 timestep을 적용한 입력을 준다. student 중간층의 feature를 teacher의 깊은 층 feature에 cosine으로 맞춘다.
[9.body.0.caption] **Fig. 3** Self-Flow 학습 구조
[9.body.1.right.0.items.0] teacher 입력: 모든 토큰에 $\tau_{\min} = \min(t, s)$
[9.body.1.right.0.items.1] 층 $l = 0.3D$, $k = 0.7D$ (SiT-XL에서 8, 20)
[9.body.1.right.0.items.3] projection 약 10M 추가
[9.notes.0] 앞 그림의 구조를 논문 Fig. 3으로 보면 이렇습니다. teacher는 student 가중치의 EMA이고, 모든 토큰에 τ_min을 적용한 입력을 받습니다. 층은 전체 깊이의 0.3과 0.7 지점, SiT-XL에서는 8층과 20층입니다.
[9.notes.1] 식 6은 projection한 student feature와 teacher feature의 cosine을 비교하고, 식 7은 이 항에 γ 0.8을 곱해 생성 loss에 더합니다. 저자들은 이렇게 하면 student가 noise가 적은 토큰을 단서로 noise가 많은 토큰의 feature를 추론하게 된다고 설명합니다. 이 설명이 맞는지는 뒤의 probe와 토론에서 다시 보겠습니다.

## Slide 10 — ImageNet 256×256 비교
[10.title] ImageNet 256×256 비교
[10.message] ImageNet에서 Self-Flow는 SD-VAE 4M step과 RAE 1M step 비교에서 각각 FID를 낮췄고, 지표별 순위는 달랐다.
[10.body.0.left.0.columns.0.label] 모델
[10.body.0.left.1.text] **Table 1** SiT-XL 약 675M, no CFG. 굵은 글씨는 같은 AE 안에서 가장 좋은 값. SD-VAE에서 REPA와의 FID 순위는 2M–4M step 사이에 바뀐다(Fig. 20a).
[10.notes.0] ImageNet 결과입니다. SD-VAE에서 4M step 기준 Self-Flow의 FID는 5.70으로, DINOv2에 정렬한 REPA의 5.89보다 0.19 낮습니다. 다만 IS와 Recall은 REPA가 더 높습니다.
[10.notes.1] RAE와 같은 semantic autoencoder를 써도 FID가 3.24에서 2.95로 내려갔습니다. 모두 CFG 없이 측정한 수치입니다.

## Slide 11 — Text-to-image 생성 지표
[11.title] Text-to-image 생성 지표
[11.message] 이 T2I 설정에서 Self-Flow는 DINOv2에 정렬한 REPA보다 FID와 FD-DINO가 낮고 CLIP score가 높았다.
[11.body.0.left.0.title] Text-to-image FID, 1M step (낮을수록 좋음)
[11.body.0.left.0.items.0.sub] 외부 모델 없음
[11.body.0.left.0.items.1.sub] 외부 모델 없음
[11.body.0.left.0.items.2.sub] DINOv2에 정렬
[11.body.0.left.0.items.3.sub] SigLIP 2에 정렬
[11.body.0.left.0.items.4.sub] 정렬 없음
[11.body.0.left.1.text] **Table 2** 약 625M, 내부 20M 쌍, SD-VAE, no CFG, 50 ODE steps. sFID는 SRA 8.05, REPA–SigLIP 2 8.13, Self-Flow 8.14.
[11.body.0.right.1.text] Fig. 1(a)의 약 2.8배는 REPA의 1M step FID에 도달하는 데 필요한 step 수를 비교한 값으로, teacher forward 비용은 포함하지 않는다.
[11.notes.0] Text-to-image에서도 Self-Flow의 FID가 3.61로 가장 낮습니다. DINOv2 feature로 잰 거리인 FD-DINO도 DINOv2에 직접 정렬한 REPA보다 낮습니다.
[11.notes.1] 표지의 2.8배 빠른 수렴은 같은 FID에 도달하기까지 필요한 step 수를 비교한 결과입니다. Self-Flow는 매 step teacher forward를 한 번 더 하므로, 연산량으로 비교하면 그 배율이 더 작아진다는 것이 제 해석입니다.

## Slide 12 — 비디오와 오디오 생성 지표
[12.title] 비디오와 오디오 생성 지표
[12.message] 논문이 고른 설정에서 Self-Flow의 비디오·오디오 지표가 모두 가장 낮았고, 외부 encoder의 효과는 encoder와 지표에 따라 달랐다.
[12.body.0.left.0.columns.0.label] 비디오
[12.body.0.left.1.text] **Table 3** 내부 6M 영상, Wan2.2 AE, 45프레임·192p, 600K step, 프레임별 FID. 학습 timestep의 5%는 [0.95, 1.00]에서 뽑는다(App. C).
[12.body.0.right.0.columns.0.label] 오디오 FAD
[12.body.0.right.1.text] **Table 4·5** FMA 10초, Songbloom AE, 350K step. 방법마다 trainshift를 골랐고(App. B), Self-Flow의 $R_M$ 0.50도 탐색으로 정했다. 모든 지표 no CFG.
[12.notes.0] 비디오에서는 Self-Flow의 FVD가 47.81로 가장 낮았습니다. 비디오 전용 encoder인 V-JEPA 2나 깊이 추정 모델 Depth Anything 3에 정렬한 REPA의 FVD는 오히려 vanilla보다 높았습니다.
[12.notes.1] 다만 비디오를 학습할 때는 timestep의 5%를 noise가 매우 높은 구간에서 따로 뽑습니다. 이 별도 샘플링을 빼면 Self-Flow의 프레임 FID가 나빠집니다. 이 결과는 분석에서 다시 보겠습니다.
[12.notes.2] 오디오의 FAD 지표 세 가지 모두 Self-Flow가 가장 낮습니다. 표 오른쪽 열에서 보듯 Self-Flow만 trainshift가 1.0입니다. 이 차이는 토론에서 다시 다루겠습니다.

## Slide 13 — 공유 backbone과 loss 가중치
[13.title] 공유 backbone과 loss 가중치
[13.message] 공유 backbone 실험에서는 시험한 가중치 다섯 가지에서 모두 Self-Flow의 이미지 FID, 비디오 FVD, 오디오 FAD가 Vanilla FM보다 낮았다.
[13.body.0.columns.0.label] 가중치 (이미지, 비디오, 오디오)
[13.body.0.columns.1.label] 이미지 ΔFID
[13.body.0.columns.2.label] 비디오 ΔFVD
[13.body.0.columns.3.label] 오디오 ΔFAD (CLAP)
[13.body.1.text] **Table 6** Δ = Self-Flow − Vanilla FM, 음수가 좋음. 약 625M, 1M step, no CFG, 이미지는 FLUX.2 AE. 강조 행(video-weighted): FID 3.35 → 3.19, FVD 62.7 → 58, FAD 160.1 → 157.4. 이 실험의 대조군은 Vanilla FM뿐이다.
[13.notes.0] 하나의 backbone으로 세 모달리티를 함께 학습했습니다. loss 가중치를 다섯 가지로 바꿔도 세 지표 모두 Self-Flow가 vanilla보다 좋았습니다.
[13.notes.1] 표에서 강조한 행은 비디오에 가중치를 많이 준 설정입니다. 다음 슬라이드의 로봇 실험에서는 이 checkpoint로 모델을 초기화했습니다. 공유 backbone 실험의 비교 대상은 vanilla뿐입니다.

## Slide 14 — Video-action 전이
[14.title] Video-action 전이
[14.message] 같은 RT-1 fine-tuning 뒤에도 Self-Flow 초기화의 이점은 두 물체를 다루거나 순서를 따라야 하는 과제에서 남았다.
[14.body.0.left.0.alt] Fig. 8(b). SIMPLER 네 과제의 성공률 레이더 차트. Self-Flow와 FM의 30K, 100K step 결과.
[14.body.0.left.0.caption] **Fig. 8(b)** SIMPLER 성공률. video-weighted 625M에서 RT-1(73.5K episode)로 fine-tuning
[14.body.0.right.0.items.0.items.0] 네 과제 모두 Self-Flow가 앞섬
[14.body.0.right.0.items.0.items.1] FM은 Open and Place 0%
[14.body.0.right.0.items.1.items.0] Pick Up Coke Can: 비슷하게 수렴
[14.body.0.right.0.items.1.items.1] Open/Close Drawer: FM이 소폭 앞섬
[14.body.0.right.0.items.1.items.2] Move Near: Self-Flow 50%, 격차 확대
[14.body.0.right.0.items.1.items.3] Open and Place: Self-Flow 29%, 격차 유지
[14.body.0.right.1.text] 과제별 평가 15·18·10·7회, checkpoint마다 2회 반복(App. E).
[14.notes.0] 멀티모달 checkpoint에서 시작해 로봇 데이터로 fine-tuning했습니다. 30K step에서는 네 과제 모두 Self-Flow가 앞섰고, FM은 Open and Place에 한 번도 성공하지 못했습니다.
[14.notes.1] 100K step에서는 Coke Can과 Drawer의 결과가 비슷해집니다. 그림으로는 Drawer에서 FM이 조금 앞섭니다. 반면 두 물체를 다루는 Move Near와 순서가 있는 Open and Place에서는 차이가 남습니다. 다만 Open and Place는 7회를 두 번 반복한 14회 평가여서 성공률은 대략적인 경향으로 봐야 합니다.

## Slide 15 — 생성 샘플의 정성 비교
[15.title] 생성 샘플의 정성 비교
[15.message] 논문은 글자의 판독성, 물체의 형태, 프레임 사이 신체 일관성을 서로 다른 예시로 보여 준다.
[15.body.0.reveals] 정성 예시를 하나씩 크게 보며 글자 철자, 물체 형태, 프레임 사이 일관성을 비교한다.
[15.body.0.states.0.label] 글자
[15.body.0.states.0.alt] Fig. 9 일부. FLUX 문구를 생성한 이미지 네 장. 위는 vanilla flow matching, 아래는 Self-Flow.
[15.body.0.states.0.title] 같은 문구의 철자
[15.body.0.states.0.text] 위 vanilla, 아래 Self-Flow. 4B multi-modal 모델, 고해상도 100K step.
[15.body.0.states.1.label] 이미지
[15.body.0.states.1.alt] Fig. 10(a) 일부. Vanilla, REPA, SRA, Self-Flow가 그린 파란 Vespa 스쿠터.
[15.body.0.states.1.title] 물체 형태와 세부
[15.body.0.states.1.text] Vanilla, REPA, SRA, Self-Flow 순. 약 625M T2I.
[15.body.0.states.2.label] 비디오
[15.body.0.states.2.alt] Fig. 10(b) 일부. 네 방법의 춤 영상 프레임을 두 줄로 다시 배치(위 Vanilla·REPA, 아래 SRA·Self-Flow).
[15.body.0.states.2.title] 프레임 사이 일관성
[15.body.0.states.2.text] baseline이 생성한 일부 프레임에서 팔다리가 사라진다. 위 Vanilla·REPA, 아래 SRA·Self-Flow. 약 625M, 6M 영상.
[15.body.0.mediaCaption] **Fig. 9 · 10** 정성 샘플은 50 steps, CFG 이미지 3.5, 비디오 5 (App. A.3). 이미지·비디오 탭은 원 그림의 한 예시만 잘라 크게 보였다.
[15.notes.0] 정성 결과는 탭으로 하나씩 보겠습니다. [1] 글자는 4B 모델의 결과로, 위가 vanilla, 아래가 Self-Flow입니다. 철자가 맞는지 보시면 됩니다.
[15.notes.1] [2] 이미지는 Vespa 예시만 잘라 크게 보였습니다. 네 방법의 차체 형태를 비교해 보시면 됩니다. [3] 비디오는 춤 영상 줄을 두 줄로 다시 배치했고, baseline이 생성한 일부 프레임에서 팔다리가 사라집니다. 모두 저자가 고른 예시라는 점은 감안해야 합니다.

## Slide 16 — 모델 크기와 학습 FLOPs
[16.title] 모델 크기와 학습 FLOPs
[16.message] 논문의 T2I sweep에서는 모델이 커질수록 Self-Flow와 REPA의 CLIP score 격차가 벌어졌다.
[16.body.0.reveals] 같은 sweep에서 학습 step과 training FLOPs 두 축을 써도 625M Self-Flow와 1B REPA의 CLIP score 순위가 같은지 비교
[16.body.0.states.0.alt] Fig. 6(a). 네 모델 크기에서 Self-Flow와 REPA의 학습 step별 CLIP score.
[16.body.0.states.0.title] 가로축: 학습 step
[16.body.0.states.0.text] 625M Self-Flow가 1M step에서 1B REPA보다 높은 CLIP score.
[16.body.0.states.1.alt] Fig. 6(b). 같은 결과를 training FLOPs 축으로 그린 그래프.
[16.body.0.states.1.title] 가로축: training FLOPs
[16.body.0.states.1.text] FLOPs 축에서도 625M Self-Flow가 1B REPA보다 높다. FLOPs 산정 방식은 본문에 없다.
[16.body.0.mediaCaption] **Fig. 6** 290M, 420M, 625M, 1B = 층 수 8, 14, 21, 28. 내부 T2I 20M 쌍, SD-VAE, no CFG. 비교 지표는 CLIP score뿐이다.
[16.notes.0] 모델 크기를 290M에서 1B까지 키우면서 CLIP score를 비교했습니다. [1] step 축에서 625M Self-Flow가 1B REPA보다 높습니다.
[16.notes.1] [2] FLOPs를 가로축에 놓아도 앞서 비교한 두 모델 중 Self-Flow의 CLIP score가 더 높습니다. 다만 teacher forward를 FLOPs에 어떻게 반영했는지는 본문에 나오지 않고, 이 sweep에서 보고한 지표는 CLIP score뿐입니다.

## Slide 17 — 층별 ImageNet linear probe
[17.title] 층별 ImageNet linear probe
[17.message] Self-Flow의 linear probe 정확도는 모든 층에서 vanilla보다 높았고, 차이는 앞쪽 층과 중간층에서 컸다.
[17.body.0.left.0.alt] Fig. 4(b). 층별 ImageNet linear probe top-1 정확도. 모든 층에서 Self-Flow가 높고, 차이는 4–16층에서 크고 20–28층에서 작다.
[17.body.0.left.0.caption] **Fig. 4(b)** ImageNet, SiT-XL 약 675M, 2M step
[17.body.0.right.0.items.0.heading] 4–16층
[17.body.0.right.0.items.0.items.0] Self-Flow가 크게 높음
[17.body.0.right.0.items.0.items.1] 논문이 강조한 구간
[17.body.0.right.0.items.1.heading] 20–28층
[17.body.0.right.0.items.1.items.0] 둘 다 정점을 지나 하락
[17.body.0.right.0.items.1.items.1] 차이는 작아짐
[17.body.0.right.1.text] linear probe는 클래스 분리도를 잰다. student가 noise 수준이 낮은 토큰을 단서로 쓰는지는 직접 재지 않는다.
[17.notes.0] feature가 실제로 개선됐는지는 층별 linear probe로 확인했습니다. 모든 층에서 Self-Flow의 정확도가 높고, 특히 4층부터 16층까지 차이가 큽니다.
[17.notes.1] 20층 이후에는 두 모델 모두 정확도가 내려가고 차이도 작아집니다. 또 linear probe는 클래스 분리도를 잴 뿐, 논문이 제시한 기전대로 student가 noise 수준이 낮은 토큰을 쓰는지는 직접 재지 않습니다.

## Slide 18 — Self-Flow 구성요소 ablation
[18.title] Self-Flow 구성요소 ablation
[18.message] ImageNet ablation에서 representation loss를 뺐을 때 FID가 가장 크게 나빠졌고, mask를 빼거나 두 번째 timestep을 제한해도 나빠졌다.
[18.body.0.left.0.alt] Fig. 11(a). Ablation 설정별 FID 학습 곡선. representation loss를 뺀 설정이 가장 높다.
[18.body.0.left.0.caption] **Fig. 11(a)** ImageNet, SiT-XL 약 675M, no CFG, 200K–600K step
[18.body.0.right.0.items.0] $\mathcal{L}_{\mathrm{rep}}$ 제거: FID 4점 넘게 악화
[18.body.0.right.0.items.1] mask 제거($\mathcal{L}_{\mathrm{rep}}$ 유지): 1점 넘게 악화
[18.body.0.right.0.items.2] $s$를 $t$보다 최대 0.2 낮은 범위로 제한. mask 제거와 비슷하게 FID 악화.
[18.body.0.right.0.items.3] cosine 대신 $\ell_1$: 후반 FID가 내려가지 않음
[18.body.0.right.1.text] 수치는 §4.4 본문 서술이고 측정 step과 표는 없다. $\ell_1$에서 후반 FID가 낮아지지 않은 원인(feature norm 증가)은 저자 설명.
[18.notes.0] 구성요소를 하나씩 뺀 결과입니다. representation loss를 빼면 FID가 4점 넘게 나빠집니다. FID 악화 폭이 이 설정에서 가장 큽니다.
[18.notes.1] representation loss는 두고 mask만 빼도 FID가 1점 넘게 나빠집니다. 이를 근거로 저자들은 단순한 층간 정렬만으로는 부족하다고 주장합니다. 두 번째 timestep을 t와 거의 같게 제한해도 mask를 뺐을 때만큼 FID가 나빠집니다. 이 ablation은 모두 ImageNet에서만 했습니다.

## Slide 19 — Timestep 분포와 low-SNR 구간
[19.title] Timestep 분포와 low-SNR 구간
[19.message] Self-Flow의 이점은 T2I에서 timestep을 어떤 분포로 뽑는지, 비디오에서 noise 수준이 높은 구간을 따로 샘플링하는지에 따라 달라졌다.
[19.body.0.left.0.alt] Fig. 11(b). REPA와 Self-Flow를 logit-normal과 uniform 분포로 학습한 FID 곡선. uniform에서 둘 다 낮고 차이가 더 크다.
[19.body.0.left.0.caption] **Fig. 11(b)** T2I 약 625M, SD-VAE, no CFG, 최대 1M step. logit-normal은 trainshift 1.78
[19.body.0.right.0.items.0.items.0] uniform에서 두 방법 모두 FID 개선
[19.body.0.right.0.items.0.items.1] Self-Flow와 REPA의 차이도 커짐
[19.body.0.right.0.items.1.heading] 비디오
[19.body.0.right.0.items.1.items.0] timestep 5%를 [0.95, 1.00]에서 추출
[19.body.0.right.0.items.1.items.1] 이 처리를 빼면 Self-Flow의 프레임 FID 악화(FVD는 여전히 가장 낮음)
[19.body.0.right.1.text] 저자 가설: Dual-Timestep에서는 샘플 전체의 SNR이 평균 부근에 모여 noise 수준이 높은 구간에서 학습이 덜 이뤄진다.
[19.notes.0] Self-Flow의 이점은 timestep 분포에 따라 달라집니다. T2I에서 uniform 분포로 바꿨을 때 두 방법 모두 FID가 낮아졌고, FID 차이도 더 커졌습니다.
[19.notes.1] 비디오의 기본 분포에서는 noise 수준이 매우 높은 구간에서 timestep이 거의 뽑히지 않습니다. 그래서 timestep의 5%를 이 구간에서 따로 뽑았습니다. 이 별도 샘플링을 빼면 Self-Flow의 프레임 FID가 나빠집니다. 저자들은 Dual-Timestep을 쓰면 SNR이 평균 부근에 모이기 때문이라고 추정합니다.

## Slide 20 — 한계와 검증 범위
[20.title] 한계와 검증 범위
[20.message] 실험마다 대조군, 평가 지표, 데이터 범위가 달라서 결론을 다른 조건으로 그대로 넓히기 어렵다.
[20.body.0.groups.0.heading] 대조군
[20.body.0.groups.0.items.0] 멀티모달, 로봇, 4B 글자, RAE, FLUX.2 AE 실험은 Vanilla FM과만 비교
[20.body.0.groups.0.items.1] 이 설정들에 SRA·REPA 비교는 없다
[20.body.0.groups.1.heading] 측정 범위
[20.body.0.groups.1.items.0] scaling에서는 CLIP score만 보고했다. FID 결과나 SRA와의 비교는 없다.
[20.body.0.groups.1.items.1] 구성요소 ablation과 linear probe는 ImageNet만
[20.body.0.groups.1.items.2] $\gamma$ sweep과 이미지·비디오 $R_M$ ablation은 없고, 오디오도 $R_M$별 비교는 따로 보고하지 않았다
[20.body.0.groups.2.heading] 비용과 재현
[20.body.0.groups.2.items.0] 학습 step마다 teacher forward 추가. FLOPs 산정식은 없다.
[20.body.0.groups.2.items.1] T2I·T2V는 내부 데이터로 평가
[20.body.0.groups.2.items.2] 공개 코드는 ImageNet 추론뿐, 학습 코드는 없다
[20.notes.0] 결과를 다른 조건에 적용할 때 주의할 점은 세 가지입니다.
[20.notes.1] 먼저 멀티모달, 로봇, 4B 모델 등 규모가 큰 실험은 vanilla만 비교 대상으로 삼았습니다. 둘째로 ablation과 linear probe는 ImageNet에서만 했고, scaling은 CLIP score만 봤습니다. 셋째로 teacher forward 비용이 들고, 공개된 코드는 ImageNet 추론 코드뿐이라 학습을 그대로 재현하기는 어렵습니다.

## Slide 21 — 정리와 토론
[21.title] 정리와 토론
[21.message] 실험 결과와 ablation은 두 timestep 배정과 EMA teacher 정렬을 함께 쓰는 방법을 뒷받침한다. 다만 이득이 어디서 오는지, 학습 시간을 맞추면 얼마나 남는지는 추가 비교가 필요하다.
[21.body.0.groups.0.heading] 정리
[21.body.0.groups.0.items.0] 두 timestep 중 하나를 토큰마다 배정하고, noise가 더 적은 입력에서 얻은 EMA teacher의 feature를 정렬 목표로 사용
[21.body.0.groups.0.items.1] 이미지·비디오·오디오 생성 지표가 좋아졌고, ImageNet probe 정확도는 앞쪽 층과 중간층에서 많이 올랐다
[21.body.0.groups.0.items.2] 이득의 크기는 timestep 분포와 평가 조건에 따라 달라진다
[21.body.0.groups.1.heading] 토론
[21.body.0.groups.1.items.0] App. A.3은 $p(t)$를 학습 전에 정해 대조군에 똑같이 쓴다고 적었다. 오디오(App. B)는 방법마다 shift를 탐색해 대조군 0.75, Self-Flow 1.0을 골랐다. 같은 trainshift면 FAD 차이는 얼마나 남는가?
[21.body.0.groups.1.items.1] 같은 FAD를 오디오 설정 선택과 최종 결과 보고에 사용했다. 다른 검증 데이터로 설정을 골라도 순위가 같은가?
[21.body.0.groups.1.items.2.text] Jiang et al.(2026)은 noise가 다른 토큰 사이 attention을 막아도 성능이 유지된다고 보고했다. 이득은 noise가 적은 토큰의 정보를 참고하는 데서 오는가, noise 수준을 섞는 데이터 증강 효과인가?
[21.body.0.groups.1.items.3.text] teacher forward가 추가된다. 학습 시간을 같게 맞추면 256토큰 이미지와 약 3K 토큰 비디오에서 이득이 얼마나 남는가?
[21.notes.0] 정리하면, Self-Flow는 토큰마다 두 noise 수준 중 하나를 주고, noise가 더 적은 입력을 받은 EMA teacher의 feature에 맞춥니다. 여러 모달리티에서 생성 지표가 좋아졌습니다.
[21.notes.1] 토론 주제는 네 가지입니다. 첫째, 부록 A.3은 noise 분포를 학습 전에 정해 모든 대조군에 똑같이 쓴다고 설명합니다. 그런데 오디오에서는 방법마다 shift를 탐색했고, 대조군은 0.75, Self-Flow는 1.0이 골라졌습니다. 둘째, 오디오 설정을 고를 때 쓴 지표로 최종 결과도 보고했습니다.
[21.notes.2] 셋째, 외부 연구에서 SRA 저자들은 올해 7월에 noise가 다른 토큰 사이의 attention을 막아도 성능이 유지된다고 보고했습니다. 그러면 이득이 정말 noise가 적은 토큰의 정보에서 오는지 다시 물어볼 수 있습니다. 넷째는 제 해석에서 나온 질문입니다. 학습 시간이 같을 때 이득이 얼마나 남는지 비교해 볼 수 있습니다.

## Slide 22 — 감사합니다
[22.title] 감사합니다
[22.links.1] 코드 · github.com/black-forest-labs/Self-Flow (ImageNet 256×256 추론, Hugging Face Hila/Self-Flow)
[22.notes.0] 들어 주셔서 감사합니다. 특히 어떤 실험을 더 하면 Self-Flow의 이득이 어디서 오는지 가려낼 수 있을지 의견을 듣고 싶습니다.

