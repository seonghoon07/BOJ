n = int(input())
cnt = 0
value = 666

while True:
  if "666" in str(value):
    cnt += 1
  if cnt == n:
    break
  value += 1

print(value)