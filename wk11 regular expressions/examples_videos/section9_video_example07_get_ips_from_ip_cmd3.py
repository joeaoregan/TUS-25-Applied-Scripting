# Program to extract IPv4 addresses from the "ip a" command
# IP Address: 192.168.26.10
# Text output: inet 192.168.68.123/
# Regular Expression: inet (.*)/
import re
from subprocess import getoutput 

# Run the "ip a" command and store the output
output = getoutput("ip a")

# Find all the IP addresses in the output
#ips = re.findall("(\d{1,3}\.){3}\d{1,3}", output)
ips = re.findall("inet (.*)/", output) # round brackets are capturing

print(ips)


