# Example Program: Check Eligibility using or

age = int(input("Enter child's age: "))

height = float(input("Enter child's heigh: "))

if age < 3 or height < 1.02:
    print("Child is not permitted to use the ride")
else:
    print("Child is permitted to use the ride")