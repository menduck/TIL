# this

## 1. this의 뜻 : this를 콘솔에 띄우면?
```js
  console.log(this); // {window}

  function 함수(){
    console.log(this); // {window}

  }
  
  함수()
```
- {window} 객체를 보여줌
- {window} : 기본 함수를 가지고 있는 객체.

<br>
```js
  'use strict'; //자바스크립트 엄격모드

  console.log(this) // {window}

  function 함수(){
    console.log(this); 
  }
  
  함수() // undefiend
  ```
## 2. this의 뜻 : object안에 있을 경우

```js

const 오브젝트 ={
  data : 'kim',
  함수 : function(){
    console.log('안녕')
  },
  함수2 : function(){
    console.log(this) // this는 나를 포함하고 있는 오브젝트를 뜻함
  }
}

console.log(오브젝트.data) // kim
오브젝트.함수() // 안녕
오브젝트.함수2() // { data: 'kim', '함수': [Function: 함수], '함수2': [Function: 함수2] }
```
- 오브젝트 안, 함수 안에 this를 쓸 경우 this는 <b>나를 포함하고 있는 오브젝트</b>를 뜻한다.

```js
const 오브젝트 ={
  data : {
    함수 : function(){
      console.log(this);
    }
  }
};
```
- 여기서 this는 오브젝트 객체를 뜻하는 this가 아니라 <b> 오브젝트.data 객체</b>를 뜻한다.

##### Arrow function일 경우
```js
console.log(this) // {window}
const 오브젝트 ={
  data : {
    함수 : ()=>{
      console.log(this) // {window}
    }
  }
}
```
- this값을 함수 밖에 있던 것을 그대로 받는다.
- 내부의 this값을 변화시키지 않는다.

## 3. this의 뜻 : keyword
```js
function 기계(){
  //constructor -> 오브젝트 생성기계
  this.이름 = 'kim' // this의 뜻 : 기계로부터 새로 생성되는 오브젝트(instance)
}

const 오브젝트 = new 기계()
console.log(오브젝트) // 기계 { '이름': 'kim' }
```
>>> this.이름 =  "kim" : 새로 생성되는 오브젝트에 이름이라는 키값에 kim이라는 value값 할당

- 기계라는 함수안에 쓰면 <b>새로 생성되는 오브젝트를</b> 뜻한다.

## 4. this의 뜻 : 이벤트 리스너 안일 경우
```js
// html
<div></div>
<button id="버튼">버튼</button>
<script>
document.getElementById('버튼').addEventListener('click',
function(e){
  this; // <button id="버튼">버튼</button>
  e.currentTarget; // <button id="버튼">버튼</button>
</script>
})
```
- this는 이벤트리스너 안에서는 지금 이벤트 동작하는 태그를 알려준다.

## 특수한 경우

### 1. 콜백함수에서 this?
```js
const arr = [1,2,3];
arr.forEach(function(a){
  console.log(this)
})
```
>>> arr.forEach(function(a){}) 에서 function(a){} 의 의미는?
: 콜백함수 / 함수 안에 들어가는 함수를 콜백함수라 뜻함.

- this는 {window}를 뜻한다.
- 일반 함수에서 this는 window를 뜻한다. (this의 1번 뜻)

### 2. 오브젝트 내에 콜백함수의 this?
```js
const 오브젝트 = {
  과자들 : ['뻥이요',"고구마칩","빼빼로"],
  함수 : function(){
    console.log(this) //{ '과자들': [ '뻥이요', '고구마칩', '빼빼로' ], '함수': [Function: 함수] }
    오브젝트.과자들.forEach(function(){
      console.log(this) //{window}
    })
  }
}
```
- 첫번째 this는 함수의 주인인 오브젝트를 뜻한다.
- 두번째 this는 콜백함수인 기본함수의 this임으로 window를 뜻한다.

### 3. 오브젝트 내 arrow function 안에서의 this?
```js
const 오브젝트 = {
  과자들 : ['뻥이요',"고구마칩","빼빼로"],
  함수 : function(){
    console.log(this) // { '과자들': [ '뻥이요', '고구마칩', '빼빼로' ], '함수': [Function: 함수] }
    오브젝트.과자들.forEach(function(){
      console.log(this) // { '과자들': [ '뻥이요', '고구마칩', '빼빼로' ], '함수': [Function: 함수] } X 3
  }
}
```