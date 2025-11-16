# Q8
# Which of the following is the correct regex to represent a decimal number, 
# where no unnecessary zeros are displayed to the right of the decimal point, e.g. 6.25 or 3?
import re

# a.
# regex = "^\d+\.\d+?$" # definite no
# b.
# regex = "^\d+(\.\d+)*$" # no allows 2 decimal places
# c.
# regex = "^\d+(\.\d+)$" # definite no
# d.
regex = "^\d+(\.\d+)?$" # 


def check_decimal(decimal):
    match = re.fullmatch(regex, decimal) # must start with lowercase letter, 4 or more characters

    # check if they match
    if match:
        print("Valid decimal")
    else:
        print("Not a valid decimal")

# OK
print("yes:")
check_decimal("6.25")
check_decimal("3")
check_decimal("1.2")
# Maybe OK
print("maybe:")
check_decimal("3.0")
check_decimal("3.00")
check_decimal("3.10")
# Not OK
print("no:")
check_decimal(".12")
check_decimal("12.")
check_decimal("")
check_decimal("3?3")
check_decimal("3.2.1")