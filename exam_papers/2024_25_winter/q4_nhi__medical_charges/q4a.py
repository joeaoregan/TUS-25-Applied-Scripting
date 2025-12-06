import re

while True:
    nhi_number = input("Enter the NHI Number or q to quit: ")

    if nhi_number == 'q':
        break

    match = re.fullmatch("[A-Z]{3}\d{2}(\d{2}|[A-Z{2}])", nhi_number)

    if match:
        print("Valid NHI Number")
    else:
        print("Not a valid NHI Number")