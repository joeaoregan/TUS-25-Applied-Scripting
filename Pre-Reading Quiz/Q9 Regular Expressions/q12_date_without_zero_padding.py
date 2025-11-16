# Q12
# What is the correct regex to represent a date in the format dd/mm/yyyy, 
# without zero-padding, e.g. 19/11/2021 or 8/1/2022?
import re

# a.
# regex = "^\d{,2}/\d{,2}/\d{4}$" # allows putting no day or month
# b.
# regex = "^\d{2}/\d{2}/\d{4}$" # no, must be 2 digit day/month
# c.
# regex = "^\d{1,2}/\d{1,2}/\d{1,4}$" # year?
# d.
regex = "^\d{1,2}/\d{1,2}/\d{4}$" # ok


def check_date(date):
    match = re.fullmatch(regex, date) # must start with lowercase letter, 4 or more characters

    # check if they match
    if match:
        print("Valid date")
    else:
        print("Not a valid date")

# OK
print("yes:")
check_date("19/11/2021")
check_date("8/1/2022")

# # Not OK
print("no:")
# padding
check_date(" 19/11/2021")
check_date("19/11/2021 ")
# year
check_date("19/11/20")
check_date("19/11/202")
# month
check_date("19/111/2021")
check_date("19//2021")
# day
check_date("119/11/2021")
check_date("/11/2021")
