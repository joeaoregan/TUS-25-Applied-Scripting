# Capturing Matches

# Round bradckets () can be used to "capture" matches.
# that means you can store part of the string matched by the regular expression.

# The Linux command "ip a" displays the info. associated with network interfaces.

# The regex: inet(.*)/
# matches the lines containing the word "inet" followed by any number of characters (the IP address),
# followed by a forward slash /, and uses the roudn brackets () to capture the IP address.

# The method re.findall() returns a list of all match captured by the regex.
# ip_list = re.findall("inet (.*)/", output)
# e.g.: ['127.0.0.1', '192.168.0.26']


# Program 4: Extracting the IP Address from command-line output

# Program to get the IP address from the ip a / ipconfig command
# Example of capturing using regular expressions
import re
from subprocess import getoutput

# Run the ip a command and get the output
# output = getoutput("ip a") # linux
output = getoutput("ipconfig") # windows

# Look for a match using the regex
# ip_list = re.findall("inet (.*)/", output) # linux
ip_list = re.findall("IPv4 .*: (.*)", output) # windows

# Display the list of ip addresses found
print("List of IP Addresses")
for ip_address in ip_list:
    print(ip_address)