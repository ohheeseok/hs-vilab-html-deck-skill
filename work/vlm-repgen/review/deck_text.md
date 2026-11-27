# Deck text — Let Vision-Language Models Generate Images through Their Representations

## Slide 1 — Let Vision-Language Models Generate Images through Their Representations
[1.subtitle] VLM의 시각 표현을 이해와 생성이 함께 쓰는 Integral
[1.figure.alt] Fig. 1 왼쪽. 이미지가 vision encoder를 지나 Abstraction Fusion으로 가고, Vision-Language Model이 이해를 맡으며, 생성은 Block-wise MoT가 맡는 구조도.
[1.figure.caption] **Fig. 1** Integral 개요: Abstraction Fusion과 Block-wise MoT
[1.notes.0] 오늘은 NAVER Cloud와 KAIST의 Integral을 소개합니다. 사전학습 VLM에 이미지 생성을 붙이되, 이해와 생성이 같은 시각 표현을 쓰게 한 연구입니다. 그 효과를 통제 비교 중심으로 보겠습니다.

## Slide 2 — Integral 한눈에 보기
[2.title] Integral 한눈에 보기
[2.message] Integral은 고정된 VLM의 vision encoder 여러 층을 모은 시각 토큰 하나를 이해 입력과 생성 latent로 함께 쓴다.
[2.body.0.text] 고정된 VLM의 vision encoder 여러 층을 모은 시각 토큰 $z$ 하나를 이해 입력과 생성 latent로 함께 쓴다.
[2.body.1.items.0.text] encoder 28개 층의 표현을 모아 이해와 재구성을 함께 맡는 256차원 $z$
[2.body.1.items.1.text] VLM 32층 중 4층마다 K/V를 읽는 생성 stream, 생성 전용 0.89B
[2.body.1.items.2.title] 표현 공유 통제 비교
[2.body.1.items.2.text] tokenizer·조건 모델·의미 정렬·백본 크기를 바꾼 50K step 비교
[2.notes.0] Integral은 사전학습 VLM을 고정한 채 이미지 생성을 붙입니다. 핵심은 이해와 생성이 같은 시각 토큰 z를 쓴다는 점입니다.
[2.notes.1] 구성 요소는 둘입니다. vision encoder의 여러 층을 모아 z를 만드는 Abstraction Fusion, 그리고 VLM의 네 층마다 조건을 읽는 Block-wise MoT입니다. 저자들은 통제 비교로 이 공유가 생성 학습을 돕는다고 주장하고, 이 발표는 그 비교를 중심으로 따라가겠습니다.

## Slide 3 — 통합 멀티모달 모델의 갈래
[3.title] 통합 멀티모달 모델의 갈래
[3.message] 통합 멀티모달 모델은 이해와 생성이 어떤 시각 표현을 쓰고, 그것을 얼마나 공유하는지로 갈린다.
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
[3.body.0.groups.0.rows.4.cells.0] 사전학습 VLM + 생성 경로
[3.body.0.groups.0.rows.4.cells.2] 생성은 별도 latent(BAGEL: FLUX.1-VAE)
[3.body.1.text] 질문: 재구성 품질이 비슷할 때, 이해와 같은 시각 표현에서 생성하면 생성 학습이 달라지는가?
[3.notes.0] 논문은 비교 대상을 다섯 갈래로 나눕니다. 이산 토큰으로 통합하는 Emu3, autoregressive와 diffusion을 섞는 Transfusion, 이해와 생성의 encoder를 나눈 Janus-Pro, 연속 표현을 공유하는 Harmon, 그리고 사전학습 VLM에 생성 경로를 붙이는 MetaQuery와 BAGEL입니다.
[3.notes.1] Integral은 마지막 갈래에 속하지만, 생성을 별도 VAE latent가 아니라 VLM과 공유하는 표현에서 한다는 점이 다릅니다. 이 발표가 던질 질문은 재구성 품질이 비슷할 때 같은 표현을 쓰는 것만으로 생성 학습이 달라지는가입니다.

## Slide 4 — 이해용 표현과 생성용 latent
[4.title] 이해용 표현과 생성용 latent
[4.message] VLM이 읽는 의미 표현에는 재구성에 필요한 세부가 부족하고, encoder를 재구성에 맞추면 의미가 흐려진다.
[4.body.0.items.0.heading] 이해 쪽
[4.body.0.items.0.items.0] VLM은 vision encoder가 만든 시각 embedding $s$를 읽는다
[4.body.0.items.0.items.1] 고수준 의미 표현에는 이미지 재구성에 필요한 세부가 부족하다
[4.body.0.items.1.heading] 생성 쪽
[4.body.0.items.1.items.0] 기존 방법은 재구성 지향 VAE latent(FLUX.1-VAE 등)에서 생성한다
[4.body.0.items.1.items.1] encoder를 재구성에 맞춰 학습하면 의미 성능이 떨어질 수 있다
[4.body.1.text] VLM이 그대로 읽으면서 픽셀로도 되돌릴 수 있는 토큰을 만들 수 있는가?
[4.notes.0] 이해 쪽에서 VLM이 읽는 것은 의미가 담긴 고수준 표현입니다. 논문은 이런 표현만으로는 이미지를 재구성할 세부가 부족하다고 짚습니다.
[4.notes.1] 반대로 encoder를 재구성에 맞춰 학습하면 의미 성능이 떨어질 수 있습니다. 그래서 기존 방법은 생성용 latent를 따로 둡니다. Integral이 푸는 문제는 두 요구를 한 토큰에 담는 것입니다.

## Slide 5 — Integral이 VLM에 생성을 붙이는 방식
[5.title] Integral이 VLM에 생성을 붙이는 방식
[5.message] Integral은 생성 latent를 VLM의 이해 입력과 같은 토큰 z로 바꾸고, 생성 stream이 VLM을 읽는 곳을 네 층마다로 줄인다.
[5.body.0.reveals] 별도 VAE latent가 VLM과 공유하는 z로 바뀌고, 층마다 붙던 생성 expert가 네 층 간격으로 줄어드는 것을 따라가면, Integral이 무엇을 공유하고 무엇을 새로 더하는지 보인다.
[5.body.0.beats.0.title] 기존 설계
[5.body.0.beats.0.text] 이해는 encoder 출력, 생성은 별도 VAE latent와 층마다 붙은 expert
[5.body.0.beats.1.title] 공유 토큰 $z$
[5.body.0.beats.1.text] encoder 여러 층을 AF가 모아 $z$로. 이해 입력과 생성 latent가 모두 $z$의 공간
[5.body.0.beats.2.text] 생성 stream은 VLM 32층 중 4층마다, 8곳에서만 VLM의 K/V를 읽는다
[5.body.0.beats.3.title] 두 질문
[5.body.0.beats.3.text] ① 공유 표현의 생성 이득은 무엇에서 오나 ② 그 이득은 어떤 조건에서 확인됐나
[5.body.0.caption] **Fig. 1 · 4 · 5**와 Sec. 2.2–2.3, App. A.1을 바탕으로 그림. 기존 설계는 Sec. 3.2의 BAGEL 서술(MoT, FLUX.1-VAE)
[5.notes.0] 먼저 논문이 대비하는 기존 설계입니다. 이해는 vision encoder의 출력을 VLM에 넣고, 생성은 별도 VAE latent에서 VLM의 층마다 붙은 생성 expert가 맡습니다. BAGEL이 이런 구조입니다.
[5.notes.1] [1] Integral은 고정된 encoder의 여러 층을 Abstraction Fusion으로 모아 토큰 z를 만듭니다. VLM의 이해 입력도, 생성할 latent도 이 z의 공간에 놓이고, 이미지는 pixel decoder가 되돌립니다.
[5.notes.2] [2] 생성 stream은 VLM 32층 전부가 아니라 네 층마다, 여덟 곳에서만 VLM의 key와 value를 읽습니다.
[5.notes.3] [3] 뒤의 분석에서 답할 질문은 두 가지입니다. 공유 표현의 이득이 재구성 품질 말고 무엇에서 오는지, 그리고 그 이득이 어떤 조건에서 확인됐는지입니다.

## Slide 6 — Propagation bottleneck 가설
[6.title] Propagation bottleneck 가설
[6.message] 저자들은 encoder를 재구성에 맞춰 학습하면 깊은 층이 초기층을 닮게 된다는 관측을 가설의 근거로 들고, encoder를 고정한 채 여러 층을 모으는 AF를 제안한다.
[6.body.0.alt] Fig. 3. (a) Joint 학습은 마지막 층까지 저수준 정보가 전달되어야 하고 AF는 고정 encoder의 여러 층을 직접 합친다. (b) 층별 CKA: Joint는 깊은 층에서도 약 0.85로 높고, 강한 의미 감독 Joint는 약 0.2, AF(고정)는 0.05까지 내려간다. (c) 20K step 동안 cosine과 PSNR: AF는 Frozen과 비슷한 cosine에 PSNR이 가장 높다.
[6.body.0.caption] **Fig. 3** (a) Joint 학습과 AF (b) 각 층과 초기층의 CKA (c) tokenizer 20K step 동안의 의미 cosine과 PSNR
[6.body.1.items.0] 저자 가설: 최종층만으로 재구성하게 학습하면 깊은 층이 초기층 정보를 붙들어 의미 추상화가 제약될 수 있다
[6.body.1.items.1] Joint 학습은 깊은 층의 CKA를 높인다. 의미 감독을 키우면 덜 높지만 PSNR이 낮다(Fig. 3b–c)
[6.body.1.items.2] AF는 20K step에서 cosine 약 0.97(Frozen 수준)과 PSNR 약 26.7 dB를 함께 얻는다(곡선)
[6.body.1.items.3.text] CKA는 상관 근거이고, 가설에 개입해 확인한 실험은 없다
[6.notes.0] 저자들은 이 trade-off를 propagation bottleneck이라는 가설로 설명합니다. 최종층만으로 재구성하게 학습하면 깊은 층이 초기층의 세부를 붙들어야 해서 의미 추상화가 제약된다는 것입니다.
[6.notes.1] 근거는 가운데 그림입니다. encoder를 함께 학습한 Joint는 깊은 층에서도 초기층과의 CKA가 높고, 의미 감독을 강화하면 CKA는 내려가지만 오른쪽 그림처럼 PSNR이 낮아집니다. AF는 encoder를 고정한 채 여러 층을 모아 cosine과 PSNR을 함께 얻습니다.
[6.notes.2] 다만 CKA는 상관을 보여 줄 뿐이고, 가설에 직접 개입한 실험은 없습니다.

## Slide 7 — Abstraction Fusion의 토큰 구성
[7.title] Abstraction Fusion의 토큰 구성
[7.message] AF는 같은 위치에서 encoder의 여러 층이 낸 표현을 모아 256차원 토큰 하나로 압축한다.
[7.body.0.left.0.alt] Fig. 4. 고정 vision encoder의 여러 층이 Abstraction Fusion(per-layer norm과 projection, self-attention, linear pooler)으로 들어가고, VAE를 지나 z가 된 뒤 semantic projector와 pixel decoder로 갈라진다.
[7.body.0.left.0.caption] **Fig. 4** Abstraction Fusion과 두 출력
[7.body.0.right.0.steps.0.title] 28개 표현
[7.body.0.right.0.steps.0.text] Qwen3.5-9B vision encoder 27블록 + patch embedding, patch 16, $d_h$ = 1152
[7.body.0.right.0.steps.1.title] 층별 정규화와 projection
[7.body.0.right.0.steps.1.text] ImageNet 50K장으로 구한 고정 통계, 4층씩 묶어 위치당 7개
[7.body.0.right.0.steps.2.title] 층 방향 self-attention과 pooler
[7.body.0.right.0.steps.2.text] 16 head, 위치마다 융합 표현 $f$, $d_f$ = 1152 (Eq. 1)
[7.body.0.right.0.steps.3.text] $z$, $d_z$ = 256. 학습 때는 샘플, 추론 때는 posterior mean
[7.notes.0] Qwen3.5-9B의 vision encoder는 27개 블록입니다. patch embedding까지 28개 표현을 모두 씁니다.
[7.notes.1] 층마다 고정 통계로 정규화하고, 네 층씩 묶어 위치마다 일곱 개 feature를 만듭니다. 층 방향 self-attention과 linear pooler가 이것을 융합 표현 f로 합치고, variational bottleneck이 256차원 z로 압축합니다. encoder 자체는 바꾸지 않습니다.

## Slide 8 — AF의 두 출력과 학습 목표
[8.title] AF의 두 출력과 학습 목표
[8.message] 같은 z에서 VLM의 원래 시각 embedding을 예측하는 손실과 이미지를 복원하는 손실을 함께 건다.
[8.body.0.left.0.items.0.text] 2×2 토큰을 합쳐 MLP로 VLM 시각 입력($d_s$ = 4096)에. 표적은 원래 VLM의 $s$
[8.body.0.left.0.items.1.text] RAE의 ViT-XL(28층, 폭 1152). 마지막 단계에서 decoder만 adversarial loss로 미세조정
[8.body.0.right.0.symbols.1.1] 토큰별 RMS 정규화: 둘째 항은 $2(1-\cos)$
[8.notes.0] z는 두 곳으로 갑니다. semantic projector는 이웃한 네 토큰을 합쳐 원래 VLM이 받던 4096차원 시각 입력을 예측하고, pixel decoder는 같은 z에서 이미지를 복원합니다.
[8.notes.1] 의미 손실은 원래 embedding의 MSE와 토큰별로 정규화한 MSE를 섞습니다. 정규화한 두 벡터의 MSE를 전개하면 cosine distance의 두 배이므로, 본문이 말하는 cosine-distance 항이 이것입니다. 학습 내내 vision encoder와 VLM은 고정입니다.

## Slide 9 — Block-wise MoT의 조건 전달
[9.title] Block-wise MoT의 조건 전달
[9.message] 생성 stream의 query가 VLM 블록 경계에서 두 stream의 key와 value를 읽고, 생성 전용 파라미터는 0.89B다.
[9.body.0.left.0.alt] Fig. 5(a)(b). Full MoT는 VLM 층마다 MoT 층을 짝짓고, Block-wise MoT는 VLM 층 여러 개를 묶어 경계에서만 MoT 층을 두고 AdaLN으로 timestep을 넣는다.
[9.body.0.left.0.caption] **Fig. 5(a)(b)** Full MoT와 Block-wise MoT
[9.body.0.right.0.groups.0.heading] 조건 전달
[9.body.0.right.0.groups.0.items.0] VLM 32층에 4층 간격으로 생성 block 8개
[9.body.0.right.0.groups.0.items.1] query는 생성 stream, key·value는 두 stream(VLM 층의 것을 재사용, Eq. 4)
[9.body.0.right.0.groups.0.items.2] $z_t$는 2층 MLP를 거쳐 생성 stream에만. VLM은 그대로
[9.body.0.right.0.groups.1.heading] 규격
[9.body.0.right.0.groups.1.items.0] QKV 차원은 VLM과 같고 나머지 폭 $d_g$ = 2048
[9.body.0.right.0.groups.1.items.1] timestep은 block마다 adaLN-single(Fig. 5d)
[9.body.0.right.0.groups.1.items.2] DDT head 2블록·폭 3072가 velocity 예측. 생성 전용 0.89B(891M)
[9.notes.0] 생성 stream은 VLM 32층 중 네 층마다 붙은 여덟 개 block입니다. 각 block의 query는 생성 stream에서 나오고, key와 value는 생성 stream과 해당 VLM 층 양쪽에서 가져옵니다. VLM의 계산은 바뀌지 않습니다.
[9.notes.1] timestep은 block마다 adaLN-single로 넣는데, Fig. 5d에서 입력에 더하는 방식보다 GenEval 곡선이 높았습니다. 마지막 DDT head가 velocity를 예측하고, 생성 전용 파라미터는 모두 0.89B입니다. 참고로 부록 C.2는 Full MoT를 31블록으로 적어 32층과 하나가 다른데, 논문은 이유를 밝히지 않습니다.

## Slide 10 — 학습 단계와 규모
[10.title] 학습 단계와 규모
[10.message] tokenizer를 먼저 학습해 z의 공간을 고정하고 생성을 600K step 학습한다. 뒤의 통제 비교는 생성 1단계 설정의 50K step이다.
[10.body.0.columns.0.label] 단계
[10.body.0.columns.1.label] 학습
[10.body.0.columns.3.label] 해상도
[10.body.0.groups.0.rows.0.cells.1] AF 전체
[10.body.0.groups.0.rows.1.cells.1] 동적 해상도
[10.body.0.groups.0.rows.2.cells.1] pixel decoder만, adversarial
[10.body.0.groups.1.label] 생성
[10.body.1.text] Sec. 3.4–3.6의 통제 비교는 생성 1단계 설정의 50K step: 1단계 200K의 1/4, 생성 전체 600K의 1/12
[10.notes.0] tokenizer는 세 단계로 학습하고, 마지막에는 z의 공간을 고정한 채 pixel decoder만 미세조정합니다. 생성은 text-to-image부터 interleaved SFT까지 600K step입니다. VLM은 처음부터 끝까지 고정입니다.
[10.notes.1] 뒤에서 볼 통제 비교는 생성 1단계 설정에서 50K step까지만 학습한 결과입니다. 생성 전체 일정의 12분의 1이라는 점을 기억해 두시면 좋겠습니다.

## Slide 11 — AF의 재구성과 이해 유지
[11.title] AF의 재구성과 이해 유지
[11.message] 최종 AF tokenizer는 재구성 전용 VAE와 비슷하거나 나은 재구성을 하면서 Qwen3.5-9B의 이해 성능을 평균 99.8% 유지한다.
[11.body.0.left.0.groups.0.label] 통합 tokenizer
[11.body.0.left.0.groups.1.label] 재구성 전용
[11.body.0.left.1.text] **Table 1** ImageNet-1k 256×256 재구성. 최종 tokenizer(전체 학습과 decoder 미세조정 후). 행 일부만 옮김
[11.body.0.right.0.body.0.items.0.label] 이해 20개 벤치마크 평균 유지율
[11.body.0.right.0.body.1.text] **Table 2** Qwen3.5-9B와 AF를 붙인 Qwen3.5-9B
[11.notes.0] 왼쪽은 최종 tokenizer의 재구성 결과입니다. AF는 PSNR 32.2 dB로, 재구성 전용인 FLUX.1-VAE의 31.1 dB보다 조금 높습니다.
[11.notes.1] 오른쪽은 이해 성능입니다. VLM이 원래 시각 입력 대신 AF를 거친 입력을 받아도 20개 벤치마크 평균으로 99.8%를 유지합니다. MMMU는 조금 오르고 OCRBench는 조금 내립니다.

## Slide 12 — 이해·생성 시스템 비교
[12.title] 이해·생성 시스템 비교
[12.message] 최종 Integral은 기반 VLM의 이해 점수를 유지하면서 GenEval 0.88, ImgEdit 3.50을 얻는다. 백본과 데이터가 다른 시스템끼리의 비교다.
[12.body.0.columns.0.label] 모델
[12.body.1.text] **Table 3 · 4** 최종 시스템 비교: 백본과 학습 데이터가 모델마다 다르다(통제 비교 아님). ImgEdit-Bench Overall은 GPT-4.1 평가. GPT-4o 행은 Table 3의 GPT-4o-Image와 Table 4의 GPT-4o. 행·열 일부
[12.notes.0] 최종 시스템끼리의 비교입니다. Integral은 기반인 Qwen3.5-9B의 MMMU를 그대로 유지하고, GenEval 0.88과 GenEval++ 0.743을 얻습니다. GenEval++는 GPT-4o-Image와 비슷하고, DPG에서는 TUNA-2가 더 높습니다.
[12.notes.1] 편집에서는 ImgEdit Overall 3.50으로 BAGEL과 OmniGen2보다 높고 GPT-4o보다는 낮습니다. 다만 이 표는 백본과 학습 데이터가 모두 다른 시스템을 나란히 놓은 것입니다. BAGEL과의 이해 점수 차이도 출발한 VLM에서 이미 납니다.

## Slide 13 — 세계 지식이 필요한 생성과 편집
[13.title] 세계 지식이 필요한 생성과 편집
[13.message] 지식이 필요한 생성과 편집에서도 Integral은 BAGEL보다 높고, 생성에서는 56B FLUX.2-dev에 가깝다.
[13.body.0.reveals] 같은 지식 평가를 생성과 편집으로 나누어 보면, 프롬프트가 이름을 대지 않는 대상을 그리는 일과 입력 이미지를 지식에 맞게 바꾸는 일 모두에서 BAGEL과의 차이가 난다.
[13.body.0.states.0.label] 지식 생성
[13.body.0.states.0.alt] Fig. 2 둘째 줄. 도쿄가 있는 나라의 산(후지산), 영국의 선사시대 거석 원(스톤헨지), 교토의 수천 개 주황 문 아래 참배길(후시미 이나리), 물에 녹는 과망간산칼륨(보라색 용액)을 생성한 이미지.
[13.body.0.states.0.text] Overall: Integral 0.556, BAGEL 0.352, FLUX.2-dev(56B) 0.565. CoT를 쓰면 Integral 0.788, BAGEL 0.628.
[13.body.0.states.1.label] 지식 편집
[13.body.0.states.1.alt] Fig. 2 편집. 고양이 가면을 베네치아 카니발의 화려한 가면으로, 덜 익은 스테이크를 웰던으로 바꾼 전후 이미지.
[13.body.0.states.1.text] Overall: Integral 60.79, BAGEL 56.40. 사실·개념·절차 세 범주 모두 Integral이 높다(GPT-4o 평가).
[13.body.0.mediaCaption] **Fig. 2** 굵은 글씨가 지식이 필요한 부분, 괄호는 그 뜻. 저자가 고른 예시. 두 표 모두 최종 시스템 비교
[13.notes.0] [1] 지식 생성 예시입니다. 프롬프트는 후지산이라는 이름을 말하지 않고 도쿄가 있는 나라의 산이라고만 합니다. WISE-Verified에서 Integral은 0.556으로 BAGEL보다 높고, 56B인 FLUX.2-dev의 0.565에 가깝습니다. CoT를 붙이면 0.788까지 오릅니다.
[13.notes.1] [2] 편집에서는 입력 이미지를 지시가 가리키는 지식에 맞게 바꿔야 합니다. KRIS-Bench에서 Integral은 60.79로 BAGEL보다 높고, 세 범주 모두에서 앞섭니다. 이 역시 최종 시스템끼리의 비교이고, 예시는 저자가 고른 것입니다.

## Slide 14 — AF와 FLUX.1-VAE: 50K step 비교
[14.title] AF와 FLUX.1-VAE: 50K step 비교
[14.message] 같은 VLM 조건과 생성 설정에서 재구성 PSNR은 1.1 dB 차이지만 50K step GenEval은 0.41 대 0.18이다.
[14.body.0.left.0.alt] Fig. 1 오른쪽. 10K–50K step GenEval: AF는 0.12에서 0.41로, FLUX.1 VAE는 0.07에서 0.18로 오른다.
[14.body.0.left.0.caption] **Fig. 1** 오른쪽. 256×256 text-to-image, 50K step까지의 GenEval
[14.body.0.right.0.items.1.label] PSNR, 최종 tokenizer
[14.body.0.right.1.items.0] 같게 둔 것: Qwen3.5-9B 조건, 생성 구조, 256×256 50K step 학습
[14.body.0.right.1.items.1.text] 저자 해석: 재구성 품질이 비슷한데 생성 차이가 크니, VLM과 표현을 공유한 덕이다
[14.body.0.right.1.items.2] 두 latent의 차원·토큰 수·분포를 맞췄다는 보고는 없다
[14.notes.0] 이제 이 발표의 중심인 통제 비교입니다. VLM 조건과 생성 구조, 학습 설정은 같고 생성할 latent만 AF와 FLUX.1-VAE로 바꿨습니다.
[14.notes.1] 두 tokenizer의 재구성 PSNR은 1.1 dB 차이인데, 50K step의 GenEval은 0.41 대 0.18로 두 배 넘게 벌어집니다. 저자들은 재구성 품질로 설명되지 않는 이 차이를 VLM과 표현을 공유한 덕으로 봅니다.
[14.notes.2] 다만 두 latent는 차원과 토큰 수, 분포도 다를 수 있고, 이를 맞췄다는 보고는 없습니다. 다음 장의 네 비교가 이 해석을 하나씩 좁혀 갑니다.

## Slide 15 — 통제 비교 네 가지
[15.title] 통제 비교 네 가지
[15.message] 네 비교는 각각 다른 대안 설명을 겨누고, 조건 VLM이 없는 LLM + AF도 VLM + FLUX.1-VAE보다 높다는 점이 함께 드러난다.
[15.body.0.reveals] 같은 50K step 예산에서 한 가지씩 바꾼 비교를 넘겨 보면, 각 결과가 어떤 대안 설명을 지우고 어떤 설명을 남기는지 보인다.
[15.body.0.states.0.label] 외부 encoder
[15.body.0.states.0.alt] Fig. 6(a). 10K–50K step GenEval: AF(ours) 0.12에서 0.41, SigLIP2-AF 0.15에서 0.31, FLUX.1-VAE 0.07에서 0.18. 10K에서는 SigLIP2-AF가 조금 위, 20K부터 AF가 위.
[15.body.0.states.0.title] SigLIP2-AF: 같은 AF, 다른 encoder
[15.body.0.states.0.text] 50K GenEval: AF 0.41, SigLIP2-AF 0.31. 함께 바뀐 것: 정렬 표적과 PSNR(34.08 dB). 의미 표현이면 어느 encoder든 같다는 설명을 겨눈다.
[15.body.0.states.1.label] 조건 모델
[15.body.0.states.1.alt] Fig. 6(b). 10K–50K step GenEval: VLM + AF 0.41, LLM + AF 약 0.28, VLM + FLUX.1-VAE 약 0.18, LLM + FLUX.1-VAE 약 0.17.
[15.body.0.states.1.title] VLM 조건과 text-only LLM 조건
[15.body.0.states.1.text] VLM으로 바꾸면 AF +0.13, FLUX.1-VAE +0.01. 곡선에서 LLM + AF(약 0.28)도 VLM + FLUX.1-VAE(약 0.18)보다 위. 비교 LLM의 이름과 크기는 밝히지 않았다.
[15.body.0.states.2.label] 의미 정렬 제거
[15.body.0.states.2.alt] Fig. 10(a). 10K–50K step GenEval: AF(ours) 0.12에서 0.41, AF w/o sem. 0.07에서 0.25.
[15.body.0.states.2.title] AF w/o sem.: 재구성은 더 좋다
[15.body.0.states.2.text] 의미 정렬 손실만 뺐다. PSNR 32.2 → 33.7 dB, rFID 0.15 → 0.13. 50K 동안 GenEval·DPG·WISE 곡선은 모두 AF보다 낮다.
[15.body.0.states.3.label] 2B 백본
[15.body.0.states.3.title] Qwen3.5-2B에 AF
[15.body.0.states.3.text] 2B AF 0.26, 9B FLUX.1-VAE 0.18, 9B AF 0.41. 2B AF의 PSNR 32.33 dB, 이해 유지율 99.2%. 2B × FLUX.1-VAE는 없다.
[15.body.0.mediaCaption] **Fig. 6a · 6b · 10a · 7** 256×256 text-to-image, 50K step까지의 GenEval. 네 그림 모두 x축 10K–50K, y축 0부터
[15.notes.0] [1] 첫째, 같은 AF 구조를 외부 의미 encoder인 SigLIP2에 붙였습니다. 재구성은 34.08 dB로 더 좋지만 50K GenEval은 0.31로 낮습니다. 다만 encoder를 바꾸면서 정렬 표적과 PSNR도 함께 바뀌었고, 10K에서는 SigLIP2-AF가 잠깐 앞섭니다.
[15.notes.1] [2] 둘째, 조건을 주는 모델을 VLM과 text-only LLM으로 바꿨습니다. VLM으로 바꿀 때 AF는 0.13 오르고 FLUX.1-VAE는 0.01 오릅니다. 저자들은 공유 표현이 VLM 조건을 더 잘 쓴다는 근거로 봅니다. 그런데 그림을 보면 VLM 없이 LLM 조건만 준 AF도 0.28로, VLM 조건의 FLUX.1-VAE 0.18보다 높습니다.
[15.notes.2] [3] 셋째, AF에서 의미 정렬 손실만 뺐습니다. 재구성은 33.7 dB로 오히려 좋아지는데, GenEval과 DPG, WISE 곡선은 모두 낮아집니다. 재구성 품질이 생성을 정한다는 설명은 여기서 다시 맞지 않습니다.
[15.notes.3] [4] 넷째, 2B 백본에 AF를 붙이면 9B FLUX.1-VAE보다 높습니다. 다만 2B에 FLUX.1-VAE를 붙인 짝은 없습니다.

## Slide 16 — 지운 설명과 남은 설명
[16.title] 지운 설명과 남은 설명
[16.message] 재구성 품질만으로 생성 차이를 설명할 수는 없다. 하지만 그 차이가 VLM과의 공유에서 오는지, latent 자체에서 오는지는 다 갈리지 않았다.
[16.body.0.columns.0.label] 대안 설명
[16.body.0.columns.1.label] 겨눈 비교
[16.body.0.columns.2.label] 결과(256², 50K step)
[16.body.0.columns.3.label] 판정
[16.body.0.groups.0.rows.0.cells.0] 재구성 품질이 생성을 정한다
[16.body.0.groups.0.rows.0.cells.2] PSNR이 비슷하거나 높아도 GenEval은 낮다
[16.body.0.groups.0.rows.0.cells.3] **지움**
[16.body.0.groups.0.rows.1.cells.0] 의미 표현이면 충분하다
[16.body.0.groups.0.rows.1.cells.2] 0.31 대 0.41. encoder·표적·PSNR도 다름
[16.body.0.groups.0.rows.1.cells.3] 일부
[16.body.0.groups.0.rows.2.cells.0] latent 자체가 학습하기 쉽다
[16.body.0.groups.0.rows.2.cells.1] LLM 조건
[16.body.0.groups.0.rows.2.cells.2] LLM + AF 약 0.28 > VLM + FLUX.1-VAE 약 0.18
[16.body.0.groups.0.rows.2.cells.3] **남음**
[16.body.0.groups.0.rows.3.cells.0] 9B 백본이라서
[16.body.0.groups.0.rows.3.cells.1] 2B 백본
[16.body.0.groups.0.rows.3.cells.2] 2B AF 0.26 > 9B FLUX.1-VAE 0.18. 2B짝 없음
[16.body.0.groups.0.rows.3.cells.3] 일부
[16.body.0.groups.0.rows.4.cells.0] 초기 수렴이 빠를 뿐이다
[16.body.0.groups.0.rows.4.cells.1] 없음
[16.body.0.groups.0.rows.4.cells.2] 50K까지만, 600K 전체 비교 없음
[16.body.0.groups.0.rows.4.cells.3] **남음**
[16.body.1.text] 판정은 발표자의 해석. ‘약’이 붙은 값은 Fig. 6b 곡선에서 읽음. 남은 두 설명은 토론 1·2번
[16.notes.0] 앞의 비교들을 대안 설명별로 정리했습니다. 재구성 품질이 생성을 정한다는 설명은 FLUX.1-VAE와 의미 정렬 제거, 두 비교에서 모두 맞지 않습니다. 이것은 지워졌다고 봐도 됩니다.
[16.notes.1] 의미 표현이면 충분하다는 설명과 백본 크기 설명은 일부만 지워졌습니다. SigLIP2 비교에서는 다른 것도 함께 바뀌었고, 2B에는 FLUX.1-VAE 짝이 없습니다.
[16.notes.2] 남은 것은 둘입니다. LLM 조건에서도 AF가 앞서므로 이득의 일부는 VLM과의 공유가 아니라 latent 자체에서 올 수 있습니다. 그리고 모든 비교가 50K step이라, 수렴이 빠른 것인지 최종 품질이 다른 것인지는 알 수 없습니다. 이 둘을 토론에서 다시 묻겠습니다.

## Slide 17 — AF 융합 방식 비교
[17.title] AF 융합 방식 비교
[17.message] 20K step tokenizer 비교에서 AF는 단순 합산이나 attention pooling보다 재구성이 좋으면서 고정 encoder 수준의 cosine을 유지한다.
[17.body.0.left.0.alt] Fig. 8. tokenizer 학습 5K–20K step 동안 의미 cosine과 PSNR. AF의 PSNR이 24에서 26.7로 가장 높고, attention pooling 약 22, MLS 약 20.4, Frozen 약 19.4. cosine은 Frozen과 AF가 약 0.97로 가장 높다.
[17.body.0.left.0.caption] **Fig. 8** 융합 방식별 cosine과 PSNR, tokenizer 20K step. AF는 MLS보다 PSNR +6.27 dB
[17.body.0.right.0.columns.0.label] 변형
[17.body.0.right.0.groups.0.rows.1.cells.0] norm·proj. 공유
[17.body.0.right.0.groups.0.rows.2.cells.0] self-attention 제거
[17.body.0.right.1.text] **Table 10** 20K step 시점. 최종 tokenizer(Table 1, 32.2 dB)와 학습량이 다르다
[17.notes.0] AF의 융합 구조를 단순한 대안과 비교했습니다. 층별 표현을 그냥 더하는 MLS보다 PSNR이 6.27 dB 높고, cosine은 고정 encoder 수준입니다.
[17.notes.1] 오른쪽 표는 AF의 구성요소를 하나씩 바꾼 결과입니다. 어느 것을 바꿔도 세 지표가 모두 나빠지고, attention pooling으로 바꾸면 크게 떨어집니다. 여기 26.67 dB는 20K step 시점이라 앞의 32.2 dB와는 학습량이 다릅니다.

## Slide 18 — 생성 구조 비교: MMDiT와 Full MoT
[18.title] 생성 구조 비교: MMDiT와 Full MoT
[18.message] 같은 AF 공간에서 Block-wise MoT는 MMDiT보다 GenEval이 높고, Full MoT와는 비슷한 품질을 더 적은 계산으로 낸다.
[18.body.0.left.0.alt] Fig. 9. 10K–50K step GenEval: Block-wise MoT(891M) 0.12에서 0.41, MMDiT(962M) 0.06에서 0.28.
[18.body.0.left.0.caption] **Fig. 9** Block-wise MoT(891M)와 MMDiT(962M). 같은 AF, DDT head, 학습 설정
[18.body.0.right.0.columns.0.label] 구조(blocks)
[18.body.0.right.1.items.0.label] denoising 계산, Full MoT가 더 큼
[18.body.0.right.1.items.1.label] batch당 지연, Full MoT가 더 큼
[18.body.0.right.2.text] **Table 13** 같은 AF, 50K step 학습 후. 배치 크기와 denoising step 수는 보고되지 않음
[18.notes.0] 생성 구조도 비교했습니다. 같은 AF 공간과 DDT head를 쓰면, 파라미터가 조금 적은 Block-wise MoT가 MMDiT보다 GenEval 곡선이 계속 높습니다.
[18.notes.1] 층마다 block을 붙인 Full MoT와 비교하면 GenEval과 DPG는 Block-wise가, WISE는 Full MoT가 조금 높습니다. 대신 Full MoT는 계산이 2.5배, 지연이 3.1배입니다. 측정에 쓴 배치 크기와 step 수는 논문에 없습니다.

## Slide 19 — 한계와 비용
[19.title] 한계와 비용
[19.message] 공유의 이득은 짧은 학습과 Qwen3.5 계열에서 확인됐고, 생성 전용 0.89B 밖에도 비용이 든다.
[19.body.0.groups.0.heading] 검증 범위
[19.body.0.groups.0.items.0] tokenizer 통제 비교는 256², 50K step, 주로 GenEval
[19.body.0.groups.0.items.1] 조건 VLM은 Qwen3.5 계열(9B, 2B)만
[19.body.0.groups.0.items.2] $z$를 다음 턴 입력으로 바로 쓰면 손실이 없다는 이점(Sec. 2.2)은 측정 없음
[19.body.0.groups.1.heading] 평가
[19.body.0.groups.1.items.0] 20K ablation의 의미 지표는 학습 표적과 같은 cosine
[19.body.0.groups.1.items.1] WISE-Verified의 판정 모델은 Qwen3.5-35B-A3B로 백본과 같은 계열(외부 자료)
[19.body.0.groups.1.items.2] GenEval 2 저자들은 GenEval이 이미 포화됐다고 본다(외부 자료)
[19.body.0.groups.2.heading] 비용
[19.body.0.groups.2.items.0] VLM의 시각 입력 경로 456.0M → 582.1M, pixel decoder 475.1M 별도
[19.body.0.groups.2.items.1] prefill 42.6 → 54.9 ms(+28.9%). 100 토큰 생성까지 포함하면 +2.1%
[19.notes.0] 한계는 세 가지로 정리했습니다. 먼저 검증 범위입니다. 통제 비교는 256 해상도에서 50K step까지, 주로 GenEval로 했고, 조건 VLM은 Qwen3.5 계열뿐입니다. z를 다음 턴에 바로 다시 쓰면 손실이 없다는 이점도 실험으로 재지 않았습니다.
[19.notes.1] 평가에서는 외부 자료 두 가지를 덧붙입니다. WISE-Verified는 Qwen3.5-35B로 채점하는데, Integral의 백본과 같은 계열입니다. 또 GenEval 2의 저자들은 GenEval이 이미 포화됐다고 봅니다.
[19.notes.2] 비용도 있습니다. 생성 전용 0.89B 말고도 시각 입력 경로가 126M 커지고, pixel decoder가 475M입니다. 이해 추론에서 prefill은 29% 늘지만, 100 토큰을 생성하는 전체 지연으로는 2.1%입니다.

## Slide 20 — 정리와 토론
[20.title] 정리와 토론
[20.message] 재구성 품질만으로 생성 차이를 설명할 수 없다는 점은 여러 비교가 뒷받침하지만, 그 차이를 VLM과의 공유로 돌리는 것은 저자 해석이다.
[20.body.0.groups.0.heading] 정리
[20.body.0.groups.0.items.0] 고정 encoder의 여러 층을 모은 $z$ 하나로 이해(99.8% 유지)와 재구성(32.2 dB)을 함께
[20.body.0.groups.0.items.1] 50K step 비교에서 재구성 품질로는 생성 차이가 설명되지 않는다
[20.body.0.groups.0.items.2] 그 차이를 VLM과의 공유로 돌리는 것은 저자 해석이다
[20.body.0.groups.1.heading] 토론
[20.body.0.groups.1.items.0] LLM + AF(약 0.28)도 VLM + FLUX.1-VAE(약 0.18)보다 높다. 공유의 몫과 latent 자체의 몫을 어떻게 나눠 잴까?
[20.body.0.groups.1.items.1] 통제 비교는 생성 600K 중 50K step의 GenEval이다. 수렴이 빠른 것인가, 최종 품질이 다른 것인가?
[20.body.0.groups.1.items.2] $z$를 다음 턴에 다시 쓰는 이점과 propagation bottleneck은 측정·개입 실험이 없다. 무엇을 재면 될까?
[20.body.0.groups.1.items.3.text] 0.89B 밖의 비용(시각 경로 +126.1M, pixel decoder 475.1M, VLM마다 tokenizer 650K step)을 넣어도 이득이 큰 조건은?
[20.notes.0] 정리하겠습니다. Integral은 고정된 encoder의 여러 층을 모은 z 하나로 이해를 거의 그대로 유지하면서 재구성까지 해냅니다. 50K step 비교들은 재구성 품질만으로는 생성 차이가 설명되지 않는다는 점을 뒷받침합니다. 다만 그 차이를 VLM과의 공유로 돌리는 것은 저자들의 해석입니다.
[20.notes.1] 토론하고 싶은 것은 네 가지입니다. 첫째, VLM 조건 없이 LLM 조건만 준 AF도 FLUX.1-VAE보다 높았습니다. 공유에서 오는 몫과 latent 자체에서 오는 몫을 어떻게 나눠 잴 수 있을까요? 둘째, 비교는 모두 50K step의 GenEval입니다. 수렴이 빠른 것인지 최종 품질이 다른 것인지 어떻게 가릴 수 있을까요?
[20.notes.2] 셋째, z를 다음 턴에 다시 쓰는 이점과 propagation bottleneck은 직접 잰 실험이 없습니다. 무엇을 재면 확인할 수 있을까요? 넷째는 제 해석에서 나온 질문입니다. 생성 전용 0.89B 밖에도 시각 경로와 pixel decoder, VLM을 바꿀 때마다 다시 하는 tokenizer 학습이 듭니다. 이 비용을 넣어도 이득이 큰 조건은 무엇일까요?

## Slide 21 — 감사합니다
[21.title] 감사합니다
[21.links.1] 코드 · github.com/the-jb/integral · 체크포인트 · huggingface.co/the-jb/Integral-9B
[21.notes.0] 들어 주셔서 감사합니다. 특히 공유의 몫과 latent 자체의 몫을 가르려면 어떤 실험이 필요할지 의견을 듣고 싶습니다.

