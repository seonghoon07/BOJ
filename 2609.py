a,b = map(int, input().split())
gcd = 0


for i in range(1, (a or b) + 1):
  if (a % i == 0 and b % i == 0):
    gcd = w 
print(gcd)
print(int(a*b / gcd))