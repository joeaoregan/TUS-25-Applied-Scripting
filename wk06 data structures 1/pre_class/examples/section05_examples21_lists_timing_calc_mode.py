from time import perf_counter
from random import randint

def calc_mode1(numbers):
    # take the first number as the mode
    mode = numbers[0]
    max_freq = numbers.count(mode)
    
    # Count the frequency of all the other numbers
    for num in numbers[1:]:
        count = numbers.count(num)
        # if there's a new higher frequency
        if count > max_freq:
            # we have a new mode
            mode = num
            max_freq = count # remember its frequency
    
    return mode

def calc_mode2(numbers):
    """
    Calculate the mode of a list of numbers

    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    int
        The mode (most common number)
    """
    # create a sorted list of the unique numbers
    values = list(set(numbers))

    # create a list of the frequencies of each unique value
    frequencies = [ numbers.count(value) for value in values ]

    # identify the highest frequency
    max_freq = max(frequencies)
    # find the index associated with the highest frequency
    mode_index = frequencies.index(max_freq)
    #  return the unique value at that index - that's the mode
    return values[mode_index]

def time_calc_mode(mode_function, reps, list_size, min_value, max_value):
    start = perf_counter()     # Start the timer
    
    # Run the simulation a specified number of times
    for i in range(reps):
        numbers = [ randint(min_value, max_value) for i in range(list_size) ]
        mode_function(numbers)
    
    end = perf_counter()     # stop the timer

    return end-start


if __name__ == "__main__":
    num_sims = 100000
    list_size = 50
    min_value = 0
    max_value = 10
    
    print("Timing calc_mode1")
    duration1 = time_calc_mode(calc_mode1, num_sims, list_size, min_value, max_value)
    print(f"Time taken: {duration1:.3f} seconds for {num_sims} repetitions")
    
    
    print()
    print("Timing calc_mode2")
    duration2 = time_calc_mode(calc_mode2, num_sims, list_size, min_value, max_value)
    print(f"Time taken: {duration2:.3f} seconds for {num_sims} repetitions")