#  Example Program: Validation Lotto Numbers using a counting while loop

print("Pick 6 Numbers from 1-47")
print("------------------------")

count = 0

while count < 6:
    print("\nNumber", count + 1)
    number = int(input("Enter a number between 1 and 47: "))

    while not 1 <= number <= 47:
        print("Invalid number")

        number = int(input("Enter a number between 1 and 47: "))

    print("Number is valid")

    count += 1

print("6 Valid Numbers")