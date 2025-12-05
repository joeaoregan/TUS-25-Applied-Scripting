from string import ascii_lowercase
from q2a import create_cipher_key

def albert_cipher(cipher1, cipher2, plaintext):
    ciphertext = ""
    for i, char in enumerate(plaintext.lower()):
        if char in ascii_lowercase:
            if i % 2 == 0:
                ciphertext += cipher1[char]
            else:
                ciphertext += cipher2[char]
    return ciphertext


if __name__  == "__main__":
    cipher1 = create_cipher_key()
    cipher2 = create_cipher_key()
    plaintext = input("Enter the message to encipher: ")
    print(f"Ciphertext: {albert_cipher(cipher1, cipher2, plaintext)}")
