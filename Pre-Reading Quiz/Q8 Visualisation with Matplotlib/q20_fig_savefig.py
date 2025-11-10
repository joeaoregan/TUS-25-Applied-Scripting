# Question 20

# Given the variables fig, ax and filename, what is the 
# correct code to save the visualisation(s) in a file?

import matplotlib.pyplot as plt

data_dict = {} # create an empty dictionary for the data

# read the data from the file
with open("../../wk10 visualisation and matplotlib/examples (older)/amazon2.csv") as datafile:
    # for each line in the file
    for line in datafile:        
        _, state, _, fires, _ = line.strip().split(",") # split the line into the relevant components 
        data_dict[state] = int(fires) # insert into the dictionary

fig, ax = plt.subplots() # create figure and an axis objects


ax.set(title="Question 20", ylabel="Number of Fires per month") # set the labels on the axes

ax.boxplot(data_dict.values(),showfliers=False) # show outliers with whiskers
# ax.boxplot(data_dict.values()) # leave out whiskers

plt.show() # display

filename = "question20.png"

# a.
fig.savefig(filename) # This

# b.
# ax.savefig(filename) # AttributeError: 'Axes' object has no attribute 'savefig'

# c.
# fig.save(filename) # AttributeError: 'Figure' object has no attribute 'save'. Did you mean: 'stale'?

# d.
# ax.save(filename) # AttributeError: 'Axes' object has no attribute 'save'. Did you mean: 'stale'?

# e.
# plt.savefig(filename) # creates a blank file