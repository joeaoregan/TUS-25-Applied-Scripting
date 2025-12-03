# Example Program: Validate Lotto Numbers using a counting for loop

print("Pick 6 Numbers from 1-47")
print("------------------------")

for i in range(6):
    print("\nNumber", i+1)
    number = int(input("Enter a number between 1 and 47: "))

    while not 1 <= number <= 47:
        print("Invalid number")

        number = int(input("Enter a number between 1 and 47: "))

    print("Number is valid")

print("6 Valid Numbers")