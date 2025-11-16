# Q9
# Which of the following is the correct regex to represent an amount of money in US Dollars, 
# in the form $xyz.dd?
import re

# a.
# regex = "^$\d+\.\d+$" # no, not escaped
# b.
regex = "^\$\d+\.\d+$" # 
# c.
# regex = "^\$\d*\.\d*$" # allows nothing before decimal
# d.
# regex = "^$\d+.\d+$" # no, not escaped


def check_dollar(dollar):
    match = re.fullmatch(regex, dollar) # must start with lowercase letter, 4 or more characters

    # check if they match
    if match:
        print("Valid dollar")
    else:
        print("Not a valid dollar")

# OK
print("yes:")
check_dollar("$6.25")
check_dollar("$7.00")

# Maybe OK
print("maybe:")
check_dollar("$3")
check_dollar("$1.2")
check_dollar("$1.123")

# Not OK
print("no:")
check_dollar("$")
check_dollar("$.00")
check_dollar("$$6.25")

check_dollar("3.0")
check_dollar("3.00")
check_dollar("3.10")
check_dollar("")
check_dollar("3?3")
check_dollar("3.2.1")