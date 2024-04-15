import sys
input = sys.stdin.readline

n = int(input())
arr = []

m = int(input())
for j in range(m):
  total = 0
  find_item = int(input())
  for k in range(n):
    if (arr[k] == find_item):
      total += 1
  print(total)