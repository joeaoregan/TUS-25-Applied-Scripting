# A00258304

# A username must have between 4 and 8 characters (inclusive).

# Which of the following is not the correct code for a condition to the check if the value of username contains a suitable number of characters?

# Hint: If you find this a bit confusing, try it out in the interactive Python interpreter with different lengths of username, 
# e.g. valid ones like "root", "joseph", "jbloggs" (3 of the answers should return True, and the incorrect answer should return False), 
# and try invalid usernames such as "joe", "josephbloggs" and again check which answers correctly return False)

# a. len(username) >=4 and len(username) <= 8 # OK
# b. len(username) >= 4 or len(username) <= 8 # Correct
# c. 4 <= len(username) <=8 # OK
# d. not len(username) < 4 and not len(username) > 8 # OK

username = "root"
username = "joseph"
username = "jbloggs"

username = "joe"
username = "josephbloggs"

# print(len(username) >= 4 and len(username) <= 8) # between 4 and 8 inclusive

print(len(username) >= 4 or len(username) <= 8) # True for all test cases

# print(4 <= len(username) <=8)

# print(not len(username) < 4 and not len(username) > 8)