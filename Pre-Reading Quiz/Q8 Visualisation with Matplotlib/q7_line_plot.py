# Question 7

# The variable data_list contains a list of numbers representing data values. 
# Which of the following is the correct code to create a line plot of the values with the axes object ax?

import matplotlib.pyplot as plt

data_list = [12, 5, 0, 0, 21, 87, 533, 2188, 3586, 509, 46, 6] # Set the data

fig, ax = plt.subplots() # Create the figure and axes

fig.suptitle("Question 7: Line Plot")

ax.set(title="Fires per Month in Acre, 2016", xlabel="Time", ylabel="Number of Fires")

# a.
# ax.line(data_list) # AttributeError: 'Axes' object has no attribute 'line'. Did you mean: 'lines'?

# b.
ax.plot(data_list) # This

# c.
# ax.lineplot(data_list) # AttributeError: 'Axes' object has no attribute 'lineplot'

# d.
# ax.plot(data_list.values()) # AttributeError: 'list' object has no attribute 'values'

# d.
# ax.line(data_list.values()) # AttributeError: 'Axes' object has no attribute 'line'. Did you mean: 'lines'?

plt.show() # show the plot
