# The variable variable_name contains a string.

# What is the correct for loop statement to process each character of the string, one at a time?

# a. for character: variable_name
# b. for i=0; i < len(variable_name); i++
# c. for character in variable_name:
# d. foreach character in variable_name:


variable_name = "example"

# for character:
#     variable_name

# for i = 0; i < len(variable_name); i++:
#     print(variable_name[i])

for character in variable_name:
    print(character)

# foreach char in variable_name:
#     print(char)