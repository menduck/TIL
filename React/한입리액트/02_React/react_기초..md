#  리액트를 사용하는 이유

1. 유지 보수의 용이성 
  - 공통적으로 사용해야 되는 부분을 컴포넌트화 해서 재사용성을 높임
  - 산탄총 수술인 상황을 만들지 않음 
    - 산탄총 수술: 한 개의 문제가 수 많은 파일들을 동시에 수정해야 하는 상황

2. 선언형 프로그래밍
3. virtual DOM
  - 실제 DOM의 변경 사항을 빠르게 파악, 반영하기 위해서 내부적으로 가상 DOM을 만들어서 관리.
  - 변경 전과 변경 후를 비교 한 뒤 최소 내용만 반영, 성능 향상을 이끔


# JSX

## 닫힌 태그
## 최상위 태그
- 반드시 최상위 태그로 묶어 줘야 함.

- 만약 최상위 태그로 묶고 싶지 않다면, 아래의 방식으로 가능
```js
// 방법 1
import React from 'react';

function App() {
  return (
    <React.Fragment>
      // ... 최상위 태그를 두고 싶지 않은 코드들
    </React.Fragment>
  )
}

// 방법 2
function App() {
  return (
    <>
      // ... 최상위 태그를 두고 싶지 않은 코드들
    </>
  )
}
```

## CSS

1. 외부 CSS 파일 사용
2. 내부 CSS 사용 (인라인)

```js
function App() {
  const style = {
    App: {
      // 객체 형태로 넣어줌.
      // 카멜 케이스로 표기
      backgroundColor: 'yellow',
    },
  };

  return (
    <div className="App" style={style.App}>
      <MyHeader />
      <MyFooter />
    </div>
  );
}
```

## 자바스크립트 표현식
- JSX 내부에서 {} 로 감싸서 표현
- 조건부랜더링 가능

```js
function App() {
  const name = '미미';
  const number = 1;

  return (
    <div className="App">
      <MyHeader />
      <h1>안녕 {name} </h1>
      <b>
        {number}는 : {number % 2 === 0 ? '짝수' : '홀수'}
      </b>
      <MyFooter />
    </div>
  );
}
```

# State
- 계속해서 변화하는 특정 상태
- 상태에 따라 각각 다른 동작을 함

## 예제 - 버튼이 누르면 숫자가 오르고 내려가는 카운터 만들기

```js
import React, { useState } from 'react';

const Counter = () => {
  const [count, setCount] = useState(0);

  const onIncrease = () => {
    setCount(count + 1)
  }

  const onDecrease = () => {
    setCount(count - 1)
  }
  return (
    <div>
      {/* 
      * 카운터 숫자는 동적으로 변화해야 하는 값 
      - 0에서 출발 / 1씩 증감소하는 카운트 상태
      */}
      <h2>{count}</h2>
      <button onClick={onDecrease}>-</button>
      <button onClick={onIncrease}>+</button>
    </div>
  );
};
export default Counter;
```

- 컴포넌트는 자신이 가진 State가 변화하면 리렌더링을 한다.

  - 만약 현재 count = 0인 상태에서 +를 버튼을 누른다면?

     1. onIncrease 함수가 실행되고, setCount(0 + 1)이 됨.
     2. count가 1로 바뀜
     3. return 안에 {count}가 1로 랜더링됨.(***리렌더링***)

- 하나의 컴포넌트에 여러 개의 State를 가져도 된다.

# Props