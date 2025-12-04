# Program to calculate the mode, version 2 using a single for loop
# Example of: lists, iteration, counting

# Input a sequence of values as a string
number_string = input("Enter a sequence of values separated by spaces: ")

# Start with an empty list
numbers = []
# initialise the mode and max_freq
mode = None
max_freq = 0

# Process each value as we build the list
for num_str in number_string.split():
    num = int(num_str)
    numbers.append(num)               # build the list
    count = numbers.count(num)        # count frequencies so far
    print(f"{num=} {count=}")
    if count > max_freq:              # check if it's the new mode
        mode = num
        max_freq = count
        print(f"New mode: {mode=} {max_freq=}")

print(f"The mode is {mode} with a frequency of {max_freq}")

