#  Example Program: Input Validation Loop using infinite while loop and break

octet = int(input("Enter the octet: "))

while not 0 <= octet <= 255:
    print("Invalid, try again")
    octet = int(input("Enter the octet: "))

print("Valid octet entered")