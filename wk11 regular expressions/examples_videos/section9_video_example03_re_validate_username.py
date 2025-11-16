# Program to validate a Debian Username
# Regular Expression: ^[a-z][-a-z0-9_]*$
import re

# input the username
username = input("Enter the username: ")

# apply the regex to the username string
match = re.fullmatch("[a-z][-a-z\d_]*", username)

# check if they match
if match:
    print("Valid username")
else:
    print("Not a valid username")

