# The choice method from the module random can randomly select an item from a sequence.
# Assuming that choice has been imported from random what is the correct code to randomly
# select a number from the all_numbers list?

from random import choice

all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# a.
print(choice(all_numbers))

# b.
# print(choice.all_numbers()) # AttributeError: 'function' object has no attribute 'all_numbers'

# c.
# print(all_numbers.choice()) # AttributeError: 'list' object has no attribute 'choice'

# d.
# print(all_numbers(choice)) # TypeError: 'list' object is not callable