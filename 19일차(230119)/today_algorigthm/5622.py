# 5622	다이얼	
'''
https://www.acmicpc.net/problem/5622
'''
import sys
alphabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
dial_dict = {alphabet[i] : i+3 for i in range(len(alphabet))}


word = sys.stdin.readline().strip()

result = 0
for a in alphabet:
  for w in word:
    if w in a:
      result += int(dial_dict[a])

print(result)


