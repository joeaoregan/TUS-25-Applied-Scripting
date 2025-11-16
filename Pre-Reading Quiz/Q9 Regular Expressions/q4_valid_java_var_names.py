# Q4
# The regex ^[a-zA-Z_$][a-zA-Z0-9_$]*$ represents valid variable names in Java Script.

# Which of the following will not match the regex?
import re

# regex = "^[a-zA-Z_$][a-zA-Z0-9_$]*$"
regex = "[a-zA-Z_$][a-zA-Z0-9_$]*"

# a.
# var_name = "$4ever" # Valid variable name
# b.
# var_name = "$4ever$" # Valid variable name
# c.
# var_name = "$" # Valid variable name
# d.
var_name = "4ever." # Not a valid variable name


match = re.fullmatch(regex, var_name) # must start with lowercase letter, 4 or more characters

# check if they match
if match:
    print("Valid variable name")
else:
    print("Not a valid variable name")
