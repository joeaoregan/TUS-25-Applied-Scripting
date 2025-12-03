# Example Program: Temperature Conversion using a counting while loop 

count = 0

while count < 6:
    fahrenheit = float(input("Enter the Fahrenheit temperature: "))
    celsius = 5/9 * (fahrenheit - 32)
    print(f"The temperature in Celsius is: {celsius:.1f}")
    count += 1
    