num_test_cases = int(input())


def plusOneSubsetFunc(arr):
    return max(arr) - min(arr)


for _ in range(num_test_cases):
    num_el = int(input())

    arr = list(map(int, input().split()))
    print(plusOneSubsetFunc(arr=arr))
