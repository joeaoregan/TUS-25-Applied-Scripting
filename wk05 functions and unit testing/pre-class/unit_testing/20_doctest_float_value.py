# doctest Example: Function to convert feet and inches to metres

# Doesn't work for float values:

# >>> convert_to_metres(29, 2.5)
# 8.9027
# >>> convert_to_metres(0, 12)
# 0.3048
# >>> convert_to_metres(6, 0)
# 1.8288

def convert_to_metres(feet, inches):
    """
    Convert a distance from feet and inches to metres.
    
    This function assumes feet and inches are non-negative.
    It uses standard conversion: 1 inch = 0.0254 m.

    Parameters
    ----------
    feet : int
        The feet part of the distance.
    inches : float
        The inches part of the distance.
    
    Returns
    -------
    float
        The distance in metres.
    
    Examples
    --------
    >>> f"{convert_to_metres(29, 2.5):.4f}"
    '8.9027'
    >>> f"{convert_to_metres(0, 12):.4f}"
    '0.3048'
    >>> f"{convert_to_metres(6, 0):.4f}"
    '1.8288'
    """
    return (feet*12 + inches) * 0.0254

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)