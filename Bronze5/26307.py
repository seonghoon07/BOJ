h,m = map(int, input().split())
start_time = 9

d_h = h - start_time
d_m = 60*d_h + m
print(d_m)