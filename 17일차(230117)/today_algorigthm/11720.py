# 11720 숫자의 합
import sys
t = int(sys.stdin.readline().strip())
numbers = sys.stdin.readline().strip()
sum = 0
for num in list(numbers):
  sum += int(num)

print(sum)