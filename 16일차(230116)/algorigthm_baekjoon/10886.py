'''
https://www.acmicpc.net/problem/10886

# 문제 풀이
- 모든 학생들의 투표 결과를 for문을 통해 list에 담는다.
- count를 사용해 0과 1의 개수를 세주고 비교하여 출력한다.
'''

import sys

t = int(sys.stdin.readline().strip())
vote_list = []
for _ in range(t):
  vote_list.append(int(sys.stdin.readline().strip()))

if vote_list.count(0) > vote_list.count(1) :
  print('Junhee is not cute!')
else:
  print('Junhee is cute!')

# 다른 방법
# 각 사람들의 설문 조사를 모두 더한 다음 투표인원수의 과반이 되면 귀엽다고 출력함.

import sys

t = int(sys.stdin.readline().strip())
score = 0

for _ in range(t) :
  vote = int(sys.stdin.readline().strip())
  score += vote

if score > t//2:
  print('Junhee is cute!')
else:
  print('Junhee is not cute!')