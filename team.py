def isProblem(test_arr):
    count = 0
    if test_arr[0] == 1 or test_arr[-1] == 1 and test_arr[0] == 1 or test_arr[1] == 1:
        count += 1
    return count


if "__main__" == __name__:
    n_t = int(input())
    count = 0
    for _ in range(n_t):
        test_arr = list(map(int, input().split()))
        count += isProblem(test_arr)
    print(count)
