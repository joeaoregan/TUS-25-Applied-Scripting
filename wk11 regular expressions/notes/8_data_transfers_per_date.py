# Program 8: Get Data Transfers per date from FTP xferlog file

# The xferlog file records the size (in bytes) of each file transferred, e.g:
# Tue Mar 12 09:51:02 2019 4 192.168.22.96 53108736 /srv/ftp/pub/dsl.iso b _ o a ftp 0 * c

# The following program calculates and displays the amount of data transferred 
# each day by applying a regular expression to each line of the file to capture 
# the date and filesize and storing the results in a dictionary. 

import re
import datetime

# Create an empty dictionary
transfers = {}

# Open "xferlog" as logfile
# with open("xferlog") as logfile:
with open("../examples_notes/xferlog") as logfile:
    # For each line in logfile
    for line in logfile:
        # Use a regex to search and capture the date and file size
        # data is Thu Mar 14 14:24:15 2019 0 192.168.22.153 53108736
        # The regex will match and capture the date and time (Mar 14 14:24:15 2019) and the file size (53108736)
        # match = re.search(r"([A-Z][a-z]{2} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \d+ (?:\d{1,3}\.){3}\d{1,3}\d{1,3} (\d+)", line)
        match = re.search(r"([A-Z][a-z]{2} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \d+ (?:\d{1,3}\.){3}\d{1,3} (\d+)", line)
        # match = re.search(r"([A-Z][a-z]{2} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \d+ (?:(?:\d{1,3}\.){3}\d{1,3}|localhost) (\d+)", line)

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
