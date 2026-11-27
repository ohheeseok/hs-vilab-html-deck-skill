| location | original | edit | rule |
|---|---|---|---|
| 4.body.0.beats.3.text | ① 무엇을, 어느 층에 ② 수렴과 생성이 얼마나 | ① 무엇을, 어느 층에 맞추나 ② 수렴과 생성 품질이 얼마나 바뀌나 | L3-3 |
| 7.body.0.reveals | 정렬 loss를 적용하는 층. 학습에만 쓰는 경로(인코더·MLP·REPA loss)와 추론 경로의 차이 | 단계를 넘기면 정렬 loss가 어느 층에 붙는지, 학습에만 쓰는 경로(인코더·MLP·REPA loss)와 추론 경로가 어떻게 다른지 보인다. | L3-3 |
| 10.body.0.reveals | 패널마다 같은 축에 그린 vanilla와 REPA를 확대해 분류 정확도와 정렬이 달라지는 층을 비교 | 패널을 하나씩 확대해 vanilla와 REPA를 같은 축에서 보면, 분류 정확도와 정렬이 어느 층에서 달라지는지 보인다. | L3-3 |
| 13.body.0.reveals | 같은 noise·sampler 조건에서 REPA 출력의 물체 형태가 갖춰지는 학습 step을 클래스별로 비교 | 같은 noise·sampler 조건에서 클래스별로 보면, REPA 출력에서 물체 형태가 어느 step부터 갖춰지는지 비교할 수 있다. | L3-3 |
| 14.body.0.right.1.text | 같은 checkpoint의 sampling 설정 차이 (Table 9·10) | 같은 checkpoint에서 sampling 설정만 바꾼 결과 (Table 9·10) | L3-3 |
| 21.message | REPA는 학습 step을 기준으로 비교했을 때 FID를 크게 낮췄다. 정렬 대상, 정렬 층, 정렬을 유지할 기간, 평가와 비용의 근거는 더 따져 볼 수 있다. | 학습 step 기준으로 비교하면 REPA는 FID를 크게 낮췄다. 다만 무엇을 어느 층에 정렬할지, 정렬을 언제까지 유지할지, 보고한 수치의 근거와 비용은 더 따져 볼 수 있다. | L3-3 |
| 21.body.0.groups.0.items.0 | Vanilla SiT 표현은 DINOv2보다 약하다 | Vanilla SiT의 표현은 DINOv2보다 linear probe 정확도와 정렬이 낮다 | L3-3 |
| 21.body.0.groups.0.items.1 | clean 인코더 표현을 8층에 patch마다 정렬 | 깨끗한 이미지의 인코더 표현에 SiT 8층 출력을 patch마다 맞춘다 | L3-3 |
| 21.body.0.groups.0.items.2 | ImageNet 256×256, no CFG. 400K step에서 vanilla 7M step 수준의 FID | ImageNet 256×256, CFG 없이: 400K step으로 vanilla 7M step보다 낮은 FID | L3-3 |
| 21.body.0.groups.1.items.0 | **깊이**: 8층→16층에서 Acc.는 오르고 FID는 나빠진다. 무엇을 정렬해야 하나? | **정렬 층**: 8층 대신 16층에 정렬하면 분류 정확도는 오르고 FID는 나빠진다. 생성에는 무엇을 정렬해야 하나? | L3-3 |
| 21.body.0.groups.1.items.1 | **평가**: 1.42는 Table 10에서 FID가 가장 낮은 설정. 고르는 데이터와 보고하는 데이터가 같아도 되나? | **수치 선택**: 1.42는 Table 10의 설정 가운데 FID가 가장 낮은 것이다. 설정을 고른 데이터와 결과를 보고한 데이터가 같아도 되나? | L3-3 |
| 21.body.0.groups.1.items.2 | **기록**: Table 3의 SiT-L/2 400K 수치는 어느 target 설정인가? | **표 기록**: Table 3의 SiT-L/2 400K 수치(9.7)는 Table 2의 DINOv2-B 행과 같은데, Table 7은 DINOv2-L로 적는다. 어느 설정인가? | L1-11 |
| 21.body.0.groups.1.items.3.text | **비용**: 인코더 forward 비용과 후반 정체. 정렬은 언제까지 유지해야 하나? | **비용**: 학습 중 인코더 forward 비용이 들고, 학습 후반에 REPA가 정체한다는 보고가 있다. 정렬은 언제까지 유지해야 하나? | L3-3 |
