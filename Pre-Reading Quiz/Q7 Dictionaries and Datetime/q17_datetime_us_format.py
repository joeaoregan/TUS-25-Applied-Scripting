# Question 17
# Which of the following is the correct code to generate a datetime object from the string "3/17/2026" which represents a date in US format?

import datetime

print(datetime.datetime.strptime("3/17/2026", "%m/%d/%Y")) # correct output: 2026-03-17 00:00:00
# print(datetime.datetime.fromisoformat("3/17/2026")) # ValueError: Invalid isoformat string: '3/17/2026'
# print(datetime.datetime.strptime("3/17/2026", "%d/%m/%Y")) # ValueError: time data '3/17/2026' does not match format '%d/%m/%Y'
# print(datetime.datetime.fromisoformat("17/3/2026")) # ValueError: Invalid isoformat string: '17/3/2026'