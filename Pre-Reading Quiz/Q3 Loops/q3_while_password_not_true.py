# What's the correct way to repeat a code block until the correct username and password are entered?

# a. while username == "aladdin" or password == "open_sesame":
# b. while username != "aladdin" or password != "open_sesame": # Correct
# c. while username != "aladdin" and password != "open_sesame":
# d. while username == "aladdin" and password == "open_sesame":


username = "aladdin3"
password = "open_sesame"

while username != "aladdin" or password != "open_sesame":
    print("Access denied")
    username = input("Enter username: ")
    password = input("Enter password: ")
else:
    print("Access granted")