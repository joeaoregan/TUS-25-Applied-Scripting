# Q14
# A Python program has read in the contents of a file and needs to extract 
# all valid usernames from it.

# Which of the following is the correct code to do this?
import re

regex = "^[a-z][-a-z0-9_]*$"

username = "a-az19_"

match = re.findall("[a-z][-a-z0-9_]*", contents)
# b.
# match = re.search("[a-z][-a-z0-9_]*", contents) # finds first instance
# c.
# match = re.fullmatch("[a-z][-a-z0-9_]*", contents) # match wholestring
# d.
# match = re.match("[a-z][-a-z0-9_]*", contents) # start of string




