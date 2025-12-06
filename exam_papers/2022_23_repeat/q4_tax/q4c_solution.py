import re

frequencies = {}

# with open("taxes.txt") as tax_file:
with open("exam_papers\\2022_23_repeat\\q4_tax\\taxes.txt") as tax_file:
    contents = tax_file.read()

    tax_category_list = re.findall(r"[A-Z{2}[0-9]{6}[A-Z] ([1-4][A-B]?) \d+.\d{2}", contents)

    for tax_category in tax_category_list:
        frequencies[tax_category] = frequencies.get(tax_category, 0) + 1

    max_freq = max(frequencies, key=frequencies.get)
    print(f"Tax category with highest frequency: {max_freq}")



