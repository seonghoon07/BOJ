hour,drink = map(int, input().split())
if drink:
  print("280")
elif hour >= 12 and hour <= 16:
  print("320")
else:
  print("280")