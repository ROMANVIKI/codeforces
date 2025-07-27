user_inp = input()

len_str = len(user_inp)
count_uppercase_char = 0
for char in user_inp:
    if char.isupper():
        count_uppercase_char += 1

lower_case_count = len_str - count_uppercase_char
if lower_case_count > count_uppercase_char or lower_case_count == count_uppercase_char:
    print(user_inp.lower())
else:
    print(user_inp.upper())
