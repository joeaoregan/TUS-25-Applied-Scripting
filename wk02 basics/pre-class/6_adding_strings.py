#  Adding Strings
 # You can add (join) two or more strings using the addition symbol:

firstname = "Joe"
lastname = "Bloggs"
name = firstname + " " + lastname
print(name)  # Joe Bloggs

# You can't add a number to a string (or vice versa).
# You have to convert the number to a string using the str() fucntion:

number = 7
response = "the lucky number is: " + str(number)
print(response)  # the lucky number is: 7