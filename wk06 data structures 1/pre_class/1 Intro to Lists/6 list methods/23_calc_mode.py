# Input a sequence of values as a string
number_string = input("Enter a sequence of values separated by spaces: ")

# Turn the input sequence into a list of numbers
numbers = [] # start with an empty list
for num in number_string.split():
    numbers.append(int(num))

# take the first number as the mode
mode = numbers[0]
max_freq = numbers.count(mode)
print(f"{mode=} {max_freq=}")

# Count he frequency of all the other numbers
for num in numbers[1:]:
    count = numbers.count(num)
    print(f"{num=} {count=}")
    # if there's a new higher frequency
    if count > max_freq:
        # we have a new mode
        max_freq = count
        mode = num
        print(f"New mode: {mode=} {max_freq=}")

print(f"The mode is {mode} with a frequency of {max_freq}")