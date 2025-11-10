import matplotlib.pyplot as plt

data = {"derp": 10, "derp2": 20, "derp3": 50, "derp4": 5}


# create a figure and an axis object
fig, ax = plt.subplots()

# set the title
ax.set_title("Question 12")

# do a pie chart
# ax.pie(data.values(), labels = data.keys(),autopct="%.0f%%") # Specify the percentage to the nearest integer
# ax.pie(data.values(), labels = data.keys())

# a.
ax.pie(data.values(), labels=data.keys(), autopct="%.1f%%") # This

# b.
# ax.pie(data.values(), labels=data.keys(), autopct="%.1f%") # ValueError: incomplete format

# c.
# ax.pie(data.values(), labels=data.keys(), autopct=".1f%") # ValueError: incomplete format

# d.
# ax.pie(data.values(), labels=data.keys(), autopct=".1f%%") # .1f% on all sections, no actual percentage

# e.
# ax.pie(data.values(), labels=data.keys(), autopct=".1f") # .1f on all sections, no actual percentage

plt.show()