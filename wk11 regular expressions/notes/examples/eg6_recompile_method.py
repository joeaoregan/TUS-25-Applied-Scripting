# Using the re.compile() method for Efficiency
# In the previous example, the same regular expression was applied to each line of the file:
# match = re.search(r"([A-Z][a-z]{2} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \d+ (?:\d{1,3}\.){3}\d{1,3} (\d+)", line)

# Python has to interpret the regular expression each time it is applied.
# A more efficient approach is to compile the regex which saves if for future repeated use.

# The regex is saved as an re.Pattern object.
# It can then be used to apply the regex to each line of the file, without having to re-interpret it each time.
# The output is the same as before.

# It is recommended to use re.compile() whenever you need to apply the same regex multiple times in a program.

import re
import datetime

# Create an empty dictionary
transfers = {}

regex = re.compile(r"([A-Z][a-z]{2} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \d+ (?:\d{1,3}\.){3}\d{1,3} (\d+)")

# Open "xferlog" as logfile
with open("../examples_notes/xferlog") as logfile:
    # For each line in logfile
    for line in logfile:
        # apply the previously compiled regex
        match = regex.search(line)

        if match:
            # create a datetime object from the date time string
            datetime_object = datetime.datetime.strptime(match.group(1), "%b %d %H:%M:%S %Y")
            # extract the date part of the datetime object
            date_object = datetime_object.date()

            # print(match.group(1))

            # If this is the first occurrence of the date
            if date_object not in transfers:
                # Insert the date into the dictionary with the file size
                transfers[date_object] = int(match.group(2))
            else:
                # Add the size onto the existing value for the date
                transfers[date_object] += int(match.group(2))

# Display the amount transferred by date
print(f"{'Date':10} Amount Transferred (Bytes)")
for date_object,size in transfers.items():
    print(f"{date_object} {size:>10}")