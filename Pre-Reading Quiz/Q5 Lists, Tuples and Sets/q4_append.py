my_numbers = [1, 2, 3]
number = 4

print(my_numbers)
# a.
# my_numbers = my_numbers + number # TypeError

# b.
# my_numbers += number # TypeError: 'int' object is not iterable

# c.
# my_numbers.add(number) # AttibuteError: 'list' object has no attribute 'add'

# d.
my_numbers.append(number)
print(my_numbers)