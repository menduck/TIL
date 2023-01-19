# 10809 알파벳찾기
'''
https://www.acmicpc.net/problem/10809
'''

import sys
str = sys.stdin.readline().strip()
# 알파벳 a~Z까지 아스키코드값을 리스트에 저장하고
alphablet = list(range(97,123))
for i in alphablet :
  # 아스키코드값을 문자로 변환하고 인덱스 값을 반환한다.
  print(str.find(chr(i)), end = ' ')