# 2720 세탁소 사장 동혁
'''
https://www.acmicpc.net/problem/2720

# 문제 풀이
- 거스름돈에서 큰 동전 단위 기준으로 나누고 몫을 저장하고 나머지 값은 다시 거스름돈으로 계산한다.
  - 거스름돈에 가장 큰 동전 단위로 나눠 몫을 저장한다.
  - 가장 큰 동전 단위로 나눈 나머지 값이 다시 거스름돈이 되고 2번째로 큰 동전 단위로 나눠 몫을 저장하고 나머지 값이 거스름돈이 된다.
  - 마지막 동전 단위까지 위 과정을 반복하고 저장한 몫을 출력한다.

'''
import sys
T = int(sys.stdin.readline().strip())
coin_unit = [25,10,5,1]
for _ in range(T):
  coin_count = []
  changes = int(sys.stdin.readline().strip())
  for coin in coin_unit:
    coin_count.append(changes//coin)
    changes = changes%coin
  print(*coin_count)