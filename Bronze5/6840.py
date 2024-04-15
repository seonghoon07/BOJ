import sys
input = sys.stdin.readline

bowl_list = []
for _ in range(3):
  bowl = int(input())
  bowl_list.append(bowl)

bowl_list.remove(max(bowl_list))
bowl_list.remove(min(bowl_list))

print(*bowl_list)