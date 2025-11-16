# Program to extract IPv4 addresses from the "ip a" command
# IP Address: 192.168.26.10
# Regular Expression: \d{1,3}\.\d{1,3}.\d{1,3}\.\d{1,3}
import re
from subprocess import getoutput 

# Run the "ip a" command and store the output
output = getoutput("ip a")

# Find all the IP addresses in the output
ips = re.findall("\d{1,3}\.\d{1,3}.\d{1,3}\.\d{1,3}", output)

print(ips)


