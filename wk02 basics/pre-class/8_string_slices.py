# String Slices
# You can take a slice of a string using the syntax:
# variable[start:end]
message = "Hello World"
print(message[3:8])  # lo Wor
print(message[0:5])  # Hello
print(message[6:11]) # World
print(message[6:])   # World
print()

#  Omitting both start and end values returns a copy of the entire string:
print(message[:])    # Hello World
print()

# step counting
# select every nth item from the start index up to and not 
# including the end index, using the syntax: 
# variable[start:end:step], for example

message[1:10:2] # selects every second character from index 1 to 9
print(message[1:10:2])  # el ol
print(message[2::3])    # l r
print(message[:9:2])    # HloWr
print()

# Negative index
#  You can use a negative index to work from the end of the string:
message = "hello world"
print(message[-1])      # d
print(message[-2])      # l
print(message[6:-2])    # wor
print()

# reverse
# You can use therefore use the slice syntax [::-1] 
# to return a copy of the string in reverse:

message = "hello world"
print(message[::-1])    # dlrow olleh

# message[::-1] is the same message[0:11:-1] which means 
# return a slice of the original string 
# from index 0 (the start) to the end of the string 
# (i.e. the entire string), stepping backwards from 
# the end, one character at a time