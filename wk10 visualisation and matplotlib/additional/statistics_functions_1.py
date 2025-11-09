# Functions for calculating statistics of lists
from math import sqrt
def calc_mean(numbers):
    """
    Calculate the mean (average) of a list of numbers

    Paramters
    ---------
    numbers : list
        A list of numbers.
    
    Returns
    -------
    float
        The mean value.
    """

    # mean is the sum of the numbers divided by the number of numbers
    return sum(numbers)/len(numbers)

def calc_median(numbers):
    """
    Calculate the median (middle value) of a list of numbers

    Parameters
    ----------
    numbers : list
        A list of numbers

    Returns
    -------
    float
        The median (middle value).
    """
    # take a sorted copy of the list (lists are passed by reference)
    values = sorted(numbers)

    # determine the mid-index
    mid_index = int(len(values)/2)

    # if there's an odd number of numbers
    if len(values) % 2:
        # median is the value at the mid index
        return values[mid_index]
    
def calc_mode(numbers):
    """
    Calculate the mode of a list of numbers

    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
        The mode (most common number)
    """
    # create a list to store the frequencies of each number
    frequencies = [0] * (max(numbers+1))

    # go through the list and increase the frequency for each number found
    for number in numbers:
        frequencies[number] += 1
    # identify the highest frequency
    max_frequency = max(frequencies)
    # find the index associated with the highest frequency - that's the mode 
    
    return max(frequencies, key=frequencies.get)