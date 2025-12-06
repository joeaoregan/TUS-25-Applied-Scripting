import re

frequencies = {}
regex = re.compile(r"[A-Z{2}[0-9]{6}[A-Z] ([1-4][A-B]{,1})")

# with open("taxes.txt") as data_file:
with open("exam_papers\\2022_23_repeat\\q4_tax\\taxes.txt") as data_file:
    contents = data_file.read()

    tax_list = re.findall(regex, contents)

    for category in tax_list:
        frequencies[category] = frequencies.get(category, 0) + 1

    max_freq = max(frequencies, key=frequencies.get)
    print(f"Highest frequency: {max_freq} with: {frequencies[max_freq]}")



