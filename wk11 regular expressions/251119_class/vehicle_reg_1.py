import re

# LLL SSSS
regex = "[A-Z]{2,3} \d{1.4}"

# YY-CC-SSSSSS
regex2 = "\d{2]-[A-Z]{1,2}-\d{1,6}}"

# YYH-CC-SSSSSS
regex3 = "\d{3}-[A-Z]{1,2}-\d{1,6}" # first digit has to be a 1 or 2, Cormac will fix after class
# regex3 = "\d{2}[12]-[A-Z]{1,2}-\d{1,6}"
