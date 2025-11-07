# Question 13
# For the letter_frequencies dictionary, which of the following correctly provides the most frequent letter (the letter with highest frequency)?

from string import ascii_lowercase
text = "The quick brown fox jumps over a lazy dog"

letter_frequencies = { character : text.lower().count(character) for character in ascii_lowercase } # Correct
print(letter_frequencies)

print(max(letter_frequencies.values()))
print(max(letter_frequencies))
print(max(letter_frequencies,key=letter_frequencies.get))
print(max(letter_frequencies.keys()))


