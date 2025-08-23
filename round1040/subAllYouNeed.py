def subFunc(n, arr):
    count = 0
    for num in arr:
        if num > 0:
            count += num
        elif num == 0:
            count += 1
    return count


no_inps = int(input())
for _ in range(no_inps):
    n = int(input())
    arr = list(map(int, input().split()))
    print(subFunc(n, arr))
