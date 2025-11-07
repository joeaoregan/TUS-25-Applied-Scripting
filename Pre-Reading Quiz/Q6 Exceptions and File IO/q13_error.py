try:
    with open("D:\\temp\\test.txt"):
        pass

except IsADirectoryError:
    print("This is a directory")