no_test_cases = int(input())
user_str = input()

count_danik = 0
count_anton = 0
for ch in user_str:
    if ch == "A":
        count_anton += 1
    else:
        count_danik += 1
if count_danik > count_anton:
    print("Danik")
elif count_anton > count_danik:
    print("Anton")
else:
    print("Friendship")
