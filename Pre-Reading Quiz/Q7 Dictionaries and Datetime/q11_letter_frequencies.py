# Question 11
# A string variable text contains a section of text (sentence or paragraph).

# Assuming the string variable ascii_lowercase has been imported from the string module, 
# which of the following dictionary comprehensions will create a dictionary containing 
# the frequencies of each letter in the text (ignoring case, e.g. 'T' and 't' should be  
# treated as the same letter)? (The dictionary keys are the lowercase letters, 
# the values are the frequencies of the letters).

# Hint: Try it in the interactive Python interpreter:
# from string import ascii_lowercase
# text = "The quick brown fox jumps over a lazy dog"

from string import ascii_lowercase
text = "The quick brown fox jumps over a lazy dog"

# letter_frequencies = { character : text.count(character) for character in ascii_lowercase } # Incorrect doesn't count upper case
# print(letter_frequencies)

letter_frequencies = { character : text.lower().count(character) for character in ascii_lowercase } # Correct
print(letter_frequencies)

# letter_frequencies = { character : ascii_lowercase.count(character) for character in text } # Incorrect: counts upper and lower case and non-alpha
# print(letter_frequencies)


letter_frequencies = { character : ascii_lowercase.count(character) for character in text.lower() if character.isalpha() } # Incorrect: only counts letters once
print(letter_frequencies)