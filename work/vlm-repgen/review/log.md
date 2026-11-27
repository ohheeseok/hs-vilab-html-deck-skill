# Integral 개요 검토 처리 (`critic.md`, `verify.md`, `research_verified.md`)

critic(C)과 verifier(V)는 서로의 답을 보지 않았다. 곡선 근거는 내가 그림을 확대해 확인한 것만 적는다.

## 내가 그림에서 직접 확인한 것

- Fig. 6b(p. 9, 확대): 50K에서 VLM + AF ≈ 0.41, LLM + AF ≈ 0.28(40K ≈ 0.28에서 멈춤), VLM + FLUX.1-VAE ≈ 0.18, LLM + FLUX.1-VAE ≈ 0.17. **LLM + AF가 20K 이후 모든 점에서 VLM + FLUX.1-VAE보다 위**(10K에서는 0.08 대 0.07로 거의 같다). 곡선 근거.
- Fig. 6a: 10K에서는 SigLIP2-AF(≈ 0.15)가 AF(≈ 0.12)보다 위, 20K에서 거의 같고 그 뒤로 AF가 위. 곡선 근거.
- Fig. 3c: 20K에서 AF의 cosine ≈ 0.971(Frozen ≈ 0.972), Joint ≈ 0.865, Joint(강한 sem.) ≈ 0.943. PSNR은 AF ≈ 26.7, Joint ≈ 26.3, Joint(강한 sem.) ≈ 23.2, Frozen ≈ 19.4. Joint(강한 sem.)도 PSNR은 오르지만 Joint보다 낮다(V5 맞음).
- Table 7(p. 19): 생성 Stage 1 200K step·256²·32 H100, Stage 2 50K·≤512·48 H100, Stage 3 350K·≤512·48–64 H100. 통제 비교 50K는 Stage 1의 1/4 지점이다.
- Table 10: 20K step AF는 PSNR 26.67, rFID 2.26, Sem. 0.971 — Table 1의 32.2 dB는 전체 학습(+adversarial decoder) 후 값.

## 결정

| ID | 처리 | 무엇을 하나 |
|---|---|---|
| C1 overview가 빈 무대 + 화살표 5개(stepper) | 수용 | beat 0 = 논문이 대비하는 기존 설계(BAGEL식, §3.2: VLM + 층마다 짝지은 생성 expert(Full MoT) + 별도 FLUX.1-VAE latent). beat 1 = VAE latent 자리에 AF의 z가 들어오고 vision encoder 여러 층이 AF로 모임, 이해 입력도 z에서(projector). beat 2 = 층마다 잇던 생성 stream이 4층 간격 8블록으로 줄어듦(32층). beat 3 = 두 질문. 결과 수치 없음, 가설은 그리지 않음 |
| C2·V1 14–15 중복, Fig. 6b 누락 | 수용 | 14 = AF vs FLUX.1-VAE(Fig. 1 오른쪽, PSNR·GenEval deltas, 조건). 15 = **대표 인터랙션** toggle 4상태: [1] SigLIP2-AF(Fig. 6a) [2] LLM 조건(Fig. 6b) [3] 의미 정렬 제거(Fig. 10a, Table 11) [4] 2B 백본(Fig. 7). 네 그림 모두 x 10K–50K, y GenEval 0–약 0.45(Fig. 10a는 0–0.43, 캡션에 밝힘). 상태마다 "바꾼 것 / 고정한 것 / 결과 / 이 비교가 지우는 설명" |
| C5 대안 설명 프레임 | 수용 | 16 = "지운 설명과 남은 설명" 표(재구성 품질, 의미 표현 일반, 조건 모델, 의미 정렬, 모델 크기 | 비교 | 지움/남음). 남은 것: LLM + AF > VLM + FLUX.1-VAE(latent 자체 효과와 조건 공유 효과가 다 갈리지 않음), SigLIP2-AF는 encoder·정렬 표적·PSNR이 함께 바뀜, 50K·256²·GenEval 중심, 2B × FLUX.1-VAE 없음 |
| C3·V3 토론 2번(cosine vs RMS-MSE) | 수용 | 전제가 틀렸다: per-token RMS 정규화 MSE = 2(1 − cos). 뺀다. 8번 Eq. (6)에는 "본문의 cosine-distance에 해당"으로 적는다(V6) |
| C3 진짜 쟁점 | 일부 수용 | 멀티턴 z 재사용(§2.2)이 측정되지 않은 것, 0.89B 밖의 비용(AF 경로 456.0M → 582.1M, pixel decoder 475.1M)은 토론에 넣는다. "Fig. 5b 3층 간격 도식"은 개념도라 쟁점으로 삼지 않는다. 32층 vs Full MoT 31블록(App. A.1 vs C.2)은 발표 메모에만 |
| C4 12–13 비통제 비교, 13 과밀 | 수용 | 12에 "시스템 비교: 백본·데이터가 다름(Qwen3.5-9B MMMU 73.2 vs BAGEL 55.3)" 조건을 화면에. 13 = toggle 2상태 [1] 지식 생성(WISE-Verified + Fig. 2 생성 예) [2] 지식 편집(KRIS-Bench + Fig. 2 편집 예) |
| C6 중심 줄기 지연, 4·6 중복, Fig. 3 판독 | 수용 | 4는 간극과 질문만(trade-off 곡선은 6). 6은 Fig. 3 전폭, "CKA 상관 근거, 개입 실험 아님"을 화면에. 방법 7–10에서 시간을 줄여 통제 비교가 9분 안쪽에서 시작 |
| C7 19 두 메시지, 20 억지 결합, prefill | 수용 | 17 = AF 융합 비교(Fig. 8, Table 10). 18 = 생성 구조 비교(Fig. 9 MMDiT, Table 13 Full MoT). 19 = 한계와 비용 groups 3열(검증 범위 / 평가 / 비용): prefill 42.6 → 54.9 ms(+28.9%)와 end-to-end +2.1%(생성 텍스트 100 토큰) 함께 |
| C8 인터랙션 | 수용 | 5 animation, 13 toggle, 15 toggle(signature) = 3 ≤ ⌊21×0.2⌋ = 4. Fig. 3c와 Fig. 8은 toggle로 겹치지 않는다(축이 다름) |
| C9 ① Fig. 11·Table 10 | 일부 수용 | Table 10은 17에 넣는다. Fig. 11은 cut: 층을 지울수록 남는 feature 수도 줄어 가설과의 "긴장"으로 읽기 어렵다 |
| C9 ② 연속 공유 표현 계열 | 수용 | 3에 "연속 시각 표현 공유: Harmon, Ming-UniVision"(§3.2 Baselines) 추가 |
| C9 ③ 학습 규모 | 수용 | 10에 Table 7 GPU 수와 "통제 비교 50K = 생성 Stage 1(200K)의 앞 1/4" |
| C10 9 과밀, 토론 시간, 용어 | 수용 | 9는 Fig. 5a–b 구조와 규격만. Fig. 5c는 18의 Table 13이, Fig. 5d(adaLN-single)는 9의 한 줄이 맡는다. 토론 2:30 이상. 용어는 `vision encoder`로 통일 |
| V2 Table 12 조건 | 수용 | "생성 텍스트 100 토큰", text generation 1837 → 1865 ms, peak +7.3%. Table 13: compute 2.50×, latency/batch 3.10×, 배치·step 수 미보고 |
| V4 장부 | 수용 | Fig. 1 use 1·5·14, Fig. 6 use 15, Eq. (1)의 출력은 f, bottleneck을 지나 z |
| V5 Fig. 3c 서술 | 수용 | "강한 의미 감독 Joint는 Joint보다 PSNR이 낮다(곡선)" |
| V7 0.89B = 891M | 수용 | 9에 "0.89B(891M, Fig. 9)". 32 vs 31은 메모만 |
| V8 PSNR 조건 | 수용 | 14에 "PSNR은 각 tokenizer의 최종본(Table 1), GenEval은 256² 50K step T2I(§3.4)" |
| V9 SigLIP2-AF 조건 | 수용 | 15 [1]에 "바뀐 것: vision encoder(siglip2-so400m-patch16-256)·정렬 표적·PSNR(34.08 dB)", 10K 역전은 곡선 근거로 메모 |
| V10 Fig. 8·9 곡선 | 수용 | 곡선 근거 표시, 891M = 0.89B |
| 외부(research_verified) | 수용 | 19·20에 external 2건: WISE-Verified 판정 모델이 Qwen3.5-35B-A3B(같은 계열), GenEval 2 초록의 GenEval 포화 주장. ending에 코드·체크포인트 링크 |

## 토론 포인트(20장)

1. 근거 · 무엇이 이득을 만드나 — LLM + AF(≈ 0.28) > VLM + FLUX.1-VAE(≈ 0.18): 조건 VLM 없이도 AF latent가 앞선다. 남는 이득(+0.13)이 "공유"의 몫이라면, 앞의 몫은 의미 정렬된 latent 자체의 몫인가 [Fig. 6b, 곡선]
2. 근거 · 짧은 학습의 GenEval — 통제 비교는 256² 50K step(생성 600K 중), 주로 GenEval. GenEval 2 저자들은 GenEval이 포화됐다고 본다(external). 수렴 속도의 차이인가, 최종 품질의 차이인가 [§3.4, Table 7]
3. 근거 · 측정하지 않은 주장 — z를 다음 턴 입력으로 바로 다시 쓰면 정보 손실을 피한다(§2.2)는 측정이 없다. propagation bottleneck도 CKA 상관뿐 [§2.1–2.2]
4. 대가 · 해석 — 0.89B 밖의 비용: VLM의 시각 입력 경로 교체(+126.1M, prefill +28.9%), pixel decoder 475.1M, VLM을 바꿀 때마다 tokenizer 650K step [App. C.3, Table 7–12]

## 목표 구조(21장, 20분)

| # | section | 제목(안) | 블록 | 시간 |
|---|---|---|---|---|
| 1 | — | 표지 | cover + Fig. 1 왼쪽 | 20 |
| 2 | summary | Integral 한눈에 보기 | statement | 40 |
| 3 | background | 통합 멀티모달 모델의 갈래 | table(갈래·대표·시각 표현) | 55 |
| 4 | background | 이해용 표현과 생성용 latent | compare + lead 질문 | 45 |
| 5 | background | Integral의 구조 한 장 | animation(4 stop) | 60 |
| 6 | method | Propagation bottleneck 가설 | figure 전폭 + bullets | 65 |
| 7 | method | Abstraction Fusion의 토큰 구성 | split figure + process | 55 |
| 8 | method | AF의 두 출력과 학습 목표 | diagram + equation | 55 |
| 9 | method | Block-wise MoT의 조건 전달 | figure + groups | 60 |
| 10 | method | 학습 단계와 규모 | table(Table 7 일부) | 40 |
| 11 | results | AF의 재구성과 이해 유지 | table + deltas | 50 |
| 12 | results | 이해·생성 시스템 비교 | table + bars | 60 |
| 13 | results | 세계 지식이 필요한 생성과 편집 | toggle 2 | 60 |
| 14 | analysis | AF와 FLUX.1-VAE: 50K step 비교 | figure + deltas | 60 |
| 15 | analysis | 통제 비교 네 가지 | toggle 4 (signature) | 120 |
| 16 | analysis | 지운 설명과 남은 설명 | table | 60 |
| 17 | analysis | AF 융합 방식 비교 | figure + table | 45 |
| 18 | analysis | 생성 구조 비교: MMDiT와 Full MoT | figure + table | 45 |
| 19 | analysis | 한계와 비용 | groups 3열 | 55 |
| 20 | discussion | 정리와 토론 | statement | 150 |
| 21 | — | 감사합니다 | ending | 0 |

합계 1200초.
