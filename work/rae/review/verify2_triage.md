# verify2 (deck.json 검증 2차) — 처리

| ID | 처리 | 결정 |
|---|---|---|
| W1 11번 증강 목적 문구 | 수용 | "인코더 latent에 노이즈를 섞어 학습해, 확산이 생성한 latent에도 대응" — 디코더는 생성 latent로 학습하지 않는다 |
| W2 14번 기준점 | 수용 | 내가 쓴 "Table 8의 balanced 값(8.61·5.78)"이 틀렸다: SiT 8.61은 random, balanced는 8.54. Fig. 4의 8.26은 어느 값과도 다르다 — 캡션과 notes 수정 |
| W3 15번 alt "L 약 2.4" | **기각** | 조율자가 Fig. 6a를 확대해 확인: DiT^DH-L 점은 2.5 눈금선 **아래**(약 2.36). 라벨 글자가 점 위에 있어 검증자가 라벨 위치를 읽었다. 곡선 읽기는 조율자가 그림에서 확인한다는 규칙이 세 번째 덱에서도 필요했다 |
| W4 18번 message | 수용 | "DiT-XL에서는" 조건 추가 (DiT^DH-XL은 S→B 개선, L 악화) |
| W5 3번 ReDi | 수용 | ReDi는 정렬이 아니라 DINOv2 PCA를 함께 생성 |
| W6 7번 가설 1 | 수용 | 논문은 "design choices" 전반; 폭은 4.1의 결론 |
| W7 8번 "손실 0" | 수용 | "0에 가깝게", "거의 그대로" |
| W8 9번 하한 | 수용 | $(n-d)/n$은 차원당 평균 손실의 하한. 원문 ✓/✗는 번들 글꼴에 없어 ○/×로 그리고 "논문의 체크 표시"라고 적는다 |
| W9 12번 675M | 수용 | 675M은 VAE 기반 DiT-XL |
| W10 13번 마지막 막대 | 수용 | message에 "DDT head와 전용 최적화", SVG 출처 줄 "Table 6 · App. D", `<desc>` 보강 |
| W11 20번 guidance·R9 | 수용 | App. I는 scale sweep만 명시 → "scale을 sweep해 고른 1.42와 기본(20)과 다른 14 epoch guide". DINOv2는 "(LVD-142M)"까지 |
