import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
  password = input()
  if len(password)-1 >= 6 and len(password)-1 <= 9:
    print("yes")
  else:
    print("no")