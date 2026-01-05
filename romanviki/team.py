def code(arr):
    return sum(arr) >= 2


n = int(input())
res = 0
for i in range(n):
    arr = list(map(int, input().strip().split()))
    if code(arr):
        res += 1
print(res)
