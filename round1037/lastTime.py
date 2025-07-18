def lastTime(arr, coin_count):
    for c in arr:
        print(c)


no_inp = int(input())
for _ in range(no_inp):
    n_casinos, coin_count = map(int, input().split())
    arr = []
    for _ in range(n_casinos):
        arr.append(list(map(int, input().split())))
    print(lastTime(arr, coin_count))
