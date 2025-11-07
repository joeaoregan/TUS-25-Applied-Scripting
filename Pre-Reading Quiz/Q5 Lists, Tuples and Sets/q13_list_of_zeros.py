# what is the correct code to create a list frequencies containing 26 elements, 
# each of which is assigned to zero?

# a.
# frequencies = list(26) # TypeError: 'int' object is not iterable

# b.
# frequencies = [26] # [26]

# c.
# frequencies = list[26] # list[26]

# d.
frequencies = [0] * 26 # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(frequencies)
