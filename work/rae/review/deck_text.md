# Deck text — Diffusion Transformers with Representation Autoencoders

## Slide 1 — Diffusion Transformers with Representation Autoencoders
[1.subtitle] 고정한 표현 인코더가 출력한 latent로 DiT를 학습하는 RAE
[1.figure.alt] Fig. 7 위 두 줄. DiT^DH-XL이 생성한 512×512 샘플: 흰 앵무새, 바다거북, 등대, 햄버거, 클래스마다 여러 장.
[1.figure.caption] **Fig. 7** DiT^{DH}-XL(DINOv2-B)의 512×512 샘플, AutoGuidance
[1.notes.0] 오늘 다룰 논문은 NYU의 Diffusion Transformers with Representation Autoencoders입니다.
[1.notes.1] 표지의 이미지는 이 논문의 모델이 512×512로 생성한 샘플입니다. 사전학습한 표현 인코더를 고정하고, 그 출력을 압축하지 않은 채 확산 모델의 latent로 씁니다.

## Slide 2 — RAE와 DiT^{DH} 요약
[2.title] RAE와 DiT^{DH} 요약
[2.message] 논문은 고정한 표현 인코더에 ViT 디코더를 붙인다. 확산 모델이 인코더의 고차원 토큰을 학습하도록 DiT의 폭, 노이즈 schedule, 디코더, head를 조정한다.
[2.body.0.text] VAE 대신 고정한 표현 인코더를 쓰고, 그 고차원 latent에서 DiT가 학습되도록 네 가지를 바꾼다.
[2.body.1.items.0.title] RAE 복원
[2.body.1.items.0.text] 고정한 DINOv2-B·SigLIP2-B·MAE-B + ViT 디코더. 셋 모두 SD-VAE보다 낮은 rFID
[2.body.1.items.1.title] 고차원 토큰의 확산 학습 설정
[2.body.1.items.1.text] 토큰 차원 이상의 DiT 폭, 실효 차원에 따른 schedule shift, 노이즈 증강 디코더
[2.body.1.items.2.text] 얕고 넓은 DDT head. ImageNet 256×256, guidance 없이 gFID **1.51** (800 epoch)
[2.notes.0] 이 논문이 하는 일은 세 가지입니다. 첫째, 고정한 표현 인코더의 토큰에서 이미지를 복원하는 디코더를 학습합니다.
[2.notes.1] 둘째, 토큰 차원이 768로 높아서 확산 학습에서 세 가지를 조정합니다. 셋째, 넓은 head를 붙인 DiT^{DH}로 연산량 대비 성능을 높입니다.
[2.notes.2] 대표 수치 1.51은 DINOv2-B의 토큰으로 DiT^{DH}-XL을 800 epoch 학습한 뒤, 클래스마다 같은 수의 이미지를 guidance 없이 생성해 잰 값입니다.

## Slide 3 — 잠재 확산과 표현 학습 관련 연구
[3.title] 잠재 확산과 표현 학습 관련 연구
[3.message] 이 논문은 압축 latent에서 확산을 학습하는 연구와 사전학습 표현을 복원이나 생성에 쓰는 연구를 연결한다.
[3.body.0.groups.0.heading] 압축 latent의 확산
[3.body.0.groups.0.items.1] SD-VAE: 256² 이미지 → 32²×4 latent
[3.body.0.groups.1.heading] 표현으로 tokenizer 개선
[3.body.0.groups.1.items.1] VAE를 표현에 정렬하거나 MAE식 목표 추가
[3.body.0.groups.2.heading] 표현으로 생성 개선
[3.body.0.groups.2.items.1] DiT 내부 표현을 외부 인코더에 정렬(REPA·DDT·REG), DINOv2 PCA를 함께 생성(ReDi)
[3.body.1.text] 인코더 자체를 표현 인코더로 바꾸면 복원과 확산이 모두 되는가?
[3.notes.0] LDM, DiT, SiT는 autoencoder가 만든 압축 latent에서 확산을 학습합니다. SD-VAE는 256×256 이미지를 32×32×4로 줄입니다.
[3.notes.1] VA-VAE, MAETok 같은 연구는 VAE를 학습할 때 표현 정렬이나 MAE식 목표를 더해 tokenizer를 개선합니다. REPA, DDT, REG는 생성 모델의 중간 층을 외부 인코더에 맞춥니다.
[3.notes.2] 이 논문에서는 인코더 자체를 표현 인코더로 바꿔도 복원과 확산이 모두 가능한지 묻습니다.

## Slide 4 — 같은 이미지, 다른 latent: SD-VAE와 RAE
[4.title] 같은 이미지, 다른 latent: SD-VAE와 RAE
[4.message] RAE는 SD-VAE의 압축 latent 대신 고정한 표현 인코더의 패치 토큰을 그대로 쓴다. DiT가 받는 토큰 수는 256개로 같고, 토큰 하나의 차원이 16에서 768로 48배가 된다.
[4.body.0.reveals] 격자가 토큰이 되고 그 토큰이 48배로 늘어나는 것을 따라가면, 두 autoencoder에서 DiT의 토큰 수는 같고 토큰 하나의 차원만 다르다는 것이 보인다.
[4.body.0.beats.0.text] U-Net 인코더가 256×256 이미지를 32×32×4로 압축
[4.body.0.beats.1.title] DiT 토큰
[4.body.0.beats.1.text] 2×2씩 묶어 토큰 256개, 토큰마다 16차원
[4.body.0.beats.2.text] 고정 DINOv2-B의 패치 토큰 그대로: 256개 × 768차원
[4.body.0.beats.3.title] 두 질문
[4.body.0.beats.3.text] ① 이 토큰에서 복원이 되나 ② 이 차원에서 확산이 되나
[4.body.0.caption] **Fig. 2**를 바탕으로 다시 그림. 막대 8개가 토큰 256개, 막대 길이가 토큰 차원. GFLOPs는 256×256 이미지 한 장
[4.notes.0] 먼저 SD-VAE를 쓰는 DiT입니다. U-Net 인코더가 256×256 이미지를 32×32×4 latent로 압축합니다.
[4.notes.1] [1] DiT는 이 latent를 2×2씩 묶어 읽습니다. 토큰은 256개이고, 토큰 하나는 2×2×4, 16차원입니다.
[4.notes.2] [2] RAE는 인코더를 고정한 DINOv2-B로 바꿉니다. 패치 토큰을 압축하지 않고 그대로 쓰니 토큰 수는 256개로 같고, 토큰 하나가 768차원으로 48배가 됩니다. 디코더는 ViT로 바뀌고, 연산량은 인코더가 135에서 22, 디코더가 310에서 106 GFLOPs입니다.
[4.notes.3] [3] 그래서 두 가지를 확인해야 합니다. 의미를 학습한 인코더는 고수준 정보만 남겨 복원을 못 한다는 통념이 있고, 확산은 고차원 latent에서 잘 안 된다는 통념이 있습니다. 논문은 두 통념을 차례로 검증합니다.

## Slide 5 — RAE의 복원·생성 경로와 바꾸는 네 곳
[5.title] RAE의 복원·생성 경로와 바꾸는 네 곳
[5.message] 복원은 이미지에서 얻은 토큰에서, 생성은 DiT가 잡음에서 만든 토큰에서 시작해 같은 디코더로 간다. 고차원 때문에 DiT 폭, noise schedule, 디코더 학습을 바꾸고 DDT head를 더한다.
[5.body.0.reveals] 두 경로를 차례로 그리면 복원과 생성이 같은 디코더를 쓰되 출발점(이미지의 토큰과 잡음)이 다르다는 것, 그리고 네 가지 변경이 각각 어디에 붙는지가 보인다.
[5.body.0.beats.0.title] 복원 경로
[5.body.0.beats.0.text] 고정 인코더의 토큰을 ViT 디코더가 이미지로 복원
[5.body.0.beats.1.title] 생성 경로
[5.body.0.beats.1.text] DiT가 잡음에서 토큰을 만들고, 같은 디코더가 이미지로 바꾼다
[5.body.0.beats.2.title] 고차원에서 바꾸는 세 곳
[5.body.0.beats.2.text] DiT 폭, noise schedule, 디코더 학습
[5.body.0.beats.3.text] 얕고 넓은 DDT head가 DiT 출력과 잡음 섞인 입력을 함께 받는다
[5.body.0.caption] Sec. 3–5를 바탕으로 그림. ① 복원은 6–7장, ② 생성과 네 가지 변경은 8–14장
[5.notes.0] RAE를 쓰는 방법은 두 갈래입니다. 위는 복원입니다. 고정 인코더가 이미지에서 만든 토큰을 ViT 디코더가 다시 이미지로 바꿉니다.
[5.notes.1] [1] 아래는 생성입니다. DiT가 잡음에서 같은 모양의 토큰을 만들고, 같은 디코더가 그것을 이미지로 바꿉니다.
[5.notes.2] [2] 토큰이 768차원이라서 세 곳을 바꿉니다. DiT의 폭은 토큰 차원 이상이어야 하고, noise schedule은 차원에 맞춰 옮기고, 디코더는 학습할 때 노이즈를 섞은 토큰도 보게 합니다.
[5.notes.3] [3] 마지막으로 DiT 뒤에 얕고 넓은 DDT head를 붙인 것이 DiT^{DH}입니다. head는 DiT의 출력과 잡음 섞인 입력을 함께 받습니다. 이제 위쪽, 복원부터 보겠습니다.

## Slide 6 — RAE: 고정 인코더와 ViT 디코더
[6.title] RAE: 고정 인코더와 ViT 디코더
[6.message] RAE는 사전학습한 ViT의 patch 토큰을 고정하고, 그 토큰에서 픽셀을 복원하는 ViT 디코더만 학습한다.
[6.body.0.left.0.items.0] 256×256 입력 → **256 토큰 × 768 채널**, 압축 없음
[6.body.0.left.0.items.1] DINOv2-B 입력은 224×224로 보간 (인코더 patch 14, 디코더 16)
[6.body.0.left.0.items.2] [CLS]·[REG] 토큰은 버리고 patch 토큰만 정규화
[6.body.0.left.0.items.3] 디코더 손실: L1 + LPIPS + GAN, 판별자는 고정한 DINO-S/8
[6.body.0.right.0.columns.0.label] 디코더
[6.body.0.right.1.text] **Table 1b** 인코더 DINOv2-B, ImageNet-1K val. GFLOPs는 디코더
[6.notes.0] RAE의 인코더는 학습하지 않습니다. 256×256 이미지에서 768채널 토큰 256개가 나오고, 이것을 압축하지 않고 latent로 씁니다.
[6.notes.1] DINOv2는 patch 크기가 14라서 입력을 224로 줄입니다. 디코더는 patch 16으로 이미지를 원래 해상도로 복원합니다.
[6.notes.2] 디코더는 L1, LPIPS, GAN 손실로 학습하고, 판별자로 고정한 DINO-S/8을 씁니다. 오른쪽 표에서 가장 작은 ViT-B 디코더도 SD-VAE보다 rFID가 낮고, 연산량은 14분의 1입니다.

## Slide 7 — 세 인코더의 복원과 linear probe
[7.title] 세 인코더의 복원과 linear probe
[7.message] 세 고정 인코더에 디코더를 붙인 RAE는 모두 SD-VAE보다 rFID가 낮고, 인코더의 표현 품질은 그대로 남는다.
[7.body.0.left.0.columns.0.label] 인코더
[7.body.0.left.1.text] **Table 1a · d** ImageNet-1K val rFID, linear probe Top-1. 디코더 ViT-XL
[7.body.0.right.0.alt] Fig. 8. 두 행(앵무새, 버스) × 다섯 열. 왼쪽부터 입력, RAE(DINOv2-B), RAE(SigLIP2-B), RAE(MAE-B), SD-VAE의 복원. 다섯 열 모두 입력과 거의 같아 보인다.
[7.body.0.right.0.caption] **Fig. 8** 왼쪽부터 입력 · DINOv2-B · SigLIP2-B · MAE-B · SD-VAE
[7.body.1.text] ①은 ImageNet 복원에서 반박된다. 남은 질문: 복원이 좋으면 생성도 좋은가? (19번)
[7.notes.0] 세 인코더 모두 SD-VAE보다 rFID가 낮고, 그중 MAE-B가 0.16으로 가장 낮습니다. DINOv2 크기를 S, B, L로 바꿔도 rFID는 0.5 안팎으로 비슷합니다.
[7.notes.1] RAE는 인코더를 고정하므로 linear probe 정확도가 원래 인코더에서 측정한 값과 같습니다. SD-VAE latent의 정확도는 8%에 그칩니다.
[7.notes.2] 오른쪽 복원 예시에서 다섯 열의 차이는 눈으로 거의 보이지 않습니다. 첫 번째 통념은 ImageNet 복원에서는 반박됩니다. 다만 복원이 좋은 인코더가 생성에도 좋은지는 19번에서 다시 보겠습니다.

## Slide 8 — 고차원 RAE latent에서의 기본 DiT
[8.title] 고차원 RAE latent에서의 기본 DiT
[8.message] 토큰 수를 똑같이 256개로 맞춰도, 기본 DiT 설정에서는 RAE의 gFID가 SD-VAE보다 훨씬 높다.
[8.body.0.left.0.columns.0.label] 모델
[8.body.0.left.1.text] **Table 2** gFID. ImageNet 256×256, 80 epoch, guidance 없음. RAE는 DINOv2-B(patch 1), SD-VAE는 patch 2 — 둘 다 256 토큰
[8.body.0.right.0.items.0.title] DiT 설계
[8.body.0.right.0.items.0.text] 저차원 VAE 토큰에 맞춘 DiT 설계가 768차원 토큰에도 맞는가
[8.body.0.right.0.items.1.text] 이미지·VAE 입력에서 나온 schedule이 고차원 토큰에도 맞는가
[8.body.0.right.0.items.2.title] 디코더
[8.body.0.right.0.items.2.text] 노이즈를 섞지 않은 latent로만 학습한 디코더가 생성된 latent를 복원하는가
[8.notes.0] RAE에는 patch 1을, SD-VAE에는 patch 2를 써서 DiT가 보는 토큰 수를 똑같이 256개로 맞췄습니다. 연산량도 거의 같습니다.
[8.notes.1] 그런데 기본 DiT 설정으로 학습하면 RAE는 DiT-S에서 215.76으로 사실상 실패하고, XL로 키워도 23.08로 SD-VAE의 7.13보다 나쁩니다.
[8.notes.2] 저자들은 DiT의 폭, 노이즈 schedule, 디코더가 원인일 수 있다고 봅니다. 다음 여섯 장에서 세 가지를 하나씩 검토합니다.

## Slide 9 — 한 이미지 과적합: 폭과 깊이
[9.title] 한 이미지 과적합: 폭과 깊이
[9.message] DiT 폭이 토큰 차원 768 이상이어야 이미지 한 장에 과적합할 수 있다. 폭이 384일 때 깊이만 늘리면 손실은 0.5 부근에 머문다.
[9.body.0.left.0.alt] Fig. 3 왼쪽. 깊이를 고정하고 DiT 폭 d를 384, 512, 640, 768, 896으로 바꾼 단일 이미지 과적합 손실. 관측 손실은 384에서 약 0.5, 512에서 0.35, 640에서 0.18로 내려가고 768과 896에서 0에 가깝다. 빨간 점선 이론선 max(1 − d/768, 0)과 겹친다. d < 768의 생성 앵무새는 뭉개지고 d ≥ 768에서는 입력과 같다.
[9.body.0.left.0.caption] **Fig. 3 왼쪽** 깊이 고정, 폭 $d$를 바꿈
[9.body.0.right.0.alt] Fig. 3 오른쪽. 폭 384를 고정하고 깊이를 4, 12, 16, 24로 바꾼 손실. 네 점 모두 이론선 0.5 부근에 머물고, 생성 앵무새에는 모두 아티팩트가 남는다.
[9.body.0.right.0.caption] **Fig. 3 오른쪽** 폭 384 고정, 깊이를 바꿈
[9.body.1.text] DINOv2-B 토큰 $n=768$, 두 패널 같은 손실 축(0–0.5). 이미지 3장 × 3회 평균, 1,200 step (App. F). 점선은 다음 장의 하한
[9.notes.0] 원인을 확인하려고 저자들은 한 번에 이미지 한 장으로만 모델을 학습해 과적합을 시도합니다. 이미지 세 장에 대해 각각 세 번씩 반복한 결과를 평균했습니다.
[9.notes.1] 왼쪽은 깊이를 고정하고 폭을 바꾼 결과입니다. 폭이 토큰 차원 768보다 작으면 이미지 한 장에도 과적합하지 못합니다. 폭이 768 이상이면 손실이 0에 가깝게 내려가고 입력 이미지를 거의 그대로 복원합니다.
[9.notes.2] 오른쪽은 폭을 384로 고정하고 층을 24개까지 늘린 결과입니다. 손실은 0.5 부근에 머뭅니다. 이 실험에서는 층을 늘려 모델 용량을 키워도 좁은 폭이 손실을 제한합니다. 빨간 점선의 근거는 다음 장에서 설명하겠습니다.

## Slide 10 — Theorem 1: DiT 폭과 토큰 차원
[10.title] Theorem 1: DiT 폭과 토큰 차원
[10.message] 출력 투영의 rank가 토큰 차원보다 작으면 velocity 예측 손실에 하한이 생긴다. Table 3에서 수렴한 경우는 모두 폭이 토큰 차원 이상이다.
[10.body.0.left.0.symbols.0.1] 토큰 차원 (DINOv2-B: 768)
[10.body.0.left.0.symbols.1.1] DiT 폭
[10.body.0.left.0.symbols.2.1] $\varepsilon-x$ 공분산의 고유값 (내림차순)
[10.body.0.left.1.text] 한 이미지면 $\lambda_i=1$, 차원당 평균 손실의 하한 $(n-d)/n$: $d=384$에서 0.5
[10.body.0.right.0.columns.0.label] 인코더 ($n$)
[10.body.0.right.1.text] **Table 3** 한 이미지 과적합 손실. 폭 S 384·B 768·L 1024. ○ 수렴, × 실패
[10.notes.0] DiT는 입력을 폭 d로 투영하고 마지막에 다시 n차원으로 투영합니다. 출력 투영 B의 rank가 d 이하이므로, 모델이 내놓는 velocity는 d차원 부분공간을 벗어나지 못합니다.
[10.notes.1] 그런데 학습 목표인 ε − x에는 모든 방향으로 퍼진 Gaussian noise가 들어 있습니다. 그 부분공간 밖의 분산이 그대로 손실의 하한으로 남습니다.
[10.notes.2] 이미지가 한 장이면 고유값이 모두 1이어서, 차원당 평균 손실의 하한은 (n − d)/n입니다. 폭 384와 토큰 차원 768을 대입하면 앞 그림의 0.5가 나옵니다.
[10.notes.3] 오른쪽 표에서 수렴한 칸은 모두 폭이 토큰 차원 이상입니다. 이 정리는 표현 가능성에 대한 결과이고, 생성 품질은 실험으로 확인합니다. 이후 실험은 DINOv2-B에 폭 1,152인 DiT-XL을 씁니다.

## Slide 11 — 실효 차원에 따른 schedule shift
[11.title] 실효 차원에 따른 schedule shift
[11.message] 토큰 수와 채널 수를 곱한 실효 차원에 따라 timestep을 조정하면, 같은 RAE DiT-XL의 gFID가 23.08에서 4.81로 내려간다.
[11.body.0.left.0.symbols.0.1] 기준 차원 4,096 (Esser et al., 2024)
[11.body.0.left.0.symbols.1.1] 실효 차원 = 토큰 수 × 채널 수 = 256 × 768 = 196,608
[11.body.0.left.0.symbols.2.1] $\sqrt{48}\approx 6.93$ → $t_n=0.5$이면 $t_m\approx0.87$
[11.body.0.left.1.text] $t=1$은 순수 노이즈. $m$, $\alpha$, 0.87은 정의에서 계산
[11.body.0.right.0.body.1.text] **Table 4** DINOv2-B RAE, DiT-XL, 80 epoch, 노이즈 증강 전
[11.notes.0] 노이즈 수준이 같을 때 해상도가 높을수록 정보 손실이 적다는 점은 이미 알려져 있습니다. 그래서 timestep을 해상도에 따라 조정해 왔습니다.
[11.notes.1] 저자들은 해상도에 따른 timestep 조정을 실효 차원에 따른 조정으로 일반화합니다. 실효 차원은 토큰 수와 채널 수의 곱입니다. DINOv2-B RAE의 실효 차원은 기준의 48배이고, α는 약 6.93입니다.
[11.notes.2] 그러면 기준 timestep 0.5가 약 0.87로 바뀌어 노이즈가 훨씬 많이 섞입니다. 이 한 가지 변경으로 gFID가 23.08에서 4.81로 내려갑니다.

## Slide 12 — 노이즈 증강 디코더
[12.title] 노이즈 증강 디코더
[12.message] 디코더를 학습할 때 latent에 노이즈를 섞으면 생성 gFID는 낮아지고, 노이즈를 섞지 않은 latent를 복원할 때의 rFID는 조금 높아진다.
[12.body.0.left.0.symbols.0.1] 고정 인코더의 출력 latent
[12.body.0.left.0.symbols.1.1] 디코더 학습 노이즈 세기 (기본 0.8)
[12.body.0.left.1.text] 인코더 latent에 노이즈를 섞어 학습해, 확산이 생성한 latent에도 대응
[12.body.0.right.1.text] **Table 5 · 15c** DINOv2-B RAE, shift 적용 DiT-XL, 80 epoch
[12.notes.0] VAE 디코더는 연속 분포에서 뽑은 latent로 학습하지만, RAE 디코더는 학습 이미지에서 얻은 latent에 노이즈를 섞지 않고 그대로 학습합니다. 확산 모델이 만든 latent는 학습 이미지의 latent에서 조금씩 벗어나 있을 수 있습니다.
[12.notes.1] 그래서 디코더를 학습할 때 latent에 Gaussian noise를 더하고, 노이즈 세기 σ도 매번 무작위로 뽑습니다.
[12.notes.2] 표에서 τ를 키우면 gFID는 내려가고 rFID는 올라갑니다. 기본값 0.8에서 gFID는 4.81에서 4.28로 0.53 낮아지고, rFID는 0.08 높아집니다.

## Slide 13 — DiT^{DH}: 얕고 넓은 DDT head
[13.title] DiT^{DH}: 얕고 넓은 DDT head
[13.message] DiT^{DH}는 backbone의 폭을 유지한다. 노이즈가 섞인 latent를 직접 받는 2층 head(폭 2,048)가 폭 조건을 만족한다.
[13.body.0.left.0.alt] Fig. 5. x_t, t, y가 DiT로 들어가고, DiT 출력과 x_t, t가 오른쪽의 세로로 긴 DDT Head로 들어가 velocity v_t를 낸다.
[13.body.0.left.1.text] 파라미터: DiT^{DH}-XL 839M, VAE 기반 DiT-XL 675M (Table 8)
[13.body.0.right.0.columns.0.label] head 깊이 × 폭
[13.body.0.right.1.text] **Table 16** DINOv2-B RAE, DiT-XL backbone(28층, 폭 1152), 80 epoch
[13.notes.0] Theorem 1의 폭 조건을 만족하려면 폭이 토큰 차원 이상이어야 합니다. backbone 전체를 넓히면 연산량은 폭의 제곱에 비례해 늘어납니다.
[13.notes.1] DiT^{DH}는 기존 DiT에 얕고 넓은 head를 추가합니다. head는 backbone 출력 z_t와 노이즈가 섞인 latent x_t를 직접 받아 velocity를 냅니다.
[13.notes.2] 오른쪽 표에서 2층·폭 2,048 head가 비슷한 연산량의 6층·폭 1,152 head보다 낫고, 4층으로 늘려도 좋아지지 않습니다. 표에는 head의 GFLOPs만 나와 있습니다. 전체 파라미터 수는 839M으로 VAE 기반 DiT-XL보다 164M 많습니다.

## Slide 14 — 설계 변경을 차례로 적용한 gFID
[14.title] 설계 변경을 차례로 적용한 gFID
[14.message] 같은 80 epoch 조건에서 schedule shift를 적용할 때 gFID가 가장 크게 내려간다. 이후 노이즈 증강과 DiT^{DH}(DDT head와 전용 최적화)를 적용하면 gFID가 더 낮아진다.
[14.body.0.reveals] 막대를 하나씩 더하면 설계 변경마다 gFID가 얼마나 내려가는지, 어느 변경에서 SD-VAE 기준선 아래로 내려가는지 보인다.
[14.body.0.steps.0.title] 기본 DiT-XL
[14.body.0.steps.0.text] 23.08 · SD-VAE 7.13보다 +15.95 (Table 2)
[14.body.0.steps.1.text] 4.81 · −18.27, 기준선 아래로 (Table 4)
[14.body.0.steps.2.title] + 노이즈 증강
[14.body.0.steps.3.text] DiT^{DH}-XL 2.16 · −2.12, 전용 최적화 포함 (Table 6, App. D)
[14.body.0.caption] 모든 막대: DINOv2-B RAE, ImageNet 256×256, 80 epoch, guidance 없음. Table 2·4·5·6을 다시 그림
[14.notes.0] 네 막대는 모두 DINOv2-B RAE를 256×256에서 80 epoch 학습하고 guidance 없이 평가한 결과입니다. 점선은 같은 해상도와 학습·평가 조건을 적용한 SD-VAE DiT-XL의 결과입니다.
[14.notes.1] 기본 DiT-XL은 23.08로 점선보다 한참 위입니다. [1] schedule shift를 더하면 4.81로 내려가 처음으로 점선 아래에 들어옵니다.
[14.notes.2] [2] 노이즈 증강 디코더를 쓰면 4.28이 됩니다. [3] DDT head를 붙인 DiT^{DH}-XL은 2.16입니다.
[14.notes.3] 다만 마지막 단계는 head만 바뀐 것이 아닙니다. DiT^{DH}는 learning rate schedule, EMA, gradient clipping을 따로 씁니다. 이 점은 토론에서 다시 다루겠습니다.

## Slide 15 — 학습 epoch에 따른 수렴
[15.title] 학습 epoch에 따른 수렴
[15.message] 세 가지 설계 변경을 적용한 RAE DiT-XL은 head 없이도 SiT-XL과 REPA-XL의 최종 FID에 훨씬 적은 epoch로 도달한다.
[15.body.0.left.0.alt] Fig. 4. 학습 epoch(20–1400, 로그 축)에 따른 FID-50K. SiT-XL(주황)은 1400 epoch에 8.26, REPA-XL(초록)은 800 epoch에 5.90, DiT-XL(RAE: DINOv2-B, 파랑)은 30 epoch 부근에서 8.26을, 50 epoch 부근에서 5.90을 지나 80 epoch 4.28, 720 epoch 2.39에 이른다. 화살표에 47× faster, 16× faster 표시.
[15.body.0.left.0.caption] **Fig. 4** ImageNet 256×256, guidance 없음. RAE는 DINOv2-B, head 없는 DiT-XL
[15.body.0.right.0.items.1] SiT-XL 1400 epoch의 8.26까지 **47×** 빠름
[15.body.0.right.0.items.2] REPA-XL 800 epoch의 5.90까지 **16×** 빠름
[15.body.0.right.1.text] 47×·16×는 그림의 화살표(곡선 근거). 기준점도 표와 다르다: SiT 8.26 (표: 8.61, balanced 8.54), REPA 5.90 (balanced 5.78)
[15.notes.0] 이 곡선의 RAE 모델은 아직 wide head를 붙이지 않은 DiT-XL입니다. 80 epoch에 4.28, 720 epoch에 2.39입니다.
[15.notes.1] SiT-XL이 1,400 epoch에 기록한 8.26에 RAE는 30 epoch 남짓이면 도달합니다. REPA-XL이 800 epoch에 기록한 5.90에도 50 epoch 부근에서 도달합니다. 그림의 화살표에 47배와 16배가 표시돼 있습니다.
[15.notes.2] 그림의 기준점 8.26과 5.90은 뒤에 나오는 표의 값과 다릅니다. REPA의 5.90은 random 평가 값이고, SiT의 8.26은 표의 8.61이나 8.54와도 다릅니다. 평가 방식의 차이는 토론에서 다시 다루겠습니다.

## Slide 16 — DiT^{DH}의 학습 연산량
[16.title] DiT^{DH}의 학습 연산량
[16.message] 같은 RAE를 쓰면 DiT^{DH}는 기본 DiT-XL보다 적은 학습 연산량으로 더 낮은 gFID에 도달한다. VAE 기반 방법들보다도 빨리 수렴한다.
[16.body.0.reveals] 같은 RAE에서 DiT^{DH} 크기별로 학습 연산량과 gFID를 보고(6a), 누적 학습 연산량에 따른 수렴을 VAE 기반 방법과 비교한다(6b).
[16.body.0.states.0.label] 크기별 (6a)
[16.body.0.states.0.alt] Fig. 6a. 학습 GFLOPs(로그 축)에 따른 FID. DiT^DH-S 약 6.07, B 3.38, L 약 2.4, XL 2.16으로 내려가는 파란 선. 빨간 점 DiT-XL은 4.28이고 같은 값의 점선이 그어져 있다.
[16.body.0.states.0.title] DiT^{DH}-S/B/L/XL과 DiT-XL 한 점
[16.body.0.states.0.text] DiT^{DH}-B는 DiT-XL 학습 FLOPs의 약 40%로 3.38 (DiT-XL 4.28). S 6.07 → XL 2.16
[16.body.0.states.1.label] 누적 (6b)
[16.body.0.states.1.alt] Fig. 6b. 누적 학습 GFLOPs(로그 축)에 따른 FID. RAE의 DiT^DH-XL 곡선이 가장 아래에 있고, RAE의 DiT-XL, VA-VAE, REPA-XL, MDTv2-XL, SiT-XL, DiT-XL은 위에 있다.
[16.body.0.states.1.title] 누적 학습 GFLOPs와 VAE 기반 방법
[16.body.0.states.1.text] DiT^{DH}-XL 곡선이 가장 아래. baseline은 곡선이 아니라 보고된 최종점만 표시
[16.body.0.mediaCaption] **Fig. 6** DINOv2-B RAE, 256×256, guidance 없음. 두 패널의 축 범위는 다르다
[16.notes.0] [1] 첫 그래프는 DINOv2-B를 고정하고 backbone 크기가 다른 DiT^{DH} 네 가지를 기본 DiT-XL 한 점과 비교합니다. DiT^{DH}-B는 DiT-XL 학습 연산량의 약 40%로 3.38을 기록해 DiT-XL의 4.28보다 낮습니다.
[16.notes.1] [2] 두 번째 그래프는 누적 학습 연산량에 따른 곡선입니다. 다른 방법들은 곡선이 아니라 보고된 최종점만 찍혀 있다는 점에 주의해야 합니다.
[16.notes.2] 같은 RAE를 쓸 때는 넓은 head가 연산량 대비 성능을 높입니다. 인코더 크기에 따른 비교는 19번에서 하겠습니다.

## Slide 17 — ImageNet 256·512 벤치마크
[17.title] ImageNet 256·512 벤치마크
[17.message] class-balanced 평가에서 DiT^{DH}-XL은 256×256에서 guidance 없이 gFID 1.51을 기록한다. AutoGuidance를 쓰면 두 해상도 모두 1.13이다.
[17.body.0.alt] Fig. 1. 2020–2025년 ImageNet 256×256 FID(로그 축) 연표. 회색 점은 VAE 기반 이전 연구(VQ-VAE2 약 30에서 REPA-E 약 2까지), 오른쪽 파란 점은 RAE 기반 DiT와 DiT^{DH}(DINOv2-S, DINOv2-B)이며 가장 낮은 위치에 있다. 빈 원은 AutoGuidance 적용.
[17.body.0.caption] **Fig. 1** ImageNet 256×256 FID 연표. 회색: VAE 기반, 파랑: RAE 기반(빈 원은 AutoGuidance)
[17.body.1.columns.0.label] 모델 (256×256)
[17.body.2.text] **Table 8** w/o·w/: guidance 없음·있음, class-balanced. **Table 7** 512×512 guided: DiT^{DH}-XL 1.13 (400 epoch), EDM2 1.25. DiT^{DH}의 guided는 AutoGuidance(App. I)
[17.notes.0] 위의 연표는 ImageNet 256×256 FID를 연도별로 찍은 것이고, 오른쪽 파란 점이 이 논문의 결과입니다.
[17.notes.1] 256×256에서 REPA-E와 두 RAE 모델은 모두 800 epoch이고, 파라미터는 DiT^{DH}-XL이 839M으로 가장 많습니다.
[17.notes.2] DiT^{DH}-XL은 guidance 없이 1.51로 REPA-E보다 0.19 낮고, guidance를 쓰면 1.13으로 0.02 낮습니다. 512×512에서는 400 epoch에 1.13으로 EDM2의 1.25보다 낮습니다.
[17.notes.3] guided 평가에는 작은 DiT^{DH}-S를 guide로 쓰는 AutoGuidance를 적용했습니다. 256의 1.13은 scale과 guide checkpoint를 골라 얻은 값입니다. guided IS는 262.6으로 REPA-E의 304.0보다 낮습니다.

## Slide 18 — 512×512 샘플과 디코더 업샘플링
[18.title] 512×512 샘플과 디코더 업샘플링
[18.message] 256 토큰 확산 모델에서 디코더만 업샘플링 디코더로 교체해도 512×512 이미지를 생성할 수 있다. 다만 1,024 토큰으로 직접 학습한 모델보다 gFID가 0.48 높다.
[18.body.0.left.0.alt] Fig. 7. 512×512 생성 샘플 네 열: 흰 앵무새(cockatoo), 바다거북, 등대, 햄버거. 열마다 큰 이미지 4장과 작은 이미지 8장이 있고, 같은 클래스 안에서 자세·배경·시점·조명이 다르다.
[18.body.0.left.0.caption] **Fig. 7** 512×512 직접 학습 DiT^{DH}-XL, AutoGuidance
[18.body.0.right.0.columns.0.label] 경로
[18.body.0.right.0.columns.1.label] 토큰
[18.body.0.right.2.items.0] Upsample: 디코더 patch $p_d=2p_e$, 256×256용 확산 모델 재사용
[18.body.0.right.2.items.1] 토큰 ¼, gFID +0.48, rFID +0.44
[18.notes.0] 왼쪽은 512×512로 직접 학습한 모델의 샘플입니다. 같은 클래스 안에서도 거북은 물속에 있는 모습과 땅 위에 있는 모습이 나오고, 등대는 시점과 조명이 다릅니다.
[18.notes.1] 오른쪽은 디코더로 출력 해상도를 높이는 방법입니다. 디코더의 patch 크기를 두 배로 늘리면, 256×256에서 학습한 확산 모델을 그대로 써서 512×512 이미지를 출력할 수 있습니다.
[18.notes.2] 토큰은 4분의 1만 쓰는 대신 gFID가 0.48, rFID가 0.44 높습니다.

## Slide 19 — 인코더 선택과 토큰 차원
[19.title] 인코더 선택과 토큰 차원
[19.message] 복원이 가장 좋은 인코더가 생성에서는 가장 나쁘고, DiT-XL에서는 DINOv2 토큰 차원이 클수록 gFID가 나빠진다.
[19.body.0.left.0.columns.0.label] 인코더
[19.body.0.left.1.text] **Table 15a** 노이즈 증강 디코더, DiT-XL, 80 epoch. 증강 전 MAE-B gFID 16.14
[19.body.0.right.1.text] **Table 6** gFID, 80 epoch. DiT^{DH}의 개선 폭은 L에서 가장 크다(−3.36)
[19.body.1.text] MAE-B는 복원 성능이 가장 좋지만 생성 성능은 가장 나쁘다. DiT-XL에서는 토큰 차원이 클수록 gFID가 나빠진다.
[19.notes.0] 7번에서 복원이 가장 좋았던 MAE-B는 생성에서 가장 나쁩니다. 노이즈 증강 전에는 16.14였고, 증강 뒤에도 8.38입니다. 논문도 낮은 rFID가 좋은 tokenizer를 보장하지 않는다고 적습니다.
[19.notes.1] 오른쪽 표는 DINOv2 크기별 결과입니다. 폭이 1,152인 DiT-XL은 세 인코더를 쓸 때 모두 폭 조건을 만족합니다. 그래도 토큰 차원이 커질수록 gFID가 3.50, 4.28, 6.09로 나빠집니다.
[19.notes.2] DiT^{DH}를 쓰면 개선 폭은 L에서 가장 크지만, gFID 자체는 B가 가장 낮습니다. 이런 설계 변경을 적용한 뒤에야 고차원이 불리하지 않다고 말할 수 있습니다. 차원이 커질수록 성능이 좋아진다는 뜻은 아닙니다.
[19.notes.3] 후속 연구 LV-RAE도 의미 표현에 색과 질감 정보가 부족하다는 점을 복원의 병목으로 지적했습니다.

## Slide 20 — SD-VAE·픽셀·RAE에서 DDT head 비교
[20.title] SD-VAE·픽셀·RAE에서 DDT head 비교
[20.message] DDT head를 쓰면 SD-VAE에서는 gFID가 높아지고 픽셀에서는 낮아진다. 픽셀의 gFID는 토큰 수와 차원이 같은 RAE의 gFID와 여전히 큰 차이가 난다.
[20.body.0.columns.0.label] 입력
[20.body.0.columns.2.label] 토큰 × 차원
[20.body.0.groups.0.rows.1.cells.0] 픽셀
[20.body.1.text] **Table 10 · 11** gFID, ImageNet 256×256, 80 epoch, guidance 없음. 16 = 2×2×4, 768 = 16×16×3 (계산)
[20.body.2.text] DiT와 DiT^{DH}는 최적화 설정도 다르다(App. D). Δ에는 head와 최적화 설정의 차이가 함께 들어 있다
[20.notes.0] SD-VAE latent는 토큰 하나가 16차원입니다. 여기에 DDT head를 붙이면 gFID가 7.13에서 11.70으로 오히려 나빠집니다. 저자들은 head의 이점이 고차원에서만 나온다고 해석합니다.
[20.notes.1] 픽셀을 patch 16으로 나누면 RAE와 똑같이 768차원 토큰이 256개 나옵니다. 픽셀에서도 head를 쓰면 gFID가 낮아지지만, 30.56으로 RAE의 2.16보다 훨씬 높습니다.
[20.notes.2] 논문은 높은 차원만으로는 부족하며 표현 인코더가 만든 구조가 필요하다고 결론짓습니다. 다만 이 표의 두 열은 최적화 설정도 다릅니다.

## Slide 21 — 정리와 토론
[21.title] 정리와 토론
[21.message] ImageNet에서 RAE에 맞춘 설계 변경 네 가지를 적용하면 두 통념은 반박된다. 다만 FID 평가 방식, guidance 설정을 고른 방법, head와 최적화 설정의 효과 구분, latent 저장 비용은 더 따져 볼 수 있다.
[21.body.0.groups.0.heading] 정리
[21.body.0.groups.0.items.0] ① 고정한 DINOv2·SigLIP2·MAE에 ViT 디코더를 붙이면 SD-VAE보다 rFID가 낮다
[21.body.0.groups.0.items.1] ② DiT 폭을 토큰 차원 이상으로 하고 schedule shift, 노이즈 증강 디코더, DDT head를 더하면 256×256에서 guidance 없이 gFID 1.51
[21.body.0.groups.0.items.2] 단서: 복원이 좋다고 생성도 좋지는 않고(MAE), 토큰 차원이 클수록 좋은 것도 아니다(DINOv2-L)
[21.body.0.groups.1.heading] 토론
[21.body.0.groups.1.items.0] **FID 평가 방식**: 클래스를 무작위로 뽑아 평가하면 guidance를 쓴 결과의 순위가 뒤집힌다(1.28 대 REPA-E 1.26). 0.02 차이를 어떻게 볼까?
[21.body.0.groups.1.items.1] **Guidance 설정**: 1.13은 FID를 보며 scale 1.42와 14 epoch guide 모델을 골라 얻은 값이다. 이 값을 그대로 보고해도 되나?
[21.body.0.groups.1.items.2] **Head와 최적화**: DiT^{DH}만 learning rate·EMA·gradient clipping 설정이 다르다. head만의 효과는 얼마일까?
[21.body.0.groups.1.items.3.text] **Latent 저장 비용**: 이미지당 latent 원소가 SD-VAE의 48배(196,608 대 4,096)다. latent를 미리 저장해 두는 학습에서 저장·읽기 비용은?
[21.notes.0] 정리하면, 첫 번째 통념은 고정한 세 인코더로 ImageNet 이미지를 복원한 결과로 반박됩니다. 두 번째 통념은 네 가지 설계 변경을 적용한 뒤에야 반박됩니다. 복원과 생성은 다르고 차원이 클수록 좋은 것은 아니라는 점이 이 결론의 범위를 제한합니다.
[21.notes.1] 첫째는 FID 평가 방식입니다. 생성 이미지를 클래스마다 같은 수로 뽑는 class-balanced 평가와 클래스를 무작위로 뽑는 random 평가가 있습니다. Table 8 캡션에는 재평가 후 baseline 값이 높아졌다고 적혀 있습니다. 그런데 Table 14에서는 모든 방법에서 class-balanced 평가의 FID가 더 낮습니다. random 평가에서 guidance를 쓴 결과는 DiT^{DH}-XL이 1.28, REPA-E가 1.26으로 순위가 바뀝니다.
[21.notes.2] 둘째, 1.13은 guidance scale을 sweep해 1.42를 고르고, 기본 20 epoch 대신 14 epoch guide를 쓴 결과입니다. 같은 저자 그룹의 RAEv2는 원래 RAE가 CFG에 약해 별도의 guide 모델이 필요했다고 적고 있습니다.
[21.notes.3] 셋째, DiT^{DH}는 learning rate schedule, EMA, gradient clipping을 따로 썼습니다. 저자가 겹치는 text-to-image 후속 연구는 큰 규모에서 wide head와 노이즈 증강의 이득이 미미하고 schedule shift만 여전히 중요했다고 보고합니다. head만의 효과를 보려면 어떤 비교가 필요할까요?
[21.notes.4] 넷째는 제 해석입니다. 이미지당 latent 원소 수가 SD-VAE의 48배라 latent를 미리 저장해 두는 학습에서는 저장과 읽기 비용이 커집니다. 또 DINOv2(LVD-142M)의 사전학습 데이터에는 ImageNet-1k 학습 이미지가 들어 있습니다. 이런 비용과 조건을 어떻게 볼지 의견을 듣고 싶습니다.

## Slide 22 — 감사합니다
[22.title] 감사합니다
[22.links.0] 논문 · arXiv:2510.11690 · rae-dit.github.io
[22.links.1] 코드 · github.com/bytetriper/RAE (MIT)
[22.notes.0] 들어 주셔서 감사합니다. 논문과 코드 링크를 화면에 두었습니다. 질문과 의견을 받겠습니다.

