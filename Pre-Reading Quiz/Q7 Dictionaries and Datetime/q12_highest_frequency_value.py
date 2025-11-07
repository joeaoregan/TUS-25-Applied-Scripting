# Question 12
# For the letter_frequencies dictionary, which of the following correctly provides the highest frequency (the highest vaue)?

from string import ascii_lowercase
text = "The quick brown fox jumps over a lazy dog"

letter_frequencies = { character : text.lower().count(character) for character in ascii_lowercase } # Correct
print(letter_frequencies)

print(max(letter_frequencies.keys())) # incorrect
print(max(letter_frequencies,key=letter_frequencies.get)) # correct
print(max(letter_frequencies.values())) # correct
print(max(letter_frequencies)) # incorrect


