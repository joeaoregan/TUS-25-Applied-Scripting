imo_digits = input("Enter the digits of the IMO number: ")

total = 0

for i, digit in enumerate(imo_digits[:6]):
    total += int(digit) * (7-i)
print(f"{total=}")

if total % 10 == int(imo_digits[-1]):
    print("Valid IMO number")
else:
    print("Not a valid IMO number")