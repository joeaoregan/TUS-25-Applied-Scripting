# The variable character contains a single character. 
# What is the correct code to check if the character is a lowercase letter?

# a. if character.lower():
# b. if character.islower(): # Correct
# c. if character.isalnum():
# d. if character.isalpha():


character = "A"

# if charcacter.lower():
if character.islower():
    print("Lowercase letter")

if character.isalnum():
    print("Alphanumeric character")

if character.isalpha():
    print("Alphabetic character")