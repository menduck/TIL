# comprehension
- list,dictionary,set, generator comprehension이 있다.
- 코드가 간결하고, 
- 새로운 배열을 만들때 유용하다. 
- 또한 반복문으로 빈 배열을 만들고 추가하는 것 보다 처리속도가 빠르다.

- 하지만 가독성이 떨어진다는 단점이 있다

# List Comprehension
- 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

```py
[표현식 for 변수 in iterable]
[표현식 for 변수 in iterable if 조건식]
```
# 예제
- 1~3의 세제곱의 결과가 담긴 리스트를 만드시오

```py
# 빈 리스트로 만들고 해당 값을 append해서 리스트 만드는 방법
result = []
for number in range(1,4):
  result.append(number**3)
print(result) # [1,8,27]

# list comprehension
[number**3 for number in range(1,4)]
```
# dictionary Comprehension
- 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법

```py
{key:value for 변수 in iterable}
{key:value for 변수 in iterable if 조건문}
```
# 예제
- 1~3의 세제곱의 결과가 담긴 딕셔너리를 만드시오

```py
# 빈 딕셔너리로 만들고 해당 값을 append해서 딕셔너리 만드는 방법
result = {}
for number in range(1,4):
  result[number]=(number**3)
print(result) # {1: 1, 2: 8, 3: 27}

# list comprehension
{number: number**3 for number in range(1,4)} # {1: 1, 2: 8, 3: 27}
```

참고[geonoo9.log](https://velog.io/@geonoo99/%ED%8C%8C%EC%9D%B4%EC%8D%AC-list-comprehension)