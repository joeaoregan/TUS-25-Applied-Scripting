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
    >>> convert_to_metres(29, 2.5)
    >>> convert_to_metres(0, 12)
    >>> convert_to_metres(6, 0)
    """