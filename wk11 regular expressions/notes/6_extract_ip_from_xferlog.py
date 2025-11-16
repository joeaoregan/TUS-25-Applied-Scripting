# To specify that the round brackets should not capture the matching text contained within them and so the 
# regex will return the full IP address, use the syntax: (?:regex)
# e.g.:  (?:\d{1,3}\.){3}\d{1,3}

#  Program 6: Extract IP addresses from FTP xferlog file

# The file xferlog contains details of file transfers to and from an FTP server.  
# Each line corresponds to a single request, e.g.
# Tue Mar 12 09:53:41 2019 0 192.168.22.115 /srv/ftp/pub/dsl.iso b _ o a A00777981 ftp 0 * c

# Each line records:
# The date and time of the file transfer    e.g. Tue Mar 12 09:53:41 2019
# The IP address of the client              e.g. 192.168.22.115
# The size of the file in bytes,            e.g. 53108736
# The path of the file,                     e.g. /srv/ftp/pub/dsl.iso
# The username associated with the transfer e.g. A00777981

# The following program
#  • Opens the file xferlog
#  • Reads in its entire contents as a string
#  • Uses a regex to create a list of all IPv4 addresses re.findall(regex,contents)
#  • Creates a dictionary containing each unqiue IP address and the number of times 
#    it appears in the file (its frequency)
#  • Displays each unique IP address and its frequency


# Program to extract IP addresses from a log file
# Example of regular expressions with non-captureing syntax (?:)
import re

# with open("xferlog") as logfile:
with open("../examples_notes/xferlog") as logfile:
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