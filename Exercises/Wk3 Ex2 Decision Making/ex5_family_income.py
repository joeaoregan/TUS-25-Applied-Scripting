# A00258304

# # The family income limits for eligibility for a maintenance grant in 2022-2023 are:

# Number of   | Full
# dependent   | maintenance
# children    |
# ------------|--------------
# less than 4 | €40,875
# 4 to 7      | €44,810
# 8 or more   | €48,575

# Write a program which inputs the number of dependants and the family income, 
# and then displays a message indicating whether or not a person is eligible for a full maintenance grant.

# Example:

# Input | Result
#-------|---------------------------------------------------
# 0     | Number of dependents: 0
# 25000 | Input income: 25000
#       | You are eligible for a full maintenance grant
#-------|---------------------------------------------------
# 0     | Number of dependents: 0
# 40876 | Input income: 40876
#       | You are not eligible for a full maintenance grant
#-------|---------------------------------------------------
# 3     | Number of dependents: 3
# 30000 | Input income: 30000
#       | You are eligible for a full maintenance grant
#-------|---------------------------------------------------
# 3     | Number of dependents: 3
# 42000 | Input income: 42000
#       | You are not eligible for a full maintenance grant
#-------|---------------------------------------------------
# 4     | Number of dependents: 4
# 44810 | Input income: 44810
#       | You are eligible for a full maintenance grant
#-------|---------------------------------------------------
# 4     | Number of dependents: 4
# 44811 | Input income: 44811
#       | You are not eligible for a full maintenance grant
#-------|---------------------------------------------------
# 7     | Number of dependents: 7
# 44810 | Input income: 44810 
#       | You are eligible for a full maintenance grant
#-------|---------------------------------------------------
# 8     | Number of dependents: 8
# 46000 | Input income: 46000
#       | You are eligible for a full maintenance grant
#-------|---------------------------------------------------
# 8     | Number of dependents: 8
# 48575 | Input income: 48575
#       | You are eligible for a full maintenance grant
#-------|---------------------------------------------------
# 8     | Number of dependents: 8
# 48576 | Input income: 48576
#       | You are not eligible for a full maintenance grant
#-------|---------------------------------------------------
# 12    | Number of dependents: 12
# 48000 | Input income: 48000
#       | You are eligible for a full maintenance grant
#-------|---------------------------------------------------
# 14    | Number of dependents: 14
# 70000 | Input income: 70000
#       | You are not eligible for a full maintenance grant


# dependents = 8
# income = 46000

# # dependents = int(input("Number of dependents: "))
# # income = int(input("Input income: "))

# message = ""

# if dependents < 4 and income <= 40875:
#     message = "You are eligible for a full maintenance grant"
# elif 4 <= dependents <= 7 and income <= 44810:
#     message = "You are eligible for a full maintenance grant"
# elif dependents >= 8 and income <= 48575:
#     message = "You are eligible for a full maintenance grant"
# else:
#     message = "You are not eligible for a maintenance grant"

# print(message)


# Uploaded:
# A00258304
ELIGIBLE = "You are eligible for a full maintenance grant"
NOT_ELIGIBLE = "You are not eligible for a full maintenance grant"

message = ""

dependents = int(input("Number of dependents: "))
income = int(input("Input income: "))

if dependents < 4 and income <= 40875:
    message = ELIGIBLE
elif 4 <= dependents <= 7 and income <= 44810:
    message = ELIGIBLE
elif dependents >= 8 and income <= 48575:
    message = ELIGIBLE
else:
    message = NOT_ELIGIBLE
    
print(message)