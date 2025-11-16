# Program to get the IP address from the ip a / ipconfig command
# Example of capturing using regular expressions

# Modified to check platform 

import re
from subprocess import getoutput
from sys import platform

# Run the ip a command and get the output
if platform == "linux" or platform == "linux2":
    output = getoutput("ip a") # linux
    # Look for a match using the regex
    ip_list = re.findall("inet (.*)/", output)
elif platform == "win32":
    output = getoutput("ipconfig") # windows
    # Look for a match using the regex
    ip_list = re.findall("IPv4 .*: (.*)", output)

# Display the list of ip addresses found
print("List of IP Addresses")
for ip_address in ip_list:
    print(ip_address)