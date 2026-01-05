def main(n, a):
    smash = 0
    min_val = min(a)
    fin_arr = [min_val] * n
    count =0
    i = 0
    while a != fin_arr:
        

    return fin_arr, min_val


# no_test_cases = int(input())
# for _ in range(no_test_cases):
#     n = int(input())
#     a = list(map(int, input().split()))
#     print(main(n, a))

print(main(n=9, a=[9, 9, 3, 2, 4, 4, 8, 5, 3]))
