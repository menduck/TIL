상속기능을 구현하는 ES5/ES6

# 상속 기능 ES5

```js
const 부모 ={name : "kim", age : 50};
const 자식 = Object.create(부모);
console.log(자식) // {}
console.log(자식.name) // kim
```
>>> const 자식 = Object.create(부모);

- 부모의 프로토타입을 정의를 해줌.

>>> 자식.name

- 자식의 프로토타입은 부모로 두고 있다.
- 1. 자식이 name을 직접 가지고 있나? -> 아니
- 2. 자식의 부모 prototype에는 name을 가지고 있나? - 네, 출력

### 자식 값 수정

```js
const 부모 ={name : "kim", age : 50};
const 자식 = Object.create(부모); 
console.log(자식.age);//50
자식.age = 20
console.log(자식.age);//20
```
>>> console.log(자식.age);//50
- 1. 자식이 age를 직접 가지고 있는가? - 아니
- 2. 자식의 부모 prototype에는 age를 가지고 있는가? - 네, 50 출력
>>> 자식.age = 20
console.log(자식.age);//20
- 1. 자식이 age를 직접 가지고 있는가? - 네, 20 출력

### 손자 상속
```js
const 부모 ={name : "kim", age : 50};
const 자식 = Object.create(부모); 
자식.age = 20;

const 손자 = Object.create(자식);
console.log(손자.name); //kim
console.log(손자.age); //20
```
>>> 손자.name

- 손자가 name을 직접 가지고 있는가? -> 아니
- 손자의 부모인 자식은 name을 가지고 있는가? -아니
- 손자의 부모인 자식의 부모는 name을 가지고 있는가? - 네, kim 출력

>>> 손자.age

- 손자가 age을 직접 가지고 있는가? -> 아니
- 손자의 부모인 자식은 age을 가지고 있는가? -네, 20 출력

# 상속 기능 ES6
## construtor 만드는 법
```js
class 부모 {
  constructor(){
    this.name = "kim"
  }
}
```
## 부모 자식

```js
class 부모 {
  constructor(){
    this.name = "kim"
  }
}
const 자식 = new 부모();
```

## 함수 추가하기

### constructor에 추가하는 방법.
- 자식이 직접 함수를 가지고 싶으면 이 방법 추천!

```js
class 부모 {
  constructor(){
    this.name = "kim"
    this.sayHi = function(){
      console.log(`Hello, ${this.name}`)}
  }
}
const 자식 = new 부모();
자식.sayHi()// Hello, kim
```
### 메소드를 만들기
- 자식 오브젝트에 추가 되는게 아니라 부모.prototype에 추가됨.
- 모든 자식들이 쓸 수 있는 내장함수같은 함수를 가질 수 있다.
- 관리도 편하다

```js
class 부모 {
  constructor(){
    this.name = "kim"
  }
  sayHi(){
    console.log(`Hello, ${this.name}`)}
}
const 자식 = new 부모();
자식.sayHi()// Hello, kim
```

### 함수 여러개 추가하기
- 방법1
```js
class 부모 {
  constructor(){
    this.name = "kim"
  }
  sayHi(){
    console.log(`Hello, ${this.name}`)}
  
  sayBye(){
    console.log(`Bye, ${this.name}`)
  }
}

const 자식 = new 부모();
자식.sayBye(); // Bye, kim

```
방법2
```js
class 부모 {
  constructor(){
    this.name = "kim"
  }
  sayHi(){
    console.log(`Hello, ${this.name}`)}
}

부모.prototype.hahaha = function(){
  console.log("HaHaHa");
}
const 자식 = new 부모();
자식.hahaha(); // HaHaHa
```
### 상속 확인

<b>자식.__ _proto_ __ </b>는 <b>부모.prototype</b>이랑 같다.

- 내장함수 Object.getPrototypeOf()이용해서 확인 가능하다.

### 파라미터 추가
```js
class 과자들 {
  constructor(name){
    this.name = name
  }
}

const 자식 = new 과자들('새우깡')

console.log(자식) // 과자들 { name: '새우깡' }
``` 
### class의 extends (class 상속)
- super()
```js
class 할아버지{
  constructor(name){
    this.성 = "Lee"
    this.이름 = name;
  }
}

//할아버지의 속성들 그대로 물러받는다.
class 아버지 extends 할아버지{
  constructor(name){
    super(name); // super()없이 extends에 this를 사용하지 못한다. 앞에 할아버지의 속성을 붙이는 역할을 함.
    this.나이 = 50;
  }
}

const 슈퍼할아버지 = new 할아버지('만수')
console.log(슈퍼할아버지) // 할아버지 { '성': 'Lee', '이름': '만수' }

const 닭집아버지 = new 아버지('만수'); 
console.log(닭집아버지) //아버지 { '성': 'Lee', '이름': '만수', '나이': 50 }
```
- super()의 또다른 용도
```js
class 할아버지{
  constructor(name){
    this.성 = "Lee"
    this.이름 = name;
  }
  sayHi(){
    console.log('안녕 저는 할아버지에요');
  }
}

class 아버지 extends 할아버지{
  constructor(name){
    super(name); 
    this.나이 = 50;
  }
  sayHi(){
    console.log('안녕 저는 아버지에요');
    super.sayHi();
  }
}

const 닭집아버지 = new 아버지('만수'); 
닭집아버지.sayHi() // 안녕 저는 아버지에요 \n 안녕 저는 할아버지에요
```
>>>   sayHi(){
    console.log('안녕 저는 아버지에요');
    super.sayHi();
  }

- 유전자가 더 가까운 아버지 class에 가서 sayHi 함수 실행한다.
- 그 다음 super 는 부모의 prototype.sayHi()를 의미하기 때문에 부모의 sayHi함수를 실행한다.

## 객체지향 문법의 목적
1. object 여러개 만들어 쓰려고