# 10101 삼각형 외우기
'''
https://www.acmicpc.net/problem/10101


# 문제 풀이
- set의 특징인 유일한 값의 모임을 이용하여 문제를 풀었다.
- 입력받은 세 각의 유일한 값이 60이면 Equilateral 출력한다.
- 입력받은 세 각의 유일한 값이 2개이고, 합이 180이면 Isosceles 출력한다.
- 입력받은 세 각의 유일한 값이 3개이고, 합이 180이면 Scalene 출력한다.
- 나머지 조건들은 Error를 출력한다.

# solution
```py 
import sys
angles = [int(sys.stdin.readline().strip()) for _ in range(3)]
unique_angles = set(angles)

if unique_angles == {60}:
  print('Equilateral')
elif sum(angles) == 180 and len(unique_angles) == 2:
  print('Isosceles')
elif sum(angles) == 180 and len(unique_angles) == 3:
  print('Scalene')
else:
  print('Error')

```
- 합이 180인 공통인 조건에서 두 각이 같은지, 모든 각이 다른지가 조건이기 때문에 공통인 조건을 묶어서 조건식을 수정하였다. 

'''
import sys
angles = [int(sys.stdin.readline().strip()) for _ in range(3)]
unique_angles = set(angles)

if unique_angles == {60}:
  print('Equilateral')
elif sum(angles) == 180 :
  if len(unique_angles) == 2:
    print('Isosceles')
  if len(unique_angles) == 3:
    print('Scalene')
else:
  print('Error')
