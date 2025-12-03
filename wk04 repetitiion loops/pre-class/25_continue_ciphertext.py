# Simple substitution cipher
from string import ascii_lowercase

plaintext = input("Enter the message to be enciphered: ")

ciphertext = ""

for character in plaintext.lower():
    if not character.isalpha():
        continue
    else:
        index = ascii_lowercase.index(character)
        ciphertext += str(index) + " "

print(f"The ciphertext is: {ciphertext}")
