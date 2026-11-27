# 검토 기록 (fk-steering, outline.md → outline_v2.md)

비평가(agy, `critic.md`)와 검증자(agy, `verify.md`)는 서로의 결과를 보지 않고 따로 돌았다. 자료조사는 `research_verified.md`에서 출처를 열어 확인한 것만 쓴다.
진행자가 직접 확인한 것: Fig. 2 오른쪽 확대(400 dpi), Table 9·10(p. 22) 렌더링, Fig. 6·7(pp. 26–27), Naesseth et al. §2.2.2 원문.

## 진행자가 직접 확인한 사실
- **Fig. 2 오른쪽의 x축은 로그 척도로 읽힌다.** SDv1.4 점의 x 좌표가 약 15.83, 16.13, 16.31, 16.43, 16.73, 17.03(k = 1, 2, 3, 4, 8, 16). 간격 0.30·0.18·0.12·0.30·0.30은 log10(2)·log10(1.5)·log10(4/3)·log10(2)·log10(2)와 맞는다. 라벨은 `FLOPs (×10^14)`. 검증자 V10과 같은 결론.
- **Table 10의 λ = 10, 20-80-20 행의 IR 최댓값(0.927, 1.006, 1.298)이 Table 1의 FK(k = 4) IR과 소수 셋째 자리까지 같다.** Table 1은 Max potential(§4.1), App. A는 "Here we use the difference potential"이라고 쓴다. HPS 최댓값(0.259, 0.266, 0.297)은 Table 1(0.263, 0.268, 0.302)과 다르다. 검증자 V15와 같은 관찰.
- Table 9의 schedule 이름(5-30-5, 20-80-20)은 App. A 본문의 일정([0,20,40,60,80], [0,70,75,80,85,90])과 이름이 맞지 않는다. 대본에서 표 표기 그대로 쓰고 대응은 말하지 않는다.
- Naesseth et al. §2.2.2(31쪽): ESS가 N/2 아래로 떨어질 때만 재추출하고, 임계값보다 크면 재추출을 건너뛰며 이전 가중치를 이어 받는다. App. C.3은 "If ESS_t < k/2, then we skip the resampling step" — 방향이 반대다(external, 토론).
- §4.3 'Better Rewards vs. More Particles'의 "learned reward's toxicity rate of 22.3%"는 Table 6의 SSD-LM(∇ guidance) 행 값이다. learned r_φ 행은 k = 4에서 15.2%, k = 8에서 39.0%.

## 비평가
| ID | 판정 | 처리 |
|---|---|---|
| C1 animation이 빈 무대에서 시작, 기호 선행 노출, diagram 병기 | 채택 | beat 0 = Fig. 1 가운데의 best-of-n 독립 경로(4번의 대조군). ① 중간 단계에서 점수 → ② 낮은 경로 끊김·높은 경로 복제 → ③ 복제된 부모에서 갈라져 x_0까지. 3 beat, 4개 정지점. 화면 문구는 말로("중간 보상", "재추출"), G_t·τ·Eq. 5는 6–8번에서 처음 정의. diagram 병기 삭제 |
| C2 toggle 조작 방식, G_T·G_0 문제 | 일부 채택 | toggle 유지(숫자 키·버튼으로 상태 선택, 클리커 다음 키는 슬라이드를 넘김 — "순환" 문구 삭제), `print: expand`. 가상 궤적 A·B·C에 λ = 1을 넣은 가중치 수치 예를 대본에. G_T = 1과 G_0 보정의 문제는 토론 3번으로 |
| C3 14·18·19 과밀 | 채택 | 14번에서 Fig. 2 제외(아래 V10), 18번을 텍스트 독성(Fig. 5 + Table 6)과 ImageNet(Table 7) 두 장으로 분리, 19번의 Fig. 6·7은 전체 폭 이미지 toggle(2상태) + Table 9·10 발췌 |
| C4 이론과 실험의 거리, 보상 = 평가 지표 | 채택 | 8번에 Algorithm 1이 t = 0에서 G_0을 계산하고 재추출 없이 반환함을 명시. 토론 2번에 "최고 보상 입자 + 조향 보상(IR)으로 평가"와 HPS 역전(SDv2.1 FK 0.268 < SDXL-DPO 0.296) |
| C5 연속 split·equation, 13번 cards | 채택 | 13번은 table(IS · TDS · SVDD · 이 논문의 이미지 설정; 열: potential / proposal / 선택 방식 / 적용 범위). 방법 구간의 레이아웃을 장마다 바꿈(equation 단독 valign center, split 비율 변화, process, table, toggle) |
| C6 기호 정의 순서 | 채택 | 4번에서 p_θ, x_t, k, r, λ 정의. 가중치 기호는 논문의 G_t^i로 통일(W 제거). 9번(proposal) 독립 슬라이드를 없애고 Eq. 10은 gradient proposal 결과 슬라이드에, Eq. 11은 대본에만 |
| C7 토론 시간, 장부 정합 | 채택 | 20번 120 s. Table 8은 gradient proposal 슬라이드에 시간 발췌 표로 올려 use. Algorithm 1은 8번 use |
| C8 steering/조향 혼용, '반복 다양성' | 채택 | 전체 "steering". 텍스트 슬라이드 제목은 "텍스트 품질: perplexity·CoLA·Dist" |
| C9 빠진 근거 | 일부 채택 | ① Chopin et al. 정리 10.1(분산 최소화) 언급과 실제 학습 r_φ가 분류기 fine-tuning(App. B.2: 26K+26K, 3개 시간 구간)임을 11번에 ② 텍스트 슬라이드에 MDLM 행(기본 / FK Trigram / BoN Trigram) 추가 ③ Fig. 5 두 패널 모두 ④ SDv2.1 k = 1 행 추가 ⑤ 4번·10번 대본에 수치 예 |

## 검증자
| ID | 판정 | 처리 |
|---|---|---|
| V1 Algorithm 1과 interval resampling | 채택 | 10번에 "Algorithm 1은 매 단계, interval resampling은 R의 시점에서만" 명시. Fig. 4 cut 사유에 오른쪽 분포 패널 포함 |
| V2 4번의 "반환할 수 없다" | 채택 | "고보상 표본이 p_θ에서 드물어 저보상 표본에 계산이 쓰이고 많은 입자가 필요하다(§1, §3.2–3.3)"로. Chatterjee & Diaconis의 exp(KL) 표본 수는 대본에서 external로 |
| V3 animation과 Algorithm 1 | 채택 | 캡션: "Fig. 1을 바탕으로 다시 그림. 재추출 시점을 한 번으로 줄인 개념도". 대본에 실제 Algorithm 1의 재추출 시점 |
| V4–V7 식을 고쳐 적음 | 채택 | 화면은 논문 식의 기호를 지키되 정규화 형태로 적은 곳은 대본에 "다시 적은 식"이라고 밝힌다. Eq. 3 곱 안의 G_t → G_s, Eq. 7의 = → ∝, Eq. 10의 I_d. 7번의 주변화 전개는 "p. 7 서술을 풀어 쓴 유도". 8번 일관성은 논문 문장 그대로(k → ∞에서 입자 경험분포가 p_target으로 수렴, Del Moral & Miclo 정리 3.19), 지지집합 조건 삭제 |
| V8 Difference의 G_T = 1 | 채택 | 화면에 G_T = 1을 논문 표기로 두고, 토론 3번(해석 표시): 곱이 exp(λ[r(x_0) − r_φ(x_T)])가 되어 Eq. 5와 어긋난다 |
| V9 learned r_φ의 실제 형태 | 채택 | 11번: 분류기 p_φ(y \| x_t) 학습(실험에서 사용)과 일반 보상의 Eq. 8 |
| V10 Fig. 2 축 | 채택 | 직접 확인(위). Fig. 2는 cut: 왼쪽은 Table 1의 최고 입자 GenEval을 k별로 다시 보인 것, 오른쪽은 축 라벨과 점 간격이 맞지 않아 그대로 보이면 계산량을 잘못 읽게 된다. 대본과 토론 1번 보조 문장에서 언급 |
| V11 HPS 역전, Fig. 3 발췌 | 채택 | 13번 table에 HPS 열 유지, 대본과 토론 2번. Fig. 3은 2열(orange cow, purple sandwich) 세 행 전체 |
| V12 CoLA 불일치 | 채택 | 텍스트 슬라이드 대본 |
| V13 Table 3 절사 | 채택 | 대본: "Table 1 값을 소수 둘째 자리에서 자른 값" |
| V14 MDLM 집계, Fig. 5 곡선 근거, Table 7 단일 분류기 | 채택 | 대본·캡션 |
| V15 Table 9·10 potential 표기 | 채택 | 19번 대본, 토론 2번의 보조 문장 |
| V16 Fig. 6·7 adaptive resampling | 채택 | 19번 캡션 |
| V17 코드 링크 | 채택 | arXiv 초록이 거는 주소(research_verified 3) |

## 토론 (정리와 함께 한 장, 4개)
1. 근거 · 시간 비교: §4.1 "11.5s versus 9.1s" — 11.5 s는 SDXL k = 1(A100 1장), 9.1 s는 SDv2.1 FK k = 4의 A100 2장 병렬. 1장이면 17.4 s(Table 8).
2. 근거 · 무엇을 쟀나: Table 1의 FK 값은 k개 중 최고 보상 입자, IR은 steering에 쓴 보상과 같은 모델. 조향하지 않은 HPS에서는 SDv2.1 FK 0.268 < SDXL-DPO 0.296. Table 10의 IR 최댓값은 Table 1과 같지만 App. A는 Difference potential이라고 적는다.
3. 근거(해석 표시) · 인쇄된 절차와 Eq. 5: Difference의 G_T = 1이면 곱이 exp(λ[r(x_0) − r_φ(x_T)]); Algorithm 1은 t = 0에서 G_0을 계산하고 재추출 없이 반환해 Max·Sum의 G_0 보정이 출력에 반영되지 않는다; App. C.3의 ESS 규칙은 표준(Naesseth et al. §2.2.2, external)과 반대 방향.
4. 대가(해석) · 계산을 어디에 쓰나: 입자 수 k, 입자당 표본 N, 학습한 r_φ(분류기 fine-tuning, 독성 26K+26K 문장, 시간 구간별 3개)는 서로 다른 곳에 계산을 쓴다. 논문은 같은 계산 예산으로 맞춘 비교를 하지 않았다(§4.3 마지막 문단이 trade-off라고만 적음). 또 입자들이 재추출 때마다 서로를 기다리므로 병렬 구현이 필요하다(Table 8의 parallel 열).

## 목표 구조 (21장, 1200 s)
| # | section | 제목(안) | 블록 | 시간 |
|---|---|---|---|---|
| 1 | — | 표지 | cover (Fig. 1 오른쪽 크롭) | 30 |
| 2 | summary | FK steering 요약 | statement: lead + cards 3 | 60 |
| 3 | background | Diffusion steering의 연구 갈래 | table(갈래 · 대표 방법 · 필요한 것 · 한계) + callout 질문 | 50 |
| 4 | background | 목표 분포와 importance sampling | split: equation(Eq. 2, 기호) / compare(IS · BoN) | 70 |
| 5 | background | 입자를 중간에 고르는 FK steering | animation (3 beat, signature) | 70 |
| 6 | method | Feynman-Kac 경로 분포 | equation(Eq. 3–4) + symbols, valign center | 65 |
| 7 | method | Potential 곱 조건과 목표 분포 | split: equation(Eq. 5, 주변화) / process 3 | 60 |
| 8 | method | SMC 가중치와 Algorithm 1 | split: process(Resample·Propose·Re-weight) / equation(Eq. 7) + callout(일관성) | 75 |
| 9 | method | Difference·Max·Sum potential | toggle 3상태(가상 궤적 SVG) + equation | 70 |
| 10 | method | Interval resampling과 ESS | split: diagram(T = 100 시간축, 재추출 시점) / equation(Eq. 13) | 50 |
| 11 | method | 중간 보상 r_φ를 얻는 세 방법 | cards 3 + equation(Eq. 8) | 60 |
| 12 | method | IS·TDS·SVDD를 FK 선택으로 | table | 55 |
| 13 | results | Text-to-image: Table 1 | split: table(SDv2.1 k=1·BoN·FK k=3·k=4, SDXL k=1, SDXL-DPO) / figure Fig. 3 열 | 55 |
| 14 | results | 텍스트 품질: PPL·CoLA·Dist | table(SSD-LM, MDLM 발췌) + deltas | 45 |
| 15 | analysis | Gradient proposal의 비용 | split: table(Table 3) + table(Table 8 발췌) / equation(Eq. 10) | 50 |
| 16 | analysis | Potential 비교: GenEval 입자 평균 | table(Table 5, focus Max) | 45 |
| 17 | analysis | 텍스트 독성: 중간 보상의 질 | split: figure Fig. 5 / table Table 6 발췌 | 55 |
| 18 | analysis | ImageNet: 학습한 r_φ와 potential | table(Table 7) + deltas | 45 |
| 19 | analysis | λ·potential과 입자 다양성 | toggle 2상태(Fig. 6 / Fig. 7 이미지) + table(Table 9·10 발췌) | 55 |
| 20 | discussion | 정리와 토론 | statement: 정리 3 + 토론 4 | 120 |
| 21 | — | 감사합니다 | ending | 15 |

인터랙션 3장(5 animation·signature, 9 toggle, 19 toggle) ≤ ⌊21 × 0.2⌋ = 4.
장부: Fig. 1 use 5(표지에도), Fig. 2 cut(위 V10), Fig. 3 use 13, Fig. 4 cut(입자 평균 스케일링 곡선과 분포; 입자 평균 비교는 Table 5로), Fig. 5 use 17, Table 1 use 13, Table 2 cut(fine-tuned 모델 위 steering, 줄기 밖), Table 3 use 15, Table 4 use 14, Table 5 use 16, Table 6 use 17, Table 7 use 18, Algorithm 1 use 8, Table 8 use 15, Table 9·10 use 19, Fig. 6·7 use 19, Fig. 8·9 cut, Table 11 cut.
