# Korean edits not applied (conductor)

표현(representation)은 개념어로 유지, message는 발화 문장 유지, 제목 첫 글자 유지.

- `1.subtitle`: 외부 encoder 없이 flow matching 안에서 표현을 학습하는 Self-Flow → ~~외부 encoder 없이 flow matching 과정에서 feature를 학습하는 Self-Flow~~
- `1.notes.0`: 오늘은 Black Forest Labs의 Self-Flow를 소개합니다. 생성 모델이 외부 encoder 없이 스스로 표현을 배우게 하는 방법이고, 그 근거가 어디까지인지를 함께 보겠습니다. → ~~오늘은 Black Forest Labs의 Self-Flow를 소개합니다. 생성 모델이 외부 encoder 없이 자체 feature를 학습하는 방법입니다. 이 방법에 대한 설명을 실험이 어디까지 뒷받침하는지도 살펴보겠습니다.~~
- `2.body.0.text`: 외부 encoder 없이, noise 수준이 다른 두 입력의 표현을 맞춰 flow matching 안에서 표현을 학습한다. → ~~외부 encoder 없이 noise 수준이 다른 두 입력의 feature를 맞춰 flow matching 과정에서 feature를 학습한다.~~
- `4.body.0.right.0.items.2.text`: 저자 설명: 고정된 외부 표현이 생성 목표와 어긋나 병목이 된다 → ~~저자 설명: 고정된 외부 feature가 생성 목표와 맞지 않아 생성 성능을 제한~~
- `4.notes.1`: 저자들은 고정된 외부 표현이 생성 목표와 맞지 않아 병목이 된다고 설명합니다. 이 설명 자체는 실험으로 확인한 것이 아니라 해석이라는 점을 짚어 두겠습니다. → ~~저자들은 고정된 외부 feature가 생성 목표와 맞지 않아 생성 성능을 제한한다고 설명합니다. 이 설명은 저자의 해석입니다. 실험에서 이 원인을 확인하지는 않았습니다.~~
- `18.title`: Timestep 분포와 low-SNR 구간 → ~~timestep 분포와 low-SNR 구간~~
- `21.message`: 어떤 비교가 Self-Flow의 작동 기전을 가장 잘 가려낼 수 있을지 함께 논의한다. → ~~Self-Flow의 작동 기전을 가장 잘 가려낼 비교 방법 논의~~
