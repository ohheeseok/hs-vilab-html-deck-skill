# Deck text — Let Vision-Language Models Generate Images through Their Representations

## Slide 1 — Let Vision-Language Models Generate Images through Their Representations
[1.subtitle] VLM의 시각 표현을 이해와 생성이 함께 쓰는 Integral
[1.figure.alt] Fig. 1 왼쪽. 이미지가 vision encoder를 지나 Abstraction Fusion으로 가고, Vision-Language Model이 이해를 맡으며, 생성은 Block-wise MoT가 맡는 구조도.
[1.figure.caption] **Fig. 1** Integral 개요: Abstraction Fusion과 Block-wise MoT
[1.notes.0] 오늘은 NAVER Cloud와 KAIST의 Integral을 소개합니다. 사전학습 VLM에 이미지 생성 기능을 붙이면서, 이미지를 이해할 때와 생성할 때 같은 시각 토큰을 쓰게 한 연구입니다. 이렇게 같은 토큰을 쓰는 것이 생성에 정말 도움이 되는지, 논문의 비교 실험을 중심으로 보겠습니다.

## Slide 2 — Integral의 구조와 비교 실험
[2.title] Integral의 구조와 비교 실험
[2.message] Integral은 고정된 VLM의 vision encoder에서 여러 층의 표현을 모아 시각 토큰 하나를 만든다. VLM이 이미지를 읽을 때도, 이미지를 생성할 때도 이 토큰을 쓴다.
[2.body.0.text] 고정된 VLM의 vision encoder에서 여러 층의 표현을 모아 시각 토큰 $z$ 하나를 만든다. VLM이 이미지를 읽을 때도, 이미지를 생성할 때도 이 토큰을 쓴다.
[2.body.1.items.0.text] encoder 27블록과 patch embedding, 28개 표현을 모아 만든 256차원 $z$를 이해와 재구성에 함께 사용
[2.body.1.items.1.text] 생성을 맡는 별도 transformer(0.89B)가 VLM 32층 중 4층마다 VLM의 K/V를 참조
[2.body.1.items.2.title] 생성 비교 실험
[2.body.1.items.2.text] tokenizer, 조건을 주는 모델, 의미 정렬 손실, 백본 크기를 하나씩 바꾸고 50K step 학습해 비교
[2.notes.0] Integral은 사전학습 VLM을 고정한 채 이미지 생성 기능을 추가합니다. 이해와 생성에는 같은 시각 토큰 z를 씁니다.
[2.notes.1] 구성 요소는 둘입니다. Abstraction Fusion은 vision encoder의 여러 층에서 나온 표현을 모아 z를 만들고, Block-wise MoT는 생성을 맡는 transformer가 VLM의 네 층마다 VLM의 정보를 참조하게 합니다. 저자들은 비교 실험을 근거로, 이해와 생성이 같은 토큰을 쓰면 생성 학습이 잘된다고 주장합니다.

## Slide 3 — 통합 멀티모달 모델의 갈래
[3.title] 통합 멀티모달 모델의 갈래
[3.message] 통합 멀티모달 모델은 이해와 생성에 쓰는 시각 표현의 종류와 공유 범위에 따라 나뉜다.
[3.body.0.columns.0.label] 갈래
[3.body.0.columns.1.label] 대표 모델
[3.body.0.columns.2.label] 이해와 생성의 시각 표현
[3.body.0.groups.0.rows.0.cells.0] 이산 토큰 autoregressive
[3.body.0.groups.0.rows.0.cells.2] 이산 시각 토큰 하나
[3.body.0.groups.0.rows.1.cells.2] 연속 표현, 생성은 diffusion·flow
[3.body.0.groups.0.rows.2.cells.0] 인코딩 분리
[3.body.0.groups.0.rows.2.cells.2] 이해와 생성에 다른 시각 encoder
[3.body.0.groups.0.rows.3.cells.0] 연속 표현 공유
[3.body.0.groups.0.rows.3.cells.2] 하나의 연속 시각 표현
[3.body.0.groups.0.rows.4.cells.2] 생성은 별도 VAE latent(FLUX.1-VAE)
[3.body.0.groups.0.rows.5.cells.0] 사전학습 VLM + diffusion 생성
[3.body.0.groups.0.rows.5.cells.2] 생성은 별도 latent
[3.body.1.text] 재구성 품질이 비슷할 때, 이해에 쓰는 시각 표현으로 이미지를 생성하면 생성 학습이 달라지는가?
[3.notes.0] 논문은 비교 대상을 여섯 갈래로 나눕니다. 이산 토큰으로 통합하는 Emu3, autoregressive와 diffusion을 섞는 Transfusion, 이해와 생성의 encoder를 나눈 Janus-Pro, 연속 표현을 공유하는 Harmon, MoT 구조의 BAGEL, 그리고 사전학습 VLM에 diffusion 생성을 붙이는 MetaQuery입니다.
[3.notes.1] Integral은 사전학습 VLM을 쓴다는 점에서 BAGEL이나 MetaQuery와 가깝습니다. 다만 별도 VAE latent를 쓰는 대신 VLM과 공유하는 표현에서 이미지를 생성합니다. 재구성 품질이 비슷할 때 같은 표현을 쓰는 것만으로 생성 학습이 달라질까요?

## Slide 4 — 이해용 표현과 생성용 latent
[4.title] 이해용 표현과 생성용 latent
[4.message] VLM에 입력하는 의미 표현에는 재구성에 필요한 세부 정보가 부족하다. encoder를 재구성에 맞춰 학습하면 의미 성능이 떨어진다.
[4.body.0.items.0.heading] 이해 쪽
[4.body.0.items.0.items.0] VLM은 vision encoder가 만든 시각 embedding $s$를 읽는다
[4.body.0.items.0.items.1] 고수준 의미 표현에는 이미지 재구성에 필요한 세부가 부족하다
[4.body.0.items.1.heading] 생성 쪽
[4.body.0.items.1.items.0] 기존 방법은 재구성용 VAE latent(예: FLUX.1-VAE)로 이미지를 생성한다
[4.body.0.items.1.items.1] encoder를 재구성에 맞춰 학습하면 의미 성능이 떨어질 수 있다
[4.body.1.text] VLM에 그대로 입력하고 픽셀 이미지 재구성에도 쓸 토큰을 만들 수 있는가?
[4.notes.0] 이해 쪽에서 VLM이 읽는 것은 의미가 담긴 고수준 표현입니다. 논문은 이런 표현만으로는 이미지를 재구성할 세부가 부족하다고 짚습니다.
[4.notes.1] 반대로 encoder를 재구성에 맞춰 학습하면 의미 성능이 떨어질 수 있습니다. 그래서 기존 방법은 생성용 latent를 따로 둡니다. Integral에서는 하나의 토큰을 이해와 재구성에 모두 쓸 수 있게 했습니다.

## Slide 5 — Integral의 VLM 기반 생성 구조
[5.title] Integral의 VLM 기반 생성 구조
[5.message] Integral은 VLM이 읽는 이미지 토큰 z를 생성 모델의 latent로도 쓴다. 생성 stream이 VLM의 key와 value를 참조하는 곳은 네 층마다 한 곳으로 줄인다.
[5.body.0.reveals] Integral은 별도 VAE latent 대신 VLM과 공유하는 z를 쓴다. 생성 expert도 VLM의 층마다 두던 설계에서 네 층마다 두는 설계로 바꾼다.
[5.body.0.beats.0.title] 기존 설계
[5.body.0.beats.0.text] 이해에는 encoder 출력을 쓰고, 생성에는 별도 VAE latent와 층마다 배치한 expert를 쓴다
[5.body.0.beats.1.title] 공유 토큰 $z$
[5.body.0.beats.1.text] AF가 encoder 여러 층을 모아 $z$를 만든다. VLM은 $z$에서 만든 입력을 읽고, 생성 모델은 $z$와 같은 공간의 토큰을 만든다
[5.body.0.beats.2.text] 생성 stream(생성을 맡는 transformer)은 VLM 32층 중 4층마다, 8곳에서만 VLM의 K/V를 참조한다
[5.body.0.beats.3.title] 두 질문
[5.body.0.beats.3.text] ① AF 토큰으로 생성이 잘되는 이유는 무엇인가 ② 어떤 실험 조건에서 확인했나
[5.body.0.caption] **Fig. 1 · 4 · 5** 다시 그림(Sec. 2.2–2.3, App. A.1 반영). 기존 설계는 Fig. 5a의 Full MoT와 Sec. 3.2의 BAGEL 서술(MoT, FLUX.1-VAE)을 합침
[5.notes.0] 먼저 논문이 대비하는 기존 설계입니다. 이해할 때는 vision encoder의 출력을 VLM에 넣습니다. 생성은 별도 VAE latent에서 하고, VLM의 층마다 생성 layer를 짝짓습니다. Fig. 5a의 Full MoT이고, BAGEL이 MoT와 FLUX.1-VAE를 씁니다.
[5.notes.1] [1] Integral은 고정된 encoder의 여러 층에서 나온 표현을 Abstraction Fusion으로 모아 토큰 z를 만듭니다. VLM은 z를 projector에 통과시킨 입력을 읽고, 생성 모델은 z와 같은 공간의 토큰을 만듭니다. 이미지는 pixel decoder가 이 토큰에서 재구성합니다.
[5.notes.2] [2] 생성 stream은 생성을 맡는 별도 transformer입니다. VLM 32층 전부가 아니라 네 층마다, 여덟 곳에서만 VLM의 key와 value를 참조합니다.
[5.notes.3] [3] 뒤에서 답할 질문은 두 가지입니다. 첫째, AF 토큰으로 생성하면 왜 잘되는가, 재구성 품질 말고 다른 이유가 있는가. 둘째, 그 결과를 어떤 실험 조건에서 확인했는가입니다.

## Slide 6 — Propagation bottleneck 가설
[6.title] Propagation bottleneck 가설
[6.message] 저자들은 encoder를 재구성에 맞춰 학습하면 깊은 층의 표현이 초기층의 표현과 비슷해진다는 관측을 가설의 근거로 든다. 이를 바탕으로 encoder를 고정한 채 여러 층의 표현을 모으는 AF를 제안한다.
[6.body.0.alt] Fig. 3. (a) Joint 학습에서는 마지막 층까지 저수준 정보를 전달해야 하고, AF는 고정 encoder의 여러 층에서 나온 표현을 직접 합친다. (b) 층별 CKA는 Joint의 깊은 층에서 약 0.85–0.90으로 높고, 의미 감독을 강화한 Joint는 끝층에서 약 0.15, AF(고정)는 약 0.05까지 내려간다. (c) 20K step 동안 cosine과 PSNR을 비교하면, AF의 cosine은 Frozen과 비슷하고 PSNR은 가장 높다.
[6.body.0.caption] **Fig. 3** (a) Joint 학습과 AF (b) 각 층과 초기층의 CKA (c) tokenizer 20K step 동안의 의미 cosine과 PSNR
[6.body.1.items.0] 저자 가설에 따르면 최종층만으로 재구성하도록 학습할 때 깊은 층에서 초기층 정보를 유지해야 하므로 의미 추상화가 제약될 수 있다
[6.body.1.items.1] Joint 학습은 깊은 층의 CKA를 높인다. 의미 감독을 강화하면 CKA는 내려가지만 PSNR이 낮다(Fig. 3b–c)
[6.body.1.items.2] AF는 20K step에서 cosine 약 0.97(Frozen 수준)과 PSNR 약 26.7 dB를 함께 얻는다(곡선)
[6.body.1.items.3.text] CKA는 상관을 보여 준다. 직접 개입해 가설을 검증한 실험은 없다
[6.notes.0] 저자들은 이 trade-off를 propagation bottleneck이라는 가설로 설명합니다. 최종층만으로 재구성하도록 학습하면 깊은 층에서 초기층의 세부 정보를 유지해야 하므로 의미 추상화가 제약된다고 봅니다.
[6.notes.1] 근거는 가운데 그림입니다. encoder를 함께 학습한 Joint는 깊은 층에서도 초기층과의 CKA가 높고, 의미 감독을 강화하면 CKA는 내려가지만 오른쪽 그림처럼 PSNR이 낮아집니다. AF는 encoder를 고정한 채 여러 층을 모아 cosine과 PSNR을 함께 얻습니다.
[6.notes.2] 다만 CKA는 상관을 보여 줄 뿐입니다. 직접 개입해 가설을 검증한 실험은 없습니다.

## Slide 7 — Abstraction Fusion의 토큰 구성
[7.title] Abstraction Fusion의 토큰 구성
[7.message] AF는 같은 위치에서 encoder의 여러 층이 낸 표현을 모아 256차원 토큰 하나로 압축한다.
[7.body.0.left.0.alt] Fig. 4. 고정 vision encoder의 여러 층에서 나온 표현을 Abstraction Fusion(per-layer norm과 projection, self-attention, linear pooler)에서 합친다. VAE를 거쳐 만든 z는 semantic projector와 pixel decoder에 각각 입력한다.
[7.body.0.left.0.caption] **Fig. 4** Abstraction Fusion과 두 출력
[7.body.0.right.0.steps.0.title] 28개 표현
[7.body.0.right.0.steps.0.text] Qwen3.5-9B vision encoder의 27개 block과 patch embedding, patch 16, $d_h$ = 1152
[7.body.0.right.0.steps.1.title] 층별 정규화와 projection
[7.body.0.right.0.steps.1.text] ImageNet 50K장으로 구한 고정 통계로 정규화한 뒤 4층씩 묶어 위치마다 표현 7개를 만든다
[7.body.0.right.0.steps.2.title] 층 방향 self-attention과 pooler
[7.body.0.right.0.steps.2.text] 16 head, 위치마다 융합 표현 $f$, $d_f$ = 1152 (Eq. 1)
[7.body.0.right.0.steps.3.text] $z$, $d_z$ = 256. 학습 때는 샘플, 추론 때는 posterior mean
[7.notes.0] Qwen3.5-9B의 vision encoder는 27개 block으로 구성됩니다. patch embedding까지 28개 표현을 모두 씁니다.
[7.notes.1] 층마다 고정 통계로 정규화하고, 네 층씩 묶어 위치마다 일곱 개 표현을 만듭니다. 층 방향 self-attention과 linear pooler로 이 표현들을 융합 표현 f로 합친 뒤, variational bottleneck으로 256차원 z로 압축합니다. encoder 자체는 바꾸지 않습니다.

## Slide 8 — AF의 두 출력과 학습 목표
[8.title] AF의 두 출력과 학습 목표
[8.message] 같은 z에서 VLM의 원래 시각 embedding을 예측하는 손실과 이미지를 재구성하는 손실을 함께 쓴다.
[8.body.0.left.0.items.0.text] 2×2 토큰을 합친 뒤 MLP로 VLM 시각 입력($d_s$ = 4096)을 예측. 표적은 원래 VLM의 $s$
[8.body.0.left.0.items.1.text] RAE의 ViT-XL(28층, 폭 1152). 마지막 단계에서 decoder만 adversarial loss로 미세조정
[8.body.0.right.0.symbols.1.1] 토큰별 RMS 정규화. 둘째 항은 $2(1-\cos)$
[8.notes.0] z는 두 모듈에 입력됩니다. semantic projector는 이웃한 네 토큰을 합쳐 원래 VLM이 받던 4096차원 시각 입력을 예측합니다. pixel decoder는 같은 z에서 이미지를 재구성합니다.
[8.notes.1] 의미 손실에는 원래 embedding을 표적으로 삼는 MSE와 토큰별로 정규화한 MSE를 함께 씁니다. 정규화한 두 벡터의 MSE를 전개하면 cosine distance의 두 배가 됩니다. 논문 본문에서 이 항을 cosine-distance 항이라고 부릅니다. 학습 내내 vision encoder와 VLM은 고정입니다.

## Slide 9 — Block-wise MoT의 조건 전달
[9.title] Block-wise MoT의 조건 전달
[9.message] 생성 stream의 query는 VLM의 block 경계에서 생성 stream과 VLM 양쪽의 key·value를 참조한다. 생성 전용 파라미터는 0.89B다.
[9.body.0.left.0.alt] Fig. 5(a)(b). Full MoT는 VLM 층마다 MoT 층을 짝짓고, Block-wise MoT는 VLM 층 여러 개를 묶어 경계에서만 MoT 층을 두고 AdaLN으로 timestep을 넣는다.
[9.body.0.left.0.caption] **Fig. 5(a)(b)** 왼쪽 Full MoT, 오른쪽 Block-wise MoT
[9.body.0.right.0.groups.0.heading] 조건 전달
[9.body.0.right.0.groups.0.items.0] VLM 32층에 4층 간격으로 생성 block 8개
[9.body.0.right.0.groups.0.items.1] query는 생성 stream에서, key·value는 두 stream에서(VLM 쪽은 재사용, Eq. 4)
[9.body.0.right.0.groups.0.items.2] $z_t$는 2층 MLP를 거쳐 생성 stream에만 입력한다. VLM의 계산은 그대로다
[9.body.0.right.0.groups.1.heading] 규격
[9.body.0.right.0.groups.1.items.0] QKV 차원은 VLM과 같고 나머지 폭 $d_g$ = 2048
[9.body.0.right.0.groups.1.items.1] timestep은 block마다 adaLN-single(Fig. 5d)
[9.body.0.right.0.groups.1.items.2] DDT head(2개 block, 폭 3072)가 velocity를 예측한다. 생성 전용 파라미터 0.89B(891M)
[9.notes.0] 생성 stream은 생성을 맡는 별도 transformer로, VLM 32층 중 네 층마다 붙은 여덟 개 block입니다. 각 block의 query는 생성 stream에서 나오고, key와 value는 생성 stream과 해당 VLM 층 양쪽에서 가져옵니다. VLM의 계산은 바뀌지 않습니다.
[9.notes.1] timestep은 block마다 adaLN-single로 넣는데, Fig. 5d에서 입력에 더하는 방식보다 GenEval 곡선이 높았습니다. 마지막 DDT head가 velocity를 예측하고, 생성 전용 파라미터는 모두 0.89B입니다. 부록 C.2에는 Full MoT가 31개 block이라고 나옵니다. VLM의 32층과 하나 차이가 나는데, 논문은 이유를 밝히지 않습니다.

## Slide 10 — 학습 단계와 규모
[10.title] 학습 단계와 규모
[10.message] tokenizer를 먼저 학습해 z의 공간을 고정한 뒤 생성 모델을 600K step 학습한다. 뒤의 비교 실험은 생성 1단계를 50K step만 학습한 결과다.
[10.body.0.columns.0.label] 단계
[10.body.0.columns.1.label] 학습
[10.body.0.columns.3.label] 해상도
[10.body.0.groups.0.rows.0.cells.1] AF 전체
[10.body.0.groups.0.rows.1.cells.1] 동적 해상도
[10.body.0.groups.0.rows.2.cells.1] adversarial 학습으로 pixel decoder만 미세조정
[10.body.0.groups.1.label] 생성
[10.body.1.text] **Table 7** 학습 단계별 step, 해상도, H100 수. 학습률·배치 등은 생략
[10.body.2.text] Sec. 3.4–3.6의 생성 비교 실험은 1단계를 50K step만 학습한 결과: 생성 전체 step 수의 1/12
[10.notes.0] tokenizer는 세 단계로 학습하고, 마지막에는 z의 공간을 고정한 채 pixel decoder만 미세조정합니다. 생성은 text-to-image부터 interleaved SFT까지 600K step입니다. VLM은 처음부터 끝까지 고정입니다.
[10.notes.1] 뒤에서 볼 생성 비교 실험은 생성 1단계, 즉 256 해상도 text-to-image를 50K step까지만 학습한 결과입니다. step 수로는 생성 전체의 12분의 1이고, 뒤 단계는 해상도와 배치도 다릅니다. tokenizer 구조 비교는 이와 별도로 20K step입니다.

## Slide 11 — AF의 재구성 품질과 이해 성능 유지
[11.title] AF의 재구성 품질과 이해 성능 유지
[11.message] 최종 AF tokenizer는 재구성 전용 VAE와 비슷하거나 더 좋은 재구성 품질을 보이며 Qwen3.5-9B의 이해 성능을 평균 99.8% 유지한다.
[11.body.0.left.0.groups.0.label] 통합 tokenizer
[11.body.0.left.0.groups.1.label] 재구성 전용
[11.body.0.left.1.text] **Table 1** ImageNet-1k 256×256 재구성. 최종 tokenizer(전체 학습과 decoder 미세조정 후). 행 일부만 옮김
[11.body.0.right.0.body.0.items.0.label] 이해 성능 유지율(20개 벤치마크 평균)
[11.body.0.right.0.body.1.text] **Table 2** Qwen3.5-9B와 AF를 붙인 Qwen3.5-9B
[11.notes.0] 왼쪽은 최종 tokenizer의 재구성 결과입니다. AF는 PSNR 32.2 dB로, 재구성 전용인 FLUX.1-VAE의 31.1 dB보다 조금 높습니다.
[11.notes.1] 오른쪽은 이해 성능입니다. VLM이 원래 시각 입력 대신 AF를 거친 입력을 받아도 20개 벤치마크에서 이해 성능을 평균 99.8% 유지합니다. MMMU 점수는 조금 오르고 OCRBench 점수는 조금 내려갑니다.

## Slide 12 — 이해·생성 시스템 비교
[12.title] 이해·생성 시스템 비교
[12.message] 최종 Integral은 기반 VLM의 이해 점수를 유지하면서 GenEval 0.88, ImgEdit 3.50을 얻는다. 백본과 데이터가 다른 시스템끼리의 비교다.
[12.body.0.columns.0.label] 모델
[12.body.1.text] **Table 3 · 4** 최종 시스템 비교: 백본과 학습 데이터가 모델마다 다르다(조건을 맞춘 비교 아님). ImgEdit-Bench Overall은 GPT-4.1 평가이고, 비공개 GPT-4o는 4.20. 굵게는 표에 보인 행 중 최고. 행·열 일부
[12.notes.0] 최종 시스템끼리의 비교입니다. Integral은 기반인 Qwen3.5-9B의 MMMU를 그대로 유지하고, GenEval 0.88과 GenEval++ 0.743을 얻습니다. GenEval++는 GPT-4o-Image와 비슷하고, DPG에서는 TUNA-2가 더 높습니다.
[12.notes.1] 편집에서는 ImgEdit Overall 3.50으로 BAGEL과 OmniGen2보다 높고 GPT-4o보다는 낮습니다. 다만 이 표는 백본과 학습 데이터가 모두 다른 시스템을 비교한 것입니다. BAGEL과의 이해 점수 차이는 두 시스템의 기반 VLM에서 이미 나타납니다.

## Slide 13 — 세계 지식이 필요한 생성과 편집
[13.title] 세계 지식이 필요한 생성과 편집
[13.message] 지식이 필요한 생성과 편집에서도 Integral은 BAGEL보다 높고, 생성에서는 56B FLUX.2-dev에 가깝다.
[13.body.0.reveals] 같은 지식 평가에서 생성은 프롬프트에 이름이 나오지 않는 대상을 그리는 과제이고, 편집은 입력 이미지를 지식에 맞게 바꾸는 과제다. 두 과제 모두에서 BAGEL과 점수 차이가 난다.
[13.body.0.states.0.label] 지식 생성
[13.body.0.states.0.alt] Fig. 2 둘째 줄. 도쿄가 있는 나라의 산(후지산), 영국의 선사시대 거석 원(스톤헨지), 교토의 수천 개 주황 문 아래 참배길(후시미 이나리), 물에 녹는 과망간산칼륨(보라색 용액)을 생성한 이미지.
[13.body.0.states.0.text] Overall: Integral 0.556, BAGEL 0.352, FLUX.2-dev(56B) 0.565. CoT를 쓰면 Integral 0.788, BAGEL 0.628.
[13.body.0.states.1.label] 지식 편집
[13.body.0.states.1.alt] Fig. 2 편집. 고양이 가면을 베네치아 카니발의 화려한 가면으로, 덜 익은 스테이크를 웰던으로 바꾼 전후 이미지.
[13.body.0.states.1.text] Overall: Integral 60.79, BAGEL 56.40. 세 지식 범주 모두 Integral이 높다(사실·개념·절차, GPT-4o 평가).
[13.body.0.mediaCaption] **Fig. 2** 굵은 글씨가 지식이 필요한 부분, 괄호는 그 뜻. 저자가 고른 예시. 두 표 모두 최종 시스템 비교
[13.notes.0] [1] 지식 생성 예시입니다. 프롬프트는 후지산이라는 이름을 말하지 않고 도쿄가 있는 나라의 산이라고만 합니다. WISE-Verified에서 Integral은 0.556으로 BAGEL보다 높고, 56B인 FLUX.2-dev의 0.565에 가깝습니다. CoT를 붙이면 0.788까지 오릅니다.
[13.notes.1] [2] 편집에서는 지시를 이해하는 데 필요한 지식을 바탕으로 입력 이미지를 바꿔야 합니다. KRIS-Bench에서 Integral은 60.79로 BAGEL보다 높고, 세 범주 모두에서 앞섭니다. 이 역시 최종 시스템끼리의 비교이고, 예시는 저자가 고른 것입니다.

## Slide 14 — AF와 FLUX.1-VAE: 50K step 비교
[14.title] AF와 FLUX.1-VAE: 50K step 비교
[14.message] VLM, 생성 모델 구조, 학습 설정을 같게 두고 latent만 바꾸면, 재구성 PSNR은 1.1 dB 차이인데 50K step GenEval은 0.41 대 0.18이다.
[14.body.0.left.0.alt] Fig. 1 오른쪽. 10K–50K step GenEval: AF는 0.12에서 0.41로, FLUX.1 VAE는 0.07에서 0.18로 오른다.
[14.body.0.left.0.caption] **Fig. 1** 오른쪽. 256×256 text-to-image, 50K step까지의 GenEval
[14.body.0.right.0.items.1.label] PSNR, 최종 tokenizer
[14.body.0.right.1.items.0] 같게 둔 것: 조건을 주는 Qwen3.5-9B, 생성 모델 구조, 학습(256×256, 50K step)
[14.body.0.right.1.items.1.text] 저자 해석에 따르면 재구성 품질이 비슷한데도 생성 성능에 큰 차이가 난 것은 VLM과 표현을 공유했기 때문이다
[14.body.0.right.1.items.2] 두 latent의 차원·토큰 수·분포를 맞췄다는 보고는 없다
[14.notes.0] 이제 이 발표의 중심인 비교 실험입니다. 한 가지만 바꾸고 나머지는 같게 둔 실험입니다. 여기서는 조건을 주는 VLM, 생성 모델 구조, 학습 설정을 같게 두고, 생성 모델이 만들 latent만 AF와 FLUX.1-VAE로 바꿨습니다.
[14.notes.1] 두 tokenizer의 재구성 PSNR은 1.1 dB 차이인데, 50K step의 GenEval은 0.41 대 0.18로 두 배 넘게 벌어집니다. 저자들은 재구성 품질로 설명되지 않는 이 차이를 VLM과 표현을 공유한 덕으로 봅니다.
[14.notes.2] 다만 두 latent는 차원과 토큰 수, 분포도 다를 수 있고, 이를 맞췄다는 보고는 없습니다. 다음 장에서는 네 비교를 하나씩 보면서 이 해석이 어느 범위까지 맞는지 살펴보겠습니다.

## Slide 15 — 하나씩 바꾼 비교 실험 네 가지
[15.title] 하나씩 바꾼 비교 실험 네 가지
[15.message] 네 실험은 GenEval 차이를 다른 이유로 설명할 수 있는지 하나씩 확인한다. VLM 대신 텍스트 전용 LLM이 조건을 줘도 AF가 FLUX.1-VAE보다 높다.
[15.body.0.reveals] 같은 50K step 학습에서 한 가지씩 바꾼 실험을 넘겨 보면, GenEval 차이를 설명하는 이유 가운데 어떤 것이 맞지 않고 어떤 것이 아직 가능한지 보인다.
[15.body.0.states.0.label] 외부 encoder
[15.body.0.states.0.alt] Fig. 6(a). 10K–50K step GenEval: AF(ours) 0.12에서 0.41, SigLIP2-AF 0.15에서 0.31, FLUX.1-VAE 0.07에서 0.18. 10K에서는 SigLIP2-AF가 조금 위, 20K에서 겹치고 30K부터 AF가 위.
[15.body.0.states.0.title] SigLIP2-AF: 같은 AF, 다른 encoder
[15.body.0.states.0.text] 50K GenEval은 Qwen AF 0.41, SigLIP2-AF 0.31. encoder를 바꾸면서 정렬 대상과 재구성 PSNR(ImageNet 256², 34.08 대 32.20 dB)도 함께 바뀌었다. 의미를 담은 encoder면 어느 것이든 효과가 같은지 본 실험이다.
[15.body.0.states.1.label] 조건 모델
[15.body.0.states.1.alt] Fig. 6(b). 50K step GenEval: VLM + AF 0.41, LLM + AF 약 0.28, VLM + FLUX.1-VAE 0.18, LLM + FLUX.1-VAE 약 0.17.
[15.body.0.states.1.title] VLM이 조건을 줄 때와 텍스트 전용 LLM이 줄 때
[15.body.0.states.1.text] LLM 대신 VLM이 조건을 주면 AF +0.13, FLUX.1-VAE +0.01. LLM 조건에서도 AF(곡선, 약 0.28)가 VLM 조건의 FLUX.1-VAE(0.18)보다 높다. 비교한 LLM의 이름과 크기는 밝히지 않았다.
[15.body.0.states.2.label] 의미 정렬 제거
[15.body.0.states.2.alt] Fig. 10(a). 10K–50K step GenEval: AF(ours) 0.12에서 0.41, AF w/o sem. 약 0.07에서 약 0.25(곡선).
[15.body.0.states.2.title] AF w/o sem.: 재구성은 더 좋다
[15.body.0.states.2.text] 의미 정렬 손실만 뺐다. 재구성은 좋아졌지만(PSNR 32.2 → 33.7 dB, rFID 0.15 → 0.13) GenEval·DPG·WISE(Fig. 10b–c)는 모두 AF보다 낮다.
[15.body.0.states.3.label] 2B 백본
[15.body.0.states.3.alt] Fig. 7. 50K step 기준 GenEval: AF(9B) 0.41, AF(2B) 0.26, FLUX.1-VAE(9B) 0.18.
[15.body.0.states.3.title] Qwen3.5-2B에 AF
[15.body.0.states.3.text] 50K GenEval: 2B AF 0.26, 9B FLUX.1-VAE 0.18, 9B AF 0.41. 2B AF는 PSNR 32.33 dB(ImageNet 256²), 이해 유지율 99.2%(2B 기준 20개 평균). 2B × FLUX.1-VAE는 없다.
[15.body.0.mediaCaption] **Fig. 6a · 6b · 10a · 7** 256² T2I, 50K step GenEval, y축 0부터
[15.notes.0] [1] 첫째, 같은 AF 구조를 Qwen의 encoder 대신 외부 encoder인 SigLIP2에 붙였습니다. 재구성은 34.08 dB로 더 좋지만 50K GenEval은 0.31로 낮습니다. 다만 encoder를 바꾸면서 정렬 대상과 PSNR도 함께 바뀌었고, 10K에서는 SigLIP2-AF가 잠깐 앞섭니다.
[15.notes.1] [2] 둘째, 생성 모델에 조건을 주는 모델을 VLM과 텍스트 전용 LLM으로 바꿔 봤습니다. LLM 대신 VLM이 조건을 주면 AF는 0.13 오르고 FLUX.1-VAE는 0.01 오릅니다. 저자들은 이것을 VLM과 같은 토큰을 쓰는 AF가 VLM의 정보를 더 잘 활용한다는 근거로 봅니다. 그런데 그림을 보면 LLM이 조건을 준 AF도 곡선에서 약 0.28로, VLM이 조건을 준 FLUX.1-VAE의 0.18보다 높습니다.
[15.notes.2] [3] 셋째, AF에서 의미 정렬 손실만 뺐습니다. 재구성 PSNR은 33.7 dB로 오히려 높아지는데, GenEval과 DPG, WISE 곡선은 모두 낮아집니다. 이 결과도 재구성 품질이 생성 성능을 결정한다는 설명과 맞지 않습니다.
[15.notes.3] [4] 넷째, 2B 백본에 AF를 붙이면 9B FLUX.1-VAE보다 점수가 높습니다. 다만 2B에 FLUX.1-VAE를 적용한 비교 항목은 없습니다.

## Slide 16 — 50K step 비교로 확인한 것과 남은 질문
[16.title] 50K step 비교로 확인한 것과 남은 질문
[16.message] 재구성 품질만으로는 GenEval 차이를 설명할 수 없다. 하지만 그 차이가 VLM과 같은 토큰을 써서 생긴 것인지, AF latent가 원래 학습하기 쉬워서인지는 실험으로 가르지 못했다.
[16.body.0.columns.0.label] 다른 설명
[16.body.0.columns.1.label] 확인한 실험
[16.body.0.columns.2.label] 결과(256², 50K step)
[16.body.0.columns.3.label] 결론
[16.body.0.groups.0.rows.0.cells.0] 재구성을 잘하는 latent라서?
[16.body.0.groups.0.rows.0.cells.2] 재구성이 비슷하거나 더 좋아도 GenEval은 낮다
[16.body.0.groups.0.rows.0.cells.3] 아니다
[16.body.0.groups.0.rows.1.cells.0] 의미를 담은 encoder면 다 되나?
[16.body.0.groups.0.rows.1.cells.2] 0.31 대 0.41. 정렬 대상·PSNR도 바뀜
[16.body.0.groups.0.rows.1.cells.3] 일부만 확인
[16.body.0.groups.0.rows.2.cells.0] AF latent가 원래 학습하기 쉬워서?
[16.body.0.groups.0.rows.2.cells.1] LLM이 조건을 줌
[16.body.0.groups.0.rows.2.cells.2] LLM 조건: AF 약 0.28 > FLUX.1-VAE 약 0.17
[16.body.0.groups.0.rows.2.cells.3] **가능성 남음**
[16.body.0.groups.0.rows.3.cells.0] 9B 큰 백본이라서?
[16.body.0.groups.0.rows.3.cells.1] 2B 백본(AF만)
[16.body.0.groups.0.rows.3.cells.3] 일부만 확인
[16.body.0.groups.0.rows.4.cells.0] 학습 초반에 빨리 오를 뿐?
[16.body.0.groups.0.rows.4.cells.1] 없음
[16.body.0.groups.0.rows.4.cells.2] 50K step까지만. 600K 전체 학습 비교 없음
[16.body.0.groups.0.rows.4.cells.3] **확인 안 됨**
[16.body.1.text] 결론 열은 발표자의 판단. ‘약’이 붙은 값은 Fig. 6b 곡선에서 읽음, 나머지는 본문 값. 마지막 두 질문은 토론 1·2번
[16.notes.0] 앞의 실험들을 질문 형태로 정리했습니다. GenEval 차이를 다르게 설명할 수 있는지 하나씩 봅니다. 먼저 재구성을 잘하는 latent라서 생성도 잘한다는 설명은 맞지 않습니다. FLUX.1-VAE와 비교할 때도, 의미 정렬 손실을 뺀 AF와 비교할 때도 재구성 점수가 비슷하거나 더 높은 쪽의 GenEval이 낮았습니다.
[16.notes.1] 의미를 담은 encoder면 아무것이나 되는지, 9B 큰 모델이라서인지는 일부만 확인됐습니다. SigLIP2 실험에서는 encoder와 함께 정렬 대상과 PSNR도 바뀌었고, 2B 백본에는 FLUX.1-VAE를 붙인 비교가 없습니다.
[16.notes.2] 아직 답이 없는 질문은 둘입니다. 첫째, LLM이 조건을 줘도 AF가 FLUX.1-VAE보다 높습니다. 그러면 이득의 일부는 VLM과 같은 토큰을 써서가 아니라 AF latent 자체가 학습하기 쉬워서 생겼을 수 있습니다. VLM이 조건을 줄 때 AF가 더 오른 부분만 같은 토큰을 쓴 효과로 볼 수 있습니다. 둘째, 모든 비교가 50K step이라 AF가 빨리 배우는 것인지 끝까지 학습해도 더 좋은 것인지 알 수 없습니다. 이 두 질문은 토론에서 다시 묻겠습니다.

## Slide 17 — AF 융합 방식 비교
[17.title] AF 융합 방식 비교
[17.message] 20K step으로 학습한 tokenizer를 비교하면, AF는 단순 합산이나 attention pooling보다 재구성 품질이 높고 cosine은 고정 encoder 수준을 유지한다.
[17.body.0.left.0.alt] Fig. 8. tokenizer 학습 5K–20K step 동안 의미 cosine과 PSNR을 비교했다. AF의 PSNR은 24에서 26.7로 올라 가장 높다. attention pooling은 약 22, MLS는 약 20.4, Frozen은 약 19.4다. cosine은 Frozen과 AF가 약 0.97로 가장 높다.
[17.body.0.left.0.caption] **Fig. 8** 융합 방식별 cosine과 PSNR, tokenizer 20K step. AF는 MLS보다 PSNR +6.27 dB
[17.body.0.right.0.columns.0.label] 변형
[17.body.0.right.0.groups.0.rows.1.cells.0] norm·proj. 공유
[17.body.0.right.0.groups.0.rows.2.cells.0] self-attention 제거
[17.body.0.right.1.text] **Table 10** 20K step 시점. 최종 tokenizer(Table 1, 32.2 dB)와 학습량이 다르다
[17.notes.0] AF의 융합 구조를 단순한 대안과 비교했습니다. 층별 표현을 그냥 더하는 MLS보다 PSNR이 6.27 dB 높고, cosine은 고정 encoder 수준입니다.
[17.notes.1] 오른쪽 표는 AF의 구성 요소를 하나씩 바꾼 결과입니다. 어느 것을 바꿔도 세 지표가 모두 나빠지고, attention pooling으로 바꾸면 크게 떨어집니다. 여기서 본 26.67 dB는 20K step에서 측정한 값입니다. 앞서 본 32.2 dB를 측정했을 때와는 학습량이 다릅니다.

## Slide 18 — 생성 구조 비교: MMDiT와 Full MoT
[18.title] 생성 구조 비교: MMDiT와 Full MoT
[18.message] 같은 AF 공간, 50K step 학습에서 Block-wise MoT는 MMDiT보다 GenEval이 높고, Full MoT와는 비슷한 품질을 더 적은 계산으로 낸다.
[18.body.0.left.0.alt] Fig. 9. 10K–50K step GenEval: Block-wise MoT(891M) 0.12에서 0.41, MMDiT(962M) 0.06에서 0.28.
[18.body.0.left.0.caption] **Fig. 9** Block-wise MoT(891M)와 MMDiT(962M). 같은 AF, DDT head, 학습 설정
[18.body.0.right.0.columns.0.label] 구조(blocks)
[18.body.0.right.1.items.0.label] Full MoT의 denoising 계산량이 더 많음
[18.body.0.right.1.items.1.label] Full MoT의 batch당 지연이 더 김
[18.body.0.right.2.text] **Table 13** 같은 AF, 50K step 학습 후. 배치 크기와 denoising step 수는 보고되지 않음
[18.notes.0] 생성 구조도 비교했습니다. 같은 AF 공간과 DDT head를 썼을 때, Block-wise MoT는 MMDiT보다 파라미터가 조금 적고 GenEval 곡선은 계속 높습니다.
[18.notes.1] 층마다 block을 붙인 Full MoT와 비교하면 GenEval과 DPG는 Block-wise가, WISE-Verified는 Full MoT가 조금 높습니다. 대신 Full MoT의 계산량은 2.5배, batch당 지연은 3.1배, step당 지연은 3.23배입니다. 측정에 쓴 배치 크기와 step 수는 논문에 없습니다.

## Slide 19 — 한계와 비용
[19.title] 한계와 비용
[19.message] 비교 실험은 짧은 학습과 Qwen3.5 계열에서만 했고, 생성 전용 0.89B 외에도 비용이 든다.
[19.body.0.groups.0.heading] 검증 범위
[19.body.0.groups.0.items.0] tokenizer 비교 실험은 256², 50K step, 주로 GenEval
[19.body.0.groups.0.items.1] 조건 VLM은 Qwen3.5 계열(9B, 2B)만
[19.body.0.groups.0.items.2] 생성한 $z$를 다음 턴 입력으로 바로 쓰면 디코딩·재인코딩 손실이 없다는 장점(Sec. 2.2)은 실험하지 않음
[19.body.0.groups.1.heading] 평가
[19.body.0.groups.1.items.0] 20K ablation의 의미 지표는 학습 표적과 같은 cosine
[19.body.0.groups.1.items.1] WISE-Verified의 판정 모델은 Qwen3.5-35B-A3B로 백본과 같은 계열(외부 자료)
[19.body.0.groups.1.items.2] GenEval 2 저자들은 GenEval이 이미 포화됐다고 본다(외부 자료)
[19.body.0.groups.2.heading] 비용
[19.body.0.groups.2.items.0] Qwen3.5-9B 이해 추론, 800×800 이미지 1장 기준
[19.body.0.groups.2.items.1] VLM의 시각 입력 경로 456.0M → 582.1M, pixel decoder 475.1M 별도
[19.body.0.groups.2.items.2] prefill 42.6 → 54.9 ms (+28.9%). 100 토큰 생성까지 포함하면 +2.1%
[19.notes.0] 한계는 세 가지로 정리했습니다. 먼저 검증 범위입니다. 비교 실험은 256 해상도에서 50K step까지, 주로 GenEval로 했고, 실험한 VLM은 Qwen3.5 계열뿐입니다. 생성한 z를 다음 턴에 바로 다시 쓰면 손실이 없다는 장점도 실험으로 재지 않았습니다.
[19.notes.1] 평가와 관련해 외부 자료 두 가지를 참고했습니다. WISE-Verified의 채점 모델인 Qwen3.5-35B-A3B는 Integral의 백본과 같은 계열입니다. 또 GenEval 2의 저자들은 GenEval이 이미 포화됐다고 봅니다.
[19.notes.2] 생성 전용 0.89B 외에도 시각 입력 경로의 파라미터가 126M 늘고, pixel decoder의 파라미터가 475M입니다. Qwen3.5-9B가 800×800 이미지 한 장을 이해할 때 prefill 지연은 29% 늘지만, 100 토큰 생성까지 포함한 전체 지연은 2.1% 늘어납니다.

## Slide 20 — 정리와 토론
[20.title] 정리와 토론
[20.message] 재구성 품질만으로 GenEval 차이를 설명할 수 없다는 점은 여러 실험이 보여 준다. 그 차이가 VLM과 같은 토큰을 써서 생긴다는 것은 저자의 해석이다.
[20.body.0.groups.0.heading] 정리
[20.body.0.groups.0.items.0] 고정 encoder의 여러 층 표현을 모은 토큰 $z$ 하나로 VLM 이해 성능을 99.8% 지키면서 이미지 재구성(32.2 dB)도 한다
[20.body.0.groups.0.items.1] 50K step 비교에서 AF 토큰으로 생성한 쪽의 GenEval이 높았고, 그 차이는 재구성 점수로 설명되지 않는다
[20.body.0.groups.0.items.2] 그 차이가 VLM과 같은 토큰을 써서 생긴다는 것은 저자의 해석이다
[20.body.0.groups.1.heading] 토론
[20.body.0.groups.1.items.0] 텍스트 전용 LLM이 조건을 줘도 AF가 FLUX.1-VAE보다 높았다(Fig. 6b). VLM과 같은 토큰을 쓴 효과와 AF latent 자체의 효과를 어떻게 따로 잴까?
[20.body.0.groups.1.items.1] 비교는 모두 생성 학습 50K step(전체 600K)에서, 주로 GenEval로 했다. AF가 빨리 배우는 것인가, 끝까지 학습해도 더 좋은가?
[20.body.0.groups.1.items.2] 생성한 $z$를 다음 턴에 바로 쓰는 장점과 propagation bottleneck 가설은 실험으로 확인하지 않았다. 무엇을 재면 확인할 수 있을까?
[20.body.0.groups.1.items.3.text] 생성 전용 0.89B 외에 VLM 이미지 입력 모듈 교체, pixel decoder, VLM을 바꿀 때마다 tokenizer 재학습이 든다. 이 비용을 감안해도 쓸 만한 경우는?
[20.notes.0] 정리하겠습니다. Integral은 고정된 encoder의 여러 층에서 나온 표현을 토큰 z 하나로 모아, VLM의 이해 성능을 거의 그대로 지키면서 이미지도 재구성합니다. 50K step 비교 실험에서는 AF 토큰으로 생성한 쪽의 GenEval이 높았고, 그 차이는 재구성 점수로 설명되지 않았습니다. 다만 그 차이가 VLM과 같은 토큰을 써서 생긴다는 것은 저자들의 해석입니다.
[20.notes.1] 토론할 질문은 네 가지입니다. 첫째, VLM 대신 텍스트 전용 LLM이 조건을 줘도 AF가 FLUX.1-VAE보다 높았습니다. VLM과 같은 토큰을 쓴 효과와 AF latent 자체가 학습하기 쉬운 효과를 어떻게 따로 잴 수 있을까요? 둘째, 비교 실험은 생성 학습 50K step에서, 주로 GenEval로 했습니다. AF가 빨리 배우는 것인지, 끝까지 학습해도 더 좋은 것인지 어떻게 가릴 수 있을까요?
[20.notes.2] 셋째, 생성한 z를 다음 턴에 바로 쓰는 장점과 propagation bottleneck 가설은 실험으로 확인하지 않았습니다. 무엇을 측정하면 확인할 수 있을까요? 넷째는 제 해석에서 나온 질문입니다. 생성 전용 0.89B 외에도 VLM의 이미지 입력 모듈을 바꾸고, pixel decoder를 따로 두고, VLM을 바꿀 때마다 tokenizer를 다시 학습해야 합니다. 이 비용을 감안해도 쓸 만한 경우는 언제일까요?

## Slide 21 — 감사합니다
[21.title] 감사합니다
[21.links.1] 코드 · github.com/the-jb/integral · 체크포인트 · huggingface.co/the-jb/Integral-9B
[21.notes.0] 들어 주셔서 감사합니다. 특히 VLM과 같은 토큰을 쓴 효과와 AF latent 자체의 효과를 가르려면 어떤 실험이 필요할지 의견을 듣고 싶습니다.

