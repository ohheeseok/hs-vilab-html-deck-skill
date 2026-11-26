# review/log.md — 지적마다 수용·기각과 이유

작성: Claude(조율). 초안 codex `outline.md`, 비평 agy `critic.md`, 검증 agy `verify.md`(서로 모르게), 조사 agy `research.md` → `research_verified.md`.
조율자가 논문에서 직접 확인한 것: Fig. 3(p. 5) 두 패널의 y축이 같다(0–0.5), Fig. 4(p. 7)의 47×·16×는 곡선 위 화살표다, Table 15b(p. 25)와 Table 6(p. 8)의 인코더 크기별 gFID, App. D(p. 24)의 DiT^DH 전용 최적화 레시피, App. I(p. 27)의 guidance 설정.

## 비평(critic)

| ID | 처리 | 이유와 결정 |
|---|---|---|
| C1 방법 8장, 두 가정 경계 없음 | 수용 | 구간을 둘로 나눈다: `claim1` "① 복원"(5–6), `claim2` "② 고차원 확산"(7–13). 6번은 ①의 판정과 남은 것(복원이 좋은 인코더가 생성에서도 좋은가 → 18번)으로 끝낸다. 13번(처방 누적 사다리)이 ②의 전환 마디. |
| C2 반박을 좁히는 근거 누락 | 수용 | 새 18번 "인코더 선택과 차원"(구간 `scope`): Table 15a(MAE-B rFID 0.16인데 gFID 16.14 → 8.38, SigLIP2-B 6.69 → 4.93, DINOv2-B 4.81 → 4.28)와 Table 6/15b(DiT-XL: S 3.50, B 4.28, L 6.09 / DiT^DH-XL: 2.42, 2.16, 2.73). ①은 "복원은 된다"까지, ②는 "처방을 하면 된다, 그러나 차원이 클수록 더 좋아지지는 않는다"까지. 5번에 판별자 frozen DINO-S/8(Table 12, App. C.2). |
| C3 대표 인터랙션 약함 | 수용 | 대표 stepper를 13번 **처방 누적 사다리**로 옮긴다(새로 그린 SVG 막대, 같은 조건: DINOv2-B, ImageNet 256, 80 epoch, 무가이던스). 단계: 기본 DiT-XL 23.08(Table 2) → + schedule shift 4.81(Table 4) → + 노이즈 증강 디코더 4.28(Table 5) → + wide DDT head(DiT^DH-XL) 2.16(Table 6). 처음부터 SD-VAE DiT-XL 7.13(Table 2) 기준선을 그어 둔다. 한 축(gFID, 0–25 선형)이라 축 왜곡 없음. 8번 Fig. 3은 정적 두 패널(두 패널 y축이 같다: 0–0.5). 13·16 토글 제안은 기각: Fig. 4(epoch)와 Fig. 6b(GFLOPs)는 x축 단위가 달라 한 토글로 묶지 않는다. 16번 샘플은 Fig. 7 한 장. 덱 전체 인터랙션 1장. |
| C4 그림 과적재 | 수용 | 2번: 밝은 TL;DR — 위 `lead`, 가운데 `cards` 3, 아래 전폭 Fig. 1. 14번: Fig. 4 한 장(Fig. 6b는 15번으로). 15번: Fig. 6a + Table 6 원값(버블 범례 지시 삭제, Fig. 6c는 cut). 17번: Fig. 7 한 장(부록 Fig. 10·13 cut: 같은 메시지). |
| C5 split 단조, bars 0, 10·11 블록 | 일부 | 13번 사다리가 막대. 10번에 \(t_n=0.5 \to t_m\approx0.87\)(α=√48에서 계산, `derived`)을 보태 shift가 무엇을 하는지 수로 보인다. 11번은 `equation` + Table 15c(τ 4행) 표 + deltas 1, compare 삭제. 3·4·13·20번은 split이 아닌 전폭 배치. |
| C6 18·19 중복, 토론 시간 | 수용 | 18·19(Table 10·11)를 한 장(19번)으로: 3열 표 SD-VAE(256×16) / 픽셀(256×768) / RAE DINOv2-B(256×768) × DiT-XL / DiT^DH-XL. 확보한 1장은 C2의 18번에 쓴다. 20번 토론은 2:15. "내용 장수"는 19장(표지·ending 제외)으로 바로잡는다. |
| C7 빠진 것 3가지 | 일부 | 12번에 파라미터 839M(Table 8, DiT-XL 675M). 16번 표에 IS 열과 DiT-XL(DINOv2-S) 800 epoch 1.87 / 1.41 행. random sampling 역전(DiT^DH-XL guided 1.28 vs REPA-E 1.26, Table 14)과 CFG(§I: interval 없으면 FID 악화)는 20번 토론 1·2에. |
| C8 제목, Fig. 3 이론선, Table 3 | 수용 | 5–13번 제목이 어느 가정을 다루는지 읽히게(예: "RAE: 고정 인코더와 ViT 디코더", "고차원 RAE latent에서의 기본 DiT"). 8번에서 이론선은 "9번에서 설명할 하한"이라고 한 줄로 예고. 9번은 Table 3 3×3 전체(✓/✗). |
| C9 Table 13 장부 | 수용 | Table 13은 장부에서 "use: 9, 12(폭 값만 본문에 인용)". 토론 1번에 REPA(5.90→5.78)·REPA-E(1.83→1.70)도 Table 14에서 바뀐 값으로. |

## 검증(verify)

| ID | 처리 | 결정 |
|---|---|---|
| V1 2번 조건 | 수용 | "DINOv2-B, DiT^DH-XL 800 epoch, class-balanced sampling". |
| V2 5번 Table 1b 조건 | 수용 | "DINOv2-B 인코더, ImageNet-1K val rFID". |
| V3 7번 RAE 조건·256토큰 근거 | 수용 | "DINOv2-B RAE(patch 1)와 SD-VAE(patch 2), 둘 다 256토큰, 노이즈 증강 전". |
| V4 Table 13 장부 | 수용 | C9와 같음. Fig. 3 실험은 head 4(App. F)로 Table 13과 다르다. |
| V5 8번 서술 | 수용 | "층을 늘려도 손실이 0.5 부근에 머문다", "대상 이미지 3장 × 각 3회 평균(App. F)". |
| V6 9번 Table 3 | 수용 | 3×3 전체와 ✓/✗, "단일 이미지 과적합 손실", Theorem의 가정(선형 투영 A·B, E[x]=0). |
| V7 10번 계산값 | 수용 | 196,608과 α≈6.93은 `derived`(정의에서 계산), Table 4는 노이즈 증강 전. |
| V8 12번 Table 16 조건 | 수용 | DiT-XL backbone, 무가이던스, GFLOPs는 head만. |
| V9 13번 곡선 근거 | 수용 | 14번(Fig. 4)에서 47×·16×·720 epoch 2.39는 "곡선 근거". 기준점 SiT-XL 8.26·REPA-XL 5.90은 Fig. 4에 적힌 값이며 Table 8(balanced)과 다르다고 notes에서 말한다. |
| V10 14번 과잉 일반화 | 수용 | "DiT^DH-S…XL을 DiT-XL 한 점과 비교(Fig. 6a)", Table 6은 DiT-XL 대 DiT^DH-XL. 약 40%·3.38·6.07은 본문·Fig. 6a 근거. |
| V11 15번 조건 | 수용 | balanced(클래스당 50장), random 값은 토론으로; 256 1.13은 guide DiT^DH-S 14 epoch·scale 1.42, 512는 20 epoch·1.5; 파라미터 839M vs 675M. EDM2 epoch은 표에 없음 → "—". |
| V12 17번 조건 | 수용 | Table 9는 DiT^DH-XL, DINOv2-B, 400 epoch, guidance 적용(Table 7의 1.13과 같은 수). |
| V13 18번 16차원 | 수용 | "2×2×4=16(계산)", 두 모델의 최적화 레시피가 다름(App. D)을 19번 note에. |

## 조율자가 더하는 것

- **토론 4개**(20번): ① 근거 · FID 프로토콜: Table 8 캡션은 재평가로 "baseline이 높아졌다"고 쓰지만 Table 14는 balanced가 모든 방법에서 낮다; SiT 8.61은 Table 14의 random 값; random으로 보면 guided 순위가 바뀐다(DiT^DH-XL 1.28 vs REPA-E 1.26). ② 근거 · guidance 설정을 FID로 고르고 같은 FID로 보고: scale 1.42, 14 epoch guide(App. I), CFG는 interval 없이 FID 악화. ③ 근거 · head 효과와 최적화 레시피가 분리되지 않음(App. D: DiT^DH만 linear decay·warmup 40 epoch·EMA 0.9995·grad clip 1.0); Table 6·10·11의 DiT 대 DiT^DH 비교 모두 해당. ④ 대가 · 해석: 이미지당 latent 원소 196,608 vs SD-VAE 4,096(48배) — latent 캐시·전송 비용은 논문에 없음; 동결 인코더의 사전학습 데이터는 research_verified.md에 있으면 `external`로.
- **8번 Fig. 3 표기 불일치**(본문 "384 to 784", 축 896; 본문 "SiT-S"; App. F 폭·깊이 뒤바뀜)는 슬라이드에 올리지 않고 notes에도 넣지 않는다(오탈자, 결론과 무관).
- 18번은 "통념의 범위"이지 반례 모음이 아니다: 논문이 직접 한 말(§G.1 "a low rFID does not necessarily imply a good image tokenizer", §5 "the advantage grows with encoder size")을 그대로 둔다. 둘째 말은 Δ 기준으로는 맞고 절대값 기준으로는 L이 B보다 나쁘다 — 두 사실을 같이 보인다.

## 목표 구조(21장, 20:00)

| # | section | 제목(초안) | 블록 | 시간 |
|---|---|---|---|---|
| 1 | — | 표지 | cover | 0:25 |
| 2 | summary | RAE와 DiT^DH 한눈에 | lead + cards 3 + 전폭 Fig. 1 | 0:50 |
| 3 | background | 잠재 확산과 표현 학습의 갈래 | groups 3 + 질문 callout | 0:55 |
| 4 | background | 논문이 겨냥한 두 통념 | compare 2열(통념 / 논문의 검증 방법) | 0:50 |
| 5 | claim1 | RAE: 고정 인코더와 ViT 디코더 | split: Fig. 2 / 사실(토큰·patch·손실·판별자·GFLOPs) | 1:00 |
| 6 | claim1 | 세 인코더의 복원과 linear probe | split: table(Table 1a/c/d) / Fig. 8 | 1:00 |
| 7 | claim2 | 고차원 RAE latent에서의 기본 DiT | split: table(Table 2)+deltas / cards 3(가설) | 0:55 |
| 8 | claim2 | 한 이미지 과적합: 폭과 깊이 | Fig. 3 두 패널 정적 | 1:00 |
| 9 | claim2 | Theorem 1: 폭과 토큰 차원 | split: equation / Table 3 3×3 | 1:20 |
| 10 | claim2 | 차원 의존 schedule shift | split: equation + 계산 / deltas | 0:50 |
| 11 | claim2 | 노이즈 증강 디코더 | split: equation / table(Table 15c)+deltas | 0:50 |
| 12 | claim2 | DiT^DH: 얕고 넓은 DDT head | split: Fig. 5 / table(Table 16) | 0:55 |
| 13 | claim2 | 처방을 하나씩 더한 gFID | **대표 stepper**(SVG 막대 4단계 + SD-VAE 기준선) | 1:15 |
| 14 | results | 학습 epoch에 따른 수렴 | Fig. 4 + 읽기 3줄 | 0:50 |
| 15 | results | DiT^DH의 연산량과 인코더 크기 | split: Fig. 6a / table(Table 6) | 0:50 |
| 16 | results | ImageNet 256·512 벤치마크 | table(Table 8·7 발췌, gFID·IS·epoch·params) | 1:10 |
| 17 | results | 512×512 샘플과 디코더 업샘플링 | split: Fig. 7 / table(Table 9) | 0:45 |
| 18 | scope | 인코더 선택과 차원 | split: table(Table 15a) / table(Table 6·15b) | 1:00 |
| 19 | scope | SD-VAE·픽셀·RAE 위의 DDT head | table 3열(Table 10·11) + note | 0:50 |
| 20 | discussion | 정리와 토론 | 어두운 statement: 정리 2 + 토론 cards 4 | 2:15 |
| 21 | discussion | 감사합니다 / Q&A | ending | 0:15 |

합계 20:00. 구간 7개는 많다 → `summary`와 `background`를 "요약·배경"으로 합쳐 6개: 요약·배경 / ① 복원 / ② 고차원 확산 / 결과 / 범위 / 정리와 토론.
