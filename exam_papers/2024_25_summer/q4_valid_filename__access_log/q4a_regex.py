# QUESTION 4 [TOTAL MARKS: 20]
# For this question you may assume that Python's re (regular expression) module has been imported.  You 
# may not import anything else.

# Q 4(a) [4 Marks]
# A web developer uses the following filename convention: x.y
# where x consists of letters, numbers, underscores and hypens (dashes) 
#       y consists only of letters, with a maximum of 4 permitted.

# Write a Python program which repeatedly inputs filenames and uses a regular expression to determine 
# and display whether or not it is valid according to the above convention. 

import re

regex = r"\w+\.\w{1,4}"

def check_filename(filename):
    if re.fullmatch(regex, filename):
        return("Valid Filename")
    return("Not a valid Filename")

while True:
    filename = input("Enter the filename or q to quit: ")

    if filename == "q":
        break

    print(check_filename(filename))

