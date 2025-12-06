import re

tax_codes = {}

regex = re.compile(r"([A-Z{2}[0-9]{6}[A-Z]) [1-4][A-B]{,1} (\d+.\d{2})")
# regex = re.compile(r"([A-Z{2}[0-9]{6}[A-Z]) [1-4][A-B]? (\d+.\d{2})")

# with open("taxes.txt") as data_file:
with open("exam_papers\\2022_23_repeat\\q4_tax\\taxes.txt") as data_file:
    for line in data_file:
        result = re.search(regex, line)

        tax_codes[result.group(1)] = float(result.group(2))

    print(f"Tax code with the highest amount of Tax Paid: {max(tax_codes, key=tax_codes.get)}")