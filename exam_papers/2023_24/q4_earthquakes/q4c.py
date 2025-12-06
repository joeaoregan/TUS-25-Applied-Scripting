import re

regex = re.compile(r"[a-z]{2}[0-9]{4}[0-9a-z]* ([a-zA-Z\s-]+)")
# regex = re.compile(r"([a-zA-Z-\s]+)$")

# with open("earthquakes.log") as data_file:
with open("exam_papers\\2023_24\\q4_earthquakes\\earthquakes.log") as data_file:
    contents = data_file.read()

    locations = re.findall(regex, contents)

    frequencies = {}
    for location in locations:
        location.strip()
        frequencies[location] = frequencies.get(location, 0) + 1

    highest_freq = max(frequencies, key=frequencies.get)

    print(f"Location: {highest_freq} has highest frequency of: {frequencies[highest_freq]}")