# Program to extract IPv4 addresses from the xferlog
# IP Address: 192.168.26.10
# Regular Expression: (\d{1,3}\.){3}\d{1,3}
import re

ips_dict = {}

# open the file for reading
with open("xferlog") as logfile:
    # for each line in the file
    for line in logfile:
        # Find all the IP addresses in the output
        match = re.search("((?:\d{1,3}\.){3}\d{1,3}) (\d+)", line)
    
        if match: 
            ip = match.group(1) 
            size = int(match.group(2))
            if ip in ips_dict:
                ips_dict[ip] += size
            else:
                ips_dict[ip] = size
                
    
    print("Number of IP addresses:", len(ips_dict))


