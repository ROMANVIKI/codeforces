n = 5
l, m = 2, 2
j, k = 0, 0
for i in range(n):
    cur_arr = list(map(int, input().strip().split()))
    c = 0
    while c <= 4:
        if cur_arr[c] == 1:
            j, k = i, c
            break
        else:
            c += 1

print(abs(l - j) + abs(m - k))
