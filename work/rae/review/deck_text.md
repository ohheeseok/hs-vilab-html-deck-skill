# Deck text — Diffusion Transformers with Representation Autoencoders

## Slide 1 — Diffusion Transformers with Representation Autoencoders
[1.subtitle] 고정한 표현 인코더의 latent 위에서 DiT를 학습하는 RAE
[1.figure.alt] Fig. 7 맨 윗줄. DiT^DH-XL이 생성한 512×512 샘플: 흰 앵무새, 바다거북, 등대, 햄버거.
[1.figure.caption] **Fig. 7** DiT^{DH}-XL(DINOv2-B)의 512×512 샘플, AutoGuidance
[1.notes.0] 오늘 다룰 논문은 NYU의 Diffusion Transformers with Representation Autoencoders입니다.
[1.notes.1] 표지의 이미지는 이 논문의 모델이 512×512로 생성한 샘플입니다. 사전학습한 표현 인코더를 고정하고, 그 출력을 압축하지 않은 채 확산 모델의 latent로 씁니다.

## Slide 2 — RAE와 DiT^{DH} 요약
[2.title] RAE와 DiT^{DH} 요약
[2.message] 논문은 고정한 표현 인코더에 ViT 디코더를 붙이고, 그 고차원 토큰을 확산 모델이 학습하도록 DiT의 폭, noise schedule, 디코더, head를 조정한다.
[2.body.0.items.0.title] RAE 복원
[2.body.0.items.0.text] 고정한 DINOv2-B·SigLIP2-B·MAE-B + ViT 디코더. 셋 모두 SD-VAE보다 낮은 rFID
[2.body.0.items.1.title] 고차원 확산 처방
[2.body.0.items.1.text] 토큰 차원 이상의 DiT 폭, 차원 의존 schedule shift, 노이즈 증강 디코더
[2.body.0.items.2.text] 얕고 넓은 DDT head. ImageNet 256×256, 무가이던스 gFID **1.51** (800 epoch)
[2.body.1.alt] Fig. 1. 2020–2025년 ImageNet 256×256 FID(로그 축) 연표. 회색 점은 VAE 기반 이전 연구(VQ-VAE2 약 30에서 REPA-E 약 2까지), 오른쪽 파란 점은 RAE 기반 DiT와 DiT^{DH}(DINOv2-S, DINOv2-B)이며 가장 낮은 위치에 있다. 빈 원은 AutoGuidance 적용.
[2.body.1.caption] **Fig. 1** ImageNet 256×256 FID 연표. 회색: VAE 기반, 파랑: RAE 기반(빈 원은 AutoGuidance)
[2.notes.0] 이 논문이 하는 일은 세 가지입니다. 첫째, 고정한 표현 인코더의 토큰에서 이미지를 복원하는 디코더를 학습합니다.
[2.notes.1] 둘째, 그 토큰이 768차원으로 높기 때문에 확산 학습을 세 군데 고칩니다. 셋째, 넓은 head를 붙인 DiT^{DH}로 연산량 대비 성능을 높입니다.
[2.notes.2] 대표 수치 1.51은 DINOv2-B 위의 DiT^{DH}-XL을 800 epoch 학습하고, 클래스마다 같은 수를 guidance 없이 생성해 잰 값입니다. 아래 연표에서 파란 점이 이 논문의 결과입니다.

## Slide 3 — 잠재 확산과 표현 학습의 갈래
[3.title] 잠재 확산과 표현 학습의 갈래
[3.message] 이 논문은 압축 latent에서 확산을 학습하는 연구와, 사전학습 표현을 복원이나 생성에 쓰는 연구가 만나는 자리에 있다.
[3.body.0.groups.0.heading] 압축 latent의 확산
[3.body.0.groups.0.items.1] SD-VAE: 256² 이미지 → 32²×4 latent
[3.body.0.groups.1.heading] 표현으로 tokenizer 개선
[3.body.0.groups.1.items.1] VAE를 표현에 정렬하거나 MAE식 목표 추가
[3.body.0.groups.2.heading] 표현으로 생성 개선
[3.body.0.groups.2.items.1] DiT 중간 층을 외부 인코더에 정렬
[3.body.1.text] 인코더 자체를 표현 인코더로 바꾸면 복원과 확산이 모두 되는가?
[3.notes.0] LDM, DiT, SiT는 autoencoder가 만든 압축 latent에서 확산을 학습합니다. SD-VAE는 256×256 이미지를 32×32×4로 줄입니다.
[3.notes.1] VA-VAE, MAETok 같은 연구는 VAE를 학습할 때 표현 정렬이나 MAE식 목표를 더해 tokenizer를 개선합니다. REPA, DDT, REG는 생성 모델의 중간 층을 외부 인코더에 맞춥니다.
[3.notes.2] 이 논문은 한 걸음 더 갑니다. 인코더 자체를 표현 인코더로 바꾸면 복원과 확산이 모두 됩니까?

## Slide 4 — 논문이 겨냥한 두 통념
[4.title] 논문이 겨냥한 두 통념
[4.message] 표현 토큰에 복원할 정보가 남아 있는지와, DiT가 그 고차원 토큰의 분포를 배울 수 있는지는 따로 검증해야 한다.
[4.body.0.items.0.heading] ① 의미 인코더는 복원을 못 한다
[4.body.0.items.0.items.0] “high-level semantic similarities”만 남는다는 통념 (Yu et al., 2024b)
[4.body.0.items.0.items.1] 검증: 인코더 고정, 디코더 학습, SD-VAE와 rFID 비교 (Table 1)
[4.body.0.items.1.heading] ② 확산은 고차원 latent에서 안 된다
[4.body.0.items.1.items.0] 그래서 저차원 VAE latent를 쓴다는 통념
[4.body.0.items.1.items.1] 검증: 기본 DiT의 실패, 폭의 손실 하한, 처방 전후 gFID (Table 2–6)
[4.notes.0] 논문은 서론에서 두 가지 통념이 틀렸을 수 있다고 말합니다.
[4.notes.1] 첫째는 의미를 배운 인코더는 고수준 정보만 남겨서 픽셀을 충실히 복원하지 못한다는 것입니다. 둘째는 확산 모델이 고차원 latent에서 잘 학습되지 않으니 저차원 VAE latent를 써야 한다는 것입니다.
[4.notes.2] 발표는 이 두 통념을 차례로 따라갑니다. 진행 표시줄의 ①과 ②가 지금 어느 쪽을 보고 있는지 알려 줍니다.

## Slide 5 — RAE: 고정 인코더와 ViT 디코더
[5.title] RAE: 고정 인코더와 ViT 디코더
[5.message] RAE는 사전학습한 ViT의 patch token을 고정한 채, 그 토큰을 픽셀로 되돌리는 ViT 디코더만 학습한다.
[5.body.0.left.0.items.0] 256×256 입력 → **256 토큰 × 768 채널**, 압축 없음
[5.body.0.left.0.items.1] DINOv2-B: 224×224로 보간, encoder patch 14 · decoder patch 16
[5.body.0.left.0.items.2] [CLS]·[REG] 토큰은 버리고 patch token만 정규화
[5.body.0.left.0.items.3] 디코더 손실: L1 + LPIPS + GAN, 판별자는 고정한 DINO-S/8
[5.body.0.right.0.columns.0.label] 디코더
[5.body.0.right.1.text] **Table 1b** 인코더 DINOv2-B, ImageNet-1K val. GFLOPs는 디코더
[5.body.1.alt] Fig. 2. 왼쪽은 SD-VAE를 쓰는 DiT: U-Net 블록 인코더(135 GFLOPs)가 4채널 latent로 압축하고 디코더(310 GFLOPs)가 복원한다. 오른쪽은 RAE를 쓰는 DiT: ViT 블록 인코더(22 GFLOPs)가 압축 없이 768채널 latent를 만들고 ViT 디코더(106 GFLOPs)가 복원한다.
[5.body.1.caption] **Fig. 2** SD-VAE와 RAE(DINOv2-B). 256×256 이미지 한 장의 GFLOPs
[5.notes.0] RAE의 인코더는 학습하지 않습니다. 256×256 이미지에서 768채널 토큰 256개가 나오고, 이것을 압축하지 않고 latent로 씁니다.
[5.notes.1] DINOv2는 patch 크기가 14라서 입력을 224로 줄이고, 디코더는 patch 16으로 원래 해상도를 되돌립니다.
[5.notes.2] 디코더는 L1, LPIPS, GAN 손실로 학습하고, 판별자로 고정한 DINO-S/8을 씁니다. 오른쪽 표에서 가장 작은 ViT-B 디코더도 SD-VAE보다 rFID가 낮고, 연산량은 14분의 1입니다.

## Slide 6 — 세 인코더의 복원과 linear probe
[6.title] 세 인코더의 복원과 linear probe
[6.message] 세 고정 인코더에 디코더를 붙인 RAE는 모두 SD-VAE보다 rFID가 낮고, 인코더의 표현 품질은 그대로 남는다.
[6.body.0.left.0.columns.0.label] 인코더
[6.body.0.left.1.text] **Table 1a·d** ImageNet-1K val rFID, linear probe Top-1. 디코더 ViT-XL
[6.body.0.right.0.alt] Fig. 8. 두 행(앵무새, 버스) × 다섯 열. 왼쪽부터 입력, RAE(DINOv2-B), RAE(SigLIP2-B), RAE(MAE-B), SD-VAE의 복원. 다섯 열 모두 입력과 거의 같아 보인다.
[6.body.0.right.0.caption] **Fig. 8** 왼쪽부터 입력 · DINOv2-B · SigLIP2-B · MAE-B · SD-VAE
[6.body.0.right.1.text] ①은 ImageNet 복원에서 반박된다. 남은 질문: 복원이 좋으면 생성도 좋은가? (18번)
[6.notes.0] 세 인코더 모두 SD-VAE보다 rFID가 낮고, 그중 MAE-B가 0.16으로 가장 낮습니다. DINOv2 크기를 S, B, L로 바꿔도 rFID는 0.5 안팎으로 비슷합니다.
[6.notes.1] RAE는 인코더를 고정하므로 linear probe 정확도는 원래 인코더의 것을 그대로 가집니다. SD-VAE의 latent는 8%에 그칩니다.
[6.notes.2] 오른쪽 복원 예시에서 다섯 열의 차이는 눈으로 거의 보이지 않습니다. 첫 번째 통념은 ImageNet 복원에서는 반박됩니다. 다만 복원이 좋은 인코더가 생성에도 좋은지는 18번에서 다시 보겠습니다.

## Slide 7 — 고차원 RAE latent에서의 기본 DiT
[7.title] 고차원 RAE latent에서의 기본 DiT
[7.message] 토큰 수를 똑같이 256개로 맞춰도, 기본 DiT 설정에서는 RAE의 gFID가 SD-VAE보다 훨씬 높다.
[7.body.0.left.0.columns.0.label] 모델
[7.body.0.left.1.text] **Table 2** gFID. ImageNet 256×256, 80 epoch, guidance 없음. RAE는 DINOv2-B(patch 1), SD-VAE는 patch 2 — 둘 다 256 토큰
[7.body.0.right.0.items.0.title] DiT 설계
[7.body.0.right.0.items.0.text] 저차원 VAE 토큰에 맞춘 폭이 768차원 토큰에도 맞는가
[7.body.0.right.0.items.1.text] 이미지·VAE 입력에서 나온 schedule이 고차원 토큰에도 맞는가
[7.body.0.right.0.items.2.title] 디코더
[7.body.0.right.0.items.2.text] 깨끗한 latent만 본 디코더가 생성된 latent를 복원하는가
[7.notes.0] RAE에는 patch 1을, SD-VAE에는 patch 2를 써서 DiT가 보는 토큰 수를 똑같이 256개로 맞췄습니다. 연산량도 거의 같습니다.
[7.notes.1] 그런데 기본 DiT 설정으로 학습하면 RAE는 DiT-S에서 215.76으로 사실상 실패하고, XL로 키워도 23.08로 SD-VAE의 7.13보다 나쁩니다.
[7.notes.2] 저자들은 원인을 세 가지로 가정합니다. DiT의 폭, noise schedule, 그리고 디코더입니다. 다음 여섯 장이 이 셋을 하나씩 다룹니다.

## Slide 8 — 한 이미지 과적합: 폭과 깊이
[8.title] 한 이미지 과적합: 폭과 깊이
[8.message] DiT 폭이 토큰 차원 768에 닿아야 한 이미지도 과적합되고, 폭 384에서 깊이만 늘리면 손실이 0.5 부근에 머문다.
[8.body.0.left.0.alt] Fig. 3 왼쪽. 깊이를 고정하고 DiT 폭 d를 384, 512, 640, 768, 896으로 바꾼 단일 이미지 과적합 손실. 관측 손실은 384에서 약 0.5, 512에서 0.35, 640에서 0.18로 내려가고 768과 896에서 0에 가깝다. 빨간 점선 이론선 max(1 − d/768, 0)과 겹친다. d < 768의 생성 앵무새는 뭉개지고 d ≥ 768에서는 입력과 같다.
[8.body.0.left.0.caption] **Fig. 3 왼쪽** 깊이 고정, 폭 $d$를 바꿈
[8.body.0.right.0.alt] Fig. 3 오른쪽. 폭 384를 고정하고 깊이를 4, 12, 16, 24로 바꾼 손실. 네 점 모두 이론선 0.5 부근에 머물고, 생성 앵무새에는 모두 아티팩트가 남는다.
[8.body.0.right.0.caption] **Fig. 3 오른쪽** 폭 384 고정, 깊이를 바꿈
[8.body.1.text] DINOv2-B 토큰 $n=768$, 두 패널 같은 손실 축(0–0.5). 이미지 3장 × 3회 평균, 1,200 step (App. F). 점선은 다음 장의 하한
[8.notes.0] 원인을 떼어 보기 위해 저자들은 이미지 한 장만 외우게 합니다. 이미지 세 장에서 세 번씩 돌린 평균입니다.
[8.notes.1] 왼쪽은 깊이를 고정하고 폭을 바꾼 결과입니다. 폭이 토큰 차원 768보다 작으면 이미지 한 장조차 외우지 못하고, 768부터 손실이 0으로 떨어지며 입력이 그대로 나옵니다.
[8.notes.2] 오른쪽은 폭을 384로 두고 층을 24개까지 늘린 결과입니다. 손실은 0.5 부근에서 움직이지 않습니다. 용량이 아니라 폭이 문제라는 뜻이고, 빨간 점선이 어디서 나오는지 다음 장에서 보겠습니다.

## Slide 9 — Theorem 1: DiT 폭과 토큰 차원
[9.title] Theorem 1: DiT 폭과 토큰 차원
[9.message] 출력 투영의 rank가 토큰 차원보다 작으면 velocity 예측 손실에 하한이 생기고, Table 3에서 수렴한 칸은 모두 폭 ≥ 토큰 차원이다.
[9.body.0.left.0.symbols.0.1] 토큰 차원 (DINOv2-B: 768)
[9.body.0.left.0.symbols.1.1] DiT 폭
[9.body.0.left.0.symbols.2.1] $\varepsilon-x$ 공분산의 고유값 (내림차순)
[9.body.0.left.1.text] 한 이미지면 $\lambda_i=1$, 차원당 하한 $(n-d)/n$: $d=384$에서 0.5
[9.body.0.right.0.columns.0.label] 인코더 ($n$)
[9.body.0.right.1.text] **Table 3** 한 이미지 과적합 손실. 폭 S 384 · B 768 · L 1024. ○ 수렴, × 실패 (논문 표기)
[9.notes.0] DiT는 입력을 폭 d로 투영하고 마지막에 다시 n차원으로 투영합니다. 출력 투영 B의 rank가 d 이하이므로, 모델이 내놓는 velocity는 d차원 부분공간을 벗어나지 못합니다.
[9.notes.1] 그런데 학습 목표인 ε − x에는 모든 방향으로 퍼진 Gaussian noise가 들어 있습니다. 그 부분공간 밖의 분산이 그대로 손실의 하한으로 남습니다.
[9.notes.2] 이미지 한 장이면 고유값이 모두 1이라 하한은 (n − d)/n이고, 폭 384, 토큰 768을 넣으면 앞 그림의 0.5가 나옵니다.
[9.notes.3] 오른쪽 표에서 수렴한 칸은 모두 폭이 토큰 차원 이상입니다. 이 정리는 표현 가능성에 대한 결과이고, 생성 품질은 실험으로 확인합니다. 이후 실험은 DINOv2-B에 폭 1,152인 DiT-XL을 씁니다.

## Slide 10 — 차원 의존 schedule shift
[10.title] 차원 의존 schedule shift
[10.message] 토큰 수와 채널 수를 곱한 실효 차원으로 timestep을 옮기면, 같은 RAE DiT-XL의 gFID가 23.08에서 4.81로 내려간다.
[10.body.0.left.0.symbols.0.1] 기준 차원 4,096 (Esser et al., 2024)
[10.body.0.left.0.symbols.1.1] 실효 차원 = 토큰 수 × 채널 = 256 × 768 = 196,608
[10.body.0.left.0.symbols.2.1] $\sqrt{48}\approx 6.93$ → $t_n=0.5$이면 $t_m\approx0.87$
[10.body.0.left.1.text] $t=1$이 순수 noise. $m$, $\alpha$, 0.87은 정의에서 계산
[10.body.0.right.1.text] **Table 4** DINOv2-B RAE, DiT-XL, 80 epoch, 노이즈 증강 전
[10.notes.0] 해상도가 높을수록 같은 noise 수준에서 정보가 덜 망가진다는 것은 이미 알려져 있고, 그래서 timestep을 해상도에 따라 옮겨 왔습니다.
[10.notes.1] 저자들은 이것을 해상도가 아니라 토큰 수 곱하기 채널 수, 즉 실효 차원으로 일반화합니다. DINOv2-B RAE는 실효 차원이 기준의 48배이고, α는 약 6.93입니다.
[10.notes.2] 그러면 기준 timestep 0.5가 약 0.87로 옮겨져 noise가 훨씬 많이 섞입니다. 이 한 가지 변경으로 gFID가 23.08에서 4.81로 내려갑니다.

## Slide 11 — 노이즈 증강 디코더
[11.title] 노이즈 증강 디코더
[11.message] 디코더를 학습할 때 latent에 노이즈를 섞으면 생성 gFID는 낮아지고, 깨끗한 latent의 복원 rFID는 조금 높아진다.
[11.body.0.left.0.symbols.0.1] 고정 인코더의 출력 latent
[11.body.0.left.0.symbols.1.1] 디코더 학습 노이즈 세기 (기본 0.8)
[11.body.0.left.1.text] 디코더가 생성된 latent의 주변까지 복원하도록
[11.body.0.right.1.text] **Table 5 · 15c** DINOv2-B RAE, shift 적용 DiT-XL, 80 epoch
[11.notes.0] VAE 디코더는 연속 분포에서 뽑은 latent로 학습하지만, RAE 디코더는 학습 이미지의 깨끗한 latent만 봅니다. 확산 모델이 만든 latent는 그 점들에서 조금씩 벗어나 있을 수 있습니다.
[11.notes.1] 그래서 디코더를 학습할 때 latent에 Gaussian noise를 더하고, noise 세기 σ도 매번 무작위로 뽑습니다.
[11.notes.2] 표에서 τ를 키우면 gFID는 내려가고 rFID는 올라갑니다. 기본값 0.8에서 gFID는 4.81에서 4.28로 0.53 낮아지고, rFID는 0.08 높아집니다.

## Slide 12 — DiT^{DH}: 얕고 넓은 DDT head
[12.title] DiT^{DH}: 얕고 넓은 DDT head
[12.message] DiT^{DH}는 backbone 전체를 넓히는 대신, noisy latent를 직접 받는 2층·폭 2,048의 head로 폭 조건을 채운다.
[12.body.0.left.0.alt] Fig. 5. x_t, t, y가 DiT로 들어가고, DiT 출력과 x_t, t가 오른쪽의 세로로 긴 DDT Head로 들어가 velocity v_t를 낸다.
[12.body.0.left.1.text] 파라미터: DiT^{DH}-XL 839M, DiT-XL 675M (Table 8)
[12.body.0.right.0.columns.0.label] head 깊이 × 폭
[12.body.0.right.1.text] **Table 16** DINOv2-B RAE, DiT-XL backbone(28층, 폭 1152), 80 epoch
[12.notes.0] Theorem 1을 따르려면 폭이 토큰 차원 이상이어야 하는데, backbone 전체를 넓히면 연산량이 폭의 제곱으로 늘어납니다.
[12.notes.1] DiT^{DH}는 기존 DiT 위에 얕고 넓은 head를 붙입니다. head는 backbone 출력 z_t와 함께 noisy latent x_t를 직접 받아 velocity를 냅니다.
[12.notes.2] 오른쪽 표에서 2층·폭 2,048 head가 비슷한 연산량의 6층·폭 1,152 head보다 낫고, 4층으로 늘려도 좋아지지 않습니다. 표의 GFLOPs는 head만의 값이고, 전체 파라미터는 839M으로 DiT-XL보다 164M 많습니다.

## Slide 13 — 처방을 하나씩 더한 gFID
[13.title] 처방을 하나씩 더한 gFID
[13.message] 같은 80 epoch 조건에서 schedule shift가 gFID를 가장 크게 내리고, 노이즈 증강과 DDT head가 그 아래로 더 내린다.
[13.body.0.reveals] 처방마다 gFID가 얼마나 내려가는지, 그리고 어느 단계에서 SD-VAE 기준선 아래로 내려가는지
[13.body.0.steps.0.title] 기본 DiT-XL
[13.body.0.steps.0.text] 23.08 · SD-VAE 7.13보다 +15.95 (Table 2)
[13.body.0.steps.1.text] 4.81 · −18.27, 기준선 아래로 (Table 4)
[13.body.0.steps.2.title] + 노이즈 증강
[13.body.0.steps.3.text] DiT^{DH}-XL 2.16 · −2.12, 전용 최적화 포함 (Table 6, App. D)
[13.body.0.caption] 모든 막대: DINOv2-B RAE, ImageNet 256×256, 80 epoch, guidance 없음 · Table 2, 4, 5, 6을 다시 그림
[13.notes.0] 네 막대는 모두 같은 조건입니다. DINOv2-B RAE, 256×256, 80 epoch, guidance 없음이고, 점선은 같은 조건의 SD-VAE DiT-XL입니다.
[13.notes.1] 기본 DiT-XL은 23.08로 점선보다 한참 위입니다. [1] schedule shift를 더하면 4.81로 내려가 처음으로 점선 아래에 들어옵니다.
[13.notes.2] [2] 노이즈 증강 디코더를 쓰면 4.28이 됩니다. [3] DDT head를 붙인 DiT^{DH}-XL은 2.16입니다.
[13.notes.3] 다만 마지막 단계는 head만 바뀐 것이 아닙니다. DiT^{DH}는 learning rate schedule, EMA, gradient clipping을 따로 씁니다. 이 점은 토론에서 다시 다루겠습니다.

## Slide 14 — 학습 epoch에 따른 수렴
[14.title] 학습 epoch에 따른 수렴
[14.message] 세 처방을 적용한 RAE DiT-XL은 head 없이도 SiT-XL과 REPA-XL의 최종 FID에 훨씬 적은 epoch로 도달한다.
[14.body.0.left.0.alt] Fig. 4. 학습 epoch(20–1400, 로그 축)에 따른 FID-50K. SiT-XL(주황)은 1400 epoch에 8.26, REPA-XL(초록)은 800 epoch에 5.90, DiT-XL(RAE: DINOv2-B, 파랑)은 30 epoch 부근에서 8.26을, 50 epoch 부근에서 5.90을 지나 80 epoch 4.28, 720 epoch 2.39에 이른다. 화살표에 47× faster, 16× faster 표시.
[14.body.0.left.0.caption] **Fig. 4** ImageNet 256×256, guidance 없음. RAE는 DINOv2-B, head 없는 DiT-XL
[14.body.0.right.0.items.1] SiT-XL 1400 epoch의 8.26까지 **47×** 빠름
[14.body.0.right.0.items.2] REPA-XL 800 epoch의 5.90까지 **16×** 빠름
[14.body.0.right.1.text] 47×·16×는 그림의 화살표(곡선 근거). 8.26·5.90은 Fig. 4의 표시값으로 Table 8의 balanced 값(8.61·5.78)과 다르다
[14.notes.0] 이 곡선의 RAE 모델은 아직 wide head를 붙이지 않은 DiT-XL입니다. 80 epoch에 4.28, 720 epoch에 2.39입니다.
[14.notes.1] SiT-XL이 1,400 epoch에 도달한 8.26을 RAE는 30 epoch 남짓에 지나고, REPA-XL의 800 epoch 값 5.90도 50 epoch 부근에 지납니다. 47배와 16배는 이 화살표에서 나온 값입니다.
[14.notes.2] 한 가지 주의할 점은, 그림의 기준점 8.26과 5.90이 뒤에 볼 Table 8의 값과 다르다는 것입니다. 평가 방식이 다르기 때문이고, 토론에서 다시 다룹니다.

## Slide 15 — DiT^{DH}의 학습 연산량
[15.title] DiT^{DH}의 학습 연산량
[15.message] 같은 RAE 위에서 DiT^{DH}는 기본 DiT-XL보다 적은 학습 연산량으로 더 낮은 gFID에 도달하고, VAE 기반 방법들보다도 빨리 수렴한다.
[15.body.0.left.0.left.0.alt] Fig. 6a. 학습 GFLOPs(로그 축)에 따른 FID. DiT^{DH}-S 약 6.07, B 3.38, L 약 2.4, XL 2.16으로 내려가는 파란 선. 빨간 점 DiT-XL은 4.28이고 같은 값의 점선이 그어져 있다.
[15.body.0.left.0.left.0.caption] **Fig. 6a** DiT^{DH}-S/B/L/XL과 DiT-XL 한 점
[15.body.0.left.0.right.0.alt] Fig. 6b. 누적 학습 GFLOPs(로그 축)에 따른 FID. RAE의 DiT^{DH}-XL 곡선이 가장 아래에 있고, RAE의 DiT-XL, VA-VAE, REPA-XL, MDTv2-XL, SiT-XL, DiT-XL은 위에 있다.
[15.body.0.left.0.right.0.caption] **Fig. 6b** 누적 학습 GFLOPs
[15.body.0.right.0.items.0] DiT^{DH}-B: DiT-XL 학습 FLOPs의 약 40%로 3.38 (DiT-XL 4.28)
[15.body.0.right.0.items.2] Fig. 6b의 baseline은 보고된 최종점만 표시
[15.body.0.right.1.text] DINOv2-B RAE, ImageNet 256×256, guidance 없음. 약 40%·3.38·6.07은 본문(Sec. 5, 5.1)
[15.notes.0] 왼쪽 그래프는 DINOv2-B를 고정하고 DiT^{DH}의 backbone 네 크기를 기본 DiT-XL 한 점과 비교합니다. DiT^{DH}-B는 DiT-XL 학습 연산량의 약 40%로 3.38을 얻어 DiT-XL의 4.28보다 낮습니다.
[15.notes.1] 오른쪽은 누적 학습 연산량에 따른 곡선입니다. 다만 다른 방법들은 곡선이 아니라 보고된 최종점만 찍혀 있습니다.
[15.notes.2] 같은 RAE 위라면 넓은 head가 연산량 대비 이득이라는 것이 이 장의 내용입니다. 인코더 크기에 따른 비교는 18번에서 봅니다.

## Slide 16 — ImageNet 256·512 벤치마크
[16.title] ImageNet 256·512 벤치마크
[16.message] DiT^{DH}-XL은 class-balanced 평가에서 256×256 무가이던스 gFID 1.51, AutoGuidance로 두 해상도 모두 1.13을 기록한다.
[16.body.0.columns.0.label] 모델
[16.body.0.columns.3.label] gFID 무가이던스
[16.body.0.groups.1.label] 512×512 (guided만)
[16.body.1.text] **Table 8 · 7** class-balanced(클래스당 50장). DiT^{DH}의 guided는 AutoGuidance(guide DiT^{DH}-S: 256은 14 epoch·scale 1.42, 512는 20 epoch·1.5), DINOv2-S DiT-XL은 CFG with interval (App. I)
[16.notes.0] 256×256에서 REPA-E와 두 RAE 모델은 모두 800 epoch이고, 파라미터는 DiT^{DH}-XL이 839M으로 가장 많습니다.
[16.notes.1] DiT^{DH}-XL은 guidance 없이 1.51로 REPA-E보다 0.19 낮고, guidance를 쓰면 1.13으로 0.02 낮습니다. 512×512에서는 400 epoch에 1.13으로 EDM2의 1.25보다 낮습니다.
[16.notes.2] guided 결과는 작은 DiT^{DH}-S를 guide로 쓰는 AutoGuidance입니다. 256의 1.13은 scale과 guide checkpoint를 골라 얻은 값입니다. 그리고 guided IS는 262.6으로 REPA-E의 304.0보다 낮습니다.

## Slide 17 — 512×512 샘플과 디코더 업샘플링
[17.title] 512×512 샘플과 디코더 업샘플링
[17.message] 256 토큰 확산 모델에 업샘플링 디코더만 바꿔 끼워도 512×512를 만들 수 있지만, 1,024 토큰으로 직접 학습한 모델보다 gFID가 0.48 높다.
[17.body.0.left.0.alt] Fig. 7. 512×512 생성 샘플 네 열: 흰 앵무새(cockatoo), 바다거북, 등대, 햄버거. 열마다 큰 이미지 4장과 작은 이미지 8장이 있고, 같은 클래스 안에서 자세·배경·시점·조명이 다르다.
[17.body.0.left.0.caption] **Fig. 7** 512×512 직접 학습 DiT^{DH}-XL, AutoGuidance
[17.body.0.right.0.columns.0.label] 경로
[17.body.0.right.0.columns.1.label] 토큰
[17.body.0.right.2.items.0] Upsample: decoder patch $p_d=2p_e$, 256×256용 확산 모델 재사용
[17.body.0.right.2.items.1] 토큰 ¼, gFID +0.48, rFID +0.44
[17.notes.0] 왼쪽은 512×512로 직접 학습한 모델의 샘플입니다. 같은 클래스 안에서도 거북은 물속과 땅 위로, 등대는 시점과 조명이 다르게 나옵니다.
[17.notes.1] 오른쪽은 디코더가 해상도를 맡는 방법입니다. 디코더의 patch를 두 배로 키우면, 256×256에서 학습한 확산 모델을 그대로 두고 512×512를 출력합니다.
[17.notes.2] 토큰은 4분의 1만 쓰는 대신 gFID가 0.48, rFID가 0.44 높습니다.

## Slide 18 — 인코더 선택과 토큰 차원
[18.title] 인코더 선택과 토큰 차원
[18.message] 복원이 가장 좋은 인코더가 생성에서는 가장 나쁘고, DINOv2를 키워 토큰 차원을 늘리면 gFID는 오히려 나빠진다.
[18.body.0.left.0.columns.0.label] 인코더
[18.body.0.left.1.text] **Table 15a** 노이즈 증강 디코더, DiT-XL, 80 epoch. 증강 전 MAE-B gFID 16.14
[18.body.0.right.1.text] **Table 6** gFID, 80 epoch. DiT^{DH}의 개선 폭은 L에서 가장 크다(−3.36)
[18.body.1.text] 복원이 가장 좋은 MAE-B가 생성은 가장 나쁘고, DiT-XL에서는 토큰 차원이 클수록 gFID가 나빠진다
[18.notes.0] 6번에서 복원이 가장 좋았던 MAE-B는 생성에서 가장 나쁩니다. 노이즈 증강 전에는 16.14였고, 증강 뒤에도 8.38입니다. 논문도 낮은 rFID가 좋은 tokenizer를 보장하지 않는다고 적습니다.
[18.notes.1] 오른쪽은 DINOv2 크기입니다. 폭 1,152인 DiT-XL은 세 인코더 모두 폭 조건을 만족하는데도, 토큰 차원이 커질수록 gFID가 3.50, 4.28, 6.09로 나빠집니다.
[18.notes.2] DiT^{DH}를 쓰면 개선 폭은 L에서 가장 크지만, 절대값은 B가 가장 좋습니다. 고차원이 손해가 아니라는 주장은 처방을 한 뒤에 성립하는 것이고, 차원이 클수록 좋다는 뜻은 아닙니다.
[18.notes.3] 후속 연구 LV-RAE도 의미 특징에 색과 질감 정보가 부족한 것을 복원의 병목으로 지적했습니다.

## Slide 19 — SD-VAE·픽셀·RAE 위의 DDT head
[19.title] SD-VAE·픽셀·RAE 위의 DDT head
[19.message] DDT head는 SD-VAE에서는 gFID를 높이고, 픽셀에서는 낮추지만 같은 크기의 RAE 토큰과 큰 차이가 남는다.
[19.body.0.columns.0.label] 입력
[19.body.0.columns.2.label] 토큰 × 차원
[19.body.0.groups.0.rows.1.cells.0] 픽셀
[19.body.1.text] **Table 10 · 11** gFID, ImageNet 256×256, 80 epoch, guidance 없음. 16 = 2×2×4, 768 = 16×16×3 (계산)
[19.body.2.text] DiT와 DiT^{DH}는 최적화 설정도 다르다(App. D). Δ에는 head와 최적화 설정의 차이가 함께 들어 있다
[19.notes.0] SD-VAE latent는 토큰 하나가 16차원입니다. 여기에 DDT head를 붙이면 gFID가 7.13에서 11.70으로 오히려 나빠집니다. 저자들은 head의 이점이 고차원에서만 나온다고 해석합니다.
[19.notes.1] 픽셀을 patch 16으로 자르면 토큰이 RAE와 똑같이 256개, 768차원입니다. head는 여기서도 도움이 되지만 30.56으로 RAE의 2.16과는 거리가 멉니다.
[19.notes.2] 그러니 차원이 높다는 것만으로는 부족하고, 표현 인코더가 만든 구조가 필요하다는 것이 논문의 결론입니다. 다만 이 표의 두 열은 최적화 설정도 다르다는 점을 기억해 두겠습니다.

## Slide 20 — 정리와 토론
[20.title] 정리와 토론
[20.message] 두 통념은 ImageNet에서 처방을 갖춘 RAE로 반박되지만, 평가 프로토콜, guidance 선택, head와 최적화의 분리, latent 비용은 더 따져 볼 수 있다.
[20.body.0.groups.0.heading] 정리
[20.body.0.groups.0.items.0] ① 고정한 DINOv2·SigLIP2·MAE + ViT 디코더 → SD-VAE보다 낮은 rFID
[20.body.0.groups.0.items.1] ② 폭 ≥ 토큰 차원, 차원 의존 shift, 노이즈 증강 디코더, DDT head → 256×256 무가이던스 1.51
[20.body.0.groups.0.items.2] 범위: 복원 ≠ 생성(MAE), 차원이 클수록 좋은 것은 아님(DINOv2-L)
[20.body.0.groups.1.heading] 토론
[20.body.0.groups.1.items.0] **FID 프로토콜**: random 평가로 보면 guided 순위가 바뀐다(1.28 vs REPA-E 1.26). 0.02 차이를 어떻게 읽나?
[20.body.0.groups.1.items.1] **Guidance 선택**: 1.13의 scale·guide checkpoint를 FID로 골랐다. 고르는 데이터와 보고하는 데이터가 같아도 되나?
[20.body.0.groups.1.items.2] **Head와 최적화**: DiT^{DH}만 다른 LR·EMA·clipping. 후속 T2I 연구는 큰 규모에서 head의 이득이 미미하다고 보고. head 단독 효과는?
[20.body.0.groups.1.items.3.text] **Latent 비용**: 이미지당 latent 원소가 SD-VAE의 48배(196,608 vs 4,096). 캐시·전송 비용은?
[20.notes.0] 정리하면, 첫 번째 통념은 세 고정 인코더의 ImageNet 복원으로 반박됩니다. 두 번째 통념은 네 가지 처방을 갖춘 뒤에야 반박되고, 복원과 생성이 다르다는 점, 차원이 클수록 좋은 것은 아니라는 점이 그 범위를 정합니다.
[20.notes.1] 토론 첫째는 FID 프로토콜입니다. Table 8 캡션은 재평가로 baseline 값이 높아졌다고 쓰지만, Table 14를 보면 class-balanced가 모든 방법에서 더 낮습니다. random으로 보면 guided 결과는 DiT^{DH}-XL 1.28, REPA-E 1.26으로 순위가 바뀝니다.
[20.notes.2] 둘째, 1.13은 guidance scale과 guide checkpoint를 FID를 보며 고른 결과입니다. 같은 저자 그룹의 RAEv2는 원래 RAE가 CFG에 약해 별도의 guide 모델이 필요했다고 적고 있습니다.
[20.notes.3] 셋째, DiT^{DH}는 learning rate schedule, EMA, gradient clipping을 따로 썼습니다. 저자가 겹치는 text-to-image 후속 연구는 큰 규모에서 wide head와 노이즈 증강의 이득이 미미하고 schedule shift만 여전히 중요했다고 보고합니다. head만의 효과를 보려면 어떤 비교가 필요할까요?
[20.notes.4] 넷째는 제 해석입니다. 이미지당 latent 원소 수가 SD-VAE의 48배라 latent를 미리 저장해 두는 학습에서는 저장과 읽기 비용이 커집니다. 또 DINOv2의 사전학습 데이터에는 ImageNet-1k 학습 이미지가 들어 있습니다. 이런 비용과 조건을 어떻게 볼지 의견을 듣고 싶습니다.

## Slide 21 — 감사합니다
[21.title] 감사합니다
[21.links.0] 논문 · arXiv:2510.11690 · rae-dit.github.io
[21.links.1] 코드 · github.com/bytetriper/RAE (MIT)
[21.notes.0] 들어 주셔서 감사합니다. 논문과 코드 링크를 화면에 두었습니다. 질문과 의견을 받겠습니다.

