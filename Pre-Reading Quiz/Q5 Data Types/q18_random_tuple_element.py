# The variable vowels contains a tuple of single characters ("a", "e", "i", "o", "u").
# Assume that the module random has been imported.
# Which of the following is valid code to use with the vowels tuple?

import random

vowels = ("a", "e", "i", "o", "u")

# a.
print(random.choice(vowels)) # OK

# b.
# print(vowels.sort()) # AttributeError: 'tuple' object has no attribute 'sort'

# c.
# print(random.shuffle(vowels)) # TypeError: 'tuple' object does not support item assignment

# d.
# print(vowels.reverse()) # AttributeError: 'tuple' object has no attribute 'reverse'