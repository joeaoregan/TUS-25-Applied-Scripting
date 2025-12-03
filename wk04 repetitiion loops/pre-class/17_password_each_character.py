# Example Program: Validate Password using a for loop

password = input("Enter password: ")

lowercase = uppercase = digit = special = False

for character in password:
    if character.islower():
        lowercase = True
    elif character.isupper():
        uppercase = True
    elif character.isdigit():
        digit = True
    elif not character.isalnum():
        special = True

    if lowercase and uppercase and digit and special:
        print("Valid password.")
        break
else:
    print("Invalid password.")
    print("Include upper and lowercase letters, digits and special characters.")
