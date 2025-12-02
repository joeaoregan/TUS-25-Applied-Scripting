# Alternative Version

temperature = float(input("Enter Celsius Temperature: "))

if temperature <= 27:
    status = "Green"
elif temperature <= 30:
    status = "Yellow"
else:
    status = "Orange"

print(f"Temperature Status: {status}")
