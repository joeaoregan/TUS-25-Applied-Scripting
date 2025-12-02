# ppsn = input("Enter the PPSN: ")

ppsn = "8765432A"

valid = len(ppsn) == 8 and ppsn[:-1].isdigit() and ppsn[-1].isalpha()

if valid:
    print("PPSN is valid")
else:
    print("PPSN is not valid")