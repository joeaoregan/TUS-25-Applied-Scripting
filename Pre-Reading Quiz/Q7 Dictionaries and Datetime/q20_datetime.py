# Question 20
# Starting with a datetime object representing midnight on New Year's Eve 2025 
# (the start of the 2026 new year, i.e. 00:00 on New Year's Day), what datetime object will result in adding on 1 week, 2 days, 3 hours, 4 minutes and 5 seconds?

import datetime

start_datetime = datetime.datetime(2026, 1, 1, 0, 0, 0) 
time_delta = datetime.timedelta(weeks=1, days=2, hours=3, minutes=4, seconds=5)
print(start_datetime)  # 
print(time_delta)  # Output: 9 days, 3:04:05

print("start time + time difference:",start_datetime + time_delta)  # Output: 2026-01-10 03:04:05


print(datetime.datetime(2026, 1, 10, 3, 4, 5))

print(datetime.datetime(2026, 1, 10, 5, 4, 3))

print(datetime.datetime(2026, 1, 1, 0, 5, 2, 4003))

print(datetime.datetime(2026, 1, 9, 3, 4, 5))