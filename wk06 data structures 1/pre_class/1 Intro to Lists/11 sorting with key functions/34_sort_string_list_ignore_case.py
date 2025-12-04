# Example: Sort a list of strings ignoring case
users = ['root', 'apache', 'mysql', 'Jbloggs']
users.sort()
print(f"{users=}")

users = ['root', 'apache', 'mysql', 'Jbloggs']
users.sort(key=str.lower)
print(f"{users=}")