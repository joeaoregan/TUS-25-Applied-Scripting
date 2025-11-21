# A00258304
import re

def check_ppsn(ppsn):
    format_2012 = r"\d{7}[a-zA-Z]"
    # ppsn = "4567433L"

    if re.fullmatch(format_2012, ppsn):
        # print("Valid PPSN up to 2012")
        return "Valid PPSN up to 2012"
    else:
        # print("Not a valid PPSN or SWIN")
        return "no"

try:
    assert check_ppsn("4567432L") == "Valid PPSN up to 2012", "No"
    print("Valid PPSN up to 2012")
except AssertionError as e:
    print(e)