# A more general approach involves allowing the user to specify the number of repetitions:

count = 0

num_values = int(input("How many temperature values? "))

while count < num_values:
    fahrenheit = float(input("Enter the Fahrenheit temperature: "))
    celsius = 5/9 * (fahrenheit - 32)
    print(f"The temperature in Celsius is: {celsius:.1f}")
    count += 1

print()
print("All termperatures processed")