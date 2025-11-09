# Program Name: date_plot.py
# Purpose: To plot the fires per month in Acre, Brazil
# Example of: matplotlib date plot

import datetime

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# create empty lists for the data
x_dates = []
y_fires = []

# date format string
format_str = "%Y-%m-%d"

# read the data from the file
with open("../examples (older)/amazon2_Acre.csv") as datafile:
    # for each line in the file
    for line in datafile:
        # split the line into the components
        year, state, month, fires, date = line.strip().split(",")

        # insert into lists
        # convert date in string format to a datetime object
        x_dates.append(datetime.datetime.strptime(date, format_str)) # convert to datetime object, using the format
        y_fires.append(int(fires)) # number of fires per month for that particular date

# create a figure and an axis object
fig, ax = plt.subplots()

# format the ticks
months = mdates.MonthLocator() # every month
ax.xaxis.set_minor_locator(months)

# set the labels on the axes
ax.set_xlabel("Time")
ax.set_ylabel("Number of Fires per month")

# do a date plot: mpl.dates.date2num converts date objects to matplotlib fofmat

ax.plot_date(mpl.dates.date2num(x_dates), y_fires, marker=",", linestyle="-")
plt.show()

# save the image
fig.savefig('date plots/acre_date_plot.png', bbox_inches='tight')