# string formatting

## %-formatting (권장X)
> str %value

- Tuple(튜플)과 Dictionary(딕셔너리)를 올바르게 표시하지 못하는 등 여러 가지 일반적인 오류를 유발하기 때문에 권장하지 않음.

- C언어 sprintf()를 사용하는 것과 비슷

```py
name = 'Lee'
score = 4.5

print('Hello, %s' % name) # Hello, Lee
print('내 성적은 %d' % score) # 내 성적은 4
print('내 성적은 %f' % score) # 내 성적은 4.5
```
- s : 문자열
  d : 부호가 있는 십진수 (정수)
  f : 부동 소수점 십진수
  추가적인 변환 유형은 [공식 문서 사이트](https://docs.python.org/ko/3/library/stdtypes.html#old-string-formatting)참고

## f-string
> f'strring{표현식}'

- verion 3.6에 추가
- 문자열을 변수로 활용하여 만드는 법

### 변수 삽입
```py
name = 'minsu Kim'
age = 15

print(f'안녕! 나의 이름은 {name}, 나이는 {age}살이야! 내년에는 {age +1}살이 돼')
# 안녕! 나의 이름은 minsu, 나이는 15살이야! 내년에는 16살이 돼
```
### 함수 삽입
```py
name = 'minsu Kim'

print(f'내 이름은 총 {len(name)}글자야')
# 내 이름은 총 5글자야
```
### 여러가지 표현식
```py
name = 'minsu Kim'

print(f'나의 성은 {name[6:]}')
# 나의 성은 Kim
```
### 중괄호{} 표현하기
```py
print(f'중괄호 {{}} 두 개를 동시에 사용하면 된다')
# 중괄호 {} 두 개를 동시에 사용하면 된다
```

### 딕셔너리 삽입
```py
user = {'name' : 'minsu', 'age' : 15}

print(f'내 이름은 {user["name"]}, 나이는 {user["age"]}살이야')
# 내 이름은 minsu, 나이는 15살이야
```

## format 함수
> str.format()
```py
name = 'minsu Kim'
age = 15
print('안녕! 나의 이름은 {}, 나이는 {}살이야! 내년에는 {}살이 돼'.format(name,age,age+1))
# 안녕! 나의 이름은 minsu Kim, 나이는 15살이야! 내년에는 16살이 돼
```
- 직관적으로 어떤 변수를 쓰이는지 알 수 없음.
  - 그래서 임의로 이름을 넣어 표현할 수 있음. 
  - 하지만 반드시 'name = user_name' 형태의 입력값이 있어야 함.
```py
user_name = 'minsu Kim'
user_age = 15
print('안녕! 나의 이름은 {name}, 나이는 {age}살이야! 내년에는 {next_year_age}살이 돼'.format(name = user_name,age = user_age,next_year_age = user_age+1))
# 안녕! 나의 이름은 minsu Kim, 나이는 15살이야! 내년에는 16살이 돼
```