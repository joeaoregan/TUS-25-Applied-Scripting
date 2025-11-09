# Skewness
# Is a meassure of the asymmetry (lack of symmetry) of distibution of a variable about its mean.
# https://en.wikipedia.org/wiki/Skewness

# Symmetry, or lack of it, can be indicated by a histogram (frequency chart) of the data:

#              |#|                       #
#             #|#|#                    #|#|#
#             #|#|#                    #|#|#|#
#           #|#|#|#|#                #|#|#|#|#|#
#           #|#|#|#|#                #|#|#|#|#|#|# 
#         #|#|#|#|#|#|#            #|#|#|#|#|#|#|#|#
#      |#|#|#|#|#|#|#|#|#          #|#|#|#|#|#|#|#|#|#
#    |#|#|#|#|#|#|#|#|#|#|#      #|#|#|#|#|#|#|#|#|#|#|#
#   #|#|#|#|#|#|#|#|#|#|#|#|#    #|#|#|#|#|#|#|#|#|#|#|#|#|#
#           Symmetric                   Asymmetric

# Perfect symmetry will normally have a zero skewness value
# Asymmetric: more values on one side than the other


# Skewness can be positive, zero, negative, or undefined:
# * Positive skewness -> the values tail off to the right
# * Negative skewness -> the values tail off to the left
# * Perfectly symmetric distribution has zero skewness. (Mean = Median = Mode)


# Mode Skewness
# If the mode is available (e.g. for integer values), then the skewness can be calculated as:
# (mean - mode) / standard deviation

# Median Skewness
# If the mode is not available (e.g. for decimal values), then the skewness can be calculated as:
#  3 (mean - median) / standard deviation

import matplotlib.pyplot as plt
# from statistics_function_1 import calc_median
import sys
sys.path.insert(1, '../examples (older)') # access calc_functons in examples (older) dir
from calc_functions import calc_mean, calc_median, calc_mode, calc_standard_deviation

# create a list for the patients numbers
patients_list = []

# read the data from the file
with open("trolleywatch.csv") as data_file:
    # read the first line containing the headings and discard it
    data_file.readline()

    # for each other line in the file
    for line in data_file:
        # split the line into components
        date_string, hospital, region, trolley, ward, patients = line.strip().split(",")

        # add to the list
        patients_list.append(int(patients))

# Create the figure and axes
fig,ax = plt.subplots()

# histogram
# Set the title
ax.set_title("Trolleywatch Data")

# set the axis labels
ax.set_xlabel("Number of Patients")
ax.set_ylabel("Frequency")

# create a list for the histogram boundaries
bins_list = [ i for i in range(0,max(patients_list)+10,10)] # from zero to the maximum number of the patients list, in tens
# set the ticks on the x-axis
ax.set_xticks(bins_list)
# Display a histogram of the patient numbers
# ax.hist(patients_list)
# ax.hist(patients_list,ec="black") # set the edge colour, highlights where the intervals are
# ax.hist(patients_list,bins=9,ec="black") # change the number of bins to use to 9
ax.hist(patients_list,bins=bins_list,ec="black") # change the number of bins to use to 9

# plt.show()

# fig.savefig('figures/histogram_bins_list_xticks.png', bbox_inches='tight')


# Calculate the skewness
mean = calc_mean(patients_list)
median = calc_median(patients_list)
mode = calc_mode(patients_list)
standard_deviation = calc_standard_deviation(patients_list)
# display using f-string f"{variable=}"
print(f"{mean=}")
print(f"{median=}")
print(f"{mode=}")
print(f"{standard_deviation=}")

# calculate the mode skewness
mode_skewness = (mean - mode) / standard_deviation # skewness shows us how symmetric it is, or the lack of symmetry
median_skewness = 3*(mean - median) / standard_deviation
# print(f"{mode_skewness=}")
# print(f"{median_skewness=}")
print(f"{mode_skewness=:.3f}")
print(f"{median_skewness=:.3f}")

