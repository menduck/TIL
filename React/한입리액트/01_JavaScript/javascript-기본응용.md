# 객체
## 특정 객체에 프로퍼티가 있는지 확인하는 방법

- in 을 활용해서 확인한다.

```js
const person = {
  name: '김민선',
  age: 100,
  say: function() {
    console.log(`안녕 나는 ${this.name}이야`);
  },
};

conosole.log(`name : ${"name" in person}`); // 'name : true'
conosole.log(`name : ${"gender" in person}`); // 'gender : false'
```

# 배열 내장 함수
## findIndex
- 콜백함수를 실행하여 true를 반환하는 배열의 첫 번째 요소 인덱스를 반환한다.
- true인 값이 없으면 -1를 반환함.

```js
const arr = [
  { color: 'red' },
  { color: 'yellow' },
  { color: 'green' },
]

console.log(
  arr.findIndex((ele) => {
    return ele.color === 'red'
  })
) // 0

console.log(
  arr.findIndex((ele) => {
    return ele.color === 'purple'
  })
) // 0
```

## find
- 콜백함수를 실행하여 true를 반환하는 배열의 첫 번째 요소를 반환한다.
- true인 값이 없으면 -1를 반환함.

```js
const arr = [
  { color: 'red' },
  { color: 'yellow' },
  { color: 'green' },
]

console.log(
  arr.find((ele) => {
    return ele.color === 'red'
  })
) // { color: 'red' }

console.log(
  arr.find((ele) => {
    return ele.color === 'purple'
  })
) // undefined
```

# Truthy & Falsy

- Truthy
  - 참 같은 값

```js
if ({})
if ([])

// 더 많지만 헷갈리는 것만 정리함.
```

# 비구조할당

- 비구조할당에 기본값을 설정 할 수 있음.

```js
let [one, two, three, four] = [1,2,3]
console.log(one, two, three, four) // 1 2 3 undefined

let [one, two, three, four = 4] = [1,2,3]
console.log(one, two, three, four) // 1 2 3 4
```
- 객체일땐, key값을 기준으로 할당함. (순서 아님)

```js
let object = { one: 1, two: 2, three: 3}
let {one, three, two} = object
console.log(one, two, three) // 1 2 3

// 만약 다른 변수명에 할당 받고 싶으면?
let object = { one: 1, two: 2, three: 3}

// one의 value값을 myOne변수에 할당함.
let {one: myOne, three, two} = object
console.log(myOne, two, three) // 1 2 3
```

## swap 활용
- 임시변수를 두고 값을 교환하는 방법

```js
// 서로 값 교환하는 법
let a = 10;
let b = 20;

// 임시 변수 
let tmp = 0;

tmp = a;
a = b;
b = tmp;
console.log(a,b) // 20, 10
```

- 비구조할당으로 값을 교환하는 방법

```js
let a = 10;
let b = 20;

[a, b] = [b, a]
console.log(a,b) // 20, 10
```

# 동기 & 비동기

## 동기 방식의 처리
- 자바스크립트는 
  - 코드의 작성 순서대로 작업을 처리함.
  - 싱글 쓰레드로 동작함.
    - 만약 멀티 쓰레드라면, 여러 개의 쓰레드를 쓰면서 작업 분할이 가능함.

- 현재 작업이 끝날 때 까지 다음 작업을 수행하지 않음.

- 블로킹 방식이라고도 불림

- 단점 :  하나의 작업이 오래 걸리면, 전반적인 흐름이 느려짐

### JS Engine

```js
function one() {
  // 5. 1을 리턴하면서 OUT
  return 1;
}

function two() {
  // 4. one 함수 호출
  // 6. 2를 리턴하면서 OUT
  return one() +1;
}

function three() {
  // 3. two 함수 호출
  // 7. 3을 리턴하면서 OUT
  return two() +1;
}

// 2. three 함수 호출
// 8. 3을 출력하고 OUT
console.log(three());
```

- Call Stack
  - 4. one() ***5.OUT***
  - 3. two() ***6.OUT***
  - 2. three() ***7.OUT***
  - 1. Main Context ***8.OUT***

- Main Context
  - Call Stack에 들어온 순간 프로그램 시작, Call Stack에 나가는 순간 프로그램 종료


## 비동기 방식의 처리
- 싱글 쓰레드 방식을 이용하면서, 여러 개의 작업을 동시에 실행 시킴
- 먼저 작성된 코드의 결과를 기다리지 않고, 다음 코드를 실행함.
- 논 블로킹 방식이라고도 불림

### JS Engin

```js
function asyncAdd(a, b, cb) {
  // 3. 비동기함수 호출 -> Call Stack에서 Web APIs에 넘김
  setTimeout(() => {
    const res = a + b;
    cb(res);
  }, 3000);
}

// 2. asyncAdd 호출
// 3. OUT
asyncAdd(1, 3, (res) => {
  console.log("결과: ", res);
})
```

- Call Stack
  - 2. asyncAdd() ***3.Web APIs 로 넘김***
  - 1. Main Context ***4.OUT***

- Web APIs
  - setTimeout()과 cb() => setTimeout()이 끝나면 콜백함수인 cb()는 Callback Queue로 넘어감

- Callback Queue
  - cb()는 Event Loop을 통해 Call Stack으로 넘어감

# promise

- 콜백 지옥의 예
```js
function taskA(a, b, cb) {
  setTimeout(() => {
    const res = a + b;
    cb(res);
  }, 3000);
}

function taskB(a, cb) {
  setTimeout(() => {
    const res = a * 2;
    cb(res);
  }, 1000);
}

function taskC(a, cb) {
  setTimeout(() => {
    const res = a * -1;
    cb(res);
  }, 2000);
}

taskA(3, 4, (a_res) => {
  console.log('taskA : ', a_res); // 7
  taskB(a_res, (b_res) => {
    console.log('taskB : ', b_res); // 14
    taskC(b_res, (c_res) => {
      console.log('taskC : ', c_res); // -1
    });
  });
});
```

- promist 객체를 반환하는 함수를 만든 것은
  - 비동기 처리된 결과값을 then과 catch로 이용할 수 있게 만들기 위해서

```js
function taskA(a, b) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const res = a + b;
      resolve(res);
    }, 3000);
  });
}

function taskB(a) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const res = a * 2;
      resolve(res);
    }, 1000);
  });
}

function taskC(a, cb) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const res = a * -1;
      resolve(res);
    }, 2000);
  });
}

// 콜백함수를 활용하는 것은 다시 콜백지옥을 만드는 것과 같음
taskA(5, 1).then((a_res) => {
  console.log('A result: ', a_res);
  taskB(a_res).then((b_res) => {
    console.log('B result: ', b_res);
    taskC(b_res).then((c_res) => {
      console.log('C result: ', c_res);
    });
  });
});


// then chaining
taskA(5, 1)
  .then((a_res) => {
    console.log('A result: ', a_res);
    return taskB(a_res);
    // 여기까지 taskB를 반환받은 promise 객체
  })
  .then((b_res) => {
    console.log('B result: ', b_res);
    return taskC(b_res);
    // 여기까지 taskC를 받환받은 promise객체
  })
  .then((c_res) => {
    console.log('C result: ', c_res);
  });
```

- 비동기 호출하는 코드와 결과를 처리하는 코드를 분리할 수 있음. 

```js
const bPromiseResult = taskA(5, 1)
  .then((a_res) => {
    console.log('A result: ', a_res);
    return taskB(a_res);
    // 여기까지 taskB를 반환받은 promise 객체
  })

console.log('중간에 낀 코드들')
// some code
  
bPromiseResult.then((b_res) => {
    console.log('B result: ', b_res);
    return taskC(b_res);
    // 여기까지 taskC를 받환받은 promise객체
  })
  .then((c_res) => {
    console.log('C result: ', c_res);
  });
```

# async & await 

- async
  - function 앞에 위치.
  - 함수의 반환값으로 항상 promise를 반환함
  - 프라미스가 아닌 값을 반환하더라도 이행 상태의 프라미스(resolved promise)로 값을 감싸 이행된 프라미스가 반환함.

```js
function hello() {
  return 'hello';
}

// promise 객체로 반환함.
// 리턴값은 promise 객체의 resolve의 값이 됨
async function helloAsync() {
  return 'hello Async';
}

helloAsync().then((res) => {
  console.log(res) // hello Async
})
```

- await
  - async 함수 안에서만 동작함.
  - promise가 처리될 때까지 함수 실행을 기다림 => 마치 동기적인 것처럼
  - 기다리는 동안에 엔진이 다른 일을 처리할 수 있기 때문에 CPU 리소스가 낭비되지 않음.


```js
function delay(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

// async function helloAsync() {
//   return delay(3000).then(() => {
//     return 'hello Async';
//   });
// }

// await 활용
async function helloAsync() {
  // 마치 동기적으로 수행되는 것처럼 작동됨.
  await delay(3000);
  return 'hello Async';
}

helloAsync().then((res) => {
  console.log(res); // hello Async
});
```


[출처: [코어자바스크립트](https://ko.javascript.info/async-await)]