# The variable index stores an integer representing the position of a letter in the alphabet, where index 0 corresponds to a, index 1 is b, and so on.

# Which of the following provides the letter at the opposite end of the alphabet, i.e. a -> z, b -> y, c -> x, ..., z -> a?

# a. ascii_lowercase[index-25]
# b. ascii_lowercase[26-index]
# c. ascii_lowercase[index]
# d. ascii_lowercase[25-index] # Correct


from string import ascii_lowercase

character = 'c'
index = ascii_lowercase.index(character)

print(ascii_lowercase[25 - index])