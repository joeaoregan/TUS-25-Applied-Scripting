import re

years_freq = {}

with open("cardata.txt") as data_file:
    # Read in the entire contents of the file as a string
    contents = data_file.read()
    # Use a regular expression to find every Year and capture it
    # this returns a list of the Years.
    # re.findall(r"\d{2}-[A-Z]{1,2}-\d{1,6} (\d{4} \d+)", contents)
    years_list = re.findall(r"\d{2}-[A-Z]{1,2}-\d{1,6} (\d{4})", contents) # remove distance
    # years_list = re.findall(r"\d{4}", contents) # pick and 4 digit number, doesn't just find years


    # Store each Year and its frequency in the dictionary
    for year in years_list:
        years_freq[year] = years_freq.get(year,0) + 1
    # Display the Year associated with the highest frequency
    print("Year with most car registrations:", max(years_freq,key=years_freq.get))