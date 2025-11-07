# A00258304

# Assuming connected contains a boolean value, which of the following is the most Pythonic way to rewrite the following code?
# if connected == False:
#     print("Failed to connect")

# a. if bool(connected) == False:
#     print("Failed to connect")

# b. if not connected: # Correct
#     print("Failed to connect")

# c. if connected is False:
#     print("Failed to connect")

# d. if connected not True:
#     print("Failed to connect")

connected = True

# if bool(connected) == False: # OK
if not connected:
# if connected is False: # OK
# if connected not True: # SyntaxError: invalid syntax
    print("Failed to connect")
