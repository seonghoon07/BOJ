n = int(input())
user = []

for i in range(n):
  age,name = input().split()
  user.append([int(age),name])

for sortUser in sorted(user,key=lambda x : x[0]):
    print(*sortUser)