n = int(input())
# x = 0
# for i in range(1, n + 1):
#     if i == 1:
#         x += -1
#     elif i % 2 == 0:
#         x += i
#     else:
#         x += -1 * i
# print(x)

if n % 2 == 0:
    n = round(n / 2)
    print(n)
else:
    n = (n + 1) / 2 * (-1)
    print(round(n))
