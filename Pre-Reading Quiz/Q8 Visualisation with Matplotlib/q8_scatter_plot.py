# Question 8

# Given an Axes variable ax representing a visualisation subplot, what is the
# correct code to create a scatter plot using the lists x_values and y_values?

import matplotlib.pyplot as plt

# create empty lists for the data
x_values = []
y_values = []

# read the data from the file
with open("../../wk10 visualisation and matplotlib/examples (older)/TOP500_201906.csv") as datafile:    
    _ = datafile.readline() # read the headers line

    # for each line in the file
    for line in datafile:        
        _, _, cores, rmax, _ = line.strip().split(",") # split the line into the components
        
        if int(cores) <= 200000: # put limit to remove outliers, zooms in on busiest part of graph              
            x_values.append(int(cores))
            y_values.append(float(rmax))


fig, ax = plt.subplots() # create a figure and an axis object

ax.set(title="Top 500 Supercomputers", xlabel="Total Cores", ylabel="Rmax (TFlops)") # set title and the labels on the axes

fig.suptitle("Question 8: Scatter Plot")

# do a scatter plot
# ax.scatter(x_values, y_values, marker=".") # smaller dot

# a.
# fig.scatter(x_values, y_values) # AttributeError: 'Figure' object has no attribute 'scatter'

# b.
# ax.scatterplot(x_values, y_values) # AttributeError: 'Axes' object has no attribute 'scatterplot'

# c.
# ax.plot(x_values, y_values) # draws lines

# d.
# fig.plot(x_values, y_values) # AttributeError: 'Figure' object has no attribute 'plot'

# e.
ax.scatter(x_values, y_values) # this

plt.show()