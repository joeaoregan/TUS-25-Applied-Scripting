# Example Program: Validate Username

username = input("Enter the username: ")

if "Admin" in username:
    print("Invalid: username must not contain Admin")
elif len(username) > 15:
    print("Invalid: exceeds 15 characters")
else:
    for char in username:
        if not char.isalpha() and not char.isdigit() and char != '_':
            print("Invalid character: ", char)
            break
    else:
        print(username, "is valid")