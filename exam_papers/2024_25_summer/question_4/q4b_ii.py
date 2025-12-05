# Q 4(b) [16 Marks]
# The file access.log is a web server log file containing information on client requests.  Each line of the 
# file corresponds to a single request, and includes the following information:
#         ...FilenameStatusAmount ...
# e.g.    ... index.php 200 9873
#         ... local.xml 404 223
 
# Status is a three-digit Status code; Amount is the amount transferred in bytes (an integer).  The character  
# indicates a space separating the components on the line.

# (ii)
# Write a Python program which uses a regular expression and a dictionary to determine and 
# display the frequencies of the Status codes in the file, as follows:
#  • Open the access.log file
#  • Read in the entire contents of the file
#  • Use a regular expression to find every Status code (after the filename) in the contents and capture 
# them; this returns a list of the Status codes.
#  • Determine the frequency of each Status code in the list and assign the Status code and its 
# frequency to a dictionary.
#  • Display each Status code and the corresponding frequency, sorted in order by Status code.

import re

freq = {}
regex = re.compile(r" (\d{3}) ")

with open("access.log") as logfile:
    contents = logfile.read()

    code_list = regex.findall(contents)

    for code in code_list:
        freq[code] = freq.get(code, 0) + 1
  
print("Code Frequency")
for code in sorted(freq):
    print(f"{code} {freq[code]:9}")