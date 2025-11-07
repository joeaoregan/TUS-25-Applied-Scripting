try:
    with open("D:\\temp\\test2.txt"):
        pass

except FileNotFoundError:
    print("file does not exist")