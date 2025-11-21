# 19:20ish
# Validate a Vehicle Registration
import re

# vehicle_reg = input("Enter the Vehicle Registration: ")
# vehicle_reg = "HLI 802" # up to 1987
# vehicle_reg = "252-RN-123456" # 2013 to present
vehicle_reg = "182-AZ-123" # 

# Check if it matches the oldest format
if re.fullmatch(r"[A-Z]{2,3} \d{1,4}", vehicle_reg):
    print("Valid Vehicle Registration up to 1987")
# otherwise check if it matches the format from 1987-2012
elif re.fullmatch(r"\d{2}-[A-Z]{1,2}-\d{1,6}", vehicle_reg):
    print("Valid Vehicle Registration from 1987-2012")
# otherwise check if it matches the format from 2013 to present
elif re.fullmatch(r"\d{2}[12]-[A-Z]{1,2}-\d{1,6}", vehicle_reg):
    print("Valid Vehicle Registration from 2013 to present")
# otherwise it's not valid
else:
    print("Not a valid Vehicle Registration")