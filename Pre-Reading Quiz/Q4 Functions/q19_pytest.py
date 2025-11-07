# The function calc_area calculates and returns the area of a rectangle. It takes two parameters, length and width, and returns the area (by multiplying the length and width).

# Which of the following is the correct PyTest test code? (Assume pytest has been imported).

# a. assert calc_area == length*width
# b. assert calc_area(0.1,0.2) = 0.02
# c. assert calc_area() = 0.02
# d. assert calc_area(0.1,0.2) = pytest.approx(0.02,rel=1e-4) # Correct

from pytest import approx

def calc_area(length, width):
    return length * width

# assert calc_area(0.1,0.2) = pytest.approx(0.02,rel=1e-4)
assert calc_area(0.1,0.2) == approx(0.02,rel=1e-4)