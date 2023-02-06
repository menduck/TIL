# prototype = 상속을 구현할 수 있는 문법

## 부모와 자식
- 부모의 속성을 자식이 물러받는다.

```js
//부모
function Student(name,age) {
  this.name = name; 
  this.age = age;
  this.sayHi = function(){
    console.log(`안녕하세요 ${this.name}입니다.`);
      }
}
//자식
const 학생B = new Student('mini',20) 
```
## prototype 활용
- function을 만들면 그 안에 prototype이라는 공간이 자동으로 생긴다.
- prototype은 <b>유전자</b> 라고 생각하면, prototype에 값을 추가하면 모든 자식들이 유전자를 물러받기가 가능한다.
```js
function Student(name,age) {
  this.name = name; 
  this.age = age;
  this.sayHi = function(){
    console.log(`안녕하세요 ${this.name}입니다.`);
      };
}
Student.prototype.gender = '남' 

const 학생B = new Student('mini',20) ;
console.log(학생B) // Student { name: 'mini', age: 20, sayHi: [Function (anonymous)] }
console.log(학생B.gender) //남

```
>>> Student.prototype.gender = '남' 
console.log(학생B.gender) //남

- 부모 유전자(Student)에 gender를 등록했기때문에 자식(학생B)에 genderd인 '남'를 불러올 수 있다.

## prototype의 원리

```js
function Student(name,age) {
  this.name = name; 
  this.age = age;
  this.sayHi = function(){
    console.log(`안녕하세요 ${this.name}입니다.`);
      };
}
Student.prototype.gender = '남' 
const 학생B = new Student('mini',20) ;
console.log(학생B.name) // mini
```
- 자바스크립트의 동작 순서
>>> 학생B.name
1. 학생B가 name이 있는지 검사한다.
-> 있으므로 출력한다.

>>> 학생B.gender
1. 학생B가 gender가 있는지 검사한다.
-> 없다
2. 학생B의 부모 유전자(Student.prototype)가 gender를 가지고 있는지 검사한다.
-> 있으므로 출력

### 내장함수의 동작 원리

- 내장함수는 어떻게 모든 obj에 쓸 수 있는가?

>>>학생B.toString()
1. 학생B가 toString가 있는지 검사한다.
-> 없다
2. 학생B의 부모 유전자(Student.prototype)가 toString를 가지고 있는지 검사한다.
-> 없다
3. 부모(Student)의 부모 유전자(Object.prototype)가 toString를 가지고 있는지 검사한다.
-> 있다.

>>> const arr =[1,2,3];
const arr = new Array(1,2,3); // 실제 컴퓨터가 arr를 만드는 방식
- 상속 : 부모(Array(1,2,3))의 프로퍼티들을 arr(자식)이 사용할 수 있다.

1. arr에 sort()가 있는가?
-> 없다.
2. arr 부모의 유전자(Array.propotype)에 sort()가 있는가?
-> 있다.

<hr>

- 모든 obj 자료형의 조상은 Object() 이며,   
- 모든 arr 자료형의 조상도 Object()이다. (중간에 Array()라는 부모도 있음)
- 모든 함수 자료형의 조상도 Object()이다.
- 곧 자바스크립트는 모든게 Object라 할 수 있다.

## prototype의 특징

### 1. prototype은 함수에만 생성.

### 2. 내 부모 유전자(부모의 prototype)를 알고 싶으면?

```js
console.log(학생B.__proto__) // { gender: '남' }
```

### 3. __proto__를 이용해 부모 강제 등록하기.

```js
const 부모 = {name : "Kim"};
const 자식 ={}
자식.__proto__ = 부모;
console.log(자식.name) //Kim
```
>>> 자식.__proto__ = 부모;

- 강제로 등록한다.
- 하지만 잘 쓰지 않는다.

### 4. 콘솔창에서 알려주는 prototype chain
- 콘솔창에 학생B를 출력하면 __proto__ : Object 을 조회할 수 있다.
- 기계.prototype의 __proto__ ( 기계.prototype의 부모 유전자)도 조회 가능


#### 주의

```js
function parent(){
  this.name = "kim";
}
const a = new parent();

a.__proto__.name = "park"
console.log(a.name) // kim
```

>>> a.__ _proto___.name = "park"

- 부모 prototype에 {name : "park"}를 추가하라는 뜻

>>> a.name

- 내가 가지고 있는 {name:"kim"}을 출력한다.