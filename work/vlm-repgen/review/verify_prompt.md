너는 이 발표 개요의 **검증자**다. 이 개요를 쓰지 않았다. 파일은 만들거나 고치지 말고 결과만 출력하라.

읽을 것(이 폴더): `outline.md`(검토 대상), `paper.pdf`(논문 원본, 표 수치는 반드시 PDF 쪽에서 확인), `paper.txt`(텍스트 추출본, 표의 행이 한 칸씩 줄로 끊겨 있다).

할 일:
- 개요의 모든 주장·수치·비교·인과관계를 논문에서 찾아 쪽과 위치(§, Fig., Table, Eq., App.)를 대라. 찾지 못한 것은 "없음"으로 표시하라.
- 수치는 하나씩 표와 대조하라(행·열, 모델 크기, step, 평가자(GPT-4.1/GPT-4o), CoT·rewritten prompt 표시 †·§). Δ와 비율은 직접 다시 계산하라.
- 조건(학습 step, 해상도, 백본 크기, 평가 벤치마크)이 빠진 수치, 논문보다 일반화해서 말한 결과, 저자의 가설·해석을 사실처럼 쓴 곳을 표시하라.
- 그래프를 읽어서 쓴 서술(곡선의 값, 교차, 끝까지 위인지)은 그림을 확대해서 확인하라. 표 수치가 아니라 곡선만 근거인 서술은 그렇다고 표시하라.
- 그림 장부가 본문 Fig. 1–9, Table 1–6을 빠짐없이 담는지, 각 `use` 슬라이드가 그 그림을 정말 필요로 하는지 보라.
- 특히 확인:
  - 7–8번 App. A.1의 수치(27블록, patch 16, d_h 1152, 28개 표현, 4층씩 7개, 16 head, d_f 1152, d_z 256, ViT-XL 디코더 28층·1152, 2×2 병합, d_s 4096), Eq. (6)과 본문 "MSE and cosine-distance"의 차이
  - 9번 App. A.1(32층, 4층 간격 8블록, d_g 2048, 2층 MLP, DDT head 2블록·3072, adaLN-single), "0.89B"의 출처와 Fig. 9의 891M과의 관계, App. C.2의 "31 VLM layers"와 32층의 관계
  - 10번 Table 7의 단계별 step·해상도(어느 단계가 256², 어느 것이 ≤512), 학습률, "VLM 동결"의 근거, time shift 4.0
  - 11번 Table 1·2 수치와 Δ(POPE, MMB, MMMU, OCRBench), 99.8%의 정의(Avg. Retention20)
  - 12번 Table 3의 Integral·BAGEL·TUNA-2·Qwen3.5-9B 행 각 열, GenEval2 39.56§의 조건, ImgEdit Table 4
  - 13번 Table 5·6 수치와 Δ, FLUX.2-dev 56B, Fig. 2의 예시 설명(Saturn, Venetian Carnival)
  - 14번 0.41/0.18, 32.2/31.1(이 PSNR이 같은 조건에서 잰 것인지: Table 1의 AF는 전체 학습 후 tokenizer, Fig. 6의 AF는?), "같은 VLM 조건"의 근거
  - 15번 SigLIP2-AF 0.31, Table 9의 SigLIP2 PSNR 34.08과 zero-shot accuracy 값, "Qwen AF 32.20"
  - 16번 Fig. 6b의 +0.13/+0.01과 곡선(LLM + AF가 VLM + FLUX.1-VAE보다 위인지)
  - 17번 Table 11, Fig. 10 세 지표가 끝까지 AF보다 낮은지
  - 18번 Fig. 7, 0.26, 32.33 dB, 99.2%
  - 19번 +6.27 dB의 조건(20K step), Fig. 8의 cosine 서술, 891M vs 962M
  - 20번 Table 12·13 수치, 2.1%·7.3%를 표 값으로 다시 계산, 2.5×·3.1×
  - 21번 토론 네 항목의 사실 전제(특히 2번: 본문 Lsem 서술과 Eq. (6)이 정말 다른지, 3번: Fig. 7에 2B×FLUX.1-VAE가 없는지)

출력(한국어, 1100단어 이내): 번호 매긴 지적. 각 지적은 `[V번호] must|should · 슬라이드 n · 개요의 서술 · 논문의 실제(쪽·위치) · 고칠 문구`. 문제 없는 슬라이드는 묶어서 한 줄로 "확인됨: n, m, …".
