import re

users = {}

# with open("quota_exceeded.log") as data_file:
with open("quota_exceeded.log") as data_file:
    for line in data_file:
        result = re.search(r"[a-z][-a-z0-9_]*(\s\d+)", line)

        users[result.group(1)] = int(result.group(2))

        print(f"Username with the highest amount exceeded: {max(users,key=users.get)}")