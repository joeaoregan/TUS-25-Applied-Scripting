# A function is_server_up() takes a single string parameter representing a server's id and returns True if the server is "up", False otherwise.
# With the server "localhost", the function should return True.

# Which of the following is the correct, Pythonic, PyTest test code for this?

# a. assert is_server_up("localhost")
# b. assert is_server_up("localhost") == True
# c. assert not is_server_up("localhost")
# d. assert not is_server_up("localhost") == False

def is_server_up(id):
    if id == "localhost":
        return True
    return False

assert is_server_up("localhost")