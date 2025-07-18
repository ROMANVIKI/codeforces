def onlyOneDigit(num):
    x_str = str(num)
    if len(x_str) == 1:
        return num
    else:
        y = 10
        for x in x_str:
            if int(x) < y:
                y = int(x)
    return y


n = int(input())
for _ in range(n):
    num = int(input())
    print(onlyOneDigit(num))
