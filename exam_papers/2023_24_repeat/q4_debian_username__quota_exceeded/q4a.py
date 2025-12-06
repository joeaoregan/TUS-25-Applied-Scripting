import re

regex = r"[a-z][a-z0-9_-]*"

while True:
    debian_id = input("Enter username or q to quit: ")
    if debian_id == 'q':
        break

    match = re.fullmatch(regex, debian_id)

    if match:
        print("Valid Debian linux id")
    else:
        print("Invalid Debian linux id")
