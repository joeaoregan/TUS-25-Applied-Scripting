import re

def check_student_id(id):    
    match = re.fullmatch("[A][0-9]{8}", id) # compare the regex to the string

    if match:
        return True
    else:
        return False

# test cases

try:
    assert check_student_id("A00123456"), "Invalid AIT Student ID"
    print("Valid AIT Student ID")
except AssertionError as ae:
    print(ae)

try:
    assert check_student_id("A123456"),"Invalid AIT Student ID"
    print("Valid AIT Student ID")
except AssertionError as ae:
    print(ae)

try:
    assert check_student_id("a00123456"),"Invalid AIT Student ID"
    print("Valid AIT Student ID")
except AssertionError as ae:
    print(ae)

try:
    assert check_student_id("F00123456"),"Invalid AIT Student ID"
    print("Valid AIT Student ID")
except AssertionError as ae:
    print(ae)