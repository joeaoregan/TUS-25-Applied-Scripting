# Which of the following is not a valid way to call the snake_to_camel function from Question 7?

# a. snake_to_camel("my_variable") # OK
# b. snake_to_camel("my_variable", False) # OK
# c. snake_to_camel("my_variable", True) # OK
# d. snake_to_camel() # Correct


def snake_to_camel(name, upper=False):
    pass

snake_to_camel() # TypeError: snake_to_camel() missing 1 required positional argument: 'name'