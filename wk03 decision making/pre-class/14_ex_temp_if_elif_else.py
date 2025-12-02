# the following program determines temperature warnings using if-elif-else to process the values in order

temperature = float(input("Enter Celsius Temperature: "))

if temperature > 30:
    status = "Orange"
elif temperature > 27:
    status = "Yellow"
else:
    status = "Green"

print(f"Temperature Status: {status}")

