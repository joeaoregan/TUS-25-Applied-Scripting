def is_valid_username(name):
    if len(name) >= 5 and name.isalnum() and name[0].isalpha():
        return True
    return False

while True:
    name = input("Enter a username: ")
    if is_valid_username(name):
        print("Username accepted")
        break
    else:
        print("Invalid username, try again")