#  Example Program: Simplistic User Login, Version 2 - Max 3 Attempts

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

if count == 3:
    print("Too many failed attempts")
    sys.exit()

print("\nWelcome")