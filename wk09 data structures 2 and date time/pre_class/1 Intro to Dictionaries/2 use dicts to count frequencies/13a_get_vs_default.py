# P13 - Using .get() vs .setdefault()

# Use .setdefault() when the dictionary values are containers (like lists, sets or other dictionaries) 
# and you want to initialise them if they don’t yet exist before adding new elements.  For example:
# data_dict.setdefault(key, []).append(value)

# If the key is not already in the dictionary, .setdefault(key, []) inserts it with the empty list 
# [] as its initial value and then returns that list.  If the key already exists, it simply returns the existing 
# list, allowing you to append to it safely.

# This pattern is often used when grouping items or collecting related data, for example:

students_by_programme = {}

students_by_programme.setdefault('MSc AI', []).append('Ailbhe')
students_by_programme.setdefault('MSc AI', []).append('Conor')
students_by_programme.setdefault('MSc CNC', []).append('Bláthnaid')

print(students_by_programme)