# Example Programs: Username Validation with and / or

# Version 1: Using and

username = input("Enter username: ")

if len(username) <= 15 and username.islower():
    print("Username is acceptable")
else:
    print("Username does not meet requirements")
