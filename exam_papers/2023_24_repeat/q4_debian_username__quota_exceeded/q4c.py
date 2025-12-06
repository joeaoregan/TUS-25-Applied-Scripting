import re

with open("quota_exceeded.log") as data_file:
    contents = data_file.read()

    faculties = re.findall(r"\d+\d([A-Za-z& ]+)", contents)

    unique_faculties = list(set(faculties))

    # frequencies = {faculty: faculties.count(faculty) for faculty in unique_faculties}

    frequencies = {}
    for faculty in faculties:
        frequencies[faculty] = frequencies.get(faculty, 0) + 1

    print(f"Faculty with most users over the quota: {max(frequencies, key=frequencies.get)}")