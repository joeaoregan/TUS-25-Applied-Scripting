# test cases
import re

def check_id(id):    
    match = re.fullmatch("A[0-9]{8}", id, re.I) # compare the regex to the string
    
    # check if there's a match
    if match: # match object not None -> the regex and string match
        return True
    else:
        return False

def test_id_fullmatch(id):
    try:
        assert check_id(id), "Not a valid AIT Student ID"
        print("Valid AIT Student ID")
    except AssertionError as ae:
        print(ae)

if __name__ == "__main__":
    test_id_fullmatch("A00123456") # Valid AIT Student ID
    test_id_fullmatch("a00123456") # Valid AIT Student ID
