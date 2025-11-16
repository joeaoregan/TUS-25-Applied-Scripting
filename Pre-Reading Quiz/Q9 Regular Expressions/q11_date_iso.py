# Q11
# What is the following is the correct regex to represent a date in ISO format yyyy-mm-dd 
# with zero-padding, 2021-22-19 or 2022-01-08?
import re
import datetime

# a.
# regex = "^\d+-\d+-\d+$" # no 
# b.
# regex = "^\d-\d-\d$" # no
# c.
# regex = "^\d*-\d*-\d*$" # no 
# d.
regex = "^\d{4}-\d{2}-\d{2}$" # ok


def check_date(date):
    match = re.fullmatch(regex, date) # must start with lowercase letter, 4 or more characters

    # check if they match
    if match:
        print("Valid date")
    else:
        print("Not a valid date")

# OK
print("yes:")
check_date("2021-22-19")
check_date("2022-01-08")

# # Not OK
print("no:")
# padding
check_date(" 2021-22-19")
check_date("2021-22-19 ")
# year
check_date("21-22-19")
check_date("202-22-19")
# month
check_date("2021-2-19")
check_date("2021-222-19")
# day
check_date("2021-22-1")
check_date("2021-22-101")
