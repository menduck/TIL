# 9012 괄호
'''
https://www.acmicpc.net/problem/9012

# 문제 풀이
- stack을 이용하여 문제를 풀었다.
- 스택 안에 괄호를 하나씩 넣어 준다.
- 만약 가장 최신으로 들어간 데이터가 '('이고 들어갈 데이터가 ')'라면 스택의 최신으로 들어간 데이터 '('을 제거한다.

# solution 

```py
import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
  data = sys.stdin.readline().strip()
  stack = []

  for bracket in data:
    if len(stack) == 0 :
      stack.append(bracket) 
    elif stack[-1] == '(' and bracket == ')':
      stack.pop()
    else:
      stack.append(bracket) 
  
  if len(stack) == 0:
    print('YES')
  else:
    print('NO')
```
- 만약 '))((' 문자열이 들어온다면
- 처음에 ')' 닫힌 괄호부터 들어오면 더 이상 코드를 진행하지 않고 무조건 NO 라고 판단되지만 
- 위 코드는 모든 과정을 끝까지 실행해야 틀렸다고 판단할 수 있다.

'''
import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
  data = sys.stdin.readline().strip()
  stack = []

  for bracket in data:
    if bracket == '(':
      stack.append(bracket)
    elif bracket == ')':
        if stack: # 빈 문자열이 아니면 True
          stack.pop()
        else: # ')'이 빈 문자열에 들어오면 바로 'No'를 출력하고 실행을 종료함.
          print('NO')
          break
  
  if len(stack) == 0:
    print('YES')
  else:
    print('NO')

