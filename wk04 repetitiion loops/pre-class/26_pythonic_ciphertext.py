from string import ascii_lowercase

plaintext = input("Enter the message to be enciphered: ")

ciphertext = ""

for character in plaintext.lower():
    if character.isalpha():
        index = ascii_lowercase.index(character)

        ciphertext += str(index) + " "

print(f"The ciphertext is: {ciphertext}")