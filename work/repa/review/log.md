# review/log.md — 지적마다 수용·기각과 이유

작성: Claude(조율). 초안 codex `outline.md`, 비평 agy `critic.md`, 검증 agy `verify.md`(서로 모르게), 조사 agy `research.md` → `research_verified.md`.

## 비평(critic)

| ID | 처리 | 이유와 결정 |
|---|---|---|
| C1 진단–처방 단절, 분석 비대 | 수용 | Fig. 3(정렬 후 표현)을 방법 바로 뒤, 결과 구간 첫 장으로 옮긴다: 진단(Fig. 2) → 처방(구조·손실) → 표현이 어떻게 바뀌나(Fig. 3) → 생성이 얼마나 빨라지나(Fig. 1·Table 3·4) → 조건(Table 2·5, Fig. 5·7). 분석 구간은 5장. |
| C2 Table 2 과분할, 과밀 | 일부 | 16(목적 함수)+17(λ)을 한 장으로. 18(SiT 크기별)은 10과 질문이 다르다(같은 step의 Δ vs 모델이 클수록 더 빠른가) → 유지. 목표는 **21장**(20분, 분당 1.05장 — SKILL.md의 1.0–1.5 범위). 18–19장까지 줄이지 않는다. |
| C3 표 연속, 블록 단조, wash | 수용 | 인코더 슬라이드는 표를 빼고 Fig. 5a를 크게(같은 데이터 중복 제거). 표가 세 장 연속되지 않게 배치. 차트·표 슬라이드는 `tone: wash`(합성 단계에서 지정). |
| C4 프로젝터 가독성, 2메시지 | 수용 | Fig. 3은 패널별 탭으로 전폭. Fig. 7만 한 장(Fig. 8은 노이즈 슬라이드의 한 줄 + 장부 use). 적용 범위 슬라이드는 512px·T2I 결과만, 비용은 토론으로. |
| C5 인터랙션 0장, 축 왜곡 | 일부 | 3장(≤ ⌊21×0.2⌋=4): ① **대표: REPA 구조 stepper**(새로 그린 SVG: clean 경로 → noisy 경로 → layer 8에서 MLP·sim → 이후 층과 velocity loss → 추론에서는 인코더·MLP 없음). ② **Fig. 3 탭**(a 분류 / b 정렬 / c FID–Acc.): 한 그림 안에 vanilla와 REPA가 같은 축으로 그려져 있어 Fig. 2b↔3b 맞교환의 축 왜곡(0–0.3 vs 0–0.6)이 생기지 않는다. ③ **Fig. 4 탭**: 클래스 3개(앵무새·열기구·햄버거)를 하나씩 크게. Fig. 38 PCA 토글은 기각(부록, 시간). |
| C6 핵심 근거 누락 | 일부 | Table 4에 외부 모델 행(DiT-XL/2 2.27, MaskDiT 2.28, MDTv2-XL/2* 1.58, SiT-XL/2 2.06)을 넣어 위치를 보인다 — guidance interval·CFG 스케줄이 붙은 행(*)은 표시. Table 6(ImageNet 없이 학습한 CLIP 11.0·SigLIP 10.2, 단 최고인 DINOv2는 ImageNet 포함)은 인코더 슬라이드에. Table 3 DiT-XL/2(7M 9.6 = REPA 850K 9.6, 7M/850K ≈ 8.2×)는 400K 비교 슬라이드의 한 줄. Fig. 38은 기각. |
| C7 방법 구체성, 정성 그림 | 수용 | 구조: v_θ = g_θ∘f_θ 분해(§3.1), SiLU 3층 MLP, positional embedding 보간(App. D), 추론 때 projector 없음(App. B). 손실: sim 선택지(NT-Xent / cosine), L_velocity. Fig. 4는 클래스별로 무엇이 보이는지 — 단 이미지를 읽은 서술은 해석으로 표시. |
| C8 제목·링크·note | 수용 | 2번 제목 명사형. 12·19번 제목을 내용대로. GitHub 링크는 논문에 없지만 `research_verified.md`에서 확인 → `external`로 유지. 토론의 대가 카드는 해석 표시. |

## 검증(verify)

| ID | 처리 | 결정 |
|---|---|---|
| V1 GitHub 주소 | 일부 | 논문에 없음은 맞다. GitHub API로 확인(MIT) → ending 링크로 두고 `external`. |
| V2 Fig. 5b vanilla | 수용 | vanilla는 400K 기준선(수평선), 곡선은 REPA 세 모델. |
| V3 Fig. 3b 후반 층 | 수용(중요) | CKNNA는 layer 8 부근에서 크게 높고 후반 층(20–24)은 vanilla와 비슷하거나 낮다(곡선 근거). Linear probe는 전 층에서 REPA가 높다. Fig. 3의 vanilla step·평가 t는 미명시. |
| V4 Fig. 8 후반 층 | 수용(중요) | 정렬 층 부근만 높고 후반 층은 vanilla 기준선 아래. 토론과 연결: 후반 층은 target에서 멀어진다 — 저자 해석(고주파 세부)과 HASTE(후반 정체)를 나란히. |
| V5 Table 5 no CFG | 수용 | no CFG, Table 8 400K 행과 대응. |
| V6 4M = 800 epochs | 수용 | "batch 256에서 800 epochs = 4M step, 1,400 = 7M" 병기, App. D Table 7. |
| V7 Fig. 2c SiT-B/2 400K까지 | 수용 | DINO-B에도 못 미침, 곡선 근거. |
| V8 Table 3 SiT-L 9.7 vs Table 2 | 수용 | 실험 설정 슬라이드는 Table 7 표기를 쓰되, Table 3의 SiT-L/2 400K 9.7이 Table 2의 DINOv2-B 행과 같고 DINOv2-L 행(10.0)과 다르다는 점을 토론 "근거" 후보로 둔다(설정 기록의 불일치). |
| V9 5.4 step/s 조건 | 수용 | 모델 크기 미명시. 비용 토론에서 "논문이 보고한 것은 처리량 하나뿐"으로. |
| V10 장부 | 수용 | Table 7은 8번 표 재구성 + 인용. Fig. 5a는 인코더 슬라이드에서 표 대신. |

## 조사(research) → `research_verified.md`

- R1 코드 MIT, ICLR 2025 Oral(arXiv 표기): 표지·ending.
- R2 HASTE(2505.16792): "초기 가속, 이후 정체·저하" — 토론점 근거(external). 논문 자체도 4M까지 FID가 계속 내려간다(6.4→5.9) — 두 서술을 나란히, 결론은 내지 않는다.
- R3 iREPA(2512.10794): "전역 성능이 아니라 공간 구조가 생성 성능을 좌우" — 이 논문의 가설(의미 표현의 질이 핵심, Fig. 5a의 Acc.–FID 상관)과 긴장. 깊이 실험(Acc.↑ FID↓ 반대 방향, Table 2)과 함께 토론점(external).
- R4 REPA-E, SRA: 배경/토론의 "이후 갈래" 한 줄 이하. 필요 없으면 생략.
- 쓰지 않음: OpenReview 토론 글의 GFLOPs·메모리 수치(열어 보지 않음).

## 목표 구조 (21장, 20분)

| # | 구간 | 슬라이드 | 블록 | 시간 |
|---|---|---|---|---|
| 1 | — | 표지 | cover (Fig. 1 곡선) | 0:30 |
| 2 | 요약 | REPA 요약 | statement | 0:55 |
| 3 | 배경 | 연구 배경 | groups | 0:55 |
| 4 | 배경 | 진단 ①: 분류 성능 격차 (Fig. 2a) | figure + bullets | 0:55 |
| 5 | 배경 | 진단 ②: DINOv2 정렬 (Fig. 2b–c) | figure ×2 + bullets | 1:00 |
| 6 | 방법 | REPA 구조 — **stepper(대표)** | diagram stepper | 1:15 |
| 7 | 방법 | 정렬 손실 | equation | 1:00 |
| 8 | 방법 | 실험 설정 | table + groups | 0:45 |
| 9 | 결과 | 정렬 후 표현 — **Fig. 3 탭** | toggle (image) | 1:10 |
| 10 | 결과 | SiT-XL/2 학습 곡선 (Fig. 1 곡선, 17.5×) | figure + deltas | 0:55 |
| 11 | 결과 | 400K step 비교 (Table 3) | bars + groups | 0:50 |
| 12 | 결과 | 생성 과정 비교 — **Fig. 4 탭** | toggle (image) | 0:55 |
| 13 | 결과 | CFG 시스템 비교 (Table 4) | table + deltas | 1:00 |
| 14 | 분석 | target 인코더 (Fig. 5a, Table 6) | figure + groups | 1:00 |
| 15 | 분석 | 정렬 깊이 (Table 2) | table + deltas | 0:55 |
| 16 | 분석 | 목적 함수와 λ (Table 2·5) | table + table | 0:50 |
| 17 | 분석 | SiT 크기별 수렴 (Fig. 5b–c) | figure ×2 | 0:50 |
| 18 | 분석 | 노이즈 수준별 격차 (Fig. 7, Fig. 8 한 줄) | figure + bullets | 0:45 |
| 19 | 분석 | 적용 범위 (Table 11·12) | cards | 0:40 |
| 20 | 정리와 토론 | 정리와 토론 | statement | 1:45 |
| 21 | 정리와 토론 | 감사합니다 · Q&A | ending | 0:15 |

합계 20:00. 인터랙티브 3장(6 대표, 9, 12). 토론점(20): 근거 — 깊이(Acc.와 FID가 반대로 움직임 + iREPA), 평가 설정(guidance interval을 고르고 같은 FID로 평가, sFID는 나빠짐), 설정 기록(Table 3 SiT-L 9.7 = Table 2 DINOv2-B 행) 또는 App. J 서술 / 대가(해석) — 학습 중 인코더 forward(처리량 5.4 step/s 하나만 보고), 후반 층의 정렬 하락(Fig. 3b·8)과 HASTE의 후반 정체.

## 개요 수정 이후 (Claude)

- **codex 읽기 실패.** codex 0.170의 Windows read-only 샌드박스가 Google Drive(G:) 폴더를 전혀 읽지 못했다.
  초안·수정본은 brief에 논문을 넣어 영향이 없었지만, 수정본은 Fig. 4를 열지 못했다고 적었고(12번 관찰은 Claude가 그림을 보고 씀),
  한국어 편집 1회차는 "access denied"만 돌려줬다. → `delegate.py`가 codex용 읽기 폴더를 로컬 임시 디스크에 복사해 넘긴다. 2회차 정상.
- **합성(deck.json).** 개요 v2의 21장 구조를 그대로 따랐다. Claude가 바꾼 것: 12번 클래스별 관찰을 그림을 직접 보고 쓰고 `note`로 표시,
  20번 토론 카드 문구 축약, 11번 막대 대신 표(모델마다 두 값과 Δ — 한 지표의 모델 비교지만 짝 비교라 표가 읽기 쉽다), 6번 stepper 도식을 새로 그림.
- **한국어 편집.** 92행 중 84행 적용. 기각 2(2번 "처방" 유지 — 발표 줄기, 3번 질문형 유지 — 배경 규칙), 수정 2(5·18번 캡션에서 빠진
  '곡선 근거' 표시 복원), 건너뜀 2(6번 단계 문구는 편집 뒤 이미 바뀜, 9번 notes는 숫자 바뀜 거부). `korean_rejected.md`.
- **눈으로 본 결함(기계 QA 통과 뒤).** 표지 "* 공동 1저자"(이 논문의 *는 공동 지도) → 엔진 수정 + 게이트. 17번 캡션이 그림 캡션 위로
  끼어듦 → QA가 못 잡음 → 검사 추가. 6번 도식 라벨 잘림 → QA가 SVG 안을 안 봄 → 검사 추가. stepper 뒤 단계는 캡처조차 안 됨 → 추가.
