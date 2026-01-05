def aPlusBAgain(x):
    j = 0
    sum = 0
    while j <= len(x) - 1:
        sum += int(x[j])
        j += 1
    return sum


n = int(input())
for i in range(n):
    x = input()
    print(aPlugain(x))
