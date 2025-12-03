def snake_to_camel(snake_name, lower_camel=True):
    """
    Convert a snake_case identifier into CamelCase or lowerCamelCase format.

    This function is useful for reformatting variable or function names when converting
    code between different naming conventions. It capitalizes each word separated by
    underscores and optionally lowercases the first letter to produce lowerCamelCase.

    Parameters
    ----------
    snake_name : str
        An identifier (variable name, function name) in snake_case.
    lower_camel : bool, optional
        True to convert to lowerCamel, False to convert to UpperCamel. The default is True.

    Returns
    -------
    camel_name : str
        The corresponding identifier in Camel Case.

    Examples
    --------
    >>> snake_to_camel('variable_name')
    'variableName'
    >>> snake_to_camel('variable_name', lower_camel=True)
    'variableName'
    >>> snake_to_camel('variable_name', lower_camel=False)
    'VariableName'
    >>> snake_to_camel('some_long_variable_name', lower_camel=True)
    'someLongVariableName'
    >>> snake_to_camel('_variable_name', lower_camel=True)
    'variableName'
    """
    camel_name = snake_name.replace("_", " ") # replace _ with spaces
    camel_name = camel_name.title() # capitalise words
    camel_name = camel_name.replace(" ", "") # remove the spaces
    
    # name is now in UpperCamel
    # if the new name is required in lowerCamel
    if lower_camel:
        camel_name = camel_name[0].lower() + camel_name[1:]
        
    return camel_name

if __name__ == "__main__":
    name = input("Enter a name in snake_case: ")
    print(f"LowerCamel: {snake_to_camel(name)=}")
    print(f"UpperCamel: {snake_to_camel(name,False)=}")
    print(f"LowerCamel: {snake_to_camel(name,True)=}")
    print(f"UpperCamel: {snake_to_camel(name,lower_camel=False)=}")
    print(f"LowerCamel: {snake_to_camel(name,lower_camel=True)=}")

    # import doctest
    # doctest.testmod(verbose=True)
    
# From the interactive interpreter:
# import snake_to_camel
# import doctest
# doctest.testmod(snake_to_camel)
# doctest.testmod(snake_to_camel, verbose=True)



