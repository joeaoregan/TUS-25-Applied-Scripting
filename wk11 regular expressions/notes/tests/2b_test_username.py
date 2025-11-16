import re

def check_username(username):    
    match = re.fullmatch("[a-z][-a-z0-9_]*", username) # compare the regex to the string
    
    # check if there's a match
    if match: # match object not None -> the regex and string match
        return True
    else:
        return False

# test cases
def test_username_fullmatch(username):
    try:
        assert check_username(username), "Username is not valid"
        print("Username is valid")
    except AssertionError as ae:
        print(ae)

if __name__ == "__main__":
    test_username_fullmatch("joe_bloggs") # Username is valid
    test_username_fullmatch("JoeBloggs")   # Username is not valid
    test_username_fullmatch("ho'donnell") # Username is not valid
