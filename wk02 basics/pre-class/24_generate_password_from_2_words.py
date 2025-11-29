# Example Program: Generate Password from 2 Words

# Common advice for a strong password is to include upper and 
# lowercase letters, at least one digit # and a special 
# character.  The following program generates a password by 
# inputting two words, # capitalising them, joining them with a 
# digit and adding a special character. 

from random import choice
from string import punctuation, digits

# Input the words
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# Choose a random digit
digit = choice(digits)
# Choose a random special character
special = choice(punctuation)

# Generate the password
password = word1.capitalize() + digit + word2.capitalize() + special

# Display the password
print(f"Password: {password}")