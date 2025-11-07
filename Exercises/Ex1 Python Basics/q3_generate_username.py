# A00258304

# Purpose of Program: Create lowercase username from full name

# Write and test a program to input a user's fullname (in the format firstname lastname) and then 
# generate and display a lowercase username using their firstname and the first initial of their lastname.

# Hint: To split the fullname into firstname and lastname using the space between the names, use the code:
# firstname, lastname = fullname.split()

# This question uses exact matching, so white space matters.

# Example:

# Input          | Result
# ---------------|-----------------------------------------------------------------------
# Joe Bloggs     | Enter your first and last names, separated by a space: Joe Bloggs
#                | Your username is: joeb
# ---------------|-----------------------------------------------------------------------
# Farouk McNally | Enter your first and last names, separated by a space: Farouk McNally
#                | Your username is: faroukm


fullname = input("Enter your first and last names, separated by a space: ")
firstname, lastname = fullname.split()

username = firstname.lower() + lastname[0].lower()

print(f"Your username is: {username}")