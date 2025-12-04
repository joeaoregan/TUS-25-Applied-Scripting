# Purpose: to process web hits in a list
# Example of: lists and list functions
# Version 1: simple, but inefficient

# Create the list and initialise it using the values
webhits = [859, 1257, 724, 1003, 982, 672, 598]

# Display the number of values in the list
print(f"Number of values is {len(webhits)}")

# Display the values SORTED in order
print(f"The values in order are {sorted(webhits)}")

# Display the total (SUM) of the values
print(f"The total number of hits is {sum(webhits)}")

# Calculate and display the average SUM/LEN
print(f"The average number of hits is {sum(webhits)/len(webhits):.1f}")

# Display the MINimum
print(f"The minimum number of hits is {min(webhits)}")

# Display the MAXimum
print(f"The maximum number of hits is {max(webhits)}")

# Display the dispersion (MAX - MIN)
print(f"The dispersion is {max(webhits) - min(webhits)}")

