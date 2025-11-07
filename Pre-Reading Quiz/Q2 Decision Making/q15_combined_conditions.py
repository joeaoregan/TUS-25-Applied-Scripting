# A00258304

# A username is valid if
# * it has between 4 and 8 characters, inclusive
# * and the first character is a lowercase letter
# * and all the characters are alphanumeric
# Which of the following combined conditions is the correct code to validate a username based on the above rules?

# a. 4 <= len(username) <= 8 and username[0].islower() and username.isalnum() # Correct
# b. 4 >= len(username) <= 8 or not username[0].islower() or not username.isalnum()
# c. 4 <= len(username) <= 8 or username[0].islower() or username.isalnum()
# d. 4 >= len(username) <= 8 and not username[0].islower() and not username.isalnum()

username = "joe"

print(4 <= len(username) <= 8 and username[0].islower() and username.isalnum()) # joe123: True, joe: False - need ands
# print(4 >= len(username) <= 8 or not username[0].islower() or not username.isalnum()) # joe123: False
# print(4 <= len(username) <= 8 or username[0].islower() or username.isalnum()) # joe123: True, joe: True
# print(4 >= len(username) <= 8 and not username[0].islower() and not username.isalnum()) # joe123: False