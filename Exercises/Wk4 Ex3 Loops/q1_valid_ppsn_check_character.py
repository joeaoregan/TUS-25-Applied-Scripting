# A00258304

# The simplified (old) form of the Personal Public Services Number has the format 8765432A where A represents a check character (letter), used to check for an incorrect PPSN, based on a calculation involving the digits

# Write a Python program which inputs a PPSN and determines whether or not it is valid, based on the check character calculation. 

# A suggested approach is as follows:

# Set the alphabet
# Input ppsn
# Set total to 0
# For each digit in the ppsn
#     Multiply the digit by its weighting and add total
# Calculate the remainder after dividing by 23
# Determine the check letter in the “alphabet”
# If the check letter is equal to the actual letter in the ppsn
#     Display “PPSN x is Valid” (where x represents the input PPSN
# Otherwise
# Display “PPSN x is not valid”

# Test	                              | Input    | Result
# ------------------------------------|----------|---------------------------- 
# Valid (from Slides)                 | 2546736P | Enter the PPSN: 2546736P
#                                     |          | PPSN 2546736P is valid
# ------------------------------------|----------|---------------------------- 
# Valid, leading 0                    | 0396049T | Enter the PPSN: 0396049T
#                                     |          | PPSN 0396049T is valid
# ------------------------------------|----------|---------------------------- 
# Valid, W check character            | 1721617W | Enter the PPSN: 1721617W
#                                     |          | PPSN 1721617W is valid
# ------------------------------------|----------|---------------------------- 
# Valid, leading 0, W check character | 0557087W | Enter the PPSN: 0557087W
#                                     |          | PPSN 0557087W is valid
# ------------------------------------|----------|---------------------------- 
# Invalid                             | 8765432A | Enter the PPSN: 8765432A
#                                     |          | PPSN 8765432A is not valid
# ------------------------------------|----------|---------------------------- 
# Invalid                             | 9903182L | Enter the PPSN: 9903182L
#                                     |          | PPSN 9903182L is not valid


alphabet = "WABCDEFGHIJKLMNOPQRSTUV"
total = 0

ppsn = input("Enter the PPSN: ")

for i, digit in enumerate(ppsn[:-1]):
    total += int(digit) * (8 - i)
    
letter_index = total % 23
check_letter = alphabet[letter_index]

if ppsn[-1] == check_letter:
    print(f"PPSN {ppsn} is valid")
else:
    print(f"PPSN {ppsn} is not valid")