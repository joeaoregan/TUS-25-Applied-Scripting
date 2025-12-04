# Example: Using a set to calculate the mode

# Input a sequence of values as a string
# number_string = input("Enter a sequence of values separated by spaces: ")
number_string = "6 3 9 6 6 5 9 3"

# Turn the input sequence into a list of numbers using list comprehension
numbers = [int(num) for num in number_string.split()]

# Create a sorted list of the unique numbers using a set
values = sorted(set(numbers))
print(values)

# create a list of the frequencies of each unique value using list comprehension
frequencies = [numbers.count(value) for value in values]
print(frequencies)

# identify the highest frequency
max_freq = max(frequencies)
# find the index associated with the highest frequency
mode_index = frequencies.index(max_freq)
# get the value at that index - that's the mode
mode = values[mode_index]

print(f"The mode of the numbers is: {mode}")