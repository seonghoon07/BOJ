sentence = input()

for i in sentence:
  if (i.isupper()):
    print(i.lower(),end="")
  if (i.islower()):
    print(i.upper(),end="")