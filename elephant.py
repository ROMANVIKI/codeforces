user_inp = int(input())
int_val = user_inp // 5

if int_val * 5 == user_inp:
    print(int_val)


else:
    rem = user_inp % 5
    if rem >= 1 and rem <= 5:
        int_val += 1
    print(int_val)
