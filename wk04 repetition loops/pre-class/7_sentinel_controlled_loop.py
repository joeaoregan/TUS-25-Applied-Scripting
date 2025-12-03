# Example Program: Temperature Conversion using a Sentinel-Controlled Loop

while True:
    fahrenheit = float(input("Enter the Fahrenheit temperature or -9999 to finish: "))
    if fahrenheit == -9999:
        break
    celsius = 5/9 * (fahrenheit - 32)
    print(f"The temperature in Celsius is: {celsius:.1f}")

print()
print("All temperatures processed")