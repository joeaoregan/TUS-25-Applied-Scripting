# Q 4(b) [16 Marks]
# The file access.log is a web server log file containing information on client requests.  Each line of the 
# file corresponds to a single request, and includes the following information:
#         ...FilenameStatusAmount ...
# e.g.    ... index.php 200 9873
#         ... local.xml 404 223
 
# Status is a three-digit Status code; Amount is the amount transferred in bytes (an integer).  The character  
# indicates a space separating the components on the line.

# (i)
#  Write a Python program which uses a regular expression and a dictionary to determine and 
# display the Filename with the highest amount transferred in a single request, and the 
# corresponding amount, as follows:
#  • Create an empty dictionary to store each Filename and the associated amount
#  • Compile a single regular expression to represent the Filename, the Status code and the Amount, 
# separated by a single space, and capture the Filename and Amount separately.
#  • Open the access.log file
#  • For each line of the file:
#  ◦Apply the compiled regular expression to the current line, and store the result.
#  ◦If the result contains a match, insert the Filename and the Amount into the dictionary.
#  • Determine and display the Filename with the highest amount transferred, and the associated 
# amount.

import re

filenames = {}
regex = re.compile(r"(\w+\.\w{1,4}) (\d{3}) (\d+)")

# with open("access.log") as logfile:
with open("./exam_papers/2024_25_summer/question_4/access.log") as logfile:
    for line in logfile:
        match = regex.search(line)

        if match:
            # print(match.group(1), match.group(2), match.group(3))
            filenames[match.group(1)] = filenames.get(match.group(1), 0) + int(match.group(3))
            # if match.group(1) not in filenames:
            #     filenames[match.group(1)] = int(match.group(3))


# print(filenames)
print(f"Filename {max(filenames,key=filenames.get)} had the highest amount transferred {filenames[max(filenames,key=filenames.get)]} (bytes)")