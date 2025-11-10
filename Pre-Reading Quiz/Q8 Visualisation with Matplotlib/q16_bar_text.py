# Question 15

# A program includes an Axes variable ax representing a visualisation subplot, 
# and a dictionary data that contains key-value pairs representing a name and a number associated with that name. 
# A programmer wants to display the values at the ends of the bars in a horizontal bar chart. Given the following for loop code, 
# what's the correct code to display the values at the ends of the bars?

# for index, value in enumerate(data.values()):

import matplotlib.pyplot as plt

data = {"derp": 10, "derp2": 20, "derp3": 50, "derp4": 5} # create a dictionary
fig, ax = plt.subplots() # create a figure and an axis object
y_pos = list(range(len(data))) # set the y positions

ax.set(title="Question 15", yticks=y_pos, yticklabels=data.keys(), ylabel="Y Axis", xlabel="X Axis")

# do a horizontal bar chart
# ax.barh(y_pos,data_by_state.values(), align="center") # center = default
# ax.barh(y_pos, data.values())

for index,value in enumerate(data.values()):
    # a.
    # ax.text(str(value),index,str(value)) # blank chart

    # b.
    ax.text(value,index,str(value)) # This

    # c.
    # ax.text(index,value, str(value)) # nothing showing up

    # d.
    # ax.text(value,index,value) # This works without str() cast

    # e.
    # ax.text(index,str(value),value) # nothing

ax.barh(data.keys(),data.values())

plt.show()