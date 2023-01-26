# 2161 카드

'''
https://www.acmicpc.net/problem/2161

# 문제 풀이
- 1부터 N까지 리스트로 만든다.
- 남은 카드가 한 장일 될때까지 아래의 과정을 반복한다.
  - 가장 위에 있는 카드를 제거(pop(0))하고 그 값을 출력한다.
  - 그 다음 가장 위에 있는 카드를 카드 뒷장에 넣는다.
    - 가장 위에 있는 카드인 값(pop(0))을 카드 리스트에 append하여 넣어줌
'''

import sys
N = int(sys.stdin.readline().strip())
card_list = [num for num in range(1,N+1)]

while len(card_list) > 1:
  print(card_list.pop(0), end = ' ')
  card_list.append(card_list.pop(0))
print(*card_list)