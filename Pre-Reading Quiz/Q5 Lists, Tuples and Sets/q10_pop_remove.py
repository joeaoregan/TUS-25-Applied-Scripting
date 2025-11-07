# What is the correct code to remove the value of the variable random_number at location index frmo the all_numbers list and store it in the variable new_number?

# all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
all_numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

index = 7
random_number = 7

# a.
new_number = all_numbers.pop(index) # this

# b.
# new_number = all_numbers.pop(random_number) # same?

# c.
# new_number = all_numbers.remove(random_number) # Removes 7, but returns None

# d.
# new_number = all_numbers.remove(index) # Removes 7, but returns None

print(all_numbers)
print(new_number)