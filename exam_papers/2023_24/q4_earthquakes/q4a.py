import re

while True:
    id = input("Enter earthquake id (q to quit): ")
    if id == 'q':
        break
    match = re.fullmatch(r"[a-z]{2}\d{4}[0-9a-z]*",id)

    if match:
        print("Valid id")
    else:
        print("Invalid id")