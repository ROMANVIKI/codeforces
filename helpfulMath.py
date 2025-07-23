user_in = input().split("+")
if len(user_in) == 1:
    print(user_in[0])
else:
    user_in.sort()
    fin_str = ""
    for i in range(len(user_in)):
        if i < len(user_in) - 1:
            fin_str += f"{user_in[i]}+"
        else:
            fin_str += f"{user_in[i]}"
    print(fin_str)
