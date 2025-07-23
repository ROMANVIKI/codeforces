username = input()


unq_username = set(username)

if len(unq_username) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
