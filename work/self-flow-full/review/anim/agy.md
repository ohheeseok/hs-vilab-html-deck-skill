비평가 관점에서 Self-Flow 덱의 overview 애니메이션 구상을 검토한 결과다. 엔진 규칙은 전제로 두고, 논문에 없는 주장·수치는 쓰지 않는다.

---

## 1. 후보 (가)·(나)·(다) 비평과 권고안

1. **`[must]` 후보 (가) 원안은 "저자 가설의 사실화"와 "구간당 사건 과적"을 안고 있다.**
   - 근거: [context.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/context.md#L47-L51), [paper.txt §3.3](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/paper.txt#L309-L315), [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/animation.md#L92-L93), [deck.json S16·S20](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/deck.json#L1486)
   - **청중이 얻는 것**: 외부 encoder를 모델 자신의 EMA 사본으로 교체하는 구조 변화(연속적 교체 = 애니메이션이 성립하는 조건)와, 입력 비대칭($\tau$ vs $\tau_{\min}$) + 층간 정렬($l < k$)을 한 그림에서 연결해 볼 수 있다. REPA 세미나를 들은 청중은 대비를 즉시 알아본다.
   - **청중이 잃는 것 / 논거 결함**:
     - 원안은 Sec. 3.3의 `"can often be solved by local correlations alone"`을 Beat 0 전제로 넣었다. 이는 논문이 직접 측정하지 않은 동기 진술이며, 덱 자신이 16장([deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/deck.json#L1486))과 20장 토론 3번([deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/deck.json#L1711))에서 "cross-token 추론이 실제 원인인가"를 따진다. REPA 논의([repa_anim_log.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/repa_anim_log.md#L12))에서 "뒤 층은 세부를 맡는다"는 저자 가설을 뺀 것과 같은 이유로, 이 해석을 그림·라벨의 사실처럼 넣으면 안 된다.
     - 원안의 4번째 단계("두 noise 혼합 + teacher 더 깨끗함 + $l < k$ 정렬 선")는 **서로 다른 두 영역의 사건**(왼쪽 입력 분리 + 중앙 층간 연결)을 한 구간에 몰아넣어 `한 구간에 사건 하나` 규칙을 깬다. 반대로 이를 모두 쪼개면 Vanilla부터 시작해 6정지점이 되어 3–5 beat 상한([context.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/context.md#L13))을 넘긴다.
     - 외부 encoder 제거 직후 바로 Self-Flow로 넘어가면, 이미 EMA teacher와 층간 정렬을 쓰는 SRA([paper.txt §2](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/paper.txt#L170-L175), [App. A.5](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/paper.txt#L1829-L1834))와 Self-Flow의 차이(Dual-Timestep 입력 비대칭)가 흐려진다.
   - **기존 장과의 겹침**: 3장 표(방법 4개 분류)와는 역할이 다르지만, 8장 Fig. 3([shots/s08.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/shots/s08.png))과 전체 배치가 겹칠 위험이 크다. 단, Fig. 3은 $f_\theta, f_{\theta'}$를 내부 구조 없는 네모 상자로만 그려 $l < k$ 깊이 위치를 보이지 못하므로, overview가 **외부 encoder 교체 + 깊이 막대($0.3D \to 0.7D$)**에 집중하고 수식·하이퍼파라미터·`sg`·projection(10M)을 8장에 넘기면 겹침을 통제할 수 있다.

2. **`[must]` 후보 (나) "토큰 격자"는 6장 signature toggle·7장 격자·8장 Fig. 3과 정면 충돌하므로 기각한다.**
   - 근거: [context.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/context.md#L52-L53), [shots/s06-vanilla.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/shots/s06-vanilla.png), [shots/s06-dual.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/shots/s06-dual.png), [shots/s07.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/shots/s07.png), [fig/fig3.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/fig/fig3.png)
   - **청중이 얻는 것**: 토큰별 noise 배정($\tau$ vs $\tau_{\min}$)의 직관은 빠르다.
   - **청중이 잃는 것 / 논거 결함**:
     - 현재 6장(`signature: true`)과 7장이 이미 똑같은 6×6 앵무새 토큰 격자(`tok_vanilla.jpg`, `tok_dual.jpg` — 36칸 중 9칸 주황)를 연속으로 쓰고, 8장 Fig. 3도 5×5 고양이 격자를 쓴다. Overview까지 6×6 격자로 만들면 청중은 **같은 격자 도식을 4장 연속** 보게 되어 6장 대표 상호작용의 가치를 스스로 갉아먹는다.
     - 논문의 출발점인 **"외부 encoder 제거"**(Sec. 1, Sec. 3.2)와 **네트워크 깊이 방향 정렬**($l < k$, Sec. 3.4, App. H)이 완전히 빠진다.
     - 두 입력 격자 사이에 feature 정렬 화살표를 직접 그으면, 실제 latent 중간층 feature 정렬($h_\theta^{(l)}$ ↔ $f_{\theta'}^{(k)}$)이 입력 픽셀/패치 복원처럼 오독된다.

3. **`[must]` 후보 (다) "한 메커니즘, 세 모달리티"는 목차형 지도이고 논문 구현 사실을 단순화 과장하므로 기각한다.**
   - 근거: [context.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/context.md#L54-L55), [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/animation.md#L18-L21), [repa_anim_log.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/repa_anim_log.md#L12), [paper.txt App. A.3·B·C·D](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/paper.txt#L1794)
   - **청중이 얻는 것**: 모달리티 범용성(이미지·비디오·오디오)을 초반에 환기한다.
   - **청중이 잃는 것 / 논거 결함**:
     - `animation.md`와 `repa_anim_log.md`가 명시적으로 기각한 **목차형 지도/나열**에 해당한다. "연속적 형태 변화가 곧 논문의 기전"인 경우가 아니다.
     - **사실 과장 위험**: 논문은 세 모달리티에 완전히 동일한 파이프라인을 쓰지 않는다. 모달리티별 전용 AE(SD-VAE/FLUX.2, Wan2.2, Songbloom)와 공유 backbone의 **모달리티별 입출력 projection 층**([paper.txt App. D](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/paper.txt#L2158-L2161))을 따로 두고, mini-batch도 단일 모달리티로 구성한다([App. D](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/paper.txt#L2162)). 또한 $R_M$(0.25 / 0.10 / 0.50, [App. A.3](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/paper.txt#L1794)), 비디오 5% low-SNR 별도 샘플링([App. C](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/paper.txt#L1980-L1982)), 오디오 `trainshift` 1.0([App. B](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/paper.txt#L1868-L1869)) 등 모달리티별 조건이 다르다. 이를 한 상자로 합쳐 움직이면 18–20장의 비판적 토론과 충돌한다.
     - 5장 토큰 규격 표([shots/s05.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/shots/s05.png))·12장 공유 backbone과 겹치면서 정작 Self-Flow가 **어떻게** 표현을 배우는지(Dual-Timestep + EMA)를 보여주지 못한다.

4. **`[must]` 권고안: "수정 (가) — 외부 encoder 정렬(REPA)에서 시작해 EMA teacher 교체 → Dual-Timestep 입력 분리 → 두 질문"의 4-beat 구성.**
   - 근거: [shots/s04.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/shots/s04.png), [paper.txt §3.2–3.4](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/paper.txt#L292-L417)
   - 핵심 수정은 두 가지다. ① **Beat 0을 Vanilla가 아니라 외부 정렬(REPA)로 잡는다.** 바로 앞 4장(Fig. 2a)이 REPA 외부 encoder의 병목을 보였으므로 자연스럽게 이어지고, 정지점을 4개로 줄이면서도 구간당 사건 1개를 지킨다. ② **저자 가설("local correlations", "깨끗한 토큰으로 추론")을 그림·텍스트에서 완전히 배제**하고, 오직 구조적 사실(외부 encoder 제거, EMA 사본 $0.3D \to 0.7D$, 입력 noise 비대칭 $\tau$ vs $\tau_{\min}$)만 그린다.

---

## 2. 권고안의 Beat 구성, 끝 그림, 옆 글, 위치

5. **`[must]` 위치: 현재 4장(`외부 encoder 크기와 생성 FID`) 뒤, 5장(`Rectified flow와 토큰 규격`) 앞 — 새 5장(`배경` 섹션의 마지막 장).**
   - 근거: [deck.json S3–S5](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/deck.json#L200-L467), [repa_example/s04-step3.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/repa_example/s04-step3.png)
   - 3장과 4장 사이(새 4장)에 넣으면 overview에서 이미 외부 encoder를 걷어낸 뒤, 다음 장(구 4장 Fig. 2a)에서 다시 외부 encoder 실패 이야기로 되돌아가는 역행이 생긴다. 4장(외부 encoder 병목, `배경`) 직후, 5장(방법 시작, `방법`) 직전에 두어야 `배경(3–5장)` → `방법(6–9장)` 흐름이 매끄럽다.

6. **`[must]` Beat 구성: 총 4개 정지점(3회 전환), `side: "below"` 4열. 모든 중간 정지점이 논문 사실과 모순되지 않도록 순서를 잡는다.**
   - 근거: [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/animation.md#L78-L99), [paper.txt §3.3–3.4, §4.4, App. A.3, App. H](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/paper.txt#L352-L417)
   - **주의할 함정**: Beat 1에서 외부 encoder만 EMA teacher로 바꾸면서 위쪽 입력에 "깨끗한 이미지"를 남겨 두면, EMA flow 모델이 clean pixel을 받는다는 **거짓 중간 상태**가 화면에 정지한다. 따라서 Beat 1에서 외부 encoder 경로 전체(`깨끗한 입력 → 고정 외부 encoder → 목표`)가 `균일 noise latent → EMA teacher`로 한 번에 연쇄 교체되어야 한다([animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/animation.md#L92-L93)의 허용된 단일 연쇄 사건). 이 상태는 실제로 논문 §2·§4.4의 "masking 없는 내부 층간 정렬(SRA·w/o masking)"에 대응하므로 발표자가 "외부 모델만 없앤 상태"로 정확히 짚고 Beat 2(Dual-Timestep)로 넘어갈 수 있다.

   | Beat | 화면 사건 (1구간 1사건, 권장 1.2–1.4초) | 옆 글 제목 (`side: "below"`) | 옆 글 문장 (개조식·명사형) |
   |---|---|---|---|
   | **0 (정지 진입)** | 기준선(회색 계통): 아래 `균일 noise → Flow 모델(앞 0.3D · 뒤 0.7D) → velocity`, 위 `깨끗한 입력 → 고정 외부 encoder → 표현 목표`. 아래 `0.3D`에서 위로 수직 정렬 선(회색). 왼쪽 두 입력 사이에 주황 마커 `입력이 다름`(pixel vs latent). | **외부 정렬 (REPA)** | 고정 외부 encoder의 표현에 모델 중간층을 맞추는 기준 구조 |
   | **1 (전환 1)** | 위 행의 외부 encoder 경로(`깨끗한 입력 → 외부 encoder → 표현 목표`)와 수직 정렬 선·`입력이 다름` 라벨이 사라지고, 아래 모델과 **같은 길이**의 `EMA teacher (깊이 D · sg)` 막대가 위 행에 들어온다(입력은 아직 균일 noise, 아래→위 `EMA` 점선). 정렬 선(하늘색)이 아래 `0.3D`에서 위 `0.7D`로 꺾여 그려진다(`학습 때만`). | **EMA teacher로 교체** | 외부 encoder를 모델의 EMA 사본으로 바꾸고 `0.3D → 0.7D` 정렬 |
   | **2 (전환 2)** | **왼쪽 입력 열만 변화**: 아래 student 입력 아이콘이 일부 토큰의 noise가 더 높은 **두 timestep 혼합($x_\tau$)**으로 바뀌고, 위 teacher 입력 아이콘이 더 낮은 **단일 timestep($x_{\tau_{\min}}$)**으로 맑아진다. 두 입력 사이에 주황 양방향 화살표와 `입력 noise 차이` 라벨이 순서대로 등장한다. | **Dual-Timestep 입력** | student는 두 timestep 혼합, teacher는 더 낮은 단일 timestep 입력 |
   | **3 (전환 3)** | 위쪽 주황 브래킷 **①**과 아래쪽 주황 브래킷 **②**가 안착한다. | **두 질문** | ① 왜 작동하고 근거는 어디까지인가 ② 모달리티·크기별 이득은 |

7. **`[should]` 끝 그림(`figures/overview_selfflow.svg`, Beat 3 완성 도식)의 모양과 캡션.**
   - 근거: [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/animation.md#L50-L54), [paper.txt §3.4, App. A.3, App. H](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/paper.txt#L1790-L1793)
   - **위 행 (EMA teacher)**: 왼쪽에 추상 4×4 latent 토큰 타일(균일하고 연한 noise, 라벨 `단일 $\tau_{\min}$ 입력`) → 화살표 → student와 **같은 폭**의 가로 막대(`0.7D` 지점에서 분할: 앞 구간 연한 하늘색/테두리 `0.7D`, 뒤 구간 흐린 구조색 0.35 opacity — `0.7D` 출력만 정렬에 쓰임을 표시). 막대 아래 `EMA teacher · sg` 표시, 아래 행에서 올라가는 짧은 점선 화살표 `EMA`.
   - **아래 행 (Student)**: 왼쪽에 추상 4×4 latent 토큰 타일(12칸 연함 + 4칸 진한 회색/주황 테두리 = $R_M=0.25$ 비유, 라벨 `두 timestep $\tau$ 입력`) → 화살표 → 가로 막대(`0.3D` 구간 하늘색 면/테두리, 나머지 `0.7D` 구간 남색 `var(--color-text-heading)`) → 화살표 → `velocity 예측` 상자.
   - **중앙 연결선**: 아래 `0.3D` 끝점(하늘색 점)에서 오른쪽 위로 꺾여 위 `0.7D` 끝점으로 연결되는 5px 하늘색 선 + 라벨 `0.3D → 0.7D 정렬 · 학습 때만`.
   - **왼쪽 마커**: 두 입력 타일 사이 주황(`--color-warm`) 양방향 화살표 + `입력 noise 차이`.
   - **두 질문 브래킷**: 위 브래킷(입력~`0.7D` 정렬선 상단) `① 두 timestep과 EMA 정렬은 왜 작동하나`, 아래 브래킷(student 후반부~velocity 하단) `② 모달리티·크기를 키워도 이득이 남나`.
   - **캡션**: `Sec. 3.3–3.4와 Fig. 3을 바탕으로 그림. 막대 길이는 전체 층 수 D에 비례(예: SiT-XL 28층에서 l=8, k=20, App. A.3·H). 수치·성능은 결과 장에서 다룬다.`
   - **슬라이드 제목 제안**: `외부 encoder 없이 Self-Flow가 정렬하는 법` (22자, 한 줄 기준 22–26자 충족, 결론 선고 금지 규칙 준수).

---

## 3. 상호작용 예산, 적정 추가 장 수, 1200초 배분

8. **`[must]` 추가 장 수는 반드시 1장(총 22장)이어야 한다. 2장 추가(23장)는 예산 초과이며 기존 toggle 축소는 주객전도다.**
   - 근거: [interaction-rules.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/interaction-rules.md#L10-L12), [context.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/context.md#L38-L40), [design-system-deck.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/design-system-deck.md#L42-L44), [repa_anim_log.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/repa_anim_log.md#L10)
   - **예산 계산**: 현재 21장, 상호작용 3개(6·14·15장 toggle).
     - **1장 추가 → 22장**: 상한 $\lfloor 22 \times 0.2 \rfloor = 4$, 실제 $3 + 1 = 4$ (통과).
     - **2장 추가 → 23장**: 상한 $\lfloor 23 \times 0.2 \rfloor = 4$, 실제 $3 + 2 = 5$ (빌드 게이트 실패).
   - **기존 toggle 중 정적 전환 가능한 것이 없다**:
     - 6장(`schedulers`): `signature: true` 대표 상호작용. 제거 불가.
     - 14장(`qualitative`): Fig. 9·10a·10b 세 정성 비교를 나란히 놓으면 1024×768 프로젝터 판독 불가([design-system-deck.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/design-system-deck.md#L42-L44) 금지 사항).
     - 15장(`scaling`): Fig. 6(a)·(b) 각각 8개 곡선 범례를 가진 그래프다. 정적으로 나란히 줄이면 범례 판독 규칙 위반이다([design-system-deck.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/design-system-deck.md#L42)).
   - **내용상으로도 1장이 맞다**: RAE는 "잠재공간 교체"와 "고차원 생성 수정 4곳"이라는 두 축이 따로 있었지만, Self-Flow는 REPA와 마찬가지로 단일 학습 프레임워크(Dual-Timestep + EMA self-distillation)가 핵심이다. 두 번째 애니메이션을 억지로 만들면 6–7장(격자)이나 5장(모달리티 표)을 반복하게 된다.

9. **`[must]` 1200초(20분) 유지 방안: 새 overview에 55초를 배정하고, 설명 부담이 줄어드는 6개 장에서 정확히 55초를 감축한다.**
   - 근거: [context.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/context.md#L35), [repa_anim_log.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/repa_anim_log.md#L14)
   - 결과(구 9–14장)·분석(구 15–19장)의 시간은 건드리지 않고, overview가 앞단에서 구조를 미리 풀어줌으로써 중복 설명이 줄어드는 장에서만 덜어낸다.

   | 장 (현 번호 → 새 번호) | 기존 시간 | 조정 시간 | 증감 | 근거 |
   |---|---:|---:|---:|---|
   | 2 → 2 (`tldr`) | 45초 | 40초 | −5초 | overview가 직후 구조를 시각 설명하므로 요약 문장 압축 |
   | 3 → 3 (`background`) | 60초 | 50초 | −10초 | Self-Flow 구두 상세 설명과 발표 질문을 overview로 이관 |
   | 4 → 4 (`encoder-scaling`) | 50초 | 45초 | −5초 | 단일 그래프 + 3개 불릿, 45초로 충분 |
   | **(신규) → 5 (`overview`)** | — | **55초** | **+55초** | 4 beat × ~13초 (REPA overview 55초와 동일) |
   | 6 → 7 (`schedulers` toggle) | 80초 | 70초 | −10초 | Dual-Timestep 기본 개념을 이미 봤으므로 Fig. 2(b) 4자 비교에 집중 |
   | 8 → 9 (`teacher`, Fig. 3) | 75초 | 60초 | −15초 | 전체 구조 재설명 생략, 식 6·7(`cosine`, `sg`, $\gamma=0.8$)과 설정값만 설명 |
   | 20 → 21 (`discussion`) | 105초 | 95초 | −10초 | 정리 3항목 요약 축소, 토론 4항목 비중 유지 (REPA 120→110초와 동일) |
   | **합계 (21장 → 22장)** | **1200초** | **1200초** | **0초** | 20분 정확히 유지 |

---

## 4. REPA overview 시각 문법 계승의 득실

10. **`[should]` REPA 시각 문법(막대, 정렬 선, 두 질문)을 이어 쓰는 것이 득이 훨씬 크다. 다만 "동일 문법"을 "동일 도형 복사"로 착각하면 Self-Flow의 구조적 차이를 지워 버린다.**
    - 근거: [repa_example/overview_repa.svg](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/repa_example/overview_repa.svg#L1-L77), [repa_example/s04-step3.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/repa_example/s04-step3.png), [animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/animation.md#L96-L99)
    - **득**: ① REPA 발표를 이미 들은 청중이 Beat 0에서 시각 문법을 재학습할 필요가 없고, Beat 1에서 DINOv2가 사라지며 같은 길이의 EMA 막대가 들어오는 순간 "외부 encoder 제거 + 깊이 비대칭($l < k$)"이 즉각 대비된다. ② 논문 Fig. 3의 네모 상자가 숨기는 층 깊이 정보($0.3D \to 0.7D$)를 막대 비례로 드러낸다. ③ "어디서"와 "얼마나"를 분리해 수치 과적을 막는다.
    - **실(위험)**: ① REPA의 SiT-XL/2 28층 특화 표기를 그대로 가져오면 Self-Flow의 주력 실험(FLUX.2 21층, scaling 8/14/21/28층)과 어긋난다. ② 끝 그림의 실루엣이 REPA와 너무 비슷하면 청중이 "위 행이 외부 encoder가 아니라 자기 복제본"임을 놓칠 수 있다.

11. **`[must]` 그대로 가져올 것 vs 가져오면 안 되는 것.**
    - **그대로 가져올 것**:
      1. 토큰 색 역할: 회색 = 기준선(REPA), 하늘색(`--color-accent`) = 논문 방법·정렬 선, 남색(`--color-text-heading`) = backbone 구조, 주황(`--color-warm`) = 입력 차이 마커 및 질문 브래킷(글자색 금지).
      2. 깊이 비례 가로 막대와 분할 표현(`0.3D` / `0.7D`).
      3. `stroke-dashoffset`으로 그려지는 정렬 선 + `학습 때만` 명시(추론 시 teacher 미사용).
      4. `side: "below"` 4열 레이아웃, 정지 진입(Beat 0), 마지막 두 질문 브래킷.
    - **가져오면 안 되는 것**:
      1. **`SiT-XL/2 · 28개 block`, `block 1–8 / 9–28` 고정 라벨**: Self-Flow는 이미지(SiT-XL 28층) 외에 T2I/T2V/T2A·멀티모달에 FLUX.2(21층, 7 double + 14 single)를 쓰고 $l=0.3D, k=0.7D$ 비율로 정의한다([paper.txt App. A.3](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/paper.txt#L1783-L1793)). 본 도식에는 `깊이 D`, `0.3D`, `0.7D`를 쓰고 구체 층 번호(`8, 20`)는 캡션 예시로만 둔다.
      2. **끝 그림의 짧은 외부 encoder 상자 + 6줄 패치 표현 아이콘**: Beat 0(REPA)에서만 쓰고 Beat 1에서 `opacity="0" visibility="hidden"`으로 완전히 퇴장시켜야 한다. 끝 그림의 위 행은 반드시 student와 **동일 길이의 EMA teacher 막대**여야 한다.
      3. **수직 정렬 선과 `"입력이 다름"` 라벨**: Self-Flow의 정렬은 $l < k$이므로 수직선이 아니라 **`0.3D`에서 오른쪽 위 `0.7D`로 꺾이는 선**이어야 한다. 또한 REPA의 `"입력이 다름"`(깨끗한 이미지 vs 잡음 latent)을 그대로 두면 도메인 불일치로 오해되므로, Beat 1→2에서 순차 교체([animation.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/animation.md#L96-L97))해 **`입력 noise 차이`**로 바꿔야 한다.
      4. **REPA 고양이 사진(`cat_clean/noisy.png`) 및 본 덱 6–7장 앵무새 격자(`tok_*.jpg`)**: 고양이 사진은 다른 덱 자산이고 이미지 전용 오해를 부르며, 앵무새 격자는 6장 signature toggle을 미리 소모한다. 추상 4×4 latent 타일 SVG를 쓴다.
      5. **REPA의 두 질문 문구**: Self-Flow 덱의 핵심 축(작동 기전의 검증 범위 + 멀티모달/스케일 확장성)에 맞는 새 질문으로 교체한다.

---

## 5. Overview 추가 시 2–8장(새 2–9장)에서 겹치거나 고칠 곳

12. **`[must]` 3장 (`background`, [deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/deck.json#L200-L294), [shots/s03.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/shots/s03.png)) — 질문 중복 제거 및 미정의 기호 수정.**
    - 하단 `lead` 질문(`"질문: Self-Flow는 왜 작동하고, 그 설명은 어디까지 실험으로 뒷받침되는가?"`, L283)이 새 5장 overview Beat 3의 두 질문과 정면으로 겹친다. REPA 논의([repa_anim_log.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/repa_anim_log.md#L15))와 같이, 3장 끝 문장은 바로 다음 4장(Fig. 2a)으로 넘기는 좁은 질문으로 바꾼다(예: `"질문: 그렇다면 외부 encoder를 더 강한 모델로 바꾸면 생성 품질도 함께 좋아지는가?"`).
    - 표의 Self-Flow 행에 아직 정의되지 않은 기호 `$\tau_{\min}$ 입력`(L265)이 먼저 나온다. `"더 낮은 단일 timestep 입력"`으로 풀어 써서 표의 자족성을 높인다.
    - 대본(L292)에서 "Self-Flow가 왜 작동하는지..."를 빼고 4장 동기 실험으로 이어 준다(60→50초).

13. **`[must]` 8장 → 새 9장 (`teacher`, [deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/deck.json#L639-L700), [shots/s08.png](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/shots/s08.png)) — 구조 재설명 축소 및 대본의 저자 해석 귀속 명시.**
    - Fig. 3은 `meta.figures` 원장 항목이므로 유지하되, 대본(L697–698)이 overview에서 이미 보인 두 입력·EMA·층간 정렬을 처음부터 다시 설명하지 않도록 고친다. 대신 overview에서 의도적으로 뺀 **수식 6·7(`cosine`, `sg`, $\gamma=0.8$), EMA decay `0.9999`, projection `약 10M`, 구체 층(`8, 20`)**에 60초를 집중한다(75→60초).
    - **기존 대본 결함 수정**: L698 마지막 문장 `"student는 noise가 적은 토큰을 단서로 noise가 많은 토큰의 feature를 추론해야 합니다."`가 저자 귀속 없이 사실처럼 적혀 있다. Overview에서 저자 가설을 배제했으므로, 여기서도 `"저자들은 student가 noise가 적은 토큰을 단서로... 추론하게 된다고 설명하며, 이 설명의 근거는 뒤의 probe와 토론에서 따져 보겠습니다"`로 귀속을 명시해야 16장·20장 토론 3번과 일관된다.

14. **`[should]` 2장 (`tldr`, [deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/deck.json#L155-L198)) — 대본 용어 불일치 수정 및 5초 압축.**
    - 슬라이드 `message`(L159)는 `"같은 샘플의 noise 수준을 달리해"`인데, `notes`(L195)는 `"같은 이미지를 두 번 입력할 때"`로 좁혀 적었다. 비디오·오디오까지 다루는 논문이므로 `"같은 샘플을"`로 통일한다(45→40초).

15. **`[should]` 4장 (`encoder-scaling`, [deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/deck.json#L296-L344)) — overview 진입 브리지 추가.**
    - 대본(L342) 끝에 새 5장 Beat 0으로 바로 넘기는 한 문장만 덧붙인다(예: `"외부 고정 encoder를 걷어내고 모델 안에서 정렬 목표를 만들려면 구조가 어떻게 바뀌는지 다음 그림으로 보겠습니다."`, 50→45초).

16. **`[should]` 5장 → 새 6장 (`rectified-flow`), 6장 → 새 7장 (`schedulers`), 7장 → 새 8장 (`dual-timestep`) — 회수(callback) 연결만 보강.**
    - 새 6장([deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/deck.json#L346-L467)): 본문 겹침 없음. 대본 첫 문장(L464)에 "앞 그림 아래쪽 flow 모델의 기본 식과 모달리티별 토큰 규격"이라는 회수만 추가한다.
    - 새 7장([deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/deck.json#L469-L545)): overview에서 앵무새 격자를 쓰지 않으므로 `signature: true` toggle 본문은 그대로 유지한다. 대본(L543)에서 Dual-Timestep을 새 개념처럼 길게 풀지 않고 "앞 그림에서 본 두 timestep 혼합"으로 회수해 10초를 줄인다(80→70초).
    - 새 8장([deck.json](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/deck.json#L547-L637)): 본문 겹침 없음. 대본(L634)에서 식 4–5와 모달리티별 $R_M$(0.25 / 0.10 / 0.50)이 overview의 student 입력 $x_\tau$를 만드는 구체 규칙임을 짚어 준다.

17. **`[must]` `deck.json` 메타데이터 동기화.**
    - 근거: [deck.json meta](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/deck.json#L9-L133), [narrative-rules.md](file:///G:/내%20드라이브/%5B9%5DProject/custom_SKILLs/hs-vilab-html-deck-skill/work/self-flow-full/review/anim/ref/narrative-rules.md#L117-L124)
    - 새 5장이 삽입되면 `meta.target_slides`를 `21 → 22`로 갱신하고, `meta.figures` 원장의 5장 이후 모든 `use` 번호(`Fig. 3` 8→9, `Table 1` 9→10, …, `Fig. 11` 17→18)와 `Fig. 21` cut 메모의 `"8번의 기본 층 번호"` → `"9번"`을 함께 +1 수정해야 빌드의 figure ledger 검사를 통과한다.
