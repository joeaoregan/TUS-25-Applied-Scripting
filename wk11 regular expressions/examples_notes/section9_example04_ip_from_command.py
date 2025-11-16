# Program to get the IP address from the ip a command
# Example of capturing using regular expressions
import re
from subprocess import getoutput

# Run the ip a command and get the output
output = getoutput("ip a")

# Look for a match using the regex
ip_list = re.findall("inet (.*)/", output)

# Display the list of ip addresses found
print("List of IP Addresses")
for ip_address in ip_list:
	print(ip_address)
	

	
