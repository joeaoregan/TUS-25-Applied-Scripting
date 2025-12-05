# Q1(a)(i) Standard Sum
def standard_sum(digits):
    """
    Adds the digits of a string.

    Parameters
    ----------
    digits : str
        A string containing digits to be added together.
    
    Returns
    -------
    int
        The sum of the digits in the paramter string.

    Examples
    --------
    >>> standard_sum("1234")
    10
    >>> standard_sum("2468")
    20
    """
    total = 0
    for digit in digits:
        total += int(digit)

    return total

# Q1(a)(ii) Luhn Sum
def luhn_sum(digits):
    luhn = ""
    total = 0
    for i,digit in enumerate(digits):
        if i % 2 == 0: # odd (index starts at 0)
            luhn += digit
        else:
            luhn += str(int(digit) * 2)

    for digit in luhn:
        total += int(digit)

    return total

# print(standard_sum("12345"))
# print(luhn_sum("046454286"))
# print(luhn_sum("130692544"))

def is_valid_sin(sin):
    if len(sin) != 9:
        return False
    
    for digit in sin:
        if not digit.isnumeric():
            return False
    
    if luhn_sum(sin) % 10 != 0:
        return False
    
    return True

# print(is_valid_sin("046454286"))
# print(is_valid_sin("046454287"))
# print(is_valid_sin("13069254403"))
# print(is_valid_sin("X46454286"))
