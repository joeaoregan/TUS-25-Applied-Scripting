# Using raw strings r"regex"
# The correct approach to avoid a SyntaxWarning now and potential syntax errors 
# in future Python versions is to use a raw string (r"...").  A raw string tells 
# the interpreter not to treat backslashes (\) as # escape characters.  
# Instead, it preserves them exactly as written and passes the string to 
# Python’s regular # expression module (re) for processing.  

# The following version of the program uses a raw string:
import re

# input the username
student_id = input("Enter Student ID: ")

# compare the regex to the string
match = re.fullmatch(r"A\d{8}", student_id, re.I) # raw string

# check if there's a match
if match: # match objecgt not None -> the regex and string match
    print("Valid AIT Student ID")
else:
    print("Not a valid AIT Studen ID")
