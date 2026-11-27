# 자료조사 확인 기록 (fk-steering)

agy 자료조사(`research.md`, 5–6번이 잘려 `research2.md`로 다시 받음)에서 덱에 쓸 만한 것만 원 출처를 열어 확인했다.
확인은 web-fetch 에이전트가 페이지를 열어 인용한 문구, 그리고 SMC 교재 PDF는 내려받은 파일을 직접 검색해서 했다.
이 파일에 있는 것만 슬라이드에 `external`로 쓴다.

| # | 사실 | 출처 | 확인 | 덱에서 |
|---|---|---|---|---|
| 1 | 학회: ICML 2025(제42회), PMLR 267:55810–55827 | https://proceedings.mlr.press/v267/singhal25b.html | 페이지 제목·저자·서지 문구 확인 | 표지 venue |
| 2 | arXiv 최신판 v5(2025-07-18). Comments 필드 없음(채택 표기는 arXiv에 없다) | https://arxiv.org/abs/2501.06848 | 확인 | 표지·ending 링크 |
| 3 | 코드 링크: arXiv 초록이 `github.com/zacharyhorvitz/Fk-Diffusion-Steering`, PMLR 페이지가 `.../FK-Diffusion-Steering`을 건다 | 위 두 페이지 | 링크 문구 확인. GitHub 페이지 자체는 504로 열리지 않아 라이선스는 확인 못 함 | ending 링크(라이선스는 말하지 않음) |
| 4 | 표준 adaptive resampling: "A common approach is to resample only at iterations when the ESS falls below N/2." ESS가 임계값보다 **크면** 재추출을 건너뛰고, 건너뛴 단계는 이전 가중치를 이어 받는 가중치 갱신(Eq. 2.21)을 쓴다 | Naesseth, Lindsten, Schön, *Elements of Sequential Monte Carlo*, §2.2.2, 31쪽 (arXiv 1903.04797) | PDF 본문 직접 확인 | 토론: App. C.3의 "ESS_t < k/2이면 건너뛴다"와 방향이 반대 |
| 5 | Chatterjee & Diaconis: 표본 크기가 대략 $\exp(D(\nu\|\mu))$이면 importance sampling의 정확한 추정에 필요충분하다 | https://arxiv.org/abs/1511.01437 (초록) | 초록 문장 확인 | 4번(배경) 대본: 논문이 인용하는 "많은 입자가 필요하다"의 근거 |
| 6 | 후속: *Controllable protein design with particle-based Feynman-Kac steering* (arXiv 2511.09216) — 초록 "The Feynman-Kac (FK) framework provides a principled way to guide diffusion models using user-defined rewards", RFdiffusion에 FK steering용 potential 개발 | https://arxiv.org/abs/2511.09216 | 초록 확인 | 정리 대본 한 줄(논문이 미래 방향으로 든 protein design과 연결), 선택 |
| 7 | 후속: *Discrete Feynman-Kac Correctors* (arXiv 2601.10403) — 학습된 이산 diffusion 모델에서 SMC로 온도 등을 제어 | https://arxiv.org/abs/2601.10403 | 초록 확인 | 쓰지 않음(덱 줄기와 거리) |

## 확인하지 못해 쓰지 않는 것
- TDS가 첫 단계 가중치에 twisting function을 넣는다는 agy의 답(Algorithm 1): 원문을 열지 않았다. 토론에서 Difference potential의 $G_T = 1$을 다룰 때 TDS와 비교하지 않고 논문 식만으로 말한다.
- SVDD의 후보 수·목표 분포의 세부: 초록 전문 미확인. 덱은 논문 App. C.2의 서술만 쓴다.
- *Generalized Feynman-Kac Correctors* (arXiv 2610.40383): 열지 않았다.
- 코드 저장소 라이선스: 확인 못 함.
