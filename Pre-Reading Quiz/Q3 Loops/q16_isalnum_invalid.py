# A variable name can only consist of letters, numbers (digits) and the underscore character _

# The variable character stores a single character. What is the correct code to check for an invalid character?

# a. if not character.isalnum() or character != "_":
# b. if not character.isalnum() and character == "_":
# c. if not character.isalnum() or character == "_":
# d. if not character.isalnum() and character != "_":

character = "_"

# if not character.isalnum() or character != "_":
#     print("Invalid character")
# else:
#     print("Valid 1")    

# if not character.isalnum() and character == "_":
#     print("Invalid character")
# else:
#     print("Valid 2")

# if not character.isalnum() or character == "_":
#     print("Invalid character")
# else:
#     print("Valid 3")

if not character.isalnum() and character != "_":
    print("Invalid character")
else:
    print("Valid 4")