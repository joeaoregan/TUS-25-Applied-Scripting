# Q7
# Which of the following is the correct regex to represent a decimal number, such as 6.25 or 3.0?
import re

# a.
# regex = "^\d+.\d+$" # 6.25, 3?3
# b.
# regex = "^\d*\.\d*$" # 6.25, .12, 12.
# c.
regex = "^\d+\.\d+$" # ok
# d.
# regex = "^\d+\.\d*$" # 6.25, 12.


def check_decimal(decimal):
    match = re.fullmatch(regex, decimal) # must start with lowercase letter, 4 or more characters

    # check if they match
    if match:
        print("Valid decimal")
    else:
        print("Not a valid decimal")

# OK
check_decimal("6.25")
check_decimal("3.0")
# Not OK
check_decimal("3")
check_decimal(".12")
check_decimal("12.")
check_decimal("")
check_decimal("3?3")