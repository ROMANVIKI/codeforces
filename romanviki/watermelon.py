def watermelon(n):
    n = n - 2
    if n != 0 and n % 2 == 0:
        return "YES"
    return "NO"


n = int(input())
print(watermelon(n))
