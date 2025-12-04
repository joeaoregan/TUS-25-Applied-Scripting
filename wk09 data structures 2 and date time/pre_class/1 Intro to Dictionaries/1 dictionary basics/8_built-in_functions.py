# P8 - Build-in Functions and Dictionaries

# len() - returns the number of items (key-value pairs)

contacts = { 'Ailbhe': '0861234567', 'Bláthnaid': '0879876543', 'Conor': '0855554321' }
print(len(contacts)) # 3


# sorted() - returns a sorted list of keys
contacts = {'Emergancy': '112', 'Ailbhe': '0861234567', 'Bláthnaid': '0879876543'}
print(sorted(contacts)) # ['Ailbhe', 'Bláthnaid', 'Emergancy']

# It doesn’t affect the existing order of the keys in the dictionary, which remain in the order they were inserted:
print(contacts)

# As with lists, sorted() accepts the optional reverse= keyword argument. 
# When set to True, it returns the keys in reverse order:
print(sorted(contacts,reverse=True)) # ['Emergancy', 'Bláthnaid', 'Ailbhe']


# min() / max() - return the "smallest" / "largest" key
print(min(contacts)) # Ailbhe
print(max(contacts)) # Emergancy

# For numeric keys, the order is numerical:
ports = {80: 'HTTP', 22: 'SSH', 443: 'HTTPS'}
print(min(ports)) # 22
print(max(ports)) # 443