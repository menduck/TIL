'use strict';

// 1. class 선언
class Person {
  // Constructor
  constructor(name,age){
    this.name = name;
    this.age = age;
  }

  // Methods
  speak() {
    console.log(`${this.name}~ hello!`)
  }
}

// 1-1 object 생성
const woo = new Person('woo',14);
console.log(woo.name); //woo
console.log(woo.age); //14
woo.speak();

// 2. Getter ad setters

class User{
  constructor(firstName,lastName,age){
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;

  }

  get age() { // get을 이용해서 값을 return한다.
    return this._age;

  }

  set age(value) { // set을 이용해서 값을 설정한다.
    // 방법 1
    // if(value <0){
    //   throw Error('age can not be negative');
    // }
    // this._age = value

    // 방법2
    this._age = value <0 ? 0 : value;

  }
}

const user1 = new User('Steve','Job',-1);
console.log(user1.age)

// 3. Fields(public,private)
class Experiment{
  publicField = 2; //외부에서 접근 가능
  #privateField = 0; //class 내부안에서만 접근 가능, 외부에선 undefined
}

const experiment = new Experiment();
console.log(experiment.publicField);
console.log(experiment.privateField);

// 4.Static properties and methods
// 들어오는 obj과 상관없이 공통적으로 class에서 쓰는 경우 메모리의 사용을 줄일 수 있음.

class Article {
  static publisher = "minkmink";
  constructor(articleNumber){
    this.articleNumber = articleNumber;
  }

  static printPublisher(){
    console.log(Article.publisher);
  }
}

const article1 = new Article(1);
const article2 = new Article(2);
console.log(article1.publisher); //undefined 
console.log(Article.publisher); //class 자체에 붙어있기 때문에 클래스이름을 이용해서 호출행함.
Article.printPublisher();

// 4. 상속
// 다른 클래스에 확장할 수 있는 방법
class Shape{
  constructor(width,height,color){
    this.width =width;
    this.height=height;
    this.color=color;
  }
  draw(){
    console.log(`drawing ${this.color} color of`);
  }

  getArea(){
    return this.width * this.height;
  }
}

class Rectangle extends Shape{}
class Triangle extends Shape{
  draw(){
    super.draw();//부모의 darw()를 가져옴
    console.log("세모세모삠")
  }
  getArea(){
    return (this.width*this.height)/2
  }
}

const rectangle = new Rectangle(20,20,'blue');
rectangle.draw();
console.log(rectangle.getArea());

const triangle = new Triangle(20,20,'red');
triangle.draw();
console.log(triangle.getArea());

// 6. Class checking: instanceOf
console.log(rectangle instanceof Rectangle); //T
console.log(triangle instanceof Rectangle); //F
console.log(triangle instanceof Triangle); //T
console.log(triangle instanceof Shape); //T
console.log(triangle instanceof Object); //T 모든 클래스는 오브젝트를 상속한것이다.
