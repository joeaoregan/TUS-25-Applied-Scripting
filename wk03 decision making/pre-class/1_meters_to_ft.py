metres = float(input("Enter the distance in metres: "))
feet = metres * 3.28084
whole_feet = int(feet)
inches = (feet - whole_feet) * 12
print(f"Equivalent distance is {whole_feet} feet, {inches:.1f} inches")
