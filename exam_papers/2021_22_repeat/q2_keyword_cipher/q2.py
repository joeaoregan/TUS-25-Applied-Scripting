# Q2a(i)
from string import ascii_lowercase

# Q2a(ii)
keyword = input("Enter the keyword: ")

unique_letters = []
for letter in keyword:
    if letter not in unique_letters:
        unique_letters.append(letter)

# 2a(iii)
cipher_alphabet = {}

for i in range(len(unique_letters)):
    cipher_alphabet[ascii_lowercase[i]] = unique_letters[i]

for i in range(len(unique_letters), len(ascii_lowercase)):
    for letter in ascii_lowercase:
        if letter not in cipher_alphabet.values():
            cipher_alphabet[ascii_lowercase[i]] = letter
            break

print(" ".join(cipher_alphabet.keys()))
print(" ".join(cipher_alphabet.values()))

# 2b(i) Prompt user
choice = input("[E]ncipher or [D]ecipher? ")

# 2b(ii) Encipher
if choice.lower()[0] == 'e':
    plaintext = input("Enter the message to encipher: ")

    ciphertext = ""
    for character in plaintext:
        if character.isalpha():
            ciphertext += cipher_alphabet[character.lower()]
        else:
            ciphertext += character

    print(f"The ciphertext is: {ciphertext}")

# 2b(iii) Decipher
if choice.lower()[0] == 'd':
    ciphertext = input("Enter the ciphertext to decipher: ")

    plaintext = ""
    for character in ciphertext:
        if character.isalpha():
            character = character.lower()
            for letter in cipher_alphabet.keys():
                if cipher_alphabet[letter] == character:
                    plaintext += letter
                    break
        else:
            plaintext += character

    print(f"The plaintext message is: {plaintext}")
