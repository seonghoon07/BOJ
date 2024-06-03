n = int(input())
result = sum(list(map(int, input().split())))
if result > 0:
  print("Right")
elif result < 0:
  print("Left")
else:
  print("Stay")