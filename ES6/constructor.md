# constructor

## constructor의 용도
- object를 마구 복사하고 싶을 때 사용한다.
- 비슷한 object 여러 개 만들 때 사용한다.

```js
function Student() {
  // constructor
  this.name = "Lee"; 
  this.age = 30;
}
const 학생1 = new Student() // new는 Student()로부터 오브젝트로 뽑아 준다.
console.log(학생1) // Student { name: 'Lee', age: 30 }
```
>>> this.name = "Lee"
:  Student에서 새로 생성되는 오브젝트에는 name이란 속성에 "Lee"를 넣어준다는 뜻,
인스턴스 생성


>>> const 학생1 = new Student()
:new는 Student()로부터 오브젝트로 뽑아 준다.

## construtor사용하여 오브젝트 만드는 법
```js
const 학생A ={
  name : 'Kim',
  age : 15,
  sayHi : function(){
    console.log(`안녕하세요 ${this.name}입니다.`) // 'this.name'은 name의 value 값
  }
}

학생A.sayHi() //안녕하세요 Kim입니다.
```
- 위 코드는 학생A만 해당하는 sayHi()를 하드코딩 하였다.  

<br>
- 모든 학생 object에 sayHi()를 추가하는 방법    

```js
function Student() {
  // constructor
  this.name = "Lee"; 
  this.age = 30;
  this.sayHi = function(){
    console.log(`안녕하세요 ${this.name}입니다.`) 
      }

}
const 학생B = new Student()
const 학생C = new Student()
학생B.sayHi(); //안녕하세요 Kim입니다.
학생C.sayHi(); //안녕하세요 Kim입니다.
```
- 위 코드는 학생의 이름과 나이가 똑같이 출력되고 있다.    


<br>
- 학생들마다 정보를 반영하려면?    

```js
function Student(name,age) {
  this.name = name; 
  this.age = age;
  this.sayHi = function(){
    console.log(`안녕하세요 ${this.name}입니다.`);
      }
}

const 학생B = new Student('mini',20) 
const 학생C = new Student('ari',13)

학생B.sayHi(); // 안녕하세요 mini입니다.
학생C.sayHi(); // 안녕하세요 ari입니다.
```
