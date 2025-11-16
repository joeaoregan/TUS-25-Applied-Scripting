# Q2
# The regex ^[a-z][-a-z0-9_]*$ represents valid usernames in Debian.

# Which of the following will not match the regex?
import re

# username = "groot-1-am" # Valid username
# username = "i_am_3rd_groot" # Valid username
# username = "i" # Valid username
username = "i_am_groot." # Not a valid username

# regex = "^[a-z][-a-z0-9_]*$"
regex = "[a-z][-a-z0-9_]*"

match = re.fullmatch(regex, username) # must start with lowercase letter, 4 or more characters

# check if they match
if match:
    print("Valid username")
else:
    print("Not a valid username")
