import re

frequencies = {}

# with open("medical_charges.txt") as data_file:
with open('exam_papers\\2024_25_winter\\q4_nhi__medical_charges\\medical_charges.txt') as data_file:
    contents = data_file.read()

    regions_list = re.findall(r"([A-Z][A-Za-z\s-]+)\n", contents)

    for region in regions_list:
        frequencies[region] = frequencies.get(region, 0) + 1

    max_region = max(frequencies, key=frequencies.get)
    print(f"Region {max_region} had most patients")

    print(frequencies)
    print(max(frequencies.values()))