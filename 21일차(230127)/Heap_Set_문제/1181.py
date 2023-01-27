# 1181 단어 정렬

import sys
N = int(sys.stdin.readline().strip())
word_dict = {}
for _ in range(N):
  word = sys.stdin.readline().strip()
  word_dict[word] = len(word)


result = sorted(word_dict.items(), key = lambda x:(x[1],x[0]))

for w in result:
  print(w[0])
