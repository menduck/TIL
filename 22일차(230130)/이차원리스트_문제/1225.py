# 1225 이상한 곱셈

# solution - 시간 초과
# 이중 for문이기 때문에 시간 복잡도는 O(n)으로 계산된다.
import sys
A, B =  sys.stdin.readline().split()

result = 0
for i in A:
    for j in B:
        result += int(i)*int(j)
print(result)

# soltuion - 성공
import sys
A, B =  sys.stdin.readline().split()

result = 0
print(sum(list(map(int, A)))* sum(list(map(int, B))))

'''
A =abc, B = de
a*d+ b*d + c*d + a*e+ b*e + c*e
= (a+b+c)*d + (a+b+c)*e
= (a+b+c)*(d*e)
'''