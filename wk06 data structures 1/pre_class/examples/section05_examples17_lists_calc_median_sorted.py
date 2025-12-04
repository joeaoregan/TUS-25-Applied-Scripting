def calc_median(numbers):
    """
    Calculate the median (middle value) of a list of numbers

    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    float
        The median (middle value)
    """
    # take a sorted copy of the list (lists are passed by reference)
    values = sorted(numbers) # NOT numbers.sort()

    # determine the mid-index
    mid_index = int(len(values)/2)

    # if there's an odd number of numbers
    if len(values) % 2 == 1: # remainder after dividing by 2 
        # median is the value at the mid index
        return values[mid_index]
    else: # otherwise there's an even number of numbers
        return (values[mid_index-1] + values[mid_index])/2

if __name__ == "__main__":
    webhits =  [859, 1257, 724, 1003, 982, 672, 598]
    print(f"Median is {calc_median(webhits)}")