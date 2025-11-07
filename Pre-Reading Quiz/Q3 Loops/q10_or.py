# Which of the following statements is the correct way to repeat a block of code until 
# the value of total is equal to the value of point or the value of total is equal to 7:
# a. while total == 7 or total == point:
# b. while total != 7 and total != point: # Correct
# c. if total != 7 and total != point:
# d. while total != 7 or total != point:


total = 0
point = 8

while total != point and total != 7:
    print(f"point: {point} total: {total}")
    total += 1
else:
    print("Loop ended")


# while total == 7 or total == point:
# if total != 7 and total != point:
# while total != 7 or total != point: # infinite loop

