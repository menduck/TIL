# 2047 신문 헤드라인
'''
문제 풀이
- 언더바를 구분자로 split하여 입력받는다.
- 입력받은 리스트의 요소들을 순회하면서 대문자로 바꾼다.
- 언더바를 구분자로 하여 join하고 출력한다.
'''
headline_list = input().split('_')

upper_headline_list = []
for headline_str in headline_list :
  upper_headline_list.append(headline_str.upper())
print('_'.join(upper_headline_list))

'''
코드리뷰
- str.upper()은 언더바(_)는 그대로 출력된다.
  - 하지만 다른 특수문자도 언제나 출력되는 것은 아니니깐 안전하게 분리해서 코드를 짜야한다.
'''

# 2025 N줄덧셈
'''
문제 풀이
- 1부터 n까지 숫자 iterable를 만들어 요소 하나씩 순회하면서 누적합해준다.
'''
x = int(input())
sum = 0
for i in range(1,x+1):
  sum += i
print(sum)

# 1936 1대1 가위바위보
'''
문제 풀이
- A가 이긴 경우(if)가 아니면 다 B가 이긴것(else)이다
- A가 이기는 경우
  - 1 2
  - 2 3
  - 3 1
'''
A,B = map(int,input().split())

if (A == 1 and B == 3) or (A == 2 and B == 1) or (A == 3 and B == 2) :
  print('A')
else :
  print('B')

# 2027 대각선 출력하기
print('''#++++
+#+++
++#++
+++#+
++++#''')

# 2058 자릿수 더하기
'''
문제풀이
- 자연수를 문자열로 바꾸고 map을 통해 하나씩 정수형으로 바꾸고 list로 만든다.
- 리스트의 요소 하나씩 for문으로 순회하면서 누적합한다.
- 아니면 sum()으로 다 더해버린다.
'''
N = list(map(int,str(input())))
print(sum(N))

# 2019 더블더블
'''
문제 풀이

- 0부터 주어진 횟수만큼 for문을 순회하면서 
- 2의 (0부터 주어진 횟수번째)거듭제곱을 list에 더한다.
'''

count = int(input())

result = []
for i in range(count+1) :
  result.append(2**i)
print(*result)