# A00258304

# A program is determining a message to display based on the percentage of free space. A code block starts with:
# if percent_free == 0:
#     print("Warning: System full")
# Which of the following code blocks is the correct way (in Python!) to then check if percent_free is less than 5?

# a. else if (percent_free < 5)
# b. elif percent_free < 5:
# c. else percent_free < 5:
# d. elif (percent_free < 5)
# e. else if percent_free < 5:

percent_free = 4

if percent_free == 0:
    print("Warning: System full")
elif percent_free < 5:
    print("Less than 5")
