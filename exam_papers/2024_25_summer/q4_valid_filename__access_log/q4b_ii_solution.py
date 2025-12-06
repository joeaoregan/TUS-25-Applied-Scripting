import re

frequencies = {}

with open("exam_papers\\2024_25_summer\\q4_valid_filename__access_log\\access.log") as data_file:
    contents = data_file.read()

    status_codes_list = re.findall(r"[\w-]+\.[A-Za-z]{,4} (\d{3})", contents)

    for status_code in status_codes_list:
        frequencies[status_code] = frequencies.get(status_code, 0) + 1
  
print("Code Frequency")
for status_code in sorted(frequencies):
    print(f"{str(status_code):6} {frequencies[status_code]:>6}")