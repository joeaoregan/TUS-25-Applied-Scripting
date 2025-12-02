# Example Program: Delivery Charges using Nested If

destination = input("Enter the destination (National or International): ")

weight = float(input("Enter the weight of the package in kgs: "))

if destination.lower() == "national":
    if weight < 2:
        print("Delivery is free.")
    else:
        print("Delivery costs €5")
else:
    if weight < 5:
        print("Delivery costs €10.")
    else:
        print("Delivery costs €20.")