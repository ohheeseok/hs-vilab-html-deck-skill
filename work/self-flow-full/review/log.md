# review/log.md — 지적마다 수용·기각과 이유

작성: Claude(조율). 초안 codex `outline.md`, 비평 agy `critic.md`, 검증 agy `verify.md`(서로 모르게), 조사 agy `research.md` → `research_verified.md`.

## 비평(critic)

| ID | 처리 | 이유와 결정 |
|---|---|---|
| C1 결과 구간 과다·토론 시간 부족 | 수용 | 11(비디오)+12(오디오)를 한 장으로, 16(RAE)을 9(ImageNet 표의 RAE 행)로 흡수. 대신 **한계와 검증 범위** 슬라이드를 새로 둔다(구조의 "한계" 단계가 없었음). 목표 21장. 토론에 ≥1:40. |
| C2 프로젝터에서 안 읽히는 그림 | 수용 | Fig. 7 rollout 띠·Fig. 10(b) 8프레임·Fig. 8(a) radar는 판독 불가 → 7·8(a) cut(대신 Fig. 8(b) 막대와 Table 6), 10(b)는 탭 한 상태로 전폭. Fig. 3은 전폭(상단) 배치. Fig. 6은 (a)/(b) 중 하나씩 크게(탭). |
| C3 7번 stepper 중복·표지 관찰 포인트 | 수용 | stepper 폐기. 대신 **6번을 대표 인터랙션 toggle**로: 같은 토큰 격자에서 vanilla / full masking / diffusion forcing / Dual-Timestep 네 방식을 바꿔 보이고, 읽기 칸에 각 방식의 배정 규칙과 Fig. 2(b)에서의 결과(§3.3 서술 그대로). 7번은 Dual-Timestep 정의(정적). 표지는 teaser만. |
| C4 Fig. 1(a)·Fig. 21·Table 5 장부 | 수용 | Fig. 1(a)의 "2.8× faster"는 REPA 1M FID 3.92 기준의 **step** 비교임을 T2I 슬라이드 캡션에 적는다(teacher forward 비용 미반영은 해석). Fig. 21은 cut(층 번호만 App. H에서 인용). Table 5는 오디오가 있는 슬라이드에만. |
| C5 블록 단조로움, 근사값을 큰 숫자로 | 수용 | 2단 split 일변도 금지: 전폭 표·전폭 그림·탭을 섞는다. 같은 단일 블록 3장 연속 금지. Ablation의 "+4점 초과 / +1점 초과"는 deltas 타일이 아니라 그림 옆 항목으로. |
| C6 App. C low-SNR 5%·빠진 ablation·단일 대조군 | 수용 | 비디오 결과와 timestep 분포 슬라이드에 App. C(비디오는 5%를 [0.95, 1.0] 균일에서 뽑음, 없으면 Self-Flow framewise FID가 악화, Fig. 15(d)). 한계 슬라이드에: 멀티모달·로봇·4B 타이포·RAE/FLUX.2 AE는 Vanilla FM하고만 비교, scaling은 CLIP score만, ablation·linear probe는 ImageNet만, T2I·T2V는 내부 데이터, 공개 코드는 추론뿐(R2). |
| C7 방법 구체성·방법 비교표 | 수용 | 5번에 모달리티별 토큰 수(이미지 256, 비디오 ~3K, 오디오 250)와 차원. 3번 배경을 **REPA / SRA / LayerSync / Self-Flow 비교표**(무엇을 무엇에 맞추나, teacher, 외부 모델 유무)로. 표에 외부 사실을 쓰면 R4·R5. |
| C8 T2I 슬라이드 지표 | 수용 | 10번 = FID 막대 + REPA 대비 deltas(FID −0.31, FD-DINO −5.37, CLIP +0.21). Fig. 5는 cut(끝점 수치는 Table 2–4). sFID는 캡션 한 줄. |
| C9 제목·용어 | 일부 | 4번 제목 수정(결론 선언은 피한다: "외부 encoder 크기와 생성 FID"). 7번 "Dual-Timestep Scheduling"은 기술 용어 그대로 허용. 용어는 하나로: **loss, 층, noise, timestep, teacher, student**(한국어 편집 단계에서 통일). 3번 질문에 "왜·어디까지". |
| C10 인터랙션 재배치 | 일부 | 6번(스케줄러 네 방식, 대표)·14번(정성 비교 탭: 타이포 / Vespa / 춤)·15번(Fig. 6 step↔FLOPs 탭) = 3장 ≤ ⌊21×0.2⌋=4. 13번 Table 6 스위처는 기각: 5행×3 Δ 표가 정적으로 더 잘 읽힌다. |

## 검증(verify)

| ID | 처리 | 결정 |
|---|---|---|
| V1 | 수용 | ImageNet: no CFG, 250 SDE steps, Precision 열 추가, "약 3M"은 Fig. 20(a)의 2M–4M 사이 교차로 표현. |
| V2 | 수용 | 멀티모달: ~625M, 1M step, no CFG, T2I는 FLUX.2 AE, 배치 비율 57/30/13%. |
| V3 | 수용(중요) | 로봇: 100K에서 Coke Can 수렴, **Drawer는 FM이 소폭 앞섬**, Move Near 격차 **확대**, Open and Place 격차 유지. 평가 횟수(15·18·10·7회 × 2) 병기. |
| V4 | 수용(중요) | Linear probe: 4–16층 개선, **20–28층은 Vanilla보다 낮음**. |
| V5 | 수용 | 토론 전제 문구 교체: A.3 "학습 전 같은 p(t)" vs B·Table 5 "세 baseline 0.75, Self-Flow 1.0". |
| V6 | 수용 | C4와 같음. |
| V7 | 수용 | Fig. 2(a) 조건: REPA 설정, ImageNet 256, SiT-XL, no CFG. Fig. 2(b)는 데이터셋 명시 없음 → 표시하지 않는다. |
| V8 | 수용 | T2I: no CFG, 50 ODE steps. sFID는 SRA 8.05 · REPA-SigLIP 2 8.13 · Self-Flow 8.14. |
| V9 | 수용 | 비디오: 45프레임·192p, no CFG, low-SNR 5%(App. C). |
| V10 | 수용 | 오디오: FMA 1M, no CFG, REPA는 MERT, Self-Flow R_M=0.5는 탐색으로 선정. |
| V11 | 수용 | Fig. 9 모델은 "4B multi-modal(고해상도 100K step)". |
| V12 | 수용 | RAE·FLUX.2 AE에 no CFG와 모델 크기. |
| V13 | 일부 | "625M Self-Flow > 1B REPA"는 유지. 그래프에서 읽은 0.10 같은 근사 수치는 쓰지 않는다. FLOPs 산정식 미기재는 한계 슬라이드에. |
| V14 | 수용 | Ablation은 §4.4 서술 그대로, "정확한 표 수치 없음, Fig. 11(a) 600K step, no CFG". ℓ1은 "후반 정체·악화(원인은 저자 설명)". |

## 조사(research)

`research_verified.md` R1–R5만 사용. R3(Jiang et al. 2026-07)은 토론 포인트 하나("이득이 cross-token 정보에서 오는가, noise 축 augmentation에서 오는가")에 `external`로. R1·R2는 마무리 슬라이드.

## 목표 구조 (21장, 20분)

1 표지 · 2 TL;DR(statement) · 3 배경: 표현 정렬 방법 비교표 · 4 외부 encoder 크기와 생성 FID(Fig. 2a) · 5 Rectified flow와 토큰 규격 · 6 토큰별 noise 배치 네 방식(**대표 toggle**, Fig. 2b) · 7 Dual-Timestep Scheduling 정의 · 8 EMA teacher와 loss(Fig. 3 전폭) · 9 ImageNet 256×256(Table 1, RAE 행 포함) · 10 Text-to-image(bars + deltas, Fig. 1a 캡션) · 11 비디오와 오디오(Table 3·4) · 12 공유 backbone(Table 6) · 13 Video-action(Fig. 8b) · 14 정성 비교(**탭**: Fig. 9 / 10a / 10b) · 15 모델 크기와 FLOPs(**탭**: Fig. 6a/6b) · 16 층별 linear probe(Fig. 4b) · 17 구성요소 ablation(Fig. 11a) · 18 Timestep 분포와 low-SNR(Fig. 11b, App. C) · 19 한계와 검증 범위 · 20 정리와 토론(statement) · 21 마무리

## 2차 검증(verify2, deck.json 대상)

| ID | 처리 | 결정 |
|---|---|---|
| W1 3번 대본 "teacher에 더 깨끗한 입력"은 SRA도 같음 | 수용 | 차이는 student 입력의 토큰별 두 timestep + teacher의 τ_min. |
| W2 5번 2×2 patch 대상 | 수용 | SD-VAE·FLUX.2 AE만. |
| W3 6번 캡션 주어 누락 | 수용 | Full masking·diffusion forcing의 악화 원인으로 한정. |
| W4 7번 대본 "추론 조건과 어긋나지 않음" 과장 | 수용 | 논문의 "균형" 서술로. |
| W5 9번 SRA Rec. 굵게 | 수용 | REPA 0.69가 최고. Δ provenance 식 순서 정리. |
| W6 11번 Depth Anything 3 "비디오 전용" | 수용 | 깊이 추정 모델로. |
| W7 13번 평가 횟수·판독 표시 | 수용 | 7회×2=14회, 과제별 앞섬은 "그림 판독". |
| W8 16번 linear probe 층별 순위 | **둘 다 기각, 그림대로** | 진행자가 Fig. 4(b)를 확대해 읽음: **모든 층에서 Self-Flow가 높고**, 차이는 4–16층에서 크고 20–28층에서 작다. 1차 검증 V4("20–28층 vanilla 우세")와 2차 W8("20·24층 vanilla 우세")이 모두 틀렸고, 1차를 그대로 받아 쓴 슬라이드 문구를 고쳤다. 교훈: 곡선 판독에 기대는 지적은 진행자가 그림을 직접 확대해 확인한다. |
| W9 18번 가설 출처 | 수용 | App. B 추가. |
| W10 19번 R_M ablation | 수용 | 오디오는 R_M 탐색은 했으나 R_M별 비교는 미보고. |
| W11 20번 토론 1 전제 | 수용 | A.3 "학습 전 결정, 대조군 동일" vs App. B "방법마다 탐색, 대조군 0.75 / Self-Flow 1.0". 질문은 interpretation으로 표시. |
