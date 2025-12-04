# Start with a list of values
# webhits = [859, 1257, 724, 1003, 982, 672, 598] # odd number of values (7)
webhits = [859, 1257, 724, 1003, 982, 672]

# Display the number of values in the list
print("Number of values is", len(webhits))

# created a sorted copy of the list
sorted_numbers = sorted(webhits)
print(f"The values in order are {sorted_numbers}")

# Calculate the index of the middle value
mid_index = int(len(sorted_numbers)/2)

# Calculate and display the median value
if len(webhits) % 2 == 1: # odd number of values
    median = sorted_numbers[mid_index]
else: # even number of values
    median = (sorted_numbers[mid_index-1] + sorted_numbers[mid_index]) /2

print(f"Median value is: {median}")