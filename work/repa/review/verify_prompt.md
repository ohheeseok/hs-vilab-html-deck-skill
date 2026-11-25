너는 이 발표 개요의 **검증자**다. 이 개요를 쓰지 않았다. 파일은 만들거나 고치지 말고 결과만 출력하라.

읽을 것(이 폴더): `outline.md`(검토 대상), `paper.pdf`(논문 원본, 표 수치는 반드시 PDF 쪽에서 확인), `paper.txt`(텍스트 추출본, 표의 줄이 깨져 있다).

할 일:
- 개요의 모든 주장·수치·비교·인과관계를 논문에서 찾아 쪽과 위치(§, Fig., Table, Eq., App.)를 대라. 찾지 못한 것은 "없음"으로 표시하라.
- 수치는 하나씩 표와 대조하라(행·열이 맞는지, 모델 크기·step·epoch·설정이 맞는지). Δ는 직접 다시 계산하라.
- 조건(벤치마크, 설정, 모델 크기, step, CFG 유무)이 빠진 수치, 논문보다 일반화해서 말한 결과, 저자의 설명(가설)을 사실처럼 쓴 곳을 표시하라.
- 그래프를 읽어서 쓴 서술(곡선의 최고점, 교차, 단조성)은 그림을 확대해서 확인하라. 표 수치가 아니라 곡선만 근거인 서술은 그렇다고 표시하라.
- 그림 장부가 본문 Fig. 1–8, Table 1–5를 빠짐없이 담는지, 각 `use` 슬라이드가 그 그림을 정말 필요로 하는지 보라.
- 특히 확인:
  - 2·9번 "400K step FID 7.9 vs vanilla 7M 8.3, 17.5×"의 조건(no CFG, SiT-XL/2, Table 3)
  - 5번 "7M SiT-XL/2의 일부 층은 MAE-L 기준선 상회", CKNNA 조건(10,000장, k=10)
  - 6번 "3층 SiLU MLP projector", "projector는 학습 때만 사용"
  - 8번 Table 7의 모델별 정렬 층·target·목적 함수(B/2 layer 4, L/2 DINOv2-L + NT-Xent 등)
  - 12번: "4M step"과 "800 epochs"가 같은 checkpoint인지, w=1.50(vanilla)·w=1.35·interval [0,0.7]·w=1.80의 출처(App. G, Tables 9–10)
  - 13번 Fig. 3의 REPA 모델 설정(1M step, DINOv2-B, layer 8, cosine)
  - 14–17번 Table 2·Table 5 수치 전부와 Δ
  - 18번 Table 8의 200K 행(FID / Acc.)
  - 20번 Table 11·12 수치, "H100 8장, 약 5.4 step/s"
  - 21번 토론 포인트의 사실 전제: App. J의 "네 지표 개선" 서술과 Table 11의 precision·sFID, guidance interval 설정 선택과 평가에 같은 FID를 썼는지(App. G)
  - 22번 코드 주소(본문에 GitHub 주소가 있는지)

출력(한국어, 1100단어 이내): 번호 매긴 지적. 각 지적은 `[V번호] must|should · 슬라이드 n · 개요의 서술 · 논문의 실제(쪽·위치) · 고칠 문구`. 문제 없는 슬라이드는 묶어서 한 줄로 "확인됨: n, m, …".
