# Question 16

# A program includes an Axes variable ax representing a visualisation subplot, 
# and a dictionary data that contains key-value pairs representing a name and a number associated with that name. 
# A programmer wants to display the values at the ends of the bars in a vertical bar chart. 
# Given the following for loop code, what's the correct code to display the values at the ends of the bars?

# for index, value in enumerate(data.values()):

import matplotlib.pyplot as plt

data = {"derp": 10, "derp2": 20, "derp3": 50, "derp4": 5} # create a dictionary
fig, ax = plt.subplots() # create a figure and an axis object
# y_pos = list(range(max(data)),10) # set the y positions
y_pos=[10,20,30,40,50]

# ax.set(title="Question 16", yticks=y_pos, yticklabels=data.keys(), ylabel="Y Axis", xlabel="X Axis")
ax.set(title="Question 16", yticks=y_pos, yticklabels=y_pos, ylabel="Y Axis", xlabel="X Axis")

# do a horizontal bar chart
# ax.barh(y_pos,data_by_state.values(), align="center") # center = default
# ax.barh(y_pos, data.values())

for index,value in enumerate(data.values()):
    # a.
    ax.text(index,value,str(value)) # OK

    # b.
    # ax.text(value,index,value) # nothing

    # c.
    # ax.text(index,str(value),value) # completely blank figure

    # d.
    # ax.text(value,index,str(value)) # blank

    # e.
    ax.text(str(value),index,str(value)) # blank

ax.bar(data.keys(),data.values())

plt.show()