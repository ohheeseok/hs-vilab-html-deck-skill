| location | original | edit | rule |
|---|---|---|---|
| 5.title | RAE 위의 복원과 생성, 그리고 바꾸는 곳 | RAE의 복원·생성 경로와 바꾸는 네 곳 | L3-3 |
| 7.body.1.text | ①은 ImageNet 복원에서 반박된다. 남은 질문: 복원이 좋으면 생성도 좋은가? (18번) | ①은 ImageNet 복원에서 반박된다. 남은 질문: 복원이 좋으면 생성도 좋은가? (19번) | 장 번호 |
| 7.notes.2 | 오른쪽 복원 예시에서 다섯 열의 차이는 눈으로 거의 보이지 않습니다. 첫 번째 통념은 ImageNet 복원에서는 반박됩니다. 다만 복원이 좋은 인코더가 생성에도 좋은지는 18번에서 다시 보겠습니다. | 오른쪽 복원 예시에서 다섯 열의 차이는 눈으로 거의 보이지 않습니다. 첫 번째 통념은 ImageNet 복원에서는 반박됩니다. 다만 복원이 좋은 인코더가 생성에도 좋은지는 19번에서 다시 보겠습니다. | 장 번호 |
| 14.body.0.reveals | 설계 변경별 gFID 감소 폭과 SD-VAE 기준선보다 낮아지는 단계 | 막대를 하나씩 더하면 설계 변경마다 gFID가 얼마나 내려가는지, 어느 변경에서 SD-VAE 기준선 아래로 내려가는지 보인다. | L3-3 |
| 16.body.0.reveals | 같은 RAE 위에서 DiT^{DH}의 크기별 연산량(6a)과, 누적 학습 연산량에 따른 수렴을 VAE 기반 방법과 비교(6b) | 같은 RAE에서 DiT^{DH} 크기별로 학습 연산량과 gFID를 보고(6a), 누적 학습 연산량에 따른 수렴을 VAE 기반 방법과 비교한다(6b). | L3-3 |
| 16.notes.2 | 같은 RAE를 쓸 때는 넓은 head가 연산량 대비 성능을 높입니다. 인코더 크기에 따른 비교는 18번에서 하겠습니다. | 같은 RAE를 쓸 때는 넓은 head가 연산량 대비 성능을 높입니다. 인코더 크기에 따른 비교는 19번에서 하겠습니다. | 장 번호 |
| 19.notes.0 | 6번에서 복원이 가장 좋았던 MAE-B는 생성에서 가장 나쁩니다. 노이즈 증강 전에는 16.14였고, 증강 뒤에도 8.38입니다. 논문도 낮은 rFID가 좋은 tokenizer를 보장하지 않는다고 적습니다. | 7번에서 복원이 가장 좋았던 MAE-B는 생성에서 가장 나쁩니다. 노이즈 증강 전에는 16.14였고, 증강 뒤에도 8.38입니다. 논문도 낮은 rFID가 좋은 tokenizer를 보장하지 않는다고 적습니다. | 장 번호 |
| 21.message | ImageNet에서 RAE에 필요한 설계 변경을 적용해 두 통념을 반박했다. 평가 프로토콜, guidance 선택, head와 최적화의 효과를 구분하는 방법, latent 비용은 더 검토할 수 있다. | ImageNet에서 RAE에 맞춘 설계 변경 네 가지를 적용하면 두 통념은 반박된다. 다만 FID 평가 방식, guidance 설정을 고른 방법, head와 최적화 설정의 효과 구분, latent 저장 비용은 더 따져 볼 수 있다. | L3-3 |
| 21.body.0.groups.0.items.0 | ① 고정한 DINOv2·SigLIP2·MAE + ViT 디코더 → SD-VAE보다 낮은 rFID | ① 고정한 DINOv2·SigLIP2·MAE에 ViT 디코더를 붙이면 SD-VAE보다 rFID가 낮다 | L3-3 |
| 21.body.0.groups.0.items.1 | ② 폭 ≥ 토큰 차원, 실효 차원에 따른 schedule shift, 노이즈 증강 디코더, DDT head → 256×256에서 guidance 없이 1.51 | ② DiT 폭을 토큰 차원 이상으로 하고 schedule shift, 노이즈 증강 디코더, DDT head를 더하면 256×256에서 guidance 없이 gFID 1.51 | L3-3 |
| 21.body.0.groups.0.items.2 | 범위: 복원 ≠ 생성(MAE), 차원이 클수록 좋은 것은 아님(DINOv2-L) | 단서: 복원이 좋다고 생성도 좋지는 않고(MAE), 토큰 차원이 클수록 좋은 것도 아니다(DINOv2-L) | L3-3 |
| 21.body.0.groups.1.items.0 | **FID 프로토콜**: random 평가에서는 guided 순위가 바뀐다(1.28 vs REPA-E 1.26). 0.02 차이를 어떻게 해석할까? | **FID 평가 방식**: 클래스를 무작위로 뽑아 평가하면 guidance를 쓴 결과의 순위가 뒤집힌다(1.28 대 REPA-E 1.26). 0.02 차이를 어떻게 볼까? | L1-11 |
| 21.body.0.groups.1.items.1 | **Guidance 선택**: 1.13의 scale 1.42와 14 epoch guide는 FID를 보고 골랐다. 같은 FID로 보고해도 되나? | **Guidance 설정**: 1.13은 FID를 보며 scale 1.42와 14 epoch guide 모델을 골라 얻은 값이다. 이 값을 그대로 보고해도 되나? | L3-3 |
| 21.body.0.groups.1.items.2 | **Head와 최적화**: DiT^{DH}만 LR·EMA·clipping이 다르다. head만의 효과는? | **Head와 최적화**: DiT^{DH}만 learning rate·EMA·gradient clipping 설정이 다르다. head만의 효과는 얼마일까? | L3-3 |
| 21.body.0.groups.1.items.3.text | **Latent 비용**: 이미지당 latent 원소가 SD-VAE의 48배(196,608 vs 4,096). 캐시·전송 비용은? | **Latent 저장 비용**: 이미지당 latent 원소가 SD-VAE의 48배(196,608 대 4,096)다. latent를 미리 저장해 두는 학습에서 저장·읽기 비용은? | L3-3 |
| 21.notes.1 | 첫째는 FID 프로토콜입니다. Table 8 캡션에는 재평가 후 baseline 값이 높아졌다고 적혀 있습니다. 그런데 Table 14에서는 모든 방법에서 class-balanced 평가의 FID가 더 낮습니다. random 평가의 guided 결과는 DiT^{DH}-XL이 1.28, REPA-E가 1.26으로 순위가 바뀝니다. | 첫째는 FID 평가 방식입니다. 생성 이미지를 클래스마다 같은 수로 뽑는 class-balanced 평가와 클래스를 무작위로 뽑는 random 평가가 있습니다. Table 8 캡션에는 재평가 후 baseline 값이 높아졌다고 적혀 있습니다. 그런데 Table 14에서는 모든 방법에서 class-balanced 평가의 FID가 더 낮습니다. random 평가에서 guidance를 쓴 결과는 DiT^{DH}-XL이 1.28, REPA-E가 1.26으로 순위가 바뀝니다. | L1-11 |
