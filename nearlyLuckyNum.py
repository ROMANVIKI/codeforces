inp = input()


# def luckyNum(inp):
#     dic = {}
#     for c in inp:
#         dic[c] = dic.get(c, 0) + 1
#     total = dic.get("4", 0) + dic.get("7", 0)
#     return "YES" if all(c in "47" for c in str(total)) else "NO"


def luckyNum(inp):
    total = inp.count("4") + inp.count("7")
    return "YES" if all(c in "47" for c in str(total)) else "NO"


print(luckyNum(inp=inp))
