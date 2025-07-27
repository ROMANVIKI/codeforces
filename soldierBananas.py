k, n, w = input().split(" ")
k = int(k)
n = int(n)
w = int(w)
curr_count = 0
for i in range(1, w + 1):
    curr_count += i * k
if curr_count > n:
    print(curr_count - n)
else:
    print(0)
