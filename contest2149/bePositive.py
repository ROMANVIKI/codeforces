def func(n, arr):
    count = 0
    arr_dict = {}
    for el in arr:
        if el in arr_dict:
            arr_dict[el] += 1
        else:
            arr_dict[el] = 1
    count += arr_dict.get(0, 0)
    if arr_dict.get(-1, 0) % 2 != 0:
        count += 2
    return count


no_test_cases = int(input())
for i in range(no_test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    print(func(n, arr))
