import re

def check_student_id(id):    
    match = re.fullmatch("[A][0-9]{8}", id) # compare the regex to the string

    if match:
        return True
    else:
        return False

# test cases
def test_student_id_fullmatch(id):
    try:
        assert check_student_id(id), "Invalid AIT Student ID"
        print("Valid AIT Student ID")
    except AssertionError as ae:
        print(ae)

if __name__ == "__main__":
    test_student_id_fullmatch("A00123456") # True
    test_student_id_fullmatch("A123456") # False
    test_student_id_fullmatch("a00123456") # False
    test_student_id_fullmatch("F00123456") # False
