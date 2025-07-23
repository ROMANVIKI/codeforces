str_lst = []
for _ in range(2):
    inp = input()
    str_lst.append(inp)


def petyaFunc(str_lst):
    str1 = str_lst[0].lower()
    str2 = str_lst[1].lower()
    if str1 > str2:
        print(1)
    elif str1 < str2:
        print(-1)
    else:
        print(0)


petyaFunc(str_lst)
