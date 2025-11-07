# A variable name can only consist of letters, numbers (digits) and the underscore character _

# The variable character stores a single character. What is the correct code to check for a valid character?

# a. if not character.isalnum() and character == "_":
# b. if character.isalnum() or character == "_":
# c. if not character.isalnum() or character == "_":
# d. if character.isalnum() and character == "_":


character = "A"

# if not character.isalnum() and character == "-":
#     print("Valid character")
# else:
#     print("Invalid 1")

if character.isalnum() or character == "_":
    print("valid character")
else:
    print("Invalid 2")

# if not character.isalnum() or character == "_":
#     print("valid character")
# else:
#     print("Invalid 3")

# if character.isalnum() and character == "_":
#     print("valid character")
# else:
#     print("Invalid 4")