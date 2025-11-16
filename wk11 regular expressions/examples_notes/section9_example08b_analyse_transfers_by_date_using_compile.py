# Program to calculate and display the data transferred each date
# Version 2: uses re.compile() to save the regex for repeated use

# Import the modules
import re
import datetime

# Create an empty dictionary
transfers = {}

# Use a regex to search and capture the date and file size
# data is Thu Mar 14 14:24:15 2019 0 192.168.22.153 53108736
# The regex will match and capture the date and time (Mar 14 14:24:15 2019) and the filesize (53108736)
regex = re.compile(r"([A-Z][a-z]{2} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \d+ (?:\d{1,3}\.){3}\d{1,3}\d{1,3} (\d+)")

# Open “xferlog” as logfile
with open("xferlog") as logfile:
    # For each line in logfile
    for line in logfile:
        # apply the previously compile regex
        match = regex.search(line)
        
        if match:
            # create a datetime object from the date and time string
            datetime_object = datetime.datetime.strptime(match.group(1), "%b %d %H:%M:%S %Y")
            # extract the date part of the datetime object
            date_object = datetime_object.date()
            
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


