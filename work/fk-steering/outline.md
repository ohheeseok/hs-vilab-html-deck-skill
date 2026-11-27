## Ledger

- Fig. 1 — use: 5. 오른쪽 FK steering 패널의 입자 계보를 overview animation으로 다시 그림.
- Fig. 2 — use: 14. 오른쪽 GenEval–FLOPs 패널.
- Fig. 3 — use: 14. 주황색 소와 보라색 샌드위치 프롬프트 열.
- Fig. 4 — cut: particle 수에 따른 평균 성능 곡선. 이 발표의 입자 평균 비교는 potential을 통제한 Table 5에 집중.
- Fig. 5 — use: 18. SSD-LM의 중간 보상과 최종 보상 간 상관 패널.
- Table 1 — use: 14. SDv2.1과 SDXL 계열의 최고 보상 입자 비교.
- Table 2 — cut: DPO 모델에 FK를 추가한 결과. 대표 결과는 기본 모델에 FK를 적용한 경우로 한정.
- Table 3 — use: 16. Gradient proposal의 점수와 시간.
- Table 4 — use: 15. 텍스트 품질과 다양성, §4.1의 MDLM 수치 대조.
- Table 5 — use: 17. 네 모델의 입자 평균 GenEval.
- Table 6 — use: 18. 중간 보상별 독성 판정률과 perplexity.
- Table 7 — use: 18. ImageNet의 중간 보상과 potential 비교, TDS 행 포함.
- Algorithm 1 — use: 5, 8, 11, 20. 애니메이션 순서, SMC 갱신, 재추출 조건과 최종 출력 토론.
- Table 8 — use: 20. A100 1장과 2장 병렬 시간 대조.
- Tables 9–10 — use: 19. 입자 평균 지표와 CLIP 다양성.
- Table 11 — cut: learned toxicity gradient의 추가 실험. Gradient proposal의 비용 비교는 시간이 함께 보고된 Table 3 사용.
- Figs. 6–7 — use: 19. 같은 프롬프트에서 각각 \(\lambda\)와 potential에 따른 다양성 비교.
- Figs. 8–9 — cut: interval resampling과 프롬프트 충실도의 추가 사례. 일정은 Table 9에서, 프롬프트 사례는 Fig. 3과 Figs. 6–7에서 다룸.

## Sections

- `summary` — 요약 (2)
- `background` — 배경 (3–5)
- `method` — 방법 (6–13)
- `results` — 결과 (14–15)
- `analysis` — 분석 (16–19)
- `discussion` — 정리와 토론 (20)

표지와 ending을 포함해 21장, 20분. 1·21장은 구간 표시 없음. 나머지는 1920×1080 화면 하단에 진행 표시. 시간 배분은 표지·요약 1:00, 배경 2:40, 방법 8:55, 결과 2:10, 분석 4:20, 정리·토론 예고와 ending 0:55. 클리커로 조작하는 슬라이드는 5·10번 두 장이며, 대표 인터랙션은 5번.

## Slides

### 1. Diffusion 모델의 FK steering

- section: none
- message: 이 발표에서는 FK steering이 보상으로 기울인 분포를 어떻게 샘플링하는지 살펴봅니다.
- on-slide facts: 논문 원제 *A General Framework for Inference-time Scaling and Steering of Diffusion Models* · Singhal, Horvitz, Teehan 외 · VILAB 논문 세미나 · 발표자 `[이름]`
- source: p. 1, 제목 및 저자
- block: `lead` 제목 + `groups` 논문 정보·발표 정보
- assets: none
- interaction: none

### 2. FK steering 요약

- section: `summary`
- message: FK steering은 diffusion 경로를 중간에 평가하고 재추출해 보상으로 기울인 목표 분포를 근사합니다.
- on-slide facts: 기여 3개 · 연속·이산 모델과 비미분 보상을 포괄하는 FK 틀 · proposal, potential, 중간 보상의 선택 및 TDS·SVDD와의 관계 · 이미지·텍스트에서 표본 품질과 속성 제어 평가
- source: 초록, §1, pp. 1–4
- block: `statement` + `lead` 한 문장 요약 + `cards` 기여 3개
- assets: none
- interaction: none

### 3. Diffusion steering의 연구 갈래

- section: `background`
- message: 기존 방법은 모델을 다시 학습할지, 추론 중 gradient로 전이를 바꿀지, 여러 입자에 계산을 배분할지에서 갈립니다.
- on-slide facts: Fine-tuning — DDPO, diffusion DPO, KL 정규화 fine-tuning · Gradient guidance — classifier guidance, universal guidance · Particle — best-of-\(n\), TDS, SVDD · 마지막 줄의 발표 질문 — 목표 분포를 유지하면서 중간 단계에서 어느 경로에 계산을 더 배분할 수 있는가?
- source: §§1–2, pp. 2, 4–5
- block: `groups` 3열 + 하단 `callout` 발표 질문
- assets: none
- interaction: none

### 4. 목표 분포와 드문 고보상 표본

- section: `background`
- message: 고보상 표본이 기본 모델에서 드물면 최종 단계에서만 선별하는 방식은 낮은 보상 경로도 끝까지 생성해야 합니다.
- on-slide facts: Eq. 2 · Importance sampling — \(x_0^i\sim p_\theta\), 최종 지수 보상에 비례해 재추출 · Best-of-\(n\) — 독립 완성 표본 중 최고 보상 표본 선택 · 두 방식 모두 생성 도중에는 보상으로 계산을 재배분하지 않음
  \[
  p_{\mathrm{target}}(x_0\mid c)
  =\frac{p_\theta(x_0\mid c)\exp(\lambda r(x_0,c))}{Z}.
  \tag{2}
  \]
- source: §§1, 3.1–3.2, pp. 2, 5–6, Eqs. 1–2
- block: `split` 55:45 · `equation` | `compare`
- assets: Eq. 2
- interaction: none
- notes:
  - symbols: \(c\)는 프롬프트 등 조건, \(x_T\)는 시작 상태, \(x_0\)는 완성 표본, \(r\)은 최종 보상, \(\lambda\)는 기울임의 강도, \(Z\)는 정규화 상수.
  - derivation: 같은 조건에서 두 표본의 기본 확률비에 \(\exp(\lambda\Delta r)\)를 곱한다. 완성 표본 후보에 고보상 사례가 한 번도 들어오지 않으면 두 방식 모두 그 사례를 반환할 수 없다.

### 5. FK steering의 입자 경로

- section: `background`
- message: 중간 보상으로 부모 입자를 재추출하면 살아남은 경로에서 여러 후속 경로를 탐색할 수 있습니다.
- on-slide facts: Fig. 1의 프롬프트 *a green stop sign in a red field* · 역확산 시간축 \(T\to0\) · 부모와 자식 입자의 연결 · \(\hat x_t\), \(G_t\), \(\tau\) · 최종 경로의 potential 곱
- source: Fig. 1, p. 2, §§3.2–3.3, pp. 6–8, Eq. 5, Algorithm 1
- block: `animation` 전체 폭 + `diagram` Fig. 1 오른쪽 패널 재구성
- assets: Fig. 1의 입자 계보, 새 SVG 도식, Eq. 5의 축약 표기
- interaction: animation — **대표 인터랙션**, 클리커 1회당 1 beat
  - reveals: 어떤 입자의 계보가 끊기고, 복제된 부모에서 새 경로가 어디로 갈라지는지 한 화면에서 추적.
  - beats:
    1. 시작 열에 \(k\)개 \(x_T\) 입자 등장. §3.1, Algorithm 1.
    2. 중간 열에서 \(\hat x_t\)로 계산한 보상이 \(G_t\) 표식으로 바뀜. §3.3, p. 8.
    3. 재추출 결과에 따라 한 가지는 끊기고 다른 부모는 복제됨. Fig. 1, Algorithm 1.
    4. 복제된 부모에서 서로 다른 자식 경로가 뻗어 나감. Algorithm 1의 Propose.
    5. \(x_0\)까지 이어진 경로에 \(\prod_{t=T}^{0}G_t=\exp(\lambda r(x_0,c))\)를 붙임. Eq. 5.
- notes:
  - symbols: \(\hat x_t\)는 현재 상태의 denoised estimate, \(G_t\)는 경로의 potential, \(\tau\)는 다음 상태를 뽑는 proposal.
  - derivation: 복제는 재추출에서 일어나는 사건의 한 예로 설명한다. 마지막 등식은 경로마다 만족시킬 설계 조건이다.

### 6. Feynman–Kac 경로 분포

- section: `method`
- message: FK 경로 분포는 기본 diffusion 경로에 지금까지의 potential을 곱해 중간 시점마다 새 분포를 만듭니다.
- on-slide facts: 기본 경로 밀도 × 누적 potential · 이전 경로 분포 × potential로 기울인 한 단계 전이
  \[
  p_{\mathrm{FK},t}(x_{T:t}\mid c)
  =\frac{p_\theta(x_{T:t}\mid c)}{Z_t}
    \prod_{s=T}^{t}G_s(x_{T:s},c).
  \tag{3}
  \]
  \[
  p_{\mathrm{FK},t}(x_{T:t}\mid c)
  =\frac{Z_{t+1}}{Z_t}\,
    p_{\mathrm{FK},t+1}(x_{T:t+1}\mid c)\,
    \underbrace{p_\theta(x_t\mid x_{t+1},c)G_t(x_{T:t},c)}
    _{\text{potential로 기울인 전이}} .
  \tag{4}
  \]
- source: §3.3, p. 6, Eqs. 1, 3–4
- block: `split` 72:28 · `equation` 2개 | `diagram` 이전 경로와 새 한 단계
- assets: Eqs. 3–4, 경로 접두부 도식
- interaction: none
- notes:
  - symbols: \(x_{T:t}=(x_T,\ldots,x_t)\), \(Z_t\)는 해당 경로 분포의 정규화 상수. \(G_t\)는 \(x_t\)까지의 경로를 참조할 수 있다.
  - derivation: 기본 경로 밀도를 직전 경로와 한 단계 전이로 분해한다. potential 곱에서도 마지막 \(G_t\)를 분리하면 Eq. 4가 된다. 원문 Eq. 3의 곱 안에 인쇄된 \(G_t\)는 Eq. 4와 일치하도록 \(G_s\)로 표기한다.

### 7. Potential 곱과 최종 주변분포

- section: `method`
- message: 경로의 potential 곱을 최종 보상의 지수와 맞추면 중간 경로를 적분한 분포가 Eq. 2와 같아집니다.
- on-slide facts: 경로별 곱 조건 · \(x_{T:1}\)의 주변화 · \(Z_0=Z\)
  \[
  \prod_{t=T}^{0}G_t(x_{T:t},c)=\exp(\lambda r(x_0,c)).
  \tag{5}
  \]
  \[
  \int p_{\mathrm{FK},0}(x_{T:0}\mid c)\,dx_{T:1}
  =\frac{\exp(\lambda r(x_0,c))}{Z_0}
     p_\theta(x_0\mid c).
  \]
- source: §3.3, Eq. 5 및 직후 설명, pp. 6–7
- block: `equation` 2개 + `process` 곱 대입 → 최종 보상 인수 분리 → 중간 상태 주변화
- assets: Eq. 5, 주변화 유도식
- interaction: none
- notes:
  - symbols: \(x_{T:1}\)은 완성 표본 이전의 상태들. 이산 상태에서는 적분 대신 합.
  - derivation: Eq. 5의 우변은 \(x_0,c\)에만 의존하므로 적분 밖으로 뺀다. 남은 기본 경로 밀도를 적분하면 \(p_\theta(x_0\mid c)\)가 된다. 서로 다른 potential도 이 조건을 만족할 수 있다.

### 8. SMC 가중치와 입자 갱신

- section: `method`
- message: SMC는 proposal이 만든 경로에 전이 비율과 potential로 가중치를 매겨 각 FK 분포를 입자로 근사합니다.
- on-slide facts: Eq. 6의 목표 경로 대 proposal 경로 비율 · Eq. 7의 비정규화 가중치 · Algorithm 1의 `Resample → Propose → Re-weight` · \(k\to\infty\)에서 최종 입자 근사의 일관성
  \[
  \frac{p_{\mathrm{FK},t}(x^i_{T:t}\mid c)}
  {p_{\mathrm{FK},t+1}(x^i_{T:t+1}\mid c)\,
   \tau(x_t^i\mid x^i_{T:t+1},c)}
  \tag{6}
  \]
  \[
  W_t^i\propto
  G_t(x^i_{T:t},c)\,
  \frac{p_\theta(x_t^i\mid x_{t+1}^i,c)}
       {\tau(x_t^i\mid x^i_{T:t+1},c)} .
  \tag{7}
  \]
- source: §3.3, p. 7, Eqs. 6–7, Algorithm 1, Del Moral & Miclo (2000) 정리 3.19 인용
- block: `split` 60:40 · `equation` 2개 | `process` 3단계 + 일관성 `callout`
- assets: Eqs. 6–7, Algorithm 1의 세 갱신 줄
- interaction: none
- notes:
  - symbols: \(i\)는 입자 번호, \(W_t^i\)는 논문의 입자 가중치 \(G_t^i\), \(\tau\)는 실제 제안 분포. 재추출 확률은 \(W_t^i/\sum_jW_t^j\).
  - derivation: Eq. 6에 Eq. 4를 넣으면 Eq. 7에 공통 인수 \(Z_{t+1}/Z_t\)가 붙는다. 입자끼리 정규화할 때 이 인수는 상쇄된다. Resample에서 경로를 복제하고, Propose에서 자식을 뽑고, Re-weight에서 새 가중치를 계산한다. 일관성은 Eq. 5와 적절한 proposal 지지집합 아래의 최종 가중 경험분포에 관한 설명이다. 비가중 표본으로 읽으려면 최종 가중치에 따른 재추출을 구분해서 설명한다.
  - 설명용 가상 예: \(\tau=p_\theta\), 입자 4개의 \(G_t=(1,1,2,6)\). 재추출 확률은 \((0.1,0.1,0.2,0.6)\). 가능한 부모 인덱스는 \((4,3,4,4)\). 이 경우 4번 부모의 복제본 세 개가 각각 다음 상태를 제안한다.

### 9. Proposal의 세 가지 선택

- section: `method`
- message: Proposal을 바꾸면 어느 상태를 먼저 탐색할지가 달라지고, Eq. 7의 비율이 그 차이를 보정합니다.
- on-slide facts: 기본 전이 \(\tau=p_\theta\) · 연속 상태와 미분 가능 보상에서 Gaussian 평균 이동 · 이산 상태에서 potential을 곱한 전이의 정규화
  \[
  \tau=\mathcal N\!\left(\mu_\theta+
      \sigma_\theta^2\lambda\nabla_{x_t}r_\phi(x_t,c),
      \sigma_\theta^2 I\right)
  \tag{10}
  \]
  \[
  \sum_{x_t}p_\theta(x_t\mid x_{t+1},c)G_t(x_{T:t},c).
  \tag{11}
  \]
- source: §3.3, p. 7, App. C.1, pp. 23–24, Eqs. 10–11
- block: `split` 33:67 · `lead` 기본 전이 | `equation` 2개
- assets: Eqs. 10–11
- interaction: none
- notes:
  - symbols: \(\mu_\theta,\sigma_\theta^2\)는 기본 Gaussian 전이의 평균과 분산, \(I\)는 단위행렬, \(r_\phi\)는 중간 보상. Eq. 11의 합은 가능한 다음 이산 상태에 대한 합이다.
  - derivation: 기본 전이를 쓰면 Eq. 7의 전이 비율은 1이다. Eq. 10은 분산을 유지하고 평균을 보상 gradient 방향으로 옮긴다. Eq. 11은 \(p_\theta G_t\)를 proposal 확률로 바꾸는 분모를 계산한다.

### 10. Difference, Max, Sum potential

- section: `method`
- message: 같은 보상 이력에서도 최근 증가량, 지금까지의 최고값, 누적값 중 무엇을 쓰느냐에 따라 재추출 확률이 달라집니다.
- on-slide facts: 중간 시점의 세 식 · Difference의 \(G_T=1\) · Max·Sum의 \(G_0\) 보정 · 설명용 가상 보상 이력 세 줄
  \[
  \begin{aligned}
  G_t^{\mathrm{Diff}}&=\exp\!\left(\lambda[r_\phi(x_t,c)-r_\phi(x_{t+1},c)]\right),\\
  G_t^{\mathrm{Max}}&=\exp\!\left(\lambda\max_{s=t,\ldots,T}r_\phi(x_s,c)\right),\\
  G_t^{\mathrm{Sum}}&=\exp\!\left(\lambda\sum_{s=t}^{T}r_\phi(x_s,c)\right).
  \end{aligned}
  \]
  \[
  G_0=\exp(\lambda r(x_0,c))\left(\prod_{t=1}^{T}G_t\right)^{-1}.
  \]
- source: §3.3, pp. 7–8, *Choosing the potential*, Eq. 5
- block: `split` 60:40 · `equation` 중간 potential·종단 보정 | `toggle` + `diagram` 같은 세 보상 이력
- assets: potential 식 3종, \(G_0\) 식, 설명용 가상 궤적
- interaction: toggle — **reveals:** 이력은 고정하고 potential만 바꿨을 때 어느 입자의 재추출 확률이 가장 높은지 표시.
  - 공통 화면: 시간순 가상 보상 A \(=(0,.2,.8)\), B \(=(.9,.1,.2)\), C \(=(.6,.6,.6)\). \(\tau=p_\theta,\ \lambda>0\), 같은 중간 시점.
  - states: Difference — A의 최근 증가량 \(0.6\) 강조 → Max — B의 과거 최고값 \(0.9\) 강조 → Sum — C의 누적값 \(1.8\) 강조. 클리커 다음 키로 순환한 뒤 다음 슬라이드로 진행.
- notes:
  - symbols: \(s\)는 이미 지난 역확산 시점, \(G_0\)는 완성 표본의 최종 보정을 담당하는 potential.
  - derivation: 지수함수가 증가하므로 세 상태에서 각각 증가량·최고값·누적값으로 가중치 순서를 설명할 수 있다. Difference를 인접 단계마다 곱하면 지수 안에 \(r_\phi(x_0,c)-r_\phi(x_T,c)\)가 남는다. 최종 보상과 초기 경계값이 Eq. 5에 맞는지 확인하고, 필요하면 위의 \(G_0\) 보정으로 경로별 곱을 맞춘다.

### 11. Interval과 ESS 재추출

- section: `method`
- message: Interval resampling은 개입 시점을 정하고, ESS는 재추출을 결정할 때 현재 가중치가 얼마나 집중됐는지 보여 줍니다.
- on-slide facts: \(0\in\mathcal R\), \(t\notin\mathcal R\)이면 \(G_t=1\) · §4.1 이미지 일정 \([0,20,40,60,80]\), 진행 방향 \(80\to0\) · App. C.3의 인쇄 조건 \(\mathrm{ESS}_t<k/2\)에서 재추출 생략
  \[
  \mathrm{ESS}_t=\frac{1}{\sum_{i=1}^{k}(\widehat G_t^i)^2}
  \in[1,k].
  \tag{13}
  \]
- source: §3.3 *Interval Resampling*, p. 8, §4.1, p. 9, App. C.3, p. 24, Eq. 13
- block: `split` 55:45 · `diagram` 고정 일정 시간축 | `equation` ESS와 부록 조건
- assets: Eq. 13, \(T=100\) 일정 도식
- interaction: none
- notes:
  - symbols: \(\mathcal R\)은 potential을 적용하는 시점 집합, \(\widehat G_t^i\)는 부록의 정규화 가중치 표기, \(k\)는 전체 입자 수.
  - derivation: 균등한 가중치의 ESS는 \(k\), 한 입자에 집중되면 1이다. 표준적인 adaptive SMC는 보통 ESS가 낮을 때 재추출하고, 재추출을 건너뛴 단계에서는 이전 가중치를 이어 간다. App. C.3의 부등호와 생략 방향은 인쇄된 대로 표시하고, 실험 구현에도 같은 조건이 쓰였는지는 구분한다.

### 12. 중간 보상을 얻는 세 방법

- section: `method`
- message: 중간 보상은 현재 입자에서 기대할 수 있는 최종 보상을 추정하며, denoised estimate 평가, 여러 완성 표본, 별도 학습으로 얻을 수 있습니다.
- on-slide facts: \(r_\phi(x_t,c)=r(\hat x_t,c)\) · Many-sample은 \(x_0^j\sim p_\theta(x_0\mid x_t,c)\)를 \(N\)번 뽑아 \(\log[\frac1N\sum_j\exp(r(x_0^j,c))]\) 계산 · Learned는 아래 회귀 후 \(r_\phi=\log a_\phi\)
  \[
  \arg\min_\phi\ 
  \mathbb E_{t\sim U[0,T]}
  \mathbb E_{x_0\sim q_{\mathrm{data}}(\cdot\mid c),\,x_t\sim q(\cdot\mid x_0)}
    \bigl\|a_\phi(x_t,c)-\exp(r(x_0,c))\bigr\|_2^2 .
  \tag{8}
  \]
- source: §3.3 *Choosing intermediate rewards*, p. 8, Eq. 8
- block: `split` 42:58 · `groups` 단일 denoised estimate·many-sample | `equation` 학습 목적함수
- assets: Eq. 8, many-sample 식
- interaction: none
- notes:
  - symbols: \(\hat x_t\)는 모델에서 얻는 완성 표본 추정치, \(N\)은 입자당 완성 표본 수, \(q\)는 forward noising, \(a_\phi\)는 \(\exp(r)\)를 예측하는 모델.
  - derivation: 제곱오차의 최적 예측은 조건부 평균이다. 논문이 둔 \(p_\theta=q\) 근사 아래 \(\log a_\phi\)는 \(\log\mathbb E_{p_\theta}[\exp(r)\mid x_t,c]\)에 대응한다. Eq. 8의 학습 표적은 \(\exp(r)\)이며, 별도의 \(\lambda\)는 potential 식에서 적용한다.

### 13. Importance sampling, TDS, SVDD

- section: `method`
- message: 세 방법은 FK 틀 안에서 어떤 potential과 proposal을 쓰고 언제 입자를 선택하느냐로 구분할 수 있습니다.
- on-slide facts: Importance sampling — \(t\ge1\)에서 \(G_t=1\), \(G_0=\exp(\lambda r)\), 기본 전이 · TDS — denoised estimate에서 평가한 Difference potential, classifier-guided proposal, SMC · SVDD — Difference potential과 기본 proposal, nested importance sampling, 단계마다 후보 하나를 뽑아 복제, \(\lambda\to\infty\)에서 단계별 best-of-\(n\)
- source: §2, p. 5, §3.3, p. 7, App. C.2, p. 24, Eq. 12 및 SVDD 설명
- block: `cards` 3열, 각 카드에 potential·proposal·선택 방식
- assets: none
- interaction: none
- notes:
  - symbols: \(t=0\)은 완성 시점, \(n\)은 SVDD의 단계별 후보 수를 설명하는 best-of-\(n\) 표기.
  - derivation: SVDD에서 같은 부모의 자식을 비교하면 Difference의 부모 보상 항은 공통이다. \(\lambda\)가 커질수록 가장 높은 중간 보상의 후보에 선택 확률이 집중된다.

### 14. 이미지 품질과 추론 비용

- section: `results`
- message: ImageReward로 조향한 SDv2.1은 최고 보상 입자의 GenEval에서 SDXL-DPO를 앞섰으며, 비교 해석은 표본 선택 방식과 계산 조건에 따라 달라집니다.
- on-slide facts:
  - Table 1 발췌, 열 순서 `GenEval / ImageReward / HPS` · SDv2.1 BoN \(k=4\) `0.6172 / 0.888 / 0.263` · SDv2.1 FK \(k=3\) `0.5987 / 0.864 / 0.265` · SDv2.1 FK \(k=4\) `0.6289 / 1.006 / 0.268` · SDXL-DPO \(k=1\) `0.5811 / 0.859 / 0.296`. FK \(k=4\)와 SDXL-DPO의 GenEval 차이 **+0.0478**.
  - FK 조건 · ImageReward, \(\lambda=10\), 기본 proposal, Max, \([0,20,40,60,80]\), DDIM \(\eta=1,\ T=100\), CFG 7.5. Table 1의 FK 값은 **최고 보상 입자**. GenEval과 ImageReward·HPS의 평가 프롬프트 세트 구분.
  - Fig. 2 오른쪽 · GenEval–FLOPs 비교. Fig. 3 · *a photo of an orange cow and a purple sandwich*, SDXL 독립 표본과 SDv2.1 FK \(k=4\) 최고 보상 표본에서 물체와 색 지정의 구현 비교.
- source: §4.1, pp. 9–10, Fig. 2 p. 3, Fig. 3 p. 4, Table 1
- block: `split` 56:44 · `table` + `deltas` GenEval 1개 | `figure` FLOPs 축·범례 유지 + `figureNumbered` 프롬프트 한 열의 두 표본
- assets: Table 1 발췌, Fig. 2 오른쪽, Fig. 3 프롬프트 열 크롭
- interaction: none
- notes: SDv2.1 FK \(k=3\)는 SDXL-DPO보다 GenEval이 높고, 같은 SDv2.1의 BoN \(k=4\)보다 GenEval이 낮다. Table 1의 SDv1.5 HPS도 FK 0.263, BoN 0.265로 캡션의 포괄적인 우위 표현에 예외가 있다.

### 15. 텍스트 품질과 반복 다양성

- section: `results`
- message: 텍스트에서는 조향한 품질 지표가 좋아지는 경우에도 다른 품질 지표와 표현 다양성을 함께 확인해야 합니다.
- on-slide facts:
  - Table 4 발췌, 열 순서 `GPT2-XL PPL / CoLA / Dist-1/2/3` · SSD-LM 기본 \(k=1\) `23.2 / 68.3 / 46/83/92` · GPT2 보상 BoN \(n=4\) `13.6 / 75.6 / 42/77/88` · GPT2 보상 FK \(k=4\) `11.0 / 80.0 / 40/73/86`. 같은 보상의 BoN 대비 PPL **−2.6**.
  - FK 설정 · \(\lambda=10\), Difference, 재추출 50회, SSD-LM은 10 step마다, MDLM은 20 step마다 · 15개 프롬프트당 길이 50의 continuation 20개 · 실행마다 최고 점수 표본 반환, 3 seeds 평균.
- source: §4.1, pp. 11–13, Table 4, App. B.1–B.2, pp. 21–22
- block: `split` 70:30 · `table` | `deltas` PPL 1개 + `groups` 생성·평가 조건
- assets: Table 4의 SSD-LM 세 행
- interaction: none
- notes: GPT2 계열 보상과 GPT2-XL 평가의 관계를 짚되 두 모델 표기는 구분한다. MDLM trigram 수치를 언급할 경우 Table 4의 PPL `85.3 → 40.3`을 사용한다. §4.1 본문은 `79.2 → 37.2`로 다르게 적혀 있다.

### 16. Gradient proposal의 비용

- section: `analysis`
- message: SDv1.5에서 FK proposal에 ImageReward gradient를 추가하면 세 품질 지표가 올라가고 표에 보고된 샘플링 시간도 늘어납니다.
- on-slide facts: Table 3, SDv1.5, 열 순서 `GenEval / IR / HPS / 시간` · 기본 \(k=1\) `0.44 / 0.187 / 0.245 / 2.4초` · gradient guidance \(k=1\) `0.45 / 0.668 / 0.245 / 20초` · FK \(k=4\) `0.54 / 0.898 / 0.263 / 8.1초` · FK+gradient \(k=4\) `0.56 / 1.290 / 0.268 / 55초`. 두 FK 행의 차이 · GenEval **+0.02**, 시간 **+46.9초**.
- source: §4.1, pp. 9–11, Table 3, App. C.1, Eq. 10
- block: `split` 68:32 · `table` | `deltas` GenEval·시간
- assets: Table 3
- interaction: none
- notes: GenEval은 Table 3의 반올림 값 그대로 사용한다. §4.1 기본 이미지 FK 설정은 \(\lambda=10\)이다. Gradient 행의 별도 \(\lambda\)와 GPU 조건은 Table 3에 명시되어 있지 않다.

### 17. Potential별 입자 평균 GenEval

- section: `analysis`
- message: 이 ImageReward 설정에서는 Max가 네 모델과 두 입자 수 모두에서 가장 높은 입자 평균 GenEval을 기록했습니다.
- on-slide facts: 모델 순서 `SDv1.4 / SDv1.5 / SDv2.1 / SDXL` · GenEval은 **전체 입자 평균** · ImageReward, \(\lambda=10\), 일정 \([0,20,40,60,80]\).
  - \(k=4\) · Max `0.540 / 0.540 / 0.616 / 0.633` · Difference `0.525 / 0.526 / 0.578 / 0.603` · Sum `0.496 / 0.499 / 0.569 / 0.613`
  - \(k=8\) · Max `0.569 / 0.561 / 0.635 / 0.648` · Difference `0.566 / 0.553 / 0.615 / 0.640` · Sum `0.532 / 0.517 / 0.588 / 0.634`
  - SDv2.1의 Max–Difference 차이 · \(k=4\) **+0.038**, \(k=8\) **+0.020**
- source: §4.2, pp. 12, 14, Table 5
- block: `split` 50:50 · `bars` \(k=4\) | `bars` \(k=8\), 공통 축·범례
- assets: Table 5의 막대그래프 2개
- interaction: none
- notes: ImageReward의 보고 범위는 \([-2,2]\)다. 일찍 상한에 도달한 입자의 다음 Difference 증가량은 0이 될 수 있다는 논문의 설명을 10번 슬라이드와 연결한다. 다양성 비교는 19번에서 다룬다.

### 18. 중간 보상의 질과 속성 제어

- section: `analysis`
- message: 더 많은 표본이나 별도 학습으로 만든 중간 보상이 속성 제어 지표를 높인 경우가 있었으며, 그 차이는 평가 분류기와 proposal에도 걸쳐 있습니다.
- on-slide facts:
  - Fig. 5 오른쪽 · SSD-LM에서 추론 진행에 따른 중간 독성 보상과 최종 독성 보상의 상관. Denoised estimate 평가와 learned 보상 곡선.
  - Table 6, \(k=8,\ \lambda=10\), Difference, 기본 proposal · 열 순서 `조향 RoBERTa 독성 판정률 / holdout XLM-R 독성 판정률 / GPT2-XL PPL` · SSD-LM 기본 중간 보상 `25.0% / 29.7% / 23.9` → learned `39.0% / 38.0% / 26.9` · MDLM 기본 \(N=4\) `53.4% / 48.3% / 74.3` → many-sample \(N=16\) `64.7% / 51.7% / 82.9`. 3 seeds 평균.
  - Table 7, ImageNet 1,000 클래스, \(256\times256\), \(k=4\), gradient proposal · 분류기의 목표 클래스 확률 `입자 평균 (최대)` · TDS, denoised, Difference `0.59 (0.72)` · denoised, Max `0.65 (0.70)` · learned, Difference `0.88 (0.94)` · learned, Max `0.88 (0.96)`.
- source: §4.3, pp. 13–15, Tables 6–7, Fig. 5, App. B.2, pp. 21–23, App. C.2
- block: `split` 52:48 · `figure` Fig. 5 오른쪽 + `table` 독성·PPL | `table` ImageNet 비교
- assets: Fig. 5 오른쪽 크롭, Tables 6–7 발췌
- interaction: none
- notes: Table 7의 learned 분류기는 potential과 gradient proposal 양쪽에 쓰인다. 표에서 읽을 수 있는 것은 이 결합 변경의 결과다. MDLM의 집계는 §4.3에서 log-mean-exp 식으로, App. B.2에서는 보상 평균으로 서술된다. 두 설명이 같은 계산을 가리키는지는 확인 필요.

### 19. 조향 강도와 입자 다양성의 한계

- section: `analysis`
- message: 보상과 재추출을 강하게 적용하면 높은 점수의 경로를 남길 수 있지만, 다양한 후보를 얻는 데에는 비용이 생깁니다.
- on-slide facts:
  - Table 9, GenEval 프롬프트, SDv1.4, \(k=4\), ImageReward·Difference · `입자 평균 GenEval / CLIP-Div` · 독립 표본 `0.4408 / 0.3158` · \(\lambda=10\), `5-30-5` `0.4814 / 0.1437` · \(\lambda=10\), `20-80-20` `0.5258 / 0.1050` · \(\lambda=2\), `20-80-20` `0.4910 / 0.2239`.
  - Table 10, ImageReward 프롬프트, 같은 모델·\(k\)·potential, `20-80-20` · \(\lambda=1\to10\)에서 입자 평균 IR `0.502 → 0.811`, CLIP-Div `0.173 → 0.091`.
  - *a green stop sign in a red field* · Fig. 6, SDXL, Max, \(k=4\), \(\lambda=2\)와 \(10\)의 구도 차이 · Fig. 7, SDXL, \(k=8,\lambda=2\), Difference와 Max의 반복 구도 비교 · §5의 적용 한계, 강한 보상 함수의 가용성.
- source: §§4.2, 5, pp. 12, 16, App. A, pp. 21–22, Tables 9–10, App. D, pp. 25–27, Figs. 6–7
- block: `split` 52:48 · `table` 두 발췌 + `callout` 보상 함수 의존 | `figure` 2개, 조건·행 라벨 유지
- assets: Tables 9–10 발췌, Fig. 6의 \(\lambda=2,10\) 행, Fig. 7의 Difference·Max 행
- interaction: none
- notes: CLIP-Div는 입자 쌍의 CLIP 임베딩 제곱거리 평균이다. \(\lambda\)를 높였을 때 GenEval이 항상 오르는 것은 아니다. Table 9의 SDv2.1 `5-30-5`에서는 \(\lambda=2\)의 0.5607이 \(\lambda=10\)의 0.5523보다 높다. 정량 표의 일정 이름은 표기 그대로 사용한다.

### 20. 정리와 토론

- section: `discussion`
- message: FK 틀은 목표 분포를 정의하는 조건과 유한한 입자로 그 분포를 근사하는 설계 선택을 구분해 비교할 수 있게 합니다.
- on-slide facts:
  - 정리 · Eq. 5의 경로별 곱 → Eq. 2의 주변분포 · proposal·potential·중간 보상 → 유한 \(k\)에서의 탐색, 점수, 다양성, 비용.
  - **근거 · 시간 비교** — §4.1의 SDXL 기본 \(k=1\) `11.5초`는 A100 1장. SDv2.1 FK \(k=4\) `9.1초`는 A100 2장 병렬이고, 1장에서는 `17.4초`. 같은 장치 수로 맞추면 속도 주장을 어떻게 읽어야 하는가?
  - **근거 · 종단 가중치와 보고 표본** — Eq. 5, Algorithm 1의 \(t=0\) 가중치 계산 후 상태 반환, §4.1의 최고 보상 입자 보고. Eq. 2에 대한 근사와 최고 점수 표본의 개선을 각각 어떤 통계로 확인할 수 있는가?
  - **근거 · ESS 조건** — App. C.3는 \(\mathrm{ESS}<k/2\)에서 재추출을 생략한다고 적는다. Algorithm 1의 매 단계 재추출 및 통상적인 저ESS 재추출과 비교할 때, App. D의 다양성 결과를 해석하려면 실제 부등호와 생략 시 가중치 처리 중 무엇을 확인해야 하는가?
  - **대가 · 해석** — \(k\) 확대, 입자당 \(N\) 확대, learned 보상은 서로 다른 곳에 계산을 쓴다. 같은 추론 시간으로 맞추고 보상 모델 학습비를 별도로 드러내면 Table 6의 비교는 어떻게 달라질 수 있는가?
- source: Eq. 5·Algorithm 1, pp. 6–7, §4.1 및 Table 1, p. 10, §4.3 및 Table 6, pp. 14–15, Table 8, p. 21, Apps. B.2, C.3, D, pp. 21–25
- block: `statement` + `lead` 정리 + `cards` 토론 4개
- assets: Table 8의 SDv2.1·SDXL 시간 셀, Eq. 5·Algorithm 1·Eq. 13 참조
- interaction: none

### 21. 감사합니다 / Q&A

- section: none
- message: 목표 분포의 보장 조건과 실험에서의 설계 선택을 놓고 토론하겠습니다.
- on-slide facts: 감사합니다 / Q&A · 발표자 `[이름]` · VILAB · [논문 arXiv:2501.06848v5](https://arxiv.org/abs/2501.06848v5) · [FK Diffusion Steering 코드](https://github.com/zacharyhorvitz/FK-Diffusion-Steering)
- source: p. 1, arXiv 버전 표기 및 초록의 코드 링크
- block: `lead` + `groups` 발표자·링크
- assets: none
- interaction: none