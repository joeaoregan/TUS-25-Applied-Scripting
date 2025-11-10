# Question 14
# Given an Axes variable ax representing a visualisation subplot, 
# and a dictionary data that contains key-value pairs representing a 
# name and a number associated with that name. What's the correct code 
# to create a horizontal bar chart using this data, with the names as labels?

import matplotlib.pyplot as plt

# create a dictionary
data = {"derp": 10, "derp2": 20, "derp3": 50, "derp4": 5}

# create a figure and an axis object
fig, ax = plt.subplots()

# set the y positions
# y_pos = [ i for i in range(len(data))]
y_pos = list(range(len(data)))

ax.set(title="Question 14", yticks=y_pos, yticklabels=data.keys(), ylabel="Y Axis", xlabel="X Axis")

# do a horizontal bar chart
# ax.barh(y_pos,data_by_state.values(), align="center") # center = default
# ax.barh(y_pos, data.values())

# a.
# ax.barv(data.values()) # AttributeError: 'Axes' object has no attribute 'barv'. Did you mean: 'bar'?

# b.
# ax.barh(data.values(),data.keys()) # Wrong way around

# c.
ax.barh(data.keys(),data.values()) # This

# d.
# ax.bar(data.keys(),data.values()) # vertical

# e.
# ax.bar(data.keys(), data.values()) # same as d?

plt.show()