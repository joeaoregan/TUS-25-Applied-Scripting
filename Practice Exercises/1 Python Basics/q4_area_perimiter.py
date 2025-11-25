# Write and test a program which will calculate the area and perimeter of a rectangular room 
# and display them to 1 decimal place.

# The necessary formulae are:

# area = length × width

# perimeter = 2 × (length + width)

# Hint: use string formatting (e.g. the f-string) to display the results to 1 decimal place.

# For example:

# Input	| Result
# ----- | ------------------------------
# 10    | Enter the length in metres: 10
# 5     | Enter the width in metres: 5
#       | The area is 50.0 square metres
#       | The perimeter is 30.0 metres
# ----- | ------------------------------
# 3.5   | Enter the length in metres: 3.5
# 8.2   | Enter the width in metres: 8.2
#       | The area is 28.7 square metres
#       | The perimeter is 23.4 metres

length = float(input("Enter the length in metres: "))
width = float(input("Enter the width in metres: "))

print(f"The area is {(length * width):.1f} square metres")
print(f"The perimeter is {2 * (length + width):.1f} metres")