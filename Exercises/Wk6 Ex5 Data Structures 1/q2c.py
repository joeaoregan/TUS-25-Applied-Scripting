valid = True

# numbers_string = input("Enter the numbers separated by spaces: ")
numbers_string = "5 10 15 20 25 30 "
numbers = [int(number) for number in numbers_string.split()]

for number in numbers:
    valid = 1 <= number <= 47
    if not valid: break

valid = valid and len(set(numbers)) == 6
valid = valid and len(numbers) == len(set(numbers))
valid = valid and numbers == sorted(numbers)

print("Valid Quickpick" if valid else "Not a valid Quickpick")