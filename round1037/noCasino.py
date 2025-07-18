def noCasinoMountains(a, n, k):
    ind = 0
    count = 0
    # as we slicing the indexes in the next line we need
    while ind <= n - k:
        if all(x == 0 for x in a[ind : ind + k]):
            count += 1
            ind += k + 1
        else:
            ind += 1

    return count


num_test = int(input())
for _ in range(num_test):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(noCasinoMountains(a, n, k))
