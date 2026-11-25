# 자료조사 확인 (출처에서 직접)

agy 자료조사(`research.md`)를 Claude가 출처 페이지에서 다시 확인했다. 이 파일에 있는 것만 슬라이드에 `external`로 쓴다.

| 사실 | 확인한 곳 | 결과 |
|---|---|---|
| 공식 코드 `github.com/sihyun-yu/REPA`, MIT License | GitHub API (`gh api repos/sihyun-yu/REPA`), README | 확인. README가 arXiv와 프로젝트 페이지로 링크 |
| ICLR 2025 Oral | arXiv 2410.06940 comment 줄 "ICLR 2025 (Oral)", 최신판 v4 2025-06-18 | 확인. OpenReview에서는 형식 미확인(agy) — arXiv 표기를 근거로 씀 |
| HASTE — "REPA Works Until It Doesn't" (arXiv 2505.16792, 2025-05-22) | arXiv 초록 | 확인. 초록: REPA는 초기 epoch를 크게 가속하지만 이후 정체하거나 성능이 떨어진다, 용량 불일치 탓으로 보고 일정 시점 뒤 정렬 손실을 끈다. 학회 표기 없음 |
| iREPA — "What matters for Representation Alignment: Global Information or Spatial Structure?" (arXiv 2512.10794, 2025-12-11) | arXiv 초록 | 확인. 초록: target 표현의 전역 성능이 아니라 공간 구조가 생성 성능을 좌우한다. 학회 표기 없음 |
| REPA-E (arXiv 2504.10483, 2025-04-14) | arXiv 초록 | 확인. REPA 손실로 VAE와 확산 모델의 end-to-end 학습이 가능해진다 |
| SRA (arXiv 2505.02831, ICLR 2026) | arXiv 초록, comment 줄 | 확인. 외부 표현 없이 모델 자기 표현으로 정렬. 초록은 REPA를 이름으로 들지 않음 |

쓰지 않는 것
- U-REPA, Dispersive Loss: 초록 미확인(이번 덱의 토론에 필요 없음).
- HASTE OpenReview의 23.19 GFLOPs, 27,818 MB: OpenReview 토론 글이라 직접 열어 보지 않았다 → 쓰지 않음. 비용 토론점은 논문 App. D의 서술(인코더 forward, 처리량만 보고)에서 끌어낸 해석으로 둔다.
- 후속 연구의 1.42 재인용 여부: 덱의 주장에 필요 없음.

논문 안에서 확인한 것(조사 중 같이 본 것)
- App. D p. 23: 사전 계산하는 것은 **VAE latent**이고, 인코더 feature를 사전 계산한다는 서술은 없다. projector는 SiLU 3층 MLP, 패치 수가 다르면 인코더의 positional embedding을 보간한다. 8×H100 80GB, batch 256에서 약 5.4 step/s(모델 크기 미명시).
- App. C Table 6 p. 22: ImageNet-1K를 쓰지 않은 CLIP(WIT-400M) 11.0, SigLIP(WebLi-4B) 10.2. DINOv2(LVD-142M)는 "w/ ImageNet-1K: O"로 표시돼 있다 — 가장 좋은 target은 ImageNet을 포함한 데이터로 학습됐다.
