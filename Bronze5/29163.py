n = int(input())
nums = list(map(int,input().split()))

jjak = 0
hol = 0

for i in nums:
  if i % 2 == 0:
    jjak += 1
  else:
    hol += 1

if jjak > hol:
  print("Happy")
else:
  print("Sad")