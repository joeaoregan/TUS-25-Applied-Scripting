import matplotlib.pyplot as plt

values = [10, 20, 40, 60, 80, 90, 120, 50, 70, 90, 50, 30, 20, 10, 150,10,20,30, 95, 91, 140, 121, 125, 145] # create a list for the patients numbers

# Create the figure and axes
fig,ax = plt.subplots()

# histogram
intervals = [30,60,90,120,150]
ax.set(title="Question 9", xlabel="X-Axis", ylabel="Y-Axis",xticks=intervals) # set multiple properties in one go:

# Display a histogram of numbers
# ax.hist(values,bins=intervals)

# a.
# ax.hist(values) # This????
ax.hist(values,ec="black")

# b.
# ax.hist(values=bins)

# c.
# ax.hist(values=10) # TypeError: Axes.hist() missing 1 required positional argument: 'x'

# d.
# ax.hist(bins=values) # TypeError: Axes.hist() missing 1 required positional argument: 'x'

# e.
# ax.hist(values,bins=[10]) # blank

plt.show()