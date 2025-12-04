weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
print(weekdays)
print(weekdays[0])
print(weekdays[1])
print(weekdays[4])
print(weekdays[-1])
# print(weekdays[7]) # IndexError: list index out of range

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days[0] = 'Funday'
print(days)

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(days[0])
del days[0]
print(days)