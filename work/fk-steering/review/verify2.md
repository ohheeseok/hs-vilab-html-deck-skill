[W1] must · meta.figures(Table 10 `cut`) · "Table 9와 같은 설정을 steering 보상(ImageReward)으로 잰 표. 수치는 19번 대본과 토론 2번 대본에서 인용" · Table 10(p. 22)은 ImageReward뿐 아니라 HPS와 Mean/Max를 함께 보고하고 SDv1.5가 없으며 $\lambda=1.0$(Table 9는 $\lambda=2$)·ImageReward 프롬프트를 쓴다. 또한 19번 대본은 수치 없이 언급만 했고, 20번 토론 2 대본에는 Table 10 언급이 없다. · "SDv1.4·SDv2.1·SDXL에서 $\lambda=1,10$과 일정별 ImageReward·HPS(평균/최고)·CLIP-Div를 보고한 표. 표 1과의 일치 여부만 19번 대본에서 언급"

[W2] should · meta.figures(Fig. 1 `use`, Fig. 2 `cut`) · Fig. 1 `use: 5`, Fig. 2 `cut`에 "왼쪽은 Table 1의 최고 보상 표본 GenEval을 k별로 다시 그린 것" · Fig. 1은 1번 표지에도 사용된다. Fig. 2 왼쪽(p. 3)은 Table 1(p. 10)에 없는 $k=2,8,12,16$과 타 모델 $k=3$ 결과를 포함한다. · Fig. 1 `use: [1, 5]`; Fig. 2 `cut`: "왼쪽은 $k=2$–16의 최고 보상 표본 GenEval 비교로, 대표 비교는 Table 1의 $k=3,4$로 다룬다…"

[W3] should · 슬라이드 2(body 카드 2·notes[1]) · "proposal, potential, 중간 보상을 각각 고른다. TDS와 SVDD는 이 선택지를 조합하는 두 가지 예다" · Abstract·Sec. 1(p. 3)·App. C.2(p. 24)에서 FK 틀의 선택지는 potential·중간 보상·샘플러(proposal 및 재추출 알고리즘)이며, SVDD는 SMC 대신 nested importance sampling을 쓴다. · "proposal, potential, 중간 보상, 재추출 방식을 각각 고른다. TDS와 SVDD는 이 선택을 조합한 예다"

[W4] must · 슬라이드 3(body 표 3행·notes[0]) · 입자 기반 행에 `best-of-n, TDS, SVDD`를 `필요한 것: 표본 여러 개`, `제약: best-of-n은 최종 보상이 낮은 표본도 끝까지 생성`으로만 적고, 세 갈래로 평면화하며 `verbatim` 표기 · Sec. 2(p. 5)에서 TDS는 classifier guidance를 써 보상 gradient·미분 가능한 보상·연속 상태가 필요하고, SVDD는 매 단계 한 상태를 $k$번 복제해 다양성이 줄어든다. Sec. 1–2(pp. 2, 4)의 분류는 (1) fine-tuning과 (2) inference-time(gradient·입자)의 2단이다. · 제약 칸에 "best-of-$n$은 완성 후 선택, TDS는 보상 gradient·연속 상태 필요, SVDD는 단일 상태 복제로 다양성 감소"를 넣고, 대본에서 추론 시점 방법의 두 하위 갈래임을 명시

[W5] should · 슬라이드 4(notes[2]) · "기본 모델에서 확률 1%인 사건에 보상 1을 주겠습니다. 람다가 10이면… 99.55%… 표본 4개를 뽑아… 3.94%" · 나머지 99% 사건의 보상 값($r=0$)이 빠져 목표 확률이 정의되지 않으며, 3.94%의 독립 표본 조건도 생략됐다(해당 전제하에 99.55%·3.94% 계산은 정확). · "…사건에 보상 1, 나머지에 0을 주면 람다가 10일 때 99.55%입니다. 그런데 독립 표본 4개를 뽑아…"

[W6] should · 슬라이드 5(beats[1]–[2]·notes[1]–[2]) · "막대 길이가 중간 보상을 나타낸다" 직후 "점수에 비례하는 확률로 입자 4개를 다시 뽑는다" · Fig. 1 캡션(p. 2)·Sec. 3.3(p. 7)에서 재추출 확률은 중간 보상 $r_\phi$ 자체가 아니라 그로 정의한 potential $G_t$(예: $\exp(\lambda r_\phi)$)에 비례한다($r_\phi$는 음수도 가능). · "막대 길이가 중간 보상으로 계산한 점수(potential)를 나타낸다"

[W7] should · 슬라이드 10(notes[0])·12(body 표 4행·notes[2]) · 10번 "DDIM 100단계 중 다섯 시점에서만 다시 뽑습니다", 12번 "FK 이미지 실험 | … | SMC에서 5개 시점에만 다시 뽑기" · Sec. 4.1(p. 9)의 일정 $[0,20,40,60,80]$에서 $t=0$은 종단 단계이므로 8·20번의 "Algorithm 1은 $t=0$에서 다시 뽑지 않는다"와 충돌한다(중간 재추출 4회). 또한 해당 설정은 Sec. 4.3 ImageNet(gradient proposal)을 제외한 Sec. 4.1 text-to-image 기본 설정이다. · 10번 "일정 $[0,20,40,60,80]$에서 중간 4개 시점에 다시 뽑고 $t=0$에서 종단 평가합니다", 12번 "FK text-to-image(Sec. 4.1) | … | 일정 $[0,20,40,60,80]$의 interval resampling"

[W8] must · 슬라이드 11(body 카드 1·3, notes[1]) · 카드 3에서 "noisy 상태 $x_t$에서… 분류기를 학습한다… SSD-LM 독성 실험은… 분류기 3개를 학습했다", 카드 1·대본에서 "품질 실험은 모두 이 방법($\hat x_t$ 1회 평가)" · App. B.2(p. 23)에서 SSD-LM 독성 분류기 3개는 noisy $x_t$가 아니라 **추정 완성 텍스트 $\hat x_t$**로 기존 분류기를 fine-tuning했다(noisy $x_t$ 학습은 Sec. 4.3 ImageNet). 또 App. B.2(p. 22)는 MDLM 기본에서 $\hat x_t$로부터 4개 텍스트를 뽑아 보상을 평균낸다고 적는다(Sec. 4.1 p. 11 표기와 차이). · 카드 3 "SSD-LM 독성 실험은 $x_t$에서 추정한 $\hat x_t$로 기존 분류기 3개를 시간 구간별 fine-tuning했다", 대본에 MDLM의 App. B.2 기본 4표본 평균을 병기

[W9] must · 슬라이드 13(figure.alt·notes[2]) · `alt` "SDXL 독립 표본에는… 소와 샌드위치의 색이 바뀌어 있다. SDv2.1 + FK에서는 노란 새, 주황 소와 보라 샌드위치가 나온다", `notes[2]` "소와 샌드위치의 색을 바꿔 그렸고" · Fig. 3(p. 4)에서 SDXL 독립 표본(1행 2열)은 흰·갈색 소와 일반 햄버거이고 배경벽만 보라색이다(두 색 지정 실패이지 색 교환 아님). SDv2.1 + FK(3행 1열)는 **노란 오토바이**이며 노란 새가 없다(검은 오토바이와 노란 새는 2행 1열 SDXL + FK). · `alt` "SDXL 독립 표본은 노란 새가 없고 소·샌드위치의 두 색을 모두 구현하지 못했다(배경만 보라색). SDXL + FK는 노란 새와 주황 소를, SDv2.1 + FK는 주황 소와 보라 샌드위치를 구현했다(1열은 노란 오토바이)" 및 `notes[2]` 동일 수정

[W10] must · 슬라이드 15(Eq. 10·notes, Table 3 캡션) · Eq. (10)에 $\tau=$와 공분산 $I_d$를 보완해 `provenance`에만 `I_d 보완`이라 적고 대본에 미고지; Table 3 캡션은 `보상은 ImageReward`만 표기 · App. C.1 Eq. (10)(p. 23) 원문은 $\mathcal{N}(\mu_\theta(x_t,c)+\sigma_\theta^2\lambda\nabla_{x_t}r_\phi(x_t,c),\sigma_\theta^2)$이다($I_d$ 생략, $p_\theta(x_t|x_{t+1},c)$ 문맥과 $x_t$ 첨자 혼재). Table 3(p. 11)의 `FK(k=4)` IR·HPS는 Table 1의 최고 보상 표본과 일치하나 집계 방식과 프롬프트 세트(GenEval/IR)가 표에 미명시됐다. · 대본에 "원문 식 10의 공분산 $\sigma_\theta^2$에 $I_d$를 보완했고 원문의 $x_t$ 첨자는 유지했습니다"를 추가하고, Table 3 캡션에 "GenEval·ImageReward 각 프롬프트, FK 행 IR·HPS는 Table 1 최고 보상 표본과 일치" 보완

[W11] should · 슬라이드 16(body bullets[1]) · "Max: 같은 $\lambda$, 같은 입자 수에서 입자 다양성은 Difference보다 낮다" · Sec. 4.2(p. 12)는 App. D 정성 사례를 근거로 "낮을 수 있다(can lead to lower particle diversity)"고 서술하며, Table 5(p. 14)에는 다양성 측정치가 없다. · "Max: 같은 $\lambda$, 같은 입자 수에서 입자 다양성이 Difference보다 낮을 수 있다(App. D 사례)"

[W12] should · 슬라이드 17(body 표·캡션·provenance·notes[2]) · (a) 두 `PPL ↓` 열에 굵게 표시 없음, (b) 캡션에 집계 방식 누락 및 `provenance`가 "행 일부"만 표기, (c) `notes[2]` "논문 요약의 64.7%" · Table 6(p. 14)의 보인 행 중 최저 PPL은 SSD-LM `23.0`(BoN), MDLM `74.3`(FK 기본 $r_\phi$)이다. Sec. 4.3(p. 13)→Sec. 4.1(p. 11) 기준 $t=0$ 최고 점수 표본을 반환하며, 표는 steering 열·Dist 열을 생략하고 두 모델을 병렬 재배열했다. `64.7%`는 Abstract가 아니라 Sec. 1 기여 요약(p. 4)·Sec. 4.3(p. 14)의 MDLM($k=8,N=16$) 값이다. · `**23.0**`·`**74.3**` 굵게 표시, 캡션에 "최고 점수 표본"·`provenance`에 "열 일부·재배열" 추가, 대본을 "1절 기여 요약(p. 4)의 MDLM 64.7%"로 수정

[W13] should · 슬라이드 18(Table 7 캡션·notes) · $\lambda$ 값과 `평균`/`최대` 집계 대상 미언급 · Sec. 4.3·Table 7(pp. 14–15)에는 ImageNet 비교의 $\lambda$가 미기재이고 `p(y|x_0) Mean (Max)`만 제시된다. · 캡션에 "$\lambda$ 미기재; 표 원문의 Mean (Max)" 추가

[W14] should · 슬라이드 19(Table 9 캡션·notes[0]) · Table 9 캡션에 보상 모델 누락; `notes[0]` "같은 부모에서 복제된 입자들이기 때문입니다" · App. A(p. 21)에서 Table 9의 보상은 ImageReward다. Fig. 6(p. 26)에는 입자 계보가 제시되지 않아 동일 부모 복제는 발표자의 추론이다. · Table 9 캡션에 "ImageReward 보상" 추가, `notes[0]`을 "같은 부모에서 복제됐을 가능성이 큽니다"로 완화

[W15] should · 슬라이드 20(토론 3 본문) · "Difference에서 $G_T=1$이면 곱에 $-\lambda r_\phi(x_T)$가 남고" · Sec. 3.3(p. 7) 정의의 곱은 $\exp(\lambda[r_\phi(x_0,c)-r_\phi(x_T,c)])$이므로 곱의 **지수**에 $-\lambda r_\phi(x_T)$(곱의 인수로는 $\exp(-\lambda r_\phi(x_T))$)가 남으며 $r_\phi(x_0,c)=r(x_0,c)$ 전제가 필요하다. · "Difference에서 $G_T=1$이면 곱의 지수에 $-\lambda r_\phi(x_T)$가 남고"

확인됨: 1, 6, 7, 8, 9, 14, 21
