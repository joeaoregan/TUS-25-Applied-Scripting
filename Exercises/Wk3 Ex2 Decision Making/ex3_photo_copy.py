# A00258304

# A photo-copying centre charges 5c per copy for first 100 copies and 
# 3c per copy for each additional copy.

# Write a program to input the number of copies required, and then 
# calculate and display the cost of the photo-copying to 2 decimal places.

# Example:

# Input | Result
#-------|-----------------------------
# 50    | Enter number of copies: 50
#       | Cost is 2.50
#-------|-----------------------------
# 100   | Enter number of copies: 100
#       | Cost is 5.00
#-------|-----------------------------
# 150   | Enter number of copies: 150
#       | Cost is 6.50


# first_100_copy_cost = 0.05
# additional_copy_cost = 0.03
# cost = 0.0

# # copies = int(input("Enter number of copies: "))
# copies = 150

# if copies <= 100:
#     cost = copies * first_100_copy_cost
# else:
#     cost = (100 * first_100_copy_cost) + ((copies - 100) * additional_copy_cost)
# print(f"Cost is {cost:.2f}")

# Uploaded:
cost_first_100_copies = 0.05
cost_additional_copies = 0.03
cost_total = 0.0

copies = int(input("Enter number of copies: "))

if copies <= 100:
    cost_total = copies * cost_first_100_copies
else:
    cost_total = (cost_first_100_copies * 100) + ((copies -100) * cost_additional_copies)
    
print(f"Cost is {cost_total:.2f}")