n = int(input())
if n == 0:
  n = 1
total = 1
for i in range(1,n+1):
  total *= i
print(total)