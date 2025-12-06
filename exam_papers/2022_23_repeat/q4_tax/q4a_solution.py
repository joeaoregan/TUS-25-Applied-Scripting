import re

regex = re.compile("[A-Z{2}[0-9]{6}[A-Z]")

while True:
    tax_code = input("Enter the Tax Code or q to quit: ")
    if tax_code == 'q':
        break

    match = re.fullmatch(regex, tax_code)

    if match:
        print("Valid Tax Code")
    else:
        print("Not a valid Tax Code")