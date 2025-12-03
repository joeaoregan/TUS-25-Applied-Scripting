# Application: Simulating a User Login

username = input("Username: ")
password = input("Password: ")

while username != "jbloggs" or password != "Secret123":
    print("Invalid username or password, try again.")

    username = input("Username: ")
    password = input("Password: ")

print("Login successful")