while True:
  n = int(input())
  block = 0
  if n == 0:
    break
  for i in range(1,n+1):
    block += i
  print(block)