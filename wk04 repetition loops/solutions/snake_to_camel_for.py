# Program to convert snake_case to camelCase using a for loop

snake_name = input("Enter a variable snake_name in snake_case: ")
print(f"{snake_name=}") # f-string displays variable name and value

# initialise an empty string for the camelCase version
camel_name = ""

# Boolean variable to indicate whether or not character should be capitalised
capitalize_on = False
# for each character in the string
for char in snake_name:
    # if the current character is an underscore
    if char == "_":
        # remember that the next character has to be capitalised
        capitalize_on = True
    # otherwise it's not an underscore
    else:
        # if we're meant to capitalise the current character
        # (because the previous character was an underscore)
        if capitalize_on:
            # capitalise the character and add it on
            camel_name += char.upper()
            # turn off the capitalsiation
            capitalize_on = False
        # otherwise just add on the current character
        else:
            camel_name += char
    
    print(f"{camel_name=}")
    
print("Equivalent variable snake_name in camelCase:", camel_name)
