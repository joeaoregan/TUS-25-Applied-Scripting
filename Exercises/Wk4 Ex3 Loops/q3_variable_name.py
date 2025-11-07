# A variable name can only consist of letters, numbers (digits) and the underscore character _.

# Write and test a program which inputs a variable and displays a message indicating whether or not it is valid.

# One possible approach is as follows:

# Input the variable name
# For each character in the variable name
#     If the character is not valid
#         Display "Variable name has invalid character" and display the character
#         Break from the loop
# If the loop completed (i.e. all characters were processed)
#     Display "Valid variable name"

# For example: 

# Test                                                  | Input               | Result
# ------------------------------------------------------| --------------------| --------------------------------------------
# Valid variable name, letter only                      | mark                | Enter the variable name: mark
#                                                       |                     | # Valid variable name
# ------------------------------------------------------| --------------------| --------------------------------------------
# Valid variable name, letters and underscores          | number_of_students  | Enter the variable name: number_of_students
#                                                       |                     | Valid variable name
# ------------------------------------------------------| --------------------| --------------------------------------------
# Valid variable name, letters and numbers              | score2              | Enter the variable name: score2
#                                                       |                     | Valid variable name
# ------------------------------------------------------| --------------------| --------------------------------------------
# Valid variable name, letters, numbers and underscores | free_space_3rd_disk | Enter the variable name: free_space_3rd_disk
#                                                       |                     | Valid variable name
# ------------------------------------------------------| --------------------| --------------------------------------------
# Invalid variable name, uses a hyphen -                | num-students        | Enter the variable name: num-students
#                                                       |                     | Invalid character -
# ------------------------------------------------------| --------------------| --------------------------------------------
# Invalid variable name, uses a space                   | number of students  | Enter the variable name: number of students
#                                                       |                     | Invalid character
# ------------------------------------------------------| --------------------| --------------------------------------------
# Invalid variable name, uses an ampersand &            | ways&means          | Enter the variable name: ways&means
#                                                       |                     | Invalid character &

# A00258304

variable_name = input("Enter the variable name: ")

# for character in variable_name:
#     if not character.isalpha() and not character.isdigit() and character != "_":
#         print(f"Invalid character {character}")
#         break
# else:
#     print("Valid variable name")
    
# valid = True
# for character in variable_name:
#     if character.isalpha() or character.isdigit() or character == "_":
#         valid = True
#     else:
#         valid = False
#         break
# else:
#     print("Valid variable name")
    
# if not valid:
#     print(f"Invalid character {character}")

for character in variable_name:
    if not (character.isalpha() or character.isdigit() or character == "_"):
        print(f"Invalid character {character}")
        break
else:
    print("Valid variable name")
