# Adding lists using the + Operator

# +
users = ['root', 'apache', 'mysql', 'jbloggs']
new_users = ["jdoe", "emustermann", "jjansen"]
total_users = users + new_users
print(total_users)

# +=
users = ['root', 'apache', 'mysql', 'jbloggs']
new_users = ["jdoe", "emustermann", "jjansen"]
users += new_users
print(users)

# extend()
users = ['root', 'apache', 'mysql', 'jbloggs']
new_users = ["jdoe", "emustermann", "jjansen"]
users.extend(new_users)
print(users)