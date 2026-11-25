[W1] must · 슬라이드 2 · `slides[1].body[1].items[0].text` · "Vanilla SiT의 표현은 DINOv2-g보다 linear probe 정확도와 정렬이 낮다 (Fig. 2)" · DINOv2-g는 정렬의 비교 기준(대상)이며, SiT의 DINOv2-g 정렬도는 MAE-L보다 높고 DINO-B·MoCov3-B보다 낮다(p. 2 Fig. 2b, p. 5 Sec. 3.2) · "Vanilla SiT는 DINOv2-g보다 linear probe 정확도가 낮고, DINOv2-g와의 정렬도 DINO-B·MoCov3-B보다 낮다 (Fig. 2)"

[W2] must · 슬라이드 6 · `slides[5].message` · "REPA는 SiT 8층의 MLP를 학습할 때 같은 이미지의 clean patch token을 목표로 쓴다." · REPA는 SiT 8층 hidden state $h_t=f_\theta(z_t)$를 별도의 투영 MLP $h_\phi$로 투영해 $\theta,\phi$를 함께 학습한다. "8층의 MLP"는 블록 내부 FFN만 학습하는 뜻으로 오독된다(p. 6 Sec. 3.3, Eq. 8) · "REPA는 SiT 8층 표현을 투영 MLP로 정렬해 학습할 때 같은 이미지의 clean patch token을 목표로 쓴다."

[W3] must · 슬라이드 9 · `slides[8].body[0].states[0].text`, `slides[8].message` · "4–24층 전 구간에서 REPA의 정확도가 vanilla보다 높다", "모든 층에서" · Fig. 3(a)(p. 3, `fig3a.png`)에서 x축 눈금은 4부터 시작하지만 실제 점은 6층부터 24층(짝수 층)까지만 그려져 있고 4층과 1–5·25–28층은 없다 · "6–24층 전 구간에서 REPA의 정확도가 vanilla보다 높다", "평가한 6–24층 모두에서"

[W4] must · 슬라이드 9 · `slides[8].body[0].states[1].text`, `states[1].alt`, `notes[1]` · "20–24층에서는 vanilla와 비슷하거나 낮다", "20층 이후에는 vanilla와 비슷하다/조금 낮습니다" · `fig3b.png`(p. 3 Fig. 3b) 확대 확인 결과 20·22층은 REPA가 vanilla보다 낮지만, **24층에서는 REPA(약 0.09)가 vanilla(약 0.05)보다 뚜렷하게 높다** · "20–22층에서는 vanilla보다 낮고 24층에서는 다시 높다"

[W5] must · 슬라이드 14 · `slides[13].body[0].left[0].alt` · "일곱 점이 오른쪽 아래로 내려가는 점선 근처에 놓인다." · Fig. 5(a)(p. 8)에는 대각선 추세 점선이 없고 7개 산점도와 수평 격자선만 있다 · "일곱 점이 오른쪽 아래 방향으로 분포한다."

[W6] must · 슬라이드 20 · `slides[19].body[0].groups[1].items[1]`, `provenance["토론 2"]`, `notes[2]` · "guidance interval을 FID로 골라 FID 1.42를 보고했다. sFID는 4.50 → 4.70." (`verbatim: App. E, Table 4, Table 10`) · App. E(p. 24)는 ADM reference batch 사용만 적으며 interval을 FID로 골랐다는 진술이 없다. Table 10(p. 25)에서도 $w=2.0$에서 `[0, 0.65]`(FID 1.44)가 `[0, 0.7]`(1.48)보다 낮은데 `[0, 0.7]`에서 $w$를 낮춰 최저 FID 행(1.42)을 Table 4에 보고했다. sFID 4.50 비교 행은 Table 4·9(p. 9·25)다 · "같은 평가셋으로 interval·$w$를 탐색해 Table 10 최저 FID 행(1.42)을 보고했다. sFID는 4.50(Table 4·9) → 4.70." 및 `provenance`: `verbatim(Table 4·9·10, App. E) + interpretation`

[W7] should · 슬라이드 1 · `slides[0].notes[0]` · "KAIST와 NYU 연구진의 ICLR 2025 oral 논문입니다." · p. 1 저자 소속은 KAIST, Korea University, Scaled Foundations, New York University 4개 기관이다 · "KAIST·고려대·Scaled Foundations·NYU 연구진의 ICLR 2025 oral 논문입니다."

[W8] should · 슬라이드 2 · `slides[1].body[0].text` · "noisy latent를 받는 SiT의 8층 표현을" · Table 7(p. 23)에서 SiT-B/2는 4층에 정렬하고, Table 3·12(p. 9·42)처럼 DiT·MMDiT에도 적용된다 · "noisy latent를 받는 SiT의 중간 층(XL/2 기준 8층) 표현을"

[W9] should · 슬라이드 5 · `slides[4].body[0].left[0].left[0].alt`, `slides[4].message` · "t=0, 0.25, 0.5 곡선이 20층 부근에서 약 0.14로 가장 높고", "다른 자기지도 인코더 수준에는 못 미친다" · Fig. 2(b)(p. 2)와 Fig. 7(b)(p. 10)에서 $t=0.25$ 최대값은 약 0.16–0.17(0.14–0.15는 $t=0, 0.5$)이고, SiT-XL/2는 MAE-L보다는 높다 · "20층 부근에서 약 0.14–0.17로 가장 높고", "DINO-B·MoCov3-B 같은 다른 자기지도 인코더 수준에는 못 미친다"

[W10] should · 슬라이드 7 · `slides[6].body[0].symbols[1]`, `symbols[4]`, `notes[1]` · "noisy 입력의 8층 token을 MLP로 투영", "SiT 실험은 0.5" · Eq. 8(p. 6)은 일반 층 정의(B/2는 4층, Table 2는 6–16층)이고, Table 5(p. 10)는 SiT-XL/2에서 $\lambda\in\{0.25, 0.5, 0.75, 1.0\}$을 비교한다 · "noisy 입력의 정렬 층(예: 8층) token을 MLP로 투영", "기본 SiT 실험은 0.5"

[W11] should · 슬라이드 9 · `slides[8].body[0].mediaCaption` · "**Fig. 3** REPA: SiT-XL/2, 8층, DINOv2-B target, 1M step. 한 모델의 층별 평가" · (a)(b)는 1M step 한 모델의 층별 평가(Table 7 p. 23)지만, (c)(`fig3c.png`)는 학습 step 진행(REPA 50K–1M, vanilla 50K–7M) 궤적이다 · "**Fig. 3** REPA: SiT-XL/2, 8층, DINOv2-B target. (a)(b) 1M step 층별 평가, (c) 학습 step 진행"

[W12] should · 슬라이드 12 · `slides[11].body[0].states[1].text`, `notes[1]` · "REPA에서는 200K에 하나의 열기구 형태가 나온다." · `fig4_balloon.png` 200K·400K에는 중앙 큰 열기구 외에 왼쪽 아래 작은 빨간 열기구가 함께 있어 총 두 개다 · "REPA에서는 200K에 온전한 열기구 형태가 나온다."

[W13] should · 슬라이드 13 · `slides[12].body[0].right[1].text`, `provenance["epoch–step"]`, `body[0].left[0].groups[1].rows[3].cells[4]` · "같은 checkpoint의 sampling 설정 차이 (Table 10)", `epoch–step: verbatim: Table 7`, IS `**305.7**` 굵게 · `+ REPA`(1.80, 4.50) 행은 Table 9(p. 25)에 있고 Table 10에는 없다. `800 epochs = 4M step`은 Table 4+7·9·10 조합(`derived`)이며, 표 안에 더 높은 IS(`MDTv2-XL/2*` 314.7)가 함께 있어 305.7 단독 볼드는 오해를 부른다(p. 9 Table 4는 순수 Transformer 군 내 최댓값) · "(Table 9·10)", `derived: Table 4, 7, 9, 10`, 순수 Transformer 내 최댓값임을 캡션에 명시하거나 314.7과 구분

[W14] should · 슬라이드 18 · `slides[17].body[0].right[0].items[1]` · "후반 층의 CKNNA는 vanilla 기준선보다 낮다." · Fig. 8(p. 10)은 각 target 인코더 기준 CKNNA이며, MoCov3-L은 16–24층이 기준선 아래지만 MAE-L은 16–22층이 기준선 위이고 마지막 24층 부근에서만 기준선 수준으로 내려간다 · "각 target 인코더 기준 CKNNA가 8층 부근에서 높고, 후반 층으로 갈수록 낮아져 MoCov3-L은 기준선 아래, MAE-L은 24층에서 기준선 부근에 닿는다."

확인됨: 슬라이드 3, 4, 8, 10, 11, 15, 16, 17, 19, 21은 수치·Δ·비율·조건·provenance·notes 모두 논문과 일치. 그 외 특별 점검 항목도 일치 확인됨 — 1번 저자 표기·`*`=`Equal advising`(p. 1), 6번 도식(`repa_stepper.svg`)의 고정 DINOv2-B(p. 6·22·23)·3층 SiLU MLP(App. D)·256 token·추론 미사용(App. B·D), 9번 1M step(Table 7)·`약 73%`(`fig3a`)·`약 0.53`(`fig3b`), 12번 해석 표시·앵무새·햄버거 서술(`fig4`), 13번 Table 4 행·`800 epochs = 4M step`·deltas(−0.38, +0.20), 14번 Table 6 데이터셋·DINOv2의 ImageNet-1K 포함(p. 22), 20번 토론 1·3·4 전제(Table 2·3·7, App. D, Fig. 3b·8, `research_verified.md` HASTE·iREPA).
