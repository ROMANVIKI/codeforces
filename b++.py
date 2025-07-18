n_t = int(input())
count = 0
for _ in range(n_t):
    user_inp = str(input())
    if "+" in user_inp:
        count += 1
    elif "-" in user_inp:
        count -= 1
print(count)
