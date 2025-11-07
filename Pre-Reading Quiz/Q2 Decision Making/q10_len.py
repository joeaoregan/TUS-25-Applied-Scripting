# A00258304

# The variable username contains a string. What the is correct code to determine the length of the string, 
# that is, the number of characters in the string contained in the username variable?

# a. username.length()
# b. username.len()
# c. len(username) # correct
# d. length(username)

username = "jregan"

# print(username.length) # AttributeError: 'str' object has no attribute 'length'
# print(username.len()) # AttributeError: 'str' object has no attribute 'len'
print(len(username)) # Correct: 6
# print(length(username)) # NameError: name 'length' is not defined

