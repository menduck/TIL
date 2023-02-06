# 문제 1
# 정수 한 개를 입력 받고, 해당 숫자가 0보다 큰 숫자라면 True 아니면 False를 출력하세요.
num1 = int(input('정수를 입력하세요 > '))
print(num1 > 0)

# 문제 2
"""
정수 두 개를 입력 받고, 크기가 더 큰 정수를 출력하세요.

두 정수가 같으면 False를 출력하세요.
"""
num2 = int(input('첫 번째 정수를 입력하세요 > '))
num3 = int(input('두 번째 정수를 입력하세요 > '))

if num1 > num2 :
  print(num1)
elif num1 < num2 :
  print(num2)
else:
  print(False)

# 문제 3
'''
정수 한 개를 입력 받고, 해당 정수가 1 보다 크고, 10보다 작다면 True 아니면 False를 출력하세요.
'''
num4 = int(input('정수를 입력하세요 > '))
print(num4 > 1 and num4 < 10)

# 문제 4
'''
정수 한 개를 입력 받고 0 보다 크고, 짝수라면 True 아니면 False를 출력하세요.
'''
num5 = int(input('정수를 입력하세요 > '))
print(num5 > 0 and num5%2 == 0)

# 문제 5
'''
정수 한 개를 입력 받고, 아래 조건에 따라 출력하세요.

- 값이 100 초과 / 0 미만이면 "에러" 출력
- 값이 60 이상이면 "합격" 출력
- 값이 60 미만이면 "불합격" 출력
'''

num6 = int(input('정수를 입력하세요 > '))
if num6 > 100 or num6 < 0 :
  print("에러")
elif num6 >= 60 :
  print('합격')
else:
  print('불합격')


# 문제 6
'''
문자열을 입력 받고, 입력 받은 문자열을 반대로 한 글자씩 출력하세요.
'''

str1 = input('문자열을 입력하세요 > ')
for word in str1[::-1]:
  print(word)

# 문제 7
'''
정수 두 개를 입력 받고, 두 수 사이의 정수를 오름차순으로 출력하세요.

두 값이 같으면 False를 출력하세요
'''
num7 = int(input('첫 번째정수를 입력하세요 > '))
num8 = int(input('두 번째정수를 입력하세요 > '))
if num7 < num8 :
  for number in list(range(num7+1,num8)) :
    print(number)
elif num7 > num8 :
  for number in list(range(num8+1,num7)) :
    print(number)
else:
  print(False)

# 문제 8
'''
정수 두 개를 입력 받고, 두 수 사이의 정수를 내림차순으로 한 줄에 모두 출력하세요.

두 값이 같으면 False를 출력하세요
'''
num9 = int(input('첫 번째정수를 입력하세요 > '))
num10 = int(input('두 번째정수를 입력하세요 > '))
if num9 < num10 :
  for number in list(range(num10-1,num9,-1)) :
    print(number)
elif num9 > num10 :
  for number in list(range(num9-1,num10,-1)) :
    print(number)
else:
  print(False)

# 문제 9
'''
정수 한 개를 입력 받고, 1 부터 입력 값 사이의 정수 중 홀수만 출력하세요.

입력 값이 1보다 작으면 False를 출력하세요.
'''
num11 = int(input('정수를 입력하세요 > '))
print(0 > num11)
for number in range(1,num11,2) :
  print(number)

# 문제 10
'''
구구단을 출력하세요.
'''
for i in range(1,10) :
  for j in range(2,10) :
    print(f'{i} x {j} = {i * j}', end = '\n')