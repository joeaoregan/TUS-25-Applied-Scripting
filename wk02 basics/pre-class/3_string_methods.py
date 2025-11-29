str = "test"

print(str.endswith("est")) # True
print(str.endswith("tes")) # False

print(str.isalpha())  # True
print(str.isalnum())  # True
print(str.isdigit())  # False

print(str.islower())  # True
print(str.isupper())  # False

print(str.isspace())  # False

print(str.startswith("te"))  # True
print(str.startswith("est"))  # False

print(str.capitalize())  # Test
print(str.upper())       # TEST
print(str.lower())       # test

print(str.split("e"))   # ['t', 'st']
print(str.strip("t"))   # 'es'
print(str.swapcase())   # TEST
print(str.title())      # Test
print(str.upper())      # TEST
print()

message = "hello world"
print(message.capitalize())
print(message.title())
print(message.upper())
print(message.lower())
print(message.swapcase())
print()

# The above methods return a new string, 
# they don't change the original string, e.g.:
message = "Hello World"
message.lower() # This does not change message
print(message)

message = "Hello World"
message = message.lower() # This changes messages
print(message)

