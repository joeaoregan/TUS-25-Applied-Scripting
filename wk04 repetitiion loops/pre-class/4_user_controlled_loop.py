# Example Program: Temperature Conversion using a User-Controlled Loop

choice = "y"

while choice == "y":
    fahrenheit = float(input("Enter the Fahrenheit temperature: "))
    celsius = 5/9 * (fahrenheit - 32)
    print(f"The temperature in Celsius is: {celsius:.1f}")
    choice = input("Convert another temperature? (y/n): ").lower()

print()
print("All temperatures processed")