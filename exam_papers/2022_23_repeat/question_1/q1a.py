# 2022/23 Repeat
# Q1(a)

def is_valid_password(password):
    """
    Check if a password is valid.
    
    Parameters
    ----------
    password : str
        Password to check if valid.

    Returns
    -------
    bool
        if the password is valid or not.

    Examples
    --------
    >>> is_valid_password("$Now4Something")
    True
    >>> is_valid_password("4Ever!")
    False
    >>> is_valid_password("2Good2Be4Gotten?")
    False
    """
    if len(password) < 8 or len(password) > 15:
        return False
    
    has_upper = has_lower = has_digit = has_special = False
    
    for letter in password:
        if letter.isalpha():
            if letter.isupper():
                has_upper = True
            else:
                has_lower = True
        elif letter.isnumeric():
            has_digit = True
        else:
            has_special = True
        if has_upper and has_lower and has_digit and has_special:
            return True

    return has_upper and has_lower and has_digit and has_special
    
# print(is_valid_password("test"))
# print(is_valid_password("testtesttesttes"))
# print(is_valid_password("testtesttesttest"))

# print(is_valid_password("$Now4Something"))
# print(is_valid_password("4Ever!"))
# print(is_valid_password("2Good2Be4Gotten?"))
# print(is_valid_password("Secret123"))
# print(is_valid_password("OpenSesame!"))
# print(is_valid_password("open_sesame123"))

# Q1(b)
if __name__ == "__main__":
    while(True):
        password = input("Enter password, or q to quit: ")
        if password.lower() == 'q':
            break

        if is_valid_password(password):
            print("Valid password")
        else:
            print("Invalid password")