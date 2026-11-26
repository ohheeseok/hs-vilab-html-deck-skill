1. **must · `build_deck.py:828–829, 953`, `deck.js:13–19, 372–376`**  
   번들이 스크립트를 `<head>`의 기존 위치에 인라인하면 덱 전체가 초기화에 실패한다. 인라인 일반 스크립트에는 `defer`가 적용되지 않아 `deck.js`가 슬라이드 DOM보다 먼저 실행된다. `fit()`에서 `stage`가 `null`인 채 예외가 나고, `no-js`는 이미 제거됐으며 QA 훅도 등록되지 않는다. 뒤이어 실행되는 애니메이션 스크립트도 바인딩할 슬라이드를 찾지 못한다. 슬라이드 마크업 뒤에 `deck.js`, 애니메이션 스크립트 순으로 배치하면 외부 스크립트와 인라인 번들 모두 같은 순서로 초기화된다. [engine.diff](/C:/Users/Public/Documents/ESTsoft/CreatorTemp/hsdeck-suwt2abc/engine.diff:369)

2. **must · `deck.js:109–134, 142–165, 195–207`**  
   `render(t)`가 재생 중간에 한 번 던지면 `tick()`이 다음 rAF를 예약하기 전에 중단되지만 `play`는 남는다. 화면은 중간 프레임에 멈추고 다음 키는 멈춘 구간을 끝내는 데 소비된다. 끝 프레임에서도 예외가 나면 강제 완료가 다시 실패하고, 그 경로를 먼저 호출하는 G와 M도 동작을 끝내지 못한다. 첫 렌더 역시 바인딩의 `try` 밖에 있다. 모든 렌더 호출에 공통 오류 처리를 적용해 재생을 취소하고, 실패한 인스턴스를 해제한 뒤 원본 SVG와 마지막 설명을 복원해야 한다. [deck.js](/C:/Users/Public/Documents/ESTsoft/CreatorTemp/hsdeck-suwt2abc/deck.js:142)

3. **must · `deck.js:195, 219–222, 297–309, 335–338`**  
   G로 연 개요에서 화살표로 애니메이션 슬라이드를 선택하면 완성 썸네일이 첫 그림으로 바뀐다. G로 들어갈 때는 마지막 비트를 그리지만, 개요의 화살표가 호출하는 `go(cur)`는 비트를 0으로 설정한다. 개요에서 `#/n/1`로 해시를 바꿔도 썸네일이 중간 비트로 바뀐다. 개요가 열린 동안에는 선택과 포커스만 갱신하고, 첫 그림이나 해시의 비트는 발표 화면으로 돌아올 때 적용해야 한다. [deck.js](/C:/Users/Public/Documents/ESTsoft/CreatorTemp/hsdeck-suwt2abc/deck.js:335)

4. **must · `deck.js:108–115, 195–208`, `build_deck.py:245–256`, `qa_render.py:285–299`**  
   애니메이션 스크립트를 빼거나 `DeckAnim.define("이름", …)`을 주석에만 남기면, 완성 SVG에 첫 비트 설명이 붙고 다음 키는 그림이 그대로인 비트들을 소비한다. 주석만 남긴 경우 빌드의 등록 검사도 통과하며, QA는 `beats()`가 빈 배열이면 애니메이션 검사를 건너뛴다. 두 제공 스크립트처럼 `lib.node(k)`로 키를 조회하면 SVG에서 필요한 요소를 빠뜨려도 빌드의 리터럴 검색은 잡지 못한다. QA에서 `data-anim-name`과 `data-beats`를 기준으로 실제 바인딩과 비트 수를 확인하고, 로드에 실패한 슬라이드는 마지막 설명을 표시한 채 다음 키로 바로 넘어가게 해야 한다. [engine.diff](/C:/Users/Public/Documents/ESTsoft/CreatorTemp/hsdeck-suwt2abc/engine.diff:288)

5. **must · `deck.js:124–128, 153–157`**  
   `beats: ["0", "1.4", "3.2", "4.2"]`가 바인딩을 통과한다. 두 번째 구간을 재생하면 `"1.4" + 0.016`이 문자열 결합을 일으켜 `p.t`가 `NaN`이 되고, 종료 조건을 만족하지 못해 rAF가 계속 예약된다. 바인딩할 때 비트가 유한한 숫자의 배열인지, 개수와 증가 순서가 맞는지, `render`가 함수인지 검증해야 한다. [deck.js](/C:/Users/Public/Documents/ESTsoft/CreatorTemp/hsdeck-suwt2abc/deck.js:124)

6. **should · `deck.js:27–33, 349–354`**  
   OS의 모션 감소를 켜고 `?motion=0`으로 연 뒤 M을 누르면 “모션 켬”이 표시되지만 다음 비트는 여전히 점프한다. M이 `no-motion` 클래스만 제거하고 `still()`은 다시 OS 설정을 따르기 때문이다. M을 길게 누르면 키 반복마다 설정이 뒤집힌다. M은 현재 적용 중인 설정을 명시적인 켬 또는 끔으로 뒤집고, 상태 알림도 그 값으로 만들며, `e.repeat`는 무시해야 한다. [deck.js](/C:/Users/Public/Documents/ESTsoft/CreatorTemp/hsdeck-suwt2abc/deck.js:349)

7. **should · `deck.js:59–66, 109–111, 195, 219–222`**  
   마지막 비트가 3인 슬라이드를 `#/n/99`로 열면 그림은 비트 3인데 `data-step`은 99이고 현재 비트 표시가 사라진다. 이전 키를 눌러도 98로만 내려가 화면이 그대로다. 해시에서 받은 비트를 `0..data-steps`로 제한한 뒤 그림과 설명에 같은 값을 써야 한다. [deck.js](/C:/Users/Public/Documents/ESTsoft/CreatorTemp/hsdeck-suwt2abc/deck.js:195)

8. **should · `deck.js:239–243, 268–276, 361–366`**  
   토글 버튼 A에 키보드 포커스를 둔 채 `2`로 B를 선택하고 `→`를 누르면 B가 한 번 더 선택된다. 숫자 키는 선택과 `tabIndex`를 B로 옮기지만 포커스는 A에 남고, 방향키는 A를 기준으로 계산한다. 그룹 내부에 포커스가 있을 때 숫자 키로 선택한 버튼으로 포커스도 옮겨야 한다. [deck.js](/C:/Users/Public/Documents/ESTsoft/CreatorTemp/hsdeck-suwt2abc/deck.js:268)

9. **must · `build_deck.py:638–648`**  
   `prefix_ids`는 `data-id="icon"`을 `data-id="a4-icon"`으로 부분 치환한다. 같은 SVG에 `id="icon"`이 있으면 상대 경로 `href="icon"`도 `href="a4-icon"`으로 바꿔 이미지가 깨진다. 반대로 `href='#icon'`, `url( #icon )`, `aria-controls="icon"`은 그대로 남아 접두어가 붙은 ID를 가리키지 못한다. SVG를 파싱해 실제 `id` 속성의 매핑을 만든 뒤 `href`와 `xlink:href`의 로컬 프래그먼트, CSS `url()`의 로컬 참조, ARIA IDREF 속성만 갱신해야 한다. 제공된 두 SVG의 `aria-labelledby` 형식은 현 구현에서도 정상 치환된다. [engine.diff](/C:/Users/Public/Documents/ESTsoft/CreatorTemp/hsdeck-suwt2abc/engine.diff:315)

10. **must · `build_deck.py:129–137, 950–953`**  
    서로 다른 두 스크립트가 같은 애니메이션 `name`을 선언하면 둘 다 개별 검사를 통과하지만, 복사 단계에서 뒤쪽 스크립트 하나만 남아 두 슬라이드에 바인딩된다. SVG 키와 비트 개수가 같으면 앞 슬라이드에서 잘못된 애니메이션이 오류 없이 재생된다. 같은 이름을 재사용할 때는 같은 스크립트 경로인지 빌드에서 확인해야 한다. [engine.diff](/C:/Users/Public/Documents/ESTsoft/CreatorTemp/hsdeck-suwt2abc/engine.diff:398)

11. **should · `build_deck.py:226–256`**  
    `// setTimeout은 엔진이 관리한다`라는 주석이 있는 정상 JS와 `<g data-anim='x'>`를 `lib.node("x")`로 찾는 정상 SVG가 각각 거절된다. 반대로 `<image href='https://example.invalid/image.svg'>`는 원격 참조 검사에 걸리지 않는다. JS는 주석과 문자열을 구분해 실제 구문을 검사하고, SVG는 파싱한 요소와 속성의 URL 값을 검사해야 한다. [engine.diff](/C:/Users/Public/Documents/ESTsoft/CreatorTemp/hsdeck-suwt2abc/engine.diff:267)

12. **must · `qa_render.py:34–49, 290–299`**  
    `DETERMINISM`은 정지점만 비교해 중간 프레임의 상태 의존성을 놓친다. 예를 들어 정지점을 `[0, 1, 2]`로 두고 `t=0.5`에서만 `opacity` 설정을 빠뜨리면, `0`에서 바로 탐색했을 때와 `0.49`를 거쳐 탐색했을 때 그림이 달라져도 검사는 통과한다. 중간 캡처도 한 이력에서만 찍는다. 정지점과 중간 시각 각각을 독립적으로 초기화한 SVG에 직접 탐색한 결과와 순방향·역방향으로 접근한 결과를 비교해야 한다. [engine.diff](/C:/Users/Public/Documents/ESTsoft/CreatorTemp/hsdeck-suwt2abc/engine.diff:427)

13. **should · `qa_render.py:39–47`**  
    `outerHTML` 비교는 그림이 같아도 속성 삽입 순서 때문에 실패한다. `t<1`에는 `opacity`만, `t>1`에는 `transform`만, `t=1`에는 둘 다 두는 렌더러를 쓰면 순방향과 역방향에서 `t=1`의 속성값은 같지만 직렬화 순서가 달라진다. 요소 순서는 유지하면서 속성을 이름과 값으로 정규화해 비교하면 이 오탐을 없앨 수 있다. [engine.diff](/C:/Users/Public/Documents/ESTsoft/CreatorTemp/hsdeck-suwt2abc/engine.diff:431)

제공된 두 애니메이션에는 질문한 시간 관련 문제가 없었다. 정지점과 중간 시각을 순서를 바꿔 렌더해도 속성값이 같았고, 비트 경계에서 값이 튀거나 마지막 정지점(`latent` 4.2초, `map` 4.3초) 이후에 더 움직이는 경우도 없었다. 엔진의 정상 진입, 재생 중 다음·이전 입력 처리, `?motion=0`의 비트 점프, 슬라이드를 떠날 때의 rAF 취소에서도 문제를 찾지 못했다. 검증은 제공된 코드와 메모리 재현으로 수행했다. [overview_latent.anim.js](/C:/Users/Public/Documents/ESTsoft/CreatorTemp/hsdeck-suwt2abc/overview_latent.anim.js:33), [overview_map.anim.js](/C:/Users/Public/Documents/ESTsoft/CreatorTemp/hsdeck-suwt2abc/overview_map.anim.js:31)