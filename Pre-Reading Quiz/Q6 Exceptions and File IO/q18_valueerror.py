data_file = open("D:\\temp\\test.txt")

for line in data_file:
    print(line)
    name,student_id,ai = line.split(",") # ValueError: too many values to unpack (expected 3)
