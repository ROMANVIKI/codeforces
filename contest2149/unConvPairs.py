def func(n, arr):
    arr.sort()
    max = -1
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return abs(arr[0] - arr[1])
    else:
        i, j = 0, 1

        while i < len(arr) + 1:
            try:
                if arr[j] - arr[i] > max:
                    max = arr[j] - arr[i]
                    i += 2
                    j += 2
                else:
                    i += 2
                    j += 2
            except IndexError:
                break
        return max


no_test_cases = int(input())
for i in range(no_test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    print(func(n, arr))
