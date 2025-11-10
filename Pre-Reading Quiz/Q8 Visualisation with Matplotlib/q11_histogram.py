import matplotlib.pyplot as plt

values = [10, 20, 50, 70, 90, 50, 30, 20, 10, 150] # create a list for the patients numbers

# Create the figure and axes
fig,ax = plt.subplots()

# histogram
intervals = [30,60,90,120,150]
ax.set(title="Question 11", xlabel="X-Axis", ylabel="Y-Axis",xticks=intervals) # set multiple properties in one go:

# Display a histogram of numbers
ax.hist(values,bins=intervals)

plt.show()