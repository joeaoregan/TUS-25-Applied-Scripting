# Program to check if a username is valid
# Example of Regular Expressions
import re

# input the username
username = input("Enter username: ")

# compare the regex to the string
match = re.fullmatch("[a-z][-a-z0-9_]*", username)

# check it there's a match
if match: # match object not None -> the regex and string match
	print("Username is valid")
else:
	print("Username is not valid")










