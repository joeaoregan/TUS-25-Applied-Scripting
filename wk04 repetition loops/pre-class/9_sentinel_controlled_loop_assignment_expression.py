# Example Program: Sentinel-Controlled Loop using Assignment Expression

while (fahrenheit := float(input("Enter the Fahrenheit temperature or -9999 to finish: "))) != -9999:
    celsius = 5/9 * (fahrenheit - 32)
    print(f"The temperature in Celsius is: {celsius:.1f}")