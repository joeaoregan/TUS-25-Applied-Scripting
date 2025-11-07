# Question 19
# Which of the following is not the correct time difference between 9am on Monday 3rd November 2025 and 11.59pm on New Year's Eve 2025?
# Hint: Create two datetime objects and subtract them; this results in a timedelta object.

import datetime
start_datetime = datetime.datetime(2025, 11, 3, 9, 0, 0)
end_datetime = datetime.datetime(2025, 12, 31, 23, 59, 0)
time_difference = end_datetime - start_datetime

print(time_difference)  # Output: 58 days, 14:59:00
print(time_difference.days)  # Output: 58

print(type(time_difference))