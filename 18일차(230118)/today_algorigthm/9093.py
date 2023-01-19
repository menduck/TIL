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

