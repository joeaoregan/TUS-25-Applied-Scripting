
# Version 2: Using or

username = input("Enter username: ")

if len(username) > 15 or not username.islower():
    print("Username does not meet requirements")
else:
    print("Username is acceptable")