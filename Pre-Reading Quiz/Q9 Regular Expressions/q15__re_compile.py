# Q15
# A Python program has compiled the regex [a-z][-a-z0-9_]* using the code
# regex = re.compile("[a-z][-a-z0-9_]*")

# The program is processing each line of a file, and needs to find 
# the first valid username on the line.

# What is the correct code to do this?
import re

# a.
# re.match(regex, line) # must be at start of string
# b.
# re.findall(regex, line) # finds all valid
# c.
re.search(regex, line) # this
# d.
# re.fullmatch(regex, line) # must match full string

