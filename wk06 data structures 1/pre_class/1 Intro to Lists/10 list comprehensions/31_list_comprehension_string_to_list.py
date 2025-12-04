#  Example: Converting a string containing a sequence of numbers into a list of numbers

number_string = '3 9 5 6 6 9 3 6'
numbers = []
for num in number_string.split():
    numbers.append(int(num))
print(f"{numbers=}")

number_string = '3 9 5 6 6 9 3 6'
numbers = [int(value) for value in number_string.split()]
print(f"{numbers=}")
