from string import ascii_lowercase
from random import shuffle

def create_cipher_key():
    cipher_key = {}
    shuffled_alphabet = list(ascii_lowercase)
    shuffle(shuffled_alphabet)
    for i, letter in enumerate(ascii_lowercase):
        cipher_key[letter] = shuffled_alphabet[i]
    return cipher_key

# print(create_cipher_key())

def get_reverse_key(cipher_key):
    return {v:k for k,v in cipher_key.items()}

def encipher(cipher_key, plaintext):
    ciphertext = ""
    for i, char in enumerate(plaintext.lower()):
        if char in ascii_lowercase:
            ciphertext += cipher_key[char]
    return ciphertext

print(encipher(create_cipher_key(), "Hello World!"))