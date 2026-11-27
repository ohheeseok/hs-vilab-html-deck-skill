# 자료조사 확인 (`research.md`, agy) — 출처를 직접 연 것만

| # | 사실 | 출처 | 확인 / 다른 점 |
|---|---|---|---|
| 1 | arXiv Comments는 "Preprint. Project page: …"뿐. 학회 채택 표기 없음 | https://arxiv.org/abs/2611.31237 | 확인. 표지는 arXiv 2611.31237 (preprint) |
| 2 | 체크포인트 `the-jb/Integral-9B` 공개, 모델 카드 license: apache-2.0, base_model Qwen/Qwen3.5-9B, 코드 https://github.com/the-jb/integral | https://huggingface.co/the-jb/Integral-9B | 확인(모델 카드 원문). GitHub 저장소 주소는 응답 200으로 열림, README·라이선스는 보지 않음 → ending 링크에 코드 주소만 |
| 3 | Qwen3.5-9B config: vision depth 27, patch 16, hidden 1152, text num_hidden_layers 32 | https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/config.json | 확인. 논문 App. A.1과 같음. App. C.2의 "31 VLM layers"는 32층과 다르다(논문 안의 불일치, 덱에서는 쓰지 않음) |
| 4 | WISE-Verified(2026-04-19): 판정 모델이 **Qwen3.5-35B-A3B**(vLLM), 프롬프트 약 200개 갱신, WiScore를 0/1로 | https://github.com/PKU-YuanGroup/WISE (README) | 확인. Integral의 백본(Qwen3.5-9B)과 판정 모델이 같은 계열 → 토론점(external) |
| 5 | GenEval 2 초록: GenEval은 판정이 사람 판단에서 멀어져(benchmark drift) 최신 모델에서 절대 오차가 최대 17.7%, 포화된 지 오래라고 주장 | https://arxiv.org/abs/2512.16853 | 확인(초록). 통제 비교 지표가 GenEval 중심이라는 토론점의 외부 근거 |
| 6 | BAGEL: 14B 전체·7B 활성, MoT, FLUX VAE | https://arxiv.org/abs/2505.14683 | 초록에는 파라미터·VAE가 없다(본문 사항, 열지 않음) → 덱에서는 Integral 논문의 서술(§3.2, "FLUX.1-VAE, 약 7B 생성 전용")로만 귀속 |
| 7 | Kang et al.(arXiv 2607.04423), Harmon, PS-VAE, MoT(2411.04996) 한 줄 요약 | agy 보고 | 열지 않음 → 쓰지 않는다. 배경 슬라이드는 논문 §4의 서술로 |
