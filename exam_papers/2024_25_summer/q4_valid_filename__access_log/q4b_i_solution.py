import re

files_dict = {}
regex = re.compile(r"([\w-]+\.[A-Za-z]{,4}) \d{3} (\d+)")

# with open("access.log") as logfile:
with open("exam_papers\\2024_25_summer\\q4_valid_filename__access_log\\access.log") as data_file:
    for line in data_file:
        result = re.search(regex, line)

        if result:
            files_dict[result.group(1)] = float(result.group(2))

filename = max(files_dict, key=files_dict.get)
print(f"Filename {filename} had the highest amount transferred {files_dict[filename]} (bytes)")