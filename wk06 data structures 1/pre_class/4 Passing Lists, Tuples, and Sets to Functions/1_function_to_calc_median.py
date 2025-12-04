# Example: Function to calculate the median

def calc_median(numbers):
    # sort the list
    numbers.sort()

    # determine the mid-index
    mid_index = int(len(numbers)/2)

    # if theres's an odd number of numbers
    if len(numbers) % 2 == 1: # remainder after dividing by 2
        # median is the value at the mid index
        return numbers[mid_index]
    else: # otherwise there's an even number of nnumbers
        return (numbers[mid_index-1] + numbers[mid_index]) / 2
    
if __name__ == "__main__":
    webhits = [859, 1257, 724, 1003, 982, 672, 598]
    print(webhits)

    print(f"Median is {calc_median(webhits)}")

    print(webhits) # sorted - passed by reference to function