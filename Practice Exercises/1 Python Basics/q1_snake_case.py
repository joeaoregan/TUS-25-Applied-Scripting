# Using only string processing features (no loops/lists) design, write and test a Python program
# which will convert a variable name in snake_case to the equivalent variable name in camelCase.

# Specification Table
# Inputs     | Processing Steps                 | Outputs
# ---------- | -------------------------------- | ----------
# name in    | Input name in snake case         | name in
# snake case | Replace underscore with space    | camel case
#            | Capitalise individual "words"    |
#            | Remove the space                 |
#            | Change first letter to lowercase |
#            | Print name in camel case         |

# Test                  | Input         | Result
# --------------------- | ------------- | ----------------------------------------------------------
# Only one underscore   | variable_name | Enter the variable name in snake_case: variable_name
#                       |               | The equivalent variable name in camelCase is: variableName
# --------------------- | ------------- | ----------------------------------------------------------
# Multiple underscores  | my_var_name   | Enter the variable name in snake_case: my_var_name
#                       |               | The equivalent variable name in camelCase is: myVarName
# --------------------- | ------------- | ----------------------------------------------------------
# No underscore         | variable      | Enter the variable name in snake_case: variable
#                       |               | The equivalent variable name in camelCase is: variable
# --------------------- | ------------- | ----------------------------------------------------------
# Leading underscore    | _variable     | Enter the variable name in snake_case: _variable
#                       |               | The equivalent variable name in camelCase is: variable

# A00258304
snake_case = input("Enter the variable name in snake_case: ")

camel_case = snake_case.replace("_", " ")

camel_case = camel_case.title()

camel_case = camel_case.replace(" ", "")

camel_case = camel_case[0].lower() + camel_case[1:]

print(f"The equivalent variable name in camelCase is: {camel_case}")