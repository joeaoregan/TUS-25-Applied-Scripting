#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""



"""
import matplotlib.pyplot as plt
# colours = ["lightgreen", "yellowgreen", "darkgreen"] # replace default colours
colours = ["lightgreen", "green", "darkgreen"] # replace default colours

areas = {"Defending 3rd":2, 'Middle 3rd': 21, "Attacking 3rd": 4}

# create the figure and axis
fig,ax = plt.subplots()

# set a title
ax.set_title("GK Distribution Areas (Total: 27)")

# display the pie chart
# ax.pie(areas.values(), labels=areas.keys(), autopct="%.0f%%") #, colors=colors)
ax.pie(areas.values(), labels=areas.keys(), autopct="%.0f%%", colors=colours)

plt.show()

fig.savefig('figures/piechart_gk_distribution_colours2.png', bbox_inches='tight')
