# Example Program: Temperature Conversion using a User-Controlled Loop (boolean variable)

finished = False

while not finished:
    fahrenheit = float(input("Enter the Fahrenheit temperature: "))
    celsius = 5/9 * (fahrenheit - 32)
    print(f"The temperature in Celsius is: {celsius:.1f}")
    
    response = input("Are you finished? (y/n): ").lower()
    if response != "y":
        finished = True

print()
print("All temperatures processed")