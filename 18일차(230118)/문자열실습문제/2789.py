# 2789 유학 금지  
'''
https://www.acmicpc.net/problem/2789
'''
import sys
word = sys.stdin.readline().strip()
not_word = 'CAMBRIDGE'
for w in word: # 입력값의 요소 하나씩 순회한다.
  if w not in not_word:  # 입력값의 요소가 not_word에 포함되지 않으면 출력한다.
    print(w,end='')