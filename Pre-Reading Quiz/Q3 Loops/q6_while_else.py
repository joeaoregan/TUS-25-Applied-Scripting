# What is the effect of an else attached to a while loop block, e.g.
loop = True
counter = 0

while counter < 5:
    # do something
    print("In the loop")
    counter += 1
    # if counter == 4: break
else:
    # do something else
    print("Loop ended")