import re

regex = re.compile(r"[a-z]{2}[0-9]{4}[0-9a-z]*")

while True:
    earthquake_id = input("Enter the Earthquake ID or q to quit: ")
    if earthquake_id == "q":
        break

    match = re.fullmatch(regex, earthquake_id)

    if match:
        print("Valid Earthquake ID")
    else:
        print("Not a valid Earthquake ID")