# 함수와 내장함수,메서드의 차이점?

- ***함수*** 의 종류 중 사용자 정의 함수, ***내장 함수***, 람다 함수가 있음.
  - 내장 함수는 python 자체에 가지고 있는 함수임
  - 함수명(파라미터) 형식으로 호출함.

- ***메서드*** 는 객체에 적용되는 함수 또는 클래스 내부에 정의한 함수임.
  - 각 데이터타입마다 메소드가 있음.
  - 데이터타입.메서드(파라미터) 형식으로 호출함.

## 데이터 타입별 메소드
  
### 문자열 메소드

#### 문자열을 탐색/ 검증하는 메소드

> str.find(x)

- x의 ***첫 번째 위치*** 를 반환, 없으면 -1를 반환함.

```py
print('apple'.find('p')) # 1
print('apple'.find('-k')) # -1
```

> str.index(x)

- x의 ***첫 번째 위치*** 를 반환, 없으면 ValueError
```py
print('apple'.index('p')) # 1
print('apple'.index('-k')) # ValueError
```

> str.isalpha()

- 모든 문자열이 알파벳이면 True, 아니면 False를 반환함.
```py
print('Ab'.isalpha()) # True
print('A123'.isalpha()) # False
```

> str.isupper()

- 모든 문자열이 대문자이면 True, 아니면 False를 반환함.
```py
print('Ab'.isupper()) # False
```

> str.islower()

- 모든 문자열이 소문자면 True, 아니면 False를 반환함.
```py
print('ab'.isupper()) # True
```

> str.istitle()

- 모든 단어의 첫 글자는 대문자, 나머지는 소문자이면 True, 아니면 False를 반환함.

```py
print('Apple Is Sweet'.istitle()) # True
print('Apple is Sweet'.istitle()) # False
```
#### 문자열을 변경하는 메소드

> str.replace(old, new[,count])

- 바꿀 대상 글자를 새로운 글자로 바꿔서 변환함.
-count를 지정하면, 해당 개수만큼 실행함.

```py
print('benene'.replace('e','a')) # banana
print('---exit---'.replace('-','!',3)) # !!!exit---
```

> str.strip('char')

- 특정한 문자를 지정하면
- 양쪽을 제거 => .strip('char')
- 왼쪽을 제거 => .lstrip('char')
- 오른쪽을 제거 => .rstrip('char')
- 문자를 지정하지 않으면 공백을 제거함.

```py
print('***주의***'.strip('*')) # 주의
print('00000580'.lstrip('0')) # 580
print('010********'.rstrip('*')) # 010
print('      짠'.strip()) # 짠
```

> str.split(sep = None, maxsplit = -1)

- 구분자를 이용하여 문자열을 나눠 리스트로 반환함
- sep = None
  - 구분자(sep)의 기본값은 공백임.
  - 이용하고자 하는 구분자를 넣으면 됨.
- maxsplit 
  - maxsplit는 분리할 단어의 개수를 의미
  - maxsplit = -1이 기본값, -1이면 제한이 없음

```py
print('a&b&c&b'.split('&')) # ['a', 'b', 'c', 'b']

print('a b c b'.split()) # ['a', 'b', 'c', 'b']
print('a b c b'.split(' ',1)) # ['a', 'b c b']
print('a b c b'.split(' ',2)) # ['a', 'b', 'c b']
print('a b c b'.split(' ',3)) # ['a', 'b', 'c', 'b']
print('a b c b'.split(' ',-1)) # ['a', 'b', 'c', 'b'] 
```

> 'separator'.join([iterable])

- 반복 가능한 (iterable) 컨테이너 요소들을 separator(구분자)로 합쳐 문자열로 반환함.
- 만약 iterable에 문자열이 아닌 값이 있으면 TypeError발생

```py
print(''.join(['a', 'b', 'c', 'b'])) # abcb
print(','.join(['a', 'b', 'c', 'b'])) # a,b,c,b
print('&'.join(['a', 'b', 'c', 'b'])) # a&b&c&b
```
- 기타

```py
meg = 'Hi! Everyone!'

# str.capialize()
# 문자열 첫 글자 대문자, 나머지는 소문자로 반환
print(meg.capitalize()) # Hi! everyone!

# str.title()
# 단어 첫 글자 대문자, 나머지 소문자
print(meg.title()) # Hi! Everyone!

# str.upper()
# 모든 글자를 대문자로 반환
print(meg.upper()) # HI! EVERYONE!

# str.lower()
# 모든 글자를 소문자로 반환
print(meg.lower()) # hi! everyone!

# str.swapcase()
# 대문자는 소문자로, 소문자는 대문자로 반환
print(meg.swapcase()) # hI! eVERYONE!
```

### 리스트 메소드
- 리스트
  - 변경 가능한 값들의 나열된 자료형
  - 순서를 가지고, 서로 다른 타입의 요소를 가질 수 있음.
  - 변경 가능, 반복 가능
  - 항상 []대괄호 형태, 요소는 콤마로 구분
- 만약 리스트 메소드가 없다면 반복문을 돌리면서 요소 하나씩 적용시켜야 함.

#### 리스트의 값 추가 및 삭제

> list.append(x)

- list의 마지막 항목에 x을 추가함.

```py
과자 = ['새우깡', '바나나킥', '빼빼로']
과자.append('초코파이')

print(과자) # ['새우깡', '바나나킥', '빼빼로', '초코파이']
```

> list.insert(i,x)

- 정해진 위치 i에 값을 추가함.
- list의 길이보다 i값이 크면 마지막 항목에 x을 추가함

```py
과자 = ['새우깡', '바나나킥', '빼빼로']
과자.insert(1, '블랙새우깡')
print(과자) # ['새우깡', '블랙새우깡', '바나나킥', '빼빼로']
과자.insert(1, '블랙새우깡','쌀새우깡') # TypeError 인자는 두 개만 입력 받는다.

과자.insert(1000,'과자끝')
print(과자) # ['새우깡', '블랙새우깡', '바나나킥', '빼빼로', '과자끝']
```

> list.remove(x)

- list에서 값이 x인 것 삭제
- list에 x가 없으면 ValueError발생

```py
numbers = [1, 2, 3, 'hi']
numbers.remove('hi')
print(numbers) # [1, 2, 3]
numbers.remove('hello') # ValueError
```

> list.pop(i)

- 정해직 위치 i에 있는 값을 삭제, 그 항목을 반환함.
- i가 없으면, 마지막 항목을 삭제하고 그 항목을 반환함

```py
과자 = ['새우깡', '바나나킥', '콜라', '빼빼로']
not_과자 = 과자.pop(2) 
print(not_과자) # 콜라
print(과자) # ['새우깡', '바나나킥', '빼빼로']

last_과자 = 과자.pop()
print(last_과자) # 빼빼로
```
> list.extend(추가될 리스트, 추가할 리스트)

- 두 개의 리스트를 병합
- 추가될 리스트엔 추가할 리스트가 추가되어 데이터 변형이 발생. 주의!
- 추가할 리스트에는 원본 데이터가 유지되고 있음. 

```py
과자 = ['새우깡', '바나나킥', '콜라', '빼빼로']
my_과자 = ['뻥이요','초코과자'] 

과자.extend(my_과자)
print(과자) # ['새우깡', '바나나킥', '콜라', '빼빼로', '뻥이요', '초코 
과자']
print(my_과자) # ['뻥이요','초코과자'] 
```

> list.clear()

- 모든 항목을 삭제함

```py
과자 = ['새우깡', '바나나킥', '콜라', '빼빼로']
과자.clear()
print(과자) # []
```

#### 리스트 탐색 및 정렬

> list.index(x)

- x값을 찾아 해당 index를 반환
- x값이 없을 경우 ValueError

```py
numbers = [1,2,3,4,5]
print(numbers.index(5)) # 4
print(numbers.index(100)) # ValueError
```

> list.count(x)

- 리스트에서 x값이 몇 개 있는지를 반환함.

```py
number = [0,0,0,1,1]
print(number.count(0)) # 3
print(number.count(1)) # 2
```

> list.sort() / sorted(list)

list.sort()
- 원본 리스트를 정렬함. None 반환
  => 원본 데이터를 변경

list.sorted()
- 정렬된 리스트를 반환, 원본 데이터 유지
- 기본값은 오름차순/ reverse = True 내림차순


```py
numbers = [2,1,5,4,3]
result = numbers.sort()
print(numbers, result) # [1,2,3,4,5] None

numbers.sort(reverse = True) # 내림차순
print(numbers) # [5, 4, 3, 2, 1]

# sorted(list)
numbers = [2,1,5,4,3]
result = sorted(numbers)
# 원본 데이터 유지
print(numbers, result) # [2, 1, 5, 4, 3] [1, 2, 3, 4, 5]

sorted(numbers,reverse = True) # 내림차순 # [5, 4, 3, 2, 1]
print(numbers) # [2, 1, 5, 4, 3]
```

> list.reverse()

- 순서를 반대로 뒤집음, None 반환

```py
str = ['로','꾸','거']
result = str.reverse() 
print(str, result) # ['거', '꾸', '로'] None
```

### 세트 메소드 
- 중복을 허용하지 않음.
- 순서가 없음
  - 순서가 없기 때문에 index로 접근X (list나 tuple에 담아서 index로 접근)
  
set()의 값 추가/ 여러 값 추가/ 제거

```py
a = set([1,2,3])

# 특정 값 추가
a.add(4)
print(a) # {1, 2, 3, 4}

# 여러 값 추가
a.update([5,6,7,8])
print(a) # {1, 2, 3, 4, 5, 6, 7, 8}

# 특정 값 제거
a.remove(1)
print(a) # {2, 3, 4, 5, 6, 7, 8}
```

### 딕셔너리 메소드

- 키와 값 쌍으로 이뤄진 모음
  - 키 : 불변 자료형만 가능 (리스트, 딕셔너리 등은 불가능)
  - 값 : 어떠한 형태든 상관없음

- {키 : 값, 키:값}
- 변경 가능, 반복 가능
  - 딕셔너리를 반복하면 키가 반복됨

> dict.keys()

- 딕셔너리의 모든 키를 담아 객체로 반환

> dict.values()

- 딕셔너리의 모든 값를 담아 객체로 반환

> dict.items()

- 딕셔너리의 모든 키와 값의 쌍을 담아 객체로 반환

```py
my_dict = {'주은' : 5, '현경': 3, '태우': 7}

# 딕셔너리의 모든 키를 담아 객체로 반환
my_dict.keys()
print(my_dict.keys()) # dict_values([5, 3])
print(list(my_dict.keys())) # [5, 3]

# 딕셔너리의 모든 값를 담아 객체로 반환
my_dict.values()
print(my_dict.values()) # dict_keys(['주은', '현경'])
print(list(my_dict.values())) # ['주은', '현경']

# 딕셔너리의 모든 키와 값의 쌍을 담아 객체로 반환
my_dict.items()
print(my_dict.items()) # dict_items([('주은', 5), ('현경', 3)])
print(list(my_dict.items())) # [('주은', 5), ('현경', 3)]
```

> dict.get(key[,default])

- key를 통해 value를 가져옴
- 해당 key가 없을때, KeyError가 발생하지 않으며 default값을 설정할 수 있음.
  - 바로 인덱스로 접근했을때 key가 없으면 KeyError 발생함.

```py
my_dict = {'주은' : 5, '현경': 3, '태우': 7}
my_dict.get('주은') # 5
print(my_dict.get('태호')) # None

# 중괄호로 접근시 error발생
print(my_dict['태호']) # KeyError: '태호'

my_dict.get('태호', 10) # 10
```
> dict.pop(key[, default])

- 딕셔너리에 key가 있으면 제거하고 해당 값을 반환/ 없으면 default 반환
- key도 없고 default값도 없으면 KeyError

```py
my_dict = {'주은' : 5, '현경': 3, '태우': 7}
taewoo = my_dict.pop('태우')
print(taewoo) # 7
print(my_dict) # {'주은': 5, '현경': 3}

# key가 없지만 default값이 있으니 default 반환
taeho = my_dict.pop('태호',50)
print(taeho) # 50

# key도 없고 default값도 없으면 KeyError
minji =  my_dict.pop('민지')
print(minji) # KeyError
```

> dict.update(key=value)

- 값을 제공하는 key, value로 덮어쓰임

```py
my_dict = {'주은' : 5, '현경': 3, '태우': 7}
my_dict.update(주은=55)
print(my_dict) # {'주은': 55, '현경': 3, '태우': 7}
```


