# data_file = "D:\\temp\\test.txt"

# try:
#     with open(data_file, "r"):
#         print("file open")
#     data_file.write("Final Results")
# except Exception as e:
#     print(e)


data_file = open("D:\\temp\\test.txt")
data_file.write("Final Result")