'''
https://www.acmicpc.net/problem/10824

10824 네 수

# 문제풀이
A,B,C,D
'A''B' +'C'D'의 값을 출력
ex) '1'+'3' = '13'
'''
import sys
# string타입으로 입력받아 각 A,B,C,D에 할당함.
A,B,C,D = sys.stdin.readline().strip().split()

# 문자열 A,B를 더한 값의 int값과 문자열 C,D를 더한 값의 int값을 더해 출력함.
print(int(A+B)+int(C+D))



