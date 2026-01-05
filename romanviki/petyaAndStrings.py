def petyaAndStrings(str1, str2):
    str1_dict = {}
    str2_dict = {}
    for x in str1:
        x = x.lower()
        if x in str1_dict:
            str1_dict[x] += 1
        else:
            str1_dict[x] = 1
    for y in str2:
        y = y.lower()
        if y in str2_dict:
            str2_dict[y] += 1
        else:
            str2_dict[y] = 1

    if len(str1_dict) > len(str2_dict):
        return 1
    elif len(str2_dict) > len(str1_dict):
        return -1
    else:
        return 0


str1 = input()
str2 = input()
print(petyaAndStrings(str1, str2))
