num = input()
str_in = input()
count = 0
for i in range(len(str_in)):
    try:
        if str_in[i] == str_in[i + 1]:
            count += 1
    except IndexError:
        pass
print(count)
