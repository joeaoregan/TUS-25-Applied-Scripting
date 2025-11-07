# A00258304

# Which of the following statements is the correct way to then check if the total is equal to 2, 3 or 12:

# a. if total == 2 == 3 == 12:
# b. if total == 2 or 3 or 12: # Also works, but not correct
# c. if total is 2, 3 or 12:
# d. if total == 2 or total == 3 or total == 12: # Correct

total = 12

# if total == 2 == 3 == 12:
#     print("total:",total) # skips

# if total == 2 or 3 or 12:
#     print("Total:",total)

# if total is 2, 3 or 12: # SyntaxError: invalid syntax
#     print("Total:",total)

if total == 2 or total == 3 or total == 12:
    print("total:",total)