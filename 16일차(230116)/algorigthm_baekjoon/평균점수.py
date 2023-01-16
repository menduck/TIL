import sys

lines = sys.stdin.readlines()

sum = 0
cnt = 0
for line in lines:
  score = int(line)
  cnt += 1
  if score < 40:
    sum += 40
  else:
    sum += score
print(sum//cnt)



