# Program to calculate the mode
# Example of: lists, iteration, counting

# Input a sequence of values as a string
number_string = input("Enter a sequence of values separated by spaces: ")

# Turn the input sequence into a list of numbers using list comprehenion
numbers = [ int(num) for num in number_string.split() ]

# take the first number as the mode
mode = numbers[0]
max_freq = numbers.count(mode)
print(f"{mode=} {max_freq=}")

# Count the frequency of all the other numbers
for num in numbers[1:]:
    count = numbers.count(num)
    print(f"{num=} {count=}")
    # if there's a new higher frequency
    if count > max_freq:
        # we have a new mode
        mode = num
        max_freq = count # remember its frequency
        print(f"New mode: {mode=} {max_freq=}")

print(f"The mode is {mode} with a frequency of {max_freq}")

