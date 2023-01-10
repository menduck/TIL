# 2029 몫과 나머지 출력하기
# 문제 풀이
# - 첫 번째 줄에 케이스의 개수인 T를 입력받아 T만큼 반복해서 테스트 케이스를 입력받는다.
# - 테스트 케이스는 공백으로 구분하여 a,b를 받는다
# - a를 b로 나눈 몫과 나머지를 변수에 저장한다.
# - #테스트 번호(1부터 시작), 몫, 나머지를 공백으로 구분하여 출력한다.

# 코드
t = int(input())
for i in range(t) :
  a, b = map(int, input().split())
  quotient = a // b
  remainder = a % b
  print(f'#{i+1} {quotient} {remainder}')

# # 짧은 코드
t = int(input())
for i in range(t) :
  a, b = map(int, input().split())
  print(f'#{i+1} {a // b} {a % b}')

# - 변수에 저장하지 않고 바로 출력할 수도 있지만 변수명에 몫과 나머지라고 적으므로 더 가독성있는 코드가 되는 것 같다.

# 2071 평균값 구하기
# 문제 풀이
# - 첫 번째 줄은 케이스의 개수받아 t에 저장한다.
# - 케이스 개수만큼 반복하여 10개의 수를 numbers에 list형태로 저장한다.
# - 10개의 수를 다 더해 10으로 나눈 몫에 소수점 첫 번째 자리에서 반올림한 값을 mean 변수에 저장한다.
# - #테스트 번호(1부터 시작) mean값을 공백으로 구분하여 출력한다.

# 시도1 - 실패
# t = int(input())
# for i in range(t) :
#   numbers = list(map(int, input().split()))
#   mean = sum(numbers) // 10
#   print(f'#{i+1} {mean}')

# 문제 요구조건에 소수점 첫번째 자리에서 반올림하는 것을 놓쳤다.

# 시도2 - 성공
t = int(input())
for i in range(t) :
  numbers = list(map(int, input().split()))
  mean = round(sum(numbers) / 10)
  print(f'#{i+1} {mean}')

# 1938 아주 간단한 계산기
# 문제 풀이
# - 두 자연수를 공백으로 구분하여 입력받는다.
# - 두 자연수를 +,-,*,/ 계산한 값(소수점 이하는 버림)를 한줄에 한개씩 출력한다.
# 코드
import math
a, b = map(int, input().split())
print(math.floor(a+b)) 
print(math.floor(a-b)) 
print(math.floor(a*b)) 
print(math.floor(a/b)) 

# 2046 스탬프 찍기
# - 주어진 숫자를 입력받아 숫자만큼 #을 출력한다.
num = int(input())
print('#'*num)

# 2068 최대수 구하기
# - 주어진 10개의 수 중 가장 큰 수를 출력한다.
t = int(input())
for i in range(t) :
  numbers = list(map(int, input().split()))
  print(f'#{i+1} {max(numbers)}')

