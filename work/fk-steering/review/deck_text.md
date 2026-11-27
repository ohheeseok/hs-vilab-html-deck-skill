# Deck text — A General Framework for Inference-time Scaling and Steering of Diffusion Models

## Slide 1 — A General Framework for Inference-time Scaling and Steering of Diffusion Models
[1.subtitle] 생성 도중 입자를 보상으로 다시 뽑아 diffusion 모델을 조정하는 FK steering
[1.figure.alt] Fig. 1. 세 패널. 왼쪽 Inference는 경로 하나로 x_T에서 x_0까지 간다. 가운데 Best-of-N은 경로 여러 개를 끝까지 만든 뒤 보상이 가장 높은 하나에 별을 붙인다. 오른쪽 FK Steering은 중간 단계에서 일부 경로에 빨간 ×를 치고, 남은 경로에서 여러 갈래가 다시 갈라진다. 프롬프트는 a green stop sign in a red field.
[1.figure.caption] **Fig. 1** 독립 생성, best-of-N, FK steering의 입자 경로
[1.notes.0] 오늘은 ICML 2025에 실린 FK steering 논문을 소개합니다. diffusion 모델을 다시 학습하지 않고, 생성하는 동안 표본 여러 개를 함께 만들면서 보상이 높아 보이는 표본을 골라 이어 가는 방법입니다.
[1.notes.1] 이번 발표는 이론을 중심으로 진행합니다. 이 절차가 어떤 분포에서 표본을 뽑으려는 것인지, 그 보장이 어떤 조건에서 성립하는지를 먼저 보고, 실험은 그 선택지를 비교한 근거로 보겠습니다.

## Slide 2 — FK steering 요약
[2.title] FK steering 요약
[2.message] FK steering은 표본 여러 개를 함께 생성하면서 중간 단계마다 보상으로 점수를 매겨 다시 뽑고, 점수 함수의 곱을 맞춰 보상으로 기울인 분포를 근사한다.
[2.body.0.text] 생성 도중 여러 입자(particle)를 중간 보상으로 평가해 다시 뽑는다. 점수 함수(potential)의 곱이 $\exp(\lambda r(x_0))$가 되게 정하면, 보상으로 기울인 분포 $p_\theta(x_0)\exp(\lambda r(x_0))$를 근사한다.
[2.body.1.items.0.title] Feynman-Kac 틀
[2.body.1.items.0.text] 연속·이산 diffusion 모두에 쓰고, 미분할 수 없는 보상도 쓸 수 있는 입자 기반 샘플러
[2.body.1.items.1.title] 세 가지 선택
[2.body.1.items.1.text] proposal, potential, 중간 보상을 고르는 문제로 정리한다. TDS와 SVDD는 그중 특정한 선택이다
[2.body.1.items.2.title] 이미지·텍스트 실험
[2.body.1.items.2.text] Stable Diffusion을 ImageReward로 steering하고, 텍스트 diffusion의 품질과 독성을 조정한다. 모델은 다시 학습하지 않는다
[2.notes.0] 한 문장으로 요약하면, FK steering은 표본 여러 개를 함께 생성하면서 중간 단계마다 보상으로 점수를 매기고 그 점수에 따라 다시 뽑습니다. 이때 점수 함수, 논문 용어로 potential의 곱이 최종 보상의 지수와 같아지도록 정하면, 결과 표본이 보상으로 기울인 분포를 근사합니다.
[2.notes.1] 기여는 세 가지로 보겠습니다. 첫째, Feynman-Kac 입자 방법을 diffusion steering에 쓰는 일반적인 틀입니다. 연속 상태와 이산 상태 모델 모두에 쓰고, 보상이 미분 가능할 필요가 없습니다. 둘째, 이 틀에서 사용자가 고를 것을 proposal, potential, 중간 보상 세 가지로 정리하고, 기존 방법인 TDS와 SVDD가 그중 특정한 선택이라는 것을 보입니다. 셋째, 이미지와 텍스트 실험입니다. 모델을 다시 학습하지 않고 추론 계산만 늘립니다.

## Slide 3 — Diffusion steering의 연구 갈래
[3.title] Diffusion steering의 연구 갈래
[3.message] 보상을 반영하는 기존 방법은 모델을 다시 학습하거나, 추론 중 보상의 gradient로 전이를 옮기거나, 여러 표본 중에서 고른다.
[3.body.0.columns.0.label] 갈래
[3.body.0.columns.1.label] 대표 방법
[3.body.0.columns.2.label] 필요한 것
[3.body.0.columns.3.label] 제약
[3.body.0.groups.0.rows.0.cells.2] 보상으로 추가 학습
[3.body.0.groups.0.rows.0.cells.3] 학습 비용, 보상 하나에 묶임
[3.body.0.groups.0.rows.1.cells.2] 보상의 gradient
[3.body.0.groups.0.rows.1.cells.3] 미분 가능한 보상, 연속 상태
[3.body.0.groups.0.rows.2.cells.0] 입자 기반
[3.body.0.groups.0.rows.2.cells.2] 표본 여러 개
[3.body.0.groups.0.rows.2.cells.3] best-of-$n$: 낮은 표본도 끝까지
[3.body.1.text] 이 발표의 질문: 생성 도중 보상이 높아 보이는 표본에 계산을 더 쓰면서도, 보상으로 기울인 분포에서 표본을 얻을 수 있는가?
[3.notes.0] 보상을 반영하는 방법은 크게 세 갈래입니다. 첫째는 fine-tuning입니다. DDPO, Diffusion-DPO, 그리고 KL 정규화를 둔 fine-tuning이 있고, 학습 비용이 들고 모델이 보상 하나에 묶입니다.
[3.notes.1] 둘째는 gradient guidance입니다. classifier guidance나 universal guidance처럼 추론 중 보상의 gradient로 다음 상태를 옮깁니다. 보상이 미분 가능해야 하고 상태가 연속이어야 합니다.
[3.notes.2] 셋째는 표본 여러 개를 만드는 입자 기반 방법입니다. best-of-n은 어떤 보상이든 쓸 수 있지만, 논문 표현대로 보상이 낮게 끝날 표본에도 계산을 많이 씁니다. TDS와 SVDD는 중간에 고르는 방법이고, 뒤에서 FK 틀의 특수한 경우로 다시 봅니다. 이 발표가 답할 질문은 화면 아래와 같습니다.

## Slide 4 — 목표 분포와 importance sampling
[4.title] 목표 분포와 importance sampling
[4.message] 목표는 기본 모델의 분포를 보상의 지수로 기울인 분포이고, 완성된 표본만 보고 고르는 방법은 보상이 높은 표본이 드물면 표본이 많이 필요하다.
[4.body.0.left.0.symbols.0.1] 기본 diffusion 모델. $x_T$에서 시작해 $x_{T-1},\dots,x_0$ 순서로 노이즈를 제거
[4.body.0.left.0.symbols.1.1] 보상: 사람 선호 점수, 분류기 확률 등
[4.body.0.left.0.symbols.2.1] 기울이는 강도. 클수록 보상이 높은 표본에 확률이 몰림
[4.body.0.left.0.symbols.3.1] 조건(프롬프트), 정규화 상수
[4.body.0.right.0.items.0.items.0] $p_\theta$에서 완성 표본 $k$개 생성
[4.body.0.right.0.items.0.items.1] $\exp(\lambda r)$에 비례해 다시 뽑음
[4.body.0.right.0.items.1.items.0] 완성 표본 $n$개 생성
[4.body.0.right.0.items.1.items.1] 보상이 가장 높은 하나를 고름
[4.body.0.right.1.text] 두 방법 모두 생성이 끝난 뒤에만 보상을 본다
[4.notes.0] 먼저 목표 분포입니다. 기본 모델 p세타는 x_T에서 시작해 노이즈를 한 단계씩 제거해 x_0를 만듭니다. 여기에 보상 r을 정하고, 기본 모델의 확률에 exp(람다 r)을 곱해 보상이 높은 표본 쪽으로 기울인 분포를 만듭니다. 이것이 식 2의 p_target이고, 람다가 클수록 보상이 높은 표본에 확률이 몰립니다.
[4.notes.1] 이 분포에서 뽑는 가장 단순한 방법이 importance sampling입니다. 기본 모델에서 완성 표본 k개를 뽑고, exp(람다 r)에 비례해 다시 뽑습니다. best-of-n은 n개 중 보상이 가장 높은 하나를 고릅니다. 두 방법 모두 생성이 끝난 뒤에만 보상을 봅니다.
[4.notes.2] 문제는 보상이 높은 표본이 기본 모델에서 드물 때입니다. 설명용 가상 수치로, 기본 모델에서 확률 1%인 사건에 보상 1을 주고 나머지에 0을 주겠습니다. 람다가 10이면 목표 분포에서 그 사건의 확률은 99.55%입니다. 그런데 기본 모델에서 표본 4개를 뽑으면 그 사건이 한 번이라도 나올 확률은 3.94%에 그칩니다. Chatterjee와 Diaconis는 importance sampling에 필요한 표본 수가 대략 두 분포의 KL divergence의 지수 정도라고 보였고, 논문도 이 결과를 인용합니다. 그래서 생성 도중에 고르는 방법이 필요합니다.

## Slide 5 — FK steering의 입자 경로
[5.title] FK steering의 입자 경로
[5.message] FK steering은 생성 도중 중간 보상이 낮은 입자를 버리고 높은 입자를 복제한 뒤, 복제된 입자들이 각자 생성을 이어 간다.
[5.body.0.reveals] best-of-n과 같은 출발점에서, FK steering이 생성 중간에 어느 입자를 버리고 어느 입자를 복제해 다시 갈라지게 하는지 보인다.
[5.body.0.beats.0.text] 입자 4개가 $x_T$에서 $x_0$까지 따로 생성되고, 끝에서 보상이 가장 높은 하나를 고른다
[5.body.0.beats.1.title] 중간 단계에서 점수
[5.body.0.beats.1.text] 한 중간 단계에서 입자마다 중간 보상을 계산한다(막대 길이)
[5.body.0.beats.2.title] 다시 뽑기
[5.body.0.beats.2.text] 점수에 비례해 4개를 다시 뽑는다. 낮은 두 입자는 빠지고 가장 높은 입자가 세 번 뽑혔다
[5.body.0.beats.3.title] 다시 생성
[5.body.0.beats.3.text] 뽑힌 입자들이 각자 노이즈 제거를 이어 가 서로 다른 $x_0$에 도착한다
[5.body.0.caption] **Fig. 1** 가운데·오른쪽 패널을 바탕으로 다시 그림. 다시 뽑는 단계를 한 번으로 줄였고, 입자의 높이는 설명용
[5.notes.0] 지금 화면은 best-of-n입니다. 입자 4개가 x_T에서 출발해 각자 x_0까지 생성되고, 끝에서 보상이 가장 높은 하나에 별을 붙입니다. 논문 Fig. 1의 가운데 패널입니다.
[5.notes.1] [1] FK steering은 생성 도중 한 단계에서 멈추고, 입자마다 중간 보상을 계산합니다. 막대 길이가 그 점수입니다. 중간 보상을 어떻게 계산하는지는 뒤에서 다룹니다.
[5.notes.2] [2] 그다음 점수에 비례해 입자 4개를 다시 뽑습니다. 이 예에서는 점수가 낮은 두 입자가 한 번도 뽑히지 않아 빠지고, 점수가 가장 높은 입자가 세 번 뽑혀 복제됩니다. 입자 수는 그대로 4개입니다.
[5.notes.3] [3] 뽑힌 입자들은 각자 노이즈 제거를 이어 갑니다. 생성에 무작위성이 있으므로 같은 입자에서 복제된 세 입자도 서로 다른 x_0에 도착합니다. 이 그림은 다시 뽑는 단계를 한 번으로 줄인 개념도입니다. 실제 Algorithm 1은 첫 단계부터 매 단계 다시 뽑고, 실험에서는 정해 둔 몇 단계에서만 다시 뽑습니다. 이제 이 절차가 어떤 분포를 근사하는지 보겠습니다.

## Slide 6 — Feynman-Kac 경로 분포
[6.title] Feynman-Kac 경로 분포
[6.message] FK 경로 분포는 기본 모델의 경로 확률에 지금까지의 potential을 모두 곱한 분포이고, 한 단계마다 전이 확률에 potential 하나를 곱해 만든다.
[6.body.0.symbols.0.1] $x_T$부터 $x_t$까지의 경로
[6.body.0.symbols.1.1] potential: 지금까지의 경로에 점수를 매기는 양수 함수
[6.body.0.symbols.2.1] 기본 모델의 한 단계 전이
[6.body.0.symbols.3.1] 정규화 상수
[6.notes.0] 이제 이론입니다. FK 경로 분포는 경로 전체에 대한 분포입니다. 식 3에서 x_{T:t}는 x_T부터 x_t까지 지금까지 지나온 경로입니다. 기본 모델이 이 경로를 만들 확률에, 지나온 단계마다 계산한 potential G를 모두 곱하고 정규화합니다. potential은 경로에 점수를 매기는 양수 함수이고, 보상이 높게 끝날 경로에 큰 값을 주도록 고릅니다.
[6.notes.1] 식 4는 같은 분포를 한 단계씩 쌓는 형태로 쓴 것입니다. 직전 단계의 FK 분포에, 기본 모델의 한 단계 전이 확률과 이번 단계의 potential을 곱합니다. 논문은 전이 확률과 potential의 곱을 기울인 전이 커널이라고 부릅니다. 즉 매 단계 기본 모델의 전이를 potential로 기울이는 셈입니다.
[6.notes.2] 참고로 논문의 식 3은 곱 안의 첨자가 G_t로 인쇄되어 있는데, 식 4와 맞추려면 G_s여야 해서 화면에서는 고쳐 적었습니다. 식 4도 원문은 정규화하지 않은 형태로 적혀 있어 비례 기호로 정리했습니다.

## Slide 7 — Potential 곱 조건과 목표 분포
[7.title] Potential 곱 조건과 목표 분포
[7.message] 경로 전체의 potential 곱이 최종 보상의 지수와 같으면, 마지막 단계의 FK 경로 분포에서 완성 표본만 보면 목표 분포가 된다.
[7.body.0.right.0.steps.0.title] Eq. 5를 Eq. 3에 대입
[7.body.0.right.0.steps.0.text] potential 곱 자리에 $\exp(\lambda r(x_0,c))$
[7.body.0.right.0.steps.1.title] 보상 항을 적분 밖으로
[7.body.0.right.0.steps.1.text] $x_0$와 $c$에만 의존한다
[7.body.0.right.0.steps.2.title] 중간 상태를 적분
[7.body.0.right.0.steps.2.text] 남은 $p_\theta(x_{T:0}\mid c)$가 $p_\theta(x_0\mid c)$가 된다
[7.body.1.text] Eq. 5를 만족하는 potential은 여러 개이고, 무엇을 고르느냐에 따라 필요한 입자 수가 달라진다
[7.notes.0] FK 틀의 핵심 조건이 식 5입니다. 경로 전체에 걸친 potential의 곱이 최종 보상의 지수, exp(람다 r(x_0))와 같아야 합니다.
[7.notes.1] 이 조건이 왜 목표 분포를 보장하는지 오른쪽 세 단계로 보겠습니다. 식 3의 마지막 단계, t가 0일 때 potential 곱 자리에 식 5를 넣습니다. 그러면 남는 보상 항은 x_0와 c에만 의존하므로, 중간 상태 x_T부터 x_1까지 적분할 때 밖으로 뺄 수 있습니다. 남은 기본 모델의 경로 확률을 중간 상태에 대해 적분하면 기본 모델의 x_0 분포가 됩니다. 결과는 식 2의 목표 분포입니다. 이 적분식은 논문 7쪽의 서술을 풀어 쓴 유도입니다.
[7.notes.2] 중요한 점은 이 조건을 만족하는 potential이 하나가 아니라는 것입니다. 곱만 맞으면 중간 단계에서 점수를 어떻게 나누어 주든 됩니다. 논문은 어떤 potential을 고르느냐에 따라 보상이 높은 표본을 얻는 데 필요한 입자 수가 달라진다고 씁니다.

## Slide 8 — SMC 가중치와 Algorithm 1
[8.title] SMC 가중치와 Algorithm 1
[8.message] SMC는 매 단계 입자를 가중치에 비례해 다시 뽑고, proposal로 다음 상태를 만든 뒤, 전이 확률비와 potential로 새 가중치를 매긴다.
[8.body.0.left.0.steps.0.text] 가중치 $G_t^i$에 비례해 부모 $k$개를 뽑는다
[8.body.0.left.0.steps.1.text] 부모마다 $\tau$로 $x_{t-1}^i$를 만든다
[8.body.0.left.0.steps.2.text] Eq. 7로 $G_{t-1}^i$를 계산한다
[8.body.0.left.0.steps.3.title] 반환
[8.body.0.left.0.steps.3.text] $t=0$에서 $G_0^i$를 계산한 뒤, 다시 뽑지 않고 $\{x_0^i\}$를 반환
[8.body.0.right.0.symbols.0.1] proposal: 실제로 다음 상태를 뽑는 분포. 가장 단순하게는 $p_\theta$ 자체
[8.body.0.right.0.symbols.1.1] 입자 $i$의 가중치
[8.body.0.right.0.symbols.2.1] 입자 수
[8.body.0.right.1.text] $k\to\infty$이면 입자의 경험분포가 $p_{\mathrm{target}}$으로 수렴한다
[8.notes.0] FK 경로 분포에서 직접 뽑을 수는 없으므로 입자 방법으로 근사합니다. 논문이 쓰는 것은 sequential Monte Carlo, SMC입니다. Algorithm 1은 매 단계 세 줄을 반복합니다. 먼저 Resample, 지금 가중치에 비례해 부모 k개를 뽑습니다. 다음 Propose, 부모마다 proposal 타우로 다음 상태를 만듭니다. 마지막 Re-weight, 새 상태의 가중치를 식 7로 계산합니다.
[8.notes.1] 식 7의 가중치는 두 부분입니다. 앞은 기본 모델의 전이 확률을 proposal의 확률로 나눈 비율로, proposal이 기본 모델과 다르게 뽑은 만큼을 보정합니다. proposal로 기본 모델 자체를 쓰면 이 비율은 1이고 가중치는 potential만 남습니다. 뒤는 이번 단계의 potential입니다. 원문 식 7은 등호로 적혀 있지만 정규화 상수의 비율이 빠져 있어 비례 기호로 적었습니다.
[8.notes.2] 설명용 가상 수치로 보겠습니다. proposal이 기본 모델이고, 입자 4개의 가중치가 1, 1, 2, 6이면 다시 뽑힐 확률은 0.1, 0.1, 0.2, 0.6입니다. 결과가 4, 3, 4, 4번이라면 4번 입자가 세 번 복제되어 각자 다음 상태를 만듭니다. 앞의 애니메이션이 이 장면입니다.
[8.notes.3] 논문은 입자 수 k가 무한대로 가면 입자의 경험분포가 목표 분포로 수렴한다고 Del Moral과 Miclo의 정리 3.19를 인용합니다. 한 가지 짚어 둘 것은 인쇄된 Algorithm 1의 끝입니다. t가 0일 때 가중치 G_0를 계산한 뒤 다시 뽑지 않고 표본을 그대로 반환합니다. 이 점은 토론에서 다시 다룹니다.

## Slide 9 — Difference·Max·Sum potential
[9.message] 같은 보상 이력에서도 potential이 최근 증가량, 지금까지의 최고값, 누적값 중 무엇을 보느냐에 따라 다시 뽑힐 입자가 달라진다.
[9.body.0.reveals] 같은 보상 이력에 potential만 바꾸면, 다시 뽑힐 확률이 가장 큰 입자가 A, B, C로 바뀐다.
[9.body.0.states.0.title] 최근 증가량
[9.body.0.states.0.text] 보상이 올라가는 입자를 높게 매긴다. $\lambda=1$일 때 예시 가중치는 A 1.82 · B 1.11 · C 1.00
[9.body.0.states.1.title] 지금까지의 최고값
[9.body.0.states.1.text] 보상이 가장 높았던 입자를 높게 매긴다. 예시 가중치는 A 2.23 · B 2.46 · C 1.82
[9.body.0.states.2.title] 누적값
[9.body.0.states.2.text] 보상을 꾸준히 쌓은 입자를 높게 매긴다. 예시 가중치는 A 2.72 · B 3.32 · C 6.05
[9.body.0.mediaCaption] 설명용 보상 이력 A·B·C. 단계 1이 먼저
[9.body.0.caption] Max와 Sum은 $G_0=\exp(\lambda r(x_0,c))\big(\prod_{t=1}^{T}G_t\big)^{-1}$로 곱을 맞춘다(Sec. 3.3)
[9.notes.0] 식 5를 만족하는 potential로 논문은 세 가지를 제안합니다. 모두 중간 보상 r_phi로 계산합니다. 중간 보상은 다음다음 슬라이드에서 다루고, 지금은 중간 상태에 매긴 점수라고 보시면 됩니다. 화면의 A, B, C는 설명용 가상 보상 이력이고, 세 번째 단계에서 다시 뽑는다고 하겠습니다.
[9.notes.1] [1] Difference는 직전 단계 대비 보상의 증가량을 봅니다. 마지막 단계에서 0.2에서 0.8로 오른 A가 가장 높습니다. 람다를 1로 두면 가중치는 A 1.82, B 1.11, C 1.00입니다. 인접한 단계의 항이 서로 지워지므로 곱이 최종 보상으로 모입니다. 다만 논문은 G_T를 1로 두는데, 그러면 시작 상태의 보상 항이 남습니다. 이 점은 토론에서 다룹니다.
[9.notes.2] [2] Max는 지금까지의 최고값을 봅니다. 처음에 0.9를 찍은 B가 가장 높습니다. 가중치는 A 2.23, B 2.46, C 1.82입니다.
[9.notes.3] [3] Sum은 누적값을 봅니다. 0.6을 세 번 쌓은 C가 1.8로 가장 높고, 가중치는 C 6.05입니다. Max와 Sum은 중간 단계의 곱이 최종 보상과 맞지 않으므로, 화면 아래 식처럼 마지막 G_0에서 그만큼을 나누어 곱을 맞춥니다. 논문은 보상의 상한이 있으면 Difference가 상한에 일찍 닿은 입자를 낮게 평가할 수 있고, 그때 Max가 나을 수 있다고 설명합니다.

## Slide 10 — Interval resampling과 ESS
[10.title] Interval resampling과 ESS
[10.message] 실험은 정해 둔 몇 단계에서만 다시 뽑고, 부록은 가중치가 한 입자에 얼마나 쏠렸는지를 ESS로 재서 다시 뽑을지 정한다고 적는다.
[10.body.0.left.0.caption] **Sec. 4.1** 이미지 실험: DDIM $T=100$, 일정 $\mathcal R=[0,20,40,60,80]$. $t\notin\mathcal R$이면 $G_t=1$
[10.body.0.left.1.items.0] Algorithm 1은 $t=T,\dots,1$의 매 단계에서 다시 뽑는다
[10.body.0.left.1.items.1] interval resampling은 $\mathcal R$의 시점에서만 다시 뽑고 계산을 줄인다
[10.body.0.right.0.symbols.0.1] 합이 1이 되게 정규화한 가중치
[10.body.0.right.0.symbols.1.0] 범위
[10.body.0.right.0.symbols.1.1] 가중치가 고르면 $k$, 한 입자에 몰리면 1
[10.body.0.right.1.text] App. C.3: $\mathrm{ESS}_t<k/2$이면 다시 뽑지 않는다
[10.notes.0] Algorithm 1은 매 단계 다시 뽑지만, 논문은 diffusion에서 인접한 두 단계의 상태가 크게 다르지 않으므로 몇 단계에서만 다시 뽑아도 된다고 봅니다. 정해 둔 시점 집합 R 밖에서는 potential을 1로 둡니다. 이미지 실험에서는 DDIM 100단계 중 80, 60, 40, 20, 0의 다섯 시점에서만 다시 뽑습니다. 논문은 이렇게 하면 탐색이 늘고 시간과 계산이 줄어든다고 씁니다.
[10.notes.1] 부록 C.3은 adaptive resampling도 적습니다. ESS, effective sample size는 정규화한 가중치의 제곱합의 역수입니다. 가중치가 고르면 k, 한 입자에 몰리면 1에 가깝습니다. 설명용 가상 수치로, 입자 4개의 가중치가 0.05, 0.05, 0.10, 0.80이면 ESS는 1.53입니다.
[10.notes.2] 부록은 ESS가 k의 절반보다 작으면 다시 뽑는 단계를 건너뛴다고 적습니다. 이 예라면 다시 뽑지 않습니다. 이 방향이 표준 SMC 교재와 같은지는 토론에서 보겠습니다.

## Slide 11 — 중간 보상 $r_\phi$를 얻는 세 방법
[11.title] 중간 보상 $r_\phi$를 얻는 세 방법
[11.message] 중간 보상은 현재 상태에서 추정한 완성 표본을 평가하거나, 완성 표본 여러 개를 뽑아 평가하거나, 중간 상태에서 최종 보상을 예측하도록 따로 학습해 얻는다.
[11.body.0.items.0.title] 추정한 완성 표본에서 평가
[11.body.0.items.0.text] $r_\phi(x_t,c)=r(\hat x_t,c)$. $\hat x_t$는 모델이 추정한 $\mathbb E[x_0\mid x_t]$. 이미지·텍스트 품질 실험의 기본값
[11.body.0.items.1.title] 여러 표본에서 평가
[11.body.0.items.1.text] $x_0^j\sim p_\theta(x_0\mid x_t,c)$를 $N$개 뽑아 $r_\phi=\log\frac1N\sum_j e^{r(x_0^j,c)}$. MDLM 독성 실험에서 $N$ = 4, 16
[11.body.0.items.2.title] 따로 학습
[11.body.0.items.2.text] noisy 상태 $x_t$에서 속성을 예측하는 분류기, 일반 보상이면 Eq. 8. SSD-LM 독성: 비독성 26K·독성 26K 문장, 시간 구간별 분류기 3개
[11.notes.0] potential은 모두 중간 보상 r_phi로 계산합니다. 이상적인 중간 보상은 지금 상태에서 출발했을 때 최종 보상이 어떻게 분포하는지 아는 것인데, 그러려면 모델의 표본으로 학습해야 합니다. 논문은 계산량과 정보량이 다른 세 가지를 제시합니다.
[11.notes.1] 첫째, 현재 상태에서 모델이 추정한 완성 표본 x̂_t에 기존 보상 모델을 그대로 적용합니다. 추가 비용은 보상 평가 한 번이고, 이미지와 텍스트 품질 실험은 모두 이 방법을 씁니다. 둘째, 현재 상태에서 완성 표본을 N개 뽑아 보상의 log-mean-exp를 씁니다. MDLM 독성 실험에서 N은 4와 16입니다. 셋째, 중간 상태에서 최종 보상을 예측하도록 따로 학습합니다. 보상이 분류기라면 noisy 상태에서 속성을 예측하는 분류기를 학습하고, 일반 보상이면 식 8처럼 exp(r)을 회귀합니다.
[11.notes.2] 식 8에서 제곱오차를 최소화하는 예측값은 조건부 평균입니다. 그래서 기본 모델이 forward 과정과 일치한다고 보면 r_phi는 log E[exp(r)]가 되고, 논문은 이 선택이 단계별 potential의 분산을 최소화하는 선택이라고 Chopin 등의 정리 10.1을 인용합니다. 실제 SSD-LM 독성 실험은 RoBERTa 분류기로 고른 비독성 2만 6천, 독성 2만 6천 문장을 노이즈 시점별로 세 구간에 나누어 분류기 세 개를 fine-tuning했습니다.

## Slide 12 — IS·TDS·SVDD와 FK steering의 선택
[12.title] IS·TDS·SVDD와 FK steering의 선택
[12.message] importance sampling, TDS, SVDD는 FK 틀에서 potential, proposal, 다시 뽑는 방식을 특정하게 고른 경우다.
[12.body.0.columns.0.label] 방법
[12.body.0.columns.3.label] 다시 뽑는 방식
[12.body.0.groups.0.rows.0.cells.2] 기본 모델
[12.body.0.groups.0.rows.0.cells.3] 끝에서 한 번
[12.body.0.groups.0.rows.1.cells.1] Difference ($\hat x_t$에서 평가)
[12.body.0.groups.0.rows.2.cells.2] 기본 모델
[12.body.0.groups.0.rows.2.cells.3] 매 단계 하나를 골라 $k$번 복제
[12.body.0.groups.0.rows.3.cells.0] FK 이미지 실험
[12.body.0.groups.0.rows.3.cells.1] Max ($\hat x_t$에서 IR)
[12.body.0.groups.0.rows.3.cells.2] 기본 모델
[12.body.0.groups.0.rows.3.cells.3] 5개 시점에서 SMC
[12.body.1.text] **App. C.2** TDS는 gradient를 쓰므로 미분 가능한 보상과 연속 상태가 필요하다. SVDD는 $\lambda\to\infty$에서 매 단계 best-of-$n$과 같다. 이산 상태에서는 $p_\theta G_t$를 정규화해 proposal로 쓸 수도 있다(App. C.1, Eq. 11)
[12.notes.0] 이 틀로 기존 방법을 다시 보면, 모두 세 가지 선택의 특정한 조합입니다. importance sampling은 중간 potential을 모두 1로 두고 마지막에만 exp(람다 r)을 주는 경우입니다. 끝에서 한 번만 고르므로 중간 정보를 쓰지 않습니다.
[12.notes.1] TDS는 예상 완성 표본에서 평가한 보상의 Difference potential을 쓰고, proposal로 classifier guidance를 씁니다. 그래서 보상이 미분 가능하고 상태가 연속이어야 합니다. SVDD도 Difference potential을 쓰지만 proposal은 기본 모델이고, 매 단계 k개 중 하나를 골라 k번 복제하는 nested importance sampling을 씁니다. 부록은 SVDD가 람다를 무한대로 보낸 목표를 쓰므로 매 단계 best-of-n과 같다고 설명합니다.
[12.notes.2] 마지막 행은 이 논문의 이미지 실험 설정입니다. Max potential, 예상 완성 표본에서 평가한 ImageReward, 기본 모델 proposal, 다섯 시점에서의 SMC입니다. 이산 상태 모델에서는 기본 전이에 potential을 곱해 정규화한 것을 proposal로 쓸 수도 있지만, 논문의 텍스트 실험도 proposal은 기본 모델입니다.

## Slide 13 — Text-to-image 결과: SDv2.1과 SDXL
[13.title] Text-to-image 결과: SDv2.1과 SDXL
[13.message] ImageReward로 steering한 SDv2.1(k = 4)의 최고 보상 표본은 GenEval에서 SDXL과 SDXL-DPO보다 높았고, HPS에서는 낮았다.
[13.body.0.left.0.columns.0.label] 모델 · sampler
[13.body.0.left.0.groups.0.rows.0.cells.0] 기본, $k=1$
[13.body.0.left.0.groups.1.rows.0.cells.0] 기본, $k=1$
[13.body.0.left.1.text] **Table 1** FK·BoN 행은 $k$개 중 최고 보상 표본. FK: $\lambda=10$, Max, 기본 모델 proposal, 일정 $[0,20,40,60,80]$, DDIM $T=100$. GenEval은 GenEval 프롬프트, IR·HPS는 ImageReward 프롬프트. 행 일부
[13.body.0.right.0.alt] Fig. 3의 앞 두 열. 첫 줄 SDXL 독립 표본, 둘째 줄 FK steering + SDXL, 셋째 줄 FK steering + SDv2.1. 왼쪽 열 프롬프트는 a photo of a black motorbike and a yellow bird, 오른쪽 열은 a photo of an orange cow and a purple sandwich. SDXL 독립 표본에는 노란 새가 없고 소와 샌드위치의 색이 바뀌어 있다. SDv2.1 + FK에서는 노란 새, 주황 소와 보라 샌드위치가 나온다.
[13.body.0.right.0.caption] **Fig. 3** 앞 두 열(행 라벨 유지). FK 두 행은 $k=4$의 최고 보상 표본
[13.notes.0] 결과입니다. 이미지 실험은 Stable Diffusion 계열을 ImageReward로 steering하고, 보상과 다른 프롬프트 세트로 GenEval을 잽니다. 표의 FK와 BoN 행은 k개 입자 중 보상이 가장 높은 표본의 성능입니다.
[13.notes.1] 0.8B인 SDv2.1에 FK steering을 k = 4로 쓰면 GenEval이 0.5104에서 0.6289로 오르고, 같은 k의 best-of-n 0.6172보다 높습니다. 2.6B인 SDXL의 0.5571, DPO로 fine-tuning한 SDXL의 0.5811보다도 높습니다. SDXL-DPO 대비 차이는 0.0478입니다. 다만 k = 3에서는 0.5987로 같은 모델의 best-of-n k = 4보다 낮습니다.
[13.notes.2] IR은 steering에 쓴 보상 모델 그 자체입니다. steering에 쓰지 않은 HPS에서는 SDv2.1 FK가 0.268로, SDXL의 0.289와 SDXL-DPO의 0.296보다 낮습니다. 논문은 미적 품질도 이겼다고 쓰지만, 지표마다 따로 읽어야 합니다.
[13.notes.3] 오른쪽 그림은 Fig. 3의 앞 두 열입니다. 오른쪽 열의 프롬프트는 주황색 소와 보라색 샌드위치입니다. 제가 그림에서 읽기로는, SDXL 독립 표본은 두 색을 바꿔 그렸고, SDv2.1에 FK를 쓴 표본은 주황색 소와 보라색 샌드위치를 그렸습니다. 왼쪽 열의 노란 새도 FK를 쓴 두 행에만 나옵니다. 저자가 고른 예시입니다.

## Slide 14 — 텍스트 품질: perplexity·CoLA·Dist
[14.title] 텍스트 품질: perplexity·CoLA·Dist
[14.message] SSD-LM과 MDLM 모두에서 FK steering은 같은 보상, 같은 입자 수의 best-of-n보다 perplexity가 낮았고, distinct n-gram은 조금 줄거나 같았다.
[14.body.0.left.0.columns.0.label] 모델 · sampler
[14.body.0.left.0.groups.0.rows.0.cells.0] 기본, $k=1$
[14.body.0.left.0.groups.0.label] SSD-LM (연속, 355M), GPT2 보상
[14.body.0.left.0.groups.1.rows.0.cells.0] 기본, $k=1$
[14.body.0.left.0.groups.1.label] MDLM (이산, 170M), trigram 보상
[14.body.0.right.1.text] **Table 4** 길이 50 문장, 3 seeds 평균. PPL은 GPT2-XL로 잼. FK: $\lambda=10$, Difference, 50번 다시 뽑기, 최고 점수 표본. 행 일부
[14.notes.0] 텍스트 diffusion에서도 같은 틀을 씁니다. SSD-LM은 연속 상태, MDLM은 이산 상태 모델이고, 둘 다 proposal은 기본 모델입니다. SSD-LM은 GPT2 perplexity를, MDLM은 trigram 언어 모델 perplexity를 보상으로 쓴 행을 골랐습니다. 평가 perplexity는 GPT2-XL로 잽니다.
[14.notes.1] 같은 입자 수 4의 best-of-n과 비교하면 perplexity가 SSD-LM에서 2.6, MDLM에서 11.8 낮습니다. MDLM은 이산 상태이고 trigram 보상은 미분하지 않으므로 gradient guidance로는 할 수 없는 경우입니다. distinct n-gram은 두 모델 모두 best-of-n보다 조금 낮거나 같습니다.
[14.notes.2] 한 가지 주의할 점이 있습니다. 본문 4.1절은 MDLM의 trigram 결과를 perplexity 79.2에서 37.2로, CoLA 30.0에서 35.3으로 적었는데, 표 4에는 85.3에서 40.3, 28.9에서 37.0으로 되어 있습니다. 화면은 표 4를 따랐습니다.

## Slide 15 — Gradient proposal의 비용
[15.title] Gradient proposal의 비용
[15.message] SDv1.5에서 FK proposal에 ImageReward gradient를 더하면 GenEval은 0.02 오르고 시간은 8.1초에서 55초로 늘었다.
[15.body.0.left.0.columns.4.label] 시간
[15.body.0.left.0.groups.0.rows.0.cells.0] 기본, $k=1$
[15.body.0.left.0.groups.0.rows.0.cells.4] 2.4초
[15.body.0.left.0.groups.0.rows.1.cells.4] 20초
[15.body.0.left.0.groups.0.rows.2.cells.4] 8.1초
[15.body.0.left.0.groups.0.rows.3.cells.4] 55초
[15.body.0.left.1.text] **Table 3** 보상은 ImageReward
[15.body.0.left.2.columns.0.label] Table 8 · 시간
[15.body.0.left.2.columns.1.label] 기본 $k=1$
[15.body.0.left.2.columns.3.label] FK $k=4$, 2장 병렬
[15.body.0.left.2.groups.0.rows.0.cells.1] 2.4초
[15.body.0.left.2.groups.0.rows.0.cells.2] 8.1초
[15.body.0.left.2.groups.0.rows.0.cells.3] 5.0초
[15.body.0.left.2.groups.0.rows.1.cells.1] 4.6초
[15.body.0.left.2.groups.0.rows.1.cells.2] 17.4초
[15.body.0.left.2.groups.0.rows.1.cells.3] 9.1초
[15.body.0.left.2.groups.0.rows.2.cells.1] 11.5초
[15.body.0.left.2.groups.0.rows.2.cells.2] 43.5초
[15.body.0.left.2.groups.0.rows.2.cells.3] 21.7초
[15.body.0.left.3.text] **Table 8** A100 1장 기준, 마지막 열은 2장 병렬 구현
[15.body.0.right.0.symbols.0.1] 기본 모델 Gaussian 전이의 평균과 분산
[15.body.0.right.0.symbols.1.1] 중간 보상의 gradient. 평균만 옮긴다
[15.body.0.right.1.items.1.label] 시간
[15.body.0.right.1.items.1.small] 같은 두 행
[15.notes.0] proposal 선택의 효과입니다. 보상이 미분 가능하고 상태가 연속이면 proposal로 gradient guidance를 쓸 수 있습니다. 식 10처럼 기본 전이의 평균을 중간 보상의 gradient 방향으로 옮기고 분산은 그대로 둡니다. 기본 모델과 다르게 뽑은 만큼은 식 7의 전이 확률비가 보정합니다.
[15.notes.1] SDv1.5에서 gradient guidance만 쓰면 GenEval이 0.45, 시간 20초입니다. FK steering을 k = 4로 쓰면 gradient 없이 0.54, 8.1초입니다. 여기에 gradient proposal을 더하면 0.56으로 0.02 오르지만 시간은 55초로 46.9초 늘어납니다.
[15.notes.2] 아래 표 8은 시간의 조건입니다. A100 한 장에서 FK k = 4는 기본 생성보다 3.4배에서 3.8배 걸리고, 두 장으로 병렬화하면 줄어듭니다. 표 3의 2.4초와 8.1초는 표 8의 한 장 기준 값과 같고, GenEval 0.44와 0.54는 표 1의 값을 소수 둘째 자리에서 자른 값과 같습니다. gradient 행의 람다와 장비 조건은 표 3에 적혀 있지 않습니다.

## Slide 16 — Potential 비교: 입자 평균 GenEval
[16.title] Potential 비교: 입자 평균 GenEval
[16.message] ImageReward, λ = 10, 같은 일정에서 Max potential은 네 모델과 두 입자 수 모두에서 입자 평균 GenEval이 가장 높았다.
[16.body.0.left.1.text] **Table 5** 모든 입자의 평균 GenEval. ImageReward($[-2,2]$), $\lambda=10$, 일정 $[0,20,40,60,80]$
[16.body.0.right.0.items.0] Difference: 보상 상한 2에 일찍 닿은 입자는 이후 증가량이 0이라 낮게 매겨질 수 있다
[16.body.0.right.0.items.1] Max: 같은 $\lambda$, 같은 입자 수에서 입자 다양성은 Difference보다 낮다
[16.body.0.right.0.items.2] Sum: 작은 모델에서 가장 낮다
[16.notes.0] 이제 potential 선택의 효과입니다. 표 5는 앞의 표 1과 달리 모든 입자의 평균 GenEval입니다. ImageReward, 람다 10, 같은 다시 뽑기 일정에서 potential만 바꿨습니다.
[16.notes.1] Max가 네 모델과 두 입자 수 모두에서 가장 높습니다. SDv2.1에서 Max와 Difference의 차이는 k = 4에서 0.038, k = 8에서 0.020입니다. 논문의 설명은 이렇습니다. ImageReward는 -2에서 2 사이이므로, 생성 초반에 상한 2에 닿은 입자는 그 뒤 증가량이 0이 되어 Difference에서 낮게 매겨질 수 있습니다.
[16.notes.2] 반면 Max는 높은 점수의 입자를 더 강하게 고르기 때문에, 같은 람다와 입자 수에서 입자 다양성이 Difference보다 낮다고 논문은 씁니다. 다양성은 19번 슬라이드에서 그림으로 보겠습니다.

## Slide 17 — 텍스트 독성: 중간 보상의 질
[17.title] 텍스트 독성: 중간 보상의 질
[17.message] 독성 제어에서는 중간 보상을 학습하거나 평가 표본을 늘린 쪽이 같은 입자 수에서 독성 판정 비율이 더 높았다.
[17.body.0.left.0.alt] Fig. 5. 왼쪽: 세 이미지 모델에서 x̂_t로 잰 ImageReward와 최종 ImageReward의 상관이 추론 진행에 따라 0에서 1로 오른다. 오른쪽: SSD-LM에서 기존 독성 분류기(실선)와 학습한 보상(점선)의 상관. 진행 0.2에서 학습한 보상은 약 0.4, 기존 분류기는 약 0.17이다.
[17.body.0.left.0.caption] **Fig. 5** 중간 보상과 최종 보상의 상관. 왼쪽: 이미지(ImageReward). 오른쪽: SSD-LM 독성, 학습한 보상(점선)이 진행 초반에 더 높다(곡선 근거)
[17.body.0.right.0.columns.1.label] SSD-LM 독성
[17.body.0.right.0.columns.3.label] MDLM 독성
[17.body.0.right.0.groups.0.rows.0.cells.0] 기본 ($k=1$)
[17.body.0.right.0.groups.0.rows.2.cells.0] FK, 기본 $r_\phi$
[17.body.0.right.0.groups.0.rows.3.cells.0] FK, 개선한 $r_\phi$
[17.body.0.right.1.text] **Table 6** 독성은 steering에 쓰지 않은 holdout 분류기(XLM-R) 기준, PPL은 GPT2-XL. FK: $\lambda=10$, Difference, 기본 모델 proposal, 3 seeds 평균. 기본 $r_\phi$는 SSD-LM이 $\hat x_t$에서 평가, MDLM이 $N=4$. 개선한 $r_\phi$는 SSD-LM이 학습한 분류기, MDLM이 $N=16$
[17.notes.0] 중간 보상의 질을 보는 실험입니다. 과제는 기본 모델에서 드물게 나오는 독성 문장을 생성하는 것으로, 논문은 red-teaming 용도라고 설명합니다. 기본 SSD-LM에서 독성 판정은 0.4%, MDLM은 0.3%입니다.
[17.notes.1] 왼쪽 Fig. 5는 중간 보상이 최종 보상을 얼마나 잘 예측하는지입니다. 이미지에서는 예상 완성 이미지로 잰 ImageReward의 상관이 비교적 빨리 오릅니다. 텍스트 독성에서는 기존 분류기를 그대로 쓰면 초반 상관이 낮고, 학습한 보상이 더 높습니다. 곡선에서 읽은 것입니다.
[17.notes.2] 표 6은 steering에 쓰지 않은 holdout 분류기로 잰 독성 비율입니다. 입자 8개 기준으로, SSD-LM에서 기존 분류기를 그대로 쓰면 29.7%, 학습한 보상을 쓰면 38.0%입니다. MDLM에서 평가 표본 수 N을 4에서 16으로 늘리면 48.3%에서 51.7%입니다. 같은 입자 수의 best-of-n은 8.1%와 10.8%입니다. 논문 요약의 64.7%는 steering에 쓴 분류기로 잰 값이고, 별도 분류기로는 51.7%입니다.
[17.notes.3] 참고로 4.3절 끝 문단은 학습한 보상의 독성 비율을 22.3%라고 적었는데, 이 값은 표 6의 gradient guidance 행입니다. 학습한 보상 행은 k = 4에서 15.2%, k = 8에서 39.0%입니다. MDLM의 중간 보상 계산도 4.3절과 부록 B.2의 서술이 조금 다릅니다.

## Slide 18 — ImageNet: 학습한 $r_\phi$와 potential
[18.title] ImageNet: 학습한 $r_\phi$와 potential
[18.message] ImageNet 클래스 조건 생성에서는 noisy 상태로 학습한 분류기를 쓴 행이, 추정한 완성 이미지에서 평가한 행보다 목표 클래스 확률이 높았다.
[18.body.0.left.0.columns.0.label] 중간 보상 $r_\phi$
[18.body.0.left.0.columns.2.label] 평균
[18.body.0.left.0.columns.3.label] 최대
[18.body.0.left.0.groups.0.rows.0.cells.0] $\hat x_t$에서 평가 (TDS)
[18.body.0.left.0.groups.0.rows.1.cells.0] $\hat x_t$에서 평가
[18.body.0.left.0.groups.0.rows.2.cells.0] noisy 상태로 학습
[18.body.0.left.0.groups.0.rows.3.cells.0] noisy 상태로 학습
[18.body.0.left.1.text] **Table 7** 목표 클래스 확률 $p(y\mid x_0)$. ImageNet 1,000 클래스, 256×256, marginal diffusion, $k=4$, gradient guidance proposal. 학습한 분류기는 potential과 proposal 모두에 쓰임
[18.body.0.right.0.items.0.small] 평균, 학습 − $\hat x_t$
[18.body.0.right.0.items.1.small] 평균, 학습 − $\hat x_t$
[18.notes.0] 이미지 쪽 중간 보상 실험입니다. 클래스 조건 없이 학습한 diffusion 모델로 1,000개 클래스 중 하나를 생성하고, 보상은 분류기의 log 확률입니다. proposal로 gradient guidance를 씁니다. 첫 행은 TDS의 선택과 같습니다.
[18.notes.1] noisy 상태에서 학습한 분류기를 쓰면 목표 클래스 확률의 평균이 0.88로, 예상 완성 이미지에서 기존 분류기를 쓴 행보다 Difference에서 0.29, Max에서 0.23 높습니다. potential 차이는 작고, 기존 분류기 행끼리는 Max가 평균 0.06 높지만 최댓값은 0.02 낮습니다.
[18.notes.2] 해석할 때 두 가지를 주의합니다. 학습한 분류기는 potential과 gradient proposal 양쪽에 함께 들어가므로, 이 차이는 두 변경을 합친 효과입니다. 그리고 평가는 표에 보고된 목표 클래스 확률 하나이고, 별도 분류기나 FID는 없습니다.

## Slide 19 — $\lambda$·potential과 입자 다양성
[19.title] $\lambda$·potential과 입자 다양성
[19.message] λ를 키우거나 Max potential을 쓰면 입자들이 비슷한 이미지로 모이고, 입자 평균 점수는 대체로 오르지만 항상 오르지는 않는다.
[19.body.0.reveals] 같은 프롬프트에서 λ를 키울 때와 potential을 Max로 바꿀 때, 입자들의 구도가 얼마나 비슷해지는지 큰 그림으로 비교한다.
[19.body.0.states.0.label] $\lambda$ 비교
[19.body.0.states.0.alt] Fig. 6. 맨 위는 기본 모델의 독립 표본 4개로 구도와 표지판 모양이 제각각이다. 아래 세 줄은 λ = 2, 4, 10의 FK 입자 4개. λ = 2에서는 두 쌍이 같은 구도이고, λ = 10에서는 네 장 모두 붉은 들판 가운데 초록 정지 표지판이다.
[19.body.0.states.0.text] 맨 위는 독립 표본 4개. $\lambda$가 클수록 네 입자의 구도가 같아진다. SDXL, Max, $k=4$
[19.body.0.states.1.alt] Fig. 7. 맨 위는 독립 표본 8개. 아래 두 줄은 λ = 2, k = 8의 Difference와 Max 입자. Max 줄은 길 끝의 정지 표지판 구도가 반복되고, Difference 줄은 배경과 구도가 더 다양하다.
[19.body.0.states.1.text] 맨 위는 독립 표본 8개. Max 줄이 Difference 줄보다 구도가 더 비슷하다
[19.body.0.mediaCaption] **Fig. 6 · 7** 프롬프트 a green stop sign in a red field. SDXL, ImageReward, App. C.3의 adaptive resampling 사용
[19.body.0.side.0.groups.0.rows.0.cells.0] 독립 표본
[19.body.0.side.1.text] **Table 9** 입자 평균. Difference, 일정 이름은 표 표기 그대로. 행 일부
[19.notes.0] 다양성의 대가입니다. [1] Fig. 6은 SDXL에서 Max potential로 람다를 2, 4, 10으로 바꾼 입자 4개입니다. 맨 위 독립 표본은 구도가 제각각인데, 람다가 커질수록 네 입자의 구도가 같아지고 람다 10에서는 거의 같은 그림입니다. 같은 부모에서 복제된 입자들이기 때문입니다.
[19.notes.1] [2] Fig. 7은 람다 2, 입자 8개에서 Difference와 Max입니다. Max 줄은 길 끝의 표지판 구도가 반복되고, Difference 줄은 더 다양합니다. 앞 슬라이드의 설명과 맞습니다.
[19.notes.2] 오른쪽 표 9는 SDv1.4의 입자 평균입니다. 독립 표본의 CLIP 다양성 0.3158이 람다 10에서 0.1050까지 줄고, GenEval은 0.4408에서 0.5258로 오릅니다. 다만 항상 오르지는 않습니다. SDv2.1의 5-30-5 일정에서는 람다 2의 GenEval 0.5607이 람다 10의 0.5523보다 높고, 표 10의 SDv1.4에서 람다 1의 최고 IR 0.763은 독립 표본 4개의 최고 IR 0.800보다 낮습니다.
[19.notes.3] 한계도 함께 말씀드립니다. 논문 5절은 이 방법이 강한 보상 함수가 있어야 쓸 수 있다는 점을 한계로 듭니다. 그리고 부록 A는 이 표들이 Difference potential이라고 적는데, 표 10의 람다 10 행의 최고 IR 0.927, 1.006, 1.298은 Max로 적힌 표 1의 값과 같습니다. 어느 설정의 값인지는 확인이 필요합니다.

## Slide 20 — 정리와 토론
[20.title] 정리와 토론
[20.message] potential의 곱 조건이 목표 분포를 정하고, 유한한 입자로 얻은 실험 결과는 반환 규칙, 평가 지표, 계산 조건을 함께 봐야 해석할 수 있다.
[20.body.0.groups.0.heading] 정리
[20.body.0.groups.0.items.0] potential의 곱이 $\exp(\lambda r(x_0))$이면 FK 경로 분포의 $x_0$는 목표 분포를 따른다(Eq. 5)
[20.body.0.groups.0.items.1] 유한한 $k$에서의 성능은 proposal, potential, 중간 보상을 무엇으로 고르느냐에 달렸다
[20.body.0.groups.0.items.2] Table 1의 네 모델 모두에서 FK($k=4$)의 GenEval이 같은 $k$의 best-of-$n$보다 높았고, fine-tuning 모델이 있는 세 모델에서는 그 모델보다도 높았다(최고 보상 표본 기준)
[20.body.0.groups.1.heading] 토론
[20.body.0.groups.1.items.0] Sec. 4.1의 '11.5초 대 9.1초'는 SDXL $k=1$(A100 1장)과 SDv2.1 FK $k=4$(A100 2장 병렬)의 비교다. 1장이면 17.4초다. 같은 장비로 맞추면 속도 주장은 어떻게 되는가?
[20.body.0.groups.1.items.1] Table 1의 FK 값은 4개 중 최고 보상 표본이고, IR은 steering에 쓴 보상 모델이다. 쓰지 않은 HPS에서는 SDv2.1 FK 0.268, SDXL-DPO 0.296이다. 목표 분포를 잘 근사했는지는 무엇으로 재야 하는가?
[20.body.0.groups.1.items.2.text] Difference의 $G_T=1$이면 곱에 $-\lambda r_\phi(x_T)$ 항이 남고, Algorithm 1은 $G_0$를 계산하고도 다시 뽑지 않는다. App. C.3의 ESS 규칙은 표준 SMC와 방향이 반대다. 실제 실험 코드는 어느 쪽인가?
[20.body.0.groups.1.items.3.text] 입자 수 $k$, 입자당 표본 $N$, 분류기 학습은 서로 다른 곳에 계산을 쓰고, 논문은 같은 계산량으로 맞춘 비교를 하지 않았다. 다시 뽑을 때마다 입자들이 서로를 기다리는 비용은 어떻게 볼까?
[20.notes.0] 정리하겠습니다. potential의 곱이 최종 보상의 지수와 같으면 FK 경로 분포의 완성 표본은 목표 분포를 따릅니다. 이 조건을 만족하는 potential은 여러 개이고, 입자 수가 유한할 때 성능은 proposal, potential, 중간 보상을 무엇으로 고르느냐에 달려 있습니다. 실험에서는 표 1의 네 모델 모두에서 입자 4개의 FK steering이 같은 입자 수의 best-of-n보다 GenEval이 높았고, fine-tuning 모델이 있는 세 모델에서는 그 모델보다도 높았습니다. 최고 보상 표본 기준입니다.
[20.notes.1] 토론할 점 네 가지를 준비했습니다. 첫째는 속도 비교입니다. 4.1절의 11.5초 대 9.1초는 A100 한 장의 SDXL 기본 생성과 두 장으로 병렬화한 SDv2.1 FK steering의 비교입니다. 한 장이면 17.4초입니다. 덧붙여 Fig. 2 오른쪽의 FLOPs 축은 10의 14승 단위로 적혀 있지만, 입자 수가 두 배가 될 때 점 간격이 약 0.30으로 log 10의 2와 같아 로그 척도로 보입니다.
[20.notes.2] 둘째는 무엇을 쟀느냐입니다. 표 1의 FK 값은 네 입자 중 최고 보상 표본이고, IR은 steering에 쓴 보상 모델 그 자체입니다. 쓰지 않은 HPS에서는 순서가 바뀝니다. 이론이 말하는 것은 목표 분포의 근사인데, 최고 보상 표본 하나의 점수로 그것을 잴 수 있는지 의견을 듣고 싶습니다.
[20.notes.3] 셋째는 인쇄된 절차와 식 5의 관계이고, 제 해석이 들어간 항목입니다. Difference를 G_T = 1로 두고 곱하면 시작 상태의 보상 항이 남아 식 5와 정확히 맞지 않습니다. Algorithm 1은 마지막 가중치 G_0를 계산하지만 그 가중치로 다시 뽑거나 함께 반환하지 않으므로, Max와 Sum의 보정이 출력에 어떻게 반영되는지 알 수 없습니다. 또 부록 C.3은 ESS가 k/2보다 작으면 다시 뽑지 않는다고 적었는데, Naesseth 등의 SMC 교재 2.2.2절은 ESS가 절반 아래로 떨어질 때만 다시 뽑는다고 설명합니다. 방향이 반대입니다. 실험 코드가 어느 쪽인지는 확인이 필요합니다.
[20.notes.4] 넷째는 계산을 어디에 쓰느냐입니다. 입자를 늘리는 것, 입자당 평가 표본을 늘리는 것, 분류기를 학습하는 것은 서로 다른 곳에 계산을 씁니다. 논문은 이를 trade-off라고만 적고 같은 계산량으로 맞춘 비교는 하지 않았습니다. 또 다시 뽑을 때마다 입자들이 서로의 점수를 기다려야 하므로 병렬 구현이 필요합니다. 이것도 절차에서 끌어낸 제 해석입니다.

## Slide 21 — 감사합니다
[21.title] 감사합니다
[21.links.1] 코드 · github.com/zacharyhorvitz/Fk-Diffusion-Steering
[21.notes.0] 들어 주셔서 감사합니다. 특히 식 5의 보장과 실제 반환 절차의 관계, 그리고 같은 계산량에서의 비교를 어떻게 설계하면 좋을지 의견을 듣고 싶습니다.

