data_file = open("D:\\temp\\test.txt")

for line in data_file:
    print(line)
    name,student_id,results = line.split(",", maxsplit=2)

    print(name)
    print(student_id)
    print(results)
    print(type(results))
