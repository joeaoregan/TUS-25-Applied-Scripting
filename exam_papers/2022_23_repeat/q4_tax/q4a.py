import re

while True:
    # tax_code = input("Enter tax code or q to quit: ")
    tax_code = "AB123456C"
    tax_code = "ABC123456C"
    # tax_code = "AB12345C"
    # tax_code = "AB1234567C"
    tax_code = "AB123456c"
    if tax_code == 'q':
        break

    match = re.fullmatch(r"[A-Z]{2}\d{6}[a-zA-Z]", tax_code)

    if match:
        print("Valid Tax Code")
    else:
        print("Invalid Tax Code")
    break