# Version 3

from string import ascii_lowercase
# Input the text and convert to lowercase
text = input("Enter the text: ").lower()
# Create a list of the frequencies of the 26 letters
letter_frequencies = [0] * 26
# Use a set to get the unique characters in the text (use set(text))
unique_characters = set(text)
# For each character in the set
for character in unique_characters:
#     If the character is a letter
    if character.isalpha():
#         Find the index of the letter in the alphabet (use ascii_lowercase.index(character))
        index = ascii_lowercase.index(character)
#         Count the number of times this letter appears in the text (use text.count(character))
        count = text.count(character)
#         Store the count in the corresponding element of the frequencies list
        letter_frequencies[index] = count
# Display the letters and their frequencies
print("\nLetter Frequency")
for letter,frequency in zip(ascii_lowercase, letter_frequencies):
    print(f"{letter:^5}{frequency:^9}")
# Determine and display the most frequent letter
most_frequent = letter_frequencies.index(max(letter_frequencies))
print(f"\nMost frequent letter: {ascii_lowercase[most_frequent]}")