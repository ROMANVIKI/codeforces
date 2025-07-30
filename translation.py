# x = input()
# y = input()
#
# if x == y:
#     print("NO")
# else:
#     x = "".join(sorted(x))
#     y = "".join(sorted(y))
#     if x == y:
#         print("YES")
#     else:
#         print("NO")
x = input()
y = input()

if y == x[::-1]:  # Check if y is the reverse of x
    print("YES")
else:
    print("NO")
