# Program to calculate the mode of a list of numbers
# Version 2a: using a sorted set to get the unique values

# Input a sequence of values as a string
number_string = input("Enter a sequence of values separated by spaces: ")

# Turn the input sequence into a list of numbers using list comprehension
numbers = [ int(num) for num in number_string.split() ]

# create a sorted list of the unique numbers using a set
values = sorted(set(numbers))

# create a list of the frequencies of each unique value using list comprehension
frequencies = [ numbers.count(value) for value in values ]

# identify the highest frequency
max_freq = max(frequencies)
# find the index associated with the highest frequency
mode_index = frequencies.index(max_freq)
# get the value at that index - that's the mode
mode = values[mode_index]

print(f"The mode of the numbers is: {mode}")

