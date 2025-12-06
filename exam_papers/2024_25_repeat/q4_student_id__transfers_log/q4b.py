import re

students_dict = {}

# regex = re.compile(r"([a-zA-Z\s]+) [A-Z]{1,2}[\d]{6}[a-zA-Z\d]{1} (\d+)")
regex = re.compile(r"([A-Z]{1,2}\d{6}[0-9A]) (\d+)") # id, amount
# with open("transfers.log") as data_file:
with open("exam_papers\\2024_25_repeat\\q4_student_id__transfers_log\\transfers.log") as data_file:
    for line in data_file:
        result = re.search(regex, line)

        if result:
            students_dict[result.group(1)] = int(result.group(2))

    student_id = max(students_dict, key=students_dict.get)

    print(f"Student with ID {student_id} had the highest amount transferred {students_dict[student_id]}")
