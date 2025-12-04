# P6 - Another way: get() method

contacts = { 'Ailbhe': '0861234567', 'Bláthnaid': '0879876543', 'Conor': '0855554321' }
print(contacts.get('Ailbhe')) # 0861234567

# If the dictionary key does not exist, .get(key) returns None by default:
print(contacts.get('Deirdre')) # None

# You can specify a default value to return instead, if the key is not in the dictionary. The syntax is:
print(contacts.get('Deirdre', "Not in contacts")) # Provide a default value for when none returned