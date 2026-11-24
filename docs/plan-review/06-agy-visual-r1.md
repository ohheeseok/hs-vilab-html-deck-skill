- **[V01] s01 · P1** · 좌하단 Fig. 1`(112–1160, 500–915)`이 높이 제약으로 축소돼 `1024×768`에서 (a) 범례(`Self-Flow (Ours)`), `Vanilla Flow Matching (1M)`, 축 눈금(`200K–1.0M`), (b) 이탤릭 프롬프트·세로 `Time`이 뭉개져 판독 불가. 동시에 그림 오른쪽 끝(`x≈1160`)과 발표자 열(`x≈1428`) 사이에 ~270px 공백이 생기고, 캡션`(112–1320, 935–1008)`은 그림 폭을 ~160px 넘기며 `이미지·` / `비디오`로 끊김(발표자·크레딧 위계와 로고 크기는 적절). · `PLAN.md §7`(1024×768 원본 그림 라벨 가독성), 한국어 줄바꿈·균형 위반. · `.slide--cover` 상하 패딩 `72px→56px`, `.cover-rule` `margin-top: 40px→24px`, `.slide--cover .cover-grid` `margin-top: 40px→28px`, `.cover-grid` `grid-template-columns: 1fr 360px; gap: 56px`로 그림 높이를 키우고, `deck.json` `slides[0].figure.caption`을 1줄로 줄여 `<span class="nw">이미지·비디오</span>` 적용.

- **[V02] s03-dual · P1** · `1024×768`에서 도식 `Teacher 입력 x_{τ_min}` `(775–1025, 280–315)`의 이중 아래첨자 `min`이 뭉개지고, `f_{θ'} teacher` `(880–1080, 880–930)`의 프라임(`'`)이 거의 안 보여 `f_θ student`와 기호 구분이 어려움. 우측 기호표 `(1300, 600–655)`·좌측 `L_gen` `(148, 900)`의 TeX SVG 아래첨자는 CSS `sub` 하한(`24px`)을 받지 않아(추정) `1024×768`에서 작게 보임. · `PLAN.md §3`(24px 하한)·`§7`(1024×768 가독성). · `figures/dia_dual_timestep.svg`에서 `x_{τ_min}`을 `τ_min` 단일 첨자(`≥24px`)로 풀고 `f_{θ'}`는 프라임 크기·간격을 키우거나 `EMA teacher (θ')`로 표기; `.symbols dt` SVG 수식을 `1.15×` 확대 또는 `font-size: 28px`로 상향.

- **[V03] s03-vanilla·s03-dual · P1** · Vanilla→Dual 토글 시 우측 패널 하단이 `y≈660`에서 `y≈785`로 ~125px 내려오며, 그 아래 고정 캡션 `(1272–1808, 795–965 → 820–992)`이 아래로 밀려 푸터 선(`y≈1012`)과 ~18px만 남음(줄간격 `1.45` 축소 후에도 밀착). · 여백 리듬(`.slide-body` 하단 `40px`) 훼손 및 상태 전환 시 정적 요소 점프. · `.toggle-side .panel`에 `min-height: 580px; padding: 24px 32px`, `.toggle-side` `gap: 24px` 적용하고, `deck.json` `slides[2].body[0].caption`을 3–4줄로 압축해 푸터 상단 여백 `≥36px` 확보.

- **[V04] s03-dual · P1** · `L_rep cosine` 화살표 `(505–865, 870–895)`의 선분은 `#048DDB`인데 왼쪽 끝 화살촉 삼각형만 `#626466` 회색으로 그려짐(하단 EMA 점선 화살표 `<marker>` 공유 추정). · `design-system.md §9.2` SVG 토큰 일관성 결함. · `figures/dia_dual_timestep.svg`에 `fill="var(--color-accent)"`(`#048DDB`) 전용 `<marker id="arrow-accent">` 추가(또는 `fill="context-stroke"`).

- **[V05] s04 · P1** · 우측 패널 `(1208–1808, 185–760)`이 1번(`−0.31` FID)은 증감치(delta)인 반면 2번(`167.98` FD-DINO)·3번(`30.88` CLIP score)은 절대값을 동일 `56px` `.delta-value` 틀에 혼재. `↓`/`↑` 표시와 CLIP 기준치도 빠져 `s05`(순수 증감치만 배치)와 불일치하며 방향 오독 소지 있음. · 일관성(델타 수치) 및 `design-system.md §9.3` 명확성 위반. · `deck.json` `slides[3].body[0].right[0].body[0].items`의 `FD-DINO`·`CLIP score`를 REPA 대비 증감치(`−5.37` 등)로 통일하거나, 절대값 유지 시 `label`에 `↓`/`↑`와 기준 모델 수치를 일관 병기.

- **[V06] s04 · P1** · 막대 차트 세로 격자선 `1–5` `(515–995, 245–790)`가 `.slide--wash`(`#F3F4F4`) 위에서 `#E4E5E5`(`--chart-grid`)로 그려져 명도 차가 ~1.14:1에 불과해 `1024×768`에서 사실상 소실됨(`deck.css`가 `.slide--wash`에서 표·푸터 선만 `#B9BABB`로 올리고 차트 격자선은 누락). · `design-system.md §9.3`·`PLAN.md §7` 가독성 위반. · `deck.css` `.slide--wash`에 `--chart-grid: var(--hs-grey-40);`(`#B9BABB`) 추가.

- **[V07] s02 · P1** · 다크 배경(`#12263D`) 푸터의 미진행 구간(`방법`·`결과`·`정리와 토론`) 상단 바 `(380–1480, 1018)`가 `#263142`(`--color-border-subtle`)로 그려져 대비가 ~1.2:1에 그치며 `1024×768`에서 거의 보이지 않음. · `PLAN.md §1`(진행 표시줄의 구조 정보 전달) 및 프로젝터 다크 대비 저하. · `deck.css` `.slide[data-theme="dark"] .progress li::before`를 `background: var(--divider)`(`#4A5D78`), `.is-past::before`를 `var(--color-border-control)`(`#6B7D96`)로 조정.

- **[V08] s03, s04, s05 · P1** · `s02`와 달리 `s03`·`s04`·`s05` 상단 `(112–1808, 72–185)`에 주제명만 있고 `deck.json`의 핵심 문장(`message`)이 화면에 노출되지 않아, 근거(도식·막대·표)를 본 뒤 `24px` 캡션·보조문구에서 결론을 역추론해야 함. · 위계(`message`→근거 읽기 순서) 약화. · `deck.json` `slides[2..4]`의 `title`을 1줄 결론형으로 바꾸거나, `.slide-title` 아래 `28px` 1줄 요약 슬롯 도입.

- **[V09] s03 · P2** · 캡션 `(1272–1808, 820–992)`이 `s01`·`s04`·`s05`(왼쪽 시각물 아래 + 굵은 `**Fig./Table**` 접두어)와 달리 오른쪽 패널 아래에 떨어져 있고 `Fig. 3`이 굵지 않음. · `design-system.md §7` Figure·캡션 일관성 저하. · `deck.json` `slides[2].body[0].caption`을 `**Fig. 3** 재구성. ...`으로 통일.

- **[V10] s05 · P2** · ① 표 `FID ↓` 열 `SiT-XL/2`만 소수 1자리(`8.3`, 원논문 표기 추정)라 소수점 세로 정렬이 어긋남`(560–640, 355)`. ② 캡션은 상위 4모델과 RAE 2모델을 별도 비교군으로 묶지만 `REPA`/`RAE` 경계선`(112–1210, 645)`이 일반 행선과 동일. ③ 우측 델타 둘 다 라벨이 `FID`로 같아 작은 글을 읽어야 비교 쌍이 구분됨`(1336, 290 & 485)`. ④ `#F3F4F4` wash 위 `#E6F4FC` 강조 행과 `#E4E5E5` 패널 테두리(`s04` 포함)가 프로젝터에서 흐려질 수 있음. · `design-system.md §4`·`§7`. · ① `8.30` 확인 가능 시 통일(불가 시 `8.3` 뒤 `&#8199;`로 소수점 정렬), ② RAE 그룹 상단 `2px solid var(--hs-grey-70)`(`#8A8C8E`) 구분선 추가, ③ `deck.json` `slides[4]` 델타 `label`을 `FID (vs REPA)`·`FID (RAE 추가)`로 구분, ④ `deck.css` `.slide--wash .panel` `border-color: var(--hs-grey-40)`(`#B9BABB`).

- **[V11] s04 · P2** · ① 차트 끝(`x≈995`)과 우측 패널(`x≈1208`) 사이에 ~213px 빈 회색 띠가 생김(최대값 `4.08` 대비 축 상한 `5` + 좌측 열 내 SVG 우측 여백 추정). ② 우측 패널 `FD-DINO` 설명 `(1236–1770, 500–565)` 마지막 줄에 `낮다` 2글자 고아 줄 발생. · 여백 리듬 및 한국어 줄바꿈 결함. · ① 차트 x축 상한 `4.5` 및 좌측 열 폭 맞춤(`cols: [11, 5]` 검토), ② `deck.json` `slides[3]` `FD-DINO` `small`을 `"REPA 173.35. DINOv2 거리에서도 낮다"`로 축약.

- **[V12] s06 · P2** · 우측 `토론` 3번 `[해석]` 배지 `(1064–1135, 705–740)`가 `vertical-align: .18em` 때문에 `3`·`Fig. 4b에서` 기준선보다 위로 떠 보이고, 다크 배경 위 `1px` `#3A7FB8` 테두리가 `1024×768`에서 약함. · 정렬·다크 가독성 다듬기. · `deck.css` `.note-label` `vertical-align: .05em; padding: 5px 10px;`, `.slide[data-theme="dark"] .note-label` `border-width: 1.5px; border-color: var(--color-link);`(`#58B8F2`).

- **[V13] s02 · P2** · 리드 문장 `(1530, 315 → 112, 375)`에서 `EMA` / `teacher의`가 분리되고, `방법` 1번 `(148–880, 560–650)`에서 `(이미지에서` / `25%)에`로 괄호·수치가 끊김. · 한국어 줄바꿈 다듬기. · `deck.json` `slides[1]`에서 `EMA teacher`와 `(이미지에서 25%)`에 줄바꿈 방지(`.nw`) 적용.

*(통과 슬라이드: 없음 — `s06`이 P2 1건으로 가장 안정적)*

### 가장 먼저 고칠 3가지
1. **s01 표지 공간 회수**: 상하 패딩·가로선 여백·1줄 캡션으로 Fig. 1을 키워 `1024×768` 그래프 가독성과 우측 270px 공백을 동시에 해소한다.
2. **s03 도식·토글 안정화**: `x_{τ_min}`/`f_{θ'}`·수식 아래첨자 가독성을 높이고, 하늘색 화살촉 색상 불일치와 토글 시 패널 점프·캡션 하단 밀착을 잡는다.
3. **s04·s02 프로젝터 대비·데이터 일관성**: `s04` 델타 패널의 증감치/절대값 혼재를 정리하고, `s04` wash 격자선(`#B9BABB`)과 `s02` 다크 푸터 미진행 바(`#4A5D78`) 대비를 올린다.
