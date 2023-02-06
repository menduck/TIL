# Array 판별
>>> Array.isArray()

```js
const arr = [1,2,3];
const str = '[1,2,3]';

console.log(Array.isArray(arr)) // true
console.log(Array.isArray(str)) // false
```
# Array.length
- 객체처럼 동작하기 때문에 생기는 오류
```js
const arr = [1,2,3];
console.log(arr.length);

arr.length = 10;
console.log(arr.length) //10
console.log(arr) //[ 1, 2, 3, , , , , , ,  ]
```
## length를 이용하여 빈 배열 만들기
>>> arr.length = 0
```js
const arr = [1,2,3,4,5]
arr.length = 0
console.log(arr) //[]
```
- 의식적으로 주의하고 활용하자.

# 배열 요소에 접근하기.
- arr[index]가 무엇을 의미하는지 알 수 없음.
- 예측하기 쉽게 바꿔야함.

- 접근법 1
```js
// bad
const inputs = [1,2,3,4,5];

const result1 = inputs[0]+2
const result2 = inputs[1]+2

//good
const inputs = [1,2,3,4,5];

const [firstInput,secondInput] = inputs
const result1 = firstInput+2
const result2 = secondInput+2

// 또는 함수일 경우 매개변수를 받을때부터 분해를 한다.
```
- 접근법 2
명시적으로 표현가능
```js
// bad
function clickGroupButton() {
  const confirmButton = document.getElementsByTagName('butto')[0];
  const cancelButton = document.getElementsByTagName('butto')[1];
  const resetButton = document.getElementsByTagName('butto')[2];
}

// good
function clickGroupButton() {
  const [confirmButton,  cancelButton, resetButton]  = document.getElementsByTagName('butto');
}
```
- 접근법 3 - 배열이 하나만 있을때
```js
// bad
function formatDate(targetDate) {
  const date = targetDate.toISOString().split('T')[0]; // 하나의 배열이라도 [0]을 지양하자.

  const [year, month, day] = date.split('-');
  return ` ${year}년 ${month}월 ${day}일`
}

// good
function formatDate(targetDate) {
  const [date] = targetDate.toISOString().split('T');

  const [year, month, day] = date.split('-');
  return ` ${year}년 ${month}월 ${day}일`
}

// best 유틸함수 사용
function head(arr) {
  return arr[0] ?? 'error'
}

function formatDate(targetDate) {
  const date = head(targetDate.toISOString().split('T')); // 하나의 배열이라도 [0]을 지양하자.

  const [year, month, day] = date.split('-');
  return ` ${year}년 ${month}월 ${day}일`
}
```

# 유사 배열 객체
