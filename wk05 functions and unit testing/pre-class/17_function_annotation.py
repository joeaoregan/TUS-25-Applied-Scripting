def greeting(name: str) -> str:
    return "Hello " + name


def square(number: float) -> float:
    """
    Calculate the square of a number.

    Parameters
    ----------
    number : float
        The number to be squared.

    Returns
    -------
    float
        The number squared.
    """
    return number * number


def is_valid_password_length(password: str, min_len: int = 8, max_len: int = 32) -> bool:
    """
    Check if the length of a password is between specified minimum and maximum

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
    """
    return min_len <= len(password) <= max_len