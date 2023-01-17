'''
# 문제풀이
- while문을 통해 계속 테스트 케이스를 공백을 구분하여 A와 B를 입력 받는다.
- 단, A와 B가 0인 경우 프로그램을 종료한다. (종료 조건)
  - A > 0 , B > 10 이기때문에 A와 B가 0일때 빼곤 이 둘의 합이 0인 경우는 없다.
- 종료되지 않으면 A와 B의 합을 출력한다.
'''
import sys

while True : # 계속해서 입력받는다.
  A,B = list(map(int, sys.stdin.readline().strip().split()))
  if A+B ==0 : # 단, A와 B가 0이면 break문을 만나 while문을 종료한다
    break
  print(A+B) # A와 B가 0이 아니면 합을 출력한다.