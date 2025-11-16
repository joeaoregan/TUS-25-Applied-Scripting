# Alternation with |

# The following regex does a better job:
# [0-9]{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])

# YYYY  is the same as before [0-9]{4}
# MM    is (0[1-9]|1[012])
# DD    is (0[1-9]|[12][0-9]|3[01])

# The meta-character | represents alternation, 
# which means one or the other, e.g. a|b means a or b.

# So the regex for the month in the format MM: 0[1-9] | 1[012]
# means 01, 02, 03, 04, 05, 06, 07, 08, 09 OR 10, 11, 12
#        0 followed by a number from 1-9
# OR  1 followed by one of the numbers 0, 1, 2
# The round brackets () are used to group blocks of regex together, 
# to specify the alternate options.
# [0-9]{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])

# Similary, the regex for the day in the format DD: (0[1-9]|[12][0-9]|3[01])
# 01, 02, 03, 04, 05, 06, 07, 08, 09 
# OR
# 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29
# OR
# 30, 31
# which means 0 followed by a number from 1-9
# OR 1 or 2 followed by a digit (0-9)
# OR 3 followed by 0 or 1

# This isn’t a perfect way to validate a date, 
# as it will still match invalid dates such as 2020-02-31.
import re

def check_date_alternate(date):
    match = re.fullmatch("[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])", date)

    if match:
        print("Valid date")
    else:
        print("Invalid date")

        
check_date_alternate("2020-03-05") # Valid date
check_date_alternate("2020-99-99") # Invalid date
