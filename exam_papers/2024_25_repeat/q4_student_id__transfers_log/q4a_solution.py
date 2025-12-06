import re

while True:
    student_id = input("Enter a student id or q to quit: ")

    if student_id == 'q':
        break
    match = re.fullmatch(r"[A-Z]{1,2}\d{6}[0-9A]")
    
    if match:
        print("Valid Student ID")
    else:
        print("Not a valid Student ID")