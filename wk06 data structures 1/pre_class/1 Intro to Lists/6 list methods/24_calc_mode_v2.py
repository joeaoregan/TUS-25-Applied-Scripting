# Input a sequence of values as a string
number_string = input("Enter a sequence of values separated by spaces: ")

# start with an empty list
numbers = [] 
# Initialise the mode and max_freq
mode = None
max_freq = 0

# Process each values as we build the list
for num_str in number_string.split():
    num = int(num_str)
    numbers.append(num)
    count = numbers.count(num)
    print(f"{num=} {count=}")
    if count > max_freq:
        mode = num
        max_freq = count
        print(f"New mode: {mode=} {max_freq=}")

print(f"The mode is {mode} with a frequency of {max_freq}")