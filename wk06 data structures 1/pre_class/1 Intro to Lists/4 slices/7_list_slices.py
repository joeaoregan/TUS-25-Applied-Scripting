# List slices

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fr', 'Sat', 'Sun']
weekdays = days[:5]
print(weekdays)

weekend = days[-2:]
print(weekend)

print(days[:])


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fr', 'Sat', 'Sun']
print(days[::2])
print(days[1::2])

print(days[::-1])