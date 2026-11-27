너는 이 발표 개요의 **검증자**다. 이 개요를 쓰지 않았다. 파일은 만들거나 고치지 말고 결과만 출력하라.

읽을 것(이 폴더): `outline.md`(검토 대상), `paper.pdf`(논문 원본 "A General Framework for Inference-time Scaling and Steering of Diffusion Models", arXiv 2501.06848; 표 수치는 반드시 PDF 쪽에서 확인), `paper.txt`(텍스트 추출본, 표의 행이 한 칸씩 줄로 끊겨 있다).

할 일:
- 개요의 모든 주장·수치·비교·인과관계·식을 논문에서 찾아 쪽과 위치(§, Fig., Table, Eq., App., Algorithm)를 대라. 찾지 못한 것은 "없음"으로 표시하라.
- 수치는 하나씩 표와 대조하라(행·열, 모델, k, λ, 보상, 일정, 최고 입자인지 입자 평균인지, 어느 분류기로 쟀는지). Δ는 직접 다시 계산하라.
- 식은 논문의 식과 기호 하나하나 대조하라. 개요가 논문 식을 고쳐 적은 곳(예: Eq. 3의 G_t → G_s, Eq. 4의 Z 비율, Eq. 7의 W 표기, 7번의 주변화 유도)이 수학적으로 맞는지, 그리고 그것이 논문에 인쇄된 것과 다르다는 점이 드러나는지 보라.
- 조건이 빠진 수치, 논문보다 일반화해서 말한 결과, 저자의 해석을 사실처럼 쓴 곳, 개요 작성자의 추론을 논문 주장처럼 쓴 곳을 표시하라.
- 그래프를 읽어서 쓴 서술은 그림을 확대해서 확인하라. 곡선만 근거인 서술은 그렇다고 표시하라.
- 그림 장부가 본문 Fig. 1–5, Table 1–7, Algorithm 1을 빠짐없이 담는지, 각 `use` 슬라이드가 그 그림을 정말 필요로 하는지, cut 이유가 타당한지 보라.
- 특히 확인:
  - 4번: importance sampling의 정의(§3.2: k개를 뽑아 exp(λr)로 재추출)와 best-of-n의 관계. "두 방식 모두 고보상 사례를 반환할 수 없다"는 서술의 근거
  - 5번 animation: Fig. 1과 Algorithm 1이 실제로 그리는 것(재추출 시점, 복제, 종료) 
  - 8번: "k→∞ 일관성"의 논문 문장(p. 7)과 조건. 개요가 붙인 "적절한 proposal 지지집합" 같은 조건이 논문에 있는지. 설명용 가상 예의 계산(G = (1,1,2,6) → 확률)
  - 10번: Difference의 G_T = 1에서 potential 곱이 정말 exp(λ r(x_0))가 되는지(r_φ(x_0) = r(x_0)인지, r_φ(x_T) 항이 남는지). Max·Sum의 G_0 식. 가상 보상 이력 A·B·C에서 각 potential이 정말 그 입자를 가장 높게 매기는지 계산
  - 11번: App. C.3의 원문 부등호와 Algorithm 1의 매 단계 재추출, §3.3 interval resampling의 정의
  - 12번: Eq. 8과 "p_θ = q일 때 r_φ = log E[exp(r)]" 문장, many-sample 식
  - 13번: App. C.2의 TDS·SVDD 서술(potential, proposal, nested IS, λ = ∞)
  - 14번: Table 1 각 셀, SDXL-DPO와의 차이 +0.0478, "SDv2.1이 SDXL-DPO를 앞섰다", Fig. 3 예시가 실제로 무엇을 보이는지, GenEval과 IR·HPS 프롬프트 세트
  - 15번: Table 4 셀, −2.6, 본문 §4.1의 MDLM "37.2 vs 79.2"와 "35.3 vs 30.0"이 Table 4와 다른지
  - 16번: Table 3 셀과 Δ(+0.02, +46.9초)
  - 17번: Table 5 셀, +0.038/+0.020, "Max가 모든 경우 최고"인지(Sum과 Difference의 순위 포함)
  - 18번: Table 6·7 셀, 조향 분류기와 holdout 분류기 이름, Table 7의 proposal(gradient guidance), MDLM N=4 기본 설정(App. B.2)과 §4.3 "many rφ" 정의, §4.3 'Better Rewards vs. More Particles' 문단의 22.3%가 Table 6의 어느 행인지
  - 19번: Table 9·10 셀(특히 Table 10의 λ = 1 행들), Fig. 6·7의 설정(App. D: λ, k, potential), Table 9가 Difference potential인지(App. A)
  - 20번: Table 8 시간(11.5s, 9.1s, 17.4s)과 §4.1 문장 "11.5s versus 9.1s", Algorithm 1의 마지막 단계, App. C.3 문장
  - Fig. 2 오른쪽 FLOPs 축(×10^14, 16.0–17.5)이 k = 2…16 구성의 계산량 차이와 맞는지(Table 8의 시간과 비교)

출력(한국어, 1100단어 이내): 번호 매긴 지적. 각 지적은 `[V번호] must|should · 슬라이드 n · 개요의 서술 · 논문의 실제(쪽·위치) · 고칠 문구`. 문제 없는 슬라이드는 묶어서 한 줄로 "확인됨: n, m, …".
