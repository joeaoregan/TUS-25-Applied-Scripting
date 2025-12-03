# Function to convert from snake_case to camel case
def snake_to_camel(snake_name, lower_camel=True):
    """
    Convert an identifer in snake_case to camel case

    Parameters
    ----------
    snake_name : str
        An identifier in snake_case.
    lower_camel : bool, optional
        True to convert to lowerCamel, False to convert to UpperCamel.. The default is True.

    Returns
    -------
    camel_name : str
        The correspondign identifier converted to camel case.
        
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
    if lower_camel:
        camel_name = camel_name[0].lower() + camel_name[1:]
    return camel_name

#print(f"{__name__=}")

if __name__ == "__main__":
    # print(f"{snake_to_camel('var_name')=}")
    # print(f"{snake_to_camel('var_name', lower_camel=True)=}")
    # print(f"{snake_to_camel('var_name', lower_camel=False)=}")
    # snake_to_camel('var_name', lower_camel=False)
    import doctest
    doctest.testmod(verbose=True)

