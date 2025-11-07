# A00258304

# The variable username contains a string. Assuming that the first character is a letter, 
# which of the following is the correct condition to check if the first character of the string in username is a lowercase letter?

# a. username[0].lower()
# b. username[0].islower() # Correct
# c. username[1].islower()
# d. username[1].lower()

username = "joe"

# print(username[0].lower()) # j
print(username[0].islower()) # True
# print(username[1].islower()) # True (but 2nd character)
# print(username[1].lower()) # o