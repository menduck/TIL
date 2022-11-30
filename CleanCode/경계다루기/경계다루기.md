>>> 명시적으로 프로그래밍하려고 의식적으로 노력하기

# min - max
1. 최소값와 최대값을 다룬다.
2. 최소값와 최대값 포함 여부를 결정한다. (이상-이하/초과-미만)
3. 네이밍에 최소값과 최대값 포함 여부를 표현한다. ex) MAX_NUMBER_LIMIT, MAX_IN_NUMBER

# begin - end
- 날짜를 사용할때 쓰임
- 체크인(begin)~체크아웃(end)

```js
function reservationDate(beginDate, endDate) {
  //
}
```
# first - last
- 규칙성이 없는 데이터를 사용할 때 씀
- 포함된 양의 끝단
- ~ 부터 ~ 까지

```js
const students = ["시경","검석","준식"];

function getStudents(first,last){
  //
}
//
```

# prefix(접두사) - suffix(접미사)
- ex) private field(#)
- 코드를 읽는 가장 일관성 있는 방식
- 회사의 컨벤션에 맞게 작성함.

# 매개변수의 순서가 경계다!

```js
genRandomNumber(1,50) // 1~50까지 중 난수 생성이구나!
```
- 함수를 만들때 매개변수를 2개가 넘지 않도록 만든다.
- 만약 규칙적이지 않은 인자가 많을때는?
  - arguments, rest parameter를 이용한다.
- 매개변수를 객체에 담아서 넘긴다.
- 만약 이미 만들어놓은 함수가 있다.
  - 랩핑하는 함수

  ```js
  // 객체로 만들기
  function someFunc({someArg1,someArg2,someArg3,someArg4}){
  }
  
  // 랩핑하기
  function someFunc(someArg1,someArg2,someArg3,someArg4){
  }
  // 만약 someArg3 과 someArg4만 자주 쓴다면
  fucntion getFunc(someArg1, someArg2) {
    someFunc(someArg1,someArg2);
  }
  // 만약 someArg2 과 someArg4만 자주 쓴다면
  fucntion getFunc(someArg1,someArg3) {
    someFunc(someArg1,undefiend,someArg3); // 객체로 다루지 않기 때문에 순서를 지켜야함.
  }
  ```