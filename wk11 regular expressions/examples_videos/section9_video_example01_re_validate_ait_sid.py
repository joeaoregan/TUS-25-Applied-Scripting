# Program to validate an AIT Student ID
# Regular Expression: A[0-9]{8}
import re

# Input the student ID
student_id = input("Enter the Student ID: ")

# compate the regex to the string
match = re.fullmatch("A[0-9]{8}", student_id, re.I)

# check if there was a match
if match:
    print("Valid AIT Student ID")
else:
    print("Not a valid AIT Student ID")