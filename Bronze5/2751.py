import sys
input=sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
  item = int(input())
  arr.append(item)

sorted_arr = sorted(arr)
print(*sorted_arr,sep="\n")