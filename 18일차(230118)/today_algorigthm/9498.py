# 9488 시험성적
'''
https://www.acmicpc.net/problem/9498
'''
import sys
score = int(sys.stdin.readline().strip())

if score >= 90 :
  print('A')
elif score >= 80 :
    print('B')
elif score >= 70 :
    print('C')
elif score >= 60 :
    print('D')
else :
    print('F')