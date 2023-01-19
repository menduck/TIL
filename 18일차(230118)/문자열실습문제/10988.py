# 팰린드롬인지 확인하기
'''
https://www.acmicpc.net/problem/10988

# 문제 풀이
- 단어를 입력받아 뒤집고 원래 단어와 같은지 확인한다.
'''
import sys
word = sys.stdin.readline().strip()

if word == word[::-1]:
  print(1)
else:
  print(0)

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