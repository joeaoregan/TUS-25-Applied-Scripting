
# Indexing, slicing and searching

days_tuple = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Fri', 'Sat', 'Sun')
print(days_tuple[5])

days_tuple = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Fri', 'Sat', 'Sun')
# days_tuple[0] = "Funday" # TypeError: 'tuple' object does not support item assignment

# Slicing
weekdays = days_tuple[:5]
print(weekdays)

weekend = days_tuple[-2:]
print(weekend)

# Slice to change values
days_tuple = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Fri', 'Sat', 'Sun')
days_tuple = days_tuple[:2] + ("Meh-day",) + days_tuple[3:]
print(days_tuple)

# .count(value)
scores = (3,2,1,5,3,5)
print(scores.count(5))

# .index(value)
print(scores.index(5))
