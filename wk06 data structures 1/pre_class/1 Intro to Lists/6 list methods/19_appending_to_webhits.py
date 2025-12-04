# Example: Appending to the webhits list

users = ['root', 'apache', 'mysql', 'jbloggs']
users.append('nginx')
print(users)


users = ['root', 'apache', 'mysql', 'jbloggs']
users.insert(0, 'nginx')
print(users)

# .sort()
users = ['root', 'apache', 'mysql', 'jbloggs']
sorted(users)
print(users)

users.sort()
print(users)

# sorted() returns a list .sort() returns None
users = ['root', 'apache', 'mysql', 'jbloggs']
sorted_users = sorted(users)
print(f"{sorted_users=}") # sorted_users=['apache', 'jbloggs', 'mysql', 'root']

users = ['root', 'apache', 'mysql', 'jbloggs']
sorted_users = users.sort()
print(f"{sorted_users=}") # None
