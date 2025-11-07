# A00258304

# The format of a Personal Public Servicies Number (simplified version) is 8765432A where A represents any single letter.
# Using only string processing features (no loops/lists/regular expressions) design, write and test a Python program which will determine whether or not an input PPSN is valid.
# For example:

# Test                                   | Input     | Result
# ---------------------------------------|-----------|--------------------------
# Valid PPSN 1                           | 8765432A  | Enter the PPSN: 8765432A
#                                        |           | PPSN is Valid
# ---------------------------------------|-----------|--------------------------
# Valid PPSN 2                           | 1234567B  | Enter the PPSN: 1234567B
#                                        |           | PPSN is Valid
# ---------------------------------------|-----------|--------------------------
# Invalid - no letter                    | 1234567   | Enter the PPSN: 1234567
#                                        |           | PPSN is not valid
# ---------------------------------------|-----------|--------------------------
# Invalid - extra digit, no letter       | 12345678  | Enter the PPSN: 12345678
#                                        |           | PPSN is not valid
# ---------------------------------------|-----------|--------------------------
# Invalid - extra digit                  | 12345678C | Enter the PPSN: 12345678C
#                                        |           | PPSN is not valid
# ---------------------------------------|-----------|--------------------------
# Invalid - extra letter                 | 1234567DE | Enter the PPSN: 1234567DE
#                                        |           | PPSN is not valid
# ---------------------------------------|-----------|--------------------------
# Invalid - too few digits               | 123456F   | Enter the PPSN: 123456F
#                                        |           | PPSN is not valid
# ---------------------------------------|-----------|--------------------------
# Invalid - too few digits, extra letter | 123456GH  | Enter the PPSN: 123456GH
#                                        |           | PPSN is not valid
# ---------------------------------------|-----------|--------------------------
# Invalid - all digits                   | 12345678  | Enter the PPSN: 12345678
#                                        |           | PPSN is not valid
# ---------------------------------------|-----------|--------------------------
# Invalid - all letters                  | ABCDEFGH  | Enter the PPSN: ABCDEFGH
#                                        |           | PPSN is not valid
# ---------------------------------------|-----------|--------------------------
# Invalid - non-alphanumeric character   | 1234?67B  | Enter the PPSN: 1234?67B
#                                        |           | PPSN is not valid
# ---------------------------------------|-----------|--------------------------
# Invalid - letter in incorrect position | A1234567  | Enter the PPSN: A1234567
#                                        |           | PPSN is not valid



# ppsn = input("Enter the PPSN: ")
ppsn = "1234567A"

if len(ppsn) == 8 and ppsn[:7].isdigit() and ppsn[-1].isalpha():
    print("PPSN is valid")
else:
    print("PPSN is not valid")

# if len(ppsn) == 8 and ppsn[:7].isdigit() and ppsn[-1].isalpha():
#     print("PPSN is valid")
# elif len (ppsn) == 9 and ppsn[:7].isdigit() and ppsn[7:9].isalpha():
#     print("PPSN is valid")
# else:
#     print("PPSN is not valid")