# Q13
# A Python program needs to validate user input to check if it is a 
# valid username using the regex ^[a-z][-a-z0-9_]*$

# Which of the following is the correct code to do this?
import re

regex = "^[a-z][-a-z0-9_]*$"

username = "a-az19_"

def check_username(username):
# a.
    # match = re.findall("[a-z][-a-z0-9_]*", username)
    # b.
    match = re.fullmatch("[a-z][-a-z0-9_]*", username) # this
    # c.
    # match = re.match("[a-z][-a-z0-9_]*", username)
    # d.
    # match = re.search("[a-z][-a-z0-9_]*", username)


    # check if they match
    if match:
        print("Valid username")
    else:
        print("Not a valid username")


# OK
print("yes:")
check_username("a-az19_")
# No
print("no:")
check_username("")
check_username("a-az19_'")
check_username("1abc123-_")
check_username("-1abc123-_")
check_username("_1abc123-_")
check_username("?_1abc123-_")