n, k, t = map(int, input().split())


total_fill = n * k * t // 100
result = []
for _ in range(n):
    if total_fill >= k:
        result.append(k)
        total_fill -= k
    else:
        result.append(total_fill)
        total_fill = 0

print(*result)
