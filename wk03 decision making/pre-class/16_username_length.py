# Example Program: Check length of username

username = input("Enter your username: ")
if len(username) <= 15:
    print("Username length is acceptable")
else:
    print("Username is too long")