# 9093 단어 뒤집기
'''
https://www.acmicpc.net/problem/9093

# 문제풀이
- T를 입력받아 for문을 돌려 T만큼 문장을 입력받는다.
- 문장을 공백으로 split한다 => str.split()은 list로 반환됨.
- list로 반환된 문장을 for문을 돌려 항목을 하나씩 뒤집고 리스트에 다시 묶어 언패킹하여 출력한다.

'''

import sys
T = int(sys.stdin.readline().strip())

for _ in range(T):
  sentence = sys.stdin.readline().strip().split()
  # 문장의 항목 하나씩 뒤집어 리스트에 담고 언패킹하여 출력함.
  print(*[word[::-1] for word in sentence])

# while문으로 풀어보기

word = 'level'

# 값 초기화
# start = 0, end = 
start = 0
end = len(word) -1

is_pal = True

# while
# start<end일때
  # 매 반복마다 start값은 1씩 증가, end값은 1씩 감소한다.
while start < end:
  if word[start] != word[end]:
    is_pal = False
    break
  start += 1
  end -= 1

# 출력
# 팰린트롬이면 1, 아니면 0으로 출력

if is_pal:
  print(1)
else:
  print(0)