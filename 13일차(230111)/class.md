# Class

## 파이썬은 모든 것이 객체
- 객체 지향 프로그래밍: 독립적인 단위인 객체들의 모임으로 파악하는 컴퓨터 프로그래밍의 패러다임 중 하나임.

- 객체의 특징
  - type: 어떤 연산자와 조작(method)이 가능한가?
  - 속성(attribute): 어떤 데이터를 가지는가?
  - 조작법(method): 어떤 행위를 할 수 있는가?

- 객체끼리 동등한지 비교하기

```py
a = [1,2,3]
b = [1,2,3]
# a와 b는 알맹이만 같고 메모리 주소는 다름
print(a==b, a is b) # True False

a = [1,2,3]
b = a # a와 b는 같은 메모리를 가르킴
print(a==b, a is b) # True True
```

### Class 기본 문법

```py
# 클래스 정의
class 클래스명:
  some code..
  def 메서드():
    메서드코드

# 인스턴스 생성
인스턴스 = 클래스명()
# 메서드 호출
인스턴스.메서드()
# 속성
인스턴스.속성
```
## class와 instance
- class는 나만의 타입 instance는 나만의 타입의 사례
  ex) 123,900,5는 모두 int의 instance

- 속성: 객체들이 가지게 될 상태/데이터를 의미
- 메서드: 객체에 공통적으로 적용 가능한 동작(함수)

```py
class Person:
  # name이라는 속성을 가짐
  def __init__(self, name):
    self.name = name
  
  # 메서드 sayHello 생성
  def sayHello(self):
    print(f'Hello, {self.name}')
```

### instance
- 인스턴스 변수
  - 인스턴스가 개인적으로 가지고 있는 속성
  - 각 인스턴스가 고유한 변수

- 인스턴스 메서드
  - 인스턴스가 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드
  - 클래스 내부에 정의되는 메서드
  - 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨

```py
class Person:
  # name이라는 속성을 가짐
  def __init__(self, name):
    # 인스턴스 변수 정의
    self.name = name
  
  # 메서드 sayHello 생성
  def sayHello(self):
    print(f'Hello, {self.name}')

superman = Person('Lee')
# 인스턴스 변수 접근
print(superman.name) # Lee
# 인스턴스 변수 할당
superman.name = 'Kim'
print(superman.name) # Kim

# 인스턴스 메서드 접근
print(superman.sayHello()) # Hello, Lee
```

- 생성자 메서드
  - 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
  - 인스턴스 변수들의 초기값을 설정
  - 인스턴스 객체를 생성할때 기본값으로 변수의 초기값

- 소멸자 메서드
  - 인스턴스 객체가 소멸되기 직전에 호출되는 메서드

```py
class Person :
  # 생성자 메서드
  def __init__(self):
    print('인스턴스 객체가 생성되고 이 메시지가 보이면 자동으로 호출되는 메서드에 의해 출력된 것입니다.')
  
  def __del__(self):
    print('인스턴스 객체가 소멸되기 직전에 남긴 메시지 입니다.')


me = Person() # 인스턴스 객체가 생성되고 이 메시지가 보이면 자동으로 호출되는 메서드에 의해 출력된 것입니다.
del me # 인스턴스 객체가 소멸되기 직전에 남긴 메시지 입니다.
```
- self?
  - 인스턴스 자기 자신을 뜻함.
  - 첫 번째 인자로 인스턴스 자기 자신이 전달되게 설계
    - 꼭 self란 이름을 안써도 되지만, 암묵적인 규칙

- 매직 메소드 ( __매직 메서드__)
  - 특정 상황에 ***자동***으로 불리는 메서드

  ```py

class Circle:
    def __init__(self, r) :
      self.r = r
    def area(self):
      return 3.14*self.r*self.r
    def __str__(self):
      return f'[원]의 반지름: {self.r}'
    def __gt__(self, other):
      return self.r > other.r 

# 인스턴스 생성
c1 = Circle(10) 
c2 = Circle(1)

# __str__ 매직 메서드에 의해 프린트할때 자동으로 호출됨
print(c1) # [원]의 반지름: 10
print(c2) # [원]의 반지름: 1

# __gt__ 매직 메서드에 의해 부등호 사용시 자동으로 호출됨
print(c1 > c2) # True
print(c1 < c2) # False
```
