# Program to extract IP addresses from a log file
# Example of regular expressions with non-capturing syntax (?:)
import re

with open("xferlog") as logfile:
    # read the entire contents as a string
    contents = logfile.read()
    
    # apply the regex to get a list of IPv4 addresses
    ip_list = re.findall(r"(?:\d{1,3}\.){3}\d{1,3}", contents)
    
    # create a dictionary representing each IP address and its frequency
    unique_ips = set(ip_list) 
    ip_dict = { ip : ip_list.count(ip) for ip in unique_ips }
    
    print(f"{'IP Address':15} Frequency")
    for ip,frequency in ip_dict.items():
        print(f"{ip:18} {frequency:>2}")
        
        

