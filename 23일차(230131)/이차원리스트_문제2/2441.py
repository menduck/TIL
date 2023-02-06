# 2441 별 찍기 -4

# solution - repeat와 오른쪽 정렬 rjust 활용
import sys
n = sys.stdin.readline().strip()
repeat_num = int(n)

# 반복할 숫자를 하나씩 감소한다.
while repeat_num > 0 :
    star = '*'*repeat_num
    print(star.rjust(int(n))) # n자리수 오른쪽 정렬
    repeat_num -= 1

# solution - 공백을 활용한 풀이

import sys
n = int(sys.stdin.readline().strip())
for i in range(n):
    print(' '*i+ '*'*(n-i))

'''
i 는 0~4까지 순회한다.
빈 문자열(' ')을 i만큼 반복하고 '*'를 N-i만큼 반복한다.
i = 0, 빈문자열(' ') 0개, '*' * 5(5-0)개
i = 1, 빈문자열(' ') 1개, '*' * 4(5-1)개
...
i = 4, 빈문자열(' ') 4개, '*' * 1(5-4)개

'''