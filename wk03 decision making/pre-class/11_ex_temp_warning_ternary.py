# Example Program: Temperature Warning with the Ternary Conditional Operator

temperature = float(input("Enter Celsius Temperature: "))
status = "Yellow" if temperature > 27 else "Green"
print(f"Temperature Status: {status}")

