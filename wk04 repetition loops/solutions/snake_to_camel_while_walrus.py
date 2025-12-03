# Program to convert snake_case to camelCase using a while loop
# Version 2: Using the assignment operator (the "walrus")

name = input("Enter a variable name in snake_case: ")

# keep going while there's an underscore and get its index
while (under_index := name.find("_")) != -1:
    # combine the part before the underscore
    # with the capitalised part after the underscore    
    name = name[:under_index] + name[under_index+1:].capitalize()

if name[0].isupper(): # special case, e.g. _variable_name -> VariableName
    name = name[0].lower() + name[1:] # make first letter lowercase    
    
print("Equivalent variable name in camelCase:", name)

