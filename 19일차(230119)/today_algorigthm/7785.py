# 7785	회사에 있는 사람	
'''
https://www.acmicpc.net/problem/7785

# 문제풀이
- name를 key로 출입여부를 value로 딕셔너리를 만든다.
- 같은 key이면 후자로 추가된 value로 update되기 때문에 value가 leave가 남겨져 있는 key는 퇴근을 한 것이니 회사에 있지 않다.
- enter라는 value를 가지고 있는 key값을 리스트에 담고
- 사전 역순으로 출력한다.
'''
import sys
T = int(sys.stdin.readline().strip())

# key로 이름을, value를 출입여부로 딕셔너리를 만든다.
# 퇴근을 하려면 또 로그 흔적으로 인해 value값이 leave로 업데이트가 된다.
inout_dict = {}
for _ in range(T):
  name, inout = sys.stdin.readline().strip().split()
  inout_dict[name] = inout


# value가 enter인 key값은 리스트에 담는다. 
in_users = [key for key, value in inout_dict.items() if value == 'enter']

# 사전 역순으로 이름 하나씩 출력한다.
print(*sorted(in_users, reverse=True), sep = '\n')