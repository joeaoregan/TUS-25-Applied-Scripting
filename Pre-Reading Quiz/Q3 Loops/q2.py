# What is the correct code to check if the user has entered an incorrect username or password?

# a. if username != "aladdin" or password != "open_sesame": # Correct
# b. if username != "aladdin" and password != "open_sesame":
# c. if username == "aladdin" or password == "open_sesame":
# d. if username == "aladdin" and password == "open_sesame":

username = "aladdin"
password = "open_sesame"

if username != "aladdin" or password != "open_sesame":
    print("Access denied")
else:
    print("Access granted")

# if username != "aladdin" and password != "open_sesame":
# if username == "aladdin" or password == "open_sesame":
# if username == "aladdin" and password == "open_sesame":