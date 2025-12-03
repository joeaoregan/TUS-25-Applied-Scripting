# Example Program: Input Validation Loop using while and Walrus Operator

while not 0 <= (octet := int(input("Enter the octet: "))) <= 255:
    print("Invalid, try again")

print("Valid octet entered")