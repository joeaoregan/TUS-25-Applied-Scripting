# A00258304

# The variable username contains a string. Which of the following is the correct code for a condition 
# to check if all the characters in username are alphanumeric (i.e. letters and numbers)?

# a. username.alnum()
# b. username.isalpha()
# c. username.alpha()
# d. username.isalnum() # Correct

username = "joe123"

# print(username.alnum()) # AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
# print(username.isalpha()) # False
# print(username.alpha()) # AttributeError: 'str' object has no attribute 'alpha'. Did you mean: 'isalpha'?
print(username.isalnum()) # True