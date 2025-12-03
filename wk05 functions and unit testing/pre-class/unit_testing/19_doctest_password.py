# doctest Example: Function to validate the length of a password

def is_valid_password_length(password, min_len=8, max_len=32):
    """
    Check password is between minimum and maximum length.
    
    Parameters
    ----------
    password : str
        The password to be checked
    min_len : int, optional
        The minimum acceptable password length. The default is 8.
    max_len : int, optional
        The maximum acceptable password length. The default is 32.

    Returns
    -------
    bool
        Whether or not the password length is valid.    

    Examples
    --------
    >>> is_valid_password_length("secret")
    False
    >>> is_valid_password_length("mypassword123")
    True
    >>> is_valid_password_length("my very excellent password which is too long", 8, 16)
    False
    """    
    return min_len <= len(password) <= max_len

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)