import re

# input the phone number
student_id = input("Enter local landline (Athlone), e.g. 090 6424400: ")

# compare the regex to the string
match = re.fullmatch("090 64[0-9]{5}", student_id)

# check if there's a match
if match:
    print("Valid local landline number for Athlone")
else:
    print("Invalid local landline number for Athlone")