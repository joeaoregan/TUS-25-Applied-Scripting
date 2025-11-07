# ascii_lowercase is provided by the module string.
# It contains the letters of the alphabet in lowercase, "abcdefg...xyz".
# What is the correct code to find and return the index of a letter in the lowercase alphabet?

from string import ascii_lowercase

letter = 'j'

# a.
index = ascii_lowercase.find(letter) # this

# b.
# index = letter.find(ascii_lowercase) # -1

# c.
# index = ascii_lowercase.letter(find) # AttributeError: 'str' object has no attribute 'letter'. Did you mean: 'center'?

# d.
# index = find.ascii_lowercase(letter) # NameError: name 'find' is not defined

print(index)