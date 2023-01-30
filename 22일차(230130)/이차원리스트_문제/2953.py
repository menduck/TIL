# 2953 나는 요리사다

import sys
user,max_score = 0,0
for user_num in range(1,6):
    user_score = sum(map(int, sys.stdin.readline().split()))
    if max_score < user_score:
        user, max_score = user_num, user_score

print(user, max_score)