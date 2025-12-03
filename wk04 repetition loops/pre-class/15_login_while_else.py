import sys

count = 0

while count < 3:
    username = input("Username: ")
    password = input("Password: ")

    if username == "jbloggs" and password == "Secret123":
        print("Login successful")
        break
    else:
        print("Login failed")
        count += 1
else:
    print("Too many failed attempts")
    sys.exit()

print("\nWelcome")