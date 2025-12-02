# Example Program: Check that all letters in the username are lowercase

username = input("Enter your username: ")

if username.islower():
    print("Username is acceptable")
else:
    print("Username contains uppercase letter(s)")