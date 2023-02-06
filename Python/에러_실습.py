# 문제 1
'''
문자열을 입력 받고 문자열에서 e 의 개수를 구해서 출력하세요.
'''
str = input('문자열을 입력하세요 > ')
cnt = 0
for char in str :
  if char == 'e' :
    cnt += 1
print(cnt)

# 문제 2
'''
문자열을 입력 받고, 문자열 중 알파벳 모음의 총 개수를 출력하세요.
'''
str2 = input('문자열을 입력하세요 > ')
vowels = ['a', 'A', 'e', 'E', 'o', 'O', 'u', 'U', 'i', 'I']
cnt = 0
for char in str2 :
  if char in vowels :
    cnt += 1
print(cnt) 

# 문제 3
'''
입력과 같은 딕셔너리 변수가 있을 때, 해당 인물의 나이를 출력하세요.
'''
dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}

dict_variable['나이'] = 24

print(f'나이 : {dict_variable["나이"]}')

# 문제 4
'''
이름, 전화번호, 거주지 정보를 입력받아 딕셔너리 구조로 저장하고, 해당 딕셔너리와 딕셔너리의 정보를 구분해서 출력하세요.
'''
user_name = input('이름을 입력하세요 > ')
user_phonenumber = input('전화번호를 입력하세요 > ')
user_residence = input('거주지를 입력하세요 > ')
person_info = {}
person_info['이름'] = user_name
person_info['전화번호'] = user_phonenumber
person_info['거주지'] = user_residence

for key in person_info :
  print(f'{key} : {person_info[key]}')

'''
이름 : 정우영
전화번호 : 010-1234-5678
거주지 : 서울시
'''

# 문제 5
'''
이름, 전화번호, 이메일, 거주지 정보를 입력받아 출력 예시와 동일한 딕셔너리 구조를 출력하세요.
'''
user_name = input('이름을 입력하세요 > ')
user_phonenumber = input('전화번호를 입력하세요 > ')
user_email = input('이메일을 입력하세요 > ')
user_residence = input('거주지를 입력하세요 > ')
person = {}
person_info = {}

person_info['전화번호'] = user_phonenumber
person_info['이메일'] = user_email
person_info['거주지'] = user_residence
person[user_name] = person_info
print(person) # {'정우영': {'전화번호': '010-1234-5678','이메일': 'bee@naver.com','거주지': '서울특별시'}}

문제 6
'''
자열을 입력받고, 문자열에서 개별 문자가 나오는 횟수를 출력하세요.
'''
str3 = input('문자열을 입력하세요 > ')
result = {}

for i in str3 :
  cnt = 0
  for j in str3 : 
    if i == j :
      cnt += 1
  result[i] = cnt

for key in result :
  print(key, result[key])