# Example Program: Check Digit Calculation of an IMO Number

imo_digits = input("Enter the digits of the IMO number: ")

total = 0

for i in range(len(imo_digits)-1):
    total += int(imo_digits[i]) * (7-i)
print(f"{total=}")

if total % 10 == int(imo_digits[-1]):
    print("Valid IMO number")
else:
    print("Not a valid IMO number")