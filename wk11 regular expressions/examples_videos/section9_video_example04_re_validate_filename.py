# Program to validate a filename test.txt
# Regular Expression: \w+\.\w+   \w means [0-9a-zA_Z-], + means 1 or more

import re

# Input the filename
filename = input("Enter the filename: ")

# apply the regular expression
match = re.fullmatch("\w+\.\w+", filename)

# check if there's a match
if match:
    print("Valid filename")
else:
    print("Not a valid filename")