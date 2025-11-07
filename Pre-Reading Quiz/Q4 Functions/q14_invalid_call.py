# Which of the following is not a valid way to call the calc_dimensions function?

# a. results = calc_dimensions()
# b. length, width, height = calc_dimensions() # Correct
# c. length, width = calc_dimensions()
# d. calc_dimensions()

def calc_dimensions():
    lenght = 3
    width = 4
    return lenght, width

length, width, height = calc_dimensions() # ValueError: not enough values to unpack (expected 3, got 2)