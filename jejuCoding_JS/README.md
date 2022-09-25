# jejuCodeing_JS
제주코딩베이스캠프 JS 요약강좌 정리
:smiley:

# 1. 자바스크립트
* HTML은 콘텐츠와 골격, CSS는 웹페이지의 레이아웃, JavaScript는 웹페이지의 동작
    - 버전업이 되어도 이전 기능이 삭제되거나 새로운 기능을 막 추가할 수 없음. 
    **why?** 이미 배포된 웹페이지가 오류가 나면 안되기 때문임. 

## 1-1. 자바스크립트 삽입위치
```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title> 
</head>
<body>
    <h1>hello world</h1>
    <p id = "one">hello world</p>
    <p>hello world</p>
    <p>hello world</p>
    <p>hello world</p>
    <p>hello world</p>

    <script>
        document.getElementById("one").innerHTML ="hi world"
    </script>

</body>
</html>
```
- 일반적으로 body의 맨 끝.
- head, body의 문서 처음, 중간, 끝(미리 로드가 되어야 하는 경우)
- document가 완성된 다음 getElementById를 해줘야함.(document가 완성되지 않고 getElemnetById를 셀렉하면 도출이 안됨.)  

## 1-2 내부 스크립트와 외부 스크립트
    1. 내부 스크립트
 ```javascript
    <script>
    console.log('hello')
    </script>
```
    * 유지보수하기 안 좋음. 외부 스크립트를 사용해야 함!

    2. 외부 스크립트
```javascript
    <script src="test.js"></script>
```

## 1-3 자바스크립트 출력 4가지 방법
1. 문서 내에 요소 선택하여 출력(innerHTML, innerText 등)
2. 문서 내에 직접 출력하는 방법(document.write("hello") 등)
3. 사용자 인터렉션(alert, confirm 등)
4. 콘솔에 찍는 방법(console.log, console.table, console.error 등)

## 1-4 코드 구조
1. 문은 세미콜론으로 구분(회사컨벤션에 따라 다름.)
    * 단, 세미콜론을 안 붙였을때 문제가 생기는 구간을 인지하고 있어야 함 
#

2. 문은 값, 연산자, 키워드, 명령어, 표현식(값으로 평가, 함수나 key, index를 통한 값의 호출도 표현식) 등으로 구성

3. 공백 병합 (x=10 이나 x = 10 이나 같음)

    ```javascript
    let x = 10,
        y = 20,
        z = 30 //shift + enter
    console
        .log(
            x,
            y,
            z,
        )
    ```    
4. 주석
- // 한 줄 주석
- /* 이러쿵저러쿵 */ 여러 줄 주석

5. 엄격모드
 - ES5에서 새로운 문법(기존 문법을 변경하는 문법도 포함)이 많이 나와 기존 코드의 문제를 불러일으킬수 있음.
 - 코드의 최상단에 "use strict" 지시자를 넣어 엄격모드를 활성화 시켜 최신 문법을 사용.
 - class 문법의 경우 엄격 모드가 기본. use strict지시자를 쓰지 않아도 기본적으로 작동됨.
 - 함수별로 엄격모드를 다르게 작동시킬 수 있으나 권장하지 않음.

 # 2. 변수
## 변수 이름 규칙

        - 숫자로 시작할 수 없음 ( let 2x = 10 불가능)
        - 띄어쓰기 안됨.
        - 예약어를 사용할 수 없음 (단, 사용할 수 있는 예약어가 있긴 있음.)

 ```javascript
        let let = 10 // 예약어X
 ```
        - $,_를 제외한 특수문자를 사용하지 않음.
        - 대소문자 구분.
        - class는 첫 문자를 대문자로, 나머지 변수들은 대부분 소문자로 시작.

## var, let, const

:wink: 무조건 const, 문제가 될거 같은 경우는 let
#
> var를 안쓰는 이유 : 변수 선언 중복에서 에러를 주지 않음.
```javascript
var x = 10;
var y = 20;
console.log(x+y);

var x = 10;
var y = 20;
console.log(x+y);
```
- 다른 언어에서 변수를 중복 선언하면 에러가 뜸. 그러나 자바스크립트는 콘솔창에 에러를 주지 않음.

1.png

- 변수를 중복하여 넣었을땐 에러를 주지만, 한 번 선언하고 출력한 다음 다시 선언할 시 에러를 주지 않음.

```javascript
<script src="test.js"></script>
<script src="test2.js"></script> // 앞에 있는 스크립트가 뒤에 스크립트에도 영향을 미침.
```
- 외부 스크립트인 test.js 와 test2.js에서 x르 중복 사용하면, 에러 발생(var사용시 에러를 알려주지 않음.)

>var(ES5 이전, 지금 사용 권장 X) : 함수 레벨 스코프, 재선언시 애러 X

>let(ES5) : 블록 레벨 스코프, 재선언시 애러 O, 콘솔에서는 애러 X, 변경가능한 자료형
- 블록 레벨 스코프
```javascript
if (true) {
    const testName = 'hojun'
    let testAge = 10
}
```
if문(블록) 안에 선언된 변수는 문밖에서 꺼내 쓸 수 없음.

>const(ES5) : 블록 레벨 스코프, 재선언시 애러 O, 콘솔에서는 애러 X, 변경이 불가능한 자료형(상수), document 탐색 할때도 많이 사용.  
#
# 연산
- 산술 연산자(+, -, /, *, **, %)
- 할당 연산자(=, +=, -=, /=, *=, **=, %=)
    - 어떤 값을 누적할때 사용
```javascript
let x= 3;
console.log(x +=3) //6
console.log(x +=3) //9
console.log(x +=3) //12
// x = x + 3 을 줄여 x += 3
```
- 논리 연산자(&&, ||, !, !!, &, |)
    - 참 -> true -> 1
    - 거짓 -> false -> 0
    - &&는 곱 (AND 연산자)
        * true && false // 0 why? 1*0 = 0
        * 조건을 모두 만족 시켜야 true
    - ||는 합 (OR 연산자)
        * 조건 하나만 만족 시켜도 true
```javascript
            for (let x = 0; x < 100; x++) { // x = 0 이고, 100까지 1만큼 늘어감
                if(x % 3 == 0 && x % 5 == 0){ // 만약 x가 15의 최소공배수라면
                    console.log(x) // x값을 출력함.
                }
            }
```
    - !는 부정
```javascript
            !true // false
            !false // true

            // true와 false을 판별할때 !! 사용 (!!은 부정의 부정)
            !!true // true 
            !!false // false
            !!1 // true
            !!"hello" // true
            !!0 // false
            !!"" // false
```
    - 비트 연산자 (&, |) : 실무에서 잘 쓰이지 않음.
        9 & 5 // 1
        9의 이진수 = 1001, 5의 이진수 = 0101 임으로 서로 값을 비교하여 같은 값은 1 임.


```javascript
// 앞에 값이 널이냐를 확인하고 싶은 경우, 단락 회로 평가라고 부릅니다.
result1 = 10 || 100; //OR값을 볼 필요 없이 앞에 값이 있으니 항상 true, result1 = 10
result2 = 0 && 100; // 앞에 0이 나왔으니 && 뒤에 값을 볼 필요 없이 항상 false, result 2 =0
result3 = null || 100;
result4 = null && 100;

username = 'hojun'; // true
result5 = username || '유저 이름이 없습니다'; // OR값을 볼 필요 없이 앞이 true임으로 result5 = "hojun"

username = undefined; // false
result5 = username || '유저 이름이 없습니다'; // 앞에 값이 false임으로 뒤에 값을 봐야함. result5 = '유저 이름이 없습니다.'
```
- 비교 연산자(>, >=, <, <=, ==, !=, ===, !==)
    - ===,!== 는 타입까지 비교하여 알려줌.
```javascript
let x = 3; //number
let y = '3'; //string
console.log(x == y); //true
console.log(x === y); // false 
```
- 단항 산술 연산자(++x, x++, --x, x--)

- nullish 병합 연산자(??)
```javascript
// 단락 회로 평가와 비슷
let result1; //undefined
let result2 = result1 ?? 100; // undefined || 100 임으로 result2 = 100

let result3 = 10;
let result4 = result3 ?? 100; // result4 = 10

let result5 = null;
let result6 = result5 ?? 100; // result6 = 100
```
- typeof 연산자
```javascript
console.log(typeof 10) //number
console.log(typeof "10") // string
console.log(10+10) // 20
console.log("10"+"10") // "1010"
```
- 프로퍼티 접근 연산자
    1. 마침표 프로퍼티 접근 연산자
    2. 대괄호 프로퍼티 접근 연산자
```javascript
        let x = {"one" : 1, "two" : 2}
        // 마침표 프로퍼티 접근 연산자
        console.log(x.one); //1 
        // 대괄호 프로퍼티 접근 연산자
        console.log(x["one"]) //1
```
- 관계 연산자
    - 키만 가지고 판단 (key : vaule)
```javascript
10 in [10, 20, 30] // false
// [10,20,30]의 key는 0,1,2

1 in  // true
1 in 'hello' // error
h in 'hello' // 다른 언어에선 되지만 자바스크립트에선 안됨.
'name' in {'name':'hojun', 'age':10} //true

//array와 object의 차이
let x = [10, 20, 30] 
'length' in [10, 20, 30]; // true, array 안에 length가 있으므로 true
console.dir(x) // 변수의 형이 array / 0: 10 1: 20 2: 30 length: 3

let y = {'one' : 1, 'two' : 2}
'length' in y // false
console.dir(y) // 변수의 형 object / one: 1 two: 2
```
# 3.변수의 형

## 변수(타입, typeof로 확인 가능)
- 원시타입(primitive types) : number, string, boolean, null(아무것도 없는 것을 명시), undefined(변수는 있는데 아무런 값도 안 넣을때 생길때 생김), symbol(ES6 추가, 변경 불가능한 유일한 값)
```javascript
    let x = "hello"
    console.log(x[0]) //"h"
    x[0]=100 //100
    console.log(x) // "hello" , 고유의 값은 변경하지 못함.
```
- 참조타입(reference types) : object(object, array, map, set), function
```javascript
    let x = [10,20,30]
    console.log(x[0]) //10
    x[0]=100 //100
    console.log(x) // 100,20,30 , 값이 변경됨.
```
:bell: object, array typeof 주의
```javascript
let x = [10,20,30]
let y = {'one' : 1, 'two' : 2}
console.log(typeof x) //object
console.log(typeof y) //object
```
~~히스토리 찾아보기~~
### Number(숫자)
* 숫자 혼자 호출하지 못하고, 변수로 지정해서 변수명을 호출해야 함.
* 메서드
    * (number).toString, 변수명.toString 가능.
    * number.toFixed() : 소수점자리를 지정하여 반올림하여 값을 나타냄. 
```javascript
    let x = 10
    x.toString() // "10"
    x.toString() + x.toString() // "1010"
    ''+10+10 // "1010"
    10.toString() // 에러, 소수점 뒤에는 숫자가 나올 것이라고 예상되기 때문에
```


- Number()와 parseInt() 차이
    * 둘다 문자형을 숫자형으로 바꿔줌.
    * parseInt가 숫자와 문자가 섞여있을때 숫자만 더 안전하게 바꿔주기 때문에 권고함.
```javascript
        parseInt("1hello world") // 1
        Number("1hello world") //NaN
```
- NaN, infinity, -infinity 도 Number임.

### String(문자열)
- 형태 : 'abcde', "abcde", `abcde`, `abcde${변수명}`
- 호출 : 변수명, 변수명[0] (변수명[index], 호출은 할 수 있지만 개별 값 변경 불가/ "인데싱한다"라고 말함.)
- 메서드 :
    - str.length
    - str.slice()
        ```javascript
        'hello world'.slice(0,5) //"hello" 4까지하면 안되고 5까지 해야함.
        ```
    - str.
        ```javascript
        'hello world'.replace("hello","hi")// "hi world"
        'hello world hello'.replace(/hello/g,"hi")// "hi world hi" hello을 글로벌하게 다 잡아서 hi로 바꾸겠다.
### Boolean(논리값)
- 형태 : true, false
- 호출 : 변수명
    ```javascript
    !![]//true
    !!{}//true
    !!''//false, 아무값 없으면 false
    !!'hello'//true, 문자 하나라도 있으면 true
    !!0//false, 0만 false 나머지 true
    !!10//true
    !!-10////true
    ```
### undefine : undefined
    - 형태 : let a, console.log(a)
### null : object
    - 형태 : let a = null // 값이 없음을 명시해줌.
### Array : object
    
```javascript
    let x = ['하나', '둘', '셋'];
    console.log(x[0])//"하나"

    
    let y = [{'one':1, 'two':2}, {'one':10, 'two':20}];
    console.log(y[0])//{'one':1, 'two':2}
    console.log(y[0]['one'])//1
    
    let y =[[[1, 2], [10, 20], [100, 200]],
     [[3, 4], [30, 40], [300, 400]]]
     //400을 출력할때
    console.log(x[1][2][1])//400
```
    
- 호출 : 변수명, 변수명[0], 변수명[0][0] (변수명[index], 개별값 변경 가능)
- 메서드
    * x.length
    * x.forEach
        ```javascript
        let x = [10,20,30,40];
        x.forEach(x => console.log(x**2))//[100.400.900.1600]
    * x.map : 기존 배열 내의 모든 요소들을 주어진 함수를 호출한 결과를 모아 새로운 배열을 반환, 데이터를 뽑아내는 용도
        ```javascript
        [10,20,30,40].map(X=>x+100) // [110,120,130,140]
        ```
    * x.filter
    ```javascript
    [1,2,3,4,5,6,7].filter(x => x>4) //[5,6,7]
    ```
    * x.find : filter와 다르게 찾으면 끝남. 협업에서는 서비스중인 ID를 찾을때 쓰임.
    ```javascript
    [1,2,3,4,5,6,7].find(x => x>4) //[5] 

    ```
```javascript
array(100) // 비어있음 * 100
Array(100).fill(0).map((value, index)=> value + index) // 0~99
Array(100).fill(0).map((value, index)=> value + index +1) // 1~100
```
### Object

```javascript
[{
    "지역이름": "전국", // key : value(2개의 집합을 가리켜 객체 프로퍼티)
    "확진자수": 24889,
    "격리해제수": 23030,
    "사망자수": 438,
    "십만명당발생율": 48.0
}] // array안에 object가 있음

let x=1, y=2, z=3
let object = {x, y, z} // {x: 1, y: 2, z: 3}
```
- 호출 : 변수명, 변수명.지역이름, 변수명['지역이름'] (변수명.key, 변수명[key])
- 삭제 : delete value['hello']는 추천하지 않음(메모리 상에 'world'가 남아있음, value['hello'] = null을 권장)

-메서드 : Object.keys, Object.values, Object.entries
```javascript
    let human = {
    name:'hojun3',
    age:30,
    local:'jeju'
}
console.log(human) // object형 { name: 'hojun3', age: 30, local: 'jeju' }
let hojun = new Map(Object.entries(human)) // object를 map형식으로 바꿔줌.
console.log(hojun.keys()) //{ 'name', 'age', 'local' }
console.log(hojun.values()) // { 'hojun3', 30, 'jeju' }
console.log(hojun.entries())
/* {
    [ 'name', 'hojun3' ],
    [ 'age', 30 ],
    [ 'local', 'jeju' ]
  } */
```
### set : object
- 메서드 : add, delete, has, size
- 중복을 허락하지 않는다
- 게시물을 쓴 게시자 이름의 집합이면 몇 명이나 게시물을 썼는지 알 수 있다.
```javascript
let set = new Set()
set.add(1)
set.add(2)
console.log(set) //Set(2) { 1, 5 }
console.log(set.size) //2

// 중복 허락하지 않음.
let a = new Set([1, 2, 3, 3, 3, 3])
let b = new Set('helllllllllo')
console.log(a) //Set(3) { 1, 2, 3 }
console.log(b) //Set(4) { 'h', 'e', 'l', 'o' } 
```
## 조건문과 반복문

### 조건문
- 삼항 연산자
```javascirpt
let result = true ? 1 : 100; // ? 앞에 true이면 1를 result에게 돌려주겠다.
console.log(result) // 1

let result2 = true ? console.log("one") : console.log("two")
console.log(result2)// one

let result3 = false ? console.log("one") : console.log("two")
console.log(result3)// two
```

- switch
```javascript
let day
switch (new Date().getDay()) {
  case 0:
    day = "일";
    break;
  case 1:
    day = "월";
    break;
  case 2:
    day = "화";
    break;
  case 3:
    day = "수";
    break;
  case 4:
    day = "목";
    break;
  case 5:
    day = "금";
    break;
  case 6:
    day = "토";
}
console.log(day) // 오늘 요일을 알려줌. 화

```
### 반복문
- 구구단 만들기
```javascript
for (let i = 1; i<10; i++){
    for (let j = 1; j<10; j++){
        console.log(`${i} * ${j} = ${i*j} `)
    }
}
```
- for를 이용하여 숫자 더하기?
```javascript
let s = 0
let a = '19821'
for (let i of a){
   s += parseInt(i)
}
console.log(s) //21

//array

let c = {'one':1, 'two':2};
for (let i in a) {
    console.log(i); // key값만 출력됨.
    console.log(a[i]); // value값만 출력
}
/*
one
1
two
2
*/

//무한반복
let x = 0;
while (x < 10) {
    console.log(x);
    x++; // x++가 없다면 0<10 므로 무한반복문
} //0 1 2 3 4 5 6 7 8 9


for(;;){

}

while(true){}

// 반복문 탈출
for (let i = 0; i < 10; i++) {
    if (i == 5) {
        break; // i가 5가 되었을때 반복문을 탈출함.
    }
    console.log(i)
}

// continue
for (let i = 0; i < 10; i++) {
    if (i == 5) continue; //5를 건너띄고 다음 루프로 넘어감.
    console.log(i); 1 2 3 4 6 7 8 9
}
```

## 함수와 클래스

### 함수(파선아실)
- 사용 이유 
 1. 재사용성
 2. 아키텍처 파악
 3. 유지보수

- 여기서 x, y를 보통 한국에서는 인자
- 매개변수(파라미터, parameter) : x, y
- 전달인자(아규먼트, argument) : 3, 5

```javascript

function add(x, y){ 
    return x + y; // x,y 파라미터
}

add(3, 5) // 3,5 아규먼트

//호이스트 O -> 내용을 최상위로 올려준다. function을 쓰기 전에 써도 사용 가능.
function add(a = 100, b = 200) { //디폴트값
    console.log(a, b);
    return a + b;
}
// 호이스트 X (사실 호이스트를 일어나지만 일시적인 사각지대에 빠져 에러가 남.)
let add2 = function(x,y){
    return x+y
}

add(10, 20);
// 30
add(10);
// 210
add();
// 300
add(b=300) // a에 입력
// 500
add(undefined, 300); // undefined 변수는 있는데 아무 값이 없을때
// 400

function add({ a = 100, b = 200 }) {
    console.log(a+b);
}

add({b: 300}); // 400
```

### 콜백함수
- 함수를 아규먼트로 주고 내가 너를 나중에 시행시키겠다.
- 결국 함수도 변수다.
```javascript
function add(x, y) {
    return x + y;
}

function mul(x, y) {
    return x * y;
}

function cal(a, b){ 
    return a(10, 10) + b(10, 10); // 내부에서 시행시켜줌.
}

cal(add, mul); // 함수를 아규먼트로 받아서

// 화살표 함수를 콜백함수로 사용

function cal(a, b){
    return a(10, 10) + b(10, 10);
}

cal((a, b) => a + b, (a, b) => a * b);
    //add           , mul
```
- 화살표 함수를 콜백함수로 사용했을 경우의 장단점
    - 장점 : 네이밍을 안해도 됩니다.
    - 장점 : 다른 곳에서 사용할 수가 없다.
    - 단점 : 콜백지옥에 빠질 수가 있습니다

### 화살표 함수
```javascript
function 제곱(x) {
    return x**2
}

// 함수표현식, 호이스팅 X
let 제곱 = x => x**2;

function f(a, b) {
    let z = 10
    let result = z + a + b
    return result
}

// 함수표현식, 호이스팅 X
let f = (a, b) => {
    let z = 10
    let result = z + a + b
    return result
};
```
## 클래스

```javascript
class Notice {
    constructor(title, contents, author){
        this.title = title
        this.contents = contents
        this.author = author
    }
    수정하기(title, contents, author){
        this.title = title
        this.contents = contents
        this.author = author
    }
}

dataBase = []
게시물1 = new Notice('제목1', '내용1', '저자1') //게시물1 인스턴스
dataBase.push(게시물1)
게시물2 = new Notice('제목2', '내용2', '저자2')
dataBase.push(게시물2)
게시물3 = new Notice('제목3', '내용3', '저자3')
dataBase.push(게시물3)

dataBase.forEach(d => {
    제목 = document.createElement('h1')
    제목.textContent = d.title
    내용 = document.createElement('p')
    내용.textContent = d.contents
    저자 = document.createElement('p')
    저자.textContent = d.author
    document.body.append(제목)
    document.body.append(내용)
    document.body.append(저자)
})

// dataBase.splice()와 같은 것으로 삭제, 실제로는 mongoDB와 같은 곳에서 삭제


class human {
    attack(){
        console.log("공격!!")
    }
    defense(){
        console.log("방어!!")
    }
}

seungwoo = new human()
console.log(seungwoo.attack()) // 공격!
```
- 왜 class로 만드냐?
승우가 아니더라도 길동, 동자 등으로 

-상속
```javascript
// 고급휴먼에 구현되어 있지 않지만 human에 구현되는 기능을 쓸 수 있음.
clase 고급휴먼 extends human {
    마법(){
        console.log('파이어볼!')
    }
}

춘향 = new 고급휴먼()
춘향.마법() // 파이어볼
춘향.attack() // 공격!!
춘향.defense() // 방어!!
```
## 예외처리, 전개표현식, 정규표현식, 리터럴 등
### 예외처리
```javascript

try {
    xxxx += 10000
 } catch(e) {
    console.log("에러!")
    console.error(e)
 } finally { //무조건 시행됨.
    console.log("finally")
 }
 ```

 ### 전개구문 사용
 ```javascript
 let arr1 = [1, 2, 3, 4];
let arr2 = [10, 20, 30, 40];
let arr3 = [100, ...arr1, 200, ...arr2, 300] // 전개가 되서 들어감.
let arr4 = [100, arr1, 200, arr2, 300] 

console.log(arr3)
/* [
    100,  1,  2,  3,  4,
    200, 10, 20, 30, 40,
    300
  ] */
console.log(arr4)
// [ 100, [ 1, 2, 3, 4 ], 200, [ 10, 20, 30, 40 ], 300 ]
Math.max(...arr3); //min과 max를 사용할때도 전개를 하여 사용해야함.
let [a, b, c, ...d] = [10, 20, 30, 40, 50, 60, 70]
console.log(d) //[ 40, 50, 60, 70 ]
```
### 정규표현식
```javascript

// 0 문자 제거
let s = '010100020201020304812123';
s.replace(/[^1-9]/g,"") //1~9까지 아닌 숫자를 끄집어 내겠다.
'11221234812123'
```
연습사이트에서
h[eao]+llo world // eao가 한개 이상 나올 수도 있다.

### 리터럴
- 2진수, 8진수, 16진수 리터럴
let a = 0b1001 // a == 9 b 바이너리
let b = 0o1001 // b == 513 o 옥사
let c = 0x1001 // c == 4097 x 헥타

### 구조분해할당

```javascript
let[a,b,c] = [10,20,[100,200]]
console.log(c) // [100,200]
```

## 동기와 비동기

- 자바스크립트 동작 원리 공부하기!
- js는 일을 처리할 수 있는 thread가 1개, 싱글쓰레드라고 함.
- 벗 모든 일을 여러명이 처리할 수 없다면 ,항상 기다려야되는 문제가 생길 수 있고 무한대기에 빠질 수 있음.

```javascript
// 순서대로 한다면 덧셈, 곱셈, hello world 순이지만
// 비동기이기 때문에 hello world, 곱셈, 덧셈 순이 됨
function 덧셈(a, b, 콜백함수) {
    setTimeout(()=>{
        let result = a + b
        console.log(result)
    }, 2000)
}
function 곱셈(a, b, 콜백함수) {
    setTimeout(()=>{
        let result = a * b
        console.log(result)
    }, 1000)
}

덧셈(20, 30)
곱셈(2, 6)
console.log('hello world')
```

- Promise
     - pending(대기상태) - resolve(해결) - fulfilled(성공)
     - pending(대기상태) - reject(거부) - rejected(실패)

     ```javascript
     new Promise((resolve, reject) => {
        //code
    })
    .then(result => result) //resolve
    .then(result => result) //resolve
    .catch(err => err) // reject시 
    .finally(result => result) // 무조건

    //에러처리 안되어 있는 코드
    let p = new Promise(function(resolve, reject) {
    resolve('hello world');
    }).then(메시지 => { //resolve('hello world')가 메시지로
        alert(메시지);
        return 메시지.split(' ')[0]
    }).then(메시지 => { //위에 return된 값이 메시지로 들어감.
        alert(메시지);
        return 메시지[0]
    }).then(메시지 => { // 위에 return된 값이 메시지로 들어감.
        alert(메시지);
    });

    //html,css를 쓰면 데이터값들이 동적으로 들어가지 않게 된다.
    const f = fetch('https://raw.githubusercontent.com/paullabkorea/coronaVaccinationStatus/main/data/data.json') //마스크 알리미 데이터
    .then(function(response) {
        return response.json();

    })
    .then(function(json) { //위에 리턴값이 json으로 들어감.
        console.log(json);
        return json
    })
    ```

## DOM
    document.querySelector("selecor"); tag
    document.querySelector("#selecor"); id
    document.querySelector(".selecor"); class
