# Summer 24/25: Question 2
# The Vigenère Cipher is a polyalphabetic substitution cipher where each letter of the plaintext is encoded 
# with a different Caesar Cipher.  
# You may only import ascii_uppercase from the string module and nothing else.


# Q2(a) [7 Marks]

# The Vigenère Cipher uses a table which consists of the alphabet written out 26 times, with each alphabet 
# shifted cyclically to the left compared to the previous alphabet, corresponding to the 26 possible Caesar 
# Ciphers.  See Figure 2.1.
#  Write a function that generates a Vigenère Table and returns it as a dictionary of strings, as follows:
#  • Create an empty dictionary
#  • For each index i from 0 to 25
#  ◦ Create a shifted alphabet consisting of 
# ▪ a slice of the uppercase alphabet from index i to the end, 
# ▪ joined with a slice of the uppercase alphabet from the beginning to index i
#  ◦ Insert into the dictionary a key-value pair consisting of the uppercase letter at index i and the 
# shifted alphabet
#  • Return the dictionary

from string import ascii_uppercase

dict = {}

# for i in range (0, 26):
#     dict[ascii_uppercase[i]] = ascii_uppercase[i:len(ascii_uppercase)] + ascii_uppercase[:i]

# # print(type(ascii_uppercase[:0]))

# for line in dict:
#     print(line,dict[line])

# print(dict)

def generate_vigenere_table():
    for i in range (0, 26):
        shifted_alphabet = ascii_uppercase[i:len(ascii_uppercase)] + ascii_uppercase[:i]
        dict[ascii_uppercase[i]] = shifted_alphabet

    return dict

# for line in generate_vigenere_table():
#     print(line, dict[line])


#  Q 2(b) [6 Marks]

# When encrypting a plaintext message, the alphabet used at each point depends on a key sequence which 
# is based on a chosen keyword repeated until it matches the length of the plaintext.  See Figure 2.3.
#  Write a Python function which takes two string parameters, representing a plaintext message and a 
# keyword, and generates and returns a string representing the key sequence, as follows:
#  • Convert the keyword to uppercase
#  • Calculate the number of repeats as the integer part of the plaintext length divided by the keyword 
# length
#  • Calculate the number of letters remaining as the plaintext length modulo the keyword length
#  • Generate the key sequence as the keyword repeated and an appropriate slice of the keyword to fill 
# the remaining characters

def create_key_sequence(plaintext, keyword):
    keyword = str(keyword).upper()
    # print(keyword) # PEACE
    number_of_repeats = len(plaintext) // len(keyword)
    # print(number_of_repeats) # 3
    number_of_letters_remaining = len(plaintext) % len(keyword)
    # print(number_of_letters_remaining) # 1
    key_sequence = (keyword * number_of_repeats) + (keyword[:number_of_letters_remaining])
    # print(len(key_sequence)) # 16
    # print(key_sequence) # PEACEPEACEPEACEP
    return(key_sequence)


# print(key_sequence("LoveConquersHate", "PEACE")) # PEACEPEACEPEACEP


# Q 2(c) [7 Marks]

#  Write a Python function which takes three parameters representing a plaintext message, a key sequence, 
# and the dictionary containing the Vigenère Table, enciphers the plaintext and returns the resulting 
# ciphertext message, as follows: See Figure 2.4.
#  • Create an empty string representing the ciphertext and convert the plaintext to uppercase
#  • For each index i in the length of the plaintext 
# ◦ Get the letter at index i of the plaintext
#  ◦ Get the position of the current letter in the uppercase alphabet
#  ◦ Get the table row (alphabet string) from the Vigenère Table corresponding to the letter at 
# index i of the key sequence
#  ◦ Get the corresponding letter in the table row and add it on to the ciphertext
#  • Return the ciphertext

dict = generate_vigenere_table()
key_sequence = create_key_sequence("LoveConquersHate", "PEACE")

def create_ciphertext(plaintext, key_sequence, dict):
    # print(dict)
    ciphertext = ""
    plaintext = str(plaintext).upper()
    # print(plaintext) # LOVECONQUERSHATE
    for i in range(len(plaintext)):
        letter = plaintext[i]
        # print(letter)
        position = ascii_uppercase.index(letter)
        # print(letter, position) # L 11
        # letter2 = key_sequence[i]
        # print(letter, position, letter2) # L 11 P
        table_row = dict[key_sequence[i]]
        # print(table_row)
        enciphered_letter = table_row[position]
        # print(enciphered_letter)
        ciphertext += enciphered_letter

    return ciphertext

print(create_ciphertext("LoveConquersHate", key_sequence, dict))
