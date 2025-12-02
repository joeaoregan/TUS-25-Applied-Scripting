# Example Program: Temperature Warning with if-else

# Program to display the high temperature status

temperature = float(input("Enter Celsius Temperature: "))
if temperature > 27:
    print("Status Yellow Warning")
else:
    print("Status Green")