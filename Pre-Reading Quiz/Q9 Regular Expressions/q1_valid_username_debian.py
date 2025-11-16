# Q1
# The regex ^[a-z][-a-z0-9_]*$ represents valid usernames in Debian.

# Which of the following will match the regex?
import re

username = "i_am_sparatacus" # valid
# username = "i_am_Sparatacus" # Not a valid username
# username = "i'm_sparatacus" # Not a valid username
# username = "1_spartacus_here" # Not a valid username

# regex = "^[a-z][-a-z0-9_]*$"
regex = "[a-z][-a-z0-9_]*"

match = re.fullmatch(regex, username) # must start with lowercase letter, 4 or more characters

# check if they match
if match:
    print("Valid username")
else:
    print("Not a valid username")
