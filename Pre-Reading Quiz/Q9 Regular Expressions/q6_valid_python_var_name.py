# Q6
# A variable name in Python can only consist of letters, numbers and underscores 
# and cannot start with a number. What is the correct regex to represent this?
import re

# a.
# regex = "^\w\w\*$" # 
# b.
regex = "^[a-zA-Z_][a-zA-Z0-9_]*$" # This
# c.
# regex = "^[0-9][a-zA-Z0-9_]*$" # Valid variable name
# d.
# regex = "^[^0-9][a-zA-Z0-9_]*$" # Allows anything except number at start


var_name = "abc" 


match = re.fullmatch(regex, var_name) # must start with lowercase letter, 4 or more characters

# check if they match
if match:
    print("Valid variable name")
else:
    print("Not a valid variable name")
