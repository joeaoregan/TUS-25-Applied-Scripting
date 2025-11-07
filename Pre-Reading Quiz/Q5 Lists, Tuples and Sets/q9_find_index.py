# What is the correct code to determine the location of the value of the variable random_number in the all_numbers list?

all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

random_number = 7

# a.
print(all_numbers.index(random_number))

# b.
# random_number.find(all_numbers) # AttributeError: 'int' object has not attribute 'find'

# c.
# random_number.index(all_numbers) # AttributeError: 'int' object has not attribute 'index'

# d.
# all_numbers.find(random_number) # AttributeError: 'list' object has no attribute 'find'