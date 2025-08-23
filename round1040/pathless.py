no_inps = int(input())


def main(n, s, a):
    return a, s, n


for _ in range(no_inps):
    n, s = input().strip().split()
    a = list(map(int, input().strip().split()))
    print(main(n, s, a))
