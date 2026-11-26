`shots/1920/`·`shots/1024/` 전체 21장(13번 stepper 4단계, 15번 toggle 2상태 포함)과 [deck.json](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/rae/review/vis2/deck.json), [deck.css](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/rae/review/vis2/deck.css), [rae_ladder.svg](file:///G:/내%20드라이브/[9]Project/custom_SKILLs/hs-vilab-html-deck-skill/work/rae/review/vis2/rae_ladder.svg)를 직접 확인한 2차 검수 결과다.

**1차 처리 확인**: P0(15번 `Fig. 6b` 판독 불가)는 토글 전환으로 큰 축·곡선 라벨이 읽히게 개선됐고, **1·2·5·7·9·11·18·19·20번**의 수용·일부 수용 항목(표지 2행 교체, `Fig. 1` 확대, `valign: center`, 열 정렬, `wash` 통일, 토론 축약 등)은 회귀 없이 해결됐다(5번 `height: 315`와 18번 `.callout` 유지 사유 타당). 다만 **15·6·8·13번**에서 수정 회귀·미해결 결함이 확인됐다. (`DiT^{DH}` 위첨자 분리 없음, `valign: center` 11장 모두 자연스러움.)

---

### 지적 목록 (심각도 순, P0 없음)

- **[A1] 15번 (`scaling`, toggle 회귀) · P1** · `cols: [6, 14]`로 좌측 토글 그림(`x 112–585, y 273–870`)이 30% 폭에 좁게 묶이고, PNG 내부 흰 여백(~100px)·`.figure-mat`(20px)·2줄로 꺾인 `mediaCaption`(`y 895–970`) 때문에 실제 플롯 폭이 약 305px(`x 215–520`)에 그침. 반면 우측(`x 678–1808`)은 2줄 readout(`y 185–360`) 아래로 약 `1130×580px`의 거대한 빈 회색 공간(`y 360–940`)이 남고 하단 캡션(`y 940–970`)이 580px 떨어져 바닥에 고립됨. `s15-flops` 본문은 `S 6.07 → / XL 2.16`으로 화살표 뒤에서 끊김. · 그림이 중심이 아닌 좌측 띠처럼 축소돼 1024×768 `s15-compute`에서 소라벨 `RAE: DINOv2-B`가 여전히 뭉개지고 연노랑 `DiT-XL`·`SiT-XL`이 흐림. 우측 캡션의 소속감도 끊김. · `fig6a_flops.png`·`fig6b_compute.png`의 내부 흰 여백을 축·라벨에 바짝 재크롭(유효 높이 약 +100px), `slides[14].body[0]`에 `"cols": [9, 11]`(또는 `[8, 12]`, `mediaCaption` 1줄화로 +36px 추가)과 `"panel": true` 적용. 축 범위 `caption`은 `side`의 `caption` 블록으로 올려 readout 바로 아래에 붙이고, `states[0].text`는 `S\u00A06.07\u00A0→\u00A0XL\u00A02.16`으로 묶음.

- **[A2] 6번 (`recon`, 1차 A12 회귀·미해결) · P1** · `split` 아래로 옮긴 `lead`(`x 112–875, y 860–965`)가 하단에 붙으며 상단 표·그림(`y 185–630`)과 사이에 약 `225px`의 빈 띠(`y 630–855`)가 발생. `lead` 문장도 여전히 `남은 / 질문:`으로 분리됨. · `valign: "center"`가 없어 `.split { flex: 1 1 auto }`가 결론 문장을 바닥으로 밀어내 증거와의 연결이 끊기고, 1차 지적의 줄바꿈이 그대로 남음. · `slides[5]`에 `"valign": "center"` 추가(`.slide--center .split { flex: 0 1 auto }` 적용)하고 `slides[5].body[1].text`에 `남은\u00A0질문:`(NBSP)을 넣어 두 문장이 문장 경계에서 2줄로 나뉘게 수정.

- **[A3] 8번 (`overfit`, 1차 A4 잔존·정렬) · P1** · 공통 캡션 빈 띠는 해소됐으나, 좌측 `Fig. 3 왼쪽`(`x 112–950, y 265–747`, 캡션 `y 775`)보다 우측 `Fig. 3 오른쪽`(`x 1110–1755, y 268–760`, 캡션 `y 788`)이 약 13px 더 길게 그려져 두 패널의 `Loss 0.0` 축선과 개별 캡션 기준선이 어긋남. 열 사이(`x 950–1110`)에 약 160px 빈 띠가 남아 `height: 560`에 도달하지 못함. · 공통 캡션이 "두 패널 같은 손실 축(0–0.5)"을 강조하는데 두 `0.0` 축선이 수평 불일치하고, 1024에서 좌측 빨간 수식 `y = max(1 - x/768, 0)`과 상단 `Noisy Latent Dim n = 768`이 여전히 작고 흐림. · `slides[7].body[0].cols`를 `[54, 46]` → `[56, 44]`로 조정해 두 그림의 높이와 `0.0–0.5` 축선·캡션 기준선을 수평 일치시키고, `fig3_width.png`·`fig3_depth.png`의 좌우 여백 재크롭으로 실표시 크기를 키움.

- **[A4] 13번 (`ladder`, stepper, 1차 A3 회귀) · P2** · 기준선 라벨 대비(`fo-muted`), `4.81`·`4.28` halo·점선 간격, 단계별 막대·목록 연동과 회색→파랑→진한 파랑 색 위계는 모두 양호하나, 하단 캡션(`x 112–1080, y 810–875`) 첫 줄 끝에 가운뎃점 `·`가 단독으로 걸림(`guidance 없음 · / Table 2·4·5·6을 다시 그림`). · `Table\u00A02·4·5·6` 결합으로 줄이 밀리며 구분 기호가 줄 끝에 매달림. · `slides[12].body[0].caption`의 `없음 · Table`을 `없음. Table`로 변경.

- **[A5] 16번 (`benchmark`) · P2** · `w/o`·`w/` 헤더 구분과 1024 표 가독성은 양호하나, 하단 캡션(`x 112–1790, y 785–860`) 1–2행 경계에서 `14 epoch·scale / 1.42`로 지표명과 수치가 갈라짐. · 숫자와 수식어가 분리돼 스캔 흐름이 끊김. · `slides[15].body[1].text`에 `scale\u00A01.42`(NBSP) 적용.

- **[A6] 10번 (`shift`) · 14번 (`convergence`) · P2** · 10번 우측 패널 적용과 14번 조사 분리(A9)는 해결됐으나, 10번 패널 캡션(`x 1170–1750, y 580–650`)이 `노이즈 / 증강 전`으로, 14번 우측 캡션(`x 1135–1760, y 405–510`)이 `REPA / 5.90`으로 각각 복합어·모델명+수치가 줄 경계에서 분리됨. · 짧은 캡션에서 의미 덩어리가 쪼개져 정돈감이 떨어짐. · `slides[9].body[0].right[0].body[1].text`에 `노이즈\u00A0증강\u00A0전`, `slides[13].body[0].right[1].text`에 `REPA\u00A05.90` 적용.

---

### 통과
**1번 (`cover`), 2번 (`tldr`), 3번 (`background`), 4번 (`claims`), 5번 (`rae`), 7번 (`dit-fails`), 9번 (`theorem`), 11번 (`noise-aug`), 12번 (`ddt-head`), 17번 (`samples`), 18번 (`encoder-choice`), 19번 (`inputs`), 20번 (`discussion`), 21번 (`ending`)** — 위계, 정렬·여백, 1024 가독성, 일관성, 다크 대비·분량, 한국어 줄바꿈 모두 결함 없음.

---

### 가장 먼저 고칠 5가지
1. **15번 (`scaling`) `Fig. 6a·6b` 여백 재크롭 + `cols: [9, 11]` + `panel: true` [A1]**: 1024 `Fig. 6b` 소라벨 가독성을 끌어올리고 우측 `1130×580px` 빈 공간과 고립 캡션 회귀를 한 번에 해소.
2. **6번 (`recon`) `valign: "center"` + `남은\u00A0질문:` NBSP [A2]**: 225px 공백 회귀와 미해결 `lead` 줄바꿈을 동시에 정리.
3. **8번 (`overfit`) `cols: [56, 44]` + 여백 재크롭 [A3]**: 두 `Fig. 3` 패널의 `0.0–0.5` 축선·캡션 13px 어긋남을 맞추고 1024 수식 가독성 보강.
4. **13번 (`ladder`) 캡션 줄 끝 `·` 제거 [A4]**: 대표 stepper의 유일한 남은 회귀(`없음 · / Table`) 정리.
5. **16·10·14번 캡션 NBSP 3곳 (`scale\u00A01.42`, `노이즈\u00A0증강\u00A0전`, `REPA\u00A05.90`) [A5·A6]**: 전 덱 한국어 줄바꿈 마감 완료.
