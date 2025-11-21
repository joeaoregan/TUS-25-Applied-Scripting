# A00258304
import re

ppsn = input("Enter the PPSN/SWIN: ")

format_2012 = r"\d{7}[a-zA-Z]"
format_2013 = r"\d{7}[a-zA-Z]{2}"
# format_swin = r"\d{6}[a-zA-Z]{,1}"
format_swin = r"\d{6}[a-zA-Z]?"

if re.fullmatch(format_2013, ppsn):
    print("Valid PPSN 2013-present")
elif re.fullmatch(format_2012, ppsn):
    print("Valid PPSN up to 2012")
elif re.fullmatch(format_swin, ppsn):
    print("Valid SWIN pre-1979")
else:
    print("Not a valid PPSN or SWIN")
    
