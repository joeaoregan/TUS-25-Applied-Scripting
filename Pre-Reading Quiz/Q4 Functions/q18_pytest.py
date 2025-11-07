# The function calc_area calculates and returns the area of a rectangle. It takes two parameters, length and width, and returns the area (by multiplying the length and width).

# Which of the following is the correct PyTest test code?

# a. assert calc_area == length*width
# b. assert calc_area(4,5) = 20
# c. assert calc_area() = 20
# d. assert calc_area(4,5) == 20 # Correct

def calc_area(length, width):
    return length * width

assert calc_area(4,5) == 20