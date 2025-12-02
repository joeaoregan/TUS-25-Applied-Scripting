# Example Program: Temperature Warning with if-else, Alternative Version

temperature = float(input("Enter Celsius Temperature: "))
if temperature > 27:
    status = "Yellow"
else:
    status = "Green"

print(f"Temperature Status: {status}")