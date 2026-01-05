n, k = map(int, input().strip().split())
score_list = list(map(int, input().strip().split()))
max_val = score_list[k - 1]
total = 0
for x in score_list:
    if x >= max_val and x > 0:
        total += 1
print(total)
