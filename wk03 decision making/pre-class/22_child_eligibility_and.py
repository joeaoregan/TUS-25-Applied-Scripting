# Another way of implementing this program is using and

age = int(input("Enter child's age: "))
height = float(input("Enter child's height: "))

if age >= 3 and height >= 1.02:
    print("Child is permitted to use the ride")
else:
    print("Child is not permitted to use the ride")