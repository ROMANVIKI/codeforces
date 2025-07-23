def greedyGridFunc(n, m):
    if min(n, m) <= 1 or (n == 2 and m == 2):
        return "NO"
    return "YES"


no_t = int(input())
for _ in range(no_t):
    n, m = map(int, input().split())
    print(greedyGridFunc(n, m))
