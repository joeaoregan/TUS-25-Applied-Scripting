import re

earthquakes_dict = {}

# regex = re.compile(r"([0-9]*\.[0-9]*) ([a-z]{2}[0-9]{4}[0-9a-z]*)")
regex = re.compile(r"(\d(?:\.\d*)?) ([a-z]{2}[0-9]{4}[0-9a-z]*)")

# with open("Earthquakes.log") as data_file:
with open("exam_papers\\2023_24\\q4_earthquakes\\earthquakes.log") as data_file:
    for line in data_file:
        results = re.search(regex, line)

        earthquakes_dict[results.group(2)] = float(results.group(1))

    highest_magnitude = max(earthquakes_dict,key=earthquakes_dict.get)

    print(f"Earthquake: {highest_magnitude} had magnitude of: {earthquakes_dict[highest_magnitude]}")