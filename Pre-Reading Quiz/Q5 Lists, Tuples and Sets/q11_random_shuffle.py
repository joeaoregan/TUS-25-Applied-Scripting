# The shuffle method from the module random can randomly shuffle the order of the items in a sequence.
# Assuming that shuffle has been imported from random, what is the correct code to randomly shuffle the all_numbers list?

from random import shuffle

all_numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# a.
# all_numbers.shuffle() # AttributeError: 'list' object has no attribute 'shuffle'

# b.
# all_numbers(shuffle) # TypeError: 'list' object is not callable

# c.
shuffle(all_numbers) # this

# d.
# shuffle.all_numbers() # AttributeError: 'function' object has no attribute 'all_numbers'

print(all_numbers)