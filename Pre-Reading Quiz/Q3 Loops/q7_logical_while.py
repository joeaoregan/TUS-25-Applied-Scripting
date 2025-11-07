# The variable play_again stores a boolean value (True or False). The program needs to repeat a block of code as long as the value of play_again is True

#  Which of the following statements is not logically correct for this purpose?
# a. while not play_again == False:
# b. while not play_again: # Correct
# c. while play_again == True:
# d. while play_again:

play_again = True
counter = 0

# while not play_again == False:
#     print("In the loop 1: ", counter)
#     counter += 1
#     if counter >= 3:
#         play_again = False

while not play_again:
    print("In the loop 2: ", counter)
    counter += 1
    if counter >= 3:
        play_again = False
else:
    print("Loop ended")

# while play_again == True:
#     print("In the loop 3: ", counter)
#     counter += 1
#     if counter >= 3:
#         play_again = False
# counter = 0

# while play_again:
#     print("In the loop 4: ", counter)
#     counter += 1
#     if counter >= 3:
#         play_again = False
# counter = 0