# Q5
# A variable name can only consist of letters, numbers and underscores. 
# What is the correct regex to represent this?

# There are 2 correct answers, you just need to select one of them.
import re

# a.
regex = "^\w+$" # correct
# b.
# regex = "^\w*$" # allows blanks
# c.
regex = "^[a-zA-Z0-9_]+$" # correct
# d.
# regex = "^[a-zA-Z0-9_]*$" # allows blanks




# var_name = "asdf2224_344sf" # Test - Valid
# var_name = "troy'parrot"
var_name = "?"


match = re.fullmatch(regex, var_name) # must start with lowercase letter, 4 or more characters

# check if they match
if match:
    print("Valid variable name")
else:
    print("Not a valid variable name")
