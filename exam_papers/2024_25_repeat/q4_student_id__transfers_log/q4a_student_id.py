import re

id = "X1234568"
id = "BC123456A"

match = re.fullmatch(r"[A-Z]{1,2}[\d]{6}[a-zA-Z\d]{1}", id)

if match:
    print("valid id")
else:
    print("invalid id")