# 문제 1
''' 
문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요.

만약, 문자열에서 e 가 없으면 -1 을 출력하세요.

단, index() / find() 메서드는 사용하지마세요.
'''
str1 = input("문자열을 입력하세요 > ")

if 'e' not in str1:
  print(-1)
for idx in range(len(str1)) :
  if str1[idx] == 'e' :
    print(idx)
    break

# 문제 2
'''
문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.

단, count() 메서드는 사용하지마세요.
'''

str1 = input("문자열을 입력하세요 > ")
str_list = str1.split(' ')

result = {}
for str in str_list :
  result[str] = result.get(str,0) + 1

for key in result :
  print(key, result[key])
  
# 문제 3
'''
문자열을 입력받고, e 를 제거한 결과를 출력하세요.

단, replace() 메서드는 사용하지 마세요.
'''
str1 = input("문자열을 입력하세요 > ")
result = ""
for s in str1 :
  if s != 'e' :
    result = result + s
print(result)

# 문제 4
'''
문자열과 알파벳을 공백으로 구분해서 입력받고,문자열에서 입력한 알파벳의 개수를 출력하세요.

단, count() 메서드는 사용하지마세요.
'''
str1, target_spelling = input('문자열을 입력하세요 > ').split(' ')

cnt = 0
for s in str1 :
  if s == target_spelling :
    cnt += 1
print(cnt)

# 문제 5
'''
단어 3개를 입력받고, 3개의 단어를 - 로 연결해서 출력하세요.

단, join() 메서드는 사용하지마세요.
'''
str1 = input("문자열을 입력하세요 > ").split(' ')
print('-'.join(str1))

# 문제 6
'''
양의 정수를 입력받고, 자리수의 합을 출력하세요.

만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요.

단, 양의 정수를 문자열로 변경하지마세요. str() 함수를 사용하지마세요.
'''
number = int(input('양의 정수를 입력하세요 > '))

if number <= 0 :
  print(-1)
else : 
  number_list = []
  while number > 0 :
    number_list.append(number%10)
    number //= 10

  sum = 0
  for num in number_list:
    sum += num
  print(sum)