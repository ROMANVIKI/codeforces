def nextRoundFunc(k, s):
    count = 0
    threshold = k[s - 1]
    for score in k:
        if score >= threshold and score > 0:
            count += 1
        else:
            break
    return count


n, s = map(int, input().split())
count = 0
k = list(map(int, input().split()))
print(nextRoundFunc(k, s))
