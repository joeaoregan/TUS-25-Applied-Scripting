# Program to convert snake_case to camelCase using a counting for loop

snake_name = input("Enter a variable snake_name in snake_case: ")
camel_name = "" # initialise an empty string for the camelCase version

i = 0 # counting while loop
# keep going until we get to the end of the string
while i < len(snake_name):
    # if the current character is an underscore
    if snake_name[i] == "_":         
        i += 1 # move on to the next character
        # captialise the character and add it on
        camel_name += snake_name[i].upper()
    # otherwise just add in on as it is
    else:
        camel_name += snake_name[i]    
    i += 1 # increase the counter

if camel_name[0].isupper(): # special case, e.g. _variable_name -> VariableName
    camel_name = camel_name[0].lower() + camel_name[1:] # make first letter lowercase     
    
print("Equivalent variable name in camelCase:", camel_name)
