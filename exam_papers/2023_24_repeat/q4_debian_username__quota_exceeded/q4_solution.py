import re

while True:
    username = input("Enter a username or q to quit: ")

    if username == "q":
        break

    match = re.fullmatch(r"[a-z][-a-z0-9_]*", username)

    if match:
        print("Valid username")
    else:
        print("Invalid username")