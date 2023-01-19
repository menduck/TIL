# 2941 크로아티아 알파벳
'''
https://www.acmicpc.net/problem/2941

# 문제 풀이
- word 변수에 입력값인 단어를 할당한다.
- 크로아티아 알파벳이 단어에 있으면 다른 문자로 바꾸어 준다.
  - 길이가 2인 크로아티아 알파벳을 길이가 1인 다른 문자로 바꾼다.
- 단어에 크로아티아가 아닌 문자는 알파벳임으로 신경쓰지 않는다.
- word의 길이를 출력한다.
'''

import sys
word =  sys.stdin.readline().strip() # ljes=njak

cro_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for w in cro_alphabet:
  word = word.replace(w,'+') # +e++ak
print(len(word)) # 6