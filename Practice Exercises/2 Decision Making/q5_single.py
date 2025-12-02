age = int(input("Enter your age: "))
status = input("Enter your marital status: ")

if age < 18 or status != "single":
    print("You are not suitable for the TV show")
else:
    print("You are suitable for the TV show")