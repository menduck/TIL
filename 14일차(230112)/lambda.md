# lamba
> lambda [parameter] : 표현식

- 표현식을 계산한 결과값을 반환하는 함수, 이름이 없는 함수임으로 익명함수라고도 불림

- return문을 가지지 않고 표현식의 결과값을 리턴함.
- 간편 조건문 외 조건문이나 반복문을 가질 수 없음

- 장점
  - 함수를 정의해서 사용하는 것보다 간결
  - def를 사용할 수 없는 곳에서도 사용이 가능

# 예제
- x와 y값을 더해주는 함수

```py
# 일반함수
def sum(x,y):
  return x+y

# 람다함수
print((lambda x,y : x+y)(1,2)) #3

sum = lambda x,y : x+y
print(sum(1,2)) # 3
```

- 1~3의 세제곱의 결과값을 가진 리스트를 만든 lambda함수

```py
result = list(map(lambda x : x**3, range(1,4)))
print(result) # [1, 8, 27]
```