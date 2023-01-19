# 17249 태보태보총난타
'''
https://www.acmicpc.net/problem/17249

# 문제 풀이
- 입력값을 입력받아 (^0^) 얼굴모양을 구분자로 써 나눈다.
- 왼쪽값과 오른쪽 값에서 '@' 카운팅해서 출력한다.
'''
import sys
data = sys.stdin.readline().strip().split('(^0^)') # ['@===@==@=@==', '==@=@===@']
print(data[0].count('@'), data[1].count('@'))

