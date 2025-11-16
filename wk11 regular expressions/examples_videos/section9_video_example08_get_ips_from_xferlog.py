# Program to extract IPv4 addresses from the xferlog
# IP Address: 192.168.26.10
# Regular Expression: (\d{1,3}\.){3}\d{1,3}
import re

# open the file for reading
with open("xferlog") as logfile:
    # read in the contents of the file as a string
    contents = logfile.read()
    
    # Find all the IP addresses in the output
    ips = re.findall("(?:\d{1,3}\.){3}\d{1,3}", contents)
    
    # get the unique ip addresses
    unique_ips = set(ips)
    # create a dictionary with the ips and their frequencies
    ip_dict = { ip : ips.count(ip) for ip in unique_ips }
    
    print(f"{'IP Address':15} Frequency")
    for ip,frequency in ip_dict.items():
        print(f"{ip:18} {frequency:>2}")



