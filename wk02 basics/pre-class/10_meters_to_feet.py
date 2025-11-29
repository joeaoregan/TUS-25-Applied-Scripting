# Program to convert a distance in meters to feet and inches

# Input meters
meters = float(input("Enter the distance in meters: "))

# Calculate feet as meters x 3.28084
feet = meters * 3.28084

# Calculate whole feet as integer part of feet
whole_feet = int(feet)

# Calculate inches as (feet - whole_feet) * 12
inches = (feet - whole_feet) * 12

# Print whole_feet, inches
print(f"Equivalent distance is {whole_feet} feet, {inches:.1f} inches")