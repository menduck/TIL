# 2577	숫자의 개수	
'''
https://www.acmicpc.net/problem/2577
'''
import sys
# result_number 기본값을 1로 두고 A,B,C를 입력받아 누적곱을 해준다.
result_number = 1
for _ in range(3):
  result_number *= int(sys.stdin.readline().strip())

# 누적곱한 값에 0~9까지 숫자를 반복하여 중복된 개수를 세어주고 value에 추가한다. ( key는 0~9)
result_dict = {}
for i in range(10):
  result_dict[i] = str(result_number).count(str(i))

# result_dict = {0: 3, 1: 1, 2: 0, 3: 2, 4: 0, 5: 0, 6: 0, 7: 2, 8: 0, 9: 0}

# print을 이용한 출력하는 방법 1
print(*list(result_dict.values()), sep= '\n')


# for문으로 돌려 하나씩 출력하는 방법 2
for n in result_dict.values():
  print(n)