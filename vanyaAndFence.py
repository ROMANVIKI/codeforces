n, h = map(int, input().split())
arr_height = list(map(int, input().split()))

count = 0
for x in arr_height:
    if x > h:
        count += 2
    else:
        count += 1
print(count)
