| location | original | edit | rule |
|---|---|---|---|
| 1.notes.0 | 오늘은 NAVER Cloud와 KAIST의 Integral을 소개합니다. 사전학습 VLM에 이미지 생성을 붙이되, 이해와 생성이 같은 시각 표현을 쓰게 한 연구입니다. 그 효과를 통제 비교 중심으로 보겠습니다. | 오늘은 NAVER Cloud와 KAIST의 Integral을 소개합니다. 사전학습 VLM에 이미지 생성 기능을 붙이면서, 이미지를 이해할 때와 생성할 때 같은 시각 토큰을 쓰게 한 연구입니다. 이렇게 같은 토큰을 쓰는 것이 생성에 정말 도움이 되는지, 논문의 비교 실험을 중심으로 보겠습니다. | L1-8 |
| 2.title | Integral의 구조와 통제 비교 | Integral의 구조와 비교 실험 | L1-8 |
| 2.message | Integral은 고정된 VLM의 vision encoder에서 여러 층의 표현을 모아 시각 토큰 하나를 만든다. 이 토큰을 이해 입력과 생성 latent로 함께 쓴다. | Integral은 고정된 VLM의 vision encoder에서 여러 층의 표현을 모아 시각 토큰 하나를 만든다. VLM이 이미지를 읽을 때도, 이미지를 생성할 때도 이 토큰을 쓴다. | L3-3 |
| 2.body.0.text | 고정된 VLM의 vision encoder에서 여러 층의 표현을 모아 시각 토큰 $z$ 하나를 만든다. 이 토큰을 이해 입력과 생성 latent로 함께 쓴다. | 고정된 VLM의 vision encoder에서 여러 층의 표현을 모아 시각 토큰 $z$ 하나를 만든다. VLM이 이미지를 읽을 때도, 이미지를 생성할 때도 이 토큰을 쓴다. | L3-3 |
| 2.body.1.items.1.text | VLM 32층 중 4층마다 K/V를 읽는 생성 stream, 생성 전용 0.89B | 생성을 맡는 별도 transformer(0.89B)가 VLM 32층 중 4층마다 VLM의 K/V를 참조 | L3-3 |
| 2.body.1.items.2.title | 표현 공유의 효과를 살피는 통제 비교 | 생성 비교 실험 | L1-3 |
| 2.body.1.items.2.text | tokenizer·조건 모델·의미 정렬·백본 크기를 바꾼 50K step 비교 | tokenizer, 조건을 주는 모델, 의미 정렬 손실, 백본 크기를 하나씩 바꾸고 50K step 학습해 비교 | L3-3 |
| 2.notes.1 | 구성 요소는 둘입니다. Abstraction Fusion은 vision encoder의 여러 층에서 나온 표현을 모아 z를 만들고, Block-wise MoT는 VLM의 네 층마다 조건을 읽습니다. 저자들은 통제 비교를 근거로 표현을 공유하면 생성 학습에 도움이 된다고 주장합니다. | 구성 요소는 둘입니다. Abstraction Fusion은 vision encoder의 여러 층에서 나온 표현을 모아 z를 만들고, Block-wise MoT는 생성을 맡는 transformer가 VLM의 네 층마다 VLM의 정보를 참조하게 합니다. 저자들은 비교 실험을 근거로, 이해와 생성이 같은 토큰을 쓰면 생성 학습이 잘된다고 주장합니다. | L1-11 |
| 5.message | Integral은 VLM의 이해 입력과 같은 토큰 z를 생성 latent로 쓴다. 생성 stream이 VLM의 key와 value를 읽는 빈도는 네 층마다 한 번으로 줄인다. | Integral은 VLM이 읽는 이미지 토큰 z를 생성 모델의 latent로도 쓴다. 생성 stream이 VLM의 key와 value를 참조하는 곳은 네 층마다 한 곳으로 줄인다. | L3-3 |
| 5.body.0.beats.1.text | AF가 encoder 여러 층을 모아 $z$로. 이해 입력은 $z$에서 만들고, 생성은 $z$의 공간에서 한다 | AF가 encoder 여러 층을 모아 $z$를 만든다. VLM은 $z$에서 만든 입력을 읽고, 생성 모델은 $z$와 같은 공간의 토큰을 만든다 | L3-3 |
| 5.body.0.beats.2.text | 생성 stream은 VLM 32층 중 4층마다, 8곳에서만 VLM의 K/V를 읽는다 | 생성 stream(생성을 맡는 transformer)은 VLM 32층 중 4층마다, 8곳에서만 VLM의 K/V를 참조한다 | L1-11 |
| 5.body.0.beats.3.text | ① 공유 표현의 생성 이득은 무엇에서 오나 ② 그 이득은 어떤 조건에서 확인됐나 | ① AF 토큰으로 생성이 잘되는 이유는 무엇인가 ② 어떤 실험 조건에서 확인했나 | L3-3 |
| 5.notes.1 | [1] Integral은 고정된 encoder의 여러 층에서 나온 표현을 Abstraction Fusion으로 모아 토큰 z를 만듭니다. VLM의 이해 입력은 z에서 projector로 만들고, 생성은 z의 공간에서 합니다. 이미지는 pixel decoder로 재구성합니다. | [1] Integral은 고정된 encoder의 여러 층에서 나온 표현을 Abstraction Fusion으로 모아 토큰 z를 만듭니다. VLM은 z를 projector에 통과시킨 입력을 읽고, 생성 모델은 z와 같은 공간의 토큰을 만듭니다. 이미지는 pixel decoder가 이 토큰에서 재구성합니다. | L3-3 |
| 5.notes.2 | [2] 생성 stream은 VLM 32층 전부가 아니라 네 층마다, 여덟 곳에서만 VLM의 key와 value를 읽습니다. | [2] 생성 stream은 생성을 맡는 별도 transformer입니다. VLM 32층 전부가 아니라 네 층마다, 여덟 곳에서만 VLM의 key와 value를 참조합니다. | L1-11 |
| 5.notes.3 | [3] 뒤에서 다룰 질문은 두 가지입니다. 공유 표현이 생성에 주는 이득은 재구성 품질 외에 어떤 요인에서 올까요? 그 이득은 어떤 조건에서 확인됐을까요? | [3] 뒤에서 답할 질문은 두 가지입니다. 첫째, AF 토큰으로 생성하면 왜 잘되는가, 재구성 품질 말고 다른 이유가 있는가. 둘째, 그 결과를 어떤 실험 조건에서 확인했는가입니다. | L3-3 |
| 9.message | 생성 stream의 query가 VLM의 block 경계에서 두 stream의 key와 value를 읽고, 생성 전용 파라미터는 0.89B다. | 생성 stream의 query는 VLM의 block 경계에서 생성 stream과 VLM 양쪽의 key·value를 참조한다. 생성 전용 파라미터는 0.89B다. | L3-3 |
| 9.notes.0 | 생성 stream은 VLM 32층 중 네 층마다 붙은 여덟 개 block입니다. 각 block의 query는 생성 stream에서 나오고, key와 value는 생성 stream과 해당 VLM 층 양쪽에서 가져옵니다. VLM의 계산은 바뀌지 않습니다. | 생성 stream은 생성을 맡는 별도 transformer로, VLM 32층 중 네 층마다 붙은 여덟 개 block입니다. 각 block의 query는 생성 stream에서 나오고, key와 value는 생성 stream과 해당 VLM 층 양쪽에서 가져옵니다. VLM의 계산은 바뀌지 않습니다. | L1-11 |
| 10.message | tokenizer를 먼저 학습해 z의 공간을 고정하고 생성을 600K step 학습한다. 뒤의 통제 비교는 생성 1단계 설정의 50K step이다. | tokenizer를 먼저 학습해 z의 공간을 고정한 뒤 생성 모델을 600K step 학습한다. 뒤의 비교 실험은 생성 1단계를 50K step만 학습한 결과다. | L3-3 |
| 10.body.2.text | 생성 통제 비교(Sec. 3.4–3.6)는 1단계 설정의 50K step: step 수로 생성 전체의 1/12 | Sec. 3.4–3.6의 생성 비교 실험은 1단계를 50K step만 학습한 결과: 생성 전체 step 수의 1/12 | L3-3 |
| 10.notes.1 | 뒤에서 볼 생성 통제 비교는 생성 1단계 설정에서 50K step까지만 학습한 결과입니다. step 수로는 생성 전체의 12분의 1이고, 뒤 단계는 해상도와 배치도 다릅니다. tokenizer 구조 비교는 이와 별도로 20K step입니다. | 뒤에서 볼 생성 비교 실험은 생성 1단계, 즉 256 해상도 text-to-image를 50K step까지만 학습한 결과입니다. step 수로는 생성 전체의 12분의 1이고, 뒤 단계는 해상도와 배치도 다릅니다. tokenizer 구조 비교는 이와 별도로 20K step입니다. | L3-3 |
| 12.body.1.text | **Table 3 · 4** 최종 시스템 비교: 백본과 학습 데이터가 모델마다 다르다(통제 비교 아님). ImgEdit-Bench Overall은 GPT-4.1 평가이고, 비공개 GPT-4o는 4.20. 굵게는 표에 보인 행 중 최고. 행·열 일부 | **Table 3 · 4** 최종 시스템 비교: 백본과 학습 데이터가 모델마다 다르다(조건을 맞춘 비교 아님). ImgEdit-Bench Overall은 GPT-4.1 평가이고, 비공개 GPT-4o는 4.20. 굵게는 표에 보인 행 중 최고. 행·열 일부 | L1-8 |
| 14.message | 같은 VLM 조건과 생성 설정에서 재구성 PSNR은 1.1 dB 차이지만 50K step GenEval은 0.41 대 0.18이다. | VLM, 생성 모델 구조, 학습 설정을 같게 두고 latent만 바꾸면, 재구성 PSNR은 1.1 dB 차이인데 50K step GenEval은 0.41 대 0.18이다. | L3-3 |
| 14.body.0.right.1.items.0 | 같게 둔 것: Qwen3.5-9B 조건, 생성 구조, 256×256 50K step 학습 | 같게 둔 것: 조건을 주는 Qwen3.5-9B, 생성 모델 구조, 학습(256×256, 50K step) | L3-3 |
| 14.notes.0 | 통제 비교에서는 VLM 조건과 생성 구조, 학습 설정을 같게 두고 생성할 latent만 AF와 FLUX.1-VAE로 바꿨습니다. | 이제 이 발표의 중심인 비교 실험입니다. 한 가지만 바꾸고 나머지는 같게 둔 실험입니다. 여기서는 조건을 주는 VLM, 생성 모델 구조, 학습 설정을 같게 두고, 생성 모델이 만들 latent만 AF와 FLUX.1-VAE로 바꿨습니다. | L1-11 |
| 15.title | 통제 비교 네 가지 | 하나씩 바꾼 비교 실험 네 가지 | L1-8 |
| 15.message | 네 비교에서 각각 다른 대안 설명을 검토한다. 조건 모델에 VLM을 쓰지 않은 LLM + AF도 VLM + FLUX.1-VAE보다 점수가 높다. | 네 실험은 GenEval 차이를 다른 이유로 설명할 수 있는지 하나씩 확인한다. VLM 대신 텍스트 전용 LLM이 조건을 줘도 AF가 FLUX.1-VAE보다 높다. | L3-3 |
| 15.body.0.reveals | 같은 50K step 동안 학습하면서 한 가지씩 바꿔 비교했다. 각 결과로 배제할 수 있는 대안 설명과 여전히 가능한 설명을 구분한다. | 같은 50K step 학습에서 한 가지씩 바꾼 실험을 넘겨 보면, GenEval 차이를 설명하는 이유 가운데 어떤 것이 맞지 않고 어떤 것이 아직 가능한지 보인다. | L3-3 |
| 15.body.0.states.0.text | 50K GenEval은 AF 0.41, SigLIP2-AF 0.31. 정렬 표적과 PSNR(ImageNet 256², 34.08 대 32.20 dB)도 함께 바뀌었다. 의미 표현을 쓰면 어느 encoder든 결과가 같은지 검토한 비교다. | 50K GenEval은 Qwen AF 0.41, SigLIP2-AF 0.31. encoder를 바꾸면서 정렬 대상과 재구성 PSNR(ImageNet 256², 34.08 대 32.20 dB)도 함께 바뀌었다. 의미를 담은 encoder면 어느 것이든 효과가 같은지 본 실험이다. | L3-3 |
| 15.body.0.states.1.title | VLM 조건과 text-only LLM 조건 | VLM이 조건을 줄 때와 텍스트 전용 LLM이 줄 때 | L1-8 |
| 15.body.0.states.1.text | VLM으로 바꾸면 AF +0.13, FLUX.1-VAE +0.01. 곡선에서 LLM + AF(약 0.28)도 VLM + FLUX.1-VAE(0.18)보다 높다. 비교 LLM의 이름과 크기는 밝히지 않았다. | LLM 대신 VLM이 조건을 주면 AF +0.13, FLUX.1-VAE +0.01. LLM 조건에서도 AF(곡선, 약 0.28)가 VLM 조건의 FLUX.1-VAE(0.18)보다 높다. 비교한 LLM의 이름과 크기는 밝히지 않았다. | L3-3 |
| 15.body.0.states.2.text | 의미 정렬 손실만 뺐다. PSNR 32.2 → 33.7 dB, rFID 0.15 → 0.13. GenEval·DPG·WISE(Fig. 10b–c) 곡선이 모두 AF보다 낮다. | 의미 정렬 손실만 뺐다. 재구성은 좋아졌지만(PSNR 32.2 → 33.7 dB, rFID 0.15 → 0.13) GenEval·DPG·WISE(Fig. 10b–c)는 모두 AF보다 낮다. | L3-3 |
| 15.notes.0 | [1] 첫째, 같은 AF 구조를 외부 의미 encoder인 SigLIP2에 붙였습니다. 재구성은 34.08 dB로 더 좋지만 50K GenEval은 0.31로 낮습니다. 다만 encoder를 바꾸면서 정렬 표적과 PSNR도 함께 바뀌었고, 10K에서는 SigLIP2-AF가 잠깐 앞섭니다. | [1] 첫째, 같은 AF 구조를 Qwen의 encoder 대신 외부 encoder인 SigLIP2에 붙였습니다. 재구성은 34.08 dB로 더 좋지만 50K GenEval은 0.31로 낮습니다. 다만 encoder를 바꾸면서 정렬 대상과 PSNR도 함께 바뀌었고, 10K에서는 SigLIP2-AF가 잠깐 앞섭니다. | L1-8 |
| 15.notes.1 | [2] 둘째, 조건을 주는 모델로 VLM과 text-only LLM을 비교했습니다. VLM으로 바꿀 때 AF는 0.13 오르고 FLUX.1-VAE는 0.01 오릅니다. 저자들은 이 차이를 공유 표현이 VLM 조건을 더 잘 활용한다는 근거로 봅니다. 그런데 그림을 보면 VLM 없이 LLM 조건만 준 AF도 곡선에서 약 0.28로, VLM 조건의 FLUX.1-VAE 0.18보다 높습니다. | [2] 둘째, 생성 모델에 조건을 주는 모델을 VLM과 텍스트 전용 LLM으로 바꿔 봤습니다. LLM 대신 VLM이 조건을 주면 AF는 0.13 오르고 FLUX.1-VAE는 0.01 오릅니다. 저자들은 이것을 VLM과 같은 토큰을 쓰는 AF가 VLM의 정보를 더 잘 활용한다는 근거로 봅니다. 그런데 그림을 보면 LLM이 조건을 준 AF도 곡선에서 약 0.28로, VLM이 조건을 준 FLUX.1-VAE의 0.18보다 높습니다. | L3-3 |
| 16.title | 통제 비교에서 배제된 설명과 남은 설명 | 50K step 비교로 확인한 것과 남은 질문 | L3-3 |
| 16.message | 재구성 품질만으로 생성 성능 차이를 설명할 수는 없다. 다만 그 차이를 설명할 때 VLM과의 표현 공유 효과와 latent 자체의 효과를 완전히 구분하지는 못했다. | 재구성 품질만으로는 GenEval 차이를 설명할 수 없다. 하지만 그 차이가 VLM과 같은 토큰을 써서 생긴 것인지, AF latent가 원래 학습하기 쉬워서인지는 실험으로 가르지 못했다. | L3-3 |
| 16.body.0.columns.0.label | 대안 설명 | 이렇게도 설명할 수 있나 | L3-3 |
| 16.body.0.columns.1.label | 해당 비교 | 확인한 실험 | L1-8 |
| 16.body.0.columns.3.label | 판정 | 결론 | L1-8 |
| 16.body.0.groups.0.rows.0.cells.0 | 재구성 품질이 순위를 정한다 | 재구성을 잘하는 latent라서? | L3-3 |
| 16.body.0.groups.0.rows.0.cells.2 | PSNR이 비슷하거나 높아도 GenEval은 낮다 | 재구성 점수가 비슷하거나 더 높아도 GenEval은 낮다 | L3-3 |
| 16.body.0.groups.0.rows.0.cells.3 | 지움 | 아니다 | L3-3 |
| 16.body.0.groups.0.rows.1.cells.0 | 의미 표현이면 충분하다 | 의미를 담은 encoder면 다 되나? | L3-3 |
| 16.body.0.groups.0.rows.1.cells.2 | 0.31 대 0.41. encoder·표적·PSNR도 다름 | 0.31 대 0.41. 정렬 대상·PSNR도 함께 바뀜 | L3-3 |
| 16.body.0.groups.0.rows.1.cells.3 | 일부 | 일부만 확인 | L3-3 |
| 16.body.0.groups.0.rows.2.cells.0 | latent 자체가 학습하기 쉽다 | AF latent가 원래 학습하기 쉬워서? | L3-3 |
| 16.body.0.groups.0.rows.2.cells.1 | LLM 조건 | LLM이 조건을 줌 | L3-3 |
| 16.body.0.groups.0.rows.2.cells.2 | LLM 조건에서도 AF 약 0.28 > FLUX.1-VAE 약 0.17 | LLM 조건에서도 AF 약 0.28 > FLUX.1-VAE 약 0.17 | L1-8 |
| 16.body.0.groups.0.rows.2.cells.3 | **남음** | **가능성 남음** | L3-3 |
| 16.body.0.groups.0.rows.3.cells.0 | 9B 백본이 생성 성능 차이의 원인이다 | 9B 큰 백본이라서? | L3-3 |
| 16.body.0.groups.0.rows.3.cells.2 | 2B AF 0.26 > 9B FLUX.1-VAE 0.18. 2B짝 없음 | 2B AF 0.26 > 9B FLUX.1-VAE 0.18. 2B FLUX.1-VAE 없음 | L3-3 |
| 16.body.0.groups.0.rows.3.cells.3 | 일부 | 일부만 확인 | L3-3 |
| 16.body.0.groups.0.rows.4.cells.0 | 초기 수렴이 빠를 뿐이다 | 학습 초반에 빨리 오를 뿐? | L3-3 |
| 16.body.0.groups.0.rows.4.cells.2 | 50K까지만, 600K 전체 비교 없음 | 모두 50K step까지. 전체 600K 학습에서 비교 없음 | L3-3 |
| 16.body.0.groups.0.rows.4.cells.3 | **남음** | **확인 안 됨** | L3-3 |
| 16.body.1.text | 판정은 발표자의 해석. ‘약’이 붙은 값은 Fig. 6b 곡선에서 읽음, 나머지는 본문 값. 남은 두 설명은 토론 1·2번 | 결론 열은 발표자의 판단. ‘약’이 붙은 값은 Fig. 6b 곡선에서 읽음, 나머지는 본문 값. 마지막 두 질문은 토론 1·2번 | L1-8 |
| 16.notes.0 | 앞의 비교들을 대안 설명별로 정리했습니다. 재구성 품질이 생성 성능을 결정한다는 설명은 FLUX.1-VAE와의 비교와 의미 정렬을 제거한 비교에서 모두 결과와 맞지 않습니다. 따라서 이 설명은 배제해도 됩니다. | 앞의 실험들을 질문 형태로 정리했습니다. GenEval 차이를 다르게 설명할 수 있는지 하나씩 봅니다. 먼저 재구성을 잘하는 latent라서 생성도 잘한다는 설명은 맞지 않습니다. FLUX.1-VAE와 비교할 때도, 의미 정렬 손실을 뺀 AF와 비교할 때도 재구성 점수가 비슷하거나 더 높은 쪽의 GenEval이 낮았습니다. | L3-3 |
| 16.notes.1 | 의미 표현이면 충분하다는 설명과 백본 크기가 원인이라는 설명은 일부만 배제할 수 있습니다. SigLIP2 비교에서는 정렬 표적과 PSNR도 함께 바뀌었고, 2B에 FLUX.1-VAE를 적용한 비교 항목은 없습니다. | 의미를 담은 encoder면 아무것이나 되는지, 9B 큰 모델이라서인지는 일부만 확인됐습니다. SigLIP2 실험에서는 encoder와 함께 정렬 대상과 PSNR도 바뀌었고, 2B 백본에는 FLUX.1-VAE를 붙인 비교가 없습니다. | L3-3 |
| 16.notes.2 | 남은 설명은 둘입니다. LLM 조건만 줘도 AF가 FLUX.1-VAE보다 앞서므로, 이득의 일부는 VLM과 표현을 공유한 효과와 별개로 latent 자체에서 생길 수 있습니다. VLM을 붙였을 때 AF가 더 오르는 몫은 공유의 몫으로 볼 수 있습니다. 그리고 모든 비교가 50K step이라, 수렴이 빠른 것인지 최종 품질이 다른 것인지는 알 수 없습니다. 이 둘을 토론에서 다시 묻겠습니다. | 아직 답이 없는 질문은 둘입니다. 첫째, LLM이 조건을 줘도 AF가 FLUX.1-VAE보다 높습니다. 그러면 이득의 일부는 VLM과 같은 토큰을 써서가 아니라 AF latent 자체가 학습하기 쉬워서 생겼을 수 있습니다. VLM이 조건을 줄 때 AF가 더 오른 부분만 같은 토큰을 쓴 효과로 볼 수 있습니다. 둘째, 모든 비교가 50K step이라 AF가 빨리 배우는 것인지 끝까지 학습해도 더 좋은 것인지 알 수 없습니다. 이 두 질문은 토론에서 다시 묻겠습니다. | L3-3 |
| 19.message | Qwen3.5 계열을 사용한 짧은 학습에서 표현 공유의 이득을 확인했다. 생성 전용 0.89B 외에도 비용이 든다. | 비교 실험은 짧은 학습과 Qwen3.5 계열에서만 했고, 생성 전용 0.89B 외에도 비용이 든다. | L3-3 |
| 19.body.0.groups.0.items.0 | tokenizer 통제 비교는 256², 50K step, 주로 GenEval | tokenizer 비교 실험은 256², 50K step, 주로 GenEval | L1-8 |
| 19.body.0.groups.0.items.2 | $z$를 다음 턴 입력으로 바로 쓰면 손실이 없다는 이점(Sec. 2.2)은 측정하지 않음 | 생성한 $z$를 다음 턴 입력으로 바로 쓰면 디코딩·재인코딩 손실이 없다는 장점(Sec. 2.2)은 실험하지 않음 | L1-11 |
| 19.notes.0 | 한계는 세 가지로 정리했습니다. 먼저 검증 범위입니다. 통제 비교는 256 해상도에서 50K step까지, 주로 GenEval로 했고, 조건 VLM은 Qwen3.5 계열뿐입니다. z를 다음 턴에 바로 다시 쓰면 손실이 없다는 이점도 실험으로 재지 않았습니다. | 한계는 세 가지로 정리했습니다. 먼저 검증 범위입니다. 비교 실험은 256 해상도에서 50K step까지, 주로 GenEval로 했고, 실험한 VLM은 Qwen3.5 계열뿐입니다. 생성한 z를 다음 턴에 바로 다시 쓰면 손실이 없다는 장점도 실험으로 재지 않았습니다. | L1-8 |
| 20.message | 여러 비교 결과는 재구성 품질만으로는 생성 성능 차이를 설명할 수 없음을 뒷받침한다. 그 차이가 VLM과 표현을 공유한 데서 온다는 것은 저자 해석이다. | 재구성 품질만으로 GenEval 차이를 설명할 수 없다는 점은 여러 실험이 보여 준다. 그 차이가 VLM과 같은 토큰을 써서 생긴다는 것은 저자의 해석이다. | L3-3 |
| 20.body.0.groups.0.items.0 | 고정 encoder의 여러 층에서 나온 표현을 $z$ 하나로 모아 이해(99.8% 유지)와 재구성(32.2 dB)에 사용 | 고정 encoder의 여러 층 표현을 모은 토큰 $z$ 하나로 VLM 이해 성능을 99.8% 지키면서 이미지 재구성(32.2 dB)도 한다 | L3-3 |
| 20.body.0.groups.0.items.1 | 50K step 비교에서 재구성 품질로는 생성 차이가 설명되지 않는다 | 50K step 비교에서 AF 토큰으로 생성한 쪽의 GenEval이 높았고, 그 차이는 재구성 점수로 설명되지 않는다 | L3-3 |
| 20.body.0.groups.0.items.2 | 그 차이가 VLM과 표현을 공유한 데서 온다는 것은 저자 해석이다 | 그 차이가 VLM과 같은 토큰을 써서 생긴다는 것은 저자의 해석이다 | L3-3 |
| 20.body.0.groups.1.items.0 | LLM 조건만 줘도 AF가 FLUX.1-VAE보다 높다(Fig. 6b). 공유의 몫과 latent 자체의 몫을 어떻게 나눠 잴까? | 텍스트 전용 LLM이 조건을 줘도 AF가 FLUX.1-VAE보다 높았다(Fig. 6b). VLM과 같은 토큰을 쓴 효과와 AF latent 자체의 효과를 어떻게 따로 잴까? | L3-3 |
| 20.body.0.groups.1.items.1 | 통제 비교는 50K step(생성 600K 중)의 GenEval이다. 수렴이 빠른 것인가, 최종 품질이 다른 것인가? | 비교는 모두 생성 학습 50K step(전체 600K)에서, 주로 GenEval로 했다. AF가 빨리 배우는 것인가, 끝까지 학습해도 더 좋은가? | L3-3 |
| 20.body.0.groups.1.items.2 | $z$를 다음 턴에 다시 쓰는 이점과 propagation bottleneck은 측정·개입 실험이 없다. 무엇을 재면 될까? | 생성한 $z$를 다음 턴에 바로 쓰는 장점과 propagation bottleneck 가설은 실험으로 확인하지 않았다. 무엇을 재면 확인할 수 있을까? | L1-11 |
| 20.body.0.groups.1.items.3.text | 0.89B 밖의 비용(시각 경로, pixel decoder, VLM마다 tokenizer 재학습)을 넣어도 이득이 큰 조건은? | 생성 전용 0.89B 외에 VLM 이미지 입력 모듈 교체, pixel decoder, VLM을 바꿀 때마다 tokenizer 재학습이 든다. 이 비용을 감안해도 쓸 만한 경우는? | L3-3 |
| 20.notes.0 | 정리하겠습니다. Integral은 고정된 encoder의 여러 층에서 나온 표현을 z 하나로 모아 이해 성능을 거의 그대로 유지하면서 이미지도 재구성합니다. 50K step 비교들은 재구성 품질만으로는 생성 성능 차이가 설명되지 않는다는 점을 뒷받침합니다. 다만 그 차이가 VLM과 표현을 공유한 데서 온다는 것은 저자들의 해석입니다. | 정리하겠습니다. Integral은 고정된 encoder의 여러 층에서 나온 표현을 토큰 z 하나로 모아, VLM의 이해 성능을 거의 그대로 지키면서 이미지도 재구성합니다. 50K step 비교 실험에서는 AF 토큰으로 생성한 쪽의 GenEval이 높았고, 그 차이는 재구성 점수로 설명되지 않았습니다. 다만 그 차이가 VLM과 같은 토큰을 써서 생긴다는 것은 저자들의 해석입니다. | L3-3 |
| 20.notes.1 | 토론할 질문은 네 가지입니다. 첫째, VLM 조건 없이 LLM 조건만 준 AF도 FLUX.1-VAE보다 높았습니다. VLM과 표현을 공유한 효과와 latent 자체의 효과를 어떻게 구분해 측정할 수 있을까요? 둘째, 생성 통제 비교는 생성 1단계 설정의 50K step이고, 주로 GenEval로 쟀습니다. 수렴이 빠른 것인지 최종 품질이 다른 것인지 어떻게 가릴 수 있을까요? | 토론할 질문은 네 가지입니다. 첫째, VLM 대신 텍스트 전용 LLM이 조건을 줘도 AF가 FLUX.1-VAE보다 높았습니다. VLM과 같은 토큰을 쓴 효과와 AF latent 자체가 학습하기 쉬운 효과를 어떻게 따로 잴 수 있을까요? 둘째, 비교 실험은 생성 학습 50K step에서, 주로 GenEval로 했습니다. AF가 빨리 배우는 것인지, 끝까지 학습해도 더 좋은 것인지 어떻게 가릴 수 있을까요? | L3-3 |
| 20.notes.2 | 셋째, z를 다음 턴에 다시 쓰는 이점과 propagation bottleneck을 직접 측정한 실험은 없습니다. 무엇을 측정하면 확인할 수 있을까요? 넷째는 제 해석에서 나온 질문입니다. 생성 전용 0.89B 외에 시각 경로와 pixel decoder, VLM을 바꿀 때마다 하는 tokenizer 재학습에도 비용이 듭니다. 이 비용까지 고려해도 이득이 큰 조건은 무엇일까요? | 셋째, 생성한 z를 다음 턴에 바로 쓰는 장점과 propagation bottleneck 가설은 실험으로 확인하지 않았습니다. 무엇을 측정하면 확인할 수 있을까요? 넷째는 제 해석에서 나온 질문입니다. 생성 전용 0.89B 외에도 VLM의 이미지 입력 모듈을 바꾸고, pixel decoder를 따로 두고, VLM을 바꿀 때마다 tokenizer를 다시 학습해야 합니다. 이 비용을 감안해도 쓸 만한 경우는 언제일까요? | L3-3 |
| 21.notes.0 | 들어 주셔서 감사합니다. 특히 VLM과 표현을 공유한 효과와 latent 자체의 효과를 구분하려면 어떤 실험이 필요할지 의견을 듣고 싶습니다. | 들어 주셔서 감사합니다. 특히 VLM과 같은 토큰을 쓴 효과와 AF latent 자체의 효과를 가르려면 어떤 실험이 필요할지 의견을 듣고 싶습니다. | L3-3 |
