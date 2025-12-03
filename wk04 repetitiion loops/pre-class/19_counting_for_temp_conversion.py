# Example Program: Temperature Conversion using a counting for loop

for i in range(6):
    fahrenheit = float(input("Enter the Fahrenheit temperature: "))

    celsius = 5/9 * (fahrenheit - 32)

    print(f"The temperature in Celsius is: {celsius:.1f}")