# Program to check if an AIT Student ID is valid
# Example of Regular Expressions
import re

# input the username
student_id = input("Enter Student ID: ")

# compare the regex to the string
match = re.fullmatch("[A][0-9]{8}", student_id)

# check it there's a match
if match: # match object not None -> the regex and string match
	print("Valid AIT Student ID")
else:
	print("Not a valid AIT Student ID")










