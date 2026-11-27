## Ledger

- Fig. 1 — use: 1, 5. 표지에는 오른쪽 FK steering 패널, 5번에는 가운데 best-of-\(n\)과 오른쪽 입자 계보를 바탕으로 만든 애니메이션.
- Fig. 2 — cut: 왼쪽은 최고 보상 입자의 GenEval 비교로 Table 1과 역할이 겹친다. 오른쪽은 `FLOPs (×10¹⁴)`라는 축 라벨과 로그 척도로 읽히는 점 간격이 달라 원도에서 계산량을 오독할 수 있다. 20번 대본에서 축 문제를 짚는다.
- Fig. 3 — use: 13. 주황색 소와 보라색 샌드위치 프롬프트 열의 세 행 전체.
- Fig. 4 — cut: 왼쪽·가운데의 입자 수별 평균 GenEval·ImageReward와 오른쪽의 ImageReward 분포. 입자 평균 비교는 potential을 바꾼 Table 5에 집중한다.
- Fig. 5 — use: 17. 이미지 ImageReward와 SSD-LM 독성 보상 상관 패널 모두.
- Table 1 — use: 13. SDv2.1과 SDXL 계열의 GenEval·ImageReward·HPS.
- Table 2 — cut: DPO로 fine-tuning한 모델에 FK를 추가한 실험. 대표 결과는 기본 모델에 FK를 적용한 비교에 집중한다.
- Table 3 — use: 15. SDv1.5의 gradient proposal 결과와 시간.
- Table 4 — use: 14. SSD-LM의 GPT2 보상과 MDLM의 Trigram 보상 결과.
- Table 5 — use: 16. 네 모델의 potential별 입자 평균 GenEval.
- Table 6 — use: 17. 기본 모델, best-of-\(n\), 중간 보상 변경의 독성 판정률과 perplexity.
- Table 7 — use: 18. ImageNet의 중간 보상·potential 비교, TDS 행 포함.
- Algorithm 1 — use: 8. 세 갱신 줄과 종단 반환.
- Fig. 6 — use: 19. Max에서 \(\lambda\)에 따른 다양성.
- Fig. 7 — use: 19. 같은 \(\lambda\)에서 Difference와 Max의 다양성.
- Fig. 8 — cut: *a photo of a frisbee above a truck*의 interval resampling 사례. 일정 비교는 Table 9로 다룬다.
- Fig. 9 — cut: 같은 프롬프트의 독립 표본과 FK 표본 비교. 프롬프트 충실도 사례는 Fig. 3으로 다룬다.
- Table 8 — use: 15. A100 1장과 2장 병렬 시간 발췌. 20번에서 시간 비교의 근거로 재인용.
- Table 9 — use: 19. 일정과 \(\lambda\)별 입자 평균 GenEval·CLIP-Div.
- Table 10 — use: 19. 입자 평균·최고 ImageReward와 CLIP-Div. 20번에서 potential 표기 대조에 재인용.
- Table 11 — cut: 학습한 독성 분류기의 gradient를 추가한 실험. Gradient proposal의 비용은 시간이 함께 보고된 Table 3에서 다룬다.

## Sections

- `summary` — 요약 (2)
- `background` — 배경 (3–5)
- `method` — 방법 (6–12)
- `results` — 결과 (13–14)
- `analysis` — 분석 (15–19)
- `discussion` — 정리와 토론 (20)

1920×1080 HTML 덱, 21장, 총 1,200초. 1·21장을 제외한 모든 슬라이드에 하단 진행 표시줄. 인터랙션은 5·9·19번 총 3장이고, 대표 인터랙션은 5번이다. `panel`은 사용하지 않는다.

## Slides

### 1. Diffusion 모델의 FK steering

- section: none
- time: 30초
- message: 이 발표에서는 diffusion 경로를 중간에 선택하는 절차가 어떻게 보상으로 기울인 분포를 근사하는지 살펴봅니다.
- on-slide facts: *A General Framework for Inference-time Scaling and Steering of Diffusion Models* · Singhal, Horvitz, Teehan 외 · VILAB 논문 세미나 · 발표자 `[이름]` · ICML 2025 · arXiv v5
- source: 논문 p. 1, Fig. 1 p. 2. External 서지 및 버전. [ICML 2025, PMLR 267](https://proceedings.mlr.press/v267/singhal25b.html) · [arXiv v5](https://arxiv.org/abs/2501.06848v5)
- block: `split` 55:45 · `lead`와 논문 정보 | `figure` Fig. 1 오른쪽 크롭
- assets: Fig. 1 오른쪽의 입자 계보와 범례
- interaction: none

### 2. FK steering 요약

- section: `summary`
- time: 60초
- message: FK steering은 생성 중간에 입자를 평가하고 재추출해 최종 보상으로 기울인 목표 분포를 근사합니다.
- on-slide facts:
  - 한 문장 요약: **FK steering은 diffusion 경로에 중간 보상을 반영해 높은 최종 보상을 얻을 경로에 계산을 더 배분한다.**
  - 기여 3개 · 연속·이산 diffusion과 비미분 보상을 포괄하는 FK 틀 · proposal, potential, 중간 보상의 선택과 TDS·SVDD의 관계 · 이미지·텍스트에서 표본 품질과 속성 제어 평가
- source: 초록, §1, pp. 1–4
- block: `statement` · `lead` 한 문장 + `cards` 기여 3개
- assets: none
- interaction: none

### 3. Diffusion steering의 연구 갈래

- section: `background`
- time: 50초
- message: 기존 방법은 보상을 학습에 반영할지, 추론 중 전이를 바꿀지, 여러 입자 중에서 선택할지로 갈립니다.
- on-slide facts:

  | 갈래 | 대표 방법 | 필요한 것 | 적용 조건 또는 비용 |
  |---|---|---|---|
  | Fine-tuning | DDPO, diffusion DPO, KL 정규화 fine-tuning | 보상·선호 데이터와 추가 학습 | 학습 비용, 특정 목적에 맞춘 모델 |
  | Gradient guidance | classifier guidance, universal guidance | 추론 중 보상 gradient | 연속 상태와 미분 가능한 보상 |
  | Particle | best-of-\(n\), TDS, SVDD | 여러 후보 생성과 선택 | best-of-\(n\)은 완성 후 선택, TDS는 classifier gradient 사용 |

  하단 발표 질문 · 목표 분포를 유지하면서 생성 중간의 어느 경로에 계산을 더 배분할 수 있는가?
- source: §§1–2, pp. 2–5
- block: `table` + 하단 `callout`
- assets: none
- interaction: none

### 4. 목표 분포와 Importance sampling

- section: `background`
- time: 70초
- message: 기본 모델에서 고보상 표본이 드물면 완성 후에만 선별하는 두 방식은 저보상 경로에도 생성 비용을 쓰므로 많은 후보가 필요합니다.
- on-slide facts:
  \[
  p_{\mathrm{target}}(x_0\mid c)
  =\frac{p_\theta(x_0\mid c)\exp(\lambda r(x_0,c))}{Z}.
  \tag{2}
  \]
  - Importance sampling · 독립 완성 표본 \(k\)개 · \(\exp(\lambda r)\)에 비례해 재추출
  - Best-of-\(n\) · 독립 완성 표본 \(n\)개 · 최고 보상 후보 선택
  - 공통 조건 · 생성 도중 보상에 따른 계산 재배분 없음
- source: §1 p. 2, §§3.1–3.3 pp. 5–7, Eqs. 1–2
- block: `split` 55:45 · `equation`과 기호 | `compare` 두 선택 규칙
- assets: Eq. 2
- interaction: none
- notes:
  - symbols: \(p_\theta\)는 기본 diffusion 모델, \(c\)는 프롬프트 등 조건, \(x_t\)는 역확산 시점 \(t\)의 상태. \(x_T\)는 시작 상태, \(x_0\)는 완성 표본, \(k\)는 입자 수, \(r\)은 최종 보상, \(\lambda\)는 기울임 강도, \(Z\)는 정규화 상수.
  - derivation: Eq. 2는 두 표본의 기본 확률비에 \(\exp(\lambda\Delta r)\)를 곱한다. 후보 집합을 고정하고 최고 보상 후보가 하나라고 하면, \(\lambda\to\infty\)에서 가중 선택 확률이 그 후보에 집중된다.
  - 설명용 가상 수치: 기본 모델에서 확률 1%인 사건에 보상 1, 나머지에 0을 주면 \(\lambda=10\)에서 목표 분포의 사건 확률은 약 99.55%다. 기본 모델에서 독립 표본 4개를 뽑았을 때 이 사건이 한 번이라도 나올 확률은 약 3.94%다.
  - External: Chatterjee와 Diaconis는 논문의 설정에서 importance sampling에 필요한 표본 규모를 대략 \(\exp(D(\nu\|\mu))\)로 제시한다. \(\nu\)는 목표분포, \(\mu\)는 표본을 뽑는 분포다. [Chatterjee & Diaconis](https://arxiv.org/abs/1511.01437)

### 5. FK steering의 입자 경로

- section: `background`
- time: 70초
- message: 중간에 부모를 재추출하면 일부 경로는 끝나고 선택된 부모의 복제본에서 새 경로가 갈라집니다.
- on-slide facts: Fig. 1의 *a green stop sign in a red field* · 생성 시작 → 완성 · 중간 보상 · 재추출 · Fig. 1을 바탕으로 재구성한 개념도, 재추출 시점 한 번으로 단순화
- source: Fig. 1 p. 2, §3.3 pp. 7–8, Algorithm 1 p. 7
- block: `animation` 전체 폭
- assets: Fig. 1 가운데와 오른쪽을 참조한 애니메이션용 입자 계보
- interaction: animation — **대표 인터랙션**
  - reveals: 독립 생성과 같은 출발점에서 어느 경로가 끝나고 어디서 새 경로가 갈라지는지 추적.
  - beats:
    0. **초기 화면** · best-of-\(n\)의 독립 경로를 시작부터 완성까지 표시. Fig. 1 가운데.
    1. **중간 평가** · 같은 경로의 한 중간 시점에 보상 표시가 생김. §3.3 p. 8.
    2. **재추출** · 예시에서 낮은 보상 경로가 끊기고 높은 보상 경로의 부모가 복제됨. Fig. 1 오른쪽, Algorithm 1의 Resample.
    3. **후속 경로 생성** · 복제된 부모에서 서로 다른 경로가 갈라져 완성까지 이어짐. Algorithm 1의 Propose.
  - 조작: 초기 화면에서 시작, 클리커 다음 키로 beat 1개씩 진행. 총 4개 정지점.
- notes:
  - symbols: 화면은 ‘중간 보상’과 ‘재추출’로 표시한다. 수식 기호는 6–8번에서 정의한다.
  - derivation: 그림의 복제와 탈락은 재추출 결과의 한 예다. Algorithm 1은 시작 상태에 점수를 매긴 뒤 첫 전이 전부터 재추출하고, 완성 상태의 가중치를 계산한 뒤 상태를 반환한다.

### 6. Feynman–Kac 경로 분포

- section: `method`
- time: 65초
- message: FK 경로 분포는 지금까지의 기본 경로 밀도에 potential을 곱하며, 새 시점에서는 한 단계 전이에 해당 potential을 붙입니다.
- on-slide facts:
  \[
  p_{\mathrm{FK},t}(x_{T:t}\mid c)
  =\frac{p_\theta(x_{T:t}\mid c)}{Z_t}
    \prod_{s=T}^{t}G_s(x_{T:s},c).
  \tag{3}
  \]
  \[
  p_{\mathrm{FK},t}(x_{T:t}\mid c)
  =\frac{Z_{t+1}}{Z_t}\,
    p_{\mathrm{FK},t+1}(x_{T:t+1}\mid c)
    \underbrace{p_\theta(x_t\mid x_{t+1},c)G_t(x_{T:t},c)}
    _{\text{potential로 기울인 전이}} .
  \tag{4}
  \]
- source: §3.3 p. 6, Eqs. 1, 3–4
- block: `equation` 2개와 기호 설명 · 전체 폭, 세로 중앙 정렬
- assets: Eqs. 3–4
- interaction: none
- notes:
  - symbols: \(x_{T:t}=(x_T,\ldots,x_t)\)는 현재까지의 경로, \(Z_t\)는 그 경로 분포의 정규화 상수, \(G_t\)는 현재까지의 경로를 참조하는 potential. 곱의 인덱스는 \(T\)에서 \(t\)로 감소한다.
  - derivation: 기본 경로 밀도에서 한 단계 전이를, 누적 곱에서 \(G_t\)를 분리한다. Eq. 3의 곱 안에 인쇄된 \(G_t\)는 첨자 \(G_s\)로 맞췄다. Eq. 4는 원문의 직전 비정규화 경로 밀도를 \(Z_{t+1}p_{\mathrm{FK},t+1}\)로 치환해 다시 적은 식이다. 괄호 아래 항은 전이에 곱하는 인수이고, 이 단계의 경로 분포 전체는 \(Z_t\)로 정규화한다.

### 7. Potential 곱과 목표 분포

- section: `method`
- time: 60초
- message: 경로별 potential의 곱을 최종 지수 보상과 맞추면 중간 상태를 주변화한 분포가 Eq. 2가 됩니다.
- on-slide facts:
  \[
  \prod_{t=T}^{0}G_t(x_{T:t},c)=\exp(\lambda r(x_0,c)).
  \tag{5}
  \]
  \[
  \int p_{\mathrm{FK},0}(x_{T:0}\mid c)\,dx_{T:1}
  =\frac{\exp(\lambda r(x_0,c))}{Z_0}\,p_\theta(x_0\mid c),
  \qquad Z_0=Z .
  \]
  - Eq. 5 대입 → 최종 보상 인수를 적분 밖으로 → 기본 모델의 \(x_0\) 주변분포
- source: §3.3 pp. 6–7, Eq. 5와 p. 7의 직후 설명
- block: `split` 66:34 · `equation` 2개 | `process` 3단계
- assets: Eq. 5, 주변화 유도식
- interaction: none
- notes:
  - symbols: \(x_{T:1}\)은 \(x_0\) 이전의 경로. 이산 상태에서는 적분을 합으로 바꾼다.
  - derivation: Eq. 5의 우변에는 \(x_0,c\)만 남으므로 중간 상태에 대한 적분 밖으로 뺄 수 있다. 위 적분과 \(Z_0=Z\)는 p. 7의 서술을 풀어 쓴 유도다. 이 단계가 보장하는 대상은 최종 FK 경로 분포의 주변분포다.

### 8. SMC 가중치와 Algorithm 1

- section: `method`
- time: 75초
- message: SMC는 proposal에서 뽑은 입자에 전이 확률비와 potential로 가중치를 매겨 각 FK 경로 분포를 근사합니다.
- on-slide facts:
  - Eq. 6의 비율 · 목표 경로 밀도 / 직전 FK 경로 밀도와 proposal의 곱
  \[
  G_t^i\propto
  \frac{p_\theta(x_t^i\mid x_{t+1}^i,c)}
       {\tau(x_t^i\mid x_{T:t+1}^i,c)}
  G_t(x_{T:t}^i,c).
  \tag{7}
  \]
  - **Resample** · \(G_t^i\)에 비례해 부모 인덱스 \(k\)개 재추출
  - **Propose** · 각 부모에서 \(\tau\)로 \(x_{t-1}^i\) 제안
  - **Re-weight** · 제안한 입자의 \(G_{t-1}^i\) 계산
  - 인쇄된 Algorithm 1의 종단 · \(G_0^i\) 계산 → \(t=0\) 재추출 없이 \(\{x_0^i\}\) 반환
  - 논문의 일관성 진술 · \(k\to\infty\)에서 최종 입자의 경험분포가 \(p_{\mathrm{target}}\)으로 수렴
- source: §3.3 p. 7, Eqs. 6–7, Algorithm 1, 논문이 인용한 Del Moral & Miclo (2000) 정리 3.19
- block: `split` 45:55 · `process` Algorithm 1의 세 줄과 반환 | `equation` Eq. 7 + `callout` 일관성
- assets: Algorithm 1 갱신 줄과 반환 줄, Eq. 7
- interaction: none
- notes:
  - symbols: \(i\)는 입자 번호, \(G_t\)는 경로의 potential, \(G_t^i\)는 입자 가중치, \(\tau\)는 실제로 상태를 제안하는 분포. 재추출 확률은 \(\widehat G_t^i=G_t^i/\sum_jG_t^j\).
  - derivation: Eq. 6은 \(p_{\mathrm{FK},t}(x_{T:t}^i\mid c)/[p_{\mathrm{FK},t+1}(x_{T:t+1}^i\mid c)\tau(x_t^i\mid x_{T:t+1}^i,c)]\)를 계산한다. Eq. 4를 대입하면 Eq. 7 오른쪽에 공통 인수 \(Z_{t+1}/Z_t\)가 붙는다. 따라서 화면의 Eq. 7은 원문의 등호를 \(\propto\)로 바꿨다. 알고리즘은 \(t\)의 가중치로 부모를 고르고 \(t-1\)의 가중치를 계산하는 순서다. 정리 인용과 인쇄된 반환 절차의 관계는 20번에서 다룬다.
  - 설명용 가상 수치: \(\tau=p_\theta\)일 때 네 입자의 \(G_t^i=(1,1,2,6)\)이면 확률은 \((0.1,0.1,0.2,0.6)\). 가능한 재추출 결과 \((4,3,4,4)\)에서는 4번 부모의 복제본 세 개가 각각 다음 상태를 제안한다.

### 9. Difference·Max·Sum potential

- section: `method`
- time: 70초
- message: 같은 보상 이력에서도 최근 증가량, 최고값, 누적값 중 무엇을 쓰느냐에 따라 재추출에 유리한 입자가 달라집니다.
- on-slide facts:
  \[
  \begin{aligned}
  G_t^{\mathrm{Diff}}&=\exp\!\left(\lambda[r_\phi(x_t,c)-r_\phi(x_{t+1},c)]\right), & G_T^{\mathrm{Diff}}&=1,\\
  G_t^{\mathrm{Max}}&=\exp\!\left(\lambda\max_{s=t,\ldots,T}r_\phi(x_s,c)\right),\\
  G_t^{\mathrm{Sum}}&=\exp\!\left(\lambda\sum_{s=t}^{T}r_\phi(x_s,c)\right).
  \end{aligned}
  \]
  \[
  G_0^{\mathrm{Max/Sum}}
  =\exp(\lambda r(x_0,c))\left(\prod_{t=1}^{T}G_t\right)^{-1}.
  \]
  - Difference 식은 \(0\le t<T\), Max·Sum의 이력 식은 \(1\le t\le T\). Difference의 Eq. 5 성립에는 최종 보상과 초기 경계 항 확인 필요.
  - 설명용 가상 보상 이력, 역확산 진행 순서 · A \((0,.2,.8)\) · B \((.9,.1,.2)\) · C \((.6,.6,.6)\)
- source: §3.3 pp. 7–8, *Choosing the potential*, Eq. 5
- block: `split` 56:44 · `equation` 세 potential과 종단 보정 | `toggle` 보상 이력 SVG
- assets: potential 식 3개, \(G_0\) 식, 설명용 가상 궤적 SVG
- interaction: toggle — reveals: 동일한 보상 이력에서 potential만 바꿨을 때 재추출 가중치가 가장 큰 입자의 변경.
  - states: `1` Difference · A의 \(0.6\) 증가량 / `2` Max · B의 \(0.9\) 최고값 / `3` Sum · C의 \(1.8\) 누적값
  - 조작: 숫자 키 또는 화면 버튼으로 상태 선택. 클리커 다음 키는 다음 슬라이드로 이동. `print: expand`
- notes:
  - symbols: \(r_\phi(x_t,c)\)는 중간 상태의 보상 추정치, \(s\)는 이미 지난 역확산 시점, \(G_0\)는 종단 potential.
  - derivation: 설명용 가상 수치에서 \(\lambda=1,\ \tau=p_\theta\)를 두면 A·B·C의 비정규화 가중치는 Difference \((1.82,1.11,1.00)\), Max \((2.23,2.46,1.82)\), Sum \((2.72,3.32,6.05)\). 가령 A의 세 중간 시점을 모두 사용한 Max의 곱은 \(e^{0+.2+.8}=e^1\)이다. 가상의 최종 보상 \(r(x_0,c)=.8\)이면 \(G_0=e^{-.2}\)이고 전체 곱은 \(e^{.8}\)이다. Difference에서는 인접 보상 항이 상쇄되고 시작 상태의 항이 남는다. 이 경계와 종단 보정의 사용 여부는 20번에서 연결한다.

### 10. Interval resampling과 ESS

- section: `method`
- time: 50초
- message: Interval resampling은 개입할 시점을 미리 정하고, adaptive resampling은 가중치가 얼마나 집중됐는지 보여 주는 ESS로 판단합니다.
- on-slide facts:
  - Algorithm 1 · \(t=T,\ldots,1\)에서 매 단계 재추출
  - Interval · \(0\in\mathcal R\), \(t\notin\mathcal R\)이면 \(G_t=1\) 및 재추출 생략
  - §4.1 이미지 설정 · \(T=100\), 일정 \([0,20,40,60,80]\) · 역확산 순서 \(80\to60\to40\to20\to0\) · \(0\)은 일정의 종단 표기
  \[
  \mathrm{ESS}_t=\frac{1}{\sum_{i=1}^{k}(\widehat G_t^i)^2}\in[1,k].
  \tag{13}
  \]
  - App. C.3 인쇄 규칙 · \(\mathrm{ESS}_t<k/2\)에서 재추출 생략
- source: Algorithm 1 p. 7, §3.3 *Interval Resampling* p. 8, §4.1 p. 9, App. C.3 p. 24, Eq. 13
- block: `split` 55:45 · `diagram` 100-step 시간축과 일정 | `equation` ESS와 인쇄 규칙
- assets: 시간축 SVG, Eq. 13
- interaction: none
- notes:
  - symbols: \(\mathcal R\)은 일정에 지정된 시점 집합, \(\widehat G_t^i\)는 합이 1인 가중치, \(k\)는 입자 수.
  - derivation: 가중치가 균등하면 ESS는 \(k\), 한 입자에 몰리면 1에 가까워진다. 설명용 가상 수치로 \(k=4\), 가중치 \((.05,.05,.10,.80)\)이면 \(\mathrm{ESS}=1/.655\approx1.53<2\). 이 경우 App. C.3에 인쇄된 규칙은 재추출 생략이다. 20번에서 표준 교재의 규칙과 대조한다.

### 11. 중간 보상을 얻는 세 방법

- section: `method`
- time: 60초
- message: 중간 보상은 denoised estimate를 평가하거나, 여러 완성 후보를 평가하거나, 중간 상태에서 최종 속성을 예측하도록 학습해 얻습니다.
- on-slide facts:
  - Denoised estimate · \(r_\phi(x_t,c)=r(\hat x_t,c)\)
  - Many-sample · \(x_0^j\sim p_\theta(x_0\mid x_t,c)\)를 \(N\)개 생성 · \(r_\phi=\log[\frac1N\sum_j\exp(r(x_0^j,c))]\)
  - Learned · 속성 분류기 \(p_\phi(y\mid x_t)\) 또는 일반 보상 회귀 후 \(r_\phi=\log a_\phi\)
  \[
  \arg\min_\phi
  \mathbb E_{t\sim U[0,T]}
  \mathbb E_{\substack{x_0\sim q_{\mathrm{data}}(\cdot\mid c)\\x_t\sim q(\cdot\mid x_0)}}
  \left\|a_\phi(x_t,c)-\exp(r(x_0,c))\right\|_2^2.
  \tag{8}
  \]
  - SSD-LM 실제 학습 · RoBERTa가 분류한 OpenWebText 비독성 26K·독성 26K · noising 후 \(\hat x_t\) 변환 · 시간 구간 3개에 분류기 fine-tuning, cross-entropy
- source: §3.3 *Choosing intermediate rewards* p. 8, Eq. 8과 논문이 인용한 Chopin et al. 정리 10.1, §4.3 pp. 13–15, App. B.2 pp. 22–23
- block: `cards` 3개 + 아래 `equation` Eq. 8
- assets: Eq. 8, many-sample 식
- interaction: none
- notes:
  - symbols: \(\hat x_t\)는 현재 상태에서 얻는 완성 표본 추정치, \(N\)은 입자당 평가 후보 수, \(y\)는 목표 속성, \(q\)는 forward noising, \(a_\phi\)는 지수 보상의 예측값.
  - derivation: 제곱오차의 최적 예측값은 조건부 평균이다. 논문의 \(p_\theta=q\) 가정에서 \(r_\phi\)는 \(\log\mathbb E_{p_\theta}[\exp(r)\mid x_t,c]\)가 된다. 논문은 이 선택에서 얻는 potential과 국소 전이의 단계별 potential 분산 최소화를 Chopin et al. 정리 10.1에 연결한다. Eq. 8의 표적은 \(\exp(r)\)로, \(\exp(\lambda r)\)의 \(\lambda=1\) 형태다. SSD-LM과 ImageNet의 learned 실험은 속성 분류기를 사용했다.

### 12. IS·TDS·SVDD의 FK 구성

- section: `method`
- time: 55초
- message: Importance sampling, TDS, SVDD는 FK에서 어떤 potential과 proposal을 사용하고 언제 후보를 선택하는지로 비교할 수 있습니다.
- on-slide facts:

  | 방법 | Potential | Proposal | 선택 방식 | 적용 범위 |
  |---|---|---|---|---|
  | Importance sampling | \(G_{t\ge1}=1,\ G_0=e^{\lambda r}\) | 기본 전이 | 완성 후보를 최종 가중치로 재추출 | 최종 보상 평가 가능 |
  | TDS | Denoised estimate의 Difference | classifier guidance | SMC | 연속 상태, 미분 가능한 클래스 보상 |
  | SVDD | Difference, 기존 또는 학습한 중간 보상 | 기본 전이 | Nested importance sampling으로 단계마다 하나 선택 후 복제 | 연속·이산, 비미분 보상 |
  | 논문의 이미지 품질 실험 | ImageReward, denoised estimate, Max | 기본 전이 | Interval resampling, Table 1은 최고 보상 입자 보고 | 조건부 Stable Diffusion |

  SVDD의 \(\lambda\to\infty\) · 단계별 best-of-\(n\).
- source: §2 p. 5, §3.3 p. 7, §4.1 pp. 9–10, Apps. C.1–C.2 pp. 23–24, Eqs. 11–12
- block: `table` 전체 폭 · 네 방법과 네 비교 항목
- assets: 논문 절차를 대조한 표
- interaction: none
- notes:
  - symbols: \(\tau=p_\theta\)는 기본 전이를 그대로 proposal로 쓰는 경우. \(n\)은 단계별 best-of-\(n\)의 후보 수 표기.
  - derivation: \(\tau=p_\theta\)이면 Eq. 7의 전이 확률비는 1이다. IS의 FK 표현에서는 중간 potential이 모두 1이고 최종 가중치로 선택한다. SVDD는 같은 부모의 자식들을 비교하므로 Difference의 부모 보상 항이 공통이다. \(\lambda\)를 키우면 후보 선택이 최고 중간 보상에 집중된다.
  - Eq. 11: App. C.1의 이산 proposal은 \(\tau(x_t\mid x_{T:t+1},c)=p_\theta(x_t\mid x_{t+1},c)G_t(x_{T:t},c)/\sum_u p_\theta(u\mid x_{t+1},c)G_t(x_{T:t+1},u,c)\)로 쓸 수 있다. 분모는 가능한 다음 상태 \(u\)에 대한 정규화 합이다. 여기서 소개하는 논문 실험의 MDLM proposal은 기본 전이다.

### 13. 이미지 품질과 프롬프트 충실도

- section: `results`
- time: 55초
- message: ImageReward로 steering한 SDv2.1의 최고 보상 입자는 이 비교에서 SDXL-DPO보다 GenEval이 높았고, HPS의 순서는 반대였습니다.
- on-slide facts:

  | 모델·sampler | GenEval | ImageReward | HPS |
  |---|---:|---:|---:|
  | SDv2.1 기본 \(k=1\) | 0.5104 | 0.372 | 0.253 |
  | SDv2.1 BoN \(k=4\) | 0.6172 | 0.888 | 0.263 |
  | SDv2.1 FK \(k=3\) | 0.5987 | 0.864 | 0.265 |
  | SDv2.1 FK \(k=4\) | 0.6289 | 1.006 | 0.268 |
  | SDXL 기본 \(k=1\) | 0.5571 | 0.871 | 0.289 |
  | SDXL-DPO \(k=1\) | 0.5811 | 0.859 | 0.296 |

  - SDv2.1 FK \(k=4\)의 GenEval Δ · SDXL-DPO 대비 **+0.0478**, 같은 모델 BoN \(k=4\) 대비 +0.0117.
  - FK 행 · 최고 ImageReward 입자, \(\lambda=10\), Max, 기본 proposal, \([0,20,40,60,80]\), DDIM \(\eta=1,\ T=100\), CFG 7.5. GenEval과 ImageReward·HPS는 별도 프롬프트 세트.
  - Fig. 3 · *a photo of an orange cow and a purple sandwich* · SDXL 독립 표본은 두 색 지정 실패, SDXL FK는 소의 색 구현, SDv2.1 FK는 두 색 구현. FK 두 행은 \(k=4\) 최고 보상 표본.
- source: §4.1 pp. 9–10, Table 1, Fig. 3 p. 4
- block: `split` 60:40 · `table`과 GenEval Δ | `figureNumbered` Fig. 3 한 열의 세 행
- assets: Table 1 여섯 행, Fig. 3 두 번째 프롬프트 열의 세 행 전체
- interaction: none
- notes: SDv2.1 FK \(k=3\)의 GenEval은 SDXL-DPO보다 높고 같은 모델 BoN \(k=4\)보다 낮다. §4.1의 미적 품질 설명은 지표별로 읽는다. SDv2.1 FK의 ImageReward는 높고 HPS는 SDXL 기본과 SDXL-DPO보다 낮다. 이 슬라이드는 유한 \(k\)에서 최고 입자를 고른 결과이며, 16번에서는 입자 전체의 평균을 비교한다.

### 14. 텍스트 품질: PPL·CoLA·Dist

- section: `results`
- time: 45초
- message: 연속 SSD-LM과 이산 MDLM에서 FK는 같은 보상의 best-of-\(n\)보다 낮은 perplexity를 기록했고, distinct n-gram은 일부 줄었습니다.
- on-slide facts:

  | 모델·sampler | GPT2-XL PPL ↓ | CoLA ↑ | Dist-1/2/3 |
  |---|---:|---:|---|
  | SSD-LM 기본 \(k=1\) | 23.2 | 68.3 | 46/83/92 |
  | SSD-LM BoN(GPT2), \(n=4\) | 13.6 | 75.6 | 42/77/88 |
  | SSD-LM FK(GPT2), \(k=4\) | 11.0 | 80.0 | 40/73/86 |
  | MDLM 기본 \(k=1\) | 85.3 | 28.9 | 57/91/94 |
  | MDLM BoN(Trigram), \(n=4\) | 52.1 | 30.1 | 53/89/93 |
  | MDLM FK(Trigram), \(k=4\) | 40.3 | 37.0 | 50/87/93 |

  - 같은 보상의 BoN 대비 GPT2-XL PPL Δ · SSD-LM **−2.6** · MDLM **−11.8**
  - FK · \(\lambda=10\), Difference, 기본 proposal, 재추출 50회 · SSD-LM 10 step마다, MDLM 20 step마다 · 각 실행의 최고 점수 표본 · 프롬프트 15개당 길이 50의 continuation 20개, 3 seeds 평균
- source: §4.1 pp. 11–13, Table 4, Apps. B.1–B.2 pp. 21–22
- block: `table` 전체 폭, 모델별 행 묶음 + `deltas` PPL 2개
- assets: Table 4 여섯 행
- interaction: none
- notes: GPT2 보상과 GPT2-XL PPL 평가의 표기를 구분한다. CoLA도 논문의 다른 행에서는 보상으로 사용한다. MDLM의 이산 상태와 비미분 Trigram 보상은 기본 proposal로 steering한 사례다. MDLM 기본→FK(Trigram)의 PPL은 Table 4에서 `85.3 → 40.3`, §4.1 본문에서 `79.2 → 37.2`다. CoLA도 각각 `28.9 → 37.0`, `30.0 → 35.3`으로 다르다. 화면에는 Table 4를 사용한다.

### 15. Gradient proposal의 비용

- section: `analysis`
- time: 50초
- message: SDv1.5에서 ImageReward gradient를 FK proposal에 추가한 행은 품질 지표가 더 높고 보고된 샘플링 시간도 더 깁니다.
- on-slide facts:
  - **Table 3 · SDv1.5, ImageReward**

    | Sampler | GenEval | IR | HPS | 시간 |
    |---|---:|---:|---:|---:|
    | 기본 \(k=1\) | 0.44 | 0.187 | 0.245 | 2.4초 |
    | Gradient guidance \(k=1\) | 0.45 | 0.668 | 0.245 | 20초 |
    | FK \(k=4\) | 0.54 | 0.898 | 0.263 | 8.1초 |
    | FK + gradient \(k=4\) | 0.56 | 1.290 | 0.268 | 55초 |

    FK 두 행의 Δ · GenEval **+0.02** · 보고 시간 **+46.9초**.
  - **Table 8 · gradient 없는 설정의 시간 발췌**

    | 모델 | 기본 \(k=1\), A100 1장 | FK \(k=4\), A100 1장 | FK \(k=4\), A100 2장 |
    |---|---:|---:|---:|
    | SDv1.4/v1.5 | 2.4초 | 8.1초 | 5.0초 |
    | SDv2.1 | 4.6초 | 17.4초 | 9.1초 |
    | SDXL | 11.5초 | 43.5초 | 21.7초 |

  \[
  \tau=\mathcal N\!\left(
  \mu_\theta(x_t,c)+\sigma_\theta^2\lambda\nabla_{x_t}r_\phi(x_t,c),
  \ \sigma_\theta^2 I_d
  \right).
  \tag{10}
  \]
- source: §4.1 pp. 9–11, Tables 1, 3, 8, App. C.1 p. 23, Eq. 10
- block: `split` 62:38 · `table` 두 발췌 | `equation` Eq. 10과 FK 두 행의 Δ
- assets: Table 3, Table 8 시간 발췌, Eq. 10
- interaction: none
- notes:
  - symbols: \(\mu_\theta,\sigma_\theta^2 I_d\)는 기본 Gaussian 전이의 평균·공분산, \(d\)는 상태 차원, \(r_\phi\)는 중간 보상.
  - derivation: Eq. 10은 공분산을 유지하며 평균을 보상 gradient 방향으로 이동시킨다. Eq. 7의 전이 비율이 proposal 변경을 보정한다. 원문의 평균 인자와 gradient 평가점 \(x_t\)를 유지하고 공분산에 \(I_d\)를 보완했다. 인쇄된 gradient 평가점은 다음 상태의 제안식이라는 설명과 첨자가 겹치므로 이 식에서 구현의 평가점을 단정하지 않는다.
  - Table 3의 기본·FK GenEval `0.44 / 0.54`는 Table 1의 `0.4483 / 0.5463`을 소수 둘째 자리까지 절사한 값과 일치한다. `2.4 / 8.1초`는 Table 8의 단일 A100과, FK `IR / HPS`는 Table 1 최고 입자와 일치해 두 대조 행의 조건을 추정할 수 있다. §4.1 기본 FK 설정의 \(\lambda\)는 10이며, Table 3은 gradient 행의 별도 \(\lambda\), GPU 조건 및 입자 집계를 명시하지 않는다.

### 16. Potential별 입자 평균 GenEval

- section: `analysis`
- time: 45초
- message: ImageReward와 재추출 일정을 고정한 실험에서 Max는 네 모델과 두 입자 수 모두에서 입자 평균 GenEval이 가장 높았습니다.
- on-slide facts:
  - 모델 순서 · `SDv1.4 / SDv1.5 / SDv2.1 / SDXL` · ImageReward, \(\lambda=10\), 일정 \([0,20,40,60,80]\) · GenEval **전체 입자 평균**
  - \(k=4\) · Max `0.540 / 0.540 / 0.616 / 0.633` · Difference `0.525 / 0.526 / 0.578 / 0.603` · Sum `0.496 / 0.499 / 0.569 / 0.613`
  - \(k=8\) · Max `0.569 / 0.561 / 0.635 / 0.648` · Difference `0.566 / 0.553 / 0.615 / 0.640` · Sum `0.532 / 0.517 / 0.588 / 0.634`
  - SDv2.1의 Max–Difference Δ · \(k=4\) +0.038, \(k=8\) +0.020
- source: §4.2 pp. 12, 14, Table 5
- block: `bars` 두 패널 · \(k=4\)와 \(k=8\), 공통 축·범례, Max 강조
- assets: Table 5 수치로 그린 그룹 막대그래프
- interaction: none
- notes: ImageReward 범위는 \([-2,2]\)다. 논문은 초기에 상한에 도달한 입자가 이후 보상을 더 높이지 못해 Difference에서 낮은 점수를 받을 수 있다고 설명한다. Table 5의 관측값으로 종단 \(G_0\) 사용 여부나 그 효과까지 식별할 수는 없다. 다양성은 19번의 별도 조건에서 비교한다.

### 17. 텍스트 독성과 중간 보상의 질

- section: `analysis`
- time: 55초
- message: 이 독성 제어 실험에서 중간 보상을 학습하거나 평가 후보를 늘리자 holdout 분류기의 판정률과 perplexity가 함께 올랐습니다.
- on-slide facts:
  - Fig. 5 왼쪽 · SDv1.4·SDv2.1·SDXL-base, denoised estimate의 ImageReward와 최종 ImageReward 상관 · 역확산 초반부터 상관이 나타나는 곡선.
  - Fig. 5 오른쪽 · SSD-LM의 denoised estimate 평가와 learned 보상 · 생성 진행에 따른 최종 독성 보상과의 상관, 곡선으로 비교.
  - Table 6 · FK는 \(\lambda=10\), Difference, 기본 proposal, 아래 FK 행 \(k=8\) · 3 seeds 평균.

    | 모델·sampler | Steering RoBERTa | Holdout XLM-R | GPT2-XL PPL |
    |---|---:|---:|---:|
    | SSD-LM 기본 | 0.4% | 1.2% | 23.2 |
    | SSD-LM BoN(8) | 5.0% | 8.1% | 23.0 |
    | SSD-LM FK, denoised | 25.0% | 29.7% | 23.9 |
    | SSD-LM FK, learned | 39.0% | 38.0% | 26.9 |
    | MDLM 기본 | 0.3% | 1.9% | 85.3 |
    | MDLM BoN(8) | 3.7% | 10.8% | 84.6 |
    | MDLM FK, \(N=4\) | 53.4% | 48.3% | 74.3 |
    | MDLM FK, \(N=16\) | 64.7% | 51.7% | 82.9 |

- source: §4.3 pp. 13–15, Table 6, Fig. 5, App. B.2 pp. 21–23
- block: `split` 45:55 · `figure` Fig. 5 두 패널, 축과 범례 유지 | `table` Table 6 발췌
- assets: Fig. 5 양쪽 패널, Table 6 여덟 행
- interaction: none
- notes: Fig. 5는 곡선에 근거해 설명한다. SSD-LM의 holdout Δ는 +8.3%p, MDLM의 \(N=4\to16\) holdout Δ는 +3.4%p다. MDLM 중간 보상은 §4.3에서 \(p_\theta(x_0\mid x_t)\) 표본의 log-mean-exp, App. B.2에서 \(\hat x_t\)의 다항분포로 채운 텍스트 보상의 평균으로 서술된다. 두 기술이 같은 구현을 가리키는지는 확인 필요. §4.3의 ‘learned reward’ 22.3%는 Table 6의 SSD-LM gradient guidance 행과 일치한다. Table 6의 learned \(r_\phi\) 행은 조향에 사용한 RoBERTa 기준 \(k=4\)에서 15.2%, \(k=8\)에서 39.0%다.

### 18. ImageNet의 중간 보상과 potential

- section: `analysis`
- time: 45초
- message: ImageNet에서는 학습한 중간 분류기를 potential과 gradient proposal에 함께 쓴 두 행이 같은 potential의 denoised 평가 행보다 높은 목표 클래스 확률을 기록했습니다.
- on-slide facts:
  - ImageNet 1,000 클래스 · marginal diffusion · \(256\times256\) · \(k=4\) · gradient proposal · 목표 클래스 log-probability 보상. 이 비교의 \(\lambda\)는 Table 7과 해당 실험 설명에 미기재.

    | Sampler | 중간 보상 | Potential | 목표 클래스 확률 평균 | 최댓값 |
    |---|---|---|---:|---:|
    | TDS | Denoised estimate | Difference | 0.59 | 0.72 |
    | FK steering | Denoised estimate | Max | 0.65 | 0.70 |
    | FK steering | Noisy state에서 학습 | Difference | 0.88 | 0.94 |
    | FK steering | Noisy state에서 학습 | Max | 0.88 | 0.96 |

  - 같은 potential 내 목표 클래스 평균 확률 Δ · Difference **+0.29**, Max **+0.23**.
- source: §4.3 pp. 14–15, Table 7, App. C.2 p. 24
- block: `table` 전체 폭 + `deltas` 평균 확률 2개
- assets: Table 7 네 행
- interaction: none
- notes: 평가는 논문이 보고한 단일 분류기의 목표 클래스 확률이다. 별도 holdout 분류기나 FID는 Table 7에 없다. Learned 분류기는 potential과 proposal 양쪽에서 교체됐으므로 +0.29와 +0.23은 결합 변경의 차이다. Denoised 행끼리 비교하면 Max에서 평균은 +0.06, 최댓값은 −0.02다.

### 19. \(\lambda\)·potential과 입자 다양성

- section: `analysis`
- time: 55초
- message: Appendix의 이미지 실험에서는 보상과 선택을 강하게 적용한 행에서 다양성이 줄었으며, 점수의 변화는 \(\lambda\), 일정, 집계 방식에 따라 달랐습니다.
- on-slide facts:
  - **Table 9** · SDv1.4, \(k=4\), GenEval 프롬프트, ImageReward 보상, App. A의 Difference 설정.

    | 설정 | 입자 평균 GenEval | CLIP-Div |
    |---|---:|---:|
    | 독립 표본 | 0.4408 | 0.3158 |
    | \(\lambda=10\), `5-30-5` | 0.4814 | 0.1437 |
    | \(\lambda=10\), `20-80-20` | 0.5258 | 0.1050 |
    | \(\lambda=2\), `20-80-20` | 0.4910 | 0.2239 |

  - **Table 10** · SDv1.4, \(k=4\), ImageReward 프롬프트와 보상. App. A는 Difference로 표기.

    | 설정 | 평균 IR | 최고 IR | CLIP-Div |
    |---|---:|---:|---:|
    | 독립 표본 | 0.234 | 0.800 | 0.348 |
    | \(\lambda=1\), `20-80-20` | 0.502 | 0.763 | 0.173 |
    | \(\lambda=10\), `20-80-20` | 0.811 | 0.927 | 0.091 |

  - Fig. 6·7 공통 · *a green stop sign in a red field* · SDXL-base, 기본 proposal, ImageReward, App. C.3의 adaptive resampling 적용으로 보고.
  - 적용 한계 · 원하는 속성을 잘 평가하는 보상 함수의 가용성.
- source: §4.2 p. 12, §5 p. 16, App. A pp. 21–22, Eq. 9, Tables 9–10, Apps. C.3–D pp. 24–27, Figs. 6–7
- block: 전체 폭 `toggle` 이미지 영역 + 하단 `split` 50:50의 `table` 2개
- assets: Fig. 6의 독립 기준·\(\lambda=2,10\) 행, Fig. 7의 Difference·Max 행, Tables 9–10 발췌
- interaction: toggle — reveals: 같은 프롬프트의 표본을 큰 크기로 보며, 보상 강도를 바꾼 경우와 potential을 바꾼 경우의 구도 반복을 각각 확인.
  - states: `1` Fig. 6 · Max, \(k=4\), 독립 기준과 \(\lambda=2,10\)의 구도 차이 / `2` Fig. 7 · \(k=8,\lambda=2\), 같은 step 조건의 Difference·Max에서 구도 반복 비교.
  - 조작: 숫자 키 또는 화면 버튼. 클리커 다음 키는 다음 슬라이드로 이동. `print: expand`
- notes:
  - symbols: CLIP-Div는 입자 쌍의 CLIP 임베딩 제곱거리 평균이다. Table 10의 ‘최고 IR’은 각 후보 집합에서 최고 보상 입자를 기준으로 한 보고값이다.
  - derivation: Table 9의 일정 이름은 인쇄 표기를 유지한다. `5-30-5`·`20-80-20`의 App. A 본문 일정 대응은 확인 필요. 같은 `5-30-5`의 SDv2.1은 \(\lambda=2\)의 GenEval 0.5607이 \(\lambda=10\)의 0.5523보다 높다. Table 10의 SDv2.1도 `20-80-20`, \(\lambda=1\)에서 평균 IR은 `0.372 → 0.579`, 최고 IR은 `0.888 → 0.826`이다.
  - App. A는 Difference라고 적는다. Table 10의 \(\lambda=10\), `20-80-20` 최고 IR `0.927 / 1.006 / 1.298`은 SDv1.4·SDv2.1·SDXL 순으로 Table 1의 Max 결과와 같고, 최고 HPS 수치는 다르다. Table 10 해당 행의 실제 potential은 확인 필요.

### 20. 정리와 토론

- section: `discussion`
- time: 120초
- message: FK의 곱 조건은 목표 분포를 정해 주며, 유한한 입자로 얻은 실험 결과는 반환 규칙과 평가 지표와 계산 조건을 함께 봐야 해석할 수 있습니다.
- on-slide facts:
  - **정리 3개** · Eq. 5의 경로별 곱과 Eq. 2의 최종 주변분포 · SMC의 재추출·제안·가중치 보정 · 유한 \(k\)에서 proposal·potential·중간 보상의 선택과 품질·비용·다양성
  - **근거 1 · 시간 비교** — §4.1의 `11.5초 / 9.1초` · SDXL 기본 \(k=1\), A100 1장 `11.5초` · SDv2.1 FK \(k=4\), A100 2장 병렬 `9.1초`, 1장 `17.4초`.
  - **근거 2 · 보고 표본과 평가 지표** — Table 1의 최고 ImageReward 입자와 동일 보상 모델로 평가한 IR · HPS는 SDv2.1 FK `0.268`, SDXL-DPO `0.296` · Table 10의 최고 IR 일치와 App. A의 Difference 표기.
  - **근거 3 · 인쇄된 절차와 Eq. 5, 해석** — Difference의 \(G_T=1\)과 남는 초기 보상 항 · Algorithm 1의 \(G_0^i\) 계산 후 상태 반환 · App. C.3의 저ESS 재추출 생략과 교재의 저ESS 재추출.
  - **대가 4 · 계산 배분, 해석** — 입자 \(k\), 입자당 평가 후보 \(N\), learned 분류기 학습 · 재추출 시 병렬 입자의 동기화 · 동일 계산 예산 비교 미보고.
- source: §3.3 pp. 6–8, Eq. 5, Algorithm 1, §4.1 p. 10, Tables 1, 8, 10, §4.3 p. 15, Apps. A, B.2, C.3, D. External 비교 기준. [Naesseth et al., *Elements of Sequential Monte Carlo*, §2.2.2 p. 31](https://arxiv.org/abs/1903.04797)
- block: `statement` · `lead` 정리 3줄 + `cards` 토론 4개
- assets: Eq. 5, Algorithm 1 반환 줄, Tables 1·8·10의 근거 셀 참조
- interaction: none
- notes:
  - symbols: \(G_T\)는 시작 potential, \(G_0\)는 종단 potential, \(k\)는 입자 수, \(N\)은 입자당 중간 보상 평가 후보 수. Naesseth et al.의 \(N\)은 교재에서의 전체 입자 수다.
  - derivation: Difference를 인쇄된 대로 곱하고 \(r_\phi(x_0,c)=r(x_0,c)\)로 두면 \(\exp(\lambda[r(x_0,c)-r_\phi(x_T,c)])\)가 남는다. 초기 항이 0이면 Eq. 5와 일치한다. 초기 항이 경로에 무관한 상수라면 정규화에서 상쇄될 수 있다. 인쇄된 Algorithm 1은 \(G_0^i\)로 최종 상태를 다시 재추출하거나 그 가중치를 함께 반환하는 줄이 없어, Max·Sum 보정이 인쇄된 출력 선택에 어떻게 반영되는지 확인할 수 없다. External 교재는 ESS가 \(N/2\)보다 낮을 때 재추출하고, 임계값 위에서 건너뛴 단계는 이전 가중치를 이어 받는다. App. C.3의 인쇄 방향은 반대이며 실제 실험에 쓰인 부등호와 가중치 갱신은 확인 필요. [Naesseth et al., §2.2.2, Eq. 2.21](https://arxiv.org/abs/1903.04797)
  - 진행 메모 · 정리 20초, 토론점 소개 100초.
    1. A100 수를 같게 두면 속도 비교의 결론이 어떻게 달라지는가? Fig. 2 오른쪽의 두 배 계산량에 해당하는 점 간격 약 0.30은 \(\log_{10}2\)와 맞는다. 인쇄 축 라벨만으로 FLOPs 비율을 읽기 어렵다.
    2. 목표 분포의 근사와 최고 보상 표본의 개선을 각각 어떤 통계로 측정할 수 있는가? 최고 IR의 일치만으로 Table 10의 potential을 확정할 수 있는지도 함께 짚는다.
    3. 경계 항, 종단 가중치, ESS 생략 시 가중치 계승 중 어떤 절차를 확인해야 Eq. 5의 분포와 보고된 출력의 관계를 설명할 수 있는가?
    4. 같은 A100 시간 또는 같은 GPU 사용량으로 맞추면 \(k\), \(N\), 분류기 fine-tuning에 쓰는 계산을 어떻게 비교할 수 있는가? 재추출에서 입자가 서로를 기다리는 비용은 절차에서 끌어낸 해석이고, Table 8은 병렬 실행의 총시간을 보고한다.

### 21. 감사합니다

- section: none
- time: 15초
- message: 목표 분포의 조건과 유한한 계산에서의 선택을 중심으로 토론을 시작하겠습니다.
- on-slide facts: 감사합니다 / Q&A · 발표자 `[이름]` · VILAB · [논문 — arXiv v5](https://arxiv.org/abs/2501.06848v5) · [코드 — FK Diffusion Steering](https://github.com/zacharyhorvitz/Fk-Diffusion-Steering)
- source: 논문 p. 1, 버전 표기와 초록. External 코드 링크 대상은 확인 기록에 있는 [arXiv 초록](https://arxiv.org/abs/2501.06848)을 따름.
- block: `lead` + `groups` 발표자·링크
- assets: none
- interaction: none

## Not applied

- **16번 Table 5의 `table`과 비평가가 제안한 \(k\) toggle** · 한 지표를 네 모델에 걸쳐 비교할 때 `bars`를 쓰라는 본문 규칙에 따라 정적 막대그래프 두 패널로 구성했다. 두 \(k\)에서의 차이를 한 화면에서 비교할 수 있다.
- **Eq. 6과 Eq. 11 전체 식의 화면 배치** · 목표 구조에 맞춰 8번 화면에는 Eq. 6의 분자·분모 의미와 Eq. 7을 두고, Eq. 6의 전체 식은 대본에 넣었다. Eq. 11도 12번 대본에 proposal의 분자와 정규화 합을 함께 적었다.
- **Table 5의 Max 우위를 종단 보정 미사용의 결과로 해석하는 제안** · Table 5에는 종단 보정만 바꾼 비교가 없다. 인쇄된 Algorithm 1의 반환 절차는 8·20번에서 다루고, Max의 점수와 다양성은 각각 해당 실험 조건을 붙여 제시했다.