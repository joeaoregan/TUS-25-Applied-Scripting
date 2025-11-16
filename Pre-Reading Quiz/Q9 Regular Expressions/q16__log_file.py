# Q16
# Each log file of a webserver log file contains the client's IP address,
# the date and time and the file accessed, e.g.
# 83.149.9.216 - - [17/Apr/2015:10:05:03 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1"

# A Python program uses a regular expression to capture the IP address and the date separately:
# regex = re.compile(r"((?:\d{1,3}\.){3}\d{1,3}) - - \[(\d{1,2}/[A-Z][a-z]{2}/\d{4})")

# The regex is applied to each line using:
# match = re.search(regex,line)

# Which of the following displays the matched string? (there are 2 correct answers, just select one)
# Question 16Answer

# a.
# match.group()

# b.
# match.group(2)

# c.
# match.group(1)

# d.
# match.group(0)

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

regex = re.compile(r"((?:\d{1,3}\.){3}\d{1,3}) - - \[(\d{1,2}/[A-Z][a-z]{2}/\d{4})")

with open("q16webserverlog") as logfile:
    for line in logfile:
        match = re.search(regex,line)
        
        if match:
            # print(match.group(0)) # this
            print(match.group()) # and this
            # datetime_object = datetime.datetime.strptime(match.group(2), "%d/%b/%Y %H:%M:%S")
            datetime_object = datetime.datetime.strptime(match.group(2), "%d/%b/%Y")
            date_object = datetime_object.date()
            
            if date_object not in transfers:
                transfers[date_object] = match.group(1)
            else:
                transfers[date_object] += match.group(1)

# Display the amount transferred by date
print(f"{'Date':10} Amount Transferred (Bytes)")
for date_object,size in transfers.items():
    print(f"{date_object} {size:>10}")


