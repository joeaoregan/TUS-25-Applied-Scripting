# Write and test a program to input a user's fullname (in the format firstname lastname) and then 
# generate and display a lowercase username using their firstname and the first initial of their lastname.

# Hint: To split the fullname into firstname and lastname using the space between the names, use the code:
# firstname, lastname = fullname.split()

# This question uses exact matching, so white space matters. 

# For example:

# Input	         | Result
# -------------- | ---------------------------------------------------------------------
# Joe Bloggs     | Enter your first and last names, separated by a space: Joe Bloggs
#                | Your username is: joeb
# -------------- | ---------------------------------------------------------------------
# Farouk McNally | Enter your first and last names, separated by a space: Farouk McNally
#                | Your username is: faroukm

full_name = input("Enter your first and last names, separated by a space: ")

username = full_name.lower().split(" ")
username = username[0] + username[1][0]

print(f"Your username is: {username}")