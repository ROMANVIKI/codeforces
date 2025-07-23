t = int(input())
for _ in range(t):
    n = int(input())
    zero_deficit = 0
    one_deficit = 0
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        zero_deficit += max(0, c - a)
        one_deficit += max(0, d - b)
    print(max(zero_deficit, one_deficit))
