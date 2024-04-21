n = int(input())
text = list(input())
result = 0

aeiou = ['a','e','i','o','u']

for i in text:
  for j in aeiou:
    if i==j:
      result += 1

print(result)