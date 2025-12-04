# P30 - Merging Dictionaries

contacts1 = {'Ailbhe': '0861234567', 'Bláthnaid': '0879876543'}
contacts2 = {'Conor': '0855554321', 'Bláthnaid': '0871112222'}
# Combine the two dictionaries into a single one
merged = contacts1 | contacts2
print(f"{merged=}")

# Keys in the right-hand dictionary overwrite keys from the left-hand dictionary if there is a conflict, for 
# example, Bláthnaid’s phone number in this case: the merged dictionary uses the phone number from contacts2.


# You can also use |= to update a dictionary in place:
contacts1 = {'Ailbhe': '0861234567', 'Bláthnaid': '0879876543'}
contacts2 = {'Conor': '0855554321', 'Bláthnaid': '0871112222'}
# update the first dictionary with the contents of the second
contacts1 |= contacts2
print(f"{contacts1=}")