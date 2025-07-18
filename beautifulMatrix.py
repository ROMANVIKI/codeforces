n = 5
arrs = []
for _ in range(n):
    arrs.append(list(map(int, input().split())))


target_ind = [2, 2]
row = 0
col = 0
found = False
sol = 0

while row < n:
    for c in range(n):
        if arrs[row][c] == 1:
            col = c
            found = True
            break
    if found:
        break
    row += 1

print(abs(target_ind[0] - row) + abs(target_ind[1] - col))
