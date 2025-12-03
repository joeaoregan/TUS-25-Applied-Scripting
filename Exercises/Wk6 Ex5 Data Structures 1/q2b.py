
valid = True

# numbers_string = input("Enter the numbers separated by spaces: ")
numbers_string = "1 5 10 15 20 25"
numbers = [int(number) for number in numbers_string.split()]

for number in numbers:
    if number < 1 or number > 47:
        valid = False
        break

if len(set(numbers)) != 6:
    valid = False

if len(numbers) != len(set(numbers)):
    valid = False

if numbers != sorted(numbers):
    valid = False

print("Valid Quickpick" if valid else "Not a valid Quickpick")