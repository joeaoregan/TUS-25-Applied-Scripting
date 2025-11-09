# Histograms
# Display the frequency distribution of numerical data.

# https://en.wikipedia.org/wiki/Histogram


# You neeed to divide the range of values into "bins"
# These are the intervals corresponding to the vertical bars in the histogram.


"""

and calculate the skewness
Example of: Visualisation with matplotlib
(for simplicity, ignoring errors, i.e. no Exception Handling)
"""
import matplotlib.pyplot as plt

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

plt.show()

fig.savefig('figures/histogram_bins_list_xticks.png', bbox_inches='tight')