# nullish 병합 연산자
- null과 undefined에만 사용한다.
>> a ?? b
- a가 null도 아니고 undefined도 아니면 a이다.
- 그 외는 b

## 예제1
```js
function helloWorld(message) {
  if(!message) {
    return 'Hello! World';
  }

  return 'Hello!' + (message || 'World')
}
```
- 만약 0을 입력했을때 Hello! 0World를 기대했지만 0은 false임으로 Hello! World가 반환된다.

- 해결 코드1
```js
function helloWorld(message) {
  return 'Hello!' + (message ?? 'World')
}
```
- 해결 코드 1의 문제점 : early return을 할때 헷갈랴 실수할 가능성이 크다.
- 해결 방안 : default parameter쓰면 됨.
```js
function helloWorld(message = 'World') {
  return 'Hello!' + message 
}
```

## 제약 사항
- OR 연산자 AND연산자는 ??연산자를 혼합해서 쓰지 못한다.
- 우선 순위를 명시적으로 나타내줘야 쓸 수 있다.