n = int(input())
arr = []

for i in range(n):
  c = input()
  arr.append(c)
sorted_arr = sorted(set(arr), key=lambda x: (len(x), x)) # 길이가 같을경우 사전순
print(*sorted_arr,sep="\n")