# 2525 오븐시계
import sys
hour, min = map(int, sys.stdin.readline().strip().split(' '))
cook_min = int(sys.stdin.readline().strip())

total_time = hour * 60 + min + cook_min

after_time_hour = total_time // 60
after_time_min = total_time % 60

if after_time_hour >= 24 :
  after_time_hour = after_time_hour - 24

print(after_time_hour, after_time_min) 