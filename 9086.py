import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
  text = list(input())
  print(text[0],text[-2], sep="")