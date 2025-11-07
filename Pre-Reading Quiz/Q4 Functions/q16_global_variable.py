# A function increment() is defined as follows:
# def increment():
#     global number
#     number += 1

# What is the output of the following code:
# number = 0
# increment()
# print(number)

# a. 2
# b. 1 # Global variables are considered bad practice and should not be used in the Applied Scripting module
# c. 0
# d. Error


def increment():
    global number
    number += 1

number = 0
increment()
print(number) # 1