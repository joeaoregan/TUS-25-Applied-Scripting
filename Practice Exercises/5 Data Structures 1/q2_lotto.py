# Write a program which inputs a single string representing the numbers of a lotto quick pick, separated by spaces, and verifies that it is a valid quick pick, based on the following:
values_string = input("Enter the numbers separated by spaces: ")
numbers_list = [ int(i) for i in values_string.split() ]
# There are 6 numbers. 
valid = True
valid = len(numbers_list) == 6
# The minimum number is ≥ 1. 
valid = valid and min(numbers_list) >= 1
# The maximum number is ≤ 47. 
valid = valid and max(numbers_list) <= 47
# The numbers are unique. Hint: Use len(set(numbers)) == 6
valid = valid and len(set(numbers_list)) == 6
# The numbers are sorted in order. Hint: Use numbers == sorted(numbers)
valid = valid and numbers_list == sorted(numbers_list)

print("Valid Quickpick" if valid else "Not a valid Quickpick")
