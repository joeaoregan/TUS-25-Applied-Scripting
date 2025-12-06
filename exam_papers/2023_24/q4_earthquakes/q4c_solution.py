import re
frequencies = {}

# with open("earthquakes.log") as data_file:
with open("exam_papers\\2023_24\\q4_earthquakes\\earthquakes.log") as data_file:
    contents = data_file.read()

    locations_list = re.findall(r"[a-z]{2}[0-9]{4}[0-9a-z]* ([a-zA-Z-\s]+)", contents)

    for location in locations_list:
        location = location.strip()
        frequencies[location] = frequencies.get(location, 0) + 1

    max_location = max(frequencies, key=frequencies.get)
    print(f"Location with most Earthquakes: {max_location} with {frequencies[max_location]} earthquakes")