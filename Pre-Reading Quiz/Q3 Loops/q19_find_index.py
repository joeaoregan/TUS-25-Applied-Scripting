# The string ascii_lowercase contains the letters of the alphabet in lowercase, i.e. "abcdefg...xyz".

# Assuming the variable character contains a lowercase letter, the program needs to determine the position of the letter in the alphabet.

# Which of the following is not the correct statement to do this?

# a. index = ascii_lowercase.find(character)
# b. index = ascii_lowercase.index(character)
# c. index = ascii_lowercase.count(character)


from string import ascii_lowercase

character = 'e'

find = ascii_lowercase.find(character)
index = ascii_lowercase.index(character)
count = ascii_lowercase.count(character)

print(f"find: {find} index: {index} count: {count}")