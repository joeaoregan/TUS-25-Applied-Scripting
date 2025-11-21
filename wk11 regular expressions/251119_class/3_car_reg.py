# 19-35ish
import re
# Create an empty dictionary to store the Registration Numbers and distances
cars_dict = {}
# Compile a regular expression to match the Registration Number, the Year and the
# Distance Driven, and capture the Registration Number and the Distance Driven.

# Open the file
with open('cardata.txt') as data_file:
    # For each line of the file
    for line in data_file:
        # Maruti 800 AC 07-TN-55334 2007 100000
        # Use the compiled regular expressoin to search the current line for a match.
        result = re.search(r"(\d{2}-[A-Z]{1,2}-\d{1,6}) \d{4} (\d+)", line)
        # If a match was found, insert the Registration Number and the distance into the
        # dictionary.
        if result:
            # print(result.group(1), result.group(2)) # reg, miles
            cars_dict[result.group(1)] = int(result.group(2))


# Determine and display the Registration Number with the highest distance.
print("Car with highest distance:", max(cars_dict, key=cars_dict.get))
