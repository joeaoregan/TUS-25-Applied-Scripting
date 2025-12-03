def square(number):
    """
    Return the square of a number.

    Parameters
    ----------
    number : int or float
        The number to be squared.
    
    Returns
    -------
    int or float
        The square of the input number.
    
    Examples
    --------
    >>> square(5)
    25
    >>> square(0)
    0
    >>> square(-3)
    9
    >>> square(2.5)
    6.25
    >>> square(-1.5)
    2.25
    """
    return number * number


if __name__ == "__main__":
    import doctest
    # doctest.testmod()
    doctest.testmod(verbose=True)