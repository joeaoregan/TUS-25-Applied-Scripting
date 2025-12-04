# Purpose: to process web hits
# Example of: lists, list functions and appending to a list

# Start with an empty list
webhits = []

# Input number of values
num_values = int(input("How many values? "))

# repeat until all values are input
for i in range(num_values):
    value = int(input("Enter the value: "))    
    webhits.append(value) # add it to the list

# Precompute values
count = len(webhits)
total = sum(webhits)
minimum = min(webhits)
maximum = max(webhits)
average = total / count
dispersion = maximum - minimum
webhits.sort() # sort the list in place

# Display the results using f-strings
print(f"Number of values is {count}")
print(f"The values in order are {webhits}")
print(f"The total number of hits is {total}")
print(f"The average number of hits is {average:.1f}")
print(f"The minimum number of hits is {minimum}")
print(f"The maximum number of hits is {maximum}")
print(f"The dispersion is {dispersion}")

