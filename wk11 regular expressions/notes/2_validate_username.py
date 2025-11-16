# Program 2: Validate a Username
# The following program is used to validate a Debian Linux username:
# * Must start with a lowercase letter
# * Can only contain lowercase letters, numbers, underscores _ and hyphens -
# The regualar express is: ^[a-z][-a-z0-9_]*$

# Instead of specifying ^ and $ a the beginning and end of the regex,
# you use the method fullmatch, which matches the entire string:
# re.fullmatch("[a-z][-a-z0-9_]*", username)

# The fullmatch method returns a match object if the regex matches the string:
# Enter username: joe_bloggs
# <_sre.SRE_Match object; span=(0, 10), match='jobe_bloggs'>

# and return None if it doesn't match:
# Enter username: JoeBloggs
# None

# This can be used for input validation, e.g.

# Program to check if a username is valid
# Example of Regular Expressions
import re

# input the username
username = input("Enter username: ")

# compare the regex to the string
match = re.fullmatch("[a-z][-a-z0-9_]*", username)

# check if there's a match
if match: # match object not None -> the regex and string match
    print("Username is valid")
else:
    print("Username is not valid")