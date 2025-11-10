# Question 19

# Given a Figure object, fig, which of the following is the correct code 
# to create an overall title "Some Visualisations" for a figure fig?

import matplotlib.pyplot as plt

data_dict = {} # create an empty dictionary for the data

# read the data from the file
with open("../examples (older)/amazon2.csv") as datafile:
    # for each line in the file
    for line in datafile:        
        _, state, _, fires, _ = line.strip().split(",") # split the line into the relevant components 
        data_dict[state] = int(fires) # insert into the dictionary

fig, ax = plt.subplots() # create figure and an axis objects


ax.set(title="Question 19", ylabel="Number of Fires per month") # set the labels on the axes

ax.boxplot(data_dict.values(),showfliers=False) # show outliers with whiskers
# ax.boxplot(data_dict.values()) # leave out whiskers

# a.
# fig.subtitle("Some Visualisations") # AttributeError: 'Figure' object has no attribute 'subtitle'. Did you mean: 'suptitle'?

# b.
# fig.title("Some Visualisations") # AttributeError: 'Figure' object has no attribute 'title'

# c.
fig.suptitle("Some Visualisations") # This

# d.
# fig.title = "Some Visualisations" # Opens - shows nothing

# e.
# fig.set_title("Some Visualisations") # AttributeError: 'Figure' object has no attribute 'set_title'. Did you mean: 'suptitle'?

plt.show() # display