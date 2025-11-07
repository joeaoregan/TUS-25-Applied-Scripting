# Question 18
# A log file records the date and time of a log entry as "Fri Nov 07 14:32:57 GMT 2025".

# Which of the following is the correct format string to allow a datetime object to be generated from it?

# Hint: To try this in the interactive interpreter, import the datetime module and create a date object as follows:
# import datetime
# end_date = datetime.datetime.strptime("Fri Nov 07 14:32:57 GMT 2025", format_string)
# where you replace
# format_string
# with one of the possible ans

import datetime

# format_string = "%A %B %d %H:%M:%S %Z %Y" # ValueError: time data 'Fri Nov 07 14:32:57 GMT 2025' does not match format '%A %B %d %H:%M:%S %Z %Y'

# format_string = "%a %b %d %H:%M:%S %z %Y"  # ValueError: time data 'Fri Nov 07 14:32:57 GMT 2025' does not match format '%a %b %d %H:%M:%S %z %Y'

# format_string = "%a %b %D %H:%M:%S %Z %Y" # ValueError: 'D' is a bad directive in format '%a %b %D %H:%M:%S %Z %Y'

format_string = "%a %b %d %H:%M:%S %Z %Y"
enddate = datetime.datetime.strptime("Fri Nov 07 14:32:57 GMT 2025", format_string)
print(enddate)  # correct output: 2025-11-07 14:32:57