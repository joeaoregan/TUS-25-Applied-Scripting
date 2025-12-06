import re

with open("exam_papers\\2024_25_repeat\\q4_student_id__transfers_log\\transfers.log") as data_file:
    contents = data_file.read()

    faculties = re.findall(r"([A-Za-z ]+) [A-Z]{1,2}\d{6}[0-9A]", contents)

    unique_faculties = list(set(faculties))

    frequencies = {} # reset
    
    for faculty in faculties:
        frequencies[faculty] = frequencies.get(faculty, 0) + 1
    
    # print(frequencies)

    max_faculty = max(frequencies, key=frequencies.get)
    print(f"{max_faculty} had most students: {frequencies[max_faculty]}")