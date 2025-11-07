data_file = open("D:\\temp\\test.txt")

for line in data_file:
    print(line)
    name,student_id,ai,cdd = line.split(",")
    print(cdd)
    print(type(cdd))
