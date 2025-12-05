# Q1(a)(i)
def is_valid_username(username):
    """
    Check if a username is valid (Doesn't contain 'Admin', less than 15 characters, alphanumeric or _ characters)
    
    Parameters
    ----------
    username : str
        The username to check is valid.
    
    Returns
    -------
    boolean
        If the username is valid.
    
    Examples
    --------
    >>> is_valid_username("test123_X")
    True
    >>> is_pangram("admin1234")
    False
    >>> is_pangram("usernameusername")
    False
    """
    if "admin" in username.lower():
        return False
    
    if len(username) > 15:
        return False
    
    for letter in username:
        if not letter.isalnum() and not letter == "_":
            return False
        
    return True

# print(is_valid_username("usernameuseadmin"))

if __name__ == "__main__":
    while(True):
        username = input("\nEnter a username, or q to quit: ")
        
        if username.lower() == "q":
            break

        if is_valid_username(username):
            print("Valid username")
        else:
            print("Not a valid username")        

    