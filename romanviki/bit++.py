n = int(input())
total = 0
for i in range(n):
    s = input()
    if s[0] == "-" or s[-1] == "-":
        total -= 1
    else:
        total += 1
print(total)
