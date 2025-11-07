# A substitution cipher is a simple encryption method which replaces each letter in the original message, called the plaintext, with another character in the enciphered (encrypted) message, called the ciphertext.  

# For example, the Harha Tana cipher uses reciprocal substitution between consecutive letters.

# Write and test a Python program which implements the Harha Tana cipher, as follows:

# * Input the plaintext from the user and convert it to lowercase
# * Create a variable to store the ciphertext, which should be initialised to an empty string ""
# * For each letter in the plaintext,
#   - Determine its index in the lowercase alphabet ascii_lowercase (see below)
#   - If the index is even, then add 1; if it's odd, subtract 1.
#   - Determine the letter corresponding to the new index (use ascii_lowercase) and add this letter to the ciphertext; 
#   - Any character that is not a letter should be added on to the ciphertext as it is.
# * Display the ciphertext

# Hint: Import the variable ascii_lowercase from the module string. It contains the letters of the alphabet "abcdef...xyz". To identify the index of a lowercase letter, use ascii_lowercase.index(character), assuming character is a lowercase letter.

# Only use the Python features that have been included at this point in the course.

# For example:


# Test	                                           | Input                                                       | Result
# ------------------------------------------------ | ----------------------------------------------------------- | -----------------------------------------------------------------------------------------
# Joe Bloggs                                       | Joe Bloggs                                                  | Enter a message to encipher: Joe Bloggs
#                                                  |                                                             | The enciphered message is: ipf akphht
# ------------------------------------------------ | ----------------------------------------------------------- | -----------------------------------------------------------------------------------------
# Hello World                                      | Hello World                                                 | Enter a message to encipher: Hello World
#                                                  |                                                             | The enciphered message is: gfkkp xpqkc
# ------------------------------------------------ | ----------------------------------------------------------- | -----------------------------------------------------------------------------------------
# Groucho Marx 1                                   | I refuse to join any club that would have me as a member.   | Enter a message to encipher: I refuse to join any club that would have me as a member.
#                                                  |                                                             | The enciphered message is: j qfevtf sp ipjm bmz dkva sgbs xpvkc gbuf nf bt b nfnafq.
# ------------------------------------------------ | ----------------------------------------------------------- | -----------------------------------------------------------------------------------------
# Groucho Marx 2                                   | I've had a perfectly wonderful evening. But this wasn't it. | Enter a message to encipher: I've had a perfectly wonderful evening. But this wasn't it.
#                                                  |                                                             | The enciphered message is: j'uf gbc b ofqefdskz xpmcfqevk fufmjmh. avs sgjt xbtm's js.
# ------------------------------------------------ | ----------------------------------------------------------- | -----------------------------------------------------------------------------------------
# Pangram 1: quick brown fox                       | The quick brown fox jumps over the lazy dog.                | Enter a message to encipher: The quick brown fox jumps over the lazy dog.
#                                                  |                                                             | The enciphered message is: sgf rvjdl aqpxm epw ivnot pufq sgf kbyz cph.
# ------------------------------------------------ | ----------------------------------------------------------- | -----------------------------------------------------------------------------------------
# Pangram 2: Sphinx of black quartz, judge my vow. | Sphinx of black quartz, judge my vow.                       | Enter a message to encipher: Sphinx of black quartz, judge my vow.
#                                                  |                                                             | The enciphered message is: togjmw pe akbdl rvbqsy, ivchf nz upx.

# A00258304

from string import ascii_lowercase

message = input("Enter a message to encipher: ")

enciphered_message = ""

for character in message.lower():
    if character.isalpha():
        index = ascii_lowercase.index(character)
        
        if index % 2 == 0:
            enciphered_message += ascii_lowercase[index + 1]
        else:
            enciphered_message += ascii_lowercase[index - 1]
    else:
        enciphered_message += character
        

print(f"The enciphered message is: {enciphered_message}")