import re

earthquakes = {}

regex = re.compile(r"(\d(?:\.\d*)?) ([a-z]{2}[0-9]{4}[0-9a-z]*)")

# with open("Earthquakes.log") as data_file:
with open("exam_papers\\2023_24\\q4_earthquakes\\earthquakes.log") as earthquakes_file:
    for line in earthquakes_file:
        results = re.search(regex, line)

        earthquakes[results.group(2)] = float(results.group(1))

    max_earthquake_id = max(earthquakes, key=earthquakes.get)

    print(f"Earthquake ID with the highest magnitude: {max_earthquake_id} with magnitude {earthquakes[max_earthquake_id]}")