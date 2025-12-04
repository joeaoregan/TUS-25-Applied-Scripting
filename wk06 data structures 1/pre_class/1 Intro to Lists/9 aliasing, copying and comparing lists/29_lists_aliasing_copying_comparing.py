# Aliasing, Copying and Comparing Lists

total = 10
point = total
print(f"{total=} {point=}")
total += 1
print(f"{total=} {point=}")

# aliasing
users = ['root', 'apache', 'mysql', 'jbloggs']
accounts = users
print(users)
print(accounts)
print(accounts is users)
users[3] = "jdoe"
print(users)
print(accounts)

# .copy()
users = ['root', 'apache', 'mysql', 'jbloggs']
accounts = users.copy()
print(accounts is users)

# slice [:]
users = ['root', 'apache', 'mysql', 'jbloggs']
accounts = users[:]
print(accounts is users)

users[3] = "jdoe"
print(users)
print(accounts)



users = ['root', 'apache', 'mysql', 'jbloggs']
accounts = users.copy()
print(accounts is users, accounts == users)

users[3] = "jdoe"
print(accounts is users, accounts == users)


# multiple assignment
count = total = 0
print(f"{count=} {total=}")
count += 1
print(f"{count=} {total=}")


# multiple assignment - lists
users = accounts = []
print(users)
print(accounts)

users.append("root")
print(users)
print(accounts)